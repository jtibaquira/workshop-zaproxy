#!/usr/bin/env python
import time
import json
from pprint import pprint
from zapv2 import ZAPv2
from datetime import datetime
import csv
import re

#define alerts count
total_alert_count = 0
total_alert_high_count = 0

#define threads per host
threadsperHost = 10
hostperScan =5

# start scan
start = time.time()

# Opening JSON file
f = open('config.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)
apiKey= data["zapaikey"]
f.close()


#getting target list
def getting_targets():
    tf = open('targets.txt','r')
    lines = tf.readlines()
    targets = []
    # Strips the newline character
    for line in lines:
        targets.append(line.rstrip('\n'))
    tf.close()
    return targets

zap = ZAPv2(apikey=apiKey)


# clean alerts before scanning.

pprint('Deleted all Previous Alerts -> ' +
        zap.core.delete_all_alerts())
pprint('Enable all passive scanners -> ' +
        zap.pscan.enable_all_scanners())
pprint('Set Up Thread Per Host -> ' +
        zap.ascan.set_option_thread_per_host(integer=threadsperHost))
pprint('Set Up Host Per Scan -> ' +
        zap.ascan.set_option_host_per_scan(integer=hostperScan))


targets = getting_targets()

alertsPerScan ={}

reportcsvHeader = ['Alert','AlertID','AlertUrl']

report = open('scan_report.csv','w')

writer = csv.writer(report)

# write the header
writer.writerow(reportcsvHeader)

for i in range(len(targets)):
    print(targets[i])
    target = targets[i]
    print('Spidering target {}'.format(target))
    # The scan returns a scan id to support concurrent scanning
    scanID = zap.spider.scan(target)
    while int(zap.spider.status(scanID)) < 100:
        # Poll the status until it completes
        print('Spider progress %: {}'.format(zap.spider.status(scanID)))
        time.sleep(60)
    print('Spider has completed!')
    print('Active Scanning target {}'.format(target))
    scanID = zap.ascan.scan(target)
    print('Active Scanning ScanID {}'.format(scanID))
    while int(zap.ascan.status(scanID)) < 100:
        # Loop until the scanner has finished
        print('Active Scan progress %: {}'.format(zap.ascan.status(scanID)))
        time.sleep(60)
    print('Active Scan completed')
    #Print vulnerabilities found by the scanning
    print('Hosts: {}'.format(', '.join(zap.core.hosts)))
    print('# Alerts by Active Scanning: ')
    pprint(zap.core.number_of_alerts(baseurl=target))

    st = 0
    pg = 5000
    alert_dict = {}
    alert_count = 0
    alert_high_count = 0
    alerts = zap.alert.alerts(baseurl=target, start=st, count=pg)
    blacklist = [1,2]
    while len(alerts) > 0:
        print('Reading ' + str(pg) + ' alerts from ' + str(st))
        alert_count += len(alerts)
        for alert in alerts:
            alertName = alert.get('alert')
            alertRef = alert.get('alertRef')
            alertUrl = alert.get('url')
            alertsPerScan =[alertName,alertRef,alertUrl]
            writer.writerow(alertsPerScan)
            print('Alert:'+alertName+' AlertID: '+alertRef+" Url: "+alertUrl+"\n")
        st += pg
        alerts = zap.alert.alerts(start=st, count=pg)
report.close()
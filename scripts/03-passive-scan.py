#!/usr/bin/env python
import time
from pprint import pprint
from zapv2 import ZAPv2

apiKey = 'zap-api-1337'
target = 'https://public-firing-range.appspot.com'
zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'})

# TODO : explore the app (Spider, etc) before using the Passive Scan API, Refer the explore section for details
while int(zap.pscan.records_to_scan) > 0:
    # Loop until the passive scan has finished
    print('Records to passive scan : ' + zap.pscan.records_to_scan)
    time.sleep(2)

print('Passive Scan completed')

# Print Passive scan results/alerts
print('Hosts: {}'.format(', '.join(zap.core.hosts)))
print('Alerts: ')
pprint(zap.core.alerts())
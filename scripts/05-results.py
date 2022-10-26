#!/usr/bin/env python
from zapv2 import ZAPv2

# The URL of the application to be tested
target = 'https://public-firing-range.appspot.com'
# Change to match the API key set in ZAP, or use None if the API key is disabled
apiKey = 'zap-apikey-1337'

# By default ZAP API client will connect to port 8080
zap = ZAPv2(apikey=apiKey)
# Use the line below if ZAP is not listening on port 8080, for example, if listening on port 8090
# zap = ZAPv2(apikey=apiKey, proxies={'http': 'http://127.0.0.1:8090', 'https': 'http://127.0.0.1:8090'})

# TODO: Check if the scanning has completed

# Retrieve the alerts using paging in case there are lots of them
st = 0
pg = 5000
alert_dict = {}
alert_count = 0
alerts = zap.alert.alerts(baseurl=target, start=st, count=pg)
blacklist = [1,2]
while len(alerts) > 0:
    print('Reading ' + str(pg) + ' alerts from ' + str(st))
    alert_count += len(alerts)
    for alert in alerts:
        plugin_id = alert.get('pluginId')
        if plugin_id in blacklist:
            continue
        if alert.get('risk') == 'High':
            # Trigger any relevant postprocessing
            continue
        if alert.get('risk') == 'Informational':
            # Ignore all info alerts - some of them may have been downgraded by security annotations
            continue
    st += pg
    alerts = zap.alert.alerts(start=st, count=pg)
print('Total number of alerts: ' + str(alert_count))

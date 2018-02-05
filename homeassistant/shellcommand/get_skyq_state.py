import requests
import json
import sys

r = requests.get('http://192.168.10.143:9006/as/system/information')
resp = json.loads(r.text)

#If is activeStandby means off else is on
if resp['activeStandby']:
   print 'off'
else:
   print 'on'

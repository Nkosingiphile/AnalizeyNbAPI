import requests
import json
import time
from json import dumps
import xmltodict

headers = {
    'content-type': 'application/json'
}

address = 'http://10.13.56.195/'
session = requests.Session()
session.auth = ('vodacom', 'Vodacom01')

response = requests.get(address + 'nbapi/alarms/system', headers=headers, auth=('vodacom', 'Vodacom01'))

print(response.text)
#print(dumps(parker.data(fromstring(response.text), preserve_root=True), indent=4, sort_keys=True))
resp = xmltodict.parse(response.text)
print(resp)
resp_dict = resp['SystemAlarmResponse']['SystemAlarm']
print(len(resp_dict))

print("Creation date         Device Ip Addrr     Device Name         Reason                Severity")
for x in range(len(resp_dict)):
    creation_date = resp['SystemAlarmResponse']['SystemAlarm'][x]['@creationDate']
    device_ip = resp['SystemAlarmResponse']['SystemAlarm'][x]['@deviceIpAddress']
    device_name = resp['SystemAlarmResponse']['SystemAlarm'][x]['@deviceName']
    reason = resp['SystemAlarmResponse']['SystemAlarm'][x]['@reason']
    severity = resp['SystemAlarmResponse']['SystemAlarm'][x]['@severity']
    print(creation_date + '\t' + device_ip + '\t' + device_name + '\t\t' + reason + '\t' + severity)


if response.status_code == 200:
   #print("Successful %s" % (get_system_alarms.content))
   print("Succesfull")
else:
   #print("Not successful %s" % (get_system_alarms.content))
   print("Not successful")
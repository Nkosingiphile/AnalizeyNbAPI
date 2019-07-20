import requests
import time
import json



headers = {
    'content-type': 'application/json'
}


with open('pps.csv') as f:
    pps = f.read().splitlines()
    print(pps)
fixed = []
for Session in pps:
    IP = Session.split(',')
    PPS_BE = '{"payloadsize" : "100", "pps" : "10.00", "type": "UDP"}'
    PPS_EF = '{"payloadsize" : "100", "pps" : "20.00", "type": "UDP"}'

    #BE session stream
    Stream_BE = requests.put('http://10.132.98.167/nbapi/session/%s_BE/stream' % (IP[0].strip()), data=PPS_BE,headers=headers, auth=('vodacom', 'vodacom'))
    # BE session stream
    Stream_EF = requests.put('http://10.132.98.167/nbapi/session/%s_BE/stream' % (IP[0].strip()), data=PPS_EF,headers=headers, auth=('vodacom', 'vodacom'))

    print(Stream_EF.text)
    print("====================================================================")
    print("Status code: " + str(Stream_EF.status_code))
    print("====================================================================")

    if Stream_EF.status_code == 200:
        # print("Successful %s" % (get_system_alarms.content))
        print("Succesfull")
    else:
        # print("Not successful %s" % (get_system_alarms.content))
        print("Not successful")






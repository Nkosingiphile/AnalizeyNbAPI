import requests
import time
import json



headers = {
    'content-type': 'application/json'
}

#Opening CSV with new IP
with open('IP.csv') as f:
    New_IP = f.read().splitlines()
    print(New_IP)
fixed = []
for Session in New_IP:
    IP = Session.split(',')
    #print(IP)
    data_stop = '{"action" : "stop"}'
    terminate = '{"action" : "terminate"}'
    change_endpoint_ip = '{"ip" : "%s"}' % (IP[1].strip())
    endpoint_twamp_cp = '{"address" : "%s", "legacyMode" : "1", "port": "862","tos": "0","vprio": "0"}' % (IP[1].strip())
    start_session = '{"action" : "start"}'
    resolve_endpoint = '{"action" : "resolve"}'

    #stop session_BE
    stop_session = requests.put('http://10.132.98.167/nbapi/session/%s_BE/operate' % (IP[0].strip()), data=data_stop,headers=headers, auth=('vodacom', 'vodacom'))
    # terminate session_BE
    terminate_session = requests.put('http://10.132.98.167/nbapi/session/%s_BE/operate' % (IP[0].strip()),data=terminate, headers=headers, auth=('vodacom', 'vodacom'))
    time.sleep(1)
    # stop session_EF
    stop_session = requests.put('http://10.132.98.167/nbapi/session/%s_EF/operate' % (IP[0].strip()), data=data_stop,headers=headers, auth=('vodacom', 'vodacom'))
    # terminate session_EF
    terminate_session = requests.put('http://10.132.98.167/nbapi/session/%s_EF/operate' % (IP[0].strip()),data=terminate, headers=headers, auth=('vodacom', 'vodacom'))
    time.sleep(1)
    # terminate endpoint
    terminate_endpoint = requests.put('http://10.132.98.167/nbapi/endpoint/%s/operate' % (IP[0].strip()),data=terminate, headers=headers, auth=('vodacom', 'vodacom'))
    time.sleep(3)
    #Change enpoint

    change_ip = requests.put('http://10.132.98.167/nbapi/endpoint/reflector/%s/address' % (IP[0].strip()),data=change_endpoint_ip, headers=headers, auth=('vodacom', 'vodacom'))
    time.sleep(3)
    #change Fullcontrol
    change_endpoint_full_twamp = requests.put('http://10.132.98.167/nbapi/endpoint/reflector/%s/twampcp' % (IP[0].strip()),data=endpoint_twamp_cp, headers=headers, auth=('vodacom', 'vodacom'))
    time.sleep(3)

    #start BE session
    start_session = requests.put('http://10.132.98.167/nbapi/session/%s_BE/operate' % (IP[0].strip()), data=start_session,headers=headers, auth=('vodacom', 'vodacom'))
    time.sleep(3)
    #start EF Session
    start_session = requests.put('http://10.132.98.167/nbapi/session/%s_EF/operate' % (IP[0].strip()), data=start_session,headers=headers, auth=('vodacom', 'vodacom'))
    time.sleep(3)
    #Resolve endpoint
    start_endpoint = requests.put('http://10.132.98.167/nbapi/endpoint/%s/operate' % (IP[0].strip()),data=resolve_endpoint, headers=headers, auth=('vodacom', 'vodacom'))

    print(change_endpoint_full_twamp.text)
    print("====================================================================")
    print("Status code: " + str(change_endpoint_full_twamp.status_code))
    print("====================================================================")

    if change_endpoint_full_twamp.status_code == 200:
        # print("Successful %s" % (get_system_alarms.content))
        print("Succesfull")
    else:
        # print("Not successful %s" % (get_system_alarms.content))
        print("Not successful")








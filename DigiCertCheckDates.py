#!/usr/bin/python3
import requests
import json
import csv
#DigiCert API base URL
URL = "https://www.digicert.com/services/v2/order/certificate"
#Open key file:
f = open('key.txt', 'r')
#API connection informaion dict
CONN_INFO = {} 
#strip the newline char from the key
API_KEY = f.read().rstrip('\r|\n') 

headers = {
          'X-DC-DEVKEY': API_KEY,
          'Content-Type': "application/json"
     }
#Build a request- Receive a responese
#response = requests.request("GET", URL, headers=headers)
response = requests.get(URL, headers=headers)
response_json_dict = json.loads(response.text)
fw = open('digicert_table.json', 'w')
#print(next(i: response_json_dict))
orders_list = response_json_dict['orders']
cert_file = open('DoT_Digicert.csv', 'w')
for i in orders_list:
    for j in i:
        if j == 'certificate':
#            print(i[j]) 
            cert_dict = i[j]
            print(cert_dict['valid_till'])
            cert_file.write("%s, %s\n"%(j,i[j]))

import requests
import json
import time
import datetime
from datetime import date
import sys
from datetime import timezone
import mysql.connector as mysql


db = mysql.connect(
    host = "10.13.56.190",
    user = "willcom",
    password = "w1llc0m",
    database = "SevOne_info"
    )
	
cursor = db.cursor()
	
query = '''INSERT INTO SevOne_Object (Device_ID, Device_Name, Object_ID, Object_Name, Indicactor_ID, Indicactor_Name) VALUES (%s, %s, %s, %s, %s, %s)'''
values = ( 4, 'LIM', 77496, 'TX-TX_Groblersdal-8660-2_TO_Burgersfort_POC3_BE_93273', 2285984, 'P2R Lost Percentage') 
cursor.execute(query, values)

db.commit()

query = '''SELECT * FROM SevOne_Object'''
cursor.execute(query)
records = cursor.fetchall()

for record in records:
    print(record)
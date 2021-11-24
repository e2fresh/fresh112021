import sqlite3
import numpy as np
from datetime import datetime, timezone
from influxdb import InfluxDBClient as IDBC
import time
import json
from config import devices
from config import db
from config import groups
import save
from mgmtJSON import mgmtJSON
t=int(time.time())
try: 
    mensajes = json.loads(open('/home/pi/fresh/Data/DATA.json').read())
    client = IDBC(db[0]['broker'], 8086, 'admin', 'e2IOT2020#.', db[0]['db'])
    data=dict()
    data['measurement']=db[0]['measurement']
    data['fields']=dict()
    data['time']=str(datetime.utcfromtimestamp((t)).isoformat())+'Z'
    for z in range(0,len(groups)):                               
      keys=list(mensajes[groups[z]['name']].keys())        
      for i in range(0,len(keys)):
          if(type(mensajes[groups[z]['name']][keys[i]])==int):   	
              data['fields'][keys[i]]=float(mensajes[groups[z]['name']][keys[i]])
          else:
              data['fields'][keys[i]]=mensajes[groups[z]['name']][keys[i]]
    print(data)
    a=client.write_points([data])
    print(a)
except Exception as e:     
    save.main()
    print(e)
fileJSON = mgmtJSON()
fileJSON.writeJSON('/home/pi/fresh/Data/DATA2.json', data)
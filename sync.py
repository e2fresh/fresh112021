import sqlite3
import numpy as np
from datetime import datetime, timezone
from influxdb import InfluxDBClient as IDBC
import time
from config import devices
from config import db

client = IDBC(db[0]['broker'], 8086, 'admin', 'e2IOT2020#.', db[0]['db'])
connection = sqlite3.connect("backup.sqlite")
cursor = connection.cursor()
rows = cursor.execute("SELECT name from sqlite_master where type= 'table'").fetchall()
n=[]#tablas
k=[]#columnas de las tablas
conn=0
try:
  query = 'select last(*) from \"'+ db[0]['measurement'] +'\" '+';'
  ResultSet = client.query(query)
  conn=1
except Exception as e:
  print(e)
  conn=0
if(conn==1):  
  for i in range(0,len(rows)):
    n.append(rows[i][0])  
  
  for i in range(0,len(n)):
    k=[]
    d=[]
    x=cursor.execute("SELECT * from "+n[i]).description
    for j in range(0,len(x)):
      k.append(x[j][0])
    w=cursor.execute("SELECT * from "+ n[i] ).fetchall()
    if(len(w)!=0):
      for r in range(0,len(w)):
        #print(r)
        a=False
        p=dict()
        p['measurement']=db[0]['measurement']
        p['fields']=dict()
        p['time']=str(datetime.utcfromtimestamp((w[r][k.index('_timestamp')]) /1000.0).isoformat())+'Z'
        for q in range(0,len(k)):
          if(type(w[r][q])==int):
            p['fields'][k[q]]=float(w[r][q])
          else:
            p['fields'][k[q]]=w[r][q]
        try: 
          a=client.write_points([p])
          print(a)
          d.append(p['fields']['_timestamp'])
        except Exception as e:
          print(e)
          continue        
        time.sleep(0.1)          
    else:
      print('no data')
    for h in range(0,len(d)):
      w=cursor.execute("DELETE FROM "+ n[i] + " WHERE _timestamp = " + str(d[h])).fetchall()
      
connection.commit()
cursor.close()      

#w=cursor.execute("DELETE FROM "+ n[i] + " WHERE data_timestamp = \'"+ str(p['fields']['data_timestamp'])+"\'").fetchall()

    
   
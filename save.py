import sqlite3
import numpy as np
from datetime import datetime, timezone
from influxdb import InfluxDBClient as IDBC
import time
import json

def crear_tablas(t,tablas,connection,mensajes):
  tablas2=[]
  tipo=[]
  columna=[]
  for i in range(0,len(tablas)):
    try:
      t.index(tablas[i])

    except:
      tablas2.append(tablas[i])
  for i in range(0,len(tablas2)):
    
    w=mensajes[tablas2[i]].keys()    
    columna.append(list(w))
  for i in range(0,len(tablas2)):
    query="CREATE TABLE "
    query=query+tablas2[i] +'('
    y=[]
    for j in range(0,len(columna[i])):
      x=mensajes[tablas2[i]][columna[i][j]]
      if type(x)==str:
        y.append('DATETIME')
      else:
        y.append('FLOAT')
    tipo.append(y)

    for j in range(0,len(columna[i])): 
      if(j==len(columna[i])-1):
        query=query+ columna[i][j]+' '+tipo[i][j] + ')'
      else:
        query=query+ columna[i][j]+' '+tipo[i][j] + ','
  
    print(query)
    cursorObj = connection.cursor()
    cursorObj.execute(query)
    connection.commit()
  
def llenarDB(tablas,mensajes,connection):  
  columna=[]
  datos=[]
  for i in tablas:
    columna.append(list(mensajes[i].keys()))
  for i in range(0,len(tablas)):
    query="INSERT INTO "
    query=query+tablas[i] +'('
    
    y=tuple()
    query2=') VALUES ('
    for j in range(0,len(columna[i])):
      x=mensajes[tablas[i]][columna[i][j]]
      if j==len(columna[i])-1:
        query=query+columna[i][j]+''
        query2=query2+'? );'
      else:
        query=query+columna[i][j]+','
        query2=query2+'?,'
      y=y+(x,)
    datos.append(y)
    query =query + query2

    #print(query)
   #print(y)
    cursorObj = connection.cursor()
    cursorObj.execute(query,y)
    connection.commit()
def main(): 
  connection = sqlite3.connect("backup.sqlite")
  mensajes = json.loads(open('/home/pi/fresh/Data/DATA.json').read())
  tablas=list(mensajes.keys())
  n=[]   
  cursor = connection.cursor()
  rows = cursor.execute("SELECT name from sqlite_master where type= 'table'").fetchall()
  for i in range(0,len(rows)):
    n.append(rows[i][0])
  crear_tablas(n,tablas,connection,mensajes)
  llenarDB(tablas,mensajes,connection)
  connection.close()
  print('done')
  

  
  
  
import time
from datetime import datetime, timezone
import struct
import requests
import math
from config import devices
from config import groups
from mgmtJSON import mgmtJSON

#def main():
payload = dict()
payload2 = dict()
for group in groups:
  payload[group['name']] = dict()
  payload2[group['name']] = dict()
for device in devices:
  try: 
    instrument = device['protocol'](device)
    payload = instrument.get_data(payload, level=device['level'])
    x=list(payload[device['group']][device['name']].keys())
    for i in range(0,len(x)):
      payload2[device['group']][device['name']+'___'+x[i]]= payload[device['group']][device['name']][x[i]]
    payload2[device['group']]['_timestamp']=((int(time.time()))*1000)
    payload2[device['group']]['data_timestamp']= str(datetime.now())
    print(payload2)
  except Exception as e:
    print(e)
    print("Error de comunucación\n")
    continue
fileJSON = mgmtJSON()
fileJSON.writeJSON('/home/pi/fresh/Data/DATA.json', payload2)
        
'''if __name__ == "__main__":
  
    x=True
    while x==True: 
        segundo = datetime.now().second
        if segundo ==0:
            main()
            time.sleep(1)
            x=False'''
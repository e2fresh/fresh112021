import serial, time
import json
class Serial:
    def __init__(self, device):
        self.device = device

    def get_data(self, payload, level = 0):
        try:
          j=-1
          for i in range(0,5):
            try:
              arduino = serial.Serial('/dev/ttyUSB'+str(i), 115200 , timeout=5)
              time.sleep(0.5)
              arduino.write(b'1')
              time.sleep(0.1)
              rawString = arduino.readline()
              if(rawString.decode("utf-8")!=''):
                j=i
              else:
                continue    
              arduino.close()
            except Exception as e:
              continue 
          arduino = serial.Serial('/dev/ttyUSB'+str(j), 115200)
          time.sleep(0.5)
          arduino.write(b'1')
          time.sleep(0.1)
          rawString = arduino.readline()
          x=rawString.decode("utf-8")
          data=json.loads(str(x))
          #print(rawString.decode("utf-8"), end='')
          arduino.close()
            
          payload[self.device['group']][self.device['name']] = dict()
          for k,v in data[self.device['address']].items():
            payload[self.device['group']][self.device['name']][k.upper()] = v
          payload[self.device['group']][self.device['name']]['ESTADO'] = 1
        except Exception as e:    
          print(e)
          print("Error con la comunicación del NodeMCU\n")
          payload[self.device['group']][self.device['name']]['ESTADO'] = 0
        print("Variables leidas...")  
        return payload
import time
import pymodbus
from pymodbus.pdu import ModbusRequest
from pymodbus.client.sync import ModbusSerialClient as ModbusClient
from pymodbus.transaction import ModbusRtuFramer
from calculo_tot2 import energiaTot as energia
import math
import struct
#prueba123
class modbusRTU:
    def __init__(self, device):         
        self.device=device     
        self.type=device['type']
        for i in range(0,2):        
            try:          
                self.address = device['address']
                self.client = ModbusClient(method = 'rtu',port = '/dev/ttyUSB'+str(i), baudrate = device['baud'], parity = device['parity'], timeout=1)
                x=self.client.read_holding_registers(device['type'][0]['register'],1,unit=self.address).registers[0]
                device['port']='/dev/ttyUSB'+str(i)          
                print(device['port'])
                print(x)
            except Exception as e:
                print(e)
                continue      
        self.address = device['address']
        self.client = ModbusClient(method = 'rtu', port = device['port'], baudrate = device['baud'], parity = device['parity'], timeout=1)

    def get_data(self, payload, level=0 ):
      payload[self.device['group']][self.device['name']] = dict()
      try:
        for i in range(0,len(self.type)): 
          var = []
          addr = self.type[i]['register']
          regs_num =  self.type[i]['registers_number']
          connection = self.client.connect()
          for l in range(0,10):
            try:
              if self.type[i]['type'] == "int" and (self.type[i]['level']<=0):

                if(regs_num>1):

                  a=self.client.read_holding_registers(addr,regs_num,unit=self.address).registers[0].to_bytes(2, 'big')
                  b=self.client.read_holding_registers(addr,regs_num,unit=self.address).registers[1].to_bytes(2, 'big')
                  payload[self.device['group']][self.device['name']][self.type[i]['name']]=int.from_bytes(a+b, "big")
                  time.sleep(0.1)   

                else:

                  payload[self.device['group']][self.device['name']][self.type[i]['name']]=(self.client.read_holding_registers(addr,regs_num,unit=self.address).registers[0])
                  time.sleep(0.1)

              if self.type[i]['type'] == "float":
                  a=self.client.read_holding_registers(addr,regs_num,unit=self.address).registers[0].to_bytes(2, 'little')
                  b=self.client.read_holding_registers(addr,regs_num,unit=self.address).registers[1].to_bytes(2, 'little')
                  payload[self.device['group']][self.device['name']][self.type[i]['name']]=struct.unpack('f', b+a)[0]
                  time.sleep(0.1) 
            except:
              continue
        print(payload)       
        if self.device['device_name']=='heyi':
            DPQ = (int(payload[self.device['group']][self.device['name']]['DPQ']) >> 8) & 0xff
            active_PW = ((payload[self.device['group']][self.device['name']]['P'] / 10000) * (math.pow(10,DPQ)))/1000
            payload[self.device['group']][self.device['name']]['P'] = active_PW
            payload[self.device['group']][self.device['name']]['E'] = payload[self.device['group']][self.device['name']]['E']/1000
            reactive_PW = ((payload[self.device['group']][self.device['name']]['Q'] / 10000) * (math.pow(10,DPQ)))/1000            
            payload[self.device['group']][self.device['name']]['Q'] = reactive_PW            
            reactive_energy = (payload[self.device['group']][self.device['name']]['EQ'])/1000
            payload[self.device['group']][self.device['name']]['EQ'] = reactive_energy
            EH, ED, EM = energia().totalizar(payload[self.device['group']][self.device['name']]['E'], self.device)           
            payload[self.device['group']][self.device['name']]['EH'] = EH
            payload[self.device['group']][self.device['name']]['ED'] = ED
            payload[self.device['group']][self.device['name']]['EM'] = EM
            payload[self.device['group']][self.device['name']]['ESTADO'] = 1
            del payload[self.device['group']][self.device['name']]['DPQ'] 
        if self.device['device_name']=='heyi_md':    
            pot=(payload[self.device['group']][self.device['name']]['VAB']/10)*1.73*0.92*(payload[self.device['group']][self.device['name']]['E']['IA']/100)
            payload[self.device['group']][self.device['name']]['P'] = pot/1000
            EH, ED, EM = energia().totalizar(payload[self.device['group']][self.device['name']]['E'], self.device)           
            payload[self.device['group']][self.device['name']]['EH'] = EH
            payload[self.device['group']][self.device['name']]['ED'] = ED
            payload[self.device['group']][self.device['name']]['EM'] = EM
            payload[self.device['group']][self.device['name']]['ESTADO'] = 1
      except Exception as e:
        print(e)
        del payload[self.device['group']][self.device['name']]
        payload[self.device['group']][self.device['name']] = dict()
        payload[self.device['group']][self.device['name']]['ESTADO'] = 0
        
      return payload

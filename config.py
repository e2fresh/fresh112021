from ModbusAddress import heyi as heyi
from modbus import modbusRTU as RTU
from JSON import JSONnode as node
from JSON import JSONrpi as rpi
from Serial import Serial as Serial 



devices = [
    {'type': heyi, 'device_name':'heyi' ,'level': 0, 'protocol': RTU, 'port': '/dev/ttyUSB0', 'address': 1, 'baud': 9600, 'parity': 'E', 'name': 'RACK___CONS', 'group': 'RACK'},
    {'type': heyi, 'device_name':'heyi' ,'level': 0, 'protocol': RTU, 'port': '/dev/ttyUSB0', 'address': 2, 'baud': 9600, 'parity': 'E', 'name': 'RACK___CONG', 'group': 'RACK'},
    {'type': 'node','device_name':'node' , 'level': 0, 'protocol': node, 'port': 'http://192.168.0.10/data', 'address': 'DATA', 'baud': 0, 'parity': 'NONE', 'name': 'RACK___', 'group': 'RACK'}
]

groups = [    
    {'name': 'RACK', 'type': 'RACK'}
]

db = [
    {'measurement': "STO043", 'broker': "monitor2.e2fresh.com", 'db':"e2fresh_Olimpica"}    
]
import requests

class JSONnode:

    def __init__(self, device):
        self.device = device

    def get_data(self, payload, level = 0):
        try:
            payload[self.device['group']][self.device['name']] = dict()
            req = requests.get(url = self.device['port'], timeout=3)
            data = req.json()
            for k,v in data[self.device['address']].items():
                payload[self.device['group']][self.device['name']][k.upper()] = v
            payload[self.device['group']][self.device['name']]['ESTADO'] = 1
            print("leido...")  
        except:
            print("Error con la comunicación del NodeMCU\n")
            payload[self.device['group']][self.device['name']]['ESTADO'] = 0 
        return payload

class JSONrpi:

    def __init__(self, device):
        self.device = device
    
    def get_data(self, payload, level = 0):
        try:
            req = requests.get(url = self.device['port'])
            data = req.json()
            print(data)
            payload[self.device['group']][self.device['name']] = dict()
            payload[self.device['group']][self.device['name']]['ESTADO'] = 1
            for k,v in data[self.device['address']]['event']['payloadData'].items():
              if(k!= '_timestamp' and k!='data_timestamp'):
                payload[self.device['group']][self.device['name']][k.replace(self.device['address']+'___','').upper()] = v
        except:
            print("Error con la comunicación del NodeMCU\n")
            payload[self.device['group']][self.device['name']]['ESTADO'] = 0
        return payload
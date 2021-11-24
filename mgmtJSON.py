# -*- coding: utf-8 -*-
#!/usr/bin/env python

import json

class mgmtJSON:
    def __init__(self):
        return None
    
    def writeJSON(self, fileName, data):
        with open(fileName, 'w') as file:
            json.dump(data, file, indent=4)

    def readJSON(self, fileName):
        with open(fileName) as file:
            return json.load(file)

if __name__ == "__main__":
    wj = mgmtJSON()
    data = {}
    data['1'] = 'un'
    data['2'] = 'deux'
    data['3'] = 'Trois'
    datos = {}
    datos['nombre'] = 'numbers'
    datos['data'] = data
    wj.writeJSON('ppp.json', datos)
    var = wj.readJSON('ppp.json')
    print(var['data']['1'])


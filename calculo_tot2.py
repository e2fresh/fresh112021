# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
from datetime import datetime
from mgmtJSON import mgmtJSON

class energiaTot:
    def totalizar(self, E, device):
        current_folder = os.getcwd()
        filename = current_folder  + "/Data/totales.json"
        JSONFile = mgmtJSON()
        valores_actuales = JSONFile.readJSON(filename)
        fecha_actual = datetime.strptime(valores_actuales[device['group']][device['name']]["fecha"], "%Y-%m-%d %H:%M:%S.%f")
        flag = False
        # Horarios
        hora_actual = datetime.now().hour
        hora_ref = fecha_actual.hour
        if hora_actual > hora_ref:
            flag = True
            valores_actuales[device['group']][device['name']]["EH"] = E
            eh = 0
        else:
            eh = E - valores_actuales[device['group']][device['name']]["EH"]
        # Diarios
        dia_actual = datetime.now().day
        dia_ref = fecha_actual.day
        if dia_actual > dia_ref:
            flag = True
            valores_actuales[device['group']][device['name']]["ED"] = E
            valores_actuales[device['group']][device['name']]["EH"] = E
            ed = 0
            eh = 0
        else:
            ed = E - valores_actuales[device['group']][device['name']]["ED"]
        # Mensuales
        mes_actual = datetime.now().month
        mes_ref = fecha_actual.month
        if mes_actual > mes_ref:
            flag = True
            valores_actuales[device['group']][device['name']]["EM"] = E
            valores_actuales[device['group']][device['name']]["ED"] = E
            valores_actuales[device['group']][device['name']]["EH"] = E
            em = 0
            ed = 0
            eh = 0
        else:
            em = E - valores_actuales[device['group']][device['name']]["EM"]
        # Anuales
        anio_actual = datetime.now().year
        anio_ref = fecha_actual.year
        if anio_actual > anio_ref:
            flag = True
            valores_actuales[device['group']][device['name']]["EM"] = E
            valores_actuales[device['group']][device['name']]["ED"] = E
            valores_actuales[device['group']][device['name']]["EH"] = E
            em = 0
            ed = 0
            eh = 0
        else:
            em = E - valores_actuales[device['group']][device['name']]["EM"]

        if flag:
            valores_actuales[device['group']][device['name']]["fecha"] = str(datetime.now())
            mgmtJSON().writeJSON(filename, valores_actuales)
        return eh, ed, em
    
    
    def totalizar2(self, E, device, devicename):
        current_folder = os.getcwd()
        filename = current_folder  + "/Data/totales.json"
        JSONFile = mgmtJSON()
        valores_actuales = JSONFile.readJSON(filename)
        fecha_actual = datetime.strptime(valores_actuales[device['group']][devicename]["fecha"], "%Y-%m-%d %H:%M:%S.%f")
        flag = False
        # Horarios
        hora_actual = datetime.now().hour
        hora_ref = fecha_actual.hour
        if hora_actual > hora_ref:
            flag = True
            valores_actuales[device['group']][devicename]["EH"] = E
            eh = 0
        else:
            eh = E - valores_actuales[device['group']][devicename]["EH"]
        # Diarios
        dia_actual = datetime.now().day
        dia_ref = fecha_actual.day
        if dia_actual > dia_ref:
            flag = True
            valores_actuales[device['group']][devicename]["ED"] = E
            valores_actuales[device['group']][devicename]["EH"] = E
            ed = 0
            eh = 0
        else:
            ed = E - valores_actuales[device['group']][devicename]["ED"]
        # Mensuales
        mes_actual = datetime.now().month
        mes_ref = fecha_actual.month
        if mes_actual > mes_ref:
            flag = True
            valores_actuales[device['group']][devicename]["EM"] = E
            valores_actuales[device['group']][devicename]["ED"] = E
            valores_actuales[device['group']][devicename]["EH"] = E
            em = 0
            ed = 0
            eh = 0
        else:
            em = E - valores_actuales[device['group']][devicename]["EM"]
        # Anuales
        anio_actual = datetime.now().year
        anio_ref = fecha_actual.year
        if anio_actual > anio_ref:
            flag = True
            valores_actuales[device['group']][devicename]["EM"] = E
            valores_actuales[device['group']][devicename]["ED"] = E
            valores_actuales[device['group']][devicename]["EH"] = E
            em = 0
            ed = 0
            eh = 0
        else:
            em = E - valores_actuales[device['group']][devicename]["EM"]

        if flag:
            valores_actuales[device['group']][devicename]["fecha"] = str(datetime.now())
            mgmtJSON().writeJSON(filename, valores_actuales)
        return eh, ed, em
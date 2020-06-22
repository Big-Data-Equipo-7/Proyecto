# -*- coding: utf-8 -*-
"""
Created on Fri May 15 18:36:51 2020

@author: raulh
"""

import datetime
import pandas as pd

#Función para obtener las magnitudes de Calidad de Aire y Meteorologicas solo con valores V 
def desagrupar(dataframe):
    magnitudesCalidadAire = [1,6,8,10,14]
    magnitudesMetereologicas = [81,82,83,86,87,88,89]
    array= []
    
    print("Empezamos con el for (esto tarda en torno a 12 minutos) " + datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
    for index, row in dataframe.iterrows():
        if row.magnitud in magnitudesCalidadAire:
            #dia de la semana 0 lunes -> 6 domingo (5 y 6 fin de semana)
            diaDeLaSemana = datetime.datetime(row.ano, row.mes, row.dia).weekday()
            if row.v01 == "V":
                array.append({"id": row.fecha + "-00:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-00:00-" + row.estacion_real, "fechahora": row.fecha + " 00:00", "fecha": row.fecha, "hora": "1", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud, "factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h01, "valor_magnitud":row.h01, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana})
            if row.v02 == "V":
                array.append({"id": row.fecha + "-01:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-01:00-" + row.estacion_real, "fechahora": row.fecha + " 01:00", "fecha": row.fecha, "hora": "2", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud, "factor_calculo_horario": row.factor_calculo_horario,"ica_parcial": row.ica_h02,"valor_magnitud":row.h02, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v03 == "V":
                array.append({"id": row.fecha + "-02:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-02:00-" + row.estacion_real, "fechahora": row.fecha + " 02:00", "fecha": row.fecha, "hora": "3", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud, "factor_calculo_horario": row.factor_calculo_horario,"ica_parcial": row.ica_h03,"valor_magnitud":row.h03, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v04 == "V":
                array.append({"id": row.fecha + "-03:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-03:00-" + row.estacion_real, "fechahora": row.fecha + " 03:00", "fecha": row.fecha, "hora": "4", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud, "factor_calculo_horario": row.factor_calculo_horario,"ica_parcial": row.ica_h04,"valor_magnitud":row.h04, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v05 == "V":
                array.append({"id": row.fecha + "-04:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-04:00-" + row.estacion_real, "fechahora": row.fecha + " 04:00", "fecha": row.fecha, "hora": "5", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud, "factor_calculo_horario": row.factor_calculo_horario,"ica_parcial": row.ica_h05,"valor_magnitud":row.h05, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v06 == "V":
                array.append({"id": row.fecha + "-05:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-05:00-" + row.estacion_real, "fechahora": row.fecha + " 05:00", "fecha": row.fecha, "hora": "6", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud, "factor_calculo_horario": row.factor_calculo_horario,"ica_parcial": row.ica_h06,"valor_magnitud":row.h06, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v07 == "V":
                array.append({"id": row.fecha + "-06:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-06:00-" + row.estacion_real, "fechahora": row.fecha + " 06:00", "fecha": row.fecha, "hora": "7", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud, "factor_calculo_horario": row.factor_calculo_horario,"ica_parcial": row.ica_h07,"valor_magnitud":row.h07, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v08 == "V":
                array.append({"id": row.fecha + "-07:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-07:00-" + row.estacion_real, "fechahora": row.fecha + " 07:00", "fecha": row.fecha, "hora": "8", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud, "factor_calculo_horario": row.factor_calculo_horario,"ica_parcial": row.ica_h08,"valor_magnitud":row.h08, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v09 == "V":                
                array.append({"id": row.fecha + "-08:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-08:00-" + row.estacion_real, "fechahora": row.fecha + " 08:00", "fecha": row.fecha, "hora": "9", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud, "factor_calculo_horario": row.factor_calculo_horario,"ica_parcial": row.ica_h09,"valor_magnitud":row.h09, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v10 == "V":
                array.append({"id": row.fecha + "-09:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-09:00-" + row.estacion_real, "fechahora": row.fecha + " 09:00", "fecha": row.fecha, "hora": "10", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h10, "valor_magnitud":row.h10, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v11 == "V":
                array.append({"id": row.fecha + "-10:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-10:00-" + row.estacion_real, "fechahora": row.fecha + " 10:00", "fecha": row.fecha, "hora": "11", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h11, "valor_magnitud":row.h11, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v12 == "V":
                array.append({"id": row.fecha + "-11:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-11:00-" + row.estacion_real, "fechahora": row.fecha + " 11:00", "fecha": row.fecha, "hora": "12", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h12, "valor_magnitud":row.h12, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v13 == "V":
                array.append({"id": row.fecha + "-12:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-12:00-" + row.estacion_real, "fechahora": row.fecha + " 12:00", "fecha": row.fecha, "hora": "13", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h13, "valor_magnitud":row.h13, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v14 == "V":
                array.append({"id": row.fecha + "-13:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-13:00-" + row.estacion_real, "fechahora": row.fecha + " 13:00", "fecha": row.fecha, "hora": "14", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h14, "valor_magnitud":row.h14, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v15 == "V":
                array.append({"id": row.fecha + "-14:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-14:00-" + row.estacion_real, "fechahora": row.fecha + " 14:00", "fecha": row.fecha, "hora": "15", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h15, "valor_magnitud":row.h15, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v16 == "V":
                array.append({"id": row.fecha + "-15:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-15:00-" + row.estacion_real, "fechahora": row.fecha + " 15:00", "fecha": row.fecha, "hora": "16", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h16, "valor_magnitud":row.h16, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v17 == "V":
                array.append({"id": row.fecha + "-16:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-16:00-" + row.estacion_real, "fechahora": row.fecha + " 16:00", "fecha": row.fecha, "hora": "17", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h17, "valor_magnitud":row.h17, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v18 == "V":
                array.append({"id": row.fecha + "-17:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-17:00-" + row.estacion_real, "fechahora": row.fecha + " 17:00", "fecha": row.fecha, "hora": "18", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h18, "valor_magnitud":row.h18, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v19 == "V":
                array.append({"id": row.fecha + "-18:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-18:00-" + row.estacion_real, "fechahora": row.fecha + " 18:00", "fecha": row.fecha, "hora": "19", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h19, "valor_magnitud":row.h19, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v20 == "V":
                array.append({"id": row.fecha + "-19:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-19:00-" + row.estacion_real, "fechahora": row.fecha + " 19:00", "fecha": row.fecha, "hora": "20", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h20, "valor_magnitud":row.h20, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v21 == "V":
                array.append({"id": row.fecha + "-20:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-20:00-" + row.estacion_real, "fechahora": row.fecha + " 20:00", "fecha": row.fecha, "hora": "21", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h21, "valor_magnitud":row.h21, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v22 == "V":                
                array.append({"id": row.fecha + "-21:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-21:00-" + row.estacion_real, "fechahora": row.fecha + " 21:00", "fecha": row.fecha, "hora": "22", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h22, "valor_magnitud":row.h22, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v23 == "V":
                array.append({"id": row.fecha + "-22:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-22:00-" + row.estacion_real, "fechahora": row.fecha + " 22:00", "fecha": row.fecha, "hora": "23", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h23, "valor_magnitud":row.h23, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
            if row.v24 == "V":
                array.append({"id": row.fecha + "-23:00-" + row.estacion_real + "-" + str(row.magnitud), "id_merge": row.fecha + "-23:00-" + row.estacion_real, "fechahora": row.fecha + " 23:00", "fecha": row.fecha, "hora": "24", "estacion_real": row.estacion_real, "magnitud": row.magnitud, "descripcion_magnitud": row.descripcion_magnitud,"factor_calculo_horario": row.factor_calculo_horario, "ica_parcial": row.ica_h24, "valor_magnitud":row.h24, "provincia": row.provincia, "municipio": row.municipio, "dia_de_la_semana": diaDeLaSemana })
        
        if row.magnitud in magnitudesMetereologicas:
            if row.v01 == "V":
                array.append({ "id_merge": row.fecha + "-00:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h01})
            if row.v02 == "V":
                array.append({ "id_merge": row.fecha + "-01:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h02})
            if row.v03 == "V":
                array.append({ "id_merge": row.fecha + "-02:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h03})
            if row.v04 == "V":
                array.append({ "id_merge": row.fecha + "-03:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h04})
            if row.v05 == "V":
                array.append({ "id_merge": row.fecha + "-04:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h05})
            if row.v06 == "V":
                array.append({ "id_merge": row.fecha + "-05:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h06})
            if row.v07 == "V":
                array.append({ "id_merge": row.fecha + "-06:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h07})
            if row.v08 == "V":
                array.append({ "id_merge": row.fecha + "-07:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h08})
            if row.v09 == "V":                
                array.append({ "id_merge": row.fecha + "-08:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h09})
            if row.v10 == "V":
                array.append({ "id_merge": row.fecha + "-09:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h10})
            if row.v11 == "V":
                array.append({ "id_merge": row.fecha + "-10:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h11})
            if row.v12 == "V":
                array.append({ "id_merge": row.fecha + "-11:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h12})
            if row.v13 == "V":
                array.append({ "id_merge": row.fecha + "-12:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h13})
            if row.v14 == "V":
                array.append({ "id_merge": row.fecha + "-13:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h14})
            if row.v15 == "V":
                array.append({ "id_merge": row.fecha + "-14:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h15})
            if row.v16 == "V":
                array.append({ "id_merge": row.fecha + "-15:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h16})
            if row.v17 == "V":
                array.append({ "id_merge": row.fecha + "-16:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h17})
            if row.v18 == "V":
                array.append({ "id_merge": row.fecha + "-17:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h18})
            if row.v19 == "V":
                array.append({ "id_merge": row.fecha + "-18:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h19})
            if row.v20 == "V":
                array.append({ "id_merge": row.fecha + "-19:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h20})
            if row.v21 == "V":
                array.append({ "id_merge": row.fecha + "-20:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h21})
            if row.v22 == "V":
                array.append({ "id_merge": row.fecha + "-21:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h22})
            if row.v23 == "V":
                array.append({ "id_merge": row.fecha + "-22:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h23})
            if row.v24 == "V":
                array.append({ "id_merge": row.fecha + "-23:00-" + row.estacion_real, "valor_magnitud_"+ str(row.magnitud): row.h24})
    print("Fin del for " + datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
    return array

#Configuramos pandas sin límiete a la hora de mostrar
#pd.set_option('display.max_rows', None)

print("Inicio de script " + datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
#CALIDAD DEL AIRE
#Obtenemos los Datos Calidad del aire de la Comunidad de Madrid
urlCACMEnero18 = 'Datos/CA Comunidad de Madrid/2018_01.csv'
urlCACMFebrero18 = 'Datos/CA Comunidad de Madrid/2018_02.csv'
urlCACMMarzo18 = 'Datos/CA Comunidad de Madrid/2018_03.csv'
urlCACMAbril18 = 'Datos/CA Comunidad de Madrid/2018_04.csv'
urlCACMMayo18 = 'Datos/CA Comunidad de Madrid/2018_05.csv' 
urlCACMJunio18 = 'Datos/CA Comunidad de Madrid/2018_06.csv'
urlCACMJulio18 = 'Datos/CA Comunidad de Madrid/2018_07.csv'
urlCACMAgosto18 = 'Datos/CA Comunidad de Madrid/2018_08.csv'
urlCACMSeptiembre18 = 'Datos/CA Comunidad de Madrid/2018_09.csv'
urlCACMOctubre18 = 'Datos/CA Comunidad de Madrid/2018_10.csv'    
urlCACMNoviembre18 = 'Datos/CA Comunidad de Madrid/2018_11.csv'
urlCACMDiciembre18 = 'Datos/CA Comunidad de Madrid/2018_12.csv'
urlCACMEnero19 = 'Datos/CA Comunidad de Madrid/2019_01.csv'
urlCACMFebrero19 = 'Datos/CA Comunidad de Madrid/2019_02.csv'
urlCACMMarzo19 = 'Datos/CA Comunidad de Madrid/2019_03.csv'
urlCACMAbril19 = 'Datos/CA Comunidad de Madrid/2019_04.csv'
urlCACMMayo19 = 'Datos/CA Comunidad de Madrid/2019_05.csv' 
urlCACMJunio19 = 'Datos/CA Comunidad de Madrid/2019_06.csv'
urlCACMJulio19 = 'Datos/CA Comunidad de Madrid/2019_07.csv'
urlCACMAgosto19 = 'Datos/CA Comunidad de Madrid/2019_08.csv'
urlCACMSeptiembre19 = 'Datos/CA Comunidad de Madrid/2019_09.csv'
urlCACMOctubre19 = 'Datos/CA Comunidad de Madrid/2019_10.csv'    
urlCACMNoviembre19 = 'Datos/CA Comunidad de Madrid/2019_11.csv'
urlCACMDiciembre19 = 'Datos/CA Comunidad de Madrid/2019_12.csv'    
urlCACMEnero20 = 'Datos/CA Comunidad de Madrid/2020_01.csv'
urlCACMFebrero20 = 'Datos/CA Comunidad de Madrid/2020_02.csv'
urlCACMMarzo20 = 'Datos/CA Comunidad de Madrid/2020_03.csv'
urlCACMAbril20 = 'Datos/CA Comunidad de Madrid/2020_04.csv'
urlCACMMayo20 = 'Datos/CA Comunidad de Madrid/2020_05.csv'

datosCACMEnero18 = pd.read_csv(urlCACMEnero18, sep=";")
datosCACMFebrero18 = pd.read_csv(urlCACMFebrero18, sep=";")
datosCACMMarzo18 = pd.read_csv(urlCACMMarzo18, sep=";")
datosCACMAbril18 = pd.read_csv(urlCACMAbril18, sep=";")
datosCACMMayo18 = pd.read_csv(urlCACMMayo18, sep=";")
datosCACMJunio18 = pd.read_csv(urlCACMJunio18, sep=";")
datosCACMJulio18 = pd.read_csv(urlCACMJulio18, sep=";")
datosCACMAgosto18 = pd.read_csv(urlCACMAgosto18, sep=";")
datosCACMSeptiembre18 = pd.read_csv(urlCACMSeptiembre18, sep=";")
datosCACMOctubre18 = pd.read_csv(urlCACMOctubre18, sep=";")
datosCACMNoviembre18 = pd.read_csv(urlCACMNoviembre18, sep=";")
datosCACMDiciembre18 = pd.read_csv(urlCACMDiciembre18, sep=";")
datosCACMEnero19 = pd.read_csv(urlCACMEnero19, sep=";")
datosCACMFebrero19 = pd.read_csv(urlCACMFebrero19, sep=";")
datosCACMMarzo19 = pd.read_csv(urlCACMMarzo19, sep=";")
datosCACMAbril19 = pd.read_csv(urlCACMAbril19, sep=";")
datosCACMMayo19 = pd.read_csv(urlCACMMayo19, sep=";")
datosCACMJunio19 = pd.read_csv(urlCACMJunio19, sep=";")
datosCACMJulio19 = pd.read_csv(urlCACMJulio19, sep=";")
datosCACMAgosto19 = pd.read_csv(urlCACMAgosto19, sep=";")
datosCACMSeptiembre19 = pd.read_csv(urlCACMSeptiembre19, sep=";")
datosCACMOctubre19 = pd.read_csv(urlCACMOctubre19, sep=";")
datosCACMNoviembre19 = pd.read_csv(urlCACMNoviembre19, sep=";")
datosCACMDiciembre19 = pd.read_csv(urlCACMDiciembre19, sep=";")
datosCACMEnero20 = pd.read_csv(urlCACMEnero20, sep=";")
datosCACMFebrero20 = pd.read_csv(urlCACMFebrero20, sep=";")
datosCACMMarzo20 = pd.read_csv(urlCACMMarzo20, sep=";")
datosCACMAbril20 = pd.read_csv(urlCACMAbril20, sep=";")
datosCACMMayo20 = pd.read_csv(urlCACMMayo20, sep=";")

#Obtenemos los Datos Calidad del Aire del Ayuntamiento de Madrid
urlCAAMEnero18 = 'Datos/CA Ayuntamiento de Madrid/ene_mo18.csv'
urlCAAMFebrero18 = 'Datos/CA Ayuntamiento de Madrid/feb_mo18.csv'
urlCAAMMarzo18 = 'Datos/CA Ayuntamiento de Madrid/mar_mo18.csv'
urlCAAMAbril18 = 'Datos/CA Ayuntamiento de Madrid/abr_mo18.csv'
urlCAAMMayo18 = 'Datos/CA Ayuntamiento de Madrid/may_mo18.csv'
urlCAAMJunio18 = 'Datos/CA Ayuntamiento de Madrid/jun_mo18.csv'
urlCAAMJulio18 = 'Datos/CA Ayuntamiento de Madrid/jul_mo18.csv'
urlCAAMAgosto18 = 'Datos/CA Ayuntamiento de Madrid/ago_mo18.csv'
urlCAAMSeptiembre18 = 'Datos/CA Ayuntamiento de Madrid/sep_mo18.csv'
urlCAAMOctubre18 = 'Datos/CA Ayuntamiento de Madrid/oct_mo18.csv'
urlCAAMNoviembre18 = 'Datos/CA Ayuntamiento de Madrid/nov_mo18.csv'
urlCAAMDiciembre18 = 'Datos/CA Ayuntamiento de Madrid/dic_mo18.csv'
urlCAAMEnero19 = 'Datos/CA Ayuntamiento de Madrid/ene_mo19.csv'
urlCAAMFebrero19 = 'Datos/CA Ayuntamiento de Madrid/feb_mo19.csv'
urlCAAMMarzo19 = 'Datos/CA Ayuntamiento de Madrid/mar_mo19.csv'
urlCAAMAbril19 = 'Datos/CA Ayuntamiento de Madrid/abr_mo19.csv'
urlCAAMMayo19 = 'Datos/CA Ayuntamiento de Madrid/may_mo19.csv'
urlCAAMJunio19 = 'Datos/CA Ayuntamiento de Madrid/jun_mo19.csv'
urlCAAMJulio19 = 'Datos/CA Ayuntamiento de Madrid/jul_mo19.csv'
urlCAAMAgosto19 = 'Datos/CA Ayuntamiento de Madrid/ago_mo19.csv'
urlCAAMSeptiembre19 = 'Datos/CA Ayuntamiento de Madrid/sep_mo19.csv'
urlCAAMOctubre19 = 'Datos/CA Ayuntamiento de Madrid/oct_mo19.csv'
urlCAAMNoviembre19 = 'Datos/CA Ayuntamiento de Madrid/nov_mo19.csv'
urlCAAMDiciembre19 = 'Datos/CA Ayuntamiento de Madrid/dic_mo19.csv'
urlCAAMEnero20 = 'Datos/CA Ayuntamiento de Madrid/ene_mo20.csv'
urlCAAMFebrero20 = 'Datos/CA Ayuntamiento de Madrid/feb_mo20.csv'
urlCAAMMarzo20 = 'Datos/CA Ayuntamiento de Madrid/mar_mo20.csv'
urlCAAMAbril20 = 'Datos/CA Ayuntamiento de Madrid/abr_mo20.csv'
urlCAAMMayo20 = 'Datos/CA Ayuntamiento de Madrid/may_mo20.csv'

datosCAAMEnero18 = pd.read_csv(urlCAAMEnero18, sep=";")
datosCAAMFebrero18 = pd.read_csv(urlCAAMFebrero18, sep=";")
datosCAAMMarzo18 = pd.read_csv(urlCAAMMarzo18, sep=";")
datosCAAMAbril18 = pd.read_csv(urlCAAMAbril18, sep=";")
datosCAAMMayo18 = pd.read_csv(urlCAAMMayo18, sep=";")
datosCAAMJunio18 = pd.read_csv(urlCAAMJunio18, sep=";")
datosCAAMJulio18 = pd.read_csv(urlCAAMJulio18, sep=";")
datosCAAMAgosto18 = pd.read_csv(urlCAAMAgosto18, sep=";")
datosCAAMSeptiembre18 = pd.read_csv(urlCAAMSeptiembre18, sep=";")
datosCAAMOctubre18 = pd.read_csv(urlCAAMOctubre18, sep=";")
datosCAAMNoviembre18 = pd.read_csv(urlCAAMNoviembre18, sep=";")
datosCAAMDiciembre18 = pd.read_csv(urlCAAMDiciembre18, sep=";")

datosCAAMEnero18 = pd.read_csv(urlCAAMEnero18, sep=";")
datosCAAMFebrero18 = pd.read_csv(urlCAAMFebrero18, sep=";")
datosCAAMMarzo18 = pd.read_csv(urlCAAMMarzo18, sep=";")
datosCAAMAbril18 = pd.read_csv(urlCAAMAbril18, sep=";")
datosCAAMMayo18 = pd.read_csv(urlCAAMMayo18, sep=";")
datosCAAMJunio18 = pd.read_csv(urlCAAMJunio18, sep=";")
datosCAAMJulio18 = pd.read_csv(urlCAAMJulio18, sep=";")
datosCAAMAgosto18 = pd.read_csv(urlCAAMAgosto18, sep=";")
datosCAAMSeptiembre18 = pd.read_csv(urlCAAMSeptiembre18, sep=";")
datosCAAMOctubre18 = pd.read_csv(urlCAAMOctubre18, sep=";")
datosCAAMNoviembre18 = pd.read_csv(urlCAAMNoviembre18, sep=";")
datosCAAMDiciembre18 = pd.read_csv(urlCAAMDiciembre18, sep=";")
datosCAAMEnero19 = pd.read_csv(urlCAAMEnero19, sep=";")
datosCAAMFebrero19 = pd.read_csv(urlCAAMFebrero19, sep=";")
datosCAAMMarzo19 = pd.read_csv(urlCAAMMarzo19, sep=";")
datosCAAMAbril19 = pd.read_csv(urlCAAMAbril19, sep=";")
datosCAAMMayo19 = pd.read_csv(urlCAAMMayo19, sep=";")
datosCAAMJunio19 = pd.read_csv(urlCAAMJunio19, sep=";")
datosCAAMJulio19 = pd.read_csv(urlCAAMJulio19, sep=";")
datosCAAMAgosto19 = pd.read_csv(urlCAAMAgosto19, sep=";")
datosCAAMSeptiembre19 = pd.read_csv(urlCAAMSeptiembre19, sep=";")
datosCAAMOctubre19 = pd.read_csv(urlCAAMOctubre19, sep=";")
datosCAAMNoviembre19 = pd.read_csv(urlCAAMNoviembre19, sep=";")
datosCAAMDiciembre19 = pd.read_csv(urlCAAMDiciembre19, sep=";")
datosCAAMEnero20 = pd.read_csv(urlCAAMEnero20, sep=";")
datosCAAMFebrero20 = pd.read_csv(urlCAAMFebrero20, sep=";")
datosCAAMMarzo20 = pd.read_csv(urlCAAMMarzo20, sep=";")
datosCAAMAbril20 = pd.read_csv(urlCAAMAbril20, sep=";")
datosCAAMMayo20 = pd.read_csv(urlCAAMMayo20, sep=";")

#Unificamos los datos la Coumunidad de Madrid de 2018 para convertir campos en minuscula y así poder unificar con el resto de años de la comunidad
datosCACM18 = pd.concat([datosCACMEnero18, datosCACMFebrero18, datosCACMMarzo18, datosCACMAbril18, datosCACMMayo18, datosCACMJunio18, datosCACMJulio18, datosCACMAgosto18, datosCACMSeptiembre18, datosCACMOctubre18, datosCACMNoviembre18, datosCACMDiciembre18])
datosCACM18.columns = map(str.lower, datosCACM18.columns)

#Concatenamos Datos Calidad del Aire del Ayuntamiento de Madrid y Comunidad de Madrid por separado
print("Concatenamos datos Calidad del aire del Ayuntamiento de Madrid "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
datosCAAM = pd.concat([datosCAAMEnero18, datosCAAMFebrero18, datosCAAMMarzo18, datosCAAMAbril18, datosCAAMMayo18, datosCAAMJunio18, datosCAAMJulio18, datosCAAMAgosto18, datosCAAMSeptiembre18, datosCAAMOctubre18, datosCAAMNoviembre18, datosCAAMDiciembre18, datosCAAMEnero19, datosCAAMFebrero19, datosCAAMMarzo19, datosCAAMAbril19, datosCAAMMayo19, datosCAAMJunio19, datosCAAMJulio19, datosCAAMAgosto19, datosCAAMSeptiembre19, datosCAAMOctubre19, datosCAAMNoviembre19, datosCAAMDiciembre19, datosCAAMEnero20, datosCAAMFebrero20, datosCAAMMarzo20, datosCAAMAbril20, datosCAAMMayo20 ], sort=True)
print("Concatenamos datos Calidad del aire de la Comunidad de Madrid "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
datosCACM = pd.concat([datosCACM18, datosCACMEnero19, datosCACMFebrero19, datosCACMMarzo19, datosCACMAbril19, datosCACMMayo19, datosCACMJunio19, datosCACMJulio19, datosCACMAgosto19, datosCACMSeptiembre19, datosCACMOctubre19, datosCACMNoviembre19, datosCACMDiciembre19, datosCACMEnero20, datosCACMFebrero20, datosCACMMarzo20, datosCACMAbril20, datosCACMMayo20 ], sort=True)

#Convertimos en minusculas todas las columnas para poder concatenar con éxito.
print("Convertimos en minusculas todas las columnas de ambos dataframes "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
datosCACM.columns = map(str.lower, datosCACM.columns) 
datosCAAM.columns = map(str.lower, datosCAAM.columns) 

print("Eliminamos un punto de muestreo erróneo (28123002_14_8) "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
#Eliminamos punto de muestreo 28123002_14_8 de la comunidad de madrid. 14 Ozono se mide con técnica 6, no con 8
datosCACM = datosCACM[datosCACM["punto_muestreo"] != "28123002_14_8"]

print("Unificamos datos de Calidad del aire de Ayuntamiento y Comunidad "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
#Concatenamos Datos Calidad del aire del Ayuntamiento de Madrid y Comunidad de Madrid para unificarlos.
datosCA = pd.concat([datosCACM, datosCAAM ], sort=True)

print("Generamos el campo Estación real "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
#Creamos Estacion Real
datosCA['estacion_real'] = datosCA['punto_muestreo'].str[:8]
#datosCA['estacion_real'] = datosCA.punto_muestreo.apply(lambda x: x[:8])

print("Creamos campo fecha "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
#Creamos Fecha
datosCA['fecha'] =  datosCA.ano.apply(str) + '-' + datosCA.mes.apply(str) + '-' + datosCA.dia.apply(str)

print("Obtenemos Magnitudes de Calidad del aire "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
#Obtenemos Magnitudes Calidad del Aire
urlMagnitudesCA = 'Datos/Magnitudes Calidad del Aire.csv'
magnitudesCA = pd.read_csv(urlMagnitudesCA, sep=";")

#Exportar a CSV fichero de calidad de aire
#datosCA.to_csv('datosCaliadAire.csv', sep=";")

print("Unimos magnitudes con los datos para una mejor interpretación "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
#Hacemos el merge para introducir los valores descriptivos de cada magnitud, así como los valores límite y factor de cálculo de las 5 magnitudes a tener en cuenta
mergeCA = datosCA.merge(magnitudesCA, left_on='magnitud', right_on='codigo_magnitud')

#mergeCA["factor_calculo_horario"] = pd.to_numeric(mergeCA["factor_calculo_horario"], downcast="float")
#mergeCA["h01"] = pd.to_numeric(mergeCA["h01"], downcast="float")

print("Calculamos el ICA parcial para cada hora del día y magnitud "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h01'] = mergeCA['factor_calculo_horario'] * mergeCA['h01']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h02'] = mergeCA['factor_calculo_horario'] * mergeCA['h02']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h03'] = mergeCA['factor_calculo_horario'] * mergeCA['h03']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h04'] = mergeCA['factor_calculo_horario'] * mergeCA['h04']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h05'] = mergeCA['factor_calculo_horario'] * mergeCA['h05']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h06'] = mergeCA['factor_calculo_horario'] * mergeCA['h06']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h07'] = mergeCA['factor_calculo_horario'] * mergeCA['h07']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h08'] = mergeCA['factor_calculo_horario'] * mergeCA['h08']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h09'] = mergeCA['factor_calculo_horario'] * mergeCA['h09']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h10'] = mergeCA['factor_calculo_horario'] * mergeCA['h10']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h11'] = mergeCA['factor_calculo_horario'] * mergeCA['h11']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h12'] = mergeCA['factor_calculo_horario'] * mergeCA['h12']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h13'] = mergeCA['factor_calculo_horario'] * mergeCA['h13']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h14'] = mergeCA['factor_calculo_horario'] * mergeCA['h14']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h15'] = mergeCA['factor_calculo_horario'] * mergeCA['h15']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h16'] = mergeCA['factor_calculo_horario'] * mergeCA['h16']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h17'] = mergeCA['factor_calculo_horario'] * mergeCA['h17']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h18'] = mergeCA['factor_calculo_horario'] * mergeCA['h18']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h19'] = mergeCA['factor_calculo_horario'] * mergeCA['h19']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h20'] = mergeCA['factor_calculo_horario'] * mergeCA['h20']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h21'] = mergeCA['factor_calculo_horario'] * mergeCA['h21']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h22'] = mergeCA['factor_calculo_horario'] * mergeCA['h22']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h23'] = mergeCA['factor_calculo_horario'] * mergeCA['h23']
mergeCA.loc[mergeCA['factor_calculo_horario'].notnull(), 'ica_h24'] = mergeCA['factor_calculo_horario'] * mergeCA['h24']

print("Comenzamos el desagrupado "+ datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p'))
#Creamos array de Calidad del Aire
arrayCA = desagrupar(mergeCA)

#Creamos arrays Datos Metereológicos
#array81 = desagrupar(mergeDM[mergeDM["magnitud"]== 81])
#array82 = desagrupar(mergeDM[mergeDM["magnitud"]== 82])
#array83 = desagrupar(mergeDM[mergeDM["magnitud"]== 83])
#array86 = desagrupar(mergeDM[mergeDM["magnitud"]== 86])
#array87 = desagrupar(mergeDM[mergeDM["magnitud"]== 87])
#array88 = desagrupar(mergeDM[mergeDM["magnitud"]== 88])
#array89 = desagrupar(mergeDM[mergeDM["magnitud"]== 89])

print("Creamos de nuevo los dataframes")
datosDefinitivos = pd.DataFrame(arrayCA)
#df81 = pd.DataFrame(array81)
#df82 = pd.DataFrame(array82)
#df83 = pd.DataFrame(array83)
#df86 = pd.DataFrame(array86)
#df87 = pd.DataFrame(array87)
#df88 = pd.DataFrame(array88)
#df89 = pd.DataFrame(array89)

#merges
#datosDefinitivos = datosDefinitivos.merge(df81, on='id_merge')
#datosDefinitivos = datosDefinitivos.merge(df82, on='id_merge')
#datosDefinitivos = datosDefinitivos.merge(df83, on='id_merge')
#datosDefinitivos = datosDefinitivos.merge(df86, on='id_merge')
#datosDefinitivos = datosDefinitivos.merge(df87, on='id_merge')
#datosDefinitivos = datosDefinitivos.merge(df88, on='id_merge')
#datosDefinitivos = datosDefinitivos.merge(df89, on='id_merge')

#set Index
#datosDefinitivos.set_index('id')
#print(datosDefinitivos)

print("Exportamos a CSV los datos definitivos para el estudio")
#Exportar a Csv fichero detinitivo
datosDefinitivos.to_csv('datosdefinitivos.csv', sep=";", index=False)
print("-- Fin --")





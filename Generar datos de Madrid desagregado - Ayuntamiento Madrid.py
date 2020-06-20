# -*- coding: utf-8 -*-
"""
Created on Sat Jun 13 16:45:23 2020

@author: raulh
"""

import datetime
import pandas as pd

#Función para obtener las magnitudes de Calidad de Aire y Meteorologicas solo con valores V 
def desagrupar(dataframe):
    magnitudesCalidadAire = [1,6,8,10,14]
    magnitudesMetereologicas = [81,82,83,86,87,88,89]
    array= []
    
    print("Empezamos con el for (esto tarda)")
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
    print("Fin del for")
    return array

#Configuramos pandas sin límiete a la hora de mostrar
#pd.set_option('display.max_rows', None)

#DATOS METEREOLÓGICOS
#Obtenemos los Datos Metereológicos del Ayuntamiento de Madrid
urlDMAMEnero19 = 'Datos/DM Ayuntamiento de Madrid/ene_meteo19.csv'
urlDMAMFebrero19 = 'Datos/DM Ayuntamiento de Madrid/feb_meteo19.csv'
urlDMAMMarzo19 = 'Datos/DM Ayuntamiento de Madrid/mar_meteo19.csv'
urlDMAMAbril19 = 'Datos/DM Ayuntamiento de Madrid/abr_meteo19.csv'
urlDMAMMayo19 = 'Datos/DM Ayuntamiento de Madrid/may_meteo19.csv'
urlDMAMJunio19 = 'Datos/DM Ayuntamiento de Madrid/jun_meteo19.csv'
urlDMAMJulio19 = 'Datos/DM Ayuntamiento de Madrid/jul_meteo19.csv'
urlDMAMAgosto19 = 'Datos/DM Ayuntamiento de Madrid/ago_meteo19.csv'
urlDMAMSeptiembre19 = 'Datos/DM Ayuntamiento de Madrid/sep_meteo19.csv'
urlDMAMOctubre19 = 'Datos/DM Ayuntamiento de Madrid/oct_meteo19.csv'
urlDMAMNoviembre19 = 'Datos/DM Ayuntamiento de Madrid/nov_meteo19.csv'
urlDMAMDiciembre19 = 'Datos/DM Ayuntamiento de Madrid/dic_meteo19.csv'
urlDMAMEnero20 = 'Datos/DM Ayuntamiento de Madrid/ene_meteo20.csv'
urlDMAMFebrero20 = 'Datos/DM Ayuntamiento de Madrid/feb_meteo20.csv'
urlDMAMMarzo20 = 'Datos/DM Ayuntamiento de Madrid/mar_meteo20.csv'
urlDMAMAbril20 = 'Datos/DM Ayuntamiento de Madrid/abr_meteo20.csv'

datosDMAMEnero19 = pd.read_csv(urlDMAMEnero19, sep=";")
datosDMAMFebrero19 = pd.read_csv(urlDMAMFebrero19, sep=";")
datosDMAMMarzo19 = pd.read_csv(urlDMAMMarzo19, sep=";")
datosDMAMAbril19 = pd.read_csv(urlDMAMAbril19, sep=";")
datosDMAMMayo19 = pd.read_csv(urlDMAMMayo19, sep=";")
datosDMAMJunio19 = pd.read_csv(urlDMAMJunio19, sep=";")
datosDMAMJulio19 = pd.read_csv(urlDMAMJulio19, sep=";")
datosDMAMAgosto19 = pd.read_csv(urlDMAMAgosto19, sep=";")
datosDMAMSeptiembre19 = pd.read_csv(urlDMAMSeptiembre19, sep=";")
datosDMAMOctubre19 = pd.read_csv(urlDMAMOctubre19, sep=";")
datosDMAMNoviembre19 = pd.read_csv(urlDMAMNoviembre19, sep=";")
datosDMAMDiciembre19 = pd.read_csv(urlDMAMDiciembre19, sep=";")
datosDMAMEnero20 = pd.read_csv(urlDMAMEnero20, sep=";")
datosDMAMFebrero20 = pd.read_csv(urlDMAMFebrero20, sep=";")
datosDMAMMarzo20 = pd.read_csv(urlDMAMMarzo20, sep=";")
datosDMAMAbril20 = pd.read_csv(urlDMAMAbril20, sep=";")

#Concatenamos Datos Metereológicos del Ayuntamiento de Madrid
datosDM = pd.concat([datosDMAMEnero19, datosDMAMFebrero19, datosDMAMMarzo19, datosDMAMAbril19, datosDMAMMayo19, datosDMAMJunio19, datosDMAMJulio19, datosDMAMAgosto19, datosDMAMSeptiembre19, datosDMAMOctubre19, datosDMAMNoviembre19, datosDMAMDiciembre19, datosDMAMEnero20, datosDMAMFebrero20, datosDMAMMarzo20, datosDMAMAbril20 ], sort=True)

#Convertimos en minusculas todas las columnas para poder concatenar con éxito.
datosDM.columns = map(str.lower, datosDM.columns) 

#Creamos el campo Estacion Real para poder unirlo a la lista de estaciones
#datosDM['estacion_real'] = datosDM['punto_muestreo'].str[:8]

datosDM['estacion_real'] = datosDM.punto_muestreo.apply(lambda x: x[:8])

#Creamos campo Fecha para poder agrupar mejor
datosDM['fecha'] = datosDM.dia.apply(str) + '/' + datosDM.mes.apply(str) + '/' + datosDM.ano.apply(str)

#Obtenemos Magnitudes Calidad del Aire
urlMagnitudesDM = 'Datos/Magnitudes Metereológicas.csv'
magnitudesDM = pd.read_csv(urlMagnitudesDM, sep=";")

#Exportar a Csv
#datosDM.to_csv('datosMetereológicos.csv', sep=";")

#Hacemos el merge para introducir los valores descriptivos de cada magnitud
mergeDM = datosDM.merge(magnitudesDM, left_on='magnitud', right_on='codigo_magnitud')


#CALIDAD DEL AIRE
#Obtenemos los Datos Calidad del Aire del Ayuntamiento de Madrid
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

#Concatenamos Datos Calidad del Aire del Ayuntamiento de Madrid y Comunidad de Madrid por separado
datosCA = pd.concat([datosCAAMEnero19, datosCAAMFebrero19, datosCAAMMarzo19, datosCAAMAbril19, datosCAAMMayo19, datosCAAMJunio19, datosCAAMJulio19, datosCAAMAgosto19, datosCAAMSeptiembre19, datosCAAMOctubre19, datosCAAMNoviembre19, datosCAAMDiciembre19, datosCAAMEnero20, datosCAAMFebrero20, datosCAAMMarzo20, datosCAAMAbril20 ], sort=True)

#Convertimos en minusculas todas las columnas para poder concatenar con éxito.
datosCA.columns = map(str.lower, datosCA.columns) 

#Creamos Estacion Real
datosCA['estacion_real'] = datosCA['punto_muestreo'].str[:8]
#datosCA['estacion_real'] = datosCA.punto_muestreo.apply(lambda x: x[:8])

#Creamos Fecha
datosCA['fecha'] = datosCA.dia.apply(str) + '/' + datosCA.mes.apply(str) + '/' + datosCA.ano.apply(str)

#Obtenemos Magnitudes Calidad del Aire
urlMagnitudesCA = 'Datos/Magnitudes Calidad del Aire.csv'
magnitudesCA = pd.read_csv(urlMagnitudesCA, sep=";")

#Exportar a CSV fichero de calidad de aire
#datosCA.to_csv('datosCaliadAire.csv', sep=";")

#Hacemos el merge para introducir los valores descriptivos de cada magnitud, así como los valores límite y factor de cálculo de las 5 magnitudes a tener en cuenta
mergeCA = datosCA.merge(magnitudesCA, left_on='magnitud', right_on='codigo_magnitud')

#mergeCA["factor_calculo_horario"] = pd.to_numeric(mergeCA["factor_calculo_horario"], downcast="float")
#mergeCA["h01"] = pd.to_numeric(mergeCA["h01"], downcast="float")

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

#Creamos array de Calidad del Aire
arrayCA = desagrupar(mergeCA)

#Creamos arrays Datos Metereológicos
array81 = desagrupar(mergeDM[mergeDM["magnitud"]== 81])
array82 = desagrupar(mergeDM[mergeDM["magnitud"]== 82])
array83 = desagrupar(mergeDM[mergeDM["magnitud"]== 83])
array86 = desagrupar(mergeDM[mergeDM["magnitud"]== 86])
array87 = desagrupar(mergeDM[mergeDM["magnitud"]== 87])
array88 = desagrupar(mergeDM[mergeDM["magnitud"]== 88])
array89 = desagrupar(mergeDM[mergeDM["magnitud"]== 89])

print("Creamos dataframes")
datosDefinitivos = pd.DataFrame(arrayCA)
df81 = pd.DataFrame(array81)
df82 = pd.DataFrame(array82)
df83 = pd.DataFrame(array83)
df86 = pd.DataFrame(array86)
df87 = pd.DataFrame(array87)
df88 = pd.DataFrame(array88)
df89 = pd.DataFrame(array89)

#merges
datosDefinitivos = datosDefinitivos.merge(df81, on='id_merge')
datosDefinitivos = datosDefinitivos.merge(df82, on='id_merge')
datosDefinitivos = datosDefinitivos.merge(df83, on='id_merge')
datosDefinitivos = datosDefinitivos.merge(df86, on='id_merge')
datosDefinitivos = datosDefinitivos.merge(df87, on='id_merge')
datosDefinitivos = datosDefinitivos.merge(df88, on='id_merge')
datosDefinitivos = datosDefinitivos.merge(df89, on='id_merge')

#set Index
datosDefinitivos.set_index('id')
print(datosDefinitivos)

print("Exportamos")
#Exportar a Csv fichero detinitivo
datosDefinitivos.to_csv('datosdefinitivos-ayuntamiento2019_2020.csv', sep=";", index=False)
print("-- Fin --")





# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 00:07:40 2020

@author: svaraalo
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


#CALIDAD DEL AIRE

#Obtenemos los Datos Calidad del aire de la Comunidad de Madrid

urlCACMEnero18 = '/Datos/CA Comunidad de Madrid/2018_01.csv'
urlCACMFebrero18 = '/Datos/CA Comunidad de Madrid/2018_02.csv'
urlCACMMarzo18 = '/Datos/CA Comunidad de Madrid/2018_03.csv'
urlCACMAbril18 = '/Datos/CA Comunidad de Madrid/2018_04.csv'
urlCACMMayo18 = '/Datos/CA Comunidad de Madrid/2018_05.csv'

urlCACMEnero19 = '/Datos/CA Comunidad de Madrid/2019_01.csv'
urlCACMFebrero19 = '/Datos/CA Comunidad de Madrid/2019_02.csv'
urlCACMMarzo19 = '/Datos/CA Comunidad de Madrid/2019_03.csv'
urlCACMAbril19 = '/Datos/CA Comunidad de Madrid/2019_04.csv'
urlCACMMayo19 = '/Datos/CA Comunidad de Madrid/2019_05.csv'

urlCACMEnero = '/Datos/CA Comunidad de Madrid/2020_01.csv'
urlCACMFebrero = '/Datos/CA Comunidad de Madrid/2020_02.csv'
urlCACMMarzo = '/Datos/CA Comunidad de Madrid/2020_03.csv'
urlCACMAbril = '/Datos/CA Comunidad de Madrid/2020_04.csv'
urlCACMMayo = '/Datos/CA Comunidad de Madrid/2020_05.csv'


datosCACMEnero18 = pd.read_csv(urlCACMEnero18, sep=";")
datosCACMFebrero18 = pd.read_csv(urlCACMFebrero18, sep=";")
datosCACMMarzo18 = pd.read_csv(urlCACMMarzo18, sep=";")
datosCACMAbril18 = pd.read_csv(urlCACMAbril18, sep=";")
datosCACMMayo18 = pd.read_csv(urlCACMMayo18, sep=";")

datosCACMEnero19 = pd.read_csv(urlCACMEnero19, sep=";")
datosCACMFebrero19 = pd.read_csv(urlCACMFebrero19, sep=";")
datosCACMMarzo19 = pd.read_csv(urlCACMMarzo19, sep=";")
datosCACMAbril19 = pd.read_csv(urlCACMAbril19, sep=";")
datosCACMMayo19 = pd.read_csv(urlCACMMayo19, sep=";")

datosCACMEnero = pd.read_csv(urlCACMEnero, sep=";")
datosCACMFebrero = pd.read_csv(urlCACMFebrero, sep=";")
datosCACMMarzo = pd.read_csv(urlCACMMarzo, sep=";")
datosCACMAbril = pd.read_csv(urlCACMAbril, sep=";")
datosCACMMayo = pd.read_csv(urlCACMMayo, sep=";")

#Obtenemos los Datos Calidad del Aire del Ayuntamiento de Madrid

urlCAAMEnero18= '/Datos/CA Ayuntamiento de Madrid/ene_mo18.csv'
urlCAAMFebrero18 = '/Datos/CA Ayuntamiento de Madrid/feb_mo18.csv'
urlCAAMMarzo18 = '/Datos/CA Ayuntamiento de Madrid/mar_mo18.csv'
urlCAAMAbril18 = '/Datos/CA Ayuntamiento de Madrid/abr_mo18.csv'
urlCAAMMayo18 = '/Datos/CA Ayuntamiento de Madrid/may_mo18.csv'

urlCAAMEnero19 = '/Datos/CA Ayuntamiento de Madrid/ene_mo19.csv'
urlCAAMFebrero19 = '/Datos/CA Ayuntamiento de Madrid/feb_mo19.csv'
urlCAAMMarzo19 = '/Datos/CA Ayuntamiento de Madrid/mar_mo19.csv'
urlCAAMAbril19 = '/Datos/CA Ayuntamiento de Madrid/abr_mo19.csv'
urlCAAMMayo19 = '/Datos/CA Ayuntamiento de Madrid/may_mo19.csv'

urlCAAMEnero = '/Datos/CA Ayuntamiento de Madrid/ene_mo20.csv'
urlCAAMFebrero = '/Datos/CA Ayuntamiento de Madrid/feb_mo20.csv'
urlCAAMMarzo = '/Datos/CA Ayuntamiento de Madrid/mar_mo20.csv'
urlCAAMAbril = '/Datos/CA Ayuntamiento de Madrid/abr_mo20.csv'
urlCAAMMayo = '/Datos/CA Ayuntamiento de Madrid/may_mo20.csv'

datosCAAMEnero18 = pd.read_csv(urlCAAMEnero18, sep=";")
datosCAAMFebrero18 = pd.read_csv(urlCAAMFebrero18, sep=";")
datosCAAMMarzo18 = pd.read_csv(urlCAAMMarzo18, sep=";")
datosCAAMAbril18 = pd.read_csv(urlCAAMAbril18, sep=";")
datosCAAMMayo18 = pd.read_csv(urlCAAMMayo18, sep=";")

datosCAAMEnero19 = pd.read_csv(urlCAAMEnero19, sep=";")
datosCAAMFebrero19 = pd.read_csv(urlCAAMFebrero19, sep=";")
datosCAAMMarzo19 = pd.read_csv(urlCAAMMarzo19, sep=";")
datosCAAMAbril19 = pd.read_csv(urlCAAMAbril19, sep=";")
datosCAAMMayo19 = pd.read_csv(urlCAAMMayo19, sep=";")

datosCAAMEnero = pd.read_csv(urlCAAMEnero, sep=";")
datosCAAMFebrero = pd.read_csv(urlCAAMFebrero, sep=";")
datosCAAMMarzo = pd.read_csv(urlCAAMMarzo, sep=";")
datosCAAMAbril = pd.read_csv(urlCAAMAbril, sep=";")
datosCAAMMayo = pd.read_csv(urlCAAMMayo, sep=";")

#Concatenamos Datos Calidad del Aire del Ayuntamiento de Madrid y Comunidad de Madrid por separado

datosCAAM = pd.concat([datosCAAMEnero18, datosCAAMFebrero18, datosCAAMMarzo18, datosCAAMAbril18 ,datosCAAMMayo18,datosCAAMEnero19, datosCAAMFebrero19, datosCAAMMarzo19, datosCAAMAbril19 ,datosCAAMMayo19,datosCAAMEnero, datosCAAMFebrero, datosCAAMMarzo, datosCAAMAbril , datosCAAMMayo], sort=True)
datosCACM = pd.concat([datosCACMEnero18, datosCACMFebrero18, datosCACMMarzo18, datosCACMAbril18 ,datosCACMMayo18,datosCACMEnero19, datosCACMFebrero19, datosCACMMarzo19, datosCACMAbril19 ,datosCACMMayo19,datosCACMEnero, datosCACMFebrero, datosCACMMarzo, datosCACMAbril , datosCACMMayo], sort=True)

                 
#Convertimos en minusculas todas las columnas para poder concatenar con éxito.
datosCACM.columns = map(str.lower, datosCACM.columns) 
datosCAAM.columns = map(str.lower, datosCAAM.columns) 

#Eliminamos punto de muestreo 28123002_14_8 de la comunidad de madrid. 14 Ozono se mide con técnica 6, no con 8
datosCACM = datosCACM[datosCACM["punto_muestreo"] != "28123002_14_8"]

#Concatenamos Datos Calidad del aire del Ayuntamiento de Madrid y Comunidad de Madrid para unificarlos.
datosCA = pd.concat([datosCACM, datosCAAM ], sort=True)


#Creamos Estacion Real
datosCA['estacion_real'] = datosCA['punto_muestreo'].str[:8]


#Creamos Fecha
datosCA['fecha'] =  datosCA.ano.apply(str) + '-' + datosCA.mes.apply(str) + '-' + datosCA.dia.apply(str)
datosCA['fecha2'] = pd.DatetimeIndex(datosCA['fecha'])
datosCA['mes'] = datosCA['fecha2'].dt.month
datosCA['año'] = datosCA['fecha2'].dt.year
datosCA['dia'] = datosCA['fecha2'].dt.day

#Obtenemos Magnitudes Calidad del Aire
urlMagnitudesCA = '/Datos/Magnitudes Calidad del Aire.csv'
magnitudesCA = pd.read_csv(urlMagnitudesCA, sep=";")

#Exportar a CSV fichero de calidad de aire
datosCA.to_csv('datosCaliadAire.csv', sep=";")

#Hacemos el merge para introducir los valores descriptivos de cada magnitud, así como los valores límite y factor de cálculo de las 5 magnitudes a tener en cuenta
mergeCA = datosCA.merge(magnitudesCA, left_on='magnitud', right_on='codigo_magnitud')



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


print("Creamos dataframes")
datosDefinitivos = pd.DataFrame(arrayCA)


#set Index
datosDefinitivos.set_index('id')
print(datosDefinitivos)

print("Exportamos")
#Exportar a Csv fichero detinitivo
datosDefinitivos.to_csv('datosHistoricosCalidadAire.csv', sep=";", index=False)
print("-- Fin --")







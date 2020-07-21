## Efectos del confinamiento en la calidad del aire de la Comunidad de Madrid

_Este proyecto es una práctica docente. Su objetivo es poner en práctica las técnicas de Big Data y Machine Learning aprendidas._

_Este documento forma parte de un proyecto publicado en [https://github.com/Big-Data-Equipo-7/Proyecto](https://github.com/Big-Data-Equipo-7/Proyecto)_ 

### Integrantes del Grupo 7
* Alfonso Gallardo (Científico de datos)
* Raúl Hervás (Analista de datos)
* Carmen Reina (Analista de negocio)
* Walter Ronceros (Arquitecto de datos)
* Susana Vara (Analista de datos - Representante)

### Limitaciones ###

Para este estudio damos por hecho ciertas limitaciones insalvables como son:

* No todas las estaciones contienen medición de todos los agentes contaminantes.
* Las mediciones meteorológicas no se pueden prever.
* El índice ICA (Índice Calidad del Aire) se obtiene de la medición más adversa de 5 agentes contaminantes por lo que no puede utilizarse para buscar correlaciones directas.

### Tecnologías 📋

* Python 3.8.2
* Anaconda Navigator 3.0.1
* Docker 19.03.8
* Jupyter Notebook 6.0.3
* Spyder 
* Elasticsearch
* Databricks
* Google Colab

### Instrucciones para la reproducción del trabajo

**A tener en cuenta:** *Los scripts están preparados para funcionar en rutas concretas y han de ejecutarse en el mismo orden para tener los resultados esperados.*

1. Ejecución del script _*1 - Generar datos de Madrid desagregado.py*_ para obtener el dataset que se utilizará en el siguiente punto (datosdefinitivos.csv).
2. Ejecución del [Notebook albergado en Colab](https://colab.research.google.com/drive/1hAkG64bXv-BuhfkH0_3qH2lx-pIUcLTK#scrollTo=nh7diHL592kF). Se guarda una copia dentro del proyecto con el nombre _*2 - Estudio datos de Madrid.ipynb*_. Hay que tener en cuenta de que la reproducción de los modelos están preparadas para funcionar en Google Colab, la ejecución en local requiere algunas modificaciones del Notebook. 
3. Ejecución del script _*3 - Generar datosHistoricosCalidadDelAire.py*_ para obtener el dataset que se utilizará en el siguiente punto (datosHistoricosCalidadAire.csv)
4. Ejecución del Notebook Jupyter _*4 - Estudio datosHistoricosCalidadDelAire.ipynb*_ 

### Instrucciones para entorno de visualización ###

Esta fase se realiza apoyándonos en dockers donde utilizaremos la pila **ELK**. 

Podrás ver un video explicativo en el siguiente enlace [Video](https://photos.app.goo.gl/AvezfKMgfHQqV7C46)

#### Necesitarás ####
* Instalar [Docker Desktop](https://www.docker.com/products/docker-desktop)
* Descarga de contenedor [sebp/elk](https://hub.docker.com/r/sebp/elk/)
* Arrancar el contender indicando los puertos para Elastic, Logstash y Kibana
* Copiar dataset al contenedor para procesarlo con Logstash
* Crear config para Logstash con nombre de index global_info
* Crear índice global_info con el mapeo del campo localización para que el tipo de dato sea geo_point
* Ejecutamos logstash para realizar carga con el comando: logstash -f /opt/logstash/config/grupo7_BigData_global.config

*Para mas detalle consultar la _memoria y/o ver video explicativo._*

### Índice de links externos ###

* Proyecto en Github: [https://github.com/Big-Data-Equipo-7/Proyecto](https://github.com/Big-Data-Equipo-7/Proyecto)
* Notebook: [Colab de Google](https://colab.research.google.com/drive/1hAkG64bXv-BuhfkH0_3qH2lx-pIUcLTK#scrollTo=nh7diHL592kF)
* Video demostrativo de Dockery ELK: [Video](https://photos.app.goo.gl/AvezfKMgfHQqV7C46)
* Dataset Datos Meteorológicos Comunidad de Madrid: [Dataset](http://datos.comunidad.madrid/catalogo/dataset/calidad_aire_datos_meteo_historico)
* Dataset Datos Calidad del Aire Comunidad de Madrid: [Dataste](http://datos.comunidad.madrid/catalogo/dataset/calidad_aire_datos_historico)
* Dataset Estaciones Comunidad de Madrid: [Dataset](http://datos.comunidad.madrid/catalogo/dataset/calidad_aire_estaciones)
* Dataste Datos Meteorológicos Ayuntamiento de Madrid: [Dataset](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=8d7357cec5efa610VgnVCM1000001d4a900aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default)
* Dataste Datos Calidad del Aire Ayuntamiento de Madrid: [Dataset](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=aecb88a7e2b73410VgnVCM2000000c205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default)
* Dataset Estaciones Ayuntamiento de Madrid: [Dataset](https://datos.madrid.es/portal/site/egob/menuitem.c05c1f754a33a9fbe4b2e4b284f1a5a0/?vgnextoid=9e42c176313eb410VgnVCM1000000b205a0aRCRD&vgnextchannel=374512b9ace9f310VgnVCM100000171f5a0aRCRD&vgnextfmt=default)
* Descarga de software: [Docker Desktop](https://www.docker.com/products/docker-desktop)
* Descarga de contenedor Docker: [sebp/elk](https://hub.docker.com/r/sebp/elk/)
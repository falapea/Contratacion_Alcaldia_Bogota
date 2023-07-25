
    # Projecto de analitica de datos con una base de datos de libre acceso, detallare el paso a paso de este análisis

import pandas as pd # manejo de data frames
import seaborn as sns # visualización
import matplotlib.pyplot as plt
import numpy as np #
import io
import scipy.stats # distribuciones estadísticas

    # Agregamos la base de datos a través de la libreria pandas, la cual nos permite trabajar con archivos de excel 
datos = pd.read_excel('C:\\Users\\Camilo\\Documents\\Data Science\\Alcaldia_projecto\\AlcaldiaBogota_2017_2019.xlsx')
print(datos)

    # Contrastamos y exploramos los datos de las columnas para verificar que esten todas las columnas correctamente cargadas
print('Filas: ', datos.shape[0])
print('Columnas: ', datos.shape[1])

print(datos.columns)
    # La función dtypes nos permite conocer el tipo de elemento al que pertenecen los datos, estos elementos pueden ser: int, float, object, bool, datetime, category
    # para este conjunto de datos, la mayor parte de elementos son object, exceptuando los datos de fecha (datetime64) y int64, los cuales son propios de la librería numpy
    
print(datos.dtypes)

cualicolumns=datos.select_dtypes(exclude=['int64','float64','datetime64']).columns
cuanticolumns=datos.select_dtypes(exclude=['object','datetime64']).columns
datecolumns=datos.select_dtypes(exclude=['object','float64','int64']).columns
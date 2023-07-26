
    # Projecto de analitica de datos con una base de datos de libre acceso, detallare el paso a paso de este análisis

import pandas as pd # manejo de data frames
import seaborn as sns # visualización
import matplotlib.pyplot as plt
import numpy as np #
import io
import scipy.stats # distribuciones estadísticas

    # Agregamos la base de datos a través de la libreria pandas, la cual nos permite trabajar con archivos de excel con la función read_excel()
datos = pd.read_excel('C:\\Users\\Camilo\\Documents\\Data Science\\Alcaldia_projecto\\AlcaldiaBogota_2017_2019.xlsx')
print(datos)

    # Contrastamos y exploramos los datos de las columnas para verificar que esten todas las columnas correctamente cargadas
    # el print para filas "0" nos arroja 1359, y el print para columnas "1" arroja 27, con lo cual se verifica que los datos están en bien cargados

print('Filas: ', datos.shape[0])
print('Columnas: ', datos.shape[1])

print(datos.columns)

    # La función dtypes nos permite conocer el tipo de elemento al que pertenecen los datos, estos elementos pueden ser: int, float, object, bool, datetime, category
    # para este conjunto de datos, la mayor parte de elementos son object, exceptuando los datos de fecha (datetime64) y int64, los cuales son propios de la librería numpy
    
print(datos.dtypes)

    # La función select_dtypes() nos permite filtrar las columnas que tiene un dataframe de acuerdo al tipo de elemento 
    # Con el parametro exclude se busca excluir el tipo de elementos, que no deseamos ver con la función select_dtypes()
    # Finalmente, hacemos un print que nos muestre los resultados de la función
    
cualicolumns=datos.select_dtypes(exclude=['int64','float64','datetime64']).columns
cuanticolumns=datos.select_dtypes(exclude=['object','datetime64']).columns
datecolumns=datos.select_dtypes(exclude=['object','float64','int64']).columns

print("El número de variables categóricas es: ", len(cualicolumns))
print("El numero de variables cuantitativas es: ", len(cuanticolumns))
print("El número de variables tipo fecha es de: ",len(datecolumns))

valorcontrato = datos["Valor del Contrato"].describe()
pd.options.display.float_format = '{:.2f}'.format

print(valorcontrato)

sns.histplot(datos['Valor del Contrato'], kde=False)
plt.show()
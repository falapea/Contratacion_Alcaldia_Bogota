
    # Projecto de analitica de datos con una base de datos de libre acceso, detallare el paso a paso de este análisis

import pandas as pd # manejo de data frames
import seaborn as sns # visualización
import matplotlib.pyplot as plt
import numpy as np #
import io
import scipy.stats # distribuciones estadísticas
from scipy.stats import t

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

    # Usamos la función de seaborn para crear histogramas sns.histplot() dejando el Kernel Density Estimation como False, 
    # Dada la distribución de los datos se recomienda usar el logaritmo en base 10, para escalar los datos y tener una mejor visualización de los mismos,
    # Esto se hace mediante la función de numpy np.log10()
    # Con la función plt.title, xlabel, ylabel, se le otorga títulos y etiquetas a los ejes
    # Mostramos el histograma con la función de Matplotlib plt.show() 

datos['log_variable'] = np.log10(datos['Valor del Contrato']+1)
sns.histplot(datos['log_variable'], kde=False)
plt.title('Valores del contrato')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.show()

    # Con la función .value_counts() calculamos la frecuencia de un mismo valor en un determinada columna en este caso "Es pymes"
    # Esta función es muy interesante, dado que nos permite generar insights acerca de cuales son los valores más comunes en una serie, o los menos comunes. 

pymes= datos['Es Pyme'].value_counts()
print(pymes)

    # De igual forma, podemos sacar algunos estádisticos como el porcentaje de participación de las empresas pymes y las no pymes, 
    # esto agregando al código la formula de calculo de porcentaje cantidad/total *100

datos['Es Pyme'].value_counts()/len(datos)*100

    # Podemos describir el comportamiento de las columnas con la función .describe(include=[0]), la cual nos permite analizar columnas con datos No numericos

variables_interes= datos.describe(include = ['O'])[['Sector','Tipo de Contrato']]
print(variables_interes)    

    # Con la función .drop_duplicates, podemos ver el tipo de valores que tiene cada columna, esta función es para mirar varias columnas la vez
    # en caso de que se requiera ver el comportamiento de una sola columna se usa la función .unique() en vez de drop_duplicates()
    
tipo_datos = datos[['Sector','Tipo de Contrato']].drop_duplicates()
print(tipo_datos)

    # Ahora creamos unos diagramas de caja los cuales son muy útiles para ver la distribución por cuartiles, así como para visualizar algunos estadísticos básicos, y valores extremos
    # Esto lo hacemos con la función de seaborn llamada .boxplot
    # También, es muy importante rotar los labeles, para evitar que los datos se solapen y así tener una mejor visibilidad.  

sns.boxplot(x='Tipo de Contrato', y='Valor del Contrato', data=datos)
plt.xticks(rotation=90)
plt.show()

    # En ambos diagramas, buscamos ver la relación entre el tipo de contrato y el valor del mismo
    # así como la modalidad de contratación con relación al valor del contrato.

sns.boxplot(x='Modalidad de Contratacion', y='Valor del Contrato', data=datos)
plt.xticks(rotation=90)
plt.show()

    # Ahora queremos obtener algunos estadisticos de probabilidad de los datos, aplicando las formulas estadísticas
    # Comenzamos contado el total de los datos en la columna "valor del contrato"
total_contratos = datos['Valor del Contrato'].count()
print("El número total de registros es:", total_contratos)
    # Si quisieramos saber cual es la probabilidad de obtener un contrato con un costo mayor a 200 millones aplicamos la formula al conteo anterior
registros_mayor_200 = datos[datos['Valor del Contrato'] >200000000]['Valor del Contrato'].count()
print ('El número total de contratos con un costo mayor a 200 millones es:',registros_mayor_200)
    # Finalmente, con base en los datos anteriores calculamos la probabilidad de obtener un contrato mayor a 200 millones
probabilidad= registros_mayor_200/total_contratos
porcentaje = probabilidad*100
print("La probabilidad de obtener un contrato con un costo mayor a 200 millones es de: {:.2f}%".format(porcentaje))

    # Después de conocer los estádisticos de probabilidad, buscamos conocer los estimadores puntuales de promedio, varianza y desviación estándar, para los valores de contrato
    # lo cual es importante para conocer el comportamiento de la población con los datos de la muestra 

media_contratos = datos['Valor del Contrato'].mean()
print("El valor promedio de los contratos es", media_contratos)
var_contratos = np.var(datos['Valor del Contrato'])
print("La varianza de los contratos es: ", var_contratos)
desv_contratos  = var_contratos** 0.5
print("La desviación estándar de la varianza es: ", desv_contratos)

    # Finalmente, para terminar el análisis de los datos, calculamos los intervalos de confianza y hacemos pruebas de hipotesis con los datos
    # para ver la confiabilidad de la muestra
    # importante importar la distribución t del paquete scipy


    # Definir la muestra
n = len(datos['Valor del Contrato'])
    # Calcular la media muestral y la desviación estándar muestral
media = media_contratos
s = desv_contratos
    # Definir el nivel de significancia y los grados de libertad
alpha = 0.05
gl = n - 1
    # Calcular el valor crítico de la distribución t
t_critico = t.ppf(1 - alpha / 2, gl)
    # Calcular el intervalo de confianza
intervalo = (media - t_critico * s / np.sqrt(n), media + t_critico * s / np.sqrt(n))
print("Intervalo de confianza del 95%:", intervalo)
print("Podemos asegurar con un 95% de confianza que el valor promedio de los contratos para esta entidad está en el rango:", intervalo)

    # Para finalzar hacemos una prueba de hipotesis planteando la hipotesis nula de que los contratos tienen un costo promedio de 70.000 000
    # para esto comenzamos definiendo el valor hipotético de la media poblacional    
mu0 = 70000000
    # Calculamos el estadístico de prueba t
t_est = (media - mu0) / (s / np.sqrt(n))
    # Calculamos los grados de libertad y el valor crítico de t
gl = n - 1
t_critico = t.ppf(1 - 0.05/2, gl)
    # Finalmente, se imprime el resultado de la prueba de hipótesis
    # y se crea un reporte en word analizando los resultados de todo el trabajo hecho acá.   
if t_est > t_critico or t_est < -t_critico:
    print("Se rechaza H0, la media poblacional es diferente de", mu0)
else:
    print("No se puede rechazar H0, la media poblacional es igual a", mu0)

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
columnas = datos.columns
print = (columnas)


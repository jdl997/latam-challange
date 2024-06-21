from typing import List, Tuple
from datetime import datetime
import pandas as pd
import dataset_treatment as dt
from memory_profiler import profile

"""
Retorna una lista de tuplas con el top 10 fechas con más tweets y el usuario (username) que más publicaciones tiene por cada uno de esos días con el enfoque de optimización de memoria

Parámetros:
   file_path: str - ruta del archivo .json que contiene el dataset de los tweets 

Retorna:
    List[Tuple[pd.Timestamp, str]]: Lista de tuplas con ('date', 'username').
"""
@profile
def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:

    # convierte el path a un df con solo las columnas necesarias ['id', 'date', 'username', 'user_id']
    df = dt.dataset_q1(file_path)

    # Contar tweets por fecha
    tweet_counts = df['date'].value_counts().nlargest(10)

    # Inicializar una lista para almacenar los resultados
    results = []

    # Iterar sobre las top 10 fechas para encontrar el usuario más activo cada día
    for date in tweet_counts.index:
        # Filtrar los tweets de la fecha actual
        daily_tweets = df[df['date'] == date]
        # Encontrar el usuario más activo
        top_user = daily_tweets['username'].value_counts().idxmax()
        # Agregar a la lista de resultados
        results.append((date, top_user))

    return results
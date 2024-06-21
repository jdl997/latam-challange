from typing import List, Tuple
from datetime import datetime
import pandas as pd
import dataset_treatment as dt

"""
Retorna una lista de tuplas con el top 10 fechas con más tweets y el usuario (username) que más publicaciones tiene por cada uno de esos días.

Parámetros:
   file_path: str - ruta del archivo .json que contiene el dataset de los tweets 

Retorna:
    List[Tuple[pd.Timestamp, str]]: Lista de tuplas con ('date', 'username').
"""
def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:

    # convierte el path a un df con solo las columnas necesarias ['id', 'date', 'username', 'user_id']
    df = dt.dataset_q1(file_path)

    # Contar tweets por fecha
    tweet_counts = df.groupby('date').size().reset_index(name='tweet_count')

    # Obtener las 10 fechas con más tweets
    top_10_dates = tweet_counts.nlargest(10, 'tweet_count')['date']

    # Inicializar una lista para almacenar los resultados
    results = []

    # Iterar sobre las top 10 fechas para encontrar el usuario más activo cada día
    for date in top_10_dates:
        # Filtrar los tweets de la fecha actual
        daily_tweets = df[df['date'] == date]

        # Contar los tweets por usuario en la fecha actual
        top_user = daily_tweets['username'].mode().values[0]

        results.append((date, top_user))

    return results
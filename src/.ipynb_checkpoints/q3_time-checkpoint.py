from typing import List, Tuple
import dataset_treatment as dt
import pandas as pd
from typing import List, Tuple
from collections import defaultdict, Counter

"""
El top 10 histórico de usuarios (username) más influyentes en función del conteo de las menciones (@) que registra cada uno de ellos con enfoque de optimizacion de tiempo

Parámetros:
   file_path: str - ruta del archivo .json que contiene el dataset de los tweets 

Retorna:
    List[Tuple[str, int]]: Lista de tuplas con ('username', 'conteo').
"""
def q3_time(file_path: str) -> List[Tuple[str, int]]:
    # convierte el path a un df con solo las columnas necesarias ['id','username','id_username','mentionedUsers_dict']
    df = dt.dataset_q3(file_path)

    mention_counts = defaultdict(int)
    
    for index, row in df.iterrows():
        if pd.notnull(row['mentionedUsers_dict']):
            mentioned_users = row['mentionedUsers_dict']
            # Asegurarse de que es un diccionario
            if isinstance(mentioned_users, dict):
                mention_counts[row['username']] += len(mentioned_users)
    
    # Convertir el defaultdict a Counter para usar el most_common
    mention_counter = Counter(mention_counts)
    
    # Obtener el top 10
    top_10_users = mention_counter.most_common(10)
    return top_10_users

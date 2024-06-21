from typing import List, Tuple
import dataset_treatment as dt
import pandas as pd
from collections import Counter
import re
from itertools import chain
from memory_profiler import profile


# Compilar la expresión regular una vez
emoji_pattern = re.compile("["
                           u"\U0001F600-\U0001F64F"  # emoticons
                           u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                           u"\U0001F680-\U0001F6FF"  # transport & map symbols
                           u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                           u"\U00002702-\U000027B0"
                           u"\U000024C2-\U0001F251"
                           "]+", flags=re.UNICODE)

# Función para extraer emojis
def extract_emojis(text):
    return emoji_pattern.findall(text)

"""
Retorna una lista de tuplas con el top 10 emojis más usados con su respectivo conteo con enfoque de optimizacion de memoria

Parámetros:
   file_path: str - ruta del archivo .json que contiene el dataset de los tweets 

Retorna:
    List[Tuple[datetime.date, str]]: Lista de tuplas con ('emoji', 'conteo').
"""
# Función para extraer emojis de un solo texto
@profile
def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    # convierte el path a un df con solo las columnas necesarias ['content']
    df = dt.dataset_q2(file_path)
    
    # Generador para emojis extraídos
    emoji_gen = (emoji for text in df['content'] for emoji in extract_emojis(text))
    
    # Contar emojis directamente desde el generador
    emoji_counts = Counter(emoji_gen)
    
    # Obtener el top 10 de emojis más usados
    top_10_emojis = emoji_counts.most_common(10)
    return top_10_emojis

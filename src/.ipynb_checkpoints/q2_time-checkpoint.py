from typing import List, Tuple
import dataset_treatment as dt
import pandas as pd
from collections import Counter
import re


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
    
def q2_time(file_path: str) -> List[Tuple[str, int]]:
    # convierte el path a un df con solo las columnas necesarias ['content']
    df = dt.dataset_q2(file_path)

    # Medición del tiempo de ejecución
    all_emojis = [emoji for text in df['content'] for emoji in extract_emojis(text)]
    all_emojis = [emoji for text in df['content'] for emoji in extract_emojis(text)]
    [emoji for text in df['content'] for emoji in extract_emojis(text)]
    
    # Aplicar la extracción de emojis y contar
    all_emojis = [emoji for text in df['content'] for emoji in extract_emojis(text)]
    emoji_counts = Counter(all_emojis)
    top_10_emojis = emoji_counts.most_common(10)
    
    return top_10_emojis
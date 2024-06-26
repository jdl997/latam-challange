import json
import pandas as pd

def dataset_q1(file_path: str):
    # Lee el archivo JSON línea por línea y carga cada línea como un objeto JSON
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    
    # Convierte los datos en un DataFrame
    df = pd.DataFrame(data)

    # Filtra el dataset para solo utilizar id, date y user
    df= df.filter(items=['id','date','user'])

    # Aplanar la columna 'user' para extraer 'username' y 'id'
    df_user = pd.json_normalize(df['user'])
    
    # Seleccionar solo las columnas 'username' e 'id'
    df_user = df_user[['username', 'id']]
    
    # Renombrar la columna "id" por "username_id" para evitar conflictos con el id del tweet
    df_user = df_user.rename(columns= {'id':'id_username'})
    
    # Unir las nuevas columnas al DataFrame original
    df = pd.concat([df, df_user], axis=1)

    # Eliminar la columna original 'user' y 'mentionedUsers_dict' ya que no son mas necesarios
    df = df.drop(columns=['user'])

    # Convertir la columna 'date' a DateTime
    df['date'] = pd.to_datetime(df['date']).dt.date

    return df

def dataset_q2(file_path: str):
    # Lee el archivo JSON línea por línea y carga cada línea como un objeto JSON
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    
    # Convierte los datos en un DataFrame
    df = pd.DataFrame(data)

    # Filtra el dataset para solo utilizar content 
    df= df.filter(items=['content'])

    return df

def list_to_dict(lst):
    if lst is None:
        return None
    return {str(item['id']): item['username'] for item in lst if 'id' in item and 'username' in item}


def dataset_q3(file_path: str):
    # Lee el archivo JSON línea por línea y carga cada línea como un objeto JSON
    with open(file_path, 'r') as file:
        data = [json.loads(line) for line in file]
    
    # Convierte los datos en un DataFrame
    df = pd.DataFrame(data)

    # Filtra el dataset para solo utilizar content 
    df= df.filter(items=['id','user','mentionedUsers'])

    # Aplanar la columna 'user' para extraer 'username' y 'id'
    df_user = pd.json_normalize(df['user'])
    
    # Seleccionar solo las columnas 'username' e 'id'
    df_user = df_user[['username', 'id']]
    
    # Renombrar la columna "id" por "username_id" para evitar conflictos con el id del tweet
    df_user = df_user.rename(columns= {'id':'id_username'})
    
    # Unir las nuevas columnas al DataFrame original
    df = pd.concat([df, df_user], axis=1)
    
    # Aplicar la función a la columna 'mentionedUsers'
    df['mentionedUsers_dict'] = df['mentionedUsers'].apply(list_to_dict)

    # Eliminar la columna original 'user' y 'mentionedUsers_dict' ya que no son mas necesarios
    df = df.drop(columns=['user'])
    df = df.drop(columns=['mentionedUsers'])

    return df
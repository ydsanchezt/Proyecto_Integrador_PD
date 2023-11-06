import pandas as pd
import numpy as np
import json

with open("dataset.csv", "r", encoding="utf-8") as file:
        lineas = file.readlines()
print (lineas)

# Cargar el archivo CSV en un DataFrame

df = pd.read_csv('dataset.csv')

# Verificar que no existan valores faltantes

def limpieza_df(df):
    valores_faltantes = df.isnull().sum()
    if valores_faltantes.sum() == 0:
        print("No hay valores faltantes.")
    else:
        print("Hay valores faltantes.")
    print(valores_faltantes)

# Verificar que no existan filas repetidas

    filas_duplicadas = df[df.duplicated()]
    if filas_duplicadas.shape[0] == 0:
     print("No hay filas duplicadas.")
    else:
        print("Hay filas duplicadas.")
    print(filas_duplicadas)   

# Verificar si existen valores atípicos y eliminarlos
Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1
umbral = 1.5
filas_atipicas = ((df < (Q1 - umbral * IQR)) | (df > (Q3 + umbral * IQR))).any(axis=1)
print(df[filas_atipicas])
df_limpieza = df[~filas_atipicas]

# Crear una columna que categorice por edades

def categorizar_edad(age):
    if age <= 12:
        return 'Niño'
    elif 13 <= age <= 19:
        return 'Adolescente'
    elif 20 <= age <= 39:
        return 'Jóvenes adultos'
    elif 40 <= age <= 59:
        return 'Adulto'
    else:
        return 'Adulto mayor'
    
df['categoria_edad'] = df['age'].apply(categorizar_edad)
print(df)

# Guardar el resultado como csv
df.to_csv('Dataset_Edad_categorizada.csv', index=False)


# Encapsula toda la lógica anterior en una función que reciba un dataframe como entrada.
    
Limpieza_procesamiento_datos = limpieza_df(df)
if Limpieza_procesamiento_datos is not None:
    Limpieza_procesamiento_datos.to_csv ('Resultado_limpieza.csv', index = False)
    print("Limpieza y preparacion de datos 'resultado_limpieza.csv'")








    





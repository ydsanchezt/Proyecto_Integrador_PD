import pandas as pd
import sys

def limpieza_df(df):
    valores_faltantes = df.isnull().sum()
    if valores_faltantes.sum() == 0:
        print("No hay valores faltantes.")
    else:
        print("Hay valores faltantes.")
    print(valores_faltantes)

    filas_duplicadas = df[df.duplicated()]
    if filas_duplicadas.shape[0] == 0:
        print("No hay filas duplicadas.")
    else:
        print("Hay filas duplicadas.")
    print(filas_duplicadas)

    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    umbral = 1.5
    filas_atipicas = ((df < (Q1 - umbral * IQR)) | (df > (Q3 + umbral * IQR))).any(axis=1)
    print(df[filas_atipicas])
    df_limpieza = df[~filas_atipicas]

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

    df_limpieza['categoria_edad'] = df_limpieza['age'].apply(categorizar_edad)
    print(df_limpieza)

    df_limpieza.to_csv('Dataset_Edad_categorizada.csv', index=False)

def main(url):
    try:
        df = pd.read_csv(url)
        limpieza_df(df)
    except Exception as e:
        print(f"Error al procesar los datos: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python script.py <URL>")
    else:
        url = sys.argv[1]
        main(url)

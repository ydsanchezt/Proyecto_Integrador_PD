from datasets import load_dataset
import pandas as pd

dataset = load_dataset("mstz/heart_failure")
#print (dataset)

data = dataset["train"]
df = pd.DataFrame(data)
print (data)

Personas_Dead = df.loc[df['is_dead']==1]
print (Personas_Dead)
Personas_Vivas = df.loc[df['is_dead']!=1]
print (Personas_Vivas)

tipo_datos_age = df['age'].dtype
tipo_datos_sex = df['is_male'].dtype
tipo_datos_smoking = df['is_smoker'].dtype

print (tipo_datos_age)
print (tipo_datos_sex)
print (tipo_datos_smoking)

Cantidad_fumadores = df.groupby(['is_male', 'is_smoker']).size().unstack()
print (Cantidad_fumadores)



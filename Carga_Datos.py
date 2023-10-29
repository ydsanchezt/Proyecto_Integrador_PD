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

mean_dead = Personas_Dead['age'].mean()
mean_vivas = Personas_Vivas['age'].mean()

print (mean_dead)
print (mean_vivas)



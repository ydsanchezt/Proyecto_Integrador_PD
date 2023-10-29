from datasets import load_dataset
import numpy as np

dataset = load_dataset("mstz/heart_failure")
print (dataset)

data = dataset["train"]
print (data)

age = data['age']
print(age)

#Array edad
age_array = np.array(age)
print (age_array)

#Promedio edad
Avg_age = np.mean(age_array)
print (Avg_age)



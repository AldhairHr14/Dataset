import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


url = "https://raw.githubusercontent.com/AldhairHr14/Dataset/refs/heads/main/procesos_activos.csv"


df = pd.read_csv(url)


print("Primeras filas del dataset:")
print(df.head())


print("\nEstadísticas básicas:")
print(df[['cpu_percent', 'memory_percent']].describe())


print("\nMedia:")
print(df[['cpu_percent', 'memory_percent']].mean())

print("\nMediana:")
print(df[['cpu_percent', 'memory_percent']].median())

print("\nModa:")
print(df[['cpu_percent', 'memory_percent']].mode().iloc[0])

print("\nDesviación estándar:")
print(df[['cpu_percent', 'memory_percent']].std())


print("\nMatriz de correlación:")
correlacion = df[['cpu_percent', 'memory_percent']].corr()
print(correlacion)


sns.heatmap(correlacion, annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación")
plt.show()

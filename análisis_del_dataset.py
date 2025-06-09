import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Enlace público del CSV (reemplázalo con el tuyo)
url = "https://raw.githubusercontent.com/AldhairHr14/Dataset/refs/heads/main/procesos_activos.csv"

# Leer dataset
df = pd.read_csv(url)

# Mostrar primeras filas
print("Primeras filas del dataset:")
print(df.head())

# Estadísticas básicas
print("\nEstadísticas básicas:")
print(df[['cpu_percent', 'memory_percent']].describe())

# Media, mediana, moda, desviación estándar
print("\nMedia:")
print(df[['cpu_percent', 'memory_percent']].mean())

print("\nMediana:")
print(df[['cpu_percent', 'memory_percent']].median())

print("\nModa:")
print(df[['cpu_percent', 'memory_percent']].mode().iloc[0])

print("\nDesviación estándar:")
print(df[['cpu_percent', 'memory_percent']].std())

# Matriz de correlación
print("\nMatriz de correlación:")
correlacion = df[['cpu_percent', 'memory_percent']].corr()
print(correlacion)

# Visualización (opcional)
sns.heatmap(correlacion, annot=True, cmap="coolwarm")
plt.title("Matriz de Correlación")
plt.show()

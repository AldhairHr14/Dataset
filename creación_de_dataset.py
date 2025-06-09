import psutil
import pandas as pd
from datetime import datetime


procesos = []

for proc in psutil.process_iter(['pid', 'name', 'username', 'cpu_percent', 'memory_percent']):
    try:
        info = proc.info
        info['timestamp'] = datetime.now().isoformat()
        procesos.append(info)
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        continue


df = pd.DataFrame(procesos)


nombre_archivo = "procesos_activos.csv"
df.to_csv(nombre_archivo, index=False)

print(f"Archivo '{nombre_archivo}' guardado con éxito.")

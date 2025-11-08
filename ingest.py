import os
import requests

# Crear carpeta de destino si no existe
os.makedirs("data/raw", exist_ok=True)

# URL del dataset de ejemplo (puedes cambiarlo más adelante)
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
output_path = "data/raw/titanic.csv"

print("Descargando dataset desde:", url)
response = requests.get(url)

# Guardar el archivo
with open(output_path, "wb") as f:
    f.write(response.content)

print("✅ Descarga completada. Archivo guardado en:", output_path)

import pandas as pd
from pathlib import Path

# Definir rutas relativas al proyecto
repo_root = Path(__file__).resolve().parent
raw_path = repo_root / "data" / "raw" / "titanic.csv"
processed_path = repo_root / "data" / "processed" / "titanic_clean.csv"

print("Leyendo dataset desde:", raw_path)
df = pd.read_csv(raw_path)

# --- Exploración básica ---
print("\n🔍 Primeras 5 filas:")
print(df.head())
print("\n📏 Información general:")
print(df.info())
print("\n❓ Valores nulos por columna:")
print(df.isna().sum())

# --- Limpieza básica ---
# 1. Eliminar filas completamente vacías
df = df.dropna(how="all")

# 2. Rellenar edades faltantes con la media
if "age" in df.columns:
    df["age"] = df["age"].fillna(df["age"].mean())

# 3. Normalizar nombres de columnas (sin mayúsculas ni espacios)
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# 4. Eliminar duplicados
df = df.drop_duplicates()

# 5. Convertir columnas categóricas a minúsculas (si existen)
for col in df.select_dtypes(include="object").columns:
    df[col] = df[col].str.lower()

# --- Guardar dataset limpio ---
processed_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(processed_path, index=False)

print(f"\n✅ Limpieza completada. Archivo guardado en: {processed_path}")
print(f"Filas finales: {len(df)} | Columnas: {len(df.columns)}")

# VALIDACION DE LA CALIDAD

print("\n=== Validación extendida de calidad ===")

# 1️⃣ Nulos
print("\n% Nulos por columna:")
print(df.isnull().mean().sort_values(ascending=False) * 100)

# 2️⃣ Duplicados
print("\nFilas duplicadas:", df.duplicated().sum())

# 3️⃣ Tipos de datos
print("\nTipos de datos:")
print(df.dtypes)

# 4️⃣ Cardinalidad de categóricas
categoricas = df.select_dtypes(include='object').columns
for col in categoricas:
    print(f"\nCardinalidad de {col}: {df[col].nunique()} valores únicos")


# INDICE DE CALIDAD

# --- Data Quality Score ---
import numpy as np

# Pesos base
pesos = {
    'completitud': 0.4,
    'unicidad': 0.3,
    'validez': 0.3
}

# Completitud
completitud = 1 - (df.isnull().mean().mean())

# Unicidad
unicidad = 1 if df.duplicated().sum() == 0 else 0

# Validez (por ahora asumimos correcta tipología)
validez = 1

# Puntaje global
score = np.average([completitud, unicidad, validez], weights=list(pesos.values()))
print(f"\n📊 Data Quality Score: {score:.2%}")

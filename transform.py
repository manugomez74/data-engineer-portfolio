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

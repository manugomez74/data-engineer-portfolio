# ingest.py
"""
Ingest script - placeholder version.
Lee un CSV de data/raw/sample.csv y escribe una versión procesada en data/processed/sample_processed.csv
Este archivo será ampliado durante el Day 1.
"""

from pathlib import Path
import pandas as pd

def main():
    repo_root = Path(__file__).resolve().parent
    raw = repo_root / "data" / "raw"
    processed = repo_root / "data" / "processed"
    raw.mkdir(parents=True, exist_ok=True)
    processed.mkdir(parents=True, exist_ok=True)

    input_csv = raw / "sample.csv"
    if not input_csv.exists():
        print(f"[ERROR] No encuentro {input_csv}. Sube sample.csv a data/raw/ o crea una muestra.")
        return

    print(f"Leyendo {input_csv} ...")
    df = pd.read_csv(input_csv)
    print("Primeras 3 filas:")
    print(df.head(3).to_string())
    out = processed / "sample_processed.csv"
    df.dropna(how="all").to_csv(out, index=False)
    print(f"Guardado procesado en {out}. Filas: {len(df)}")

if __name__ == "__main__":
    main()

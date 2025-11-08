# Data Engineer Portfolio

## Objetivo del proyecto
Desarrollar un pipeline ETL que ingiera datos públicos, los transforme con Python/dbt y los cargue en Azure SQL / Data Lake. Visualización final con Power BI.

## Estructura de carpetas
- data/raw/: datos originales (subir `sample.csv` aquí)
- data/processed/: datos procesados (salida del pipeline)
- ingest.py: script de ingestión principal

## Dependencias mínimas
- Python 3.8+
- pandas
- git

## Estado
En progreso. Día 1: estructura inicial creada.

## Cómo ejecutar (mínimo)
1. Clona el repo:
   `git clone https://github.com/manugomez74/data-engineer-portfolio.git`
2. Crea y activa entorno virtual:
   `python -m venv venv`  
   Windows PowerShell: `.\venv\Scripts\Activate.ps1`  
   macOS/Linux: `source venv/bin/activate`
3. Instala dependencias:
   `pip install pandas`
4. Coloca tu CSV en `data/raw/sample.csv`
5. Ejecuta:
   `python ingest.py`

## Contacto
https://linkedin.com/in/tu-perfil

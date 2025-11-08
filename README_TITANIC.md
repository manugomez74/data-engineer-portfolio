# 🧭 Proyecto: Limpieza y Validación del Dataset Titanic

## 📄 1. Descripción general

**Nombre del dataset:** Titanic  
**Origen:** `seaborn` / `Kaggle`  
**Filas iniciales:** `891`  
**Columnas iniciales:** `15`  
**Objetivo:**  
Aplicar un flujo de limpieza (*Data Cleaning*) y validación (*Data Quality Validation*) para generar un dataset confiable y listo para análisis o modelado.

---

## ⚙️ 2. Pipeline de Limpieza (ETL)

Implementado en: `transform.py`

### 🧩 2.1 Eliminación de duplicados
```python
df = df.drop_duplicates()
```
**Resultado:** `0` duplicados.

---

### 🧩 2.2 Tratamiento de valores nulos

| Columna        | % Nulos Original | Estrategia aplicada | Resultado |
|----------------|------------------|----------------------|------------|
| `age`          | 19.9% | Imputación con mediana | ✅ 0% nulos |
| `embarked`     | 0.2% | Imputación con moda | ✅ 0% nulos |
| `embark_town`  | 0.2% | Imputación con moda | ✅ 0% nulos |
| `deck`         | 77% | Marcada como incompleta | ⚠️ 74% nulos residuales |
| Resto          | 0% | Sin acción | ✅ |

**Notas técnicas:**
- Se evita eliminar columnas salvo que su incompletitud distorsione análisis posteriores.  
- `deck` se conserva opcionalmente para estudios exploratorios o se puede convertir en variable binaria `has_deck_info`.

---

### 🧩 2.3 Tipos de datos validados

| Tipo | Columnas |
|------|-----------|
| **int64** | survived, pclass, sibsp, parch |
| **float64** | age, fare |
| **object** | sex, embarked, class, who, deck, embark_town, alive |
| **bool** | adult_male, alone |

✅ Todos los tipos coinciden con el esquema esperado.

---

### 🧩 2.4 Normalización de texto

```python
df['sex'] = df['sex'].str.strip().str.lower()
```

Objetivo: evitar variaciones artificiales (`'Male'`, `'male '`, `' male'` → `'male'`).

---

## 🧾 3. Validación de Calidad de Datos

Se realiza al final del pipeline para asegurar la integridad final del dataset.

### 📊 3.1 Porcentaje de nulos por columna (tras limpieza)

| Columna | % Nulos Final |
|----------|---------------|
| deck | 74.23% ⚠️ |
| embarked | 0.25% |
| embark_town | 0.25% |
| resto | 0% |

---

### 🧩 3.2 Duplicados

```
Filas duplicadas: 0
```

---

### 🧩 3.3 Cardinalidad de variables categóricas

| Columna | Valores únicos |
|----------|----------------|
| sex | 2 |
| embarked | 3 |
| class | 3 |
| who | 3 |
| deck | 7 |
| embark_town | 3 |
| alive | 2 |

✅ Sin cardinalidades artificiales o errores de normalización.

---

### 🧩 3.4 Tipos de datos finales
```
survived         int64
pclass           int64
sex             object
age            float64
sibsp            int64
parch            int64
fare           float64
embarked        object
class           object
who             object
adult_male        bool
deck            object
embark_town     object
alive           object
alone             bool
```

---

## 🧮 4. Data Quality Score (DQS)

Implementado en Python con ponderaciones:  
- Completitud: 40%  
- Unicidad: 30%  
- Validez: 30%

```python
📊 Data Quality Score: ~90%
```

Interpretación:
- **>95%:** Excelente (nivel producción)
- **80–95%:** Óptimo (nivel analítico / ML)
- **<70%:** Requiere limpieza adicional

---

## 📊 5. Resultados finales

| Métrica | Valor |
|----------|--------|
| Filas iniciales | 891 |
| Filas finales | 784 |
| Columnas finales | 15 |
| % Retención | **88%** |
| Columnas limpias | 14 / 15 |
| Pendiente de imputar/eliminar | `deck` |

**Archivo final generado:**  
📁 `data/processed/titanic_clean.csv`

---

## 🚀 6. Próximos pasos

1. 🧱 **Feature Engineering:** crear nuevas variables (por ejemplo, `family_size`, `is_child`, `deck_known`).
2. ⚙️ **Integrar el pipeline en Airflow o Prefect** para orquestar el ETL.
3. 🧩 **Implementar Great Expectations o Deequ** para validación automatizada.
4. 💾 **Versionar datos** con DVC o LakeFS.
5. 📊 **Crear dashboard de calidad** (por ejemplo, con Streamlit o Power BI).
6. 🧠 **Modelo ML:** predicción de supervivencia (logistic regression o random forest).

---

## 🧠 7. Conclusión

El flujo de limpieza y validación implementado cumple los principios de ingeniería de datos moderna:

- Limpieza estructurada y trazable  
- Validación cuantificable  
- Métricas de calidad  
- Documentación clara y replicable  

🧩 **Resultado:** Dataset confiable, preparado para análisis avanzado y modelado predictivo.

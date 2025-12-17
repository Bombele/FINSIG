
## 🇪🇸 README_TECHNIQUE_ES.md – core/architecture & modules/collection

markdown
# README Técnico – core/architecture & modules/collection


## 🎯 Objetivo
Este archivo proporciona instrucciones técnicas para usar y mantener el submódulo `core/architecture` y su módulo `collection`.  
Complementa los `SUB_MODULE_GUIDE` (cartas institucionales) y las `BITACORA` (registros de actividades).


## 📂 Estructura

### core/architecture
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Carta del submódulo.  
- `BITACORA_FR/EN/ES.md` → Registro de actividades trilingüe.  
- `README_TECHNIQUE_FR/EN/ES.md` → Manual técnico trilingüe.  
- `docs/ARCHITECTURE_GUIDE.md` → Principios estructurales.  
- `conformity/structure_validator.py` → Script de validación documental.  
- `conformity/workflow_checker.py` → Script de control de flujos.

### core/architecture/modules/collection
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Carta del módulo.  
- `BITACORA_FR/EN/ES.md` → Registro de actividades trilingüe.  
- `README_TECHNIQUE_FR/EN/ES.md` → Manual técnico trilingüe.  
- `data_collection.py` → Script de recolección y validación de datos.  
- `logs/collection_log.txt` → Archivo de trazabilidad de las recolecciones.


## ⚙️ Requisitos

### core/architecture
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions o pipelines en `infra_technical/ci-cd/`

### modules/collection
- Python 3.10+  
- Módulos estándar (`csv`, `json`, `datetime`)  
- CI/CD: GitHub Actions o pipelines en `infra_technical/ci-cd/`


## 🚀 Uso

### core/architecture
```bash
# Validar la conformidad documental
python conformity/structure_validator.py

# Verificar los flujos de trabajo
python conformity/workflow_checker.py

# Ejecutar las pruebas
pytest tests/
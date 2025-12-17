

## 🇪🇸 README_TECHNIQUE_ES.md – core/architecture

markdown
# README Técnico – core/architecture


## 🎯 Objetivo
Este archivo proporciona instrucciones técnicas para usar y mantener el submódulo `core/architecture` de FINSIG, junto con sus módulos asociados (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`).  
Complementa los `SUB_MODULE_GUIDE` (cartas institucionales) y las `BITACORA` (registros de actividades).



## 📂 Estructura

### core/architecture
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Carta del submódulo  
- `BITACORA_FR/EN/ES.md` → Registro de actividades trilingüe  
- `README_TECHNIQUE_FR/EN/ES.md` → Manual técnico trilingüe  
- `docs/ARCHITECTURE_GUIDE.md` → Principios estructurales  
- `conformity/structure_validator.py` → Script de validación documental  
- `conformity/workflow_checker.py` → Script de control de flujos  

### modules/collection
- `data_collection.py` → Script de recolección y validación de datos  
- `logs/collection_log.txt` → Archivo de trazabilidad de las recolecciones  

### modules/normalization
- `data_normalization.py` → Script de normalización de datos (fechas, cadenas, números, campos obligatorios, duplicados)  

### modules/orchestration
- `pipeline_orchestrator.py` → Script de orquestación del pipeline (recolección → normalización → conformidad → auditoría/scoring)  

### modules/schemas
- `base_schema.py` → Esquema institucional genérico (id, timestamp, source, valor, metadatos)  
- `finance_schema.py` → Esquema para transacciones financieras  
- `audit_schema.py` → Esquema para registros de auditoría  
- `compliance_schema.py` → Esquema para validaciones regulatorias  



## ⚙️ Requisitos
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions o pipelines en `infra_technical/ci-cd/`



## 🚀 Uso

### core/architecture
```bash
python conformity/structure_validator.py   # Validar la conformidad documental
python conformity/workflow_checker.py      # Verificar los flujos de trabajo
pytest tests/                              # Ejecutar las pruebas

# Recolectar datos JSON
python data_collection.py

# Validar la conformidad de los datos
pytest tests/

# Normalizar un conjunto de datos
python data_normalization.py

# Validar los datos normalizados
pytest tests/

# Ejecutar el pipeline completo (recolección → normalización → conformidad)
python pipeline_orchestrator.py

# Validar la integración del pipeline
pytest tests/

python finance_schema.py                   # Validar una transacción financiera
python audit_schema.py                     # Validar un registro de auditoría
python compliance_schema.py                # Validar una regla de conformidad
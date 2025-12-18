# GUÍA DE SUBMÓDULO – core/architecture

---

## 🎯 Objetivo
Esta guía define la estructura y las responsabilidades de los submódulos del directorio `core/architecture`.  
Garantiza la coherencia institucional, la trazabilidad y la auditabilidad de FINSIG.

---

## 📂 Submódulos

### 1. conformity/
- **structure_validator.py** → Verifica la presencia y conformidad de los archivos obligatorios.  
- **workflow_checker.py** → Controla la secuencia documental y la coherencia de los workflows.  
- **Rol**: Asegurar la conformidad documental e institucional.

### 2. collection/
- **data_collection.py** → Recolecta y valida datos brutos (CSV, JSON, API).  
- **logs/collection_log.txt** → Registro de las recolecciones para trazabilidad.  
- **Rol**: Centralizar la recolección institucional y garantizar la trazabilidad.

### 3. normalization/
- **data_normalization.py** → Normaliza los datos (fechas, cadenas, números, campos obligatorios, duplicados).  
- **Rol**: Estandarizar los datos para asegurar su compatibilidad con los módulos de conformidad y auditoría.

### 4. orchestration/
- **pipeline_orchestrator.py** → Orquestación del pipeline completo (recolección → normalización → conformidad → auditoría/scoring).  
- **Rol**: Garantizar el orden, la trazabilidad y la integración de las etapas.

### 5. schemas/
- **base_schema.py** → Esquema institucional genérico (id, timestamp, fuente, valor, metadatos).  
- **finance_schema.py** → Esquema para transacciones financieras.  
- **audit_schema.py** → Esquema para registros de auditoría.  
- **compliance_schema.py** → Esquema para validaciones regulatorias.  
- **Rol**: Definir estructuras de datos estandarizadas para todos los módulos, asegurando coherencia y auditabilidad.

---

## 📂 tests/
- **test_structure_validator.py** → Prueba la validación de conformidad documental.  
- **test_workflow_checker.py** → Prueba la validación de secuencias de workflow.  
- **test_pipeline_orchestrator.py** → Prueba la orquestación completa del pipeline.  
- **test_traceability.py** → Prueba el motor de trazabilidad institucional.  
- **test_utils.py** → Prueba las funciones utilitarias institucionales.  

---

## ⚙️ Requisitos
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions o pipelines en `infra_technical/ci-cd/`

---

## 📌 Buenas prácticas
- Respetar la nomenclatura trilingüe (`FR`, `EN`, `ES`) para guías, bitácoras y README técnicos.  
- Actualizar la `BITACORA` después de cada modificación.  
- Normalizar los datos antes de pasarlos a los módulos de conformidad, scoring y auditoría.  
- Usar `pipeline_orchestrator.py` como punto de entrada para garantizar orden y trazabilidad.  
- Centralizar los esquemas en `schemas/` para evitar divergencias entre módulos.  
- Ejecutar regularmente los tests unitarios para garantizar robustez y auditabilidad.  

---

## 📌 Conclusión
El submódulo `core/architecture` está ahora compuesto por cinco módulos clave (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`) y un **directorio `tests/`** que agrupa todos los archivos de validación (`test_structure_validator.py`, `test_workflow_checker.py`, `test_pipeline_orchestrator.py`, `test_traceability.py`, `test_utils.py`).  
Esta estructuración garantiza una gobernanza técnica robusta, conformidad documental, trazabilidad institucional y validación sistemática mediante tests unitarios.
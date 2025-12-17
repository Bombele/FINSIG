# GUÍA DE SUBMÓDULOS – core/architecture

---

## 🎯 Objetivo
Esta guía define la estructura y las responsabilidades de los submódulos dentro del directorio `core/architecture`.  
Garantiza la coherencia institucional, la trazabilidad y la auditabilidad en FINSIG.

---

## 📂 Submódulos

### 1. conformity/
- **structure_validator.py** → Verifica la presencia y conformidad de los archivos obligatorios.  
- **workflow_checker.py** → Controla la secuencia documental y la coherencia de los flujos.  
- **Rol**: Asegurar la conformidad institucional y documental.

### 2. collection/
- **data_collection.py** → Recolecta y valida datos brutos (CSV, JSON, API).  
- **logs/collection_log.txt** → Registro de las recolecciones para trazabilidad.  
- **Rol**: Centralizar la recolección institucional y garantizar la trazabilidad.

### 3. normalization/
- **data_normalization.py** → Normaliza los datos (fechas, cadenas, números, campos obligatorios, duplicados).  
- **Rol**: Estandarizar los datos para asegurar compatibilidad con los módulos de conformidad y auditoría.

### 4. orchestration/
- **pipeline_orchestrator.py** → Orquesta el pipeline completo (recolección → normalización → conformidad → auditoría/scoring).  
- **Rol**: Garantizar el orden, la trazabilidad y la integración de las etapas.

### 5. schemas/
- **base_schema.py** → Esquema institucional genérico (id, timestamp, source, valor, metadatos).  
- **finance_schema.py** → Esquema para transacciones financieras.  
- **audit_schema.py** → Esquema para registros de auditoría.  
- **compliance_schema.py** → Esquema para validaciones regulatorias.  
- **Rol**: Definir estructuras de datos estandarizadas para todos los módulos, asegurando coherencia y auditabilidad.

---

## ⚙️ Requisitos
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions o pipelines en `infra_technical/ci-cd/`

---

## 📌 Buenas prácticas
- Respetar la nomenclatura trilingüe (`FR`, `EN`, `ES`) para guías, bitácoras y README técnicos.  
- Actualizar la `BITACORA` después de cada modificación.  
- Normalizar los datos antes de pasarlos a los módulos de compliance, scoring y auditoría.  
- Usar `pipeline_orchestrator.py` como punto de entrada para garantizar el orden y la trazabilidad.  
- Centralizar los esquemas en `schemas/` para evitar divergencias entre módulos.  

---

## 📌 Conclusión
El submódulo `core/architecture` ahora está compuesto por cinco módulos clave: `conformity`, `collection`, `normalization`, `orchestration` y `schemas`.  
Esta estructuración garantiza una gobernanza técnica robusta, conformidad documental y trazabilidad institucional.
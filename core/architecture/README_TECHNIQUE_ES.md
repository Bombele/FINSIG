# README TÉCNICO – core/architecture

---

## 🎯 Objetivo
Este módulo define la arquitectura institucional de FINSIG.  
Garantiza la coherencia documental, la trazabilidad y la auditabilidad mediante submódulos, esquemas normalizados y pruebas unitarias.

---

## 📂 Submódulos

### 1. conformity/
- **structure_validator.py** → Verifica la presencia y conformidad de archivos obligatorios.  
- **workflow_checker.py** → Controla la secuencia documental y la coherencia de los workflows.  
- **Validación cruzada**: comprueba la integridad de las firmas SHA256 en `audit_schema.py` y `compliance_schema.py`.

### 2. collection/
- **data_collection.py** → Recolecta y valida datos brutos (CSV, JSON, API).  
- **logs/collection_log.txt** → Registro de las recolecciones para trazabilidad.

### 3. normalization/
- **data_normalization.py** → Normaliza datos (fechas, cadenas, números, campos obligatorios, duplicados).

### 4. orchestration/
- **pipeline_orchestrator.py** → Orquesta el pipeline completo (colección → normalización → conformidad → auditoría/scoring).  
- **Pruebas de dependencias**: asegura que cada etapa falle si la anterior no se ejecuta correctamente.

### 5. schemas/
- **base_schema.py** → Esquema genérico institucional.  
- **finance_schema.py** → Esquema para transacciones financieras.  
- **audit_schema.py** → Esquema para auditorías, incluye campos `version` y `signature` (SHA256).  
- **compliance_schema.py** → Esquema para validaciones regulatorias, incluye campos `version` y `signature` (SHA256).  
- **Función generate_signature()** → Genera firma criptográfica para garantizar integridad y autenticidad.

### 6. traceability/
- **traceability.py** → Motor de trazabilidad institucional.  
  - Registra eventos con horodatado en UTC (ISO 8601).  
  - Función `export_to_csv()` para exportar logs a CSV para auditoría externa.

### 7. utils/
- **utils.py** → Funciones utilitarias institucionales (validaciones, serialización JSON, merge de diccionarios, etc.).  
- Casos límite probados: valores `None`, cadenas inválidas, diccionarios vacíos.

---

## 📂 tests/
- **test_structure_validator.py** → Prueba la validación de conformidad documental.  
- **test_workflow_checker.py** → Prueba la validación de secuencias de workflow.  
- **test_pipeline_orchestrator.py** → Prueba la orquestación completa y errores de dependencias.  
- **test_traceability.py** → Prueba el motor de trazabilidad (UTC + exportación CSV).  
- **test_utils.py** → Prueba funciones utilitarias incluyendo casos límite.  
- **test_audit_schema.py** → Prueba generación y validación de firmas en auditorías.  
- **test_compliance_schema.py** → Prueba generación y validación de firmas en conformidad.

---

## 📂 workflows/
- **tests.yml** → Workflow GitHub Actions que ejecuta automáticamente `pytest` y cobertura de pruebas en cada commit y pull request.  
  - Python 3.10  
  - Dependencias: `pytest`, `pytest-cov`, `pydantic`  
  - Reporte de cobertura (`--cov=core/architecture --cov-report=term-missing`)

---

## ⚙️ Requisitos
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions (`.github/workflows/tests.yml`)

---

## 📌 Buenas prácticas
- Mantener documentación trilingüe (`FR`, `EN`, `ES`).  
- Actualizar la `BITACORA` tras cada modificación.  
- Normalizar datos antes de módulos de conformidad, scoring y auditoría.  
- Usar `pipeline_orchestrator.py` como punto de entrada.  
- Centralizar esquemas en `schemas/`.  
- Ejecutar pruebas unitarias regularmente y verificar cobertura.  
- Validar firmas SHA256 para garantizar integridad documental.  
- Exportar trazabilidad en UTC para auditoría externa.

---

## 📌 Conclusión
El módulo `core/architecture` está compuesto por submódulos robustos (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `traceability`, `utils`) y un conjunto completo de pruebas unitarias.  
La integración de **firmas SHA256**, **horodatado en UTC**, **exportación CSV** y **workflow CI/CD** asegura una gobernanza técnica sólida, trazabilidad institucional y validación sistemática.
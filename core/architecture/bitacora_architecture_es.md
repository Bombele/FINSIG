# BITACORA – core/architecture

---

## 📅 Registro de actividades

- **2025-12-17** – Actualización de `README_TECHNIQUE_ES.md` para incluir el módulo `schemas` junto con `conformity`, `collection`, `normalization` y `orchestration`.  
- **2025-12-17** – Creación de `base_schema.py` (módulo `schemas`) para definir el esquema institucional genérico.  
- **2025-12-17** – Creación de `finance_schema.py` (módulo `schemas`) para trazar transacciones financieras con conformidad ISO 4217.  
- **2025-12-17** – Creación de `audit_schema.py` (módulo `schemas`) para trazar registros de auditoría institucional.  
- **2025-12-17** – Creación de `compliance_schema.py` (módulo `schemas`) para trazar validaciones regulatorias e institucionales.  
- **2025-12-17** – Actualización de las `BITACORA` y `README_TECHNIQUE` en versiones trilingües (FR/EN/ES) para garantizar el onboarding internacional.  
- **2025-12-17** – Creación de `pipeline_orchestrator.py` (módulo `orchestration`) para orquestar el pipeline completo (recolección → normalización → conformidad → auditoría/scoring).  
- **2025-12-16** – Re-creación completa de `workflow_checker.py` para validar la secuencia documental trilingüe (guías, bitácoras, README técnicos).  
- **2025-12-16** – Actualización de `structure_validator.py` para reforzar la verificación de archivos obligatorios.  
- **2025-12-15** – Inicialización del submódulo `conformity/` con lógica de validación institucional.  
- **2025-12-14** – Estructuración inicial del submódulo `core/architecture` con guías y documentación.

---

## ✅ Estado de validaciones

- `structure_validator.py` y `workflow_checker.py` operativos y probados en local.  
- `data_collection.py` operativo, registro confirmado.  
- `data_normalization.py` operativo, pipeline de normalización probado.  
- `pipeline_orchestrator.py` operativo, orquestación completa validada.  
- `schemas/` operativo con esquemas validados (`base`, `finance`, `audit`, `compliance`).  
- Documentación técnica trilingüe (`FR`, `EN`, `ES`) en marcha para todos los módulos.  
- Bitácora actualizada para registrar las evoluciones.

---

## 📌 Notas técnicas

- Los validadores (`structure_validator.py`, `workflow_checker.py`) deben integrarse en los pipelines CI/CD (`infra_technical/ci-cd/`).  
- Los módulos deben ejecutarse en secuencia:  
  1. **Recolección** (`data_collection.py`)  
  2. **Normalización** (`data_normalization.py`)  
  3. **Conformidad** (`structure_validator.py`, `workflow_checker.py`)  
  4. **Orquestación** (`pipeline_orchestrator.py`)  
  5. **Schemas** (`base_schema.py`, `finance_schema.py`, `audit_schema.py`, `compliance_schema.py`) para garantizar la coherencia de los datos.  
- Cada submódulo debe contener:  
  - Guías trilingües (`FR`, `EN`, `ES`)  
  - Bitácoras trilingües (`FR`, `EN`, `ES`)  
  - README técnicos trilingües (`FR`, `EN`, `ES`)  
- Los archivos de registro deben colocarse en `logs/` y pueden ignorarse en `.gitignore` si no se versionan.  
- Los datos deben normalizarse y validarse mediante los esquemas antes de pasar a los módulos de compliance, scoring y auditoría.

---

## 📌 Conclusión

La bitácora `core/architecture` ahora traza la evolución completa del submódulo y sus módulos asociados (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`).  
Garantiza la trazabilidad institucional, la conformidad documental y la solidez técnica.
# BITACORA – core/architecture

---

## 📅 Registro de actividades

- **2025-12-17** – Actualización de `README_TECHNIQUE_ES.md` para incluir los módulos `collection`, `normalization` y `orchestration`.  
- **2025-12-17** – Creación de `data_collection.py` (módulo `collection`) para centralizar la recolección institucional de datos (CSV, JSON, API) con registro automático (`collection_log.txt`).  
- **2025-12-17** – Creación de `data_normalization.py` (módulo `normalization`) para normalizar datos (fechas, cadenas, números, campos obligatorios, duplicados).  
- **2025-12-17** – Creación de `pipeline_orchestrator.py` (módulo `orchestration`) para orquestar el pipeline completo (recolección → normalización → conformidad → auditoría/scoring).  
- **2025-12-17** – Actualización de las `BITACORA` y `README_TECHNIQUE` en versiones trilingües (FR/EN/ES) para garantizar el onboarding internacional.  
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
- Documentación técnica trilingüe (`FR`, `EN`, `ES`) en marcha para `architecture`, `collection`, `normalization` y `orchestration`.  
- Bitácora actualizada para registrar las evoluciones.

---

## 📌 Notas técnicas

- Los validadores (`structure_validator.py`, `workflow_checker.py`) deben integrarse en los pipelines CI/CD (`infra_technical/ci-cd/`).  
- Los módulos deben ejecutarse en secuencia:  
  1. **Recolección** (`data_collection.py`)  
  2. **Normalización** (`data_normalization.py`)  
  3. **Conformidad** (`structure_validator.py`, `workflow_checker.py`)  
  4. **Orquestación** (`pipeline_orchestrator.py`) para garantizar el orden y la trazabilidad.  
- Cada submódulo debe contener:  
  - Guías trilingües (`FR`, `EN`, `ES`)  
  - Bitácoras trilingües (`FR`, `EN`, `ES`)  
  - README técnicos trilingües (`FR`, `EN`, `ES`)  
- Los archivos de registro deben colocarse en `logs/` y pueden ignorarse en `.gitignore` si no se versionan.  
- Los datos deben normalizarse antes de pasarlos a los módulos de compliance, scoring y auditoría.

---

## 📌 Conclusión

La bitácora `core/architecture` ahora traza la evolución completa del submódulo y sus módulos asociados (`conformity`, `collection`, `normalization`, `orchestration`).  
Garantiza la trazabilidad institucional, la conformidad documental y la solidez técnica.
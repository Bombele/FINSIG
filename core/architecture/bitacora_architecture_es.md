# BITACORA – core/architecture

---

## 📅 Registro de actividades

- **2025-12-18** – Actualización de `audit_schema.py` y `compliance_schema.py` con campos `version` y `signature` (SHA256).  
- **2025-12-18** – Actualización de `structure_validator.py` para validar firmas y campos obligatorios de forma cruzada.  
- **2025-12-18** – Inclusión de la función `export_to_csv()` en `traceability.py` y uso uniforme de horodatado en UTC.  
- **2025-12-18** – Inclusión de pruebas unitarias `test_audit_schema.py` y `test_compliance_schema.py` para validación de firmas.  
- **2025-12-18** – Inclusión del workflow CI/CD `workflows/tests.yml` (pytest + cobertura).  
- **2025-12-18** – Mejora de `test_pipeline_orchestrator.py` con casos de errores de dependencias.  
- **2025-12-18** – Mejora de `test_utils.py` con casos límite (`None`, cadenas inválidas, diccionarios vacíos).  
- **2025-12-17** – Inclusión del módulo `schemas` y creación de archivos asociados.  
- **2025-12-17** – Actualización de las `BITACORA` y `README_TECHNIQUE` en versiones trilingües (FR/EN/ES).  
- **2025-12-17** – Creación de `pipeline_orchestrator.py`.  
- **2025-12-16** – Re-creación de `workflow_checker.py`.  
- **2025-12-16** – Actualización de `structure_validator.py`.  
- **2025-12-15** – Inicialización del submódulo `conformity/`.  
- **2025-12-14** – Estructuración inicial de `core/architecture`.

---

## ✅ Estado de validaciones

- Validadores operativos (`structure_validator.py`, `workflow_checker.py`).  
- Validación cruzada de firmas (`audit_schema`, `compliance_schema`).  
- Módulos de recolección y normalización probados.  
- Pipeline de orquestación validado (incluyendo errores de dependencias).  
- Esquemas validados (`base`, `finance`, `audit`, `compliance`).  
- Motor de scoring operativo.  
- Gestor de almacenamiento operativo.  
- Motor de trazabilidad operativo (UTC + exportación CSV).  
- Utilidades operativas (casos límite cubiertos).  
- Pruebas unitarias integradas (`pytest`).  
- Workflow CI/CD activo (`workflows/tests.yml`).  
- Documentación trilingüe en marcha.  
- Bitácora actualizada.

---

## 📌 Conclusión

La bitácora `core/architecture` ahora traza la evolución completa del submódulo y sus módulos (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`, `traceability`, `utils`) junto con sus **pruebas unitarias** y el **workflow CI/CD**.  
Garantiza trazabilidad institucional, conformidad documental, solidez técnica y auditabilidad confiable.
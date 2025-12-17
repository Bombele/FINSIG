# BITACORA – core/architecture/conformity

---

## 📅 Registro de actividades

- **2025-12-17** – Re-creación completa de `workflow_checker.py` para validar el flujo documental trilingüe (guías, bitácoras, README técnicos).  
- **2025-12-17** – Actualización de `structure_validator.py` para reforzar la verificación de archivos obligatorios.  
- **2025-12-17** – Incorporación de plantillas trilingües para `README_TECHNIQUE` con el fin de estandarizar la documentación técnica.  
- **2025-12-16** – Inicialización del submódulo `conformity/` con lógica de validación institucional.

---

## ✅ Estado de validaciones

- `workflow_checker.py` operativo y probado en local.  
- `structure_validator.py` validado, pendiente de integración en CI/CD.  
- Documentación técnica trilingüe en proceso de despliegue.  
- Bitácora actualizada para registrar las evoluciones.

---

## 📌 Notas técnicas

- Los validadores deben integrarse en los pipelines CI/CD (`infra_technical/ci-cd/`).  
- Cada submódulo debe contener: guías, bitácoras y README técnicos en FR/EN/ES.  
- Los scripts de conformidad deben ejecutarse antes de cada merge para garantizar la solidez documental.

# BITACORA – core/architecture/modules/collection

---

## 📅 Registro de actividades

- **2025-12-17** – Creación de `data_collection.py` para centralizar la recolección institucional de datos (CSV, JSON, API).  
- **2025-12-17** – Implementación de la lógica de validación (presencia del campo `id`) y registro automático en `collection_log.txt`.  
- **2025-12-17** – Recomendación de crear una carpeta `logs/` para almacenar archivos de seguimiento y mantener limpia la raíz.  
- **2025-12-16** – Inicialización del submódulo `collection/` con lógica de recolección y trazabilidad.

---

## ✅ Estado de validaciones

- `data_collection.py` operativo y probado en local.  
- Registro automático confirmado (`collection_log.txt` generado en la primera ejecución).  
- Carpeta `logs/` recomendada para mejor organización.  
- Bitácora actualizada para registrar las evoluciones.

---

## 📌 Notas técnicas

- Los archivos de registro deben colocarse en `logs/` y pueden ignorarse en `.gitignore` si no se versionan.  
- Cada recolección debe validarse antes de integrarse en los módulos de compliance y auditoría.  
- Próximos pasos incluyen:  
  - Añadir reglas de validación avanzadas (formato, campos obligatorios).  
  - Integración con `infra-technical/checks` para automatizar la conformidad.
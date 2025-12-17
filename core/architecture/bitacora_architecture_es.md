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
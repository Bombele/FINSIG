# BITÁCORA – infra_technical/ci-cd

---

## 📅 Registro de actividades

- **2025-12-18** – Creación del workflow `tests.yml` (pytest + cobertura).  
- **2025-12-18** – Creación del workflow `lint.yml` (flake8 + bandit) para control de calidad y seguridad.  
- **2025-12-18** – Creación del workflow `build.yml` (empaquetado Python + verificación de instalabilidad).  
- **2025-12-18** – Creación del workflow `docker.yml` (construcción y push de la imagen Docker hacia GHCR).  
- **2025-12-18** – Creación del workflow `deploy.yml` (despliegue en staging mediante docker-compose).  
- **2025-12-18** – Creación del workflow global `ci.yml` que orquesta todo el pipeline.  
- **2025-12-18** – Adición de un `docker-compose.yml` robusto (app, db, exporters, monitoreo).  
- **2025-12-18** – Adición de `prometheus.yml` y `alert_rules.yml` para monitoreo y alertas críticas.  
- **2025-12-18** – Actualización de los README técnicos (`README_TECHNIQUE_FR.md`, `README_TECHNIQUE_EN.md`, `README_TECHNIQUE_ES.md`).  
- **2025-12-18** – Actualización de la bitácora CI/CD (ES) para trazabilidad institucional.  

---

## ✅ Estado de validaciones

- Workflows CI/CD operativos (`tests.yml`, `lint.yml`, `build.yml`, `docker.yml`, `deploy.yml`, `ci.yml`).  
- Pruebas unitarias ejecutadas con cobertura.  
- Lint y seguridad validados (flake8 + bandit).  
- Empaquetado Python funcional (wheel + sdist).  
- Imagen Docker construida y enviada a GHCR.  
- Despliegue en staging operativo mediante `docker-compose`.  
- Monitoreo Prometheus activo con exporters (`postgres-exporter`, `node-exporter`).  
- Alertas críticas configuradas (`finsig-app down`, `postgres down`, uso alto de CPU/memoria).  
- Documentación trilingüe disponible (FR/EN/ES).  
- Bitácora CI/CD actualizada y alineada con las evoluciones.  

---

## 📌 Conclusión

La bitácora `infra_technical/ci-cd` registra la evolución completa del módulo CI/CD de FINSIG.  
Garantiza una **trazabilidad institucional**, una **robustez técnica**, una **seguridad reforzada** y una **auditabilidad confiable**.  
Este pipeline CI/CD constituye la **columna vertebral operativa** de FINSIG, demostrando su capacidad para ser probado, asegurado, empaquetado, contenerizado, desplegado y monitoreado de manera **fiable y transparente**.
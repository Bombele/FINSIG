# README Técnico – Pipeline CI/CD de FINSIG

---

## 🎯 Objetivo

El pipeline CI/CD de FINSIG está diseñado para garantizar la **robustez**, la **trazabilidad** y la **auditabilidad** del proyecto.  
Cada etapa asegura la calidad del código, la reproducibilidad de los entornos y la continuidad operativa, incluso en contextos de crisis.

---

## 🔎 Etapas principales

### 1. **Tests (`tests.yml`)**
- Ejecución de pruebas unitarias con `pytest`.
- Cálculo de la cobertura con `pytest-cov`.
- Generación de informes para auditoría externa.

### 2. **Lint & Seguridad (`lint.yml`)**
- Verificación del estilo y complejidad del código con `flake8`.
- Análisis de seguridad con `bandit` para detectar vulnerabilidades.
- Garantía de cumplimiento técnico y calidad del código.

### 3. **Build & Packaging (`build.yml`)**
- Generación de artefactos Python (`wheel`, `sdist`) mediante `python -m build`.
- Verificación de instalabilidad (`pip install dist/*.whl`).
- Upload de artefactos para auditoría y distribución.

### 4. **Dockerización (`docker.yml`)**
- Construcción de la imagen Docker con `docker build`.
- Push automático al GitHub Container Registry (GHCR).
- Portabilidad y reproducibilidad garantizadas.

### 5. **Despliegue Staging (`deploy.yml`)**
- Simulación de despliegue mediante `docker-compose`.
- Servicios incluidos: aplicación FINSIG, base de datos Postgres, monitoreo Prometheus.
- Healthchecks integrados para asegurar disponibilidad y auditabilidad.

---

## ✅ Resultados esperados

- **Robustez** validada por pruebas unitarias y cobertura.  
- **Calidad y seguridad** garantizadas mediante lint y análisis estático.  
- **Portabilidad** a través de empaquetado Python e imágenes Docker.  
- **Reproducibilidad** gracias a Docker Compose y CI/CD automatizado.  
- **Auditabilidad** reforzada por informes de cobertura, artefactos generados y métricas de Prometheus.  

---

## 📌 Conclusión

Este pipeline CI/CD constituye la **columna vertebral técnica** de FINSIG.  
Demuestra la capacidad del proyecto para ser probado, asegurado, empaquetado, contenerizado y desplegado de manera **fiable y transparente**.  
Es un elemento clave para la credibilidad institucional y la validación por parte de socios o reguladores.
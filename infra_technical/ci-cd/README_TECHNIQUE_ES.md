# README TÉCNICO – Pipeline CI/CD de FINSIG

---

## 🎯 Propósito

El módulo CI/CD garantiza la **robustez**, la **trazabilidad** y la **auditabilidad** de la infraestructura técnica de FINSIG.  
Permite probar, empaquetar, desplegar y monitorear los componentes en un entorno reproducible y conforme.  
Este pipeline está diseñado para operar de manera confiable incluso bajo condiciones críticas, reforzando la credibilidad institucional.

---

## 📂 Estructura General

### 🔧 `configs/`
- `pyproject.toml` → Metadatos del proyecto, dependencias y configuración de herramientas (pytest, flake8, mypy, bandit).  
- `requirements.txt` → Lista de dependencias organizadas: núcleo, desarrollo, CI/CD y monitoreo.  
- `pytest.ini` → Estandariza descubrimiento de pruebas, reportes de cobertura, salida JUnit y formato de logs.  
- `mypy.ini` → Verificación estricta de tipos, códigos de error y soporte de plugins (`pydantic.mypy`).

### ⚙️ `workflows/`
- `ci.yml` → Orquestación global de todas las etapas CI/CD.  
- `tests.yml` → Ejecución de pruebas unitarias con cobertura.  
- `lint.yml` → Control de calidad y seguridad del código.  
- `build.yml` → Empaquetado Python y verificación de instalabilidad.  
- `docker.yml` → Construcción y push de imágenes Docker a GHCR.  
- `deploy.yml` → Simulación de despliegue en staging mediante Docker Compose.

### 📈 Monitoreo y Alertas
- `prometheus.yml` → Configuración de Prometheus para recolectar métricas de la app, base de datos y exporters.  
- `alert_rules.yml` → Reglas de alerta críticas (app caída, DB caída, uso alto de CPU/memoria).  
- `docker-compose.yml` → Despliegue de app, Postgres, exporters y Prometheus en entorno staging local.

### 🧪 Pruebas y Validación
- `tests/` → Pipelines de validación (`test_ci.yml`, `test_lint.yml`, `test_build.yml`) y pruebas de utilitarios (`test_ci_cd_utils.py`).  
- `schemas/` → Esquema de validación de workflows y artefactos (`ci_cd_schema.json`).  
- `utils/` → Funciones reutilizables para logs, hash y marcas de tiempo (`ci_cd_utils.py`).

### 📚 Documentación
- `README_TECHNIQUE_FR.md / EN / ES` → Documentación técnica trilingüe.  
- `BITACORA_CI-CD_FR.md / EN / ES` → Registro institucional de la evolución CI/CD.  
- `CI_CD_GUIDE.md` → Principios de diseño, metodología y gobernanza de workflows CI/CD.

---

## 🔄 Etapas del Pipeline

1. **Pruebas**  
   - Ejecución de pruebas unitarias con `pytest`.  
   - Medición de cobertura y exportación de reportes (`coverage.xml`, `test-results.xml`).

2. **Linting y Seguridad**  
   - Reglas de estilo con `flake8`.  
   - Análisis de vulnerabilidades con `bandit`.  
   - Verificación estática de tipos con `mypy`.

3. **Build y Empaquetado**  
   - Generación de artefactos Python (`wheel`, `sdist`).  
   - Verificación de instalabilidad y reproducibilidad.

4. **Dockerización**  
   - Construcción de imagen Docker.  
   - Push a GitHub Container Registry (GHCR).

5. **Despliegue en Staging**  
   - Simulación completa mediante `docker-compose`.  
   - Incluye app, base de datos, exporters y monitoreo.

6. **Monitoreo y Alertas**  
   - Prometheus recolecta métricas.  
   - Alertas críticas activadas ante fallos o sobrecarga de recursos.

---

## ✅ Impacto Institucional

- **Robustez** → Validada mediante pruebas y empaquetado automatizado.  
- **Conformidad** → Garantizada por linting, tipado y análisis de seguridad.  
- **Auditabilidad** → Reportes de cobertura, JUnit y métricas Prometheus exportables.  
- **Reproducibilidad** → Asegurada por Docker y configuraciones estandarizadas.  
- **Resiliencia** → Monitoreo y alertas integrados para continuidad operativa.  
- **Credibilidad** → Documentación trilingüe y bitácoras para validación externa.

---

## 📌 Conclusión

Este pipeline CI/CD es la **columna vertebral técnica de FINSIG**.  
Demuestra la capacidad del proyecto para ser probado, asegurado, empaquetado, desplegado y monitoreado de manera **transparente y auditable**.  
Es un activo estratégico para la validación institucional, la integración de socios y el cumplimiento regulatorio.
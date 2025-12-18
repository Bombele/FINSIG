# README TÉCNICO – Pipeline CI/CD de FINSIG

---

## 🎯 Propósito

El módulo CI/CD garantiza la **robustez**, la **trazabilidad** y la **auditabilidad** de la infraestructura técnica de FINSIG.  
Permite pruebas controladas, empaquetado, despliegue y monitoreo de todos los componentes en un entorno reproducible y conforme.  
El pipeline está diseñado para operar de manera confiable incluso bajo crisis o restricciones geopolíticas, reforzando la credibilidad institucional.

---

## 📂 Estructura General

### 🔧 `configs/`
- `pyproject.toml` → metadatos del proyecto, dependencias y configuraciones de herramientas (pytest, flake8, mypy, bandit, docker, prometheus-client).  
- `requirements.txt` → lista jerárquica de dependencias (core, dev, CI/CD, monitoreo).  
- `pytest.ini` → descubrimiento estandarizado de pruebas, reportes de cobertura, salida JUnit y logs con timestamp.  
- `mypy.ini` → tipado estricto, códigos de error y soporte de plugins (`pydantic.mypy`).

### ⚙️ `.github/workflows/`
- `build-validation.yml` → valida empaquetado Python (wheel + sdist), instalabilidad y artefactos auditables.  
- `lint-validation.yml` → ejecuta flake8, bandit y mypy para calidad, seguridad y tipado.  
- `tests-validation.yml` → ejecuta pruebas unitarias con cobertura y reportes JUnit.  
- `security-check.yml` → escanea código y dependencias en busca de vulnerabilidades (bandit + safety).  
- `deploy-validation.yml` → simula despliegue staging vía Docker Compose con healthchecks y Prometheus.  
- `lint-check.yml` → linting ligero y chequeo de tipado para retroalimentación rápida.  
- `ci-validation.yml` → orquesta todos los workflows de validación en paralelo.

### 📈 Monitoreo y Orquestación
- `prometheus.yml` → scraping de métricas de la app, base de datos y exporters.  
- `alert_rules.yml` → define alertas críticas (app caída, DB caída, CPU/memoria altas).  
- `docker-compose.yml` → despliega app, Postgres, exporters y Prometheus en entorno staging local.

### 🧪 Pruebas y Validación
- `tests/` → workflows de prueba consolidados:  
  - `test_build.yml` → valida empaquetado e instalabilidad.  
  - `test_deploy.yml` → valida despliegue staging y healthchecks.  
  - `test_security.yml` → valida vulnerabilidades en código y dependencias.  
  - `test_lint.yml` → valida estilo, tipado y seguridad.  
  - `test_ci.yml` → orquesta todos los workflows de prueba en paralelo.  
  - `test_ci_cd_utils.py` → valida funciones utilitarias (hash, logs, timestamps, validación de artefactos).  
- `schemas/` → esquema de validación de workflows y artefactos (`ci_cd_schema.json`).  
- `utils/` → funciones reutilizables para logging, hashing y timestamps (`ci_cd_utils.py`).

### 📚 Documentación
- `README_TECHNIQUE_FR.md / EN / ES` → visión técnica trilingüe.  
- `BITACORA_CI-CD_FR.md / EN / ES` → registro institucional de la evolución del CI/CD.  
- `CI_CD_GUIDE.md` → principios de diseño, metodología y gobernanza de los workflows CI/CD.

### 📁 reports/
Contiene **reportes generados automáticamente** por los workflows CI/CD:  
- `coverage.xml` → reporte de cobertura de pruebas.  
- `test-results.xml` → reporte JUnit de pruebas unitarias.  
- `lint-report.txt` → reporte flake8/mypy.  
- `security-report.json` → reporte bandit/safety.  
- `deploy-report.log` → reporte del despliegue staging (healthchecks).  

👉 Estos archivos garantizan la **auditabilidad de los controles**.

### 📁 artifacts/
Contiene **productos finales y evidencias institucionales**:  

#### 🔧 Build
- `finsig-<version>-py3-none-any.whl`  
- `finsig-<version>.tar.gz`  

#### 🐳 Docker
- `docker-image-sha256.txt` → hash SHA256 de la imagen Docker.  
- `docker-image.tar` → export local de la imagen (opcional).  

#### 📜 Logs
- `ci_cd_events.log` → registro de eventos CI/CD.  
- `deploy-report.log` → reporte del despliegue staging.  

#### 🔒 Hashes
- `build-hash.txt` → hash SHA256 de los paquetes Python.  
- `docker-hash.txt` → hash SHA256 de la imagen Docker.  

#### ✅ Validación
- `artifact-validation.json` → archivo conforme al esquema `ci_cd_schema.json`, listando artefactos, hash y estado de validación.  

👉 Estos archivos garantizan la **trazabilidad institucional y validación externa**.

---

## 🔄 Etapas del Pipeline

1. **Pruebas**  
   - Ejecutar pruebas unitarias con `pytest`.  
   - Medir cobertura y exportar reportes (`coverage.xml`, `test-results.xml`).

2. **Linting y Seguridad**  
   - Validar estilo con `flake8`.  
   - Detectar vulnerabilidades con `bandit` y `safety`.  
   - Aplicar tipado estático con `mypy`.

3. **Build y Empaquetado**  
   - Generar artefactos Python (`wheel`, `sdist`).  
   - Verificar instalabilidad y reproducibilidad.

4. **Dockerización**  
   - Construir imagen Docker.  
   - Publicar en GitHub Container Registry (GHCR).

5. **Despliegue Staging**  
   - Simular entorno completo vía `docker-compose`.  
   - Incluye app, base de datos, exporters y monitoreo.  
   - Healthchecks en app, DB y Prometheus.

6. **Monitoreo y Alertas**  
   - Prometheus recolecta métricas.  
   - Alertas críticas se disparan ante fallos o umbrales de recursos.

---

## ✅ Impacto Institucional

- **Robustez** → validada mediante pruebas y empaquetado automatizado.  
- **Cumplimiento** → garantizado con linting, tipado y escaneo de seguridad.  
- **Auditabilidad** → reportes exportables de cobertura, JUnit y Prometheus.  
- **Reproducibilidad** → asegurada por Docker y configuraciones estandarizadas.  
- **Resiliencia** → monitoreo y alertas garantizan continuidad operativa.  
- **Credibilidad** → documentación trilingüe y bitácoras respaldan validación externa.

---

## 📌 Conclusión

Este pipeline CI/CD es la **columna vertebral técnica de FINSIG**.  
Demuestra la capacidad del proyecto para ser probado, asegurado, empaquetado, desplegado y monitoreado de manera **transparente y auditable**.  
Con la adición de los directorios **`reports/`** y **`artifacts/`**, la trazabilidad institucional está completa:  
- `reports/` → resultados de controles.  
- `artifacts/` → productos finales y evidencias institucionales.  
Es un activo estratégico para la validación institucional, la incorporación de socios y el cumplimiento regulatorio.
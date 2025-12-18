# README TÉCNICO – Pipeline CI/CD de FINSIG

---

## 🎯 Propósito

El módulo CI/CD garantiza la **robustez**, **trazabilidad** y **auditabilidad** de la infraestructura técnica de FINSIG.  
Permite probar, empaquetar, desplegar y monitorear todos los componentes en un entorno reproducible y conforme a estándares.  
El pipeline está diseñado para funcionar de manera confiable incluso en contextos de crisis o restricciones, reforzando la credibilidad institucional.

---

## 📂 Estructura general

### ⚙️ configs/
- `pyproject.toml` → Metadatos del proyecto, dependencias y configuraciones de herramientas (pytest, flake8, mypy, bandit, docker, prometheus-client).  
- `requirements.txt` → Lista jerárquica de dependencias (core, dev, CI/CD, monitoreo).  
- `pytest.ini` → Descubrimiento estandarizado de pruebas, reportes de cobertura, salida JUnit y logs con marcas de tiempo.  
- `mypy.ini` → Verificación estricta de tipos, códigos de error y soporte de plugins (`pydantic.mypy`).  

### ⚙️ .github/workflows/
- `build-validation.yml` → Valida empaquetado Python (wheel + sdist), instalabilidad y artefactos de auditoría.  
- `lint-validation.yml` → Ejecuta flake8, bandit y mypy para calidad, seguridad y tipado.  
- `tests-validation.yml` → Ejecuta pruebas unitarias con cobertura y reportes JUnit.  
- `security-check.yml` → Escanea código y dependencias en busca de vulnerabilidades (bandit + safety).  
- `docker-pipeline.yml` → Construye y publica la imagen Docker en GHCR.  
- `deploy-validation.yml` → Simula despliegue en staging vía Docker Compose con healthchecks y Prometheus.  
- `ci-validation.yml` → Orquesta todos los workflows de validación en paralelo.  

### 📊 Monitoreo y orquestación
- `prometheus.yml` → Configura métricas de app, base de datos y exporters.  
- `alert_rules.yml` → Define alertas críticas (app caída, DB caída, alto CPU/memoria).  
- `docker-compose.yml` → Despliega app, Postgres, exporters y Prometheus en entorno local de staging.  

### 🧪 Pruebas y validación
- `tests/` → Workflows de prueba: build, deploy, seguridad, lint, CI orquestado.  
- `schemas/` → Esquema de validación de workflows y artefactos (`ci_cd_schema.json`).  
- `utils/` → Funciones reutilizables para logs, hash y marcas de tiempo (`ci_cd_utils.py`).  

### 📚 Documentación
- `README_TECHNIQUE_ES.md / FR / EN` → Visión técnica trilingüe.  
- `BITACORA_CI-CD_ES.md / FR / EN` → Bitácora institucional de evolución CI/CD.  
- `CI_CD_GUIDE.md` → Principios de diseño, metodología y gobernanza de los workflows CI/CD.  

### 📂 reports/
Contiene **informes generados automáticamente** por los workflows CI/CD:  
- `coverage.xml` → informe de cobertura de pruebas.  
- `test-results.xml` → informe JUnit de pruebas unitarias.  
- `lint-report.txt` → informe flake8/mypy.  
- `security-report.json` → informe bandit/safety.  
- `deploy-report.log` → informe de despliegue en staging (healthchecks).  

👉 Estos archivos aseguran la **auditabilidad de los controles**.

### 📂 artifacts/
Contiene **productos finales y pruebas institucionales**:  
- Build → `finsig-<versión>-py3-none-any.whl`, `finsig-<versión>.tar.gz`.  
- Docker → `docker-image-sha256.txt`, `docker-image.tar`.  
- Logs → `ci_cd_events.log`, `deploy-report.log`.  
- Hashes → `build-hash.txt`, `docker-hash.txt`.  
- Validación → `artifact-validation.json` (conforme a `ci_cd_schema.json`).  

👉 Estos archivos aseguran la **trazabilidad institucional y validación externa**.

### 📂 scripts/
Contiene **scripts de orquestación CI/CD** para reproducción local y validación offline:  
- `build.sh` → Genera artefactos Python y valida con Twine.  
- `docker.sh` → Construye imagen Docker, exporta tar, genera hashes y archivos de prueba.  
- `reports.sh` → Ejecuta pruebas, cobertura, lint y auditorías de seguridad.  
- `validate.sh` → Genera `artifact-validation.json` dinámico con estados PASSED/FAILED.  
- `setup_pipeline.sh` → Instala dependencias, prepara carpetas y orquesta ejecución completa del pipeline.  
- `pipeline.sh` → Ejecuta todos los scripts secuencialmente para reproducir el pipeline CI/CD localmente.  

👉 Estos scripts proporcionan **auditabilidad offline** y demuestran autonomía institucional.

---

## 🔄 Etapas del pipeline

1. **Pruebas** → Unitarias, cobertura, reportes JUnit.  
2. **Linting y seguridad** → flake8, mypy, bandit, safety.  
3. **Build y empaquetado** → wheel + sdist, verificaciones de reproducibilidad.  
4. **Dockerización** → Construcción y push de imagen a GHCR.  
5. **Despliegue en staging** → Entorno completo vía docker-compose, healthchecks.  
6. **Monitoreo y alertas** → Métricas Prometheus, reglas de alerta.  
7. **Validación** → `artifact-validation.json` dinámico con trazabilidad institucional.

---

## ✅ Impacto institucional

- **Robustez** → Pruebas y empaquetado automatizados.  
- **Conformidad** → Garantizada por linting, tipado y escaneos de seguridad.  
- **Auditabilidad** → Informes y artefactos de validación exportables.  
- **Reproducibilidad** → Garantizada por Docker y configuraciones estandarizadas.  
- **Resiliencia** → Monitoreo y alertas aseguran continuidad operativa.  
- **Credibilidad** → Documentación trilingüe y bitácoras respaldan validación externa.  
- **Autonomía** → Carpeta scripts/ asegura reproducibilidad incluso offline.

---

## 📌 Conclusión

Este pipeline CI/CD es la **columna vertebral técnica de FINSIG**.  
Demuestra la capacidad del proyecto para ser probado, asegurado, empaquetado, desplegado y monitoreado de manera **transparente y auditable**.  
Con la adición de **reports/**, **artifacts/** y **scripts/**, la trazabilidad institucional es completa:  
- reports/ → resultados de controles.  
- artifacts/ → productos finales y pruebas institucionales.  
- scripts/ → reproducción local, validación dinámica, auditabilidad offline.
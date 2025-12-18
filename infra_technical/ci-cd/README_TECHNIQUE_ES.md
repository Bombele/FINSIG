# README TÉCNICO – Pipeline CI/CD de FINSIG

---

## 🎯 Propósito

Este módulo CI/CD garantiza la **robustez**, la **trazabilidad** y la **auditabilidad** de la infraestructura técnica de FINSIG.  
Permite pruebas controladas, empaquetado, despliegue y monitoreo de todos los componentes en un entorno reproducible y conforme.  
El pipeline está diseñado para operar de manera confiable incluso bajo restricciones geopolíticas, reforzando la credibilidad institucional.

---

## 📂 Estructura General

### 🔧 `configs/`
- `pyproject.toml` → Metadatos del proyecto, dependencias y configuraciones de herramientas (pytest, flake8, mypy, bandit, docker, prometheus-client).  
- `requirements.txt` → Lista jerárquica de dependencias (core, dev, CI/CD, monitoreo).  
- `pytest.ini` → Descubrimiento estandarizado de pruebas, reportes de cobertura, salida JUnit y logs con timestamp.  
- `mypy.ini` → Tipado estricto, códigos de error y soporte de plugins (`pydantic.mypy`).

### ⚙️ `.github/workflows/`
- `build-validation.yml` → Valida empaquetado Python (wheel + sdist), instalabilidad y artefactos auditables.  
- `lint-validation.yml` → Ejecuta flake8, bandit y mypy para calidad, seguridad y tipado.  
- `tests-validation.yml` → Ejecuta pruebas unitarias con cobertura y reportes JUnit.  
- `security-check.yml` → Escanea código y dependencias en busca de vulnerabilidades (bandit + safety).  
- `deploy-validation.yml` → Simula despliegue staging vía Docker Compose con healthchecks y Prometheus.  
- `lint-check.yml` → Linting ligero y chequeo de tipado para retroalimentación rápida.  
- `ci-validation.yml` → Orquesta todos los workflows de validación en paralelo.

### 📈 Monitoreo y Orquestación
- `prometheus.yml` → Configura scraping de métricas de la app, base de datos y exporters.  
- `alert_rules.yml` → Define alertas críticas (app caída, DB caída, CPU/memoria altas).  
- `docker-compose.yml` → Despliega app, Postgres, exporters y Prometheus en entorno staging local.

### 🧪 Pruebas y Validación
- `tests/` → Workflows de prueba consolidados:  
  - `test_build.yml` → valida empaquetado e instalabilidad.  
  - `test_deploy.yml` → valida despliegue staging y healthchecks.  
  - `test_security.yml` → valida vulnerabilidades en código y dependencias.  
  - `test_lint.yml` → valida estilo, tipado y seguridad rápida.  
  - `test_ci.yml` → orquesta todos los workflows de prueba en paralelo.  
  - `test_ci_cd_utils.py` → valida funciones utilitarias (hash, logs, timestamps, validación de artefactos).  
- `schemas/` → Esquema de validación de workflows y artefactos (`ci_cd_schema.json`).  
- `utils/` → Funciones reutilizables para logging, hashing y timestamp (`ci_cd_utils.py`).

### 📚 Documentación
- `README_TECHNIQUE_FR.md / EN / ES` → Visión técnica trilingüe.  
- `BITACORA_CI-CD_FR.md / EN / ES` → Registro institucional de la evolución del CI/CD.  
- `CI_CD_GUIDE.md` → Principios de diseño, metodología y gobernanza de los workflows CI/CD.

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

- **Robustez** → Validada mediante pruebas y empaquetado automatizado.  
- **Cumplimiento** → Garantizado con linting, tipado y escaneo de seguridad.  
- **Auditabilidad** → Reportes exportables de cobertura, JUnit y Prometheus.  
- **Reproducibilidad** → Asegurada por Docker y configuraciones estandarizadas.  
- **Resiliencia** → Monitoreo y alertas garantizan continuidad operativa.  
- **Credibilidad** → Documentación trilingüe y bitácoras respaldan validación externa.

---

## 📌 Conclusión

Este pipeline CI/CD es la **columna vertebral técnica de FINSIG**.  
Demuestra la capacidad del proyecto para ser probado, asegurado, empaquetado, desplegado y monitoreado de manera **transparente y auditable**.  
Es un activo estratégico para la validación institucional, la incorporación de socios y el cumplimiento regulatorio.
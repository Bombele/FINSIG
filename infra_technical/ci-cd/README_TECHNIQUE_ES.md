# README TÉCNICO – Pipeline CI/CD de FINSIG

---

## 🎯 Propósito

Este módulo CI/CD garantiza la **robustez**, la **trazabilidad** y la **auditabilidad** de la infraestructura técnica de FINSIG.  
Permite probar, empaquetar, desplegar y monitorear los componentes en un entorno reproducible y conforme.  
Está diseñado para operar de forma confiable incluso bajo restricciones geopolíticas, reforzando la credibilidad institucional.

---

## 📂 Estructura General

### 🔧 `configs/`
- `pyproject.toml` → Metadatos del proyecto, dependencias y configuración de herramientas (pytest, flake8, mypy, bandit, docker, prometheus-client).  
- `requirements.txt` → Lista jerárquica de dependencias (núcleo, desarrollo, CI/CD, monitoreo).  
- `pytest.ini` → Estandarización de pruebas, reportes de cobertura, salida JUnit y logs con timestamp.  
- `mypy.ini` → Tipado estricto, códigos de error, soporte de plugins (`pydantic.mypy`).

### ⚙️ `.github/workflows/`
- `build-validation.yml` → Valida el empaquetado Python (`wheel`, `sdist`), instalabilidad y artefactos para auditoría.  
- `lint-validation.yml` → Ejecuta flake8, bandit y mypy para calidad, seguridad y tipado.  
- `tests-validation.yml` → Ejecuta pruebas unitarias con cobertura y reportes JUnit.  
- `security-check.yml` → Escanea vulnerabilidades en el código y dependencias (bandit + safety).  
- `deploy-validation.yml` → Simula despliegue en staging con Docker Compose, healthchecks y monitoreo Prometheus.  
- `lint-check.yml` → Validación rápida de estilo y tipado.  
- `ci-validation.yml` → Orquesta todos los workflows en paralelo.

### 📈 Monitoreo y Orquestación
- `prometheus.yml` → Recolección de métricas desde app, base de datos y exporters.  
- `alert_rules.yml` → Reglas de alerta críticas (app caída, DB caída, CPU/memoria elevada).  
- `docker-compose.yml` → Despliegue local de app, Postgres, exporters y Prometheus.

### 🧪 Pruebas y Validación
- `tests/` → Pipelines de validación (`test_ci.yml`, `test_lint.yml`, `test_build.yml`) y pruebas de utilitarios (`test_ci_cd_utils.py`).  
- `schemas/` → Esquema de validación de workflows y artefactos (`ci_cd_schema.json`).  
- `utils/` → Funciones reutilizables para logs, hash y marcas de tiempo (`ci_cd_utils.py`).

### 📚 Documentación
- `README_TECHNIQUE_FR.md / EN / ES` → Documentación técnica trilingüe.  
- `BITACORA_CI-CD_FR.md / EN / ES` → Registro institucional de evolución CI/CD.  
- `CI_CD_GUIDE.md` → Principios de diseño, metodología y gobernanza.

---

## 🔄 Etapas del Pipeline

1. **Pruebas**  
   - Ejecución de pruebas unitarias con `pytest`.  
   - Cobertura medida y reportes exportados (`coverage.xml`, `test-results.xml`).

2. **Linting y Seguridad**  
   - Reglas de estilo con `flake8`.  
   - Vulnerabilidades detectadas con `bandit` y `safety`.  
   - Tipado estático con `mypy`.

3. **Build y Empaquetado**  
   - Generación de artefactos Python (`wheel`, `sdist`).  
   - Verificación de instalabilidad y reproducibilidad.

4. **Dockerización**  
   - Construcción de imagen Docker.  
   - Push hacia GitHub Container Registry (GHCR).

5. **Despliegue en Staging**  
   - Simulación completa vía `docker-compose`.  
   - Incluye app, base de datos, exporters y monitoreo.  
   - Healthchecks sobre app, DB y Prometheus.

6. **Monitoreo y Alertas**  
   - Prometheus recolecta métricas.  
   - Alertas críticas activadas ante fallos o sobrecarga.

---

## ✅ Impacto Institucional

- **Robustez** → Validada mediante pruebas y empaquetado automatizado.  
- **Conformidad** → Garantizada por linting, tipado y escaneo de seguridad.  
- **Auditabilidad** → Reportes de cobertura, JUnit y Prometheus exportables.  
- **Reproducibilidad** → Asegurada por Docker y configuraciones estandarizadas.  
- **Resiliencia** → Monitoreo y alertas aseguran continuidad operativa.  
- **Credibilidad** → Documentación trilingüe y bitácoras fortalecen la validación externa.

---

## 📌 Conclusión

Este pipeline CI/CD es la **columna vertebral técnica de FINSIG**.  
Demuestra la capacidad del proyecto para ser probado, asegurado, empaquetado, desplegado y monitoreado de forma **transparente y auditable**.  
Es un activo estratégico para la validación institucional, la integración de socios y el cumplimiento regulatorio.
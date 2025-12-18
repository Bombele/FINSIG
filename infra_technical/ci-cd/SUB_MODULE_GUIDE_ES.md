# GUÍA DEL SUB-MÓDULO – CI/CD

---

## 🎯 Objetivo del sub-módulo

El sub-módulo `ci-cd/` está dedicado al **desarrollo, experimentación y fortalecimiento de los workflows CI/CD**.  
Permite probar, validar y mejorar las configuraciones antes de su integración oficial en la rama principal `finsig/`.

---

## 📂 Estructura de directorios

### 📂 docs/
- **CI_CD_GUIDE.md** → principios de diseño de los workflows CI/CD, metodología y estándares institucionales.  
- **README_TECHNIQUE_FR.md / EN / ES** → documentación trilingüe del pipeline CI/CD.  
- **BITACORA_CI-CD_FR.md / EN / ES** → registro institucional de las evoluciones del CI/CD.

### 📂 workflows/
- **ci.yml** → pipeline global de integración continua.  
- **tests.yml** → ejecución de pruebas unitarias con cobertura.  
- **lint.yml** → verificación del código (flake8 + bandit).  
- **build.yml** → empaquetado Python y verificación de instalabilidad.  
- **docker.yml** → construcción y push de la imagen Docker hacia GHCR.  
- **deploy.yml** → despliegue staging vía docker-compose.  
- **prometheus.yml** → configuración de monitoreo con Prometheus.  
- **alert_rules.yml** → reglas de alerta críticas (app caída, DB caída, CPU/memoria).  
- **docker-compose.yml** → entorno completo (app, db, exporters, monitoreo).

### 📂 configs/
- **pyproject.toml** → definición de dependencias Python.  
- **requirements.txt** → lista de dependencias experimentales.  
- **mypy.ini** → configuración de tipado estático.  
- **pytest.ini** → estandarización de pruebas unitarias e integración.

### 📂 utils/
- **ci_cd_utils.py** → funciones utilitarias para automatizar los pipelines CI/CD (logs firmados, timestamps, hash).

### 📂 schemas/
- **ci_cd_schema.json** → esquema de validación de workflows y artefactos CI/CD.

### 📂 tests/
- **test_ci.yml** → valida el pipeline CI.  
- **test_lint.yml** → valida la calidad del código.  
- **test_build.yml** → valida la instalación y reproducibilidad de dependencias.  
- **test_ci_cd_utils.py** → valida la robustez de las funciones utilitarias CI/CD.

### 📂 reports/
Este directorio agrupa los **reportes generados automáticamente** por los workflows CI/CD:  
- `coverage.xml` → reporte de cobertura de pruebas.  
- `test-results.xml` → reporte JUnit de pruebas unitarias.  
- `lint-report.txt` → reporte flake8/mypy.  
- `security-report.json` → reporte bandit/safety.  
- `deploy-report.log` → reporte del despliegue staging (healthchecks).  

👉 Estos archivos sirven para la **auditabilidad de los controles**.

### 📂 artifacts/
Este directorio agrupa los **productos finales y evidencias institucionales**:  

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

👉 Estos archivos sirven para la **trazabilidad institucional y validación externa**.

---

## 🔄 Workflows CI/CD integrados

### 📂 .github/workflows/
- **ci-validation.yml**  
  → Pipeline principal:  
  - Ejecución de pruebas unitarias e integración.  
  - Verificación de robustez de dependencias.  
  - Export de resultados en `reports/`.

- **lint-check.yml**  
  → Pipeline de calidad:  
  - Verificación de código con flake8 y mypy.  
  - Control de reglas definidas en `mypy.ini`.  
  - Registro de resultados en `reports/lint-report.txt`.

- **build-validation.yml**  
  → Pipeline de build:  
  - Verificación de instalación de dependencias (`requirements.txt`).  
  - Control de reproducibilidad de entornos.  
  - Firma y hash de artefactos en `artifacts/`.

- **docker-pipeline.yml**  
  → Pipeline de contenedorización:  
  - Construcción de imagen Docker.  
  - Push hacia GHCR.  
  - Verificación de integridad de la imagen (hash en `artifacts/docker-image-sha256.txt`).

- **deploy-staging.yml**  
  → Pipeline de despliegue:  
  - Simulación vía `docker-compose`.  
  - Servicios: app, db, monitoreo, exporters.  
  - Healthchecks integrados con export en `reports/deploy-report.log`.

---

## ⚙️ Funcionamiento

- Los workflows están definidos en `workflows/` y validados por las configuraciones (`configs/`).  
- Los utilitarios (`utils/`) aseguran trazabilidad y seguridad de los pipelines.  
- Los esquemas (`schemas/`) garantizan coherencia y conformidad de los workflows.  
- Los tests (`tests/`) validan robustez y reproducibilidad de los pipelines.  
- Los archivos `prometheus.yml` y `alert_rules.yml` aseguran monitoreo y alertas.  
- El `docker-compose.yml` permite un despliegue local completo y auditable.  
- Los directorios `reports/` y `artifacts/` aseguran separación clara entre **resultados de controles** y **productos institucionales validados**.

---

## 🧭 Gobernanza e impacto institucional

- **Experimentación controlada**: el sub-módulo `ci-cd/` sirve como laboratorio para probar workflows.  
- **Trazabilidad**: cada modificación se documenta en las bitácoras CI/CD.  
- **Institucionalización**: una vez validados, los workflows y artefactos se fusionan en `finsig/`.  
- **Impacto**: garantiza robustez, reproducibilidad y auditabilidad antes de la adopción oficial.

---

## ✅ Conclusión

El sub-módulo `ci-cd/` es el **laboratorio técnico de FINSIG**.  
Permite probar y fortalecer los workflows CI/CD antes de su integración institucional en la rama principal `finsig/`, asegurando robustez, conformidad, trazabilidad y monitoreo.  
Con la adición de los directorios **`reports/`** y **`artifacts/`**, la trazabilidad institucional está completa:  
- `reports/` → resultados de controles.  
- `artifacts/` → productos finales y evidencias institucionales.
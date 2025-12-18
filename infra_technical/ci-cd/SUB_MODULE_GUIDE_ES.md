# GUÍA DEL SUBMÓDULO – CI/CD

---

## 🎯 Objetivo del submódulo

El submódulo `ci-cd/` está dedicado al **desarrollo, experimentación y endurecimiento de los workflows CI/CD**.  
Sirve como laboratorio controlado para probar, validar y mejorar las configuraciones antes de su integración oficial en la rama principal `finsig/`.

---

## 📂 Estructura de carpetas

### 📂 docs/
- **CI_CD_GUIDE.md** → principios de diseño de workflows CI/CD, metodología y estándares institucionales.  
- **README_TECHNIQUE_FR.md / EN / ES** → documentación trilingüe del pipeline CI/CD.  
- **BITACORA_CI-CD_FR.md / EN / ES** → registro institucional de la evolución del CI/CD.

### 📂 workflows/
- **ci.yml** → pipeline global de integración continua.  
- **tests.yml** → ejecución de pruebas unitarias con cobertura.  
- **lint.yml** → verificación de calidad del código (flake8 + bandit).  
- **build.yml** → empaquetado Python y verificación de instalabilidad.  
- **docker.yml** → construcción y push de la imagen Docker hacia GHCR.  
- **deploy.yml** → despliegue en staging mediante docker-compose.  
- **prometheus.yml** → configuración de monitoreo Prometheus.  
- **alert_rules.yml** → reglas de alerta críticas (app caída, DB caída, CPU/memoria alta).  
- **docker-compose.yml** → entorno completo (app, db, exporters, monitoreo).

### 📂 configs/
- **pyproject.toml** → definición de dependencias Python.  
- **requirements.txt** → lista de dependencias experimentales.  
- **mypy.ini** → configuración de verificación estática de tipos.  
- **pytest.ini** → estandarización de pruebas unitarias e integración.

### 📂 utils/
- **ci_cd_utils.py** → funciones utilitarias para automatizar pipelines CI/CD (logs firmados, marcas de tiempo, hash).

### 📂 schemas/
- **ci_cd_schema.json** → esquema de validación de workflows y artefactos CI/CD.

### 📂 tests/
- **test_ci.yml** → valida el pipeline CI.  
- **test_lint.yml** → valida la calidad del código.  
- **test_build.yml** → valida la instalación y reproducibilidad de dependencias.  
- **test_ci_cd_utils.py** → valida la robustez de las funciones utilitarias CI/CD.

---

## 🔄 Workflows CI/CD integrados

### 📂 .github/workflows/
- **ci-validation.yml**  
  → Pipeline principal:  
  - Ejecuta pruebas unitarias e integración.  
  - Verifica la robustez de las dependencias.  
  - Exporta resultados en `reports/ci-cd/`.

- **lint-check.yml**  
  → Pipeline de calidad:  
  - Verificación del código con flake8 y mypy.  
  - Control de reglas definidas en `mypy.ini`.  
  - Registro de resultados en `BITACORA.md`.

- **build-validation.yml**  
  → Pipeline de build:  
  - Verificación de instalación de dependencias (`requirements.txt`).  
  - Control de reproducibilidad de entornos.  
  - Firma y hash de reportes.

- **docker-pipeline.yml**  
  → Pipeline de contenedorización:  
  - Construcción de la imagen Docker.  
  - Push hacia GHCR.  
  - Verificación de integridad de la imagen.

- **deploy-staging.yml**  
  → Pipeline de despliegue:  
  - Simulación mediante `docker-compose`.  
  - Servicios: app, db, monitoreo, exporters.  
  - Healthchecks integrados.

---

## ⚙️ Funcionamiento

- Los workflows están definidos en `workflows/` y validados por las configuraciones (`configs/`).  
- Los utilitarios (`utils/`) aseguran trazabilidad y seguridad de los pipelines.  
- Los esquemas (`schemas/`) garantizan coherencia y conformidad de los workflows.  
- Los tests (`tests/`) validan robustez y reproducibilidad de los pipelines.  
- Los archivos `prometheus.yml` y `alert_rules.yml` aseguran monitoreo y alertas.  
- El `docker-compose.yml` permite un despliegue local completo y auditable.

---

## 🧭 Gobernanza e impacto institucional

- **Experimentación controlada**: el submódulo `ci-cd/` sirve como laboratorio para probar workflows.  
- **Trazabilidad**: cada modificación se documenta en `BITACORA_CI-CD_ES.md`.  
- **Institucionalización**: una vez validados, los workflows se fusionan en `finsig/`.  
- **Impacto**: garantiza robustez, reproducibilidad y auditabilidad antes de la adopción oficial.

---

## ✅ Conclusión

El submódulo `ci-cd/` es el **laboratorio técnico de FINSIG**.  
Permite probar y endurecer los workflows CI/CD antes de su integración institucional en la rama principal `finsig/`, asegurando robustez, conformidad, trazabilidad y monitoreo.
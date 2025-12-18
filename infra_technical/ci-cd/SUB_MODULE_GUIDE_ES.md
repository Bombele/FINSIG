
# SOUS_MODULE_GUIDE – CI/CD (Versión en Español)

---

## 🎯 Objetivo del sub-módulo

El sub-módulo `ci-cd/` está dedicado al **desarrollo, experimentación y endurecimiento de los flujos de trabajo CI/CD**.  
Permite probar, validar y mejorar las configuraciones antes de su integración oficial en la rama principal `finsig/`.

---

## 📂 Estructura de carpetas

### 📂 docs/
- CI_CD_GUIDE.md → principios de diseño de los flujos CI/CD, metodología y estándares institucionales.  
- README_TECHNIQUE_ES.md / FR / EN → documentación trilingüe del pipeline CI/CD.  
- BITACORA_CI-CD_ES.md / FR / EN → bitácora institucional de las evoluciones CI/CD.

### 📂 workflows/
- ci.yml → pipeline global de integración continua.  
- tests.yml → ejecución de pruebas unitarias con cobertura.  
- lint.yml → verificación del código (flake8 + bandit).  
- build.yml → empaquetado Python y verificación de instalabilidad.  
- docker.yml → construcción y push de la imagen Docker hacia GHCR.  
- deploy.yml → despliegue en staging vía docker-compose.  
- prometheus.yml → configuración de monitoreo Prometheus.  
- alert_rules.yml → reglas críticas de alerta (app caída, DB caída, CPU/memoria).  
- docker-compose.yml → entorno completo (app, db, exporters, monitoreo).

### 📂 configs/
- pyproject.toml → definición de dependencias Python.  
- requirements.txt → lista de dependencias experimentales.  
- mypy.ini → configuración de verificación estática de tipos.  
- pytest.ini → estandarización de pruebas unitarias e integración.

### 📂 utils/
- ci_cd_utils.py → funciones utilitarias para automatizar pipelines CI/CD (logs firmados, marcas de tiempo, hash).

### 📂 schemas/
- ci_cd_schema.json → esquema de validación de workflows y artefactos CI/CD.

### 📂 tests/
- test_ci.yml → valida la validez del pipeline CI.  
- test_lint.yml → valida la calidad del código.  
- test_build.yml → valida la instalación y reproducibilidad de dependencias.  
- test_ci_cd_utils.py → valida la robustez de las funciones utilitarias CI/CD.

### 📂 reports/
Esta carpeta agrupa los **informes generados automáticamente** por los workflows CI/CD:  
- coverage.xml → informe de cobertura de pruebas.  
- test-results.xml → informe JUnit de pruebas unitarias.  
- lint-report.txt → informe flake8/mypy.  
- security-report.json → informe bandit/safety.  
- deploy-report.log → informe de despliegue en staging (healthchecks).

👉 Estos archivos sirven para la **auditabilidad de los controles**.

### 📂 artifacts/
Esta carpeta agrupa los **productos finales y pruebas institucionales**:  

#### 🔧 Build
- finsig-<versión>-py3-none-any.whl  
- finsig-<versión>.tar.gz  

#### 🐳 Docker
- docker-image-sha256.txt → hash SHA256 de la imagen Docker.  
- docker-image.tar → exportación local de la imagen (opcional).  

#### 📜 Logs
- ci_cd_events.log → registro de eventos CI/CD.  
- deploy-report.log → informe de despliegue en staging.  

#### 🔒 Hashes
- build-hash.txt → huella SHA256 de los paquetes Python.  
- docker-hash.txt → huella SHA256 de la imagen Docker.  

#### ✅ Validación
- artifact-validation.json → archivo conforme al esquema ci_cd_schema.json, listando artefactos, hash y estado validado.  

👉 Estos archivos sirven para la **trazabilidad institucional y validación externa**.

### 📂 scripts/
Esta carpeta agrupa los **scripts de orquestación CI/CD** usados localmente o en Codespaces para reproducir manualmente los workflows, validar artefactos y generar pruebas institucionales.

#### 🔧 Scripts especializados
- build.sh → genera los artefactos Python (wheel, sdist) y los valida con Twine.  
- docker.sh → construye la imagen Docker, la exporta en tar, genera hashes y archivos de prueba.  
- reports.sh → ejecuta pruebas unitarias, cobertura, lint y auditorías de seguridad.  
- validate.sh → genera artifact-validation.json cruzando artefactos e informes.  
- setup_pipeline.sh → instala dependencias, prepara carpetas y orquesta la ejecución completa del pipeline.  
- pipeline.sh → ejecuta todos los scripts en orden para reproducir el pipeline CI/CD localmente.

👉 Estos scripts permiten probar, auditar y validar cada etapa del pipeline CI/CD sin depender únicamente de los workflows de GitHub. Aseguran una **trazabilidad offline**, útil en contextos de bloqueo o auditoría externa.

---

## 🔄 Workflows CI/CD integrados

### 📂 .github/workflows/
- ci-validation.yml → pipeline principal: pruebas, integración, exportación de informes.  
- lint-check.yml → pipeline de calidad: flake8, mypy, registro.  
- build-validation.yml → pipeline de build: reproducibilidad, hash, firma.  
- docker-pipeline.yml → pipeline de contenedorización: build, push, integridad.  
- deploy-staging.yml → pipeline de despliegue: simulación, healthchecks, monitoreo.

---

## ⚙️ Funcionamiento

- Los workflows están definidos en workflows/ y validados por las configuraciones (configs/).  
- Los utilitarios (utils/) aseguran trazabilidad y seguridad de los pipelines.  
- Los esquemas (schemas/) garantizan coherencia y conformidad de los workflows.  
- Los tests (tests/) validan robustez y reproducibilidad de los pipelines.  
- prometheus.yml y alert_rules.yml aseguran monitoreo y alertas.  
- docker-compose.yml permite un despliegue local completo y auditable.  
- Las carpetas reports/ y artifacts/ aseguran separación clara entre **resultados de controles** y **productos institucionales validados**.  
- La carpeta scripts/ permite reproducir localmente cada etapa del pipeline, con validación dinámica y trazabilidad completa.

---

## 🧭 Gobernanza e impacto institucional

- Experimentación controlada: el sub-módulo ci-cd/ sirve como laboratorio para probar workflows.  
- Trazabilidad: cada modificación se documenta en las bitácoras CI/CD.  
- Institucionalización: una vez validados, los workflows y artefactos se fusionan en finsig/.  
- Scripts como prueba de autonomía: la carpeta scripts/ muestra que FINSIG puede reproducir sus pipelines sin dependencia de GitHub Actions.  
- Auditabilidad offline: cada script produce artefactos e informes trazables, incluso en entornos restringidos.  
- Impacto: garantiza robustez, reproducibilidad y auditabilidad antes de la adopción oficial.

---

## ✅ Conclusión

El sub-módulo ci-cd/ es el **laboratorio técnico de FINSIG**.  
Permite probar y endurecer los workflows CI/CD antes de su integración institucional en la rama principal finsig/, asegurando robustez, conformidad, trazabilidad y monitoreo.  
Con la adición de las carpetas reports/, artifacts/ y scripts/, la trazabilidad institucional es completa:  
- reports/ → resultados de controles.  
- artifacts/ → productos finales y pruebas institucionales validadas.  
- scripts/ → reproducción local, validación dinámica, auditabilidad offline.

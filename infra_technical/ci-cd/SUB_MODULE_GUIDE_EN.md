# SUB-MODULE GUIDE – CI/CD

---

## 🎯 Purpose of the sub-module

The `ci-cd/` sub-module is dedicated to the **development, experimentation, and hardening of CI/CD workflows**.  
It allows testing, validation, and improvement of configurations before their official integration into the main branch `finsig/`.

---

## 📂 Directory Structure

### 📂 docs/
- **CI_CD_GUIDE.md** → design principles of CI/CD workflows, methodology, and institutional standards.  
- **README_TECHNIQUE_FR.md / EN / ES** → trilingual documentation of the CI/CD pipeline.  
- **BITACORA_CI-CD_FR.md / EN / ES** → institutional log of CI/CD evolutions.

### 📂 workflows/
- **ci.yml** → global continuous integration pipeline.  
- **tests.yml** → execution of unit tests with coverage.  
- **lint.yml** → code verification (flake8 + bandit).  
- **build.yml** → Python packaging and installability check.  
- **docker.yml** → Docker image build and push to GHCR.  
- **deploy.yml** → staging deployment via docker-compose.  
- **prometheus.yml** → Prometheus monitoring configuration.  
- **alert_rules.yml** → critical alert rules (app down, DB down, CPU/memory).  
- **docker-compose.yml** → complete environment (app, db, exporters, monitoring).

### 📂 configs/
- **pyproject.toml** → definition of Python dependencies.  
- **requirements.txt** → list of experimental dependencies.  
- **mypy.ini** → static type checking configuration.  
- **pytest.ini** → standardization of unit and integration tests.

### 📂 utils/
- **ci_cd_utils.py** → utility functions for automating CI/CD pipelines (signed logs, timestamps, hashing).

### 📂 schemas/
- **ci_cd_schema.json** → validation schema for CI/CD workflows and artifacts.

### 📂 tests/
- **test_ci.yml** → validates CI pipeline.  
- **test_lint.yml** → validates code quality.  
- **test_build.yml** → validates installation and reproducibility of dependencies.  
- **test_ci_cd_utils.py** → validates robustness of CI/CD utility functions.

### 📂 reports/
This folder contains **reports automatically generated** by CI/CD workflows:  
- `coverage.xml` → test coverage report.  
- `test-results.xml` → JUnit report of unit tests.  
- `lint-report.txt` → flake8/mypy report.  
- `security-report.json` → bandit/safety report.  
- `deploy-report.log` → staging deployment report (healthchecks).  

👉 These files serve for **auditability of controls**.

### 📂 artifacts/
This folder contains **final products and institutional evidence**:  

#### 🔧 Build
- `finsig-<version>-py3-none-any.whl`  
- `finsig-<version>.tar.gz`  

#### 🐳 Docker
- `docker-image-sha256.txt` → SHA256 hash of the Docker image.  
- `docker-image.tar` → local export of the image (optional).  

#### 📜 Logs
- `ci_cd_events.log` → CI/CD events log.  
- `deploy-report.log` → staging deployment report.  

#### 🔒 Hashes
- `build-hash.txt` → SHA256 hash of Python packages.  
- `docker-hash.txt` → SHA256 hash of the Docker image.  

#### ✅ Validation
- `artifact-validation.json` → file compliant with `ci_cd_schema.json`, listing artifacts, hash, and validation status.  

👉 These files serve for **institutional traceability and external validation**.

---

## 🔄 Integrated CI/CD Workflows

### 📂 .github/workflows/
- **ci-validation.yml**  
  → Main pipeline:  
  - Execution of unit and integration tests.  
  - Dependency robustness check.  
  - Export of results into `reports/`.

- **lint-check.yml**  
  → Quality pipeline:  
  - Code verification with flake8 and mypy.  
  - Control of rules defined in `mypy.ini`.  
  - Logging of results into `reports/lint-report.txt`.

- **build-validation.yml**  
  → Build pipeline:  
  - Dependency installation check (`requirements.txt`).  
  - Environment reproducibility control.  
  - Signing and hashing of artifacts into `artifacts/`.

- **docker-pipeline.yml**  
  → Containerization pipeline:  
  - Docker image build.  
  - Push to GHCR.  
  - Integrity check of the image (hash in `artifacts/docker-image-sha256.txt`).

- **deploy-staging.yml**  
  → Deployment pipeline:  
  - Simulation via `docker-compose`.  
  - Services: app, db, monitoring, exporters.  
  - Integrated healthchecks with export into `reports/deploy-report.log`.

---

## ⚙️ Operation

- Workflows are defined in `workflows/` and validated by configurations (`configs/`).  
- Utilities (`utils/`) ensure pipeline traceability and security.  
- Schemas (`schemas/`) guarantee workflow consistency and compliance.  
- Tests (`tests/`) validate pipeline robustness and reproducibility.  
- Files `prometheus.yml` and `alert_rules.yml` ensure monitoring and alerts.  
- `docker-compose.yml` enables complete and auditable local deployment.  
- Folders `reports/` and `artifacts/` ensure clear separation between **control results** and **validated institutional products**.

---

## 🧭 Governance and Institutional Impact

- **Controlled experimentation**: the `ci-cd/` sub-module serves as a laboratory for testing workflows.  
- **Traceability**: each modification is documented in CI/CD bitácoras.  
- **Institutionalization**: once validated, workflows and artifacts are merged into `finsig/`.  
- **Impact**: ensures robustness, reproducibility, and auditability before official adoption.

---

## ✅ Conclusion

The `ci-cd/` sub-module is the **technical laboratory of FINSIG**.  
It allows testing and hardening of CI/CD workflows before their institutional integration into the main branch `finsig/`, ensuring robustness, compliance, traceability, and monitoring.  
With the addition of **`reports/`** and **`artifacts/`**, institutional traceability is complete:  
- `reports/` → control results.  
- `artifacts/` → final products and institutional evidence.
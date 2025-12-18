# SUB_MODULE_GUIDE – CI/CD

---

## 🎯 Submodule Objective

The `ci-cd/` submodule is dedicated to the **development, experimentation, and hardening of CI/CD workflows**.  
It serves as a controlled lab to test, validate, and improve configurations before their official integration into the main `finsig/` branch.

---

## 📂 Folder Structure

### 📂 docs/
- **CI_CD_GUIDE.md** → design principles for CI/CD workflows, methodology, and institutional standards.  
- **README_TECHNIQUE_FR.md / EN / ES** → trilingual documentation of the CI/CD pipeline.  
- **BITACORA_CI-CD_FR.md / EN / ES** → institutional log of CI/CD evolution.

### 📂 workflows/
- **ci.yml** → global continuous integration pipeline.  
- **tests.yml** → unit test execution with coverage.  
- **lint.yml** → code quality checks (flake8 + bandit).  
- **build.yml** → Python packaging and installability verification.  
- **docker.yml** → Docker image build and push to GHCR.  
- **deploy.yml** → staging deployment via docker-compose.  
- **prometheus.yml** → Prometheus monitoring configuration.  
- **alert_rules.yml** → critical alert rules (app down, DB down, high CPU/memory).  
- **docker-compose.yml** → full environment (app, db, exporters, monitoring).

### 📂 configs/
- **pyproject.toml** → Python dependency definitions.  
- **requirements.txt** → list of experimental dependencies.  
- **mypy.ini** → static type check configuration.  
- **pytest.ini** → standardization of unit and integration tests.

### 📂 utils/
- **ci_cd_utils.py** → utility functions for CI/CD automation (signed logs, timestamps, hashing).

### 📂 schemas/
- **ci_cd_schema.json** → validation schema for CI/CD workflows and artifacts.

### 📂 tests/
- **test_ci.yml** → validates the CI pipeline.  
- **test_lint.yml** → validates code quality.  
- **test_build.yml** → validates dependency installation and reproducibility.  
- **test_ci_cd_utils.py** → validates robustness of CI/CD utility functions.

---

## 🔄 Integrated CI/CD Workflows

### 📂 .github/workflows/
- **ci-validation.yml**  
  → Main pipeline:  
  - Executes unit and integration tests.  
  - Verifies dependency robustness.  
  - Exports results to `reports/ci-cd/`.

- **lint-check.yml**  
  → Quality pipeline:  
  - Code checks with flake8 and mypy.  
  - Enforces rules from `mypy.ini`.  
  - Logs results in `BITACORA.md`.

- **build-validation.yml**  
  → Build pipeline:  
  - Verifies installation of `requirements.txt`.  
  - Checks environment reproducibility.  
  - Signs and hashes reports.

- **docker-pipeline.yml**  
  → Containerization pipeline:  
  - Builds Docker image.  
  - Pushes to GHCR.  
  - Verifies image integrity.

- **deploy-staging.yml**  
  → Deployment pipeline:  
  - Simulates deployment via `docker-compose`.  
  - Services: app, db, monitoring, exporters.  
  - Integrated healthchecks.

---

## ⚙️ Functionality

- Workflows are defined in `workflows/` and validated by `configs/`.  
- Utilities (`utils/`) ensure pipeline traceability and security.  
- Schemas (`schemas/`) guarantee workflow consistency and compliance.  
- Tests (`tests/`) validate pipeline robustness and reproducibility.  
- `prometheus.yml` and `alert_rules.yml` enable monitoring and alerting.  
- `docker-compose.yml` provides a complete and auditable local deployment.

---

## 🧭 Governance & Institutional Impact

- **Controlled experimentation**: the `ci-cd/` submodule serves as a lab for workflow testing.  
- **Traceability**: every change is documented in `BITACORA_CI-CD_EN.md`.  
- **Institutionalization**: once validated, workflows are merged into `finsig/`.  
- **Impact**: ensures robustness, reproducibility, and auditability before official adoption.

---

## ✅ Conclusion

The `ci-cd/` submodule is FINSIG’s **technical laboratory**.  
It enables testing and hardening of CI/CD workflows before institutional integration into the main `finsig/` branch, ensuring robustness, compliance, traceability, and monitoring.
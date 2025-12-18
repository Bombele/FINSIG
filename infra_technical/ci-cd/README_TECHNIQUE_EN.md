# TECHNICAL README – CI/CD Pipeline for FINSIG

---

## 🎯 Purpose

The CI/CD module ensures **robustness**, **traceability**, and **auditability** of FINSIG’s technical infrastructure.  
It enables controlled testing, packaging, deployment, and monitoring of all components in a reproducible and compliant environment.  
The pipeline is designed to operate reliably even under crisis or geopolitical constraints, reinforcing institutional credibility.

---

## 📂 Structure Overview

### ⚙️ configs/
- `pyproject.toml` → Project metadata, dependencies, and tool configurations (pytest, flake8, mypy, bandit, docker, prometheus-client).  
- `requirements.txt` → Hierarchical dependency list (core, dev, CI/CD, monitoring).  
- `pytest.ini` → Standardized test discovery, coverage reports, JUnit output, and timestamped logs.  
- `mypy.ini` → Strict type checking, error codes, plugin support (`pydantic.mypy`).  

### ⚙️ .github/workflows/
- `build-validation.yml` → Validates Python packaging (wheel + sdist), installability, and audit artifacts.  
- `lint-validation.yml` → Runs flake8, bandit, and mypy for code quality, security, and typing.  
- `tests-validation.yml` → Executes unit tests with coverage and JUnit reports.  
- `security-check.yml` → Scans code and dependencies for vulnerabilities (bandit + safety).  
- `docker-pipeline.yml` → Builds and pushes Docker image to GHCR.  
- `deploy-validation.yml` → Simulates staging deployment via Docker Compose with healthchecks and Prometheus.  
- `ci-validation.yml` → Orchestrates all validation workflows in parallel.  

### 📊 Monitoring & Orchestration
- `prometheus.yml` → Scrapes metrics from app, database, and exporters.  
- `alert_rules.yml` → Defines critical alerts (app down, DB down, high CPU/memory).  
- `docker-compose.yml` → Deploys app, Postgres, exporters, and Prometheus in a local staging environment.  

### 🧪 Testing & Validation
- `tests/` → Consolidated test workflows: build, deploy, security, lint, CI orchestration.  
- `schemas/` → Workflow and artifact validation schema (`ci_cd_schema.json`).  
- `utils/` → Reusable functions for logging, hashing, and timestamping (`ci_cd_utils.py`).  

### 📚 Documentation
- `README_TECHNIQUE_FR.md / EN / ES` → Trilingual technical overview.  
- `BITACORA_CI-CD_FR.md / EN / ES` → Institutional log of CI/CD evolution.  
- `CI_CD_GUIDE.md` → Design principles, methodology, and governance of CI/CD workflows.  

### 📂 reports/
Contains **reports automatically generated** by CI/CD workflows:  
- `coverage.xml` → test coverage report.  
- `test-results.xml` → JUnit report of unit tests.  
- `lint-report.txt` → flake8/mypy report.  
- `security-report.json` → bandit/safety report.  
- `deploy-report.log` → staging deployment report (healthchecks).  

👉 These files ensure **auditability of controls**.

### 📂 artifacts/
Contains **final products and institutional evidence**:  
- Build → `finsig-<version>-py3-none-any.whl`, `finsig-<version>.tar.gz`.  
- Docker → `docker-image-sha256.txt`, `docker-image.tar`.  
- Logs → `ci_cd_events.log`, `deploy-report.log`.  
- Hashes → `build-hash.txt`, `docker-hash.txt`.  
- Validation → `artifact-validation.json` (compliant with `ci_cd_schema.json`).  

👉 These files ensure **institutional traceability and external validation**.

### 📂 scripts/
Contains **CI/CD orchestration scripts** for local reproduction and offline validation:  
- `build.sh` → Generates Python artifacts and validates with Twine.  
- `docker.sh` → Builds Docker image, exports tar, generates hashes and proof files.  
- `reports.sh` → Runs tests, coverage, lint, and security audits.  
- `validate.sh` → Generates `artifact-validation.json` dynamically with PASSED/FAILED statuses.  
- `setup_pipeline.sh` → Installs dependencies, prepares folders, orchestrates full pipeline execution.  
- `pipeline.sh` → Runs all scripts sequentially to reproduce the CI/CD pipeline locally.  

👉 These scripts provide **offline auditability** and demonstrate institutional autonomy.

---

## 🔄 Pipeline Stages

1. **Testing** → Unit tests, coverage, JUnit reports.  
2. **Linting & Security** → flake8, mypy, bandit, safety.  
3. **Build & Packaging** → wheel + sdist, reproducibility checks.  
4. **Dockerization** → Build and push image to GHCR.  
5. **Staging Deployment** → Full environment via docker-compose, healthchecks.  
6. **Monitoring & Alerting** → Prometheus metrics, alert rules.  
7. **Validation** → Dynamic `artifact-validation.json` with institutional traceability.

---

## ✅ Institutional Impact

- **Robustness** → Automated testing and packaging.  
- **Compliance** → Enforced via linting, typing, and security scans.  
- **Auditability** → Reports and validation artifacts exportable.  
- **Reproducibility** → Guaranteed by Docker and standardized configs.  
- **Resilience** → Monitoring and alerting ensure operational continuity.  
- **Credibility** → Trilingual documentation and bitácoras support external validation.  
- **Autonomy** → Scripts/ folder ensures reproducibility even offline.

---

## 📌 Conclusion

This CI/CD pipeline is the **technical backbone of FINSIG**.  
It demonstrates the project’s ability to be tested, secured, packaged, deployed, and monitored in a **transparent and auditable** manner.  
With the addition of **reports/**, **artifacts/**, and **scripts/**, institutional traceability is complete:  
- reports/ → control results.  
- artifacts/ → final products and institutional evidence.  
- scripts/ → local reproduction, dynamic validation, offline auditability.
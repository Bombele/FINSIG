# TECHNICAL README – CI/CD Pipeline for FINSIG

---

## 🎯 Purpose

This CI/CD module ensures the **robustness**, **traceability**, and **auditability** of FINSIG’s technical infrastructure.  
It enables controlled testing, packaging, deployment, and monitoring of all components in a reproducible and compliant environment.  
The pipeline is designed to operate reliably even under geopolitical constraints, reinforcing institutional credibility.

---

## 📂 Structure Overview

### 🔧 `configs/`
- `pyproject.toml` → Project metadata, dependencies, and tool configurations (pytest, flake8, mypy, bandit, docker, prometheus-client).  
- `requirements.txt` → Hierarchical dependency list (core, dev, CI/CD, monitoring).  
- `pytest.ini` → Standardized test discovery, coverage reports, JUnit output, and timestamped logs.  
- `mypy.ini` → Strict type checking, error codes, plugin support (`pydantic.mypy`).

### ⚙️ `.github/workflows/`
- `build-validation.yml` → Validates Python packaging (wheel + sdist), installability, and audit artifacts.  
- `lint-validation.yml` → Runs flake8, bandit, and mypy for code quality, security, and typing.  
- `tests-validation.yml` → Executes unit tests with coverage and JUnit reports.  
- `security-check.yml` → Scans code and dependencies for vulnerabilities (bandit + safety).  
- `deploy-validation.yml` → Simulates staging deployment via Docker Compose with healthchecks and Prometheus.  
- `lint-check.yml` → Lightweight linting and type check for fast feedback.  
- `ci-validation.yml` → Orchestrates all validation workflows in parallel.

### 📈 Monitoring & Orchestration
- `prometheus.yml` → Scrapes metrics from app, database, and exporters.  
- `alert_rules.yml` → Defines critical alerts (app down, DB down, high CPU/memory).  
- `docker-compose.yml` → Deploys app, Postgres, exporters, and Prometheus in a local staging environment.

### 🧪 Testing & Validation
- `tests/` → Validation pipelines (`test_ci.yml`, `test_lint.yml`, `test_build.yml`) and utility tests (`test_ci_cd_utils.py`).  
- `schemas/` → Workflow and artifact validation schema (`ci_cd_schema.json`).  
- `utils/` → Reusable functions for logging, hashing, and timestamping (`ci_cd_utils.py`).

### 📚 Documentation
- `README_TECHNIQUE_FR.md / EN / ES` → Trilingual technical overview.  
- `BITACORA_CI-CD_FR.md / EN / ES` → Institutional log of CI/CD evolution.  
- `CI_CD_GUIDE.md` → Design principles, methodology, and governance of CI/CD workflows.

---

## 🔄 Pipeline Stages

1. **Testing**  
   - Run unit tests via `pytest`.  
   - Measure coverage and export reports (`coverage.xml`, `test-results.xml`).

2. **Linting & Security**  
   - Enforce style rules with `flake8`.  
   - Detect vulnerabilities using `bandit` and `safety`.  
   - Apply static type checks via `mypy`.

3. **Build & Packaging**  
   - Generate Python artifacts (`wheel`, `sdist`).  
   - Verify installability and reproducibility.

4. **Dockerization**  
   - Build Docker image.  
   - Push to GitHub Container Registry (GHCR).

5. **Staging Deployment**  
   - Simulate full environment via `docker-compose`.  
   - Includes app, database, exporters, and monitoring.  
   - Healthchecks on app, DB, and Prometheus.

6. **Monitoring & Alerting**  
   - Prometheus collects metrics.  
   - Alert rules trigger on critical failures or resource thresholds.

---

## ✅ Institutional Impact

- **Robustness** → Validated through automated testing and packaging.  
- **Compliance** → Enforced via linting, typing, and security scans.  
- **Auditability** → Coverage, JUnit, and Prometheus reports are exportable.  
- **Reproducibility** → Guaranteed by Docker and standardized configs.  
- **Resilience** → Monitoring and alerting ensure operational continuity.  
- **Credibility** → Trilingual documentation and bitácoras support external validation.

---

## 📌 Conclusion

This CI/CD pipeline is the **technical backbone of FINSIG**.  
It demonstrates the project’s ability to be tested, secured, packaged, deployed, and monitored in a **transparent and auditable** manner.  
It is a strategic asset for institutional validation, partner onboarding, and regulatory compliance.
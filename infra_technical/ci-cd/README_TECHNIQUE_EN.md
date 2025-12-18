# Technical README – CI/CD Pipeline for FINSIG

---

## 🎯 Purpose

The FINSIG CI/CD pipeline is designed to guarantee **robustness**, **traceability**, and **auditability** of the project.  
Each stage ensures code quality, reproducibility of environments, and operational continuity, even under crisis conditions.

---

## 🔎 Main Stages

### 1. **Tests (`tests.yml`)**
- Run unit tests using `pytest`.
- Measure coverage with `pytest-cov`.
- Generate reports for external audit.

### 2. **Lint & Security (`lint.yml`)**
- Enforce style and complexity rules with `flake8`.
- Perform security analysis with `bandit` to detect vulnerabilities.
- Ensure technical compliance and code quality.

### 3. **Build & Packaging (`build.yml`)**
- Generate Python artifacts (`wheel`, `sdist`) via `python -m build`.
- Verify installability (`pip install dist/*.whl`).
- Upload artifacts for audit and distribution.

### 4. **Dockerization (`docker.yml`)**
- Build Docker image with `docker build`.
- Push automatically to GitHub Container Registry (GHCR).
- Guarantee portability and reproducibility.

### 5. **Staging Deployment (`deploy.yml`)**
- Simulate deployment via `docker-compose`.
- Services included: FINSIG app, Postgres database, Prometheus monitoring.
- Integrated healthchecks to ensure availability and auditability.

---

## ✅ Expected Outcomes

- **Robustness** validated by unit tests and coverage.  
- **Quality and security** ensured through linting and static analysis.  
- **Portability** via Python packaging and Docker images.  
- **Reproducibility** through Docker Compose and automated CI/CD.  
- **Auditability** reinforced by coverage reports, build artifacts, and Prometheus metrics.  

---

## 📌 Conclusion

This CI/CD pipeline forms the **technical backbone** of FINSIG.  
It demonstrates the project’s ability to be tested, secured, packaged, containerized, and deployed in a **reliable and transparent** manner.  
It is a key element for institutional credibility and validation by partners or regulators.
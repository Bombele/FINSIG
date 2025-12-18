```
# SOUS_MODULE_GUIDE – CI/CD (English Version)

---

## 🎯 Purpose of the sub-module

The `ci-cd/` sub-module is dedicated to the **development, experimentation, and hardening of CI/CD workflows**.  
It allows testing, validation, and improvement of configurations before their official integration into the main branch `finsig/`.

---

## 📂 Folder structure

### 📂 docs/
- CI_CD_GUIDE.md → design principles of CI/CD workflows, methodology, and institutional standards.  
- README_TECHNIQUE_EN.md / FR / ES → trilingual documentation of the CI/CD pipeline.  
- BITACORA_CI-CD_EN.md / FR / ES → institutional log of CI/CD evolutions.

### 📂 workflows/
- ci.yml → global continuous integration pipeline.  
- tests.yml → execution of unit tests with coverage.  
- lint.yml → code verification (flake8 + bandit).  
- build.yml → Python packaging and installability check.  
- docker.yml → Docker image build and push to GHCR.  
- deploy.yml → staging deployment via docker-compose.  
- prometheus.yml → Prometheus monitoring configuration.  
- alert_rules.yml → critical alert rules (app down, DB down, CPU/memory).  
- docker-compose.yml → complete environment (app, db, exporters, monitoring).

### 📂 configs/
- pyproject.toml → definition of Python dependencies.  
- requirements.txt → list of experimental dependencies.  
- mypy.ini → static type checking configuration.  
- pytest.ini → standardization of unit and integration tests.

### 📂 utils/
- ci_cd_utils.py → utility functions to automate CI/CD pipelines (signed logs, timestamps, hashing).

### 📂 schemas/
- ci_cd_schema.json → validation schema for CI/CD workflows and artifacts.

### 📂 tests/
- test_ci.yml → validates the CI pipeline.  
- test_lint.yml → validates code quality.  
- test_build.yml → validates dependency installation and reproducibility.  
- test_ci_cd_utils.py → validates robustness of CI/CD utility functions.

### 📂 reports/
This folder gathers **automatically generated reports** from CI/CD workflows:  
- coverage.xml → test coverage report.  
- test-results.xml → JUnit report of unit tests.  
- lint-report.txt → flake8/mypy report.  
- security-report.json → bandit/safety report.  
- deploy-report.log → staging deployment report (healthchecks).

👉 These files serve **auditability of controls**.

### 📂 artifacts/
This folder gathers **final products and institutional proofs**:  

#### 🔧 Build
- finsig-<version>-py3-none-any.whl  
- finsig-<version>.tar.gz  

#### 🐳 Docker
- docker-image-sha256.txt → SHA256 hash of the Docker image.  
- docker-image.tar → local export of the image (optional).  

#### 📜 Logs
- ci_cd_events.log → CI/CD events log.  
- deploy-report.log → staging deployment report.  

#### 🔒 Hashes
- build-hash.txt → SHA256 fingerprint of Python packages.  
- docker-hash.txt → SHA256 fingerprint of the Docker image.  

#### ✅ Validation
- artifact-validation.json → file compliant with ci_cd_schema.json, listing artifacts, hashes, and validated status.  

👉 These files serve **institutional traceability and external validation**.

### 📂 scripts/
This folder gathers **CI/CD orchestration scripts** used locally or in Codespaces to manually reproduce workflows, validate artifacts, and generate institutional proofs.

#### 🔧 Specialized scripts
- build.sh → generates Python artifacts (wheel, sdist) and validates them with Twine.  
- docker.sh → builds the Docker image, exports it as tar, generates hashes and proof files.  
- reports.sh → runs unit tests, coverage, lint, and security audits.  
- validate.sh → generates artifact-validation.json by cross-checking artifacts and reports.  
- setup_pipeline.sh → installs dependencies, prepares folders, and orchestrates full pipeline execution.  
- pipeline.sh → runs all scripts in order to reproduce the CI/CD pipeline locally.

👉 These scripts allow testing, auditing, and validating each CI/CD pipeline step without relying solely on GitHub workflows. They ensure **offline traceability**, useful in constrained contexts or external audits.

---

## 🔄 Integrated CI/CD workflows

### 📂 .github/workflows/
- ci-validation.yml → main pipeline: tests, integration, export of reports.  
- lint-check.yml → quality pipeline: flake8, mypy, logging.  
- build-validation.yml → build pipeline: reproducibility, hash, signature.  
- docker-pipeline.yml → containerization pipeline: build, push, integrity.  
- deploy-staging.yml → deployment pipeline: simulation, healthchecks, monitoring.

---

## ⚙️ Operation

- Workflows are defined in workflows/ and validated by configurations (configs/).  
- Utilities (utils/) ensure traceability and pipeline security.  
- Schemas (schemas/) guarantee workflow consistency and compliance.  
- Tests (tests/) validate pipeline robustness and reproducibility.  
- prometheus.yml and alert_rules.yml ensure monitoring and alerts.  
- docker-compose.yml enables complete local deployment and auditability.  
- reports/ and artifacts/ folders ensure clear separation between **control results** and **validated institutional products**.  
- scripts/ folder enables local reproduction of each pipeline step, with dynamic validation and complete traceability.

---

## 🧭 Governance and institutional impact

- Controlled experimentation: the ci-cd/ sub-module serves as a laboratory to test workflows.  
- Traceability: each modification is documented in CI/CD bitácoras.  
- Institutionalization: once validated, workflows and artifacts are merged into finsig/.  
- Scripts as proof of autonomy: the scripts/ folder shows FINSIG can reproduce its pipelines without GitHub Actions dependency.  
- Offline auditability: each script produces traceable artifacts and reports, even in constrained environments.  
- Impact: ensures robustness, reproducibility, and auditability before official adoption.

---

## ✅ Conclusion

The ci-cd/ sub-module is the **technical laboratory of FINSIG**.  
It allows testing and hardening of CI/CD workflows before institutional integration into the main branch finsig/, ensuring robustness, compliance, traceability, and monitoring.  
With the addition of reports/, artifacts/, and scripts/ folders, institutional traceability is complete:  
- reports/ → control results.  
- artifacts/ → finished products and validated institutional proofs.  
- scripts/ → local reproduction, dynamic validation, offline auditability.
```
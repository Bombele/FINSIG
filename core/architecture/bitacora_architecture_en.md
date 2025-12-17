# BITACORA – core/architecture/conformity

---

## 📅 Activity Log

- **2025-12-17** – Full recreation of `workflow_checker.py` to validate the trilingual documentation workflow (guides, bitácoras, technical READMEs).  
- **2025-12-17** – Update of `structure_validator.py` to strengthen mandatory file checks.  
- **2025-12-17** – Addition of trilingual `README_TECHNIQUE` templates to standardize technical documentation.  
- **2025-12-16** – Initialization of the `conformity/` sub-module with institutional validation logic.

---

## ✅ Validation Status

- `workflow_checker.py` operational and tested locally.  
- `structure_validator.py` validated, pending CI/CD integration.  
- Trilingual technical documentation in progress.  
- Bitácora updated to record evolutions.

---

## 📌 Technical Notes

- Validators must be integrated into CI/CD pipelines (`infra_technical/ci-cd/`).  
- Each sub-module must contain: guides, bitácoras, and technical READMEs in FR/EN/ES.  
- Compliance scripts must be executed before each merge to ensure documentation robustness.
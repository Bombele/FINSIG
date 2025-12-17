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

# BITACORA – core/architecture/modules/collection

---

## 📅 Activity Log

- **2025-12-17** – Created `data_collection.py` to centralize institutional data collection (CSV, JSON, API).  
- **2025-12-17** – Implemented validation logic (presence of `id` field) and automatic logging in `collection_log.txt`.  
- **2025-12-17** – Recommended creating a `logs/` folder to store tracking files and keep the root clean.  
- **2025-12-16** – Initialized the `collection/` sub-module with collection and traceability logic.

---

## ✅ Validation Status

- `data_collection.py` operational and tested locally.  
- Automatic logging confirmed (`collection_log.txt` generated on first run).  
- `logs/` folder recommended for better organization.  
- Bitácora updated to record evolutions.

---

## 📌 Technical Notes

- Log files should be placed in `logs/` and may be ignored in `.gitignore` if not versioned.  
- Each collection must be validated before integration into compliance and audit modules.  
- Future steps include:  
  - Adding advanced validation rules (format, mandatory fields).  
  - Integration with `infra-technical/checks` to automate compliance.
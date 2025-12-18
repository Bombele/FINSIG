# BITACORA – core/architecture

---

## 📅 Activity Log

- **2025-12-18** – Updated `audit_schema.py` and `compliance_schema.py` with `version` and `signature` fields (SHA256).  
- **2025-12-18** – Updated `structure_validator.py` to cross-validate schema signatures and required fields.  
- **2025-12-18** – Added `traceability.py` function `export_to_csv()` and enforced UTC timestamps for logs.  
- **2025-12-18** – Added unit tests `test_audit_schema.py` and `test_compliance_schema.py` for signature validation.  
- **2025-12-18** – Added `workflows/tests.yml` for CI/CD with GitHub Actions (pytest + coverage).  
- **2025-12-18** – Enhanced `test_pipeline_orchestrator.py` with dependency error cases.  
- **2025-12-18** – Enhanced `test_utils.py` with edge case validations (`None`, invalid strings, empty dicts).  
- **2025-12-17** – Added `schemas` module (`base_schema.py`, `finance_schema.py`, `audit_schema.py`, `compliance_schema.py`).  
- **2025-12-17** – Updated `BITACORA` and `README_TECHNIQUE` in trilingual versions (FR/EN/ES).  
- **2025-12-17** – Created `pipeline_orchestrator.py` (module `orchestration`).  
- **2025-12-16** – Recreated `workflow_checker.py` for trilingual documentation validation.  
- **2025-12-16** – Updated `structure_validator.py`.  
- **2025-12-15** – Initialized `conformity/` sub-module.  
- **2025-12-14** – Initial structuring of `core/architecture`.

---

## ✅ Validation Status

- Validators operational (`structure_validator.py`, `workflow_checker.py`).  
- Cross-validation of schema signatures (`audit_schema`, `compliance_schema`).  
- Collection and normalization modules tested.  
- Orchestration pipeline validated, including dependency error handling.  
- Schemas validated (`base`, `finance`, `audit`, `compliance`).  
- Scoring engine operational.  
- Storage manager operational.  
- Traceability engine operational (UTC + CSV export).  
- Utility toolkit operational (edge cases covered).  
- Unit tests integrated (`pytest`).  
- CI/CD workflow active (`workflows/tests.yml`).  
- Trilingual documentation in place.  
- Bitácora updated.

---

## 📌 Technical Notes

- Validators integrated into CI/CD.  
- Execution sequence:  
  1. Collection (`data_collection.py`)  
  2. Normalization (`data_normalization.py`)  
  3. Conformity (`structure_validator.py`, `workflow_checker.py`)  
  4. Orchestration (`pipeline_orchestrator.py`)  
  5. Schemas (`base_schema.py`, `finance_schema.py`, `audit_schema.py`, `compliance_schema.py`)  
  6. Scoring (`scoring_engine.py`)  
  7. Storage (`storage_manager.py`)  
  8. Traceability (`traceability.py`)  
  9. Utilities (`utils.py`)  
- Unit tests ensure robustness and reproducibility.  
- Logs stored in `logs/` with UTC timestamps.  
- Data normalized and validated before compliance, scoring, and audit.  
- Signatures (`SHA256`) ensure authenticity of audit and compliance schemas.  
- CI/CD workflow executes tests and coverage on every commit/PR.  

---

## 📌 Conclusion

The `core/architecture` bitácora now traces the complete evolution of the sub-module and its modules (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`, `traceability`, `utils`) together with their **unit tests** and **CI/CD workflow**.  
It ensures institutional traceability, documentation compliance, technical robustness, and reliable auditability.
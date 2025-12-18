# BITACORA – core/architecture

---

## 📅 Activity Log

- **2025-12-18** – Updated `README_TECHNIQUE_EN.md` to include modules `scoring`, `storage`, `traceability`, `utils` and their unit tests.  
- **2025-12-18** – Added `tests/test_structure_validator.py` to validate documentation conformity.  
- **2025-12-18** – Added `tests/test_workflow_checker.py` to validate workflow sequences.  
- **2025-12-18** – Added `tests/test_pipeline_orchestrator.py` to validate the full pipeline orchestration.  
- **2025-12-18** – Added `tests/test_traceability.py` to validate the traceability engine.  
- **2025-12-18** – Added `tests/test_utils.py` to validate institutional utility functions.  
- **2025-12-18** – Created `scoring_engine.py` (module `scoring`) for institutional scoring (risk, compliance, performance).  
- **2025-12-18** – Created `storage_manager.py` (module `storage`) for institutional storage management.  
- **2025-12-18** – Created `traceability.py` (module `traceability`) for institutional traceability logging.  
- **2025-12-18** – Created `utils.py` (module `utils`) for reusable institutional functions.  
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
- Collection and normalization modules tested.  
- Orchestration pipeline validated.  
- Schemas validated (`base`, `finance`, `audit`, `compliance`).  
- Scoring engine operational.  
- Storage manager operational.  
- Traceability engine operational.  
- Utility toolkit operational.  
- Unit tests integrated (`pytest`).  
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
- Logs stored in `logs/`.  
- Data normalized and validated before compliance, scoring, and audit.  
- Scoring, storage, and traceability integrated into institutional reports.  
- Utilities ensure consistency and reusability across modules.

---

## 📌 Conclusion

The `core/architecture` bitácora now traces the complete evolution of the sub-module and its modules (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`, `traceability`, `utils`) together with their **unit tests**.  
It ensures institutional traceability, documentation compliance, technical robustness, and reliable auditability.
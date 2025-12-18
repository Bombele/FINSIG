# BITACORA – core/architecture

---

## 📅 Activity Log

- **2025-12-18** – Updated `README_TECHNIQUE_EN.md` to include the `scoring`, `storage`, `traceability`, and `utils` modules alongside `conformity`, `collection`, `normalization`, `orchestration`, and `schemas`.  
- **2025-12-18** – Created `scoring_engine.py` (module `scoring`) to calculate institutional scores (risk, compliance, performance).  
- **2025-12-18** – Created `storage_manager.py` (module `storage`) to manage institutional storage (save, load, delete, traceability).  
- **2025-12-18** – Created `traceability.py` (module `traceability`) to log institutional actions (collection, normalization, conformity, scoring, storage) with auditability.  
- **2025-12-18** – Created `utils.py` (module `utils`) to provide reusable institutional functions (IDs, timestamps, validations, JSON, safe dictionary operations).  
- **2025-12-17** – Updated `README_TECHNIQUE_EN.md` to include the `schemas` module.  
- **2025-12-17** – Created `base_schema.py`, `finance_schema.py`, `audit_schema.py`, `compliance_schema.py` (module `schemas`).  
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
- Scoring engine operational (risk, compliance, performance).  
- Storage manager operational (save, load, delete, traceability).  
- Traceability engine operational (log, filter, clear records).  
- Utility toolkit operational (ID generation, timestamps, validations, JSON, safe dictionary operations).  
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
- Each sub-module must contain trilingual guides, bitácoras, and READMEs.  
- Logs stored in `logs/`.  
- Data normalized and validated before compliance, scoring, and audit.  
- Scoring, storage, and traceability integrated into institutional reports.  
- Utilities ensure consistency and reusability across modules.

---

## 📌 Conclusion

The `core/architecture` bitácora now traces the complete evolution of the sub-module and its modules (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`, `traceability`, `utils`).  
It ensures institutional traceability, documentation compliance, and technical robustness, providing a reliable foundation for digital governance and regulatory validation.
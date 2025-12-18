# BITACORA – core/architecture

---

## 📅 Activity Log

- **2025-12-18** – Updated `README_TECHNIQUE_EN.md` to include the `scoring` and `storage` modules alongside `conformity`, `collection`, `normalization`, `orchestration`, and `schemas`.  
- **2025-12-18** – Created `scoring_engine.py` (module `scoring`) to calculate institutional scores (risk, compliance, performance).  
- **2025-12-18** – Created `storage_manager.py` (module `storage`) to manage institutional storage (save, load, delete, traceability).  
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
- Trilingual documentation in place.  
- Bitácora updated.

---

## 📌 Technical Notes

- Validators integrated into CI/CD.  
- Execution sequence:  
  1. Collection  
  2. Normalization  
  3. Conformity  
  4. Orchestration  
  5. Schemas  
  6. Scoring  
  7. Storage  
- Each sub-module must contain trilingual guides, bitácoras, and READMEs.  
- Logs stored in `logs/`.  
- Data normalized and validated before compliance, scoring, and audit.  
- Scoring and storage integrated into institutional reports.

---

## 📌 Conclusion

The `core/architecture` bitácora now traces the complete evolution of the sub-module and its modules (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`).  
It ensures institutional traceability, documentation compliance, and technical robustness.
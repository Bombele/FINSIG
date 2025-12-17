# BITACORA – core/architecture

---

## 📅 Activity Log

- **2025-12-17** – Updated `README_TECHNIQUE_EN.md` to include the `collection`, `normalization`, and `orchestration` modules.  
- **2025-12-17** – Created `data_collection.py` (module `collection`) to centralize institutional data collection (CSV, JSON, API) with automatic logging (`collection_log.txt`).  
- **2025-12-17** – Created `data_normalization.py` (module `normalization`) to normalize data (dates, strings, numbers, mandatory fields, duplicates).  
- **2025-12-17** – Created `pipeline_orchestrator.py` (module `orchestration`) to orchestrate the full pipeline (collection → normalization → conformity → audit/scoring).  
- **2025-12-17** – Updated `BITACORA` and `README_TECHNIQUE` in trilingual versions (FR/EN/ES) to ensure international onboarding.  
- **2025-12-16** – Full recreation of `workflow_checker.py` to validate the trilingual documentation sequence (guides, bitácoras, technical READMEs).  
- **2025-12-16** – Updated `structure_validator.py` to strengthen mandatory file checks.  
- **2025-12-15** – Initialization of the `conformity/` sub-module with institutional validation logic.  
- **2025-12-14** – Initial structuring of the `core/architecture` sub-module with guides and documentation.

---

## ✅ Validation Status

- `structure_validator.py` and `workflow_checker.py` operational and tested locally.  
- `data_collection.py` operational, logging confirmed.  
- `data_normalization.py` operational, normalization pipeline tested.  
- `pipeline_orchestrator.py` operational, full orchestration validated.  
- Trilingual technical documentation (`FR`, `EN`, `ES`) in place for `architecture`, `collection`, `normalization`, and `orchestration`.  
- Bitácora updated to record evolutions.

---

## 📌 Technical Notes

- Validators (`structure_validator.py`, `workflow_checker.py`) must be integrated into CI/CD pipelines (`infra_technical/ci-cd/`).  
- Modules must be executed in sequence:  
  1. **Collection** (`data_collection.py`)  
  2. **Normalization** (`data_normalization.py`)  
  3. **Conformity** (`structure_validator.py`, `workflow_checker.py`)  
  4. **Orchestration** (`pipeline_orchestrator.py`) to guarantee order and traceability.  
- Each sub-module must contain:  
  - Trilingual guides (`FR`, `EN`, `ES`)  
  - Trilingual bitácoras (`FR`, `EN`, `ES`)  
  - Trilingual technical READMEs (`FR`, `EN`, `ES`)  
- Log files should be placed in `logs/` and may be ignored in `.gitignore` if not versioned.  
- Data must be normalized before passing into compliance, scoring, and audit modules.

---

## 📌 Conclusion

The `core/architecture` bitácora now traces the complete evolution of the sub-module and its associated modules (`conformity`, `collection`, `normalization`, `orchestration`).  
It ensures institutional traceability, documentation compliance, and technical robustness.
# Technical README – core/architecture

---

## 🎯 Purpose
This file provides technical instructions for using and maintaining the `core/architecture` sub-module of FINSIG, along with its associated modules (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`, `traceability`, `utils`) and their **unit tests**.  
It complements the `SUB_MODULE_GUIDE` (institutional charters) and the `BITACORA` (activity logs).

---

## 📂 Structure

### core/architecture
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Sub-module charter  
- `BITACORA_FR/EN/ES.md` → Trilingual activity log  
- `README_TECHNIQUE_FR/EN/ES.md` → Trilingual technical manual  
- `docs/ARCHITECTURE_GUIDE.md` → Structural principles  
- `conformity/structure_validator.py` → Documentation validation script  
- `conformity/workflow_checker.py` → Workflow control script  

### modules/collection
- `data_collection.py` → Data collection and validation script  
- `logs/collection_log.txt` → Traceability file for collections  

### modules/normalization
- `data_normalization.py` → Data normalization script (dates, strings, numbers, mandatory fields, duplicates)  

### modules/orchestration
- `pipeline_orchestrator.py` → Pipeline orchestration script  
- **Tests** : `tests/test_pipeline_orchestrator.py`  

### modules/schemas
- `base_schema.py` → Generic institutional schema  
- `finance_schema.py` → Schema for financial transactions  
- `audit_schema.py` → Schema for audit logs  
- `compliance_schema.py` → Schema for regulatory validations  

### modules/scoring
- `scoring_engine.py` → Institutional scoring engine (risk, compliance, performance scoring)  

### modules/storage
- `storage_manager.py` → Institutional storage manager (read, write, delete, traceability)  

### modules/traceability
- `traceability.py` → Institutional traceability engine  
- **Tests** : `tests/test_traceability.py`  

### modules/utils
- `utils.py` → Institutional utility toolkit  
- **Tests** : `tests/test_utils.py`  

---

## 📂 Unit Tests

- `tests/test_structure_validator.py` → Validation of documentation conformity  
- `tests/test_workflow_checker.py` → Validation of workflow sequences  
- `tests/test_pipeline_orchestrator.py` → Validation of the full pipeline  
- `tests/test_traceability.py` → Validation of the traceability engine  
- `tests/test_utils.py` → Validation of utility functions  

---

## ⚙️ Requirements
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions or pipelines in `infra_technical/ci-cd/`

---

## 🚀 Usage

### core/architecture
```bash
python conformity/structure_validator.py   # Validate documentation compliance
python conformity/workflow_checker.py      # Check workflows
pytest tests/                              # Run all unit tests

pytest tests/test_structure_validator.py
pytest tests/test_workflow_checker.py
pytest tests/test_pipeline_orchestrator.py
pytest tests/test_traceability.py
pytest tests/test_utils.py
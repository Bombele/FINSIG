# Technical README – core/architecture

---

## 🎯 Purpose
This file provides technical instructions for using and maintaining the `core/architecture` sub-module of FINSIG, along with its associated modules (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`).  
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
- `pipeline_orchestrator.py` → Pipeline orchestration script (collection → normalization → conformity → audit/scoring)  

### modules/schemas
- `base_schema.py` → Generic institutional schema (id, timestamp, source, value, metadata)  
- `finance_schema.py` → Schema for financial transactions  
- `audit_schema.py` → Schema for audit logs  
- `compliance_schema.py` → Schema for regulatory validations  

### modules/scoring
- `scoring_engine.py` → Institutional scoring engine (risk, compliance, performance scoring)  
- **Role**: Provide standardized and auditable scores for institutional decision-making.

### modules/storage
- `storage_manager.py` → Institutional storage manager (read, write, delete, and traceability of records)  
- **Role**: Centralize and standardize data storage, ensuring traceability and auditability.

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
pytest tests/                              # Run tests

# Collect JSON data
python data_collection.py

# Validate data compliance
pytest tests/

# Normalize a dataset
python data_normalization.py

# Validate normalized data
pytest tests/

# Run the full pipeline (collection → normalization → conformity)
python pipeline_orchestrator.py

# Validate pipeline integration
pytest tests/

python finance_schema.py                   # Validate a financial record
python audit_schema.py                     # Validate an audit log
python compliance_schema.py                # Validate a compliance rule

python scoring_engine.py                   # Calculate a score (risk, compliance, performance)

python storage_manager.py                  # Save, load, list, or delete records in storage
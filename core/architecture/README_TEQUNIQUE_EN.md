# Technical README – core/architecture

---

## 🎯 Purpose
This file provides technical instructions for using and maintaining the `core/architecture` sub-module of FINSIG, along with its associated modules (`conformity`, `collection`, `normalization`, `orchestration`).  
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

### core/architecture/modules/collection
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Module charter  
- `BITACORA_FR/EN/ES.md` → Trilingual activity log  
- `README_TECHNIQUE_FR/EN/ES.md` → Trilingual technical manual  
- `data_collection.py` → Data collection and validation script  
- `logs/collection_log.txt` → Traceability file for collections  

### core/architecture/modules/normalization
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Module charter  
- `BITACORA_FR/EN/ES.md` → Trilingual activity log  
- `README_TECHNIQUE_FR/EN/ES.md` → Trilingual technical manual  
- `data_normalization.py` → Data normalization script (dates, strings, numbers, mandatory fields, duplicates)  

### core/architecture/modules/orchestration
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Module charter  
- `BITACORA_FR/EN/ES.md` → Trilingual activity log  
- `README_TECHNIQUE_FR/EN/ES.md` → Trilingual technical manual  
- `pipeline_orchestrator.py` → Pipeline orchestration script (collection → normalization → conformity → audit/scoring)  

---

## ⚙️ Requirements

### core/architecture
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions or pipelines in `infra_technical/ci-cd/`

### modules/collection
- Python 3.10+  
- Standard modules (`csv`, `json`, `datetime`)  

### modules/normalization
- Python 3.10+  
- Standard modules (`datetime`)  

### modules/orchestration
- Python 3.10+  
- Internal dependencies (`data_collection`, `data_normalization`, `structure_validator`, `workflow_checker`)  

---

## 🚀 Usage

### core/architecture
```bash
# Validate documentation compliance
python conformity/structure_validator.py

# Check workflows
python conformity/workflow_checker.py

# Run tests
pytest tests/

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
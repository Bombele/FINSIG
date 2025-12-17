# Technical README – core/architecture & modules/collection

---

## 🎯 Purpose
This file provides technical instructions for using and maintaining the `core/architecture` sub-module and its `collection` module.  
It complements the `SUB_MODULE_GUIDE` (institutional charters) and the `BITACORA` (activity logs).

---

## 📂 Structure

### core/architecture
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Sub-module charter.  
- `BITACORA_FR/EN/ES.md` → Trilingual activity log.  
- `README_TECHNIQUE_FR/EN/ES.md` → Trilingual technical manual.  
- `docs/ARCHITECTURE_GUIDE.md` → Structural principles.  
- `conformity/structure_validator.py` → Documentation validation script.  
- `conformity/workflow_checker.py` → Workflow control script.

### core/architecture/modules/collection
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Module charter.  
- `BITACORA_FR/EN/ES.md` → Trilingual activity log.  
- `README_TECHNIQUE_FR/EN/ES.md` → Trilingual technical manual.  
- `data_collection.py` → Data collection and validation script.  
- `logs/collection_log.txt` → Traceability file for collections.

---

## ⚙️ Requirements

### core/architecture
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions or pipelines in `infra_technical/ci-cd/`

### modules/collection
- Python 3.10+  
- Standard modules (`csv`, `json`, `datetime`)  
- CI/CD: GitHub Actions or pipelines in `infra_technical/ci-cd/`

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
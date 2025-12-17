---

## 🇬🇧 README_TECHNIQUE_EN.md

```markdown
# Technical README – core/architecture

---

## 🎯 Purpose
This file provides technical instructions for using and maintaining the `core/architecture` sub-module of FINSIG.  
It complements the `SUB_MODULE_GUIDE` (institutional charter) and the `BITACORA` (activity log).

---

## 📂 Structure
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Sub-module charter.  
- `BITACORA_FR/EN/ES.md` → Trilingual activity log.  
- `README_TECHNIQUE_FR/EN/ES.md` → Trilingual technical manual.  
- `docs/ARCHITECTURE_GUIDE.md` → Structural principles.  
- `conformity/structure_validator.py` → Validation script.  
- `conformity/workflow_checker.py` → Workflow control script.

---

## ⚙️ Requirements
- Python 3.10+  
- Frameworks: `pytest`, `pydantic`  
- CI/CD: GitHub Actions or pipelines in `infra_technical/ci-cd/`

---

## 🚀 Usage
```bash
# Validate documentation compliance
python conformity/structure_validator.py

# Check workflows
python conformity/workflow_checker.py

# Run tests
pytest tests/
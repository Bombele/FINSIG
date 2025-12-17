# README Technique – core/architecture

---

## 🎯 Objectif
Ce fichier fournit les instructions techniques pour utiliser et maintenir le sous-module `core/architecture` de FINSIG.  
Il complète le `SUB_MODULE_GUIDE` (charte institutionnelle) et la `BITACORA` (journal des activités).

---

## 📂 Structure
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Charte du sous-module.  
- `BITACORA_FR/EN/ES.md` → Journal de bord trilingue.  
- `README_TECHNIQUE_FR/EN/ES.md` → Manuel technique trilingue.  
- `docs/ARCHITECTURE_GUIDE.md` → Principes structuraux.  
- `conformity/structure_validator.py` → Script de validation.  
- `conformity/workflow_checker.py` → Script de contrôle des workflows.

---

## ⚙️ Prérequis
- Python 3.10+  
- Frameworks : `pytest`, `pydantic`  
- CI/CD : GitHub Actions ou pipelines `infra_technical/ci-cd/`

---

## 🚀 Utilisation
```bash
# Vérifier la conformité documentaire
python conformity/structure_validator.py

# Vérifier les workflows
python conformity/workflow_checker.py

# Lancer les tests
pytest tests/
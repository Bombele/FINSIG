# README Technique – core/architecture & modules/collection

---

## 🎯 Objectif
Ce fichier fournit les instructions techniques pour utiliser et maintenir le sous-module `core/architecture` ainsi que son module `collection`.  
Il complète les `SUB_MODULE_GUIDE` (chartes institutionnelles) et les `BITACORA` (journaux des activités).

---

## 📂 Structure

### core/architecture
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Charte du sous-module.  
- `BITACORA_FR/EN/ES.md` → Journal de bord trilingue.  
- `README_TECHNIQUE_FR/EN/ES.md` → Manuel technique trilingue.  
- `docs/ARCHITECTURE_GUIDE.md` → Principes structuraux.  
- `conformity/structure_validator.py` → Script de validation documentaire.  
- `conformity/workflow_checker.py` → Script de contrôle des workflows.

### core/architecture/modules/collection
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Charte du module.  
- `BITACORA_FR/EN/ES.md` → Journal de bord trilingue.  
- `README_TECHNIQUE_FR/EN/ES.md` → Manuel technique trilingue.  
- `data_collection.py` → Script de collecte et validation des données.  
- `logs/collection_log.txt` → Fichier de traçabilité des collectes.

---

## ⚙️ Prérequis

### core/architecture
- Python 3.10+  
- Frameworks : `pytest`, `pydantic`  
- CI/CD : GitHub Actions ou pipelines `infra_technical/ci-cd/`

### modules/collection
- Python 3.10+  
- Modules standards (`csv`, `json`, `datetime`)  
- CI/CD : GitHub Actions ou pipelines `infra_technical/ci-cd/`

---

## 🚀 Utilisation

### core/architecture
```bash
# Vérifier la conformité documentaire
python conformity/structure_validator.py

# Vérifier les workflows
python conformity/workflow_checker.py

# Lancer les tests
pytest tests/
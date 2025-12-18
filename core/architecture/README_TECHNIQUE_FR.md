# README Technique – core/architecture

---

## 🎯 Objectif
Ce fichier fournit les instructions techniques pour utiliser et maintenir le sous-module `core/architecture` de FINSIG, ainsi que ses modules associés (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`, `traceability`, `utils`) et leurs **tests unitaires**.  
Il complète les `SUB_MODULE_GUIDE` (chartes institutionnelles) et les `BITACORA` (journaux des activités).

---

## 📂 Structure

### core/architecture
- `SUB_MODULE_GUIDE_FR/EN/ES.md` → Charte du sous-module  
- `BITACORA_FR/EN/ES.md` → Journal de bord trilingue  
- `README_TECHNIQUE_FR/EN/ES.md` → Manuel technique trilingue  
- `docs/ARCHITECTURE_GUIDE.md` → Principes structuraux  
- `conformity/structure_validator.py` → Script de validation documentaire  
- `conformity/workflow_checker.py` → Script de contrôle des workflows  

### modules/collection
- `data_collection.py` → Script de collecte et validation des données  
- `logs/collection_log.txt` → Fichier de traçabilité des collectes  

### modules/normalization
- `data_normalization.py` → Script de normalisation des données (dates, chaînes, nombres, champs obligatoires, doublons)  

### modules/orchestration
- `pipeline_orchestrator.py` → Script d’orchestration du pipeline  
- **Tests** : `tests/test_pipeline_orchestrator.py`  

### modules/schemas
- `base_schema.py` → Schéma institutionnel générique  
- `finance_schema.py` → Schéma pour les transactions financières  
- `audit_schema.py` → Schéma pour les journaux d’audit  
- `compliance_schema.py` → Schéma pour les validations réglementaires  

### modules/scoring
- `scoring_engine.py` → Moteur institutionnel de scoring (risque, conformité, performance)  

### modules/storage
- `storage_manager.py` → Gestionnaire institutionnel de stockage (lecture, écriture, suppression, traçabilité)  

### modules/traceability
- `traceability.py` → Moteur de traçabilité institutionnelle  
- **Tests** : `tests/test_traceability.py`  

### modules/utils
- `utils.py` → Ensemble d’utilitaires institutionnels  
- **Tests** : `tests/test_utils.py`  

---

## 📂 Tests unitaires

- `tests/test_structure_validator.py` → Validation de la conformité documentaire  
- `tests/test_workflow_checker.py` → Validation des séquences de workflow  
- `tests/test_pipeline_orchestrator.py` → Validation du pipeline complet  
- `tests/test_traceability.py` → Validation du moteur de traçabilité  
- `tests/test_utils.py` → Validation des fonctions utilitaires  

---

## ⚙️ Prérequis
- Python 3.10+  
- Frameworks : `pytest`, `pydantic`  
- CI/CD : GitHub Actions ou pipelines `infra_technical/ci-cd/`

---

## 🚀 Utilisation

### core/architecture
```bash
python conformity/structure_validator.py   # Vérifier la conformité documentaire
python conformity/workflow_checker.py      # Vérifier les workflows
pytest tests/                              # Lancer tous les tests unitaires

pytest tests/test_structure_validator.py
pytest tests/test_workflow_checker.py
pytest tests/test_pipeline_orchestrator.py
pytest tests/test_traceability.py
pytest tests/test_utils.py
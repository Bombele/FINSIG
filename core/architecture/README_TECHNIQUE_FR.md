# README Technique – core/architecture

---

## 🎯 Objectif
Ce fichier fournit les instructions techniques pour utiliser et maintenir le sous-module `core/architecture` de FINSIG, ainsi que ses modules associés (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`, `storage`).  
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
- `pipeline_orchestrator.py` → Script d’orchestration du pipeline (collecte → normalisation → conformité → audit/scoring)  

### modules/schemas
- `base_schema.py` → Schéma institutionnel générique (id, timestamp, source, valeur, métadonnées)  
- `finance_schema.py` → Schéma pour les transactions financières  
- `audit_schema.py` → Schéma pour les journaux d’audit  
- `compliance_schema.py` → Schéma pour les validations réglementaires  

### modules/scoring
- `scoring_engine.py` → Moteur institutionnel de scoring (calcul des scores de risque, conformité, performance)  
- **Rôle** : fournir des scores standardisés et auditables pour la prise de décision institutionnelle.

### modules/storage
- `storage_manager.py` → Gestionnaire institutionnel de stockage (lecture, écriture, suppression et traçabilité des enregistrements)  
- **Rôle** : centraliser et standardiser le stockage des données, garantissant traçabilité et auditabilité.

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
pytest tests/                              # Lancer les tests

# Collecter des données JSON
python data_collection.py

# Normaliser un jeu de données
python data_normalization.py

# Exécuter le pipeline complet
python pipeline_orchestrator.py

# Valider un enregistrement financier
python finance_schema.py

# Valider un journal d’audit
python audit_schema.py

# Valider une règle de conformité
python compliance_schema.py

python scoring_engine.py                   # Calculer un score (risque, conformité, performance)

python storage_manager.py                  # Sauvegarder, charger, lister ou supprimer des enregistrements
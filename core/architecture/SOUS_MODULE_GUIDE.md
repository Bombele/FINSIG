# SOUS_MODULE_GUIDE – core/architecture

---

## 🎯 Objectif
Ce guide définit la structure et les responsabilités des sous-modules du répertoire `core/architecture`.  
Il garantit la cohérence institutionnelle, la traçabilité et l’auditabilité de FINSIG.

---

## 📂 Sous-modules

### 1. conformity/
- **structure_validator.py** → Vérifie la présence et la conformité des fichiers obligatoires.  
- **workflow_checker.py** → Contrôle la séquence documentaire et la cohérence des workflows.  
- **Rôle** : Assurer la conformité documentaire et institutionnelle.

### 2. collection/
- **data_collection.py** → Collecte et valide les données brutes (CSV, JSON, API).  
- **logs/collection_log.txt** → Journalisation des collectes pour traçabilité.  
- **Rôle** : Centraliser la collecte institutionnelle et garantir la traçabilité.

### 3. normalization/
- **data_normalization.py** → Normalise les données (dates, chaînes, nombres, champs obligatoires, doublons).  
- **Rôle** : Standardiser les données pour assurer leur compatibilité avec les modules de conformité et d’audit.

### 4. orchestration/
- **pipeline_orchestrator.py** → Orchestration du pipeline complet (collecte → normalisation → conformité → audit/scoring).  
- **Rôle** : Garantir l’ordre, la traçabilité et l’intégration des étapes.

### 5. schemas/
- **base_schema.py** → Schéma institutionnel générique (id, timestamp, source, valeur, métadonnées).  
- **finance_schema.py** → Schéma pour les transactions financières.  
- **audit_schema.py** → Schéma pour les journaux d’audit.  
- **compliance_schema.py** → Schéma pour les validations réglementaires.  
- **Rôle** : Définir les structures normalisées des données pour tous les modules, assurer la cohérence et l’auditabilité.

---

## ⚙️ Prérequis
- Python 3.10+  
- Frameworks : `pytest`, `pydantic`  
- CI/CD : GitHub Actions ou pipelines `infra_technical/ci-cd/`

---

## 📌 Bonnes pratiques
- Respecter la nomenclature trilingue (`FR`, `EN`, `ES`) pour guides, bitácoras et README techniques.  
- Mettre à jour la `BITACORA` après chaque modification.  
- Normaliser les données avant passage dans les modules compliance, scoring et audit.  
- Utiliser `pipeline_orchestrator.py` comme point d’entrée pour garantir l’ordre et la traçabilité.  
- Centraliser les schémas dans `schemas/` pour éviter les divergences entre modules.  

---

## 📌 Conclusion
Le sous-module `core/architecture` est désormais composé de cinq modules clés : `conformity`, `collection`, `normalization`, `orchestration`, et `schemas`.  
Cette structuration garantit une gouvernance technique robuste, une conformité documentaire et une traçabilité institutionnelle.
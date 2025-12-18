# README TECHNIQUE – core/architecture

---

## 🎯 Objectif
Ce module définit l’architecture institutionnelle de FINSIG.  
Il garantit la cohérence documentaire, la traçabilité et l’auditabilité via des sous-modules, des schémas normalisés et des tests unitaires.

---

## 📂 Sous-modules

### 1. conformity/
- **structure_validator.py** → Vérifie la présence et la conformité des fichiers obligatoires.  
- **workflow_checker.py** → Contrôle la séquence documentaire et la cohérence des workflows.  
- **Validation croisée** : vérifie l’intégrité des signatures SHA256 dans `audit_schema.py` et `compliance_schema.py`.

### 2. collection/
- **data_collection.py** → Collecte et valide les données brutes (CSV, JSON, API).  
- **logs/collection_log.txt** → Journalisation des collectes pour traçabilité.

### 3. normalization/
- **data_normalization.py** → Normalise les données (dates, chaînes, nombres, champs obligatoires, doublons).

### 4. orchestration/
- **pipeline_orchestrator.py** → Orchestration du pipeline complet (collecte → normalisation → conformité → audit/scoring).  
- **Tests de dépendances** : assure que chaque étape échoue si la précédente n’est pas exécutée correctement.

### 5. schemas/
- **base_schema.py** → Schéma institutionnel générique.  
- **finance_schema.py** → Schéma pour transactions financières.  
- **audit_schema.py** → Schéma pour journaux d’audit, inclut `version` et `signature` (SHA256).  
- **compliance_schema.py** → Schéma pour validations réglementaires, inclut `version` et `signature` (SHA256).  
- **generate_signature()** → Génère une signature cryptographique pour garantir intégrité et authenticité.

### 6. traceability/
- **traceability.py** → Moteur de traçabilité institutionnelle.  
  - Horodatage en UTC (ISO 8601).  
  - Export CSV via `export_to_csv()` pour audit externe.

### 7. utils/
- **utils.py** → Fonctions utilitaires institutionnelles (validation, JSON, fusion de dictionnaires).  
- Cas limites testés : valeurs `None`, chaînes invalides, dictionnaires vides.

---

## 📂 tests/
- **test_structure_validator.py**  
- **test_workflow_checker.py**  
- **test_pipeline_orchestrator.py**  
- **test_traceability.py**  
- **test_utils.py**  
- **test_audit_schema.py**  
- **test_compliance_schema.py**

---

## 📂 workflows/
- **tests.yml** → Workflow GitHub Actions exécutant `pytest` et la couverture sur chaque commit/PR.

---

## 📌 Conclusion
Le module `core/architecture` est complet, robuste et auditable : signatures SHA256, horodatage UTC, export CSV et CI/CD garantissent une gouvernance technique solide.
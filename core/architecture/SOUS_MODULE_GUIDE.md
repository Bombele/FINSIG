# SOUS_MODULE_GUIDE – Architecture

## 🎯 Objectif du sous-module
Le sous-module `architecture/` définit l’ossature technique et institutionnelle de FINSIG.  
Il garantit la cohérence des modules, la modularité des dossiers et l’intégration des workflows CI/CD pour assurer robustesse, traçabilité et adoption institutionnelle.

---

## 📑 Portée
- Structuration des branches et dossiers (`docs/`, `conformity/`, `schemas/`, `tests/`, `workflows/`).  
- Organisation des scripts racine en modules thématiques.  
- Validation automatique de la structure via CI/CD.  
- Alignement avec les standards ISO/IEC pour architecture logicielle et gouvernance technique.  

---

## 📂 Structure des dossiers

### 📂 docs/
- **ARCHITECTURE_GUIDE.md** → principes d’architecture, organisation des modules, standards ISO/IEC.  

### 📂 conformity/
- **structure_validator.py** → vérifie la cohérence de l’organisation des dossiers et fichiers.  
- **workflow_checker.py** → contrôle la présence et la validité des workflows CI/CD.  

### 📂 modules/
- **collection/data_collection.py** → collecte des données institutionnelles.  
- **normalization/normalization.py** → standardisation des formats.  
- **orchestration/pipeline_orchestrator.py** → orchestration des workflows.  
- **schemas/schema_design.py** → conception des schémas.  
- **scoring/scoring_engine.py** → évaluation et scoring.  
- **storage/storage_manager.py** → gestion du stockage.  
- **traceability/traceability.py** → journalisation et suivi.  
- **utils/utils.py** → fonctions utilitaires partagées.  

### 📂 tests/
- **test_structure_validator.py** → tests sur la cohérence de la structure.  
- **test_workflow_checker.py** → tests sur la validité des workflows CI/CD.  
- **test_pipeline_orchestrator.py** → tests sur l’orchestration des modules.  

---

## 🔄 Workflows CI/CD intégrés

### 📂 .github/workflows/
- **architecture.yml**  
  - Vérifie la cohérence des dossiers et fichiers.  
  - Contrôle la conformité avec `architecture_schema.json`.  
  - Export des résultats dans `reports/architecture/`.  

- **workflow-validation.yml**  
  - Vérifie la présence des workflows obligatoires (`ci.yml`, `lint.yml`, `tests.yml`).  
  - Contrôle de la syntaxe et de la validité YAML.  
  - Journalisation dans `BITACORA.md`.  

- **integration.yml**  
  - Vérifie l’interopérabilité entre les modules.  
  - Contrôle des imports et dépendances.  
  - Génère des rapports consolidés.  

---

## ⚙️ Fonctionnement
- Les scripts racine sont réorganisés dans des dossiers thématiques pour modularité.  
- Les validateurs (`structure_validator.py`, `workflow_checker.py`) assurent la conformité.  
- Les workflows CI/CD garantissent la robustesse et la traçabilité.  
- Les résultats sont journalisés dans `BITACORA.md` et exportés dans `reports/`.  

---

## ✅ Impact institutionnel
- **Robustesse** : architecture cohérente et validée en continu.  
- **Interopérabilité** : intégration harmonieuse des modules transversaux.  
- **Traçabilité** : journalisation et reporting des choix architecturaux.  
- **Certification** : alignement avec les standards ISO/IEC.  

---

## 📌 Conclusion
Le sous-module `architecture/` est le **socle technique et documentaire** de FINSIG.  
Placé à la racine du projet, il garantit que l’infrastructure est organisée, traçable et conforme aux standards internationaux, renforçant la confiance et l’adoption institutionnelle.

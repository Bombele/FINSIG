# BITACORA – core/architecture

---

## 📅 Journal des activités

- **2025-12-18** – Mise à jour du `README_TECHNIQUE_FR.md` pour inclure le module `scoring` en plus de `conformity`, `collection`, `normalization`, `orchestration` et `schemas`.  
- **2025-12-18** – Création du fichier `scoring_engine.py` (module `scoring`) pour calculer des scores institutionnels (risque, conformité, performance).  
- **2025-12-17** – Mise à jour du `README_TECHNIQUE_FR.md` pour inclure le module `schemas`.  
- **2025-12-17** – Création du fichier `base_schema.py` (module `schemas`) pour définir le schéma institutionnel générique.  
- **2025-12-17** – Création du fichier `finance_schema.py` (module `schemas`) pour tracer les transactions financières avec conformité ISO 4217.  
- **2025-12-17** – Création du fichier `audit_schema.py` (module `schemas`) pour tracer les journaux d’audit institutionnels.  
- **2025-12-17** – Création du fichier `compliance_schema.py` (module `schemas`) pour tracer les validations réglementaires et institutionnelles.  
- **2025-12-17** – Mise à jour des `BITACORA` et `README_TECHNIQUE` en versions trilingues (FR/EN/ES) pour garantir l’onboarding international.  
- **2025-12-17** – Création du script `pipeline_orchestrator.py` (module `orchestration`) pour orchestrer le pipeline complet (collecte → normalisation → conformité → audit/scoring).  
- **2025-12-16** – Recréation complète du script `workflow_checker.py` pour valider la séquence documentaire trilingue (guides, bitácoras, README techniques).  
- **2025-12-16** – Mise à jour du `structure_validator.py` pour renforcer la vérification des fichiers obligatoires.  
- **2025-12-15** – Initialisation du sous-module `conformity/` avec logique de validation institutionnelle.  
- **2025-12-14** – Structuration initiale du sous-module `core/architecture` avec guides et documentation.

---

## ✅ État des validations

- `structure_validator.py` et `workflow_checker.py` opérationnels et testés en local.  
- `data_collection.py` opérationnel, journalisation confirmée.  
- `data_normalization.py` opérationnel, pipeline de normalisation testé.  
- `pipeline_orchestrator.py` opérationnel, orchestration complète validée.  
- `schemas/` opérationnel avec schémas validés (`base`, `finance`, `audit`, `compliance`).  
- `scoring_engine.py` opérationnel, calculs de scoring validés (risque, conformité, performance).  
- Documentation technique trilingue (`FR`, `EN`, `ES`) en place pour tous les modules.  
- Bitácora mise à jour pour consigner les évolutions.

---

## 📌 Notes techniques

- Les validateurs (`structure_validator.py`, `workflow_checker.py`) doivent être intégrés dans les pipelines CI/CD (`infra_technical/ci-cd/`).  
- Les modules doivent être exécutés en séquence :  
  1. **Collecte** (`data_collection.py`)  
  2. **Normalisation** (`data_normalization.py`)  
  3. **Conformité** (`structure_validator.py`, `workflow_checker.py`)  
  4. **Orchestration** (`pipeline_orchestrator.py`)  
  5. **Schemas** (`base_schema.py`, `finance_schema.py`, `audit_schema.py`, `compliance_schema.py`)  
  6. **Scoring** (`scoring_engine.py`) pour produire des scores institutionnels.  
- Chaque sous-module doit contenir :  
  - Guides trilingues (`FR`, `EN`, `ES`)  
  - Bitácoras trilingues (`FR`, `EN`, `ES`)  
  - README techniques trilingues (`FR`, `EN`, `ES`)  
- Les fichiers de log doivent être placés dans `logs/` et peuvent être ignorés dans `.gitignore` si non versionnés.  
- Les données doivent être normalisées et validées par les schémas avant passage dans les modules compliance, scoring et audit.  
- Les résultats du scoring doivent être intégrés dans les rapports institutionnels et les audits.

---

## 📌 Conclusion

La bitácora `core/architecture` trace désormais l’évolution complète du sous-module et de ses modules associés (`conformity`, `collection`, `normalization`, `orchestration`, `schemas`, `scoring`).  
Elle garantit la traçabilité institutionnelle, la conformité documentaire et la robustesse technique.
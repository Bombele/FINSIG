# BITACORA – core/architecture

---

## 📅 Journal des activités

- **2025-12-17** – Mise à jour du `README_TECHNIQUE_FR.md` pour intégrer les modules `collection` et `normalization`.  
- **2025-12-17** – Création du script `data_collection.py` (module `collection`) pour centraliser la collecte institutionnelle de données (CSV, JSON, API) avec journalisation automatique (`collection_log.txt`).  
- **2025-12-17** – Création du script `data_normalization.py` (module `normalization`) pour normaliser les données (dates, chaînes, nombres, champs obligatoires, doublons).  
- **2025-12-17** – Mise à jour des `BITACORA` et `README_TECHNIQUE` en versions trilingues (FR/EN/ES) pour garantir l’onboarding international.  
- **2025-12-16** – Recréation complète du script `workflow_checker.py` pour valider la séquence documentaire trilingue (guides, bitácoras, README techniques).  
- **2025-12-16** – Mise à jour du `structure_validator.py` pour renforcer la vérification des fichiers obligatoires.  
- **2025-12-15** – Initialisation du sous-module `conformity/` avec logique de validation institutionnelle.  
- **2025-12-14** – Structuration initiale du sous-module `core/architecture` avec guides et documentation.

---

## ✅ État des validations

- `structure_validator.py` et `workflow_checker.py` opérationnels et testés en local.  
- `data_collection.py` opérationnel, journalisation confirmée.  
- `data_normalization.py` opérationnel, pipeline de normalisation testé.  
- Documentation technique trilingue (`FR`, `EN`, `ES`) en place pour `architecture`, `collection` et `normalization`.  
- Bitácora mise à jour pour consigner les évolutions.

---

## 📌 Notes techniques

- Les validateurs (`structure_validator.py`, `workflow_checker.py`) doivent être intégrés dans les pipelines CI/CD (`infra_technical/ci-cd/`).  
- Les modules `collection` et `normalization` doivent être exécutés en séquence :  
  1. **Collecte** (`data_collection.py`)  
  2. **Normalisation** (`data_normalization.py`)  
  3. **Conformité** (`structure_validator.py`, `workflow_checker.py`)  
- Chaque sous-module doit contenir :  
  - Guides trilingues (`FR`, `EN`, `ES`)  
  - Bitácoras trilingues (`FR`, `EN`, `ES`)  
  - README techniques trilingues (`FR`, `EN`, `ES`)  
- Les fichiers de log doivent être placés dans `logs/` et peuvent être ignorés dans `.gitignore` si non versionnés.  
- Les données doivent être normalisées avant passage dans les modules compliance, scoring et audit.

---

## 📌 Conclusion

La bitácora `core/architecture` trace désormais l’évolution complète du sous-module et de ses modules associés (`collection`, `normalization`, `conformity`).  
Elle garantit la traçabilité institutionnelle, la conformité documentaire et la robustesse technique.
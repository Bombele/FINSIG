# BITACORA – core/architecture/conformity

---

## 📅 Journal des activités

- **2025-12-17** – Recréation complète du script `workflow_checker.py` pour valider la séquence documentaire trilingue (guides, bitácoras, README techniques).  
- **2025-12-17** – Mise à jour du `structure_validator.py` pour renforcer la vérification des fichiers obligatoires.  
- **2025-12-17** – Ajout des modèles trilingues pour `README_TECHNIQUE` afin d’uniformiser la documentation technique.  
- **2025-12-16** – Initialisation du sous-module `conformity/` avec logique de validation institutionnelle.

---

## ✅ État des validations

- `workflow_checker.py` opérationnel et testé en local.  
- `structure_validator.py` validé, en attente d’intégration CI/CD.  
- Documentation technique trilingue en cours de déploiement.  
- Bitácora mise à jour pour consigner les évolutions.

---

## 📌 Notes techniques

- Les validateurs (`workflow_checker.py`, `structure_validator.py`) doivent être intégrés dans les pipelines CI/CD (`infra_technical/ci-cd/`).  
- Chaque sous-module doit contenir :  
  - Guides trilingues (`FR`, `EN`, `ES`)  
  - Bitácoras trilingues (`FR`, `EN`, `ES`)  
  - README techniques trilingues (`FR`, `EN`, `ES`)  
- Les scripts de conformité doivent être exécutés avant chaque merge pour garantir la robustesse documentaire et institutionnelle.

# BITACORA – core/architecture/modules/collection

---

## 📅 Journal des activités

- **2025-12-17** – Création du script `data_collection.py` pour centraliser la collecte institutionnelle de données (CSV, JSON, API).  
- **2025-12-17** – Mise en place de la logique de validation (présence du champ `id`) et journalisation automatique dans `collection_log.txt`.  
- **2025-12-17** – Recommandation de créer un dossier `logs/` pour stocker les fichiers de suivi et éviter l’encombrement de la racine.  
- **2025-12-16** – Initialisation du sous-module `collection/` avec logique de collecte et traçabilité.

---

## ✅ État des validations

- `data_collection.py` opérationnel et testé en local.  
- Journalisation automatique confirmée (`collection_log.txt` généré lors de la première exécution).  
- Dossier `logs/` recommandé pour une meilleure organisation.  
- Bitácora mise à jour pour consigner les évolutions.

---

## 📌 Notes techniques

- Les fichiers de log doivent être placés dans `logs/` et peuvent être ignorés dans `.gitignore` si non versionnés.  
- Chaque collecte doit être validée avant intégration dans les modules compliance et audit.  
- Les futures étapes incluent :  
  - Ajout de règles de validation avancées (format, champs obligatoires).  
  - Intégration avec `infra-technical/checks` pour automatiser la conformité.
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
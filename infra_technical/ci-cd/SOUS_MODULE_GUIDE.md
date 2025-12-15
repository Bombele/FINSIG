# SOUS_MODULE_GUIDE – CI/CD

## 🎯 Objectif du sous-module
Le sous-module `ci-cd/` est dédié au **développement, expérimentation et durcissement des workflows CI/CD**.  
Il permet de tester, valider et améliorer les configurations avant leur intégration officielle dans la branche principale `finsig/`.

---

## 📂 Structure des dossiers

### 📂 docs/
- **CI_CD_GUIDE.md** → principes de conception des workflows CI/CD, méthodologie et standards institutionnels.

### 📂 workflows/
- **ci.yml** → pipeline de tests unitaires et intégration.  
- **lint.yml** → vérification de la qualité du code (flake8, mypy).  
- **build.yml** → installation et validation des dépendances.  

### 📂 configs/
- **pyproject.toml** → définition des dépendances Python.  
- **requirements.txt** → liste des dépendances expérimentales.  
- **mypy.ini** → configuration de la vérification statique des types.  
- **pytest.ini** → standardisation des tests unitaires et d’intégration.  

### 📂 utils/
- **ci_cd_utils.py** → fonctions utilitaires pour automatiser les pipelines CI/CD (logs signés, horodatages, hashage).  

### 📂 schemas/
- **ci_cd_schema.json** → schéma de validation des workflows et artefacts CI/CD.  

### 📂 tests/
- **test_ci.yml** → Vérifie la validité du pipeline CI.  
- **test_lint.yml** → Vérifie la qualité du code.  
- **test_build.yml** → Vérifie l’installation et la reproductibilité des dépendances.  
- **test_ci_cd_utils.py** → Vérifie la robustesse des fonctions utilitaires CI/CD.  

---

## 🔄 Workflows CI/CD intégrés

### 📂 .github/workflows/
- **ci-validation.yml**  
  → Pipeline principal :  
  - Exécution des tests unitaires et d’intégration.  
  - Vérification de la robustesse des dépendances.  
  - Export des résultats dans `reports/ci-cd/`.

- **lint-check.yml**  
  → Pipeline de qualité :  
  - Vérification du code avec flake8 et mypy.  
  - Contrôle des règles définies dans `mypy.ini`.  
  - Journalisation des résultats dans `BITACORA.md`.

- **build-validation.yml**  
  → Pipeline de build :  
  - Vérification de l’installation des dépendances (`requirements.txt`).  
  - Contrôle de la reproductibilité des environnements.  
  - Signature et hash des rapports.  

---

## ⚙️ Fonctionnement
- Les workflows sont définis dans `workflows/` et validés par les configurations (`configs/`).  
- Les utilitaires (`utils/`) assurent la traçabilité et la sécurité des pipelines.  
- Les schémas (`schemas/`) garantissent la cohérence et la conformité des workflows.  
- Les tests (`tests/`) valident la robustesse et la reproductibilité des pipelines.  

---

## 🧭 Gouvernance et impact institutionnel
- **Expérimentation contrôlée** : le sous-module `ci-cd/` sert de laboratoire pour tester les workflows.  
- **Traçabilité** : chaque modification est documentée dans `BITACORA.md`.  
- **Institutionnalisation** : une fois validés, les workflows sont fusionnés dans `finsig/`.  
- **Impact** : garantit robustesse et reproductibilité avant adoption officielle.  

---

## ✅ Conclusion
Le sous-module `ci-cd/` est le **laboratoire technique de FINSIG**.  
Il permet de tester et durcir les workflows CI/CD avant leur intégration institutionnelle dans la branche principale `finsig/`, assurant robustesse, conformité et traçabilité.

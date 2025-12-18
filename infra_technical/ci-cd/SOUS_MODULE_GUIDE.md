# SOUS_MODULE_GUIDE – CI/CD

---

## 🎯 Objectif du sous-module

Le sous-module `ci-cd/` est dédié au **développement, expérimentation et durcissement des workflows CI/CD**.  
Il permet de tester, valider et améliorer les configurations avant leur intégration officielle dans la branche principale `finsig/`.

---

## 📂 Structure des dossiers

### 📂 docs/
- **CI_CD_GUIDE.md** → principes de conception des workflows CI/CD, méthodologie et standards institutionnels.  
- **README_TECHNIQUE_FR.md / EN / ES** → documentation trilingue du pipeline CI/CD.  
- **BITACORA_CI-CD_FR.md / EN / ES** → journal institutionnel des évolutions CI/CD.

### 📂 workflows/
- **ci.yml** → pipeline global d’intégration continue.  
- **tests.yml** → exécution des tests unitaires avec couverture.  
- **lint.yml** → vérification du code (flake8 + bandit).  
- **build.yml** → packaging Python et vérification d’installabilité.  
- **docker.yml** → construction et push de l’image Docker vers GHCR.  
- **deploy.yml** → déploiement staging via docker-compose.  
- **prometheus.yml** → configuration du monitoring Prometheus.  
- **alert_rules.yml** → règles d’alerte critiques (app down, DB down, CPU/mémoire).  
- **docker-compose.yml** → environnement complet (app, db, exporters, monitoring).

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
- **test_ci.yml** → vérifie la validité du pipeline CI.  
- **test_lint.yml** → vérifie la qualité du code.  
- **test_build.yml** → vérifie l’installation et la reproductibilité des dépendances.  
- **test_ci_cd_utils.py** → vérifie la robustesse des fonctions utilitaires CI/CD.

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

- **docker-pipeline.yml**  
  → Pipeline de conteneurisation :  
  - Construction de l’image Docker.  
  - Push vers GHCR.  
  - Vérification de l’intégrité de l’image.

- **deploy-staging.yml**  
  → Pipeline de déploiement :  
  - Simulation via `docker-compose`.  
  - Services : app, db, monitoring, exporters.  
  - Healthchecks intégrés.

---

## ⚙️ Fonctionnement

- Les workflows sont définis dans `workflows/` et validés par les configurations (`configs/`).  
- Les utilitaires (`utils/`) assurent la traçabilité et la sécurité des pipelines.  
- Les schémas (`schemas/`) garantissent la cohérence et la conformité des workflows.  
- Les tests (`tests/`) valident la robustesse et la reproductibilité des pipelines.  
- Les fichiers `prometheus.yml` et `alert_rules.yml` assurent le monitoring et les alertes.  
- Le `docker-compose.yml` permet un déploiement local complet et auditable.

---

## 🧭 Gouvernance et impact institutionnel

- **Expérimentation contrôlée** : le sous-module `ci-cd/` sert de laboratoire pour tester les workflows.  
- **Traçabilité** : chaque modification est documentée dans `BITACORA_CI-CD_FR.md`.  
- **Institutionnalisation** : une fois validés, les workflows sont fusionnés dans `finsig/`.  
- **Impact** : garantit robustesse, reproductibilité et auditabilité avant adoption officielle.

---

## ✅ Conclusion

Le sous-module `ci-cd/` est le **laboratoire technique de FINSIG**.  
Il permet de tester et durcir les workflows CI/CD avant leur intégration institutionnelle dans la branche principale `finsig/`, assurant robustesse, conformité, traçabilité et monitoring.

# SOUS_MODULE_GUIDE – CI/CD


## 🎯 Objectif du sous-module

Le sous-module `ci-cd/` est dédié au **développement, expérimentation et durcissement des workflows CI/CD**.  
Il permet de tester, valider et améliorer les configurations avant leur intégration officielle dans la branche principale `finsig/`.



## 📂 Structure des dossiers

### 📂 docs/
- CI_CD_GUIDE.md → principes de conception des workflows CI/CD, méthodologie et standards institutionnels.  
- README_TECHNIQUE_FR.md / EN / ES → documentation trilingue du pipeline CI/CD.  
- BITACORA_CI-CD_FR.md / EN / ES → journal institutionnel des évolutions CI/CD.

### 📂 workflows/
- ci.yml → pipeline global d’intégration continue.  
- tests.yml → exécution des tests unitaires avec couverture.  
- lint.yml → vérification du code (flake8 + bandit).  
- build.yml → packaging Python et vérification d’installabilité.  
- docker.yml → construction et push de l’image Docker vers GHCR.  
- deploy.yml → déploiement staging via docker-compose.  
- prometheus.yml → configuration du monitoring Prometheus.  
- alert_rules.yml → règles d’alerte critiques (app down, DB down, CPU/mémoire).  
- docker-compose.yml → environnement complet (app, db, exporters, monitoring).

### 📂 configs/
- pyproject.toml → définition des dépendances Python.  
- requirements.txt → liste des dépendances expérimentales.  
- mypy.ini → configuration de la vérification statique des types.  
- pytest.ini → standardisation des tests unitaires et d’intégration.

### 📂 utils/
- ci_cd_utils.py → fonctions utilitaires pour automatiser les pipelines CI/CD (logs signés, horodatages, hashage).

### 📂 schemas/
- ci_cd_schema.json → schéma de validation des workflows et artefacts CI/CD.

### 📂 tests/
- test_ci.yml → vérifie la validité du pipeline CI.  
- test_lint.yml → vérifie la qualité du code.  
- test_build.yml → vérifie l’installation et la reproductibilité des dépendances.  
- test_ci_cd_utils.py → vérifie la robustesse des fonctions utilitaires CI/CD.

### 📂 reports/
Ce dossier regroupe les **rapports générés automatiquement** par les workflows CI/CD :  
- coverage.xml → rapport de couverture des tests.  
- test-results.xml → rapport JUnit des tests unitaires.  
- lint-report.txt → rapport flake8/mypy.  
- security-report.json → rapport bandit/safety.  
- deploy-report.log → rapport du déploiement staging (healthchecks).

👉 Ces fichiers servent à l’**auditabilité des contrôles**.

### 📂 artifacts/
Ce dossier regroupe les **produits finis et preuves institutionnelles** :  

#### 🔧 Build
- finsig-<version>-py3-none-any.whl  
- finsig-<version>.tar.gz  

#### 🐳 Docker
- docker-image-sha256.txt → hash SHA256 de l’image Docker.  
- docker-image.tar → export local de l’image (optionnel).  

#### 📜 Logs
- ci_cd_events.log → journal des événements CI/CD.  
- deploy-report.log → rapport du déploiement staging.  

#### 🔒 Hashes
- build-hash.txt → empreinte SHA256 des paquets Python.  
- docker-hash.txt → empreinte SHA256 de l’image Docker.  

#### ✅ Validation
- artifact-validation.json → fichier conforme au schéma ci_cd_schema.json, listant artefacts, hash et statut validé.  

👉 Ces fichiers servent à la **traçabilité institutionnelle et à la validation externe**.

### 📂 scripts/
Ce dossier regroupe les **scripts d’orchestration CI/CD** utilisés en local ou dans Codespaces pour reproduire les workflows manuellement, valider les artefacts, et générer les preuves institutionnelles.

#### 🔧 Scripts spécialisés
- build.sh → génère les artefacts Python (wheel, sdist) et les valide avec Twine.  
- docker.sh → construit l’image Docker, l’exporte en tar, génère les hashes et les fichiers de preuve.  
- reports.sh → lance les tests unitaires, la couverture, le lint et les audits de sécurité.  
- validate.sh → génère le fichier artifact-validation.json en croisant les artefacts et les rapports.  
- setup_pipeline.sh → installe les dépendances, prépare les dossiers, et orchestre l’exécution complète du pipeline.  
- pipeline.sh → lance tous les scripts dans l’ordre pour reproduire le pipeline CI/CD en local.

👉 Ces scripts permettent de tester, auditer et valider chaque étape du pipeline CI/CD sans dépendre uniquement des workflows GitHub. Ils assurent une traçabilité hors ligne, utile en contexte de blocage ou d’audit externe.



## 🔄 Workflows CI/CD intégrés

### 📂 .github/workflows/
- ci-validation.yml → pipeline principal : tests, intégration, export des rapports.  
- lint-check.yml → pipeline qualité : flake8, mypy, journalisation.  
- build-validation.yml → pipeline de build : reproductibilité, hash, signature.  
- docker-pipeline.yml → pipeline conteneurisation : build, push, intégrité.  
- deploy-staging.yml → pipeline déploiement : simulation, healthchecks, monitoring.



## ⚙️ Fonctionnement

- Les workflows sont définis dans workflows/ et validés par les configurations (configs/).  
- Les utilitaires (utils/) assurent la traçabilité et la sécurité des pipelines.  
- Les schémas (schemas/) garantissent la cohérence et la conformité des workflows.  
- Les tests (tests/) valident la robustesse et la reproductibilité des pipelines.  
- Les fichiers prometheus.yml et alert_rules.yml assurent le monitoring et les alertes.  
- Le docker-compose.yml permet un déploiement local complet et auditable.  
- Les dossiers reports/ et artifacts/ assurent la séparation claire entre résultats des contrôles et produits institutionnels validés.  
- Le dossier scripts/ permet de reproduire localement chaque étape du pipeline, avec validation dynamique et traçabilité complète.



## 🧭 Gouvernance et impact institutionnel

- Expérimentation contrôlée : le sous-module ci-cd/ sert de laboratoire pour tester les workflows.  
- Traçabilité : chaque modification est documentée dans les bitácoras CI/CD.  
- Institutionnalisation : une fois validés, les workflows et artefacts sont fusionnés dans finsig/.  
- Scripts comme preuve d’autonomie : le dossier scripts/ montre que FINSIG peut reproduire ses pipelines sans dépendance à GitHub Actions.  
- Auditabilité hors ligne : chaque script produit des artefacts et rapports traçables, même en environnement contraint.  
- Impact : garantit robustesse, reproductibilité et auditabilité avant adoption officielle.



## ✅ Conclusion

Le sous-module ci-cd/ est le laboratoire technique de FINSIG.  
Il permet de tester et durcir les workflows CI/CD avant leur intégration institutionnelle dans la branche principale finsig/, assurant robustesse, conformité, traçabilité et monitoring.  
Avec l’ajout des dossiers reports/, artifacts/ et scripts/, la traçabilité institutionnelle est complète :  
- reports/ → résultats des contrôles.  
- artifacts/ → produits finis et preuves institutionnelles validées.  
- scripts/ → reproduction locale, validation dynamique, auditabilité hors ligne.

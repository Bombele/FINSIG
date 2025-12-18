# README TECHNIQUE – Pipeline CI/CD de FINSIG

---

## 🎯 Objectif

Le module CI/CD garantit la **robustesse**, la **traçabilité** et l’**auditabilité** de l’infrastructure technique de FINSIG.  
Il permet de tester, empaqueter, déployer et monitorer tous les composants dans un environnement reproductible et conforme aux standards.  
Le pipeline est conçu pour fonctionner de manière fiable même en contexte de crise ou de contraintes, renforçant la crédibilité institutionnelle.

---

## 📂 Structure générale

### ⚙️ configs/
- `pyproject.toml` → Métadonnées du projet, dépendances et configurations des outils (pytest, flake8, mypy, bandit, docker, prometheus-client).  
- `requirements.txt` → Liste hiérarchisée des dépendances (core, dev, CI/CD, monitoring).  
- `pytest.ini` → Découverte standardisée des tests, rapports de couverture, sortie JUnit et logs horodatés.  
- `mypy.ini` → Vérification stricte des types, codes d’erreur et support de plugins (`pydantic.mypy`).  

### ⚙️ .github/workflows/
- `build-validation.yml` → Valide le packaging Python (wheel + sdist), l’installabilité et les artefacts d’audit.  
- `lint-validation.yml` → Exécute flake8, bandit et mypy pour la qualité, la sécurité et le typage.  
- `tests-validation.yml` → Exécute les tests unitaires avec couverture et rapports JUnit.  
- `security-check.yml` → Analyse le code et les dépendances pour détecter les vulnérabilités (bandit + safety).  
- `docker-pipeline.yml` → Construit et pousse l’image Docker vers GHCR.  
- `deploy-validation.yml` → Simule le déploiement en staging via Docker Compose avec healthchecks et Prometheus.  
- `ci-validation.yml` → Orchestre tous les workflows de validation en parallèle.  

### 📊 Monitoring & Orchestration
- `prometheus.yml` → Scraping des métriques de l’app, de la base de données et des exporters.  
- `alert_rules.yml` → Définit les alertes critiques (app down, DB down, CPU/mémoire élevé).  
- `docker-compose.yml` → Déploie app, Postgres, exporters et Prometheus dans un environnement local de staging.  

### 🧪 Tests & Validation
- `tests/` → Workflows de test : build, deploy, sécurité, lint, CI orchestré.  
- `schemas/` → Schéma de validation des workflows et artefacts (`ci_cd_schema.json`).  
- `utils/` → Fonctions réutilisables pour logs, hash et horodatages (`ci_cd_utils.py`).  

### 📚 Documentation
- `README_TECHNIQUE_FR.md / EN / ES` → Vue technique trilingue.  
- `BITACORA_CI-CD_FR.md / EN / ES` → Bitácora institutionnelle des évolutions CI/CD.  
- `CI_CD_GUIDE.md` → Principes de conception, méthodologie et gouvernance des workflows CI/CD.  

### 📂 reports/
Contient les **rapports générés automatiquement** par les workflows CI/CD :  
- `coverage.xml` → rapport de couverture des tests.  
- `test-results.xml` → rapport JUnit des tests unitaires.  
- `lint-report.txt` → rapport flake8/mypy.  
- `security-report.json` → rapport bandit/safety.  
- `deploy-report.log` → rapport du déploiement staging (healthchecks).  

👉 Ces fichiers assurent l’**auditabilité des contrôles**.

### 📂 artifacts/
Contient les **produits finis et preuves institutionnelles** :  
- Build → `finsig-<version>-py3-none-any.whl`, `finsig-<version>.tar.gz`.  
- Docker → `docker-image-sha256.txt`, `docker-image.tar`.  
- Logs → `ci_cd_events.log`, `deploy-report.log`.  
- Hashes → `build-hash.txt`, `docker-hash.txt`.  
- Validation → `artifact-validation.json` (conforme à `ci_cd_schema.json`).  

👉 Ces fichiers assurent la **traçabilité institutionnelle et la validation externe**.

### 📂 scripts/
Contient les **scripts d’orchestration CI/CD** pour reproduction locale et validation hors ligne :  
- `build.sh` → Génère les artefacts Python et les valide avec Twine.  
- `docker.sh` → Construit l’image Docker, exporte en tar, génère les hashes et fichiers de preuve.  
- `reports.sh` → Exécute tests, couverture, lint et audits de sécurité.  
- `validate.sh` → Génère `artifact-validation.json` dynamique avec statuts PASSED/FAILED.  
- `setup_pipeline.sh` → Installe les dépendances, prépare les dossiers et orchestre l’exécution complète du pipeline.  
- `pipeline.sh` → Exécute tous les scripts séquentiellement pour reproduire le pipeline CI/CD localement.  

👉 Ces scripts offrent une **auditabilité hors ligne** et démontrent l’autonomie institutionnelle.

---

## 🔄 Étapes du pipeline

1. **Tests** → Unitaires, couverture, rapports JUnit.  
2. **Lint & Sécurité** → flake8, mypy, bandit, safety.  
3. **Build & Packaging** → wheel + sdist, vérifications de reproductibilité.  
4. **Dockerisation** → Construction et push de l’image vers GHCR.  
5. **Déploiement staging** → Environnement complet via docker-compose, healthchecks.  
6. **Monitoring & Alertes** → Métriques Prometheus, règles d’alerte.  
7. **Validation** → `artifact-validation.json` dynamique avec traçabilité institutionnelle.

---

## ✅ Impact institutionnel

- **Robustesse** → Tests et packaging automatisés.  
- **Conformité** → Garanties par linting, typage et scans de sécurité.  
- **Auditabilité** → Rapports et artefacts de validation exportables.  
- **Reproductibilité** → Assurée par Docker et configurations standardisées.  
- **Résilience** → Monitoring et alertes assurent la continuité opérationnelle.  
- **Crédibilité** → Documentation trilingue et bitácoras soutiennent la validation externe.  
- **Autonomie** → Le dossier scripts/ assure la reproductibilité même hors ligne.

---

## 📌 Conclusion

Ce pipeline CI/CD est la **colonne vertébrale technique de FINSIG**.  
Il démontre la capacité du projet à être testé, sécurisé, empaqueté, déployé et monitoré de manière **transparente et auditable**.  
Avec l’ajout des dossiers **reports/**, **artifacts/** et **scripts/**, la traçabilité institutionnelle est complète :  
- reports/ → résultats des contrôles.  
- artifacts/ → produits finis et preuves institutionnelles.  
- scripts/ → reproduction locale, validation dynamique, auditabilité hors ligne.
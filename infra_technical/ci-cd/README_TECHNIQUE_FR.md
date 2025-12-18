# README TECHNIQUE – Pipeline CI/CD de FINSIG

---

## 🎯 Objectif

Le module CI/CD garantit la **robustesse**, la **traçabilité** et l’**auditabilité** de l’infrastructure technique de FINSIG.  
Il permet des tests contrôlés, le packaging, le déploiement et le monitoring de tous les composants dans un environnement reproductible et conforme.  
Le pipeline est conçu pour fonctionner de manière fiable même en contexte de crise ou de contraintes géopolitiques, renforçant la crédibilité institutionnelle.

---

## 📂 Structure générale

### 🔧 `configs/`
- `pyproject.toml` → métadonnées du projet, dépendances et configurations des outils (pytest, flake8, mypy, bandit, docker, prometheus-client).  
- `requirements.txt` → liste hiérarchisée des dépendances (core, dev, CI/CD, monitoring).  
- `pytest.ini` → découverte standardisée des tests, rapports de couverture, sortie JUnit et logs horodatés.  
- `mypy.ini` → typage strict, codes d’erreur et support de plugins (`pydantic.mypy`).

### ⚙️ `.github/workflows/`
- `build-validation.yml` → valide le packaging Python (wheel + sdist), l’installabilité et les artefacts audités.  
- `lint-validation.yml` → exécute flake8, bandit et mypy pour la qualité, la sécurité et le typage.  
- `tests-validation.yml` → exécute les tests unitaires avec couverture et rapports JUnit.  
- `security-check.yml` → scanne le code et les dépendances pour détecter les vulnérabilités (bandit + safety).  
- `deploy-validation.yml` → simule le déploiement staging via Docker Compose avec healthchecks et Prometheus.  
- `lint-check.yml` → linting léger et vérification de typage pour un retour rapide.  
- `ci-validation.yml` → orchestre tous les workflows de validation en parallèle.

### 📈 Monitoring & Orchestration
- `prometheus.yml` → collecte des métriques de l’app, de la base de données et des exporters.  
- `alert_rules.yml` → définit les alertes critiques (app down, DB down, CPU/mémoire élevées).  
- `docker-compose.yml` → déploie app, Postgres, exporters et Prometheus dans un environnement staging local.

### 🧪 Tests & Validation
- `tests/` → workflows de test consolidés :  
  - `test_build.yml` → valide le packaging et l’installabilité.  
  - `test_deploy.yml` → valide le déploiement staging et les healthchecks.  
  - `test_security.yml` → valide les vulnérabilités du code et des dépendances.  
  - `test_lint.yml` → valide le style, le typage et la sécurité.  
  - `test_ci.yml` → orchestre tous les workflows de test en parallèle.  
  - `test_ci_cd_utils.py` → valide les fonctions utilitaires (hash, logs, timestamps, validation des artefacts).  
- `schemas/` → schéma de validation des workflows et artefacts (`ci_cd_schema.json`).  
- `utils/` → fonctions réutilisables pour logs, hash et horodatage (`ci_cd_utils.py`).

### 📚 Documentation
- `README_TECHNIQUE_FR.md / EN / ES` → vue technique trilingue.  
- `BITACORA_CI-CD_FR.md / EN / ES` → journal institutionnel des évolutions CI/CD.  
- `CI_CD_GUIDE.md` → principes de conception, méthodologie et gouvernance des workflows CI/CD.

### 📁 reports/
Contient les **rapports générés automatiquement** par les workflows CI/CD :  
- `coverage.xml` → rapport de couverture des tests.  
- `test-results.xml` → rapport JUnit des tests unitaires.  
- `lint-report.txt` → rapport flake8/mypy.  
- `security-report.json` → rapport bandit/safety.  
- `deploy-report.log` → rapport du déploiement staging (healthchecks).  

👉 Ces fichiers assurent l’**auditabilité des contrôles**.

### 📁 artifacts/
Contient les **produits finis et preuves institutionnelles** :  

#### 🔧 Build
- `finsig-<version>-py3-none-any.whl`  
- `finsig-<version>.tar.gz`  

#### 🐳 Docker
- `docker-image-sha256.txt` → hash SHA256 de l’image Docker.  
- `docker-image.tar` → export local de l’image (optionnel).  

#### 📜 Logs
- `ci_cd_events.log` → journal des événements CI/CD.  
- `deploy-report.log` → rapport du déploiement staging.  

#### 🔒 Hashes
- `build-hash.txt` → empreinte SHA256 des paquets Python.  
- `docker-hash.txt` → empreinte SHA256 de l’image Docker.  

#### ✅ Validation
- `artifact-validation.json` → fichier conforme au schéma `ci_cd_schema.json`, listant artefacts, hash et statut validé.  

👉 Ces fichiers assurent la **traçabilité institutionnelle et la validation externe**.

---

## 🔄 Étapes du pipeline

1. **Tests**  
   - Exécution des tests unitaires avec `pytest`.  
   - Mesure de la couverture et export des rapports (`coverage.xml`, `test-results.xml`).

2. **Linting & Sécurité**  
   - Vérification du style avec `flake8`.  
   - Détection des vulnérabilités avec `bandit` et `safety`.  
   - Application du typage statique avec `mypy`.

3. **Build & Packaging**  
   - Génération des artefacts Python (`wheel`, `sdist`).  
   - Vérification de l’installabilité et de la reproductibilité.

4. **Dockerisation**  
   - Construction de l’image Docker.  
   - Push vers GitHub Container Registry (GHCR).

5. **Déploiement Staging**  
   - Simulation de l’environnement complet via `docker-compose`.  
   - Inclut app, base de données, exporters et monitoring.  
   - Healthchecks sur app, DB et Prometheus.

6. **Monitoring & Alertes**  
   - Prometheus collecte les métriques.  
   - Les règles d’alerte se déclenchent en cas de défaillance critique ou de seuils de ressources.

---

## ✅ Impact institutionnel

- **Robustesse** → validée par tests et packaging automatisés.  
- **Conformité** → assurée par linting, typage et scans de sécurité.  
- **Auditabilité** → rapports exportables de couverture, JUnit et Prometheus.  
- **Reproductibilité** → garantie par Docker et configurations standardisées.  
- **Résilience** → monitoring et alertes assurent la continuité opérationnelle.  
- **Crédibilité** → documentation trilingue et bitácoras renforcent la validation externe.

---

## 📌 Conclusion

Ce pipeline CI/CD est la **colonne vertébrale technique de FINSIG**.  
Il démontre la capacité du projet à être testé, sécurisé, empaqueté, déployé et monitoré de manière **transparente et auditable**.  
Avec l’ajout des dossiers **`reports/`** et **`artifacts/`**, la traçabilité institutionnelle est complète :  
- `reports/` → résultats des contrôles.  
- `artifacts/` → produits finis et preuves institutionnelles.  
C’est un atout stratégique pour la validation institutionnelle, l’onboarding des partenaires et la conformité réglementaire.
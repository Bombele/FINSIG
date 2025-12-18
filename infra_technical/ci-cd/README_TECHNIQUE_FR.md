# README TECHNIQUE – Pipeline CI/CD de FINSIG

---

## 🎯 Objectif

Ce module CI/CD garantit la **robustesse**, la **traçabilité** et l’**auditabilité** de l’infrastructure technique de FINSIG.  
Il permet de tester, empaqueter, déployer et monitorer tous les composants dans un environnement reproductible et conforme.  
Le pipeline est conçu pour fonctionner de manière fiable même en contexte de crise ou de contraintes géopolitiques, renforçant la crédibilité institutionnelle.

---

## 📂 Structure Générale

### 🔧 `configs/`
- `pyproject.toml` → Métadonnées du projet, dépendances et configuration des outils (pytest, flake8, mypy, bandit, docker, prometheus-client).  
- `requirements.txt` → Liste hiérarchisée des dépendances (core, dev, CI/CD, monitoring).  
- `pytest.ini` → Découverte standardisée des tests, rapports de couverture, sortie JUnit et logs horodatés.  
- `mypy.ini` → Typage strict, codes d’erreur et support de plugins (`pydantic.mypy`).

### ⚙️ `.github/workflows/`
- `build-validation.yml` → Valide l’empaquetage Python (wheel + sdist), l’installabilité et les artefacts audités.  
- `lint-validation.yml` → Exécute flake8, bandit et mypy pour qualité, sécurité et typage.  
- `tests-validation.yml` → Exécute les tests unitaires avec couverture et rapports JUnit.  
- `security-check.yml` → Analyse le code et les dépendances pour vulnérabilités (bandit + safety).  
- `deploy-validation.yml` → Simule un déploiement staging via Docker Compose avec healthchecks et Prometheus.  
- `lint-check.yml` → Linting léger et contrôle de typage pour feedback rapide.  
- `ci-validation.yml` → Orchestre tous les workflows de validation en parallèle.

### 📈 Monitoring & Orchestration
- `prometheus.yml` → Scraping des métriques de l’app, de la base de données et des exporters.  
- `alert_rules.yml` → Définit les alertes critiques (app down, DB down, CPU/mémoire élevées).  
- `docker-compose.yml` → Déploie app, Postgres, exporters et Prometheus en environnement staging local.

### 🧪 Tests & Validation
- `tests/` → Workflows de test consolidés :  
  - `test_build.yml` → valide l’empaquetage et l’installabilité.  
  - `test_deploy.yml` → valide le déploiement staging et les healthchecks.  
  - `test_security.yml` → valide les vulnérabilités du code et des dépendances.  
  - `test_lint.yml` → valide le style, le typage et la sécurité rapide.  
  - `test_ci.yml` → orchestre tous les workflows de test en parallèle.  
  - `test_ci_cd_utils.py` → valide les fonctions utilitaires (hash, logs, timestamps, validation des artefacts).  
- `schemas/` → Schéma de validation des workflows et artefacts (`ci_cd_schema.json`).  
- `utils/` → Fonctions réutilisables pour logging, hashing et horodatage (`ci_cd_utils.py`).

### 📚 Documentation
- `README_TECHNIQUE_FR.md / EN / ES` → Vue technique trilingue.  
- `BITACORA_CI-CD_FR.md / EN / ES` → Journal institutionnel de l’évolution du CI/CD.  
- `CI_CD_GUIDE.md` → Principes de conception, méthodologie et gouvernance des workflows CI/CD.

---

## 🔄 Étapes du Pipeline

1. **Tests**  
   - Exécution des tests unitaires via `pytest`.  
   - Mesure de la couverture et export des rapports (`coverage.xml`, `test-results.xml`).

2. **Linting & Sécurité**  
   - Validation du style avec `flake8`.  
   - Détection des vulnérabilités avec `bandit` et `safety`.  
   - Vérification stricte du typage avec `mypy`.

3. **Build & Packaging**  
   - Génération des artefacts Python (`wheel`, `sdist`).  
   - Vérification de l’installabilité et de la reproductibilité.

4. **Dockerisation**  
   - Construction de l’image Docker.  
   - Publication sur GitHub Container Registry (GHCR).

5. **Déploiement Staging**  
   - Simulation d’un environnement complet via `docker-compose`.  
   - Inclut app, base de données, exporters et monitoring.  
   - Healthchecks sur app, DB et Prometheus.

6. **Monitoring & Alertes**  
   - Prometheus collecte les métriques.  
   - Les alertes critiques se déclenchent en cas de panne ou de dépassement de seuils.

---

## ✅ Impact Institutionnel

- **Robustesse** → Validée par tests et empaquetage automatisés.  
- **Conformité** → Assurée par linting, typage et scans de sécurité.  
- **Auditabilité** → Rapports exportables (coverage, JUnit, Prometheus).  
- **Reproductibilité** → Garantie par Docker et configurations standardisées.  
- **Résilience** → Monitoring et alertes assurent la continuité opérationnelle.  
- **Crédibilité** → Documentation trilingue et bitácoras renforcent la validation externe.

---

## 📌 Conclusion

Ce pipeline CI/CD est la **colonne vertébrale technique de FINSIG**.  
Il démontre la capacité du projet à être testé, sécurisé, empaqueté, déployé et monitoré de manière **transparente et auditable**.  
C’est un atout stratégique pour la validation institutionnelle, l’intégration de partenaires et la conformité réglementaire.
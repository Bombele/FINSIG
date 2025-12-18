# README Technique CI/CD – FINSIG

---

## 🎯 Objectif

Le pipeline CI/CD de FINSIG est conçu pour garantir la **robustesse**, la **traçabilité** et l’**auditabilité** du projet.  
Chaque étape assure la qualité du code, la reproductibilité des environnements et la continuité opérationnelle, même en contexte de crise.

---

## 🔎 Étapes principales

### 1. **Tests (`tests.yml`)**
- Exécution des tests unitaires avec `pytest`.
- Calcul de la couverture avec `pytest-cov`.
- Génération de rapports pour audit externe.

### 2. **Lint & Sécurité (`lint.yml`)**
- Vérification du style et de la complexité du code avec `flake8`.
- Analyse de sécurité avec `bandit` pour détecter les failles potentielles.
- Conformité technique et qualité du code assurées.

### 3. **Build & Packaging (`build.yml`)**
- Génération des artefacts Python (`wheel`, `sdist`) via `python -m build`.
- Vérification de l’installabilité (`pip install dist/*.whl`).
- Upload des artefacts pour audit et distribution.

### 4. **Dockerisation (`docker.yml`)**
- Construction de l’image Docker avec `docker build`.
- Push automatique vers GitHub Container Registry (GHCR).
- Portabilité et reproductibilité garanties.

### 5. **Déploiement Staging (`deploy.yml`)**
- Simulation de déploiement via `docker-compose`.
- Services inclus : application FINSIG, base Postgres, monitoring Prometheus.
- Healthchecks intégrés pour assurer disponibilité et auditabilité.

---

## ✅ Résultats attendus

- **Robustesse** validée par les tests unitaires et la couverture.  
- **Qualité et sécurité** assurées par lint et analyse statique.  
- **Portabilité** via packaging Python et images Docker.  
- **Reproductibilité** grâce à Docker Compose et CI/CD automatisé.  
- **Auditabilité** renforcée par les rapports de couverture, les artefacts buildés et les métriques Prometheus.  

---

## 📌 Conclusion

Ce pipeline CI/CD constitue la **colonne vertébrale technique** de FINSIG.  
Il démontre la capacité du projet à être testé, sécurisé, packagé, conteneurisé et déployé de manière **fiable et transparente**.  
Il s’agit d’un élément clé pour la crédibilité institutionnelle et la validation par des partenaires ou régulateurs.
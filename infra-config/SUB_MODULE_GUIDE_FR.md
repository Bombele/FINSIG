# SUB_MODULE_GUIDE_FR – infra-config

---

## 🎯 Objectif du sous-module
Le sous-module `infra-config/` centralise les **fichiers de configuration technique** nécessaires au bon fonctionnement de FINSIG.  
Il permet de séparer la **documentation institutionnelle** (README, guides) de la **configuration technique** (build, tests, dépendances), garantissant une structure claire et modulaire.

---

## 📑 Portée
- **Build et automatisation** : gestion des commandes via `makefile`.  
- **Qualité du code** : règles de typage et de vérification avec `mypy.ini`.  
- **Gestion des dépendances** : suivi des paquets et versions avec `poetry.lock` et `pyproject.toml`.  
- **Tests unitaires** : configuration des tests avec `pytest.ini`.  
- **Interopérabilité CI/CD** : intégration fluide avec les workflows GitHub Actions.  

---

## 📂 Organisation des fichiers

### 📂 infra-config/
- **makefile** → automatisation des tâches (build, tests, déploiement).  
- **mypy.ini** → configuration du typage statique Python.  
- **poetry.lock** → verrouillage des dépendances pour garantir la reproductibilité.  
- **pyproject.toml** → définition du projet, des dépendances et des outils.  
- **pytest.ini** → configuration des tests unitaires et d’intégration.  

---

## ⚙️ Fonctionnement
- Les développeurs exécutent les commandes via `makefile` pour simplifier les workflows.  
- `mypy.ini` assure la robustesse et la qualité du code en vérifiant les types.  
- `poetry.lock` et `pyproject.toml` garantissent une gestion cohérente des dépendances.  
- `pytest.ini` standardise l’exécution des tests pour assurer la fiabilité du projet.  
- Les workflows CI/CD utilisent ces fichiers pour valider automatiquement chaque commit.  

---

## ✅ Impact institutionnel
- **Fiabilité** : configuration centralisée et reproductible.  
- **Transparence** : règles techniques documentées et accessibles.  
- **Interopérabilité** : cohérence avec les autres sous-modules (`core`, `audit`, `data`, `governance`, `reports`).  
- **Transmission** : onboarding facilité pour les développeurs et partenaires techniques.  
- **Adoption** : crédibilité renforcée auprès des institutions et régulateurs grâce à une architecture claire.  

---

## 📌 Conclusion
Le sous-module `infra-config/` est la **chambre technique** de FINSIG.  
Il regroupe les fichiers de configuration essentiels, garantissant une séparation nette entre la **constitution documentaire** et la **configuration technique**.  
Son intégration avec les workflows CI/CD assure la robustesse et la traçabilité du projet.
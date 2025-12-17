# MODULE_GUIDE – .github/workflows/

---

## 🎯 Objectif
Le dossier `.github/workflows/` est la **chambre d’automatisation CI/CD** de FINSIG.  
Il contient les fichiers YAML définissant les pipelines GitHub Actions, assurant la validation continue, le déploiement automatisé et la qualité institutionnelle du projet.

---

## 📑 Portée
- **Intégration continue (CI)** : exécution automatique des tests unitaires et d’intégration.  
- **Déploiement continu (CD)** : automatisation des livraisons et mises en production.  
- **Qualité logicielle** : vérification des standards (linting, mypy, pytest, etc.).  
- **Traçabilité** : journalisation des workflows exécutés pour garantir la conformité.  
- **Interopérabilité** : intégration avec les autres modules (`core`, `compliance`, `infra-*`).

---

## 📂 Organisation
- Chaque fichier `.yml` ou `.yaml` dans ce dossier correspond à un **workflow spécifique** :  
  - `ci.yml` → pipeline de tests et validation.  
  - `deploy.yml` → pipeline de déploiement.  
  - `quality.yml` → pipeline de contrôle qualité.  
  - `docs.yml` → pipeline de validation documentaire.  

*(les noms exacts dépendent des fichiers présents dans ton repo, mais la logique reste la même)*

---

## ⚙️ Fonctionnement
- Les workflows sont déclenchés automatiquement par des événements GitHub :  
  - **push** → validation des commits.  
  - **pull_request** → vérification avant fusion.  
  - **release** → déploiement institutionnel.  
- Chaque workflow est une **loi technique** dans la constitution numérique : il garantit la robustesse et la conformité du projet.  
- Les résultats des workflows sont visibles dans l’onglet **Actions** du dépôt GitHub.

---

## ✅ Impact institutionnel
- **Fiabilité** : chaque modification est validée automatiquement.  
- **Transparence** : les workflows assurent une traçabilité publique.  
- **Qualité** : respect des standards techniques et réglementaires.  
- **Adoption** : crédibilité renforcée auprès des partenaires institutionnels grâce à une automatisation claire.

---

## 📌 Conclusion
Le module `.github/workflows/` est la **colonne vertébrale CI/CD** de FINSIG.  
Il incarne la discipline technique et institutionnelle, garantissant que chaque étape de développement et de déploiement respecte les standards de qualité et de conformité.
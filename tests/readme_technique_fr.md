##############################################
# 📖 README TECHNIQUE – Tests (FR)
##############################################

## 1. Objectif
Le sous-module **Tests** de FINSIG garantit la robustesse, la conformité et l’auditabilité de l’ensemble de la plateforme.  
Il couvre :  
- Les fonctions utilitaires transversales.  
- Les règles de juridiction et conformité locale/continentale.  
- La validation des identités et des accès.  
- La conformité réglementaire (KYC, AML, ISO/IEC, RGPD).  
- L’automatisation via scripts CI/CD.  

----------------------------------------------

## 2. Structure des dossiers
📂 tests/  
- **utlis/** → Tests unitaires pour fonctions utilitaires et helpers.  
- **jurisdictions/** → Tests de conformité locale et continentale.  
- **identity/** → Tests sur validation d’identité, gestion des accès et authentification.  
- **compliance/** → Tests de conformité réglementaire (KYC, AML, ISO/IEC, RGPD).  
- **ci_cd_scripts/** → Scripts et workflows CI/CD pour automatisation des tests.  
- **reports/** → Rapports exportés (JUnit, couverture, conformité).  
- **artifacts/** → Preuves institutionnelles (logs, JSON, hashes).  
- **bitacora_fr.md / bitacora_en.md / bitacora_es.md** → Journaux institutionnels trilingues.  
- **TESTS_GUIDE.md** → Guide méthodologique et gouvernance des tests.  

----------------------------------------------

## 3. Technologies utilisées
- **pytest** → Framework de tests unitaires et fonctionnels.  
- **coverage.py** → Mesure de couverture des tests.  
- **flake8 + mypy** → Vérification de style et typage strict.  
- **bandit + safety** → Analyse de sécurité du code et des dépendances.  
- **GitHub Actions** → Orchestration CI/CD des workflows de test.  
- **Prometheus/Grafana** → Monitoring des métriques de tests et alertes.  

----------------------------------------------

## 4. Workflows CI/CD
📂 tests/ci_cd_scripts/  
- `test_lint.sh` → Vérifie style, typage et sécurité.  
- `test_coverage.sh` → Mesure couverture et génère rapports.  
- `test_deploy.sh` → Simule déploiement et vérifie robustesse.  
- `test_ci.yml` → Orchestration CI/CD complète des tests.  

👉 **Bonne pratique** : intégrer ces workflows dans `ci-validation.yml` pour validation continue.  

----------------------------------------------

## 5. Rapports et artefacts
- 📂 reports/ → Export JUnit, couverture, conformité, identité, juridictions.  
- 📂 artifacts/ → Logs, hashes, JSON de validation, preuves institutionnelles.  
- `tests_schema.json` → Schéma JSON pour validation des résultats et rapports.  

👉 **Bonne pratique** : séparer résultats (reports) et preuves institutionnelles (artifacts).  

----------------------------------------------

## 6. Bitácoras
- **FR** : `bitacora_fr.md`  
- **EN** : `bitacora_en.md`  
- **ES** : `bitacora_es.md`  

Chaque bitácora trace les activités, validations et évolutions du sous-module.  
👉 **Bonne pratique** : mettre à jour la bitácora à chaque commit.  

----------------------------------------------

## 7. Résultats attendus
- Validation complète des fonctions utilitaires, juridictions, identités et conformité.  
- Rapports exportés pour auditabilité.  
- Preuves institutionnelles consolidées.  
- CI/CD automatisé et reproductible.  
- Documentation trilingue pour transmission continentale.  

----------------------------------------------

## 8. Conclusion
Le sous-module **Tests** est la **colonne vertébrale de la validation institutionnelle** de FINSIG.  
Il assure robustesse technique, conformité réglementaire et auditabilité fiable.  
Avec ses rapports, artefacts et bitácoras, il constitue un **socle transversal de validation**, prêt pour adoption et certification.

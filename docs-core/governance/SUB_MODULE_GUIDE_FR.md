# SUB_MODULE_GUIDE_FR – Governance

---

## 🎯 Objectif du sous-module
Le sous-module `governance/` définit le cadre institutionnel et technique de la **gouvernance** dans FINSIG.  
Il organise les règles, rôles, responsabilités et mécanismes de certification afin de garantir une gouvernance robuste, transparente et conforme aux standards internationaux.  
Ce sous-module est intégré dans le dossier `docs-core` aux côtés de `audit/`, `data/` et `reports/`.

---

## 📑 Portée
- **Règles de gouvernance** : définition des normes et politiques institutionnelles.  
- **Rôles et responsabilités** : clarification des fonctions et des acteurs.  
- **Certification** : intégration des mécanismes de conformité et d’audit.  
- **Interopérabilité** : harmonisation avec les autres sous-modules (`audit`, `data`, `reports`).  
- **Transmission pédagogique** : documentation claire et multilingue pour onboarding institutionnel.  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **GOVERNANCE_GUIDE.md** → cadre global de la gouvernance.  
- **ROLES_GUIDE.md** → définition des rôles et responsabilités.  
- **POLICIES_GUIDE.md** → règles et politiques institutionnelles.  
- **CERTIFICATION_GUIDE.md** → mécanismes de certification et conformité.  
- **INTEROPERABILITY_GUIDE.md** → intégration et harmonisation multi-modules.  

### 📂 conformity/
- **governance_validator.py** → vérifie la conformité des règles de gouvernance.  
- **roles_checker.py** → contrôle la cohérence des rôles et responsabilités.  
- **policies_checker.py** → valide la conformité des politiques.  
- **certification_checker.py** → assure la conformité des mécanismes de certification.  
- **interoperability_checker.py** → vérifie l’intégration multi-modules.  

### 📂 modules/
- **governance_engine.py** → moteur principal de gestion de la gouvernance.  
- **governance_mapping.py** → cartographie des règles et responsabilités.  
- **governance_logger.py** → journalisation des décisions et validations.  
- **governance_audit.py** → audit des processus de gouvernance.  

### 📂 tests/
- **test_governance_engine.py** → tests sur la robustesse du moteur de gouvernance.  
- **test_roles_checker.py** → tests sur la cohérence des rôles.  
- **test_policies_checker.py** → tests sur la conformité des politiques.  
- **test_certification_checker.py** → tests sur la certification.  
- **test_interoperability_checker.py** → tests sur l’intégration multi-modules.  

### 📂 workflows/
- **governance-validation.yml** → vérifie la conformité globale du sous-module.  
- **roles-validation.yml** → validation des rôles et responsabilités.  
- **policies-validation.yml** → validation des politiques institutionnelles.  
- **certification-validation.yml** → validation des mécanismes de certification.  
- **interoperability-validation.yml** → validation de l’intégration multi-modules.  

---

## ⚙️ Fonctionnement
- La gouvernance est définie dans `GOVERNANCE_GUIDE.md` et appliquée via `governance_engine.py`.  
- Chaque aspect (rôles, politiques, certification, interopérabilité) est validé par les checkers.  
- Les workflows CI/CD garantissent que la gouvernance reste cohérente et conforme.  
- Les audits sont journalisés dans `governance_logger.py` et intégrés à `BITACORA.md`.  

---

## ✅ Impact institutionnel
- **Fiabilité** : cadre clair et robuste pour la gouvernance.  
- **Transparence** : décisions documentées et vérifiables.  
- **Interopérabilité** : harmonisation multi-modules et multi-langues.  
- **Transmission** : onboarding facilité pour les équipes et partenaires.  
- **Adoption** : crédibilité renforcée auprès des institutions régionales et continentales.  

---

## 📌 Conclusion
Le sous-module `governance/` est la **colonne de gouvernance du dossier docs-core**.  
Il définit les règles, rôles et mécanismes de certification, garantissant robustesse, transparence et adoption institutionnelle.  
Son intégration avec `audit/`, `data/` et `reports/` assure une cohérence complète dans la documentation centrale.
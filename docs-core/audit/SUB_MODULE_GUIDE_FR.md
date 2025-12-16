# SUB_MODULE_GUIDE_FR – Audit

---

## 🎯 Objectif du sous-module
Le sous-module `audit/` définit le cadre institutionnel et technique de la **journalisation et de la traçabilité** dans FINSIG.  
Il garantit que chaque action, validation et workflow est enregistré, vérifié et conforme aux standards internationaux.  
Ce sous-module est intégré dans le dossier `docs-core` aux côtés de `data/`, `governance/` et `reports/`.

---

## 📑 Portée
- **Conformité normative** : alignement avec ISO/IEC, GDPR, AML/KYC.  
- **Journalisation technique** : enregistrement des événements, logs et validations.  
- **Traçabilité institutionnelle** : intégration des audits dans `BITACORA.md`.  
- **Interopérabilité** : harmonisation avec les autres sous-modules (`data`, `governance`, `reports`).  
- **Transparence** : documentation claire et multilingue pour adoption institutionnelle.  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **AUDIT_GUIDE.md** → cadre global de l’audit et de la traçabilité.  
- **NORMATIVE_AUDIT.md** → principes de conformité normative.  
- **TECH_AUDIT.md** → journalisation technique et logs.  
- **INSTITUTIONAL_AUDIT.md** → audit institutionnel et gouvernance.  
- **REPORTING_AUDIT.md** → intégration des audits dans les rapports.  

### 📂 conformity/
- **audit_validator.py** → vérifie la conformité des modules aux standards d’audit.  
- **normative_audit_checker.py** → contrôle la conformité normative.  
- **tech_audit_checker.py** → valide la journalisation technique.  
- **institutional_audit_checker.py** → assure la conformité institutionnelle.  
- **reporting_audit_checker.py** → vérifie l’intégration des audits dans les rapports.  

### 📂 modules/
- **audit_engine.py** → moteur principal de gestion des audits.  
- **audit_mapping.py** → cartographie des audits normatifs, techniques et institutionnels.  
- **audit_logger.py** → journalisation des événements et validations.  
- **audit_audit.py** → audit des processus internes.  

### 📂 tests/
- **test_audit_engine.py** → tests sur la robustesse du moteur d’audit.  
- **test_normative_audit_checker.py** → tests sur la conformité normative.  
- **test_tech_audit_checker.py** → tests sur la journalisation technique.  
- **test_institutional_audit_checker.py** → tests sur l’audit institutionnel.  
- **test_reporting_audit_checker.py** → tests sur l’intégration des audits dans les rapports.  

### 📂 workflows/
- **audit-validation.yml** → vérifie la conformité globale du sous-module.  
- **normative-audit-validation.yml** → validation des audits normatifs.  
- **tech-audit-validation.yml** → validation des audits techniques.  
- **institutional-audit-validation.yml** → validation des audits institutionnels.  
- **reporting-audit-validation.yml** → validation de l’intégration des audits dans les rapports.  

---

## ⚙️ Fonctionnement
- Les audits sont définis dans `AUDIT_GUIDE.md` et appliqués via `audit_engine.py`.  
- Chaque aspect (normatif, technique, institutionnel, reporting) est validé par les checkers.  
- Les workflows CI/CD garantissent que la traçabilité est respectée à chaque mise à jour.  
- Les audits sont journalisés dans `audit_logger.py` et intégrés à `BITACORA.md`.  

---

## ✅ Impact institutionnel
- **Fiabilité** : cadre clair et robuste pour la traçabilité.  
- **Transparence** : audits documentés et vérifiables.  
- **Interopérabilité** : intégration harmonisée avec `data`, `governance` et `reports`.  
- **Adoption** : crédibilité renforcée auprès des régulateurs et institutions.  

---

## 📌 Conclusion
Le sous-module `audit/` est la **colonne de traçabilité du dossier docs-core**.  
Il définit les mécanismes de journalisation et de conformité, garantissant robustesse, transparence et adoption institutionnelle.  
Son intégration avec `data/`, `governance/` et `reports/` assure une cohérence complète dans la documentation centrale.
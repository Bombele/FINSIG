# SUB_MODULE_GUIDE_FR – Reports

---

## 🎯 Objectif du sous-module
Le sous-module `reports/` définit le cadre de **reporting et de traçabilité institutionnelle** au sein de FINSIG.  
Il garantit que toutes les **audits**, **vérifications de conformité** et **décisions de gouvernance** soient documentés, accessibles et multilingues.  
Ce sous-module s’intègre dans `docs-core` aux côtés de `audit/`, `data/` et `governance/`.

---

## 📑 Portée
- **Règles de reporting** : définition des standards institutionnels de reporting.  
- **Traçabilité** : enregistrement des décisions de conformité et de gouvernance.  
- **Documentation multilingue** : FR/EN/ES pour adoption internationale.  
- **Intégration** : interopérabilité avec `audit`, `data` et `governance`.  
- **Transmission pédagogique** : guides clairs pour l’onboarding et l’usage institutionnel.  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **REPORTS_GUIDE.md** → cadre global du reporting.  
- **TRACEABILITY_GUIDE.md** → définition des règles de traçabilité.  
- **FORMATS_GUIDE.md** → formats institutionnels de reporting.  
- **INTEGRATION_GUIDE.md** → interopérabilité avec les autres modules.  

### 📂 conformity/
- **reports_validator.py** → vérifie la conformité des règles de reporting.  
- **traceability_checker.py** → contrôle la cohérence de la traçabilité.  
- **formats_checker.py** → valide les formats de reporting.  
- **integration_checker.py** → assure l’interopérabilité.  

### 📂 modules/
- **reports_engine.py** → moteur principal de gestion des reportings.  
- **reports_mapping.py** → mappage des reportings et de la traçabilité.  
- **reports_logger.py** → journalisation des reportings et validations.  
- **reports_audit.py** → audit des processus de reporting.  

### 📂 tests/
- **test_reports_engine.py** → tests sur la robustesse du moteur de reporting.  
- **test_traceability_checker.py** → tests sur la cohérence de la traçabilité.  
- **test_formats_checker.py** → tests sur les formats de reporting.  
- **test_integration_checker.py** → tests sur l’interopérabilité.  

### 📂 workflows/
- **reports-validation.yml** → vérifie la conformité globale du sous-module.  
- **traceability-validation.yml** → validation des règles de traçabilité.  
- **formats-validation.yml** → validation des formats de reporting.  
- **integration-validation.yml** → validation de l’interopérabilité.  

---

## ⚙️ Fonctionnement
- Le reporting est défini dans `REPORTS_GUIDE.md` et appliqué via `reports_engine.py`.  
- Chaque aspect (traçabilité, formats, intégration) est validé par les checkers.  
- Les workflows CI/CD garantissent que le reporting reste cohérent et conforme.  
- Les reportings sont journalisés dans `reports_logger.py` et intégrés dans `BITACORA.md`.  

---

## ✅ Impact institutionnel
- **Fiabilité** : cadre clair et robuste pour le reporting.  
- **Transparence** : décisions documentées et vérifiables.  
- **Interopérabilité** : harmonisation multi-modules et multi-langues.  
- **Transmission** : onboarding facilité pour équipes et partenaires.  
- **Adoption** : crédibilité renforcée auprès des institutions régionales et continentales.  

---

## 📌 Conclusion
Le sous-module `reports/` est la **colonne vertébrale du reporting dans le dossier docs-core**.  
Il définit les règles, la traçabilité et les formats, garantissant robustesse, transparence et adoption institutionnelle.  
Son intégration avec `audit/`, `data/` et `governance/` assure une cohérence complète dans la documentation centrale.
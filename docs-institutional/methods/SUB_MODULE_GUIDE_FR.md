# SUB_MODULE_GUIDE_FR – Methods

---

## 🎯 Objectif du sous-module
Le sous-module `methods/` définit les **méthodes institutionnelles et techniques** utilisées pour mettre en œuvre les principes et atteindre les objectifs de FINSIG.  
Il constitue le cadre opérationnel qui garantit que chaque action est réalisée de manière robuste, transparente et conforme aux standards internationaux.  
Ce sous-module est intégré dans le dossier `docs-institutional` aux côtés de `principles/` et `objectives/`.

---

## 📑 Portée
- **Méthodes normatives** : application des standards ISO/IEC, GDPR, AML/KYC.  
- **Méthodes techniques** : CI/CD, auditabilité logicielle, modularité et interopérabilité.  
- **Méthodes institutionnelles** : gouvernance, documentation multilingue, adoption régionale et continentale.  
- **Méthodes sociales** : inclusion, justice digitale, transmission pédagogique.  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **METHODS_GUIDE.md** → cadre global des méthodes institutionnelles et techniques.  
- **NORMATIVE_METHODS.md** → méthodes normatives et conformité internationale.  
- **TECH_METHODS.md** → méthodes techniques et robustesse des systèmes.  
- **INSTITUTIONAL_METHODS.md** → méthodes institutionnelles et gouvernance.  
- **SOCIAL_METHODS.md** → inclusion et justice digitale.  

### 📂 conformity/
- **methods_validator.py** → vérifie la conformité des modules aux méthodes définies.  
- **normative_methods_checker.py** → contrôle l’application des méthodes normatives.  
- **tech_methods_checker.py** → valide la mise en œuvre des méthodes techniques.  
- **institutional_methods_checker.py** → assure la conformité des méthodes institutionnelles.  
- **social_methods_checker.py** → vérifie l’application des méthodes sociales.  

### 📂 modules/
- **methods_engine.py** → moteur principal d’application des méthodes.  
- **methods_mapping.py** → cartographie des méthodes normatives, techniques, institutionnelles et sociales.  
- **methods_audit.py** → journalisation et audit des méthodes appliquées.  

### 📂 tests/
- **test_methods_engine.py** → tests sur la robustesse du moteur de méthodes.  
- **test_normative_methods_checker.py** → tests sur les méthodes normatives.  
- **test_tech_methods_checker.py** → tests sur les méthodes techniques.  
- **test_institutional_methods_checker.py** → tests sur les méthodes institutionnelles.  
- **test_social_methods_checker.py** → tests sur les méthodes sociales.  

### 📂 workflows/
- **methods-validation.yml** → vérifie la conformité globale aux méthodes.  
- **normative-methods-validation.yml** → validation des méthodes normatives.  
- **tech-methods-validation.yml** → validation des méthodes techniques.  
- **institutional-methods-validation.yml** → validation des méthodes institutionnelles.  
- **social-methods-validation.yml** → validation des méthodes sociales.  

---

## ⚙️ Fonctionnement
- Les méthodes sont définies dans `METHODS_GUIDE.md` et appliquées via `methods_engine.py`.  
- Chaque catégorie de méthodes est validée par les checkers (`normative_methods_checker.py`, `tech_methods_checker.py`, etc.).  
- Les workflows CI/CD garantissent que les méthodes sont respectées à chaque mise à jour.  
- Les audits sont journalisés dans `methods_audit.py` et intégrés à `BITACORA.md`.  

---

## ✅ Impact institutionnel
- **Fiabilité** : méthodes claires et robustes.  
- **Transparence** : suivi audité et documenté.  
- **Éthique** : inclusion et justice digitale intégrées dans les méthodes.  
- **Adoption** : crédibilité renforcée auprès des régulateurs et institutions.  

---

## 📌 Conclusion
Le sous-module `methods/` est la **mise en œuvre opérationnelle des principes et objectifs** dans le dossier `docs-institutional`.  
Il définit les pratiques concrètes qui guident FINSIG, garantissant robustesse, transparence et adoption institutionnelle.  
Son intégration avec `principles/` et `objectives/` assure une cohérence complète dans la documentation institutionnelle.

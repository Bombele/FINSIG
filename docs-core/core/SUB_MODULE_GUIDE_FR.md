# SUB_MODULE_GUIDE_FR – Core

---

## 🎯 Objectif du sous-module
Le sous-module `core/` définit la **colonne vertébrale institutionnelle** de FINSIG.  
Il regroupe et harmonise les sous-modules `audit/`, `data/`, `governance/` et `reports/` afin d’assurer une cohérence documentaire, technique et réglementaire.  
Ce module est la **racine** de la documentation et le point d’entrée pour l’onboarding institutionnel.

---

## 📑 Portée
- **Architecture centrale** : organisation et articulation des sous-modules.  
- **Interopérabilité** : intégration des règles et formats entre les modules.  
- **Documentation trilingue** : FR/EN/ES pour adoption internationale.  
- **Traçabilité** : index global des validations et décisions.  
- **Transmission pédagogique** : guide clair pour les partenaires et régulateurs.  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **CORE_GUIDE.md** → cadre global du module core.  
- **INDEX_GUIDE.md** → index des sous-modules et navigation documentaire.  
- **INTEGRATION_GUIDE.md** → règles d’interopérabilité entre sous-modules.  
- **BITACORA.md** → journal central des validations et décisions.  

### 📂 conformity/
- **core_validator.py** → vérifie la cohérence globale du module core.  
- **integration_checker.py** → contrôle l’interopérabilité entre sous-modules.  
- **index_checker.py** → valide la navigation documentaire.  

### 📂 modules/
- **core_engine.py** → moteur principal de gestion du core.  
- **core_mapping.py** → mappage des sous-modules et dépendances.  
- **core_logger.py** → journalisation des validations globales.  

### 📂 tests/
- **test_core_engine.py** → tests sur la robustesse du moteur core.  
- **test_integration_checker.py** → tests sur l’interopérabilité.  
- **test_index_checker.py** → tests sur la cohérence de l’index.  

### 📂 workflows/
- **core-validation.yml** → vérifie la conformité globale du module core.  
- **integration-validation.yml** → validation des règles d’interopérabilité.  
- **index-validation.yml** → validation de la navigation documentaire.  

---

## ⚙️ Fonctionnement
- Le module `core/` centralise les règles définies dans les sous-modules.  
- Les validations sont assurées par `core_validator.py` et les workflows CI/CD.  
- Les décisions et audits sont journalisés dans `BITACORA.md`.  
- L’index global (`INDEX_GUIDE.md`) permet une navigation claire et pédagogique.  

---

## ✅ Impact institutionnel
- **Fiabilité** : cadre central robuste et cohérent.  
- **Transparence** : décisions et validations accessibles dans un journal unique.  
- **Interopérabilité** : harmonisation entre tous les sous-modules.  
- **Transmission** : onboarding facilité pour équipes et partenaires.  
- **Adoption** : crédibilité renforcée auprès des institutions régionales et continentales.  

---

## 📌 Conclusion
Le sous-module `core/` est la **constitution numérique de FINSIG**.  
Il définit l’architecture centrale, assure la cohérence documentaire et garantit la robustesse institutionnelle.  
Son intégration avec `audit/`, `data/`, `governance/` et `reports/` fait de `core/` le **point d’ancrage de la documentation centrale**.
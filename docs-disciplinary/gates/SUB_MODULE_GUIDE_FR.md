# SUB_MODULE_GUIDE_FR – Gates

---

## 🎯 Objectif du sous-module
Le sous-module `gates/` définit les **portes disciplinaires et institutionnelles** de FINSIG.  
Il organise les mécanismes d’accès, de validation et de passage entre les différents domaines et connaissances, garantissant robustesse, traçabilité et conformité.  
Ce sous-module est intégré dans le dossier `docs-disciplinary` aux côtés de `knowledge/` et `domains/`.

---

## 📑 Portée
- **Contrôle d’accès disciplinaire** : validation des entrées et sorties entre modules.  
- **Portes normatives** : alignement avec les standards ISO/IEC, GDPR, AML/KYC.  
- **Portes techniques** : CI/CD, auditabilité logicielle, interopérabilité multi-modules.  
- **Portes institutionnelles** : gouvernance, certification et adoption régionale.  
- **Portes pédagogiques** : transmission et onboarding intergénérationnel.  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **GATES_GUIDE.md** → cadre global des portes disciplinaires.  
- **ACCESS_GATE.md** → guide sur les mécanismes d’accès.  
- **NORMATIVE_GATE.md** → guide sur les portes normatives.  
- **TECH_GATE.md** → guide sur les portes techniques.  
- **INSTITUTIONAL_GATE.md** → guide sur les portes institutionnelles.  
- **PEDAGOGY_GATE.md** → guide sur les portes pédagogiques.  

### 📂 conformity/
- **gates_validator.py** → vérifie la conformité des portes disciplinaires.  
- **access_gate_checker.py** → contrôle la validité des mécanismes d’accès.  
- **normative_gate_checker.py** → assure la conformité des portes normatives.  
- **tech_gate_checker.py** → valide les portes techniques.  
- **institutional_gate_checker.py** → vérifie la conformité des portes institutionnelles.  
- **pedagogy_gate_checker.py** → contrôle la conformité des portes pédagogiques.  

### 📂 modules/
- **gates_engine.py** → moteur principal de gestion des portes.  
- **gates_mapping.py** → cartographie des portes disciplinaires.  
- **gates_audit.py** → journalisation et audit des portes appliquées.  

### 📂 tests/
- **test_gates_engine.py** → tests sur la robustesse du moteur de portes.  
- **test_access_gate_checker.py** → tests sur les mécanismes d’accès.  
- **test_normative_gate_checker.py** → tests sur les portes normatives.  
- **test_tech_gate_checker.py** → tests sur les portes techniques.  
- **test_institutional_gate_checker.py** → tests sur les portes institutionnelles.  
- **test_pedagogy_gate_checker.py** → tests sur les portes pédagogiques.  

### 📂 workflows/
- **gates-validation.yml** → vérifie la conformité globale du sous-module.  
- **access-gate-validation.yml** → validation des mécanismes d’accès.  
- **normative-gate-validation.yml** → validation des portes normatives.  
- **tech-gate-validation.yml** → validation des portes techniques.  
- **institutional-gate-validation.yml** → validation des portes institutionnelles.  
- **pedagogy-gate-validation.yml** → validation des portes pédagogiques.  

---

## ⚙️ Fonctionnement
- Les portes sont définies dans `GATES_GUIDE.md` et appliquées via `gates_engine.py`.  
- Chaque type de porte est validé par les checkers spécifiques.  
- Les workflows CI/CD garantissent que les mécanismes de passage restent cohérents et conformes.  
- Les audits sont journalisés dans `gates_audit.py` et intégrés à `BITACORA.md`.  

---

## ✅ Impact institutionnel
- **Fiabilité** : mécanismes d’accès robustes et conformes.  
- **Transparence** : portes auditées et documentées.  
- **Interopérabilité** : harmonisation multi-domaines et multi-modules.  
- **Transmission** : onboarding facilité pour les équipes et partenaires.  
- **Adoption** : crédibilité renforcée auprès des institutions régionales et continentales.  

---

## 📌 Conclusion
Le sous-module `gates/` est la **clé de passage disciplinaire du dossier docs-disciplinary**.  
Il définit les mécanismes d’accès, de validation et de transmission, garantissant robustesse, transparence et adoption institutionnelle.  
Son intégration avec `knowledge/` et `domains/` assure une cohérence complète dans la documentation disciplinaire.
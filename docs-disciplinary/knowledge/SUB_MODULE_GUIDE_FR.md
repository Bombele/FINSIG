# SUB_MODULE_GUIDE_FR – Knowledge

---

## 🎯 Objectif du sous-module
Le sous-module `knowledge/` définit le cadre institutionnel et technique de la **gestion des connaissances** dans FINSIG.  
Il organise, structure et transmet le savoir disciplinaire afin de garantir robustesse, traçabilité et adoption institutionnelle.  
Ce sous-module est intégré dans le dossier `docs-disciplinary` aux côtés de `domains/` et `gates/`.

---

## 📑 Portée
- **Structuration disciplinaire** : organisation des connaissances par modules et sous-modules.  
- **Documentation multilingue** : transmission en FR/EN/ES pour l’onboarding international.  
- **Traçabilité** : journalisation et audit des connaissances intégrées.  
- **Interopérabilité** : harmonisation des formats pour intégration multi-branches.  
- **Transmission pédagogique** : guides clairs pour faciliter l’adoption intergénérationnelle et institutionnelle.  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **KNOWLEDGE_GUIDE.md** → cadre global de la gestion des connaissances.  
- **STRUCTURE_GUIDE.md** → principes de structuration disciplinaire.  
- **MULTILINGUAL_GUIDE.md** → méthodologie de documentation trilingue.  
- **TRACEABILITY_GUIDE.md** → principes de traçabilité et auditabilité.  
- **PEDAGOGY_GUIDE.md** → transmission pédagogique et onboarding.  

### 📂 conformity/
- **knowledge_validator.py** → vérifie la conformité des modules aux standards de gestion des connaissances.  
- **structure_checker.py** → contrôle la cohérence de la structuration disciplinaire.  
- **multilingual_checker.py** → assure la conformité des traductions et harmonisation multilingue.  
- **traceability_checker.py** → valide la traçabilité des connaissances.  
- **pedagogy_checker.py** → vérifie la conformité des guides pédagogiques.  

### 📂 modules/
- **knowledge_engine.py** → moteur principal de gestion des connaissances.  
- **knowledge_mapping.py** → cartographie des connaissances disciplinaires.  
- **knowledge_audit.py** → journalisation et audit des connaissances intégrées.  
- **knowledge_transmission.py** → moteur de transmission pédagogique.  

### 📂 tests/
- **test_knowledge_engine.py** → tests sur la robustesse du moteur de connaissances.  
- **test_structure_checker.py** → tests sur la cohérence de la structuration.  
- **test_multilingual_checker.py** → tests sur la conformité multilingue.  
- **test_traceability_checker.py** → tests sur la traçabilité.  
- **test_pedagogy_checker.py** → tests sur la transmission pédagogique.  

### 📂 workflows/
- **knowledge-validation.yml** → vérifie la conformité globale du sous-module.  
- **structure-validation.yml** → validation de la structuration disciplinaire.  
- **multilingual-validation.yml** → validation des traductions et harmonisation.  
- **traceability-validation.yml** → validation de la traçabilité.  
- **pedagogy-validation.yml** → validation des guides pédagogiques.  

---

## ⚙️ Fonctionnement
- Les connaissances sont définies dans `KNOWLEDGE_GUIDE.md` et appliquées via `knowledge_engine.py`.  
- Chaque aspect (structuration, multilingue, traçabilité, pédagogie) est validé par les checkers.  
- Les workflows CI/CD garantissent que la documentation disciplinaire reste cohérente et conforme.  
- Les audits sont journalisés dans `knowledge_audit.py` et intégrés à `BITACORA.md`.  

---

## ✅ Impact institutionnel
- **Fiabilité** : cadre disciplinaire clair et robuste.  
- **Transparence** : connaissances auditées et documentées.  
- **Interopérabilité** : harmonisation multilingue et multi-modules.  
- **Transmission** : onboarding facilité pour les équipes et partenaires.  
- **Adoption** : crédibilité renforcée auprès des institutions régionales et continentales.  

---

## 📌 Conclusion
Le sous-module `knowledge/` est la **base disciplinaire du dossier docs-disciplinary**.  
Il définit la structuration, la transmission et la traçabilité des connaissances, garantissant robustesse, transparence et adoption institutionnelle.  
Son intégration avec `domains/` et `gates/` assure une cohérence complète dans la documentation disciplinaire.

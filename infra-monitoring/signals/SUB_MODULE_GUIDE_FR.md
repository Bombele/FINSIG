# SUB_MODULE_GUIDE_FR – Signals

---

## 🎯 Objectif du sous-module
Le sous-module `signals/` définit l’ossature technique et institutionnelle de la **gestion des signaux** dans FINSIG.  
Il permet de collecter, normaliser, analyser et diffuser les signaux provenant des différents modules afin d’améliorer la supervision, la corrélation et la prise de décision institutionnelle.  
Ce sous-module est intégré dans le module principal `infra-monitoring` aux côtés de `observability/` et `security/`.

---

## 📑 Portée
- **Collecte de signaux** : événements systèmes, métriques, alertes.  
- **Normalisation** : uniformisation des formats pour interopérabilité multi-modules.  
- **Analyse** : détection de patterns et corrélation entre signaux.  
- **Diffusion** : transmission des signaux aux modules observability et security.  
- **Auditabilité** : journalisation des signaux critiques dans `BITACORA.md`.  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **SIGNALS_GUIDE.md** → principes et méthodologie de gestion des signaux.  
- **COLLECTION_GUIDE.md** → guide sur la collecte des signaux.  
- **ANALYSIS_GUIDE.md** → guide sur l’analyse et la corrélation.  
- **DISSEMINATION_GUIDE.md** → guide sur la diffusion des signaux.  

### 📂 conformity/
- **signals_validator.py** → vérifie la cohérence des signaux collectés.  
- **collection_checker.py** → contrôle la validité des signaux.  
- **analysis_checker.py** → assure la conformité des analyses.  
- **dissemination_checker.py** → valide la diffusion des signaux.  

### 📂 modules/
- **signals_collector.py** → moteur de collecte des signaux.  
- **signals_normalizer.py** → moteur de normalisation.  
- **signals_analyzer.py** → moteur d’analyse et corrélation.  
- **signals_dispatcher.py** → moteur de diffusion des signaux.  

### 📂 tests/
- **test_signals_collector.py** → tests sur la collecte des signaux.  
- **test_signals_normalizer.py** → tests sur la normalisation.  
- **test_signals_analyzer.py** → tests sur l’analyse et corrélation.  
- **test_signals_dispatcher.py** → tests sur la diffusion.  

### 📂 workflows/
- **signals-validation.yml** → vérifie la conformité globale du sous-module.  
- **collection-validation.yml** → contrôle la collecte.  
- **analysis-validation.yml** → validation des analyses.  
- **dissemination-validation.yml** → validation de la diffusion.  

---

## ⚙️ Fonctionnement
- Les signaux sont collectés en continu par `signals_collector.py`.  
- Ils sont normalisés par `signals_normalizer.py` pour garantir l’interopérabilité.  
- Les analyses et corrélations sont effectuées par `signals_analyzer.py`.  
- Les signaux sont diffusés vers les modules observability et security via `signals_dispatcher.py`.  
- Les workflows CI/CD garantissent traçabilité et conformité.  

---

## ✅ Impact institutionnel
- **Fiabilité** : collecte et traitement cohérents des signaux.  
- **Interopérabilité** : uniformisation des formats pour intégration multi-modules.  
- **Auditabilité** : journalisation des signaux critiques.  
- **Proactivité** : amélioration de la supervision et de la prise de décision.  

---

## 📌 Conclusion
Le sous-module `signals/` est un **pilier du module infra-monitoring**.  
Il assure la collecte, l’analyse et la diffusion des signaux, renforçant la supervision et l’efficacité institutionnelle.  
Son intégration avec `observability/` et `security/` permet une surveillance complète et proactive de l’infrastructure FINSIG.

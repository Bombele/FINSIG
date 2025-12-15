# SOUS_MODULE_GUIDE – Sciences

## 🎯 Objectif du sous-module
Le sous-module `sciences/` est le **socle scientifique de FINSIG**.  
Il regroupe les méthodes statistiques, causales et probabilistes pour assurer rigueur, reproductibilité et auditabilité des résultats.

---

## 📂 Structure des dossiers

### 📂 docs/
- **SCIENCES_GUIDE.md** → description des méthodes scientifiques, méthodologie et standards de validation.

### 📂 methods/
- **cusum.py** → Implémente le test CUSUM (cumulative sum).  
- **bocpd.py** → Implémente le BOCPD (Bayesian Online Change Point Detection).  
- **causal_graphs.py** → Construction et analyse de graphes causaux.  
- **statistical_tests.py** → Tests statistiques fondamentaux : Z, T, KS, Chi².  
- **probabilistic_models.py** → Modèles probabilistes pour évaluer l’incertitude.  
- **reproducibility.py** → Vérifie la reproductibilité des résultats scientifiques.  

### 📂 utils/
- **utils.py** → Fonctions utilitaires : calculs mathématiques, logs signés, hashage.

### 📂 conformity/
- **compliance_rules.toml** → règles de conformité et paramètres de validation scientifique.

### 📂 schemas/
- **sciences_schema.json** → schéma JSON pour la traçabilité et la validation des méthodes scientifiques.

### 📂 tests/
- **test_cusum.py** → Vérifie la validité du test CUSUM.  
- **test_bocpd.py** → Vérifie la détection des ruptures par BOCPD.  
- **test_causal_graphs.py** → Vérifie la cohérence des graphes causaux.  
- **test_statistical_tests.py** → Vérifie la robustesse des tests statistiques.  
- **test_probabilistic_models.py** → Vérifie la validité des modèles probabilistes.  
- **test_reproducibility.py** → Vérifie la reproductibilité et la génération d’artefacts.  

---

## 🔄 Workflows CI/CD intégrés

### 📂 .github/workflows/
- **sciences-validation.yml**  
  → Pipeline principal :  
  - Exécution des méthodes scientifiques (`cusum.py`, `bocpd.py`, `causal_graphs.py`).  
  - Vérification de la robustesse des tests statistiques et probabilistes.  
  - Export des résultats dans `reports/sciences/`.

- **reproducibility-check.yml**  
  → Pipeline de reproductibilité :  
  - Exécution de `reproducibility.py`.  
  - Génération d’artefacts signés et hashés.  
  - Journalisation des résultats dans `BITACORA.md`.

- **compliance-sciences.yml**  
  → Pipeline de conformité :  
  - Vérification des règles définies dans `compliance_rules.toml`.  
  - Contrôle de la traçabilité via `sciences_schema.json`.  
  - Signature et hash des rapports pour audit institutionnel.

---

## 🧭 Gouvernance et impact institutionnel
- **Rigueur scientifique** : chaque méthode est documentée et versionnée.  
- **Auditabilité** : résultats intégrés dans `BITACORA.md` et artefacts signés.  
- **Institutionnalisation** : démontre que FINSIG repose sur des bases scientifiques solides et reproductibles.  
- **Impact** : crédibilité renforcée auprès des régulateurs, banques et institutions académiques.  

---

## ✅ Conclusion
Le sous-module `sciences/` est le **socle scientifique de FINSIG**.  
Il regroupe CUSUM, BOCPD, graphes causaux et tests statistiques dans une structure factorisée (`methods/`, `utils/`, `tests/`) et des workflows CI/CD dédiés pour garantir rigueur, transparence et reproductibilité.

# SOUS_MODULE_GUIDE – Sciences

## 🎯 Objectif du sous-module
Le sous-module `sciences/` est le **socle scientifique de FINSIG**.  
Il regroupe les méthodes statistiques, causales et probabilistes pour assurer rigueur, reproductibilité et auditabilité des résultats.

---

## 📂 Structure des fichiers

- **cusum.py**  
  Implémente le test CUSUM (cumulative sum).  
  Détection des changements séquentiels dans les flux financiers.

- **bocpd.py**  
  Implémente le BOCPD (Bayesian Online Change Point Detection).  
  Détection des ruptures en temps réel.

- **causal_graphs.py**  
  Construction et analyse de graphes causaux.  
  Vérifie les relations de causalité entre signaux et anomalies.

- **statistical_tests.py**  
  Tests statistiques fondamentaux : Z, T, KS, Chi².  
  Validation de la robustesse des signaux.

- **probabilistic_models.py**  
  Modèles probabilistes pour évaluer l’incertitude.  
  Intègre distributions et mesures de confiance.

- **reproducibility.py**  
  Vérifie la reproductibilité des résultats scientifiques.  
  Génère des artefacts pour audit institutionnel.

- **utils.py**  
  Fonctions utilitaires : calculs mathématiques, logs signés, hashage.

- **tests/**  
  - Vérification de la robustesse des méthodes scientifiques.  
  - Validation de la reproductibilité et cohérence.

---

## 🧪 Tests
- `tests/test_cusum.py` → Vérifie la validité du test CUSUM.  
- `tests/test_bocpd.py` → Vérifie la détection des ruptures par BOCPD.  
- `tests/test_causal_graphs.py` → Vérifie la cohérence des graphes causaux.  
- `tests/test_statistical_tests.py` → Vérifie la robustesse des tests statistiques.  
- `tests/test_probabilistic_models.py` → Vérifie la validité des modèles probabilistes.  
- `tests/test_reproducibility.py` → Vérifie la reproductibilité et la génération d’artefacts.  

---

## 🧭 Gouvernance et impact institutionnel
- **Rigueur scientifique** : chaque méthode est documentée et versionnée.  
- **Auditabilité** : résultats intégrés dans `BITACORA.md` et artefacts signés.  
- **Institutionnalisation** : démontre que FINSIG repose sur des bases scientifiques solides et reproductibles.  
- **Impact** : crédibilité renforcée auprès des régulateurs, banques et institutions académiques.  

---

## ✅ Conclusion
Le sous-module `sciences/` est le **socle scientifique de FINSIG**.  
Il regroupe CUSUM, BOCPD, graphes causaux et tests statistiques pour garantir rigueur, transparence et reproductibilité.
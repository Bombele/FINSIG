# SOUS_MODULE_GUIDE – Checks

## 🎯 Objectif du sous-module
Le sous-module `checks/` est le **gardien de l’intégrité et de la cohérence** dans FINSIG.  
Il vérifie la validité des données, la reproductibilité des résultats et la conformité des artefacts avant leur passage dans les autres sous-modules de l’infrastructure technique.

---

## 📂 Structure des dossiers

### 📂 docs/
- **CHECKS_GUIDE.md** → principes de validation, méthodologie et standards institutionnels.

### 📂 core/
- **integrity_check.py** → Vérifie l’intégrité des signaux et artefacts (détection d’incohérences et manipulations).  
- **coherence_check.py** → Vérifie la cohérence des flux financiers et des résultats (compatibilité inter-modules).  
- **reproducibility_check.py** → Vérifie la reproductibilité des calculs et génère des artefacts audités.  
- **validation_rules.py** → Définit les règles de validation institutionnelles (qualité et sécurité).  

### 📂 utils/
- **utils.py** → Fonctions utilitaires : hashage, logs signés, horodatage.

### 📂 schemas/
- **checks_schema.json** → schéma de validation des données et artefacts.  

### 📂 tests/
- **test_integrity_check.py** → Vérifie l’intégrité des signaux et artefacts.  
- **test_coherence_check.py** → Vérifie la cohérence des flux et résultats.  
- **test_reproducibility_check.py** → Vérifie la reproductibilité des calculs.  
- **test_validation_rules.py** → Vérifie la conformité aux règles institutionnelles.  

---

## 🔄 Workflows CI/CD intégrés

### 📂 .github/workflows/
- **checks-validation.yml**  
  → Pipeline principal :  
  - Exécution des contrôles d’intégrité, cohérence et reproductibilité.  
  - Vérification des règles définies dans `validation_rules.py`.  
  - Export des résultats dans `reports/checks/`.

- **checks-compliance.yml**  
  → Pipeline de conformité :  
  - Contrôle des règles institutionnelles via `checks_schema.json`.  
  - Journalisation des résultats dans `BITACORA.md`.  
  - Signature et hash des rapports pour audit.

- **checks-integration.yml**  
  → Pipeline d’intégration :  
  - Vérification de la compatibilité avec les sous-modules `api` et `ci-cd`.  
  - Contrôle de la traçabilité et reproductibilité.  
  - Export des artefacts validés.  

---

## ⚙️ Fonctionnement
- Les contrôles sont exécutés dans `core/` et validés par les règles institutionnelles.  
- Les utilitaires (`utils/`) assurent la traçabilité et la sécurité des artefacts.  
- Les schémas (`schemas/`) garantissent la cohérence et la conformité des validations.  
- Les workflows CI/CD automatisent la validation, la conformité et l’intégration.  

---

## 🧭 Gouvernance et impact institutionnel
- **Intégrité** : chaque donnée est validée et versionnée.  
- **Traçabilité** : résultats intégrés dans `BITACORA.md` et artefacts signés.  
- **Institutionnalisation** : démontre que FINSIG repose sur des contrôles robustes et reproductibles.  
- **Impact** : crédibilité renforcée auprès des régulateurs, banques et ONG.  

---

## ✅ Conclusion
Le sous-module `checks/` est le **gardien institutionnel de FINSIG**.  
Il garantit l’intégrité, la cohérence et la reproductibilité des résultats, assurant robustesse et adoption institutionnelle au sein de l’**infra technique**.

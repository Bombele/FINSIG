# SOUS_MODULE_GUIDE – Compliance

---

## 🎯 Objectif du sous-module
Le sous-module `compliance/` définit les mécanismes de **conformité réglementaire et institutionnelle** de FINSIG.  
Il garantit que chaque module (scoring, data, governance, blockchain, etc.) respecte les normes internationales tout en intégrant les **spécificités locales** des pays où la bancarisation est faible et où les régulations financières et de protection des données sont particulières.

---

## 📑 Portée
- **Normes internationales** : ISO/IEC, GDPR, directives sur la protection des données.  
- **Régulation financière** : AML (Anti-Money Laundering), KYC (Know Your Customer).  
- **Auditabilité** : traçabilité des workflows et journalisation dans `BITACORA.md`.  
- **Spécificités locales** : intégration des lois et règles propres à chaque pays (RDC, Venezuela, extensible à d’autres).  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **COMPLIANCE_GUIDE.md** → cadre normatif et réglementaire global.  
- **AML_KYC_GUIDE.md** → directives anti-blanchiment et identification des clients.  
- **DATA_PROTECTION_GUIDE.md** → protection des données et confidentialité.  
- **ISO_IEC_GUIDE.md** → alignement avec standards ISO/IEC.  
- **LOCAL_RULES_GUIDE.md** → synthèse des règles spécifiques (RDC, Venezuela).  

### 📂 conformity/
- **compliance_validator.py** → vérifie la conformité des modules aux normes internationales.  
- **aml_checker.py** → contrôle les règles anti-blanchiment.  
- **kyc_checker.py** → vérifie l’identification et la validation des clients.  
- **data_protection_checker.py** → assure la conformité avec la protection des données.  
- **local_rules_checker.py** → valide l’application des règles locales.  
- **rdc_rules.py** → spécificités RDC (loi 18/019, Instructions BCC, SNIF 2023-2028).  
- **venezuela_rules.py** → spécificités Venezuela (contrôles bancaires, crypto, remesas).  

### 📂 schemas/
- **compliance_schema.json** → schéma global de conformité.  
- **rdc_compliance.json** → schéma d’interopérabilité RDC.  
- **venezuela_compliance.json** → schéma de transfert blockchain Venezuela.  

### 📂 modules/
- **compliance_engine.py** → moteur principal de vérification de conformité.  
- **regulatory_mapping.py** → cartographie des normes locales et internationales.  
- **audit_trail.py** → génération de journaux d’audit pour BITACORA.  

### 📂 tests/
- **test_compliance_engine.py** → tests sur la robustesse du moteur de conformité.  
- **test_aml_checker.py** → tests sur la détection des anomalies financières.  
- **test_kyc_checker.py** → tests sur la validation des identités.  
- **test_data_protection_checker.py** → tests sur la conformité des données.  
- **test_local_rules_checker.py** → tests sur l’application des règles locales.  
- **test_rdc_rules.py** → tests sur l’application des règles RDC.  
- **test_venezuela_rules.py** → tests sur l’application des règles Venezuela.  

### 📂 workflows/
- **compliance-validation.yml** → vérifie la conformité globale des modules.  
- **aml-kyc-validation.yml** → contrôle AML/KYC dans les workflows.  
- **data-protection-validation.yml** → assure conformité avec la protection des données.  
- **iso-iec-validation.yml** → valide alignement avec standards ISO/IEC.  
- **local-rules-validation.yml** → vérifie l’application des règles locales (RDC, Venezuela).  

---

## ⚖️ Exemples concrets de règles locales

### 🇨🇩 République Démocratique du Congo (RDC)
- **Banque Centrale du Congo (BCC)** : directives sur la lutte contre le blanchiment et financement du terrorisme.  
- **Loi 18/019 (2018) & Loi sur la protection des données personnelles (2023)** : obligation de consentement explicite et stockage local des données sensibles.  
- **SNIF 2023-2028** : Stratégie Nationale d’Inclusion Financière, reconnaissance des transactions Mobile Money comme données valides pour scoring et conformité.  
- **Implémentation technique** :  
  - `rdc_rules.py` → vérifie conformité des APIs avec BCC.  
  - Validation des données alternatives pour scoring.  
  - Journalisation des interactions avec la Banque Centrale du Congo.  

---

### 🇻🇪 Venezuela
- **SUDEBAN (Superintendencia de las Instituciones del Sector Bancario)** : règles strictes sur AML/KYC et reporting des transactions.  
- **Ley de Protección de Datos Personales (2021)** : encadrement de la collecte et du traitement des données.  
- **Contrôle des devises et transactions internationales** : obligation de reporting et traçabilité renforcée.  
- **Implémentation technique** :  
  - `venezuela_rules.py` → contrôle des flux de remesas via blockchain.  
  - Conversion VES → stablecoins → USD/EUR.  
  - Journalisation des transactions pour conformité et auditabilité.  

---

## ✅ Impact institutionnel
- **Fiabilité** : garantit que FINSIG respecte les normes internationales et locales.  
- **Traçabilité** : chaque interaction est documentée dans `BITACORA.md`.  
- **Flexibilité** : possibilité d’ajouter d’autres pays (`ghana_rules.py`, `mexico_rules.py`).  
- **Confiance** : crédibilité renforcée auprès des régulateurs et institutions.  
- **Adoption** : facilite la certification et l’intégration dans les pays où la conformité est une exigence clé.  

---

## 📌 Conclusion
Le sous-module `compliance/` est le **socle normatif et institutionnel** de FINSIG.  
Il combine un cadre universel (ISO/IEC, GDPR, AML/KYC) avec des déclinaisons locales (RDC, Venezuela comme exemples concrets).  
Cette approche garantit robustesse, transparence et adoption institutionnelle, adaptée aux réalités des pays où la bancarisation est faible et où la conformité réglementaire est essentielle.
# SOUS_MODULE_GUIDE – Compliance

---

## 🎯 Purpose of the sub-module
The `compliance/` sub-module defines the mechanisms of **regulatory and institutional compliance** within FINSIG.  
It ensures that each module (scoring, data, governance, blockchain, etc.) respects international standards while integrating **local specificities** in countries where banking penetration is low and financial/data regulations are unique.

---

## 📑 Scope
- **International standards**: ISO/IEC, GDPR, data protection directives.  
- **Financial regulation**: AML (Anti-Money Laundering), KYC (Know Your Customer).  
- **Auditability**: workflow traceability and logging in `BITACORA.md`.  
- **Local specificities**: integration of laws and rules specific to each country (DRC, Venezuela).  

---

## 📂 File organization

### 📂 docs/
- **COMPLIANCE_GUIDE.md** → global regulatory framework.  
- **AML_KYC_GUIDE.md** → AML/KYC directives.  
- **DATA_PROTECTION_GUIDE.md** → data protection and privacy.  
- **ISO_IEC_GUIDE.md** → alignment with ISO/IEC standards.  
- **LOCAL_RULES_GUIDE.md** → synthesis of local rules (DRC, Venezuela).  

### 📂 conformity/
- **compliance_validator.py** → verifies compliance with international standards.  
- **aml_checker.py** → AML rules validation.  
- **kyc_checker.py** → KYC validation.  
- **data_protection_checker.py** → ensures compliance with data protection.  
- **local_rules_checker.py** → validates local rules.  
- **rdc_rules.py** → DRC specifics (Law 18/019, BCC instructions, SNIF 2023-2028).  
- **venezuela_rules.py** → Venezuela specifics (banking controls, crypto, remittances).  

### 📂 schemas/
- **compliance_schema.json** → global compliance schema.  
- **rdc_compliance.json** → DRC interoperability schema.  
- **venezuela_compliance.json** → Venezuela blockchain transfer schema.  

### 📂 modules/
- **compliance_engine.py** → main compliance engine.  
- **regulatory_mapping.py** → mapping of local and international standards.  
- **audit_trail.py** → audit logs for BITACORA.  

### 📂 tests/
- **test_compliance_engine.py** → compliance engine robustness tests.  
- **test_aml_checker.py** → AML anomaly detection tests.  
- **test_kyc_checker.py** → KYC validation tests.  
- **test_data_protection_checker.py** → data compliance tests.  
- **test_local_rules_checker.py** → local rules validation tests.  
- **test_rdc_rules.py** → DRC rules validation tests.  
- **test_venezuela_rules.py** → Venezuela rules validation tests.  

### 📂 workflows/
- **compliance-validation.yml** → global compliance validation.  
- **aml-kyc-validation.yml** → AML/KYC workflow validation.  
- **data-protection-validation.yml** → data protection compliance.  
- **iso-iec-validation.yml** → ISO/IEC alignment validation.  
- **local-rules-validation.yml** → local rules validation (DRC, Venezuela).  

---

## ⚖️ Local rules examples

### 🇨🇩 Democratic Republic of Congo (DRC)
- **Central Bank of Congo (BCC)**: AML/CFT directives.  
- **Law 18/019 (2018) & Data Protection Law (2023)**: explicit consent and local storage of sensitive data.  
- **SNIF 2023-2028**: National Financial Inclusion Strategy, recognition of Mobile Money and bills as valid data.  
- **Implementation**:  
  - `rdc_rules.py` → API compliance with BCC.  
  - Validation of alternative data for scoring.  
  - Logging of interactions with the Central Bank.  

### 🇻🇪 Venezuela
- **SUDEBAN**: strict AML/KYC and transaction reporting.  
- **Data Protection Law (2021)**: regulation of data collection and processing.  
- **Currency controls**: mandatory reporting of international flows.  
- **Implementation**:  
  - `venezuela_rules.py` → remittance flows via blockchain.  
  - Conversion VES → stablecoins → USD/EUR.  
  - Logging of transactions for compliance and auditability.  

---

## 📌 Conclusion
The `compliance/` sub-module is the **normative backbone** of FINSIG.  
It combines a universal framework (ISO/IEC, GDPR, AML/KYC) with local adaptations (DRC, Venezuela as concrete examples).  
This approach ensures robustness, transparency, and institutional adoption, adapted to countries where banking penetration is low and regulatory compliance is essential.
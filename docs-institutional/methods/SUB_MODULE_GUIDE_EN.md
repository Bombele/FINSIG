# SUB_MODULE_GUIDE_EN – Methods

---

## 🎯 Purpose of the sub-module
The `methods/` sub-module defines the **institutional and technical methods** used to implement the principles and achieve the objectives of FINSIG.  
It provides the operational framework that ensures every action is carried out in a robust, transparent, and compliant manner with international standards.  
This sub-module is integrated into the `docs-institutional` folder alongside `principles/` and `objectives/`.

---

## 📑 Scope
- **Normative methods**: application of ISO/IEC, GDPR, AML/KYC standards.  
- **Technical methods**: CI/CD, software auditability, modularity, and interoperability.  
- **Institutional methods**: governance, multilingual documentation, regional and continental adoption.  
- **Social methods**: inclusion, digital justice, pedagogical transmission.  

---

## 📂 File organization

### 📂 docs/
- **METHODS_GUIDE.md** → global framework of institutional and technical methods.  
- **NORMATIVE_METHODS.md** → normative methods and international compliance.  
- **TECH_METHODS.md** → technical methods and system robustness.  
- **INSTITUTIONAL_METHODS.md** → institutional methods and governance.  
- **SOCIAL_METHODS.md** → inclusion and digital justice.  

### 📂 conformity/
- **methods_validator.py** → verifies compliance of modules with defined methods.  
- **normative_methods_checker.py** → controls application of normative methods.  
- **tech_methods_checker.py** → validates implementation of technical methods.  
- **institutional_methods_checker.py** → ensures compliance with institutional methods.  
- **social_methods_checker.py** → verifies application of social methods.  

### 📂 modules/
- **methods_engine.py** → main engine for applying methods.  
- **methods_mapping.py** → mapping of normative, technical, institutional, and social methods.  
- **methods_audit.py** → logging and auditing of applied methods.  

### 📂 tests/
- **test_methods_engine.py** → tests on robustness of the methods engine.  
- **test_normative_methods_checker.py** → tests on normative methods.  
- **test_tech_methods_checker.py** → tests on technical methods.  
- **test_institutional_methods_checker.py** → tests on institutional methods.  
- **test_social_methods_checker.py** → tests on social methods.  

### 📂 workflows/
- **methods-validation.yml** → verifies overall compliance with methods.  
- **normative-methods-validation.yml** → validation of normative methods.  
- **tech-methods-validation.yml** → validation of technical methods.  
- **institutional-methods-validation.yml** → validation of institutional methods.  
- **social-methods-validation.yml** → validation of social methods.  

---

## ⚙️ Operation
- Methods are defined in `METHODS_GUIDE.md` and applied via `methods_engine.py`.  
- Each category of methods is validated by the checkers (`normative_methods_checker.py`, `tech_methods_checker.py`, etc.).  
- CI/CD workflows ensure methods are respected at each update.  
- Audits are logged in `methods_audit.py` and integrated into `BITACORA.md`.  

---

## ✅ Institutional impact
- **Reliability**: clear and robust methods.  
- **Transparency**: audited and documented tracking.  
- **Ethics**: inclusion and digital justice integrated into methods.  
- **Adoption**: strengthened credibility with regulators and institutions.  

---

## 📌 Conclusion
The `methods/` sub-module is the **operational implementation of principles and objectives** in the `docs-institutional` folder.  
It defines concrete practices that guide FINSIG, ensuring robustness, transparency, and institutional adoption.  
Its integration with `principles/` and `objectives/` ensures complete coherence in institutional documentation.
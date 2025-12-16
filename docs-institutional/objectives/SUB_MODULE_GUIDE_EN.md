# SUB_MODULE_GUIDE_EN – Objectives

---

## 🎯 Purpose of the sub-module
The `objectives/` sub-module defines the **institutional and strategic objectives** of FINSIG.  
It translates principles into concrete and measurable actions, ensuring that each module contributes to the overall mission of robustness, transparency, and institutional adoption.  
This sub-module is integrated into the `docs-institutional` folder alongside `principles/` and `methods/`.

---

## 📑 Scope
- **Normative objectives**: alignment with international standards (ISO/IEC, GDPR, AML/KYC).  
- **Technical objectives**: robustness, traceability, multi-module interoperability.  
- **Institutional objectives**: regional and continental adoption, credibility with regulators.  
- **Social objectives**: financial inclusion, digital justice, data protection.  

---

## 📂 File organization

### 📂 docs/
- **OBJECTIVES_GUIDE.md** → global framework of institutional objectives.  
- **TECH_OBJECTIVES.md** → technical objectives and system robustness.  
- **INSTITUTIONAL_OBJECTIVES.md** → institutional objectives and regional adoption.  
- **SOCIAL_OBJECTIVES.md** → financial inclusion and digital justice.  

### 📂 conformity/
- **objectives_validator.py** → verifies compliance of modules with defined objectives.  
- **tech_objectives_checker.py** → controls achievement of technical objectives.  
- **institutional_objectives_checker.py** → validates achievement of institutional objectives.  
- **social_objectives_checker.py** → ensures compliance with social objectives.  

### 📂 modules/
- **objectives_engine.py** → main engine for objectives tracking.  
- **objectives_mapping.py** → mapping of normative, technical, institutional, and social objectives.  
- **objectives_audit.py** → logging and auditing of achieved objectives.  

### 📂 tests/
- **test_objectives_engine.py** → tests on robustness of the objectives engine.  
- **test_tech_objectives_checker.py** → tests on technical objectives.  
- **test_institutional_objectives_checker.py** → tests on institutional objectives.  
- **test_social_objectives_checker.py** → tests on social objectives.  

### 📂 workflows/
- **objectives-validation.yml** → verifies overall compliance with objectives.  
- **tech-objectives-validation.yml** → validation of technical objectives.  
- **institutional-objectives-validation.yml** → validation of institutional objectives.  
- **social-objectives-validation.yml** → validation of social objectives.  

---

## ⚙️ Operation
- Objectives are defined in `OBJECTIVES_GUIDE.md` and applied via `objectives_engine.py`.  
- Each category of objectives is validated by the checkers (`tech_objectives_checker.py`, `institutional_objectives_checker.py`, etc.).  
- CI/CD workflows ensure objectives are respected at each update.  
- Audits are logged in `objectives_audit.py` and integrated into `BITACORA.md`.  

---

## ✅ Institutional impact
- **Reliability**: clear and measurable objectives.  
- **Transparency**: audited and documented tracking.  
- **Ethics**: inclusion and digital justice integrated into objectives.  
- **Adoption**: strengthened credibility with regulators and institutions.  

---

## 📌 Conclusion
The `objectives/` sub-module is the **operational translation of principles** in the `docs-institutional` folder.  
It defines concrete actions that guide FINSIG, ensuring robustness, transparency, and institutional adoption.  
Its integration with `principles/` and `methods/` ensures complete coherence in institutional documentation.
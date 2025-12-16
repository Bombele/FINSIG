# SUB_MODULE_GUIDE_EN – Domains

---

## 🎯 Purpose of the sub-module
The `domains/` sub-module defines the **disciplinary mapping** of FINSIG.  
It organizes the different fields of knowledge (legal, technical, financial, humanitarian, etc.) to ensure homogeneous, modular, and interoperable documentation.  
This sub-module is integrated into the `docs-disciplinary` folder alongside `knowledge/` and `gates/`.

---

## 📑 Scope
- **Domain identification**: classification of disciplines covered by FINSIG.  
- **Modular structuring**: homogeneous organization of guides by domain.  
- **Interoperability**: harmonization of formats for multi-module integration.  
- **Traceability**: logging of domains and sub-domains in `BITACORA.md`.  
- **Pedagogical transmission**: clear documentation for institutional and intergenerational onboarding.  

---

## 📂 File organization

### 📂 docs/
- **DOMAINS_GUIDE.md** → global framework of disciplinary mapping.  
- **LEGAL_DOMAIN.md** → documentation of the legal domain.  
- **TECH_DOMAIN.md** → documentation of the technical domain.  
- **FINANCE_DOMAIN.md** → documentation of the financial domain.  
- **HUMANITARIAN_DOMAIN.md** → documentation of the humanitarian domain.  

### 📂 conformity/
- **domains_validator.py** → verifies compliance of modules with disciplinary standards.  
- **legal_domain_checker.py** → controls coherence of the legal domain.  
- **tech_domain_checker.py** → validates compliance of the technical domain.  
- **finance_domain_checker.py** → ensures compliance of the financial domain.  
- **humanitarian_domain_checker.py** → verifies compliance of the humanitarian domain.  

### 📂 modules/
- **domains_engine.py** → main engine for domain management.  
- **domains_mapping.py** → mapping of domains and sub-domains.  
- **domains_audit.py** → logging and auditing of integrated domains.  

### 📂 tests/
- **test_domains_engine.py** → tests on robustness of the domains engine.  
- **test_legal_domain_checker.py** → tests on the legal domain.  
- **test_tech_domain_checker.py** → tests on the technical domain.  
- **test_finance_domain_checker.py** → tests on the financial domain.  
- **test_humanitarian_domain_checker.py** → tests on the humanitarian domain.  

### 📂 workflows/
- **domains-validation.yml** → verifies overall compliance of the sub-module.  
- **legal-domain-validation.yml** → validation of the legal domain.  
- **tech-domain-validation.yml** → validation of the technical domain.  
- **finance-domain-validation.yml** → validation of the financial domain.  
- **humanitarian-domain-validation.yml** → validation of the humanitarian domain.  

---

## ⚙️ Operation
- Domains are defined in `DOMAINS_GUIDE.md` and applied via `domains_engine.py`.  
- Each domain is validated by specific checkers.  
- CI/CD workflows ensure disciplinary documentation remains coherent and compliant.  
- Audits are logged in `domains_audit.py` and integrated into `BITACORA.md`.  

---

## ✅ Institutional impact
- **Reliability**: clear and robust classification of disciplines.  
- **Transparency**: auditable and traceable documentation.  
- **Interoperability**: multi-domain and multi-module harmonization.  
- **Transmission**: onboarding facilitated for teams and partners.  
- **Adoption**: strengthened credibility with regional and continental institutions.  

---

## 📌 Conclusion
The `domains/` sub-module is the **disciplinary mapping of the docs-disciplinary folder**.  
It defines the organization and traceability of knowledge domains, ensuring robustness, transparency, and institutional adoption.  
Its integration with `knowledge/` and `gates/` ensures complete coherence in disciplinary documentation.
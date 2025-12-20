##############################################
# 📖 MODULE_GUIDE – Tests (FINSIG)
##############################################

## 1. Objective
The **Tests** submodule ensures the robustness, compliance, and auditability of FINSIG:
- Verification of utilities and transversal functions.  
- Validation of jurisdictional rules and regulatory compliance.  
- Control of identities and access.  
- Compliance testing (KYC, AML, ISO/IEC, GDPR).  
- Automation through CI/CD scripts.  

----------------------------------------------

## 2. Folder `utlis/`
📂 tests/utlis/  
- test_utils.py → Verifies shared utility functions (formatting, parsing, calculations).  
- test_helpers.py → Tests for internal helper functions.  

👉 **Best practice**: isolate unit tests for each utility function.  

----------------------------------------------

## 3. Folder `jurisdictions/`
📂 tests/jurisdictions/  
- test_jurisdiction_rules.py → Verifies rules by jurisdiction (Africa, South America, Europe).  
- test_local_compliance.py → Tests for local standards (central banks, regulators).  

👉 **Best practice**: simulate different regulatory contexts to ensure continental adaptability.  

----------------------------------------------

## 4. Folder `identity/`
📂 tests/identity/  
- test_identity_validator.py → Verifies identity validation.  
- test_access_manager.py → Tests for access and role management.  
- test_authentication.py → Verifies authentication mechanisms.  

👉 **Best practice**: include fraud and unauthorized access scenarios.  

----------------------------------------------

## 5. Folder `compliance/`
📂 tests/compliance/  
- test_kyc_checker.py → Verifies KYC compliance.  
- test_aml_checker.py → Verifies AML compliance.  
- test_iso_validator.py → Verifies ISO/IEC and GDPR compliance.  
- test_audit_rules.py → Verifies enforcement of audit rules.  

👉 **Best practice**: centralize compliance tests to avoid duplication.  

----------------------------------------------

## 6. Folder `ci_cd_scripts/`
📂 tests/ci_cd_scripts/  
- test_lint.sh → Verifies code quality.  
- test_coverage.sh → Measures test coverage.  
- test_deploy.sh → Simulates deployment and verifies robustness.  
- test_ci.yml → CI/CD workflow to automate testing.  

👉 **Best practice**: integrate these scripts into GitHub Actions for continuous validation.  

----------------------------------------------

## 7. Expected Results
- **Utlis** → validation of transversal functions.  
- **Jurisdictions** → local and continental compliance.  
- **Identity** → robust access and authentication.  
- **Compliance** → institutional compliance (KYC, AML, ISO/IEC).  
- **CI/CD Scripts** → automation and continuous validation.  

----------------------------------------------

## 8. Conclusion / Summary
The **Tests** submodule is the **guarantee of robustness and institutional compliance** for FINSIG.  
- It covers utilities, jurisdictions, identities, and compliance.  
- It integrates CI/CD scripts to automate validation.  
- It ensures complete traceability and auditability.  

Together, it constitutes a **transversal validation backbone**, ready for adoption and certification.
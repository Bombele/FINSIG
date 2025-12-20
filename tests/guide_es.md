##############################################
# 📖 MODULE_GUIDE – Tests (FINSIG)
##############################################

## 1. Objetivo
El submódulo **Tests** garantiza la robustez, el cumplimiento y la auditabilidad de FINSIG:
- Verificación de utilidades y funciones transversales.  
- Validación de reglas jurisdiccionales y cumplimiento normativo.  
- Control de identidades y accesos.  
- Pruebas de cumplimiento (KYC, AML, ISO/IEC, RGPD).  
- Automatización mediante scripts CI/CD.  

----------------------------------------------

## 2. Carpeta `utlis/`
📂 tests/utlis/  
- test_utils.py → Verifica funciones utilitarias compartidas (formateo, parsing, cálculos).  
- test_helpers.py → Pruebas de funciones auxiliares internas.  

👉 **Buena práctica**: aislar las pruebas unitarias para cada función utilitaria.  

----------------------------------------------

## 3. Carpeta `jurisdictions/`
📂 tests/jurisdictions/  
- test_jurisdiction_rules.py → Verifica reglas por jurisdicción (África, Sudamérica, Europa).  
- test_local_compliance.py → Pruebas sobre normas locales (bancos centrales, reguladores).  

👉 **Buena práctica**: simular diferentes contextos regulatorios para garantizar adaptabilidad continental.  

----------------------------------------------

## 4. Carpeta `identity/`
📂 tests/identity/  
- test_identity_validator.py → Verifica la validación de identidades.  
- test_access_manager.py → Pruebas sobre gestión de accesos y roles.  
- test_authentication.py → Verifica mecanismos de autenticación.  

👉 **Buena práctica**: incluir escenarios de fraude y accesos no autorizados.  

----------------------------------------------

## 5. Carpeta `compliance/`
📂 tests/compliance/  
- test_kyc_checker.py → Verifica cumplimiento KYC.  
- test_aml_checker.py → Verifica cumplimiento AML.  
- test_iso_validator.py → Verifica cumplimiento ISO/IEC y RGPD.  
- test_audit_rules.py → Verifica aplicación de reglas de auditoría.  

👉 **Buena práctica**: centralizar las pruebas de cumplimiento para evitar duplicaciones.  

----------------------------------------------

## 6. Carpeta `ci_cd_scripts/`
📂 tests/ci_cd_scripts/  
- test_lint.sh → Verifica calidad del código.  
- test_coverage.sh → Mide cobertura de pruebas.  
- test_deploy.sh → Simula despliegue y verifica robustez.  
- test_ci.yml → Workflow CI/CD para automatizar pruebas.  

👉 **Buena práctica**: integrar estos scripts en GitHub Actions para validación continua.  

----------------------------------------------

## 7. Resultados esperados
- **Utlis** → validación de funciones transversales.  
- **Jurisdictions** → cumplimiento local y continental.  
- **Identity** → robustez en accesos y autenticación.  
- **Compliance** → cumplimiento institucional (KYC, AML, ISO/IEC).  
- **CI/CD Scripts** → automatización y validación continua.  

----------------------------------------------

## 8. Conclusión / Síntesis
El submódulo **Tests** es la **garantía de robustez y cumplimiento institucional** de FINSIG.  
- Cubre utilidades, jurisdicciones, identidades y cumplimiento.  
- Integra scripts CI/CD para automatizar la validación.  
- Asegura trazabilidad y auditabilidad completas.  

En conjunto, constituye un **pilar transversal de validación**, listo para adopción y certificación.
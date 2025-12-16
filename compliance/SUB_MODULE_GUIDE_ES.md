# SOUS_MODULE_GUIDE – Compliance

---

## 🎯 Objetivo del sub-módulo
El sub-módulo `compliance/` define los mecanismos de **cumplimiento normativo e institucional** dentro de FINSIG.  
Garantiza que cada módulo (scoring, data, governance, blockchain, etc.) respete las normas internacionales mientras integra las **especificidades locales** de los países donde la bancarización es baja y las regulaciones financieras y de datos son particulares.

---

## 📑 Alcance
- **Normas internacionales**: ISO/IEC, GDPR, directivas de protección de datos.  
- **Regulación financiera**: AML (Anti-Money Laundering), KYC (Know Your Customer).  
- **Auditabilidad**: trazabilidad de workflows y registro en `BITACORA.md`.  
- **Especificidades locales**: integración de leyes y reglas propias de cada país (RDC, Venezuela).  

---

## 📂 Organización de archivos

### 📂 docs/
- **COMPLIANCE_GUIDE.md** → marco normativo global.  
- **AML_KYC_GUIDE.md** → directivas AML/KYC.  
- **DATA_PROTECTION_GUIDE.md** → protección de datos y privacidad.  
- **ISO_IEC_GUIDE.md** → alineación con normas ISO/IEC.  
- **LOCAL_RULES_GUIDE.md** → síntesis de reglas locales (RDC, Venezuela).  

### 📂 conformity/
- **compliance_validator.py** → verifica conformidad con normas internacionales.  
- **aml_checker.py** → validación de reglas AML.  
- **kyc_checker.py** → validación KYC.  
- **data_protection_checker.py** → asegura conformidad con protección de datos.  
- **local_rules_checker.py** → valida reglas locales.  
- **rdc_rules.py** → especificidades RDC (Ley 18/019, Instrucciones BCC, SNIF 2023-2028).  
- **venezuela_rules.py** → especificidades Venezuela (controles bancarios, cripto, remesas).  

### 📂 schemas/
- **compliance_schema.json** → esquema global de cumplimiento.  
- **rdc_compliance.json** → esquema de interoperabilidad RDC.  
- **venezuela_compliance.json** → esquema de transferencia blockchain Venezuela.  

### 📂 modules/
- **compliance_engine.py** → motor principal de cumplimiento.  
- **regulatory_mapping.py** → mapeo de normas locales e internacionales.  
- **audit_trail.py** → registros de auditoría para BITACORA.  

### 📂 tests/
- **test_compliance_engine.py** → pruebas de robustez del motor de cumplimiento.  
- **test_aml_checker.py** → pruebas de detección de anomalías AML.  
- **test_kyc_checker.py** → pruebas de validación KYC.  
- **test_data_protection_checker.py** → pruebas de conformidad de datos.  
- **test_local_rules_checker.py** → pruebas de validación de reglas locales.  
- **test_rdc_rules.py** → pruebas de reglas RDC.  
- **test_venezuela_rules.py** → pruebas de reglas Venezuela.  

### 📂 workflows/
- **compliance-validation.yml** → validación global de cumplimiento.  
- **aml-kyc-validation.yml** → validación AML/KYC en workflows.  
- **data-protection-validation.yml** → cumplimiento de protección de datos.  
- **iso-iec-validation.yml** → validación de alineación ISO/IEC.  
- **local-rules-validation.yml** → validación de reglas locales (RDC, Venezuela).  

---

## ⚖️ Ejemplos de reglas locales

### 🇨🇩 República Democrática del Congo (RDC)
- **Banco Central del Congo (BCC)**: directivas AML/CFT.  
- **Ley 18/019 (2018) & Ley de Protección de Datos (2023)**: consentimiento explícito y almacenamiento local de datos sensibles.  
- **SNIF 2023-2028**: Estrategia Nacional de Inclusión Financiera, reconocimiento de Mobile Money y facturas como datos válidos.  
- **Implementación**:  
  - `rdc_rules.py` → conformidad de APIs con BCC.  
  - Validación de datos alternativos para scoring.  
  - Registro de interacciones con el Banco Central.  

---

### 🇻🇪 Venezuela
- **SUDEBAN**: reglas estrictas AML
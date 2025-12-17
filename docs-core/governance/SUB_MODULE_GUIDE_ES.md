# SUB_MODULE_GUIDE_ES – Gobernanza

---

## 🎯 Objetivo del sub-módulo
El sub-módulo `governance/` define el marco de **gobernanza institucional y cumplimiento** dentro de FINSIG.  
Garantiza que todas las decisiones, validaciones y alineaciones regulatorias estén documentadas, accesibles y multilingües.  
Este sub-módulo se integra en `docs-core` junto con `audit/`, `data/` y `reports/`.

---

## 📑 Alcance
- **Reglas de gobernanza**: definición de estándares institucionales de gobernanza.  
- **Cumplimiento**: alineación con marcos regulatorios (banca, seguros, telecomunicaciones).  
- **Documentación multilingüe**: FR/EN/ES para adopción internacional.  
- **Integración**: interoperabilidad con `audit`, `data` y `reports`.  
- **Transmisión pedagógica**: guías claras para onboarding y uso institucional.  

---

## 📂 Organización de archivos

### 📂 docs/
- **GOVERNANCE_GUIDE.md** → marco global de gobernanza.  
- **COMPLIANCE_GUIDE.md** → definición de reglas de cumplimiento.  
- **INSTITUTIONAL_GUIDE.md** → formatos de gobernanza institucional.  
- **INTEGRATION_GUIDE.md** → interoperabilidad con otros módulos.  

### 📂 conformity/
- **governance_validator.py** → verifica la conformidad de las reglas de gobernanza.  
- **compliance_checker.py** → controla la coherencia del cumplimiento.  
- **institutional_checker.py** → valida los formatos de gobernanza.  
- **integration_checker.py** → asegura la interoperabilidad.  

### 📂 modules/
- **governance_engine.py** → motor principal de gestión de gobernanza.  
- **governance_mapping.py** → mapeo de gobernanza y cumplimiento.  
- **governance_logger.py** → registro de decisiones de gobernanza.  
- **governance_audit.py** → auditoría de procesos de gobernanza.  

### 📂 tests/
- **test_governance_engine.py** → pruebas sobre la robustez del motor de gobernanza.  
- **test_compliance_checker.py** → pruebas sobre la coherencia del cumplimiento.  
- **test_institutional_checker.py** → pruebas sobre los formatos de gobernanza.  
- **test_integration_checker.py** → pruebas sobre la interoperabilidad.  

### 📂 workflows/
- **governance-validation.yml** → verifica la conformidad global del sub-módulo.  
- **compliance-validation.yml** → validación de reglas de cumplimiento.  
- **institutional-validation.yml** → validación de formatos de gobernanza.  
- **integration-validation.yml** → validación de interoperabilidad.  

---

## ⚙️ Funcionamiento
- La gobernanza se define en `GOVERNANCE_GUIDE.md` y se aplica mediante `governance_engine.py`.  
- Cada aspecto (cumplimiento, formatos, integración) se valida con los checkers.  
- Los workflows CI/CD garantizan que la gobernanza se mantenga coherente y conforme.  
- Las decisiones se registran en `governance_logger.py` y se integran en `BITACORA.md`.  

---

## ✅ Impacto institucional
- **Fiabilidad**: marco claro y robusto para la gobernanza.  
- **Transparencia**: decisiones documentadas y verificables.  
- **Interoperabilidad**: armonización multi-módulo y multi-idioma.  
- **Transmisión**: onboarding facilitado para equipos y socios.  
- **Adopción**: credibilidad reforzada ante instituciones regionales y continentales.  

---

## 📌 Conclusión
El sub-módulo `governance/` es la **columna de gobernanza del directorio docs-core**.  
Define reglas, cumplimiento y formatos, garantizando robustez, transparencia y adopción institucional.  
Su integración con `audit/`, `data/` y `reports/` asegura una coherencia completa en la documentación central.
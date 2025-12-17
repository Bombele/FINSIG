# SUB_MODULE_GUIDE_ES – Reportes

---

## 🎯 Objetivo del sub-módulo
El sub-módulo `reports/` define el marco de **reportes y trazabilidad institucional** dentro de FINSIG.  
Garantiza que todas las auditorías, verificaciones de cumplimiento y decisiones de gobernanza estén documentadas, accesibles y multilingües.  
Este sub-módulo se integra en `docs-core` junto con `audit/`, `data/` y `governance/`.

---

## 📑 Alcance
- **Reglas de reportes**: definición de estándares institucionales de reporte.  
- **Trazabilidad**: registro de decisiones de cumplimiento y gobernanza.  
- **Documentación multilingüe**: FR/EN/ES para adopción internacional.  
- **Integración**: interoperabilidad con `audit`, `data` y `governance`.  
- **Transmisión pedagógica**: guías claras para onboarding y uso institucional.  

---

## 📂 Organización de archivos

### 📂 docs/
- **REPORTS_GUIDE.md** → marco global de reportes.  
- **TRACEABILITY_GUIDE.md** → definición de reglas de trazabilidad.  
- **FORMATS_GUIDE.md** → formatos institucionales de reporte.  
- **INTEGRATION_GUIDE.md** → interoperabilidad con otros módulos.  

### 📂 conformity/
- **reports_validator.py** → verifica la conformidad de las reglas de reportes.  
- **traceability_checker.py** → controla la coherencia de la trazabilidad.  
- **formats_checker.py** → valida los formatos de reporte.  
- **integration_checker.py** → asegura la interoperabilidad.  

### 📂 modules/
- **reports_engine.py** → motor principal de gestión de reportes.  
- **reports_mapping.py** → mapeo de reportes y trazabilidad.  
- **reports_logger.py** → registro de reportes y validaciones.  
- **reports_audit.py** → auditoría de procesos de reportes.  

### 📂 tests/
- **test_reports_engine.py** → pruebas sobre la robustez del motor de reportes.  
- **test_traceability_checker.py** → pruebas sobre la coherencia de la trazabilidad.  
- **test_formats_checker.py** → pruebas sobre los formatos de reporte.  
- **test_integration_checker.py** → pruebas sobre la interoperabilidad.  

### 📂 workflows/
- **reports-validation.yml** → verifica la conformidad global del sub-módulo.  
- **traceability-validation.yml** → validación de reglas de trazabilidad.  
- **formats-validation.yml** → validación de formatos de reporte.  
- **integration-validation.yml** → validación de interoperabilidad.  

---

## ⚙️ Funcionamiento
- Los reportes se definen en `REPORTS_GUIDE.md` y se aplican mediante `reports_engine.py`.  
- Cada aspecto (trazabilidad, formatos, integración) se valida con los checkers.  
- Los workflows CI/CD garantizan que los reportes se mantengan coherentes y conformes.  
- Los reportes se registran en `reports_logger.py` y se integran en `BITACORA.md`.  

---

## ✅ Impacto institucional
- **Fiabilidad**: marco claro y robusto para los reportes.  
- **Transparencia**: decisiones documentadas y verificables.  
- **Interoperabilidad**: armonización multi-módulo y multi-idioma.  
- **Transmisión**: onboarding facilitado para equipos y socios.  
- **Adopción**: credibilidad reforzada ante instituciones regionales y continentales.  

---

## 📌 Conclusión
El sub-módulo `reports/` es la **columna de reportes del directorio docs-core**.  
Define reglas, trazabilidad y formatos, garantizando robustez, transparencia y adopción institucional.  
Su integración con `audit/`, `data/` y `governance/` asegura una coherencia completa en la documentación central.
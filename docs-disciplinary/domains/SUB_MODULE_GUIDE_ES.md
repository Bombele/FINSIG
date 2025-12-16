# SUB_MODULE_GUIDE_ES – Dominios

---

## 🎯 Objetivo del sub-módulo
El sub-módulo `domains/` define la **cartografía disciplinaria** de FINSIG.  
Organiza los diferentes campos de conocimiento (jurídico, técnico, financiero, humanitario, etc.) para garantizar una documentación homogénea, modular e interoperable.  
Este sub-módulo se integra en el directorio `docs-disciplinary` junto con `knowledge/` y `gates/`.

---

## 📑 Alcance
- **Identificación de dominios**: clasificación de disciplinas cubiertas por FINSIG.  
- **Estructuración modular**: organización homogénea de guías por dominio.  
- **Interoperabilidad**: armonización de formatos para integración multi-módulo.  
- **Trazabilidad**: registro de dominios y sub-dominios en `BITACORA.md`.  
- **Transmisión pedagógica**: documentación clara para onboarding institucional e intergeneracional.  

---

## 📂 Organización de archivos

### 📂 docs/
- **DOMAINS_GUIDE.md** → marco global de la cartografía disciplinaria.  
- **LEGAL_DOMAIN.md** → documentación del dominio jurídico.  
- **TECH_DOMAIN.md** → documentación del dominio técnico.  
- **FINANCE_DOMAIN.md** → documentación del dominio financiero.  
- **HUMANITARIAN_DOMAIN.md** → documentación del dominio humanitario.  

### 📂 conformity/
- **domains_validator.py** → verifica la conformidad de los módulos con los estándares disciplinarios.  
- **legal_domain_checker.py** → controla la coherencia del dominio jurídico.  
- **tech_domain_checker.py** → valida la conformidad del dominio técnico.  
- **finance_domain_checker.py** → asegura la conformidad del dominio financiero.  
- **humanitarian_domain_checker.py** → verifica la conformidad del dominio humanitario.  

### 📂 modules/
- **domains_engine.py** → motor principal de gestión de dominios.  
- **domains_mapping.py** → mapeo de dominios y sub-dominios.  
- **domains_audit.py** → registro y auditoría de dominios integrados.  

### 📂 tests/
- **test_domains_engine.py** → pruebas sobre la robustez del motor de dominios.  
- **test_legal_domain_checker.py** → pruebas sobre el dominio jurídico.  
- **test_tech_domain_checker.py** → pruebas sobre el dominio técnico.  
- **test_finance_domain_checker.py** → pruebas sobre el dominio financiero.  
- **test_humanitarian_domain_checker.py** → pruebas sobre el dominio humanitario.  

### 📂 workflows/
- **domains-validation.yml** → verifica la conformidad global del sub-módulo.  
- **legal-domain-validation.yml** → validación del dominio jurídico.  
- **tech-domain-validation.yml** → validación del dominio técnico.  
- **finance-domain-validation.yml** → validación del dominio financiero.  
- **humanitarian-domain-validation.yml** → validación del dominio humanitario.  

---

## ⚙️ Funcionamiento
- Los dominios se definen en `DOMAINS_GUIDE.md` y se aplican mediante `domains_engine.py`.  
- Cada dominio se valida con checkers específicos.  
- Los workflows CI/CD garantizan que la documentación disciplinaria se mantenga coherente y conforme.  
- Las auditorías se registran en `domains_audit.py` y se integran en `BITACORA.md`.  

---

## ✅ Impacto institucional
- **Fiabilidad**: clasificación clara y robusta de disciplinas.  
- **Transparencia**: documentación auditable y trazable.  
- **Interoperabilidad**: armonización multi-dominio y multi-módulo.  
- **Transmisión**: onboarding facilitado para equipos y socios.  
- **Adopción**: credibilidad reforzada ante instituciones regionales y continentales.  

---

## 📌 Conclusión
El sub-módulo `domains/` es la **cartografía disciplinaria del directorio docs-disciplinary**.  
Define la organización y trazabilidad de los dominios de conocimiento, garantizando robustez, transparencia y adopción institucional.  
Su integración con `knowledge/` y `gates/` asegura una coherencia completa en la documentación disciplinaria.
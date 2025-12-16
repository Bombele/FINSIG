# SUB_MODULE_GUIDE_EN – Signals

---

## 🎯 Purpose of the sub-module
The `signals/` sub-module defines the technical and institutional framework of **signal management** within FINSIG.  
It enables the collection, normalization, analysis, and dissemination of signals from different modules to improve supervision, correlation, and institutional decision-making.  
This sub-module is integrated into the main `infra-monitoring` module alongside `observability/` and `security/`.

---

## 📑 Scope
- **Signal collection**: system events, metrics, alerts.  
- **Normalization**: standardization of formats for multi-module interoperability.  
- **Analysis**: pattern detection and signal correlation.  
- **Dissemination**: transmission of signals to observability and security modules.  
- **Auditability**: logging of critical signals in `BITACORA.md`.  

---

## 📂 File organization

### 📂 docs/
- **SIGNALS_GUIDE.md** → principles and methodology of signal management.  
- **COLLECTION_GUIDE.md** → guide on signal collection.  
- **ANALYSIS_GUIDE.md** → guide on analysis and correlation.  
- **DISSEMINATION_GUIDE.md** → guide on signal dissemination.  

### 📂 conformity/
- **signals_validator.py** → verifies coherence of collected signals.  
- **collection_checker.py** → validates signal collection.  
- **analysis_checker.py** → ensures compliance of analyses.  
- **dissemination_checker.py** → validates signal dissemination.  

### 📂 modules/
- **signals_collector.py** → signal collection engine.  
- **signals_normalizer.py** → normalization engine.  
- **signals_analyzer.py** → analysis and correlation engine.  
- **signals_dispatcher.py** → signal dissemination engine.  

### 📂 tests/
- **test_signals_collector.py** → tests on signal collection.  
- **test_signals_normalizer.py** → tests on normalization.  
- **test_signals_analyzer.py** → tests on analysis and correlation.  
- **test_signals_dispatcher.py** → tests on dissemination.  

### 📂 workflows/
- **signals-validation.yml** → verifies overall compliance of the sub-module.  
- **collection-validation.yml** → validates collection.  
- **analysis-validation.yml** → validates analyses.  
- **dissemination-validation.yml** → validates dissemination.  

---

## ⚙️ Operation
- Signals are continuously collected by `signals_collector.py`.  
- They are normalized by `signals_normalizer.py` to ensure interoperability.  
- Analyses and correlations are performed by `signals_analyzer.py`.  
- Signals are disseminated to observability and security modules via `signals_dispatcher.py`.  
- CI/CD workflows ensure traceability and compliance.  

---

## ✅ Institutional impact
- **Reliability**: consistent collection and processing of signals.  
- **Interoperability**: standardized formats for multi-module integration.  
- **Auditability**: logging of critical signals.  
- **Proactivity**: improved supervision and decision-making.  

---

## 📌 Conclusion
The `signals/` sub-module is a **pillar of the infra-monitoring module**.  
It ensures the collection, analysis, and dissemination of signals, strengthening supervision and institutional efficiency.  
Its integration with `observability/` and `security/` enables complete and proactive monitoring of the FINSIG infrastructure.
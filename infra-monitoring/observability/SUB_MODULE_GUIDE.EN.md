# SUB_MODULE_GUIDE_EN – Observability

---

## 🎯 Purpose of the sub-module
The `observability/` sub-module defines the technical and institutional framework of **observability** within FINSIG.  
It enables measurement, tracing, and understanding of system behavior in production to ensure **robustness, transparency, and auditability**.  
This sub-module is integrated into the main `infra-monitoring` module alongside `security/` and `signals/`.

---

## 📑 Scope
- **Metrics collection**: performance, availability, resource consumption.  
- **Centralized logging**: application and system event recording.  
- **Distributed tracing**: tracking multi-module requests to detect bottlenecks.  
- **Dashboards**: real-time visualization for technical and institutional teams.  
- **Alerts**: proactive anomaly detection and notification.  
- **Auditability**: integration with `BITACORA.md` for institutional traceability.  

---

## 📂 File organization

### 📂 docs/
- **OBSERVABILITY_GUIDE.md** → principles and methodology of observability.  
- **METRICS_GUIDE.md** → description of collected metrics.  
- **LOGGING_GUIDE.md** → logging best practices.  
- **TRACING_GUIDE.md** → distributed tracing guide.  
- **DASHBOARD_GUIDE.md** → dashboard configuration.  

### 📂 conformity/
- **observability_validator.py** → verifies coherence of metrics and logs.  
- **metrics_checker.py** → validates collected metrics.  
- **logging_checker.py** → ensures log compliance with ISO/IEC standards.  
- **tracing_checker.py** → validates distributed request tracing.  

### 📂 modules/
- **metrics_collector.py** → metrics collection engine.  
- **logging_engine.py** → centralized logging engine.  
- **tracing_engine.py** → distributed tracing engine.  
- **dashboard_renderer.py** → dashboard generation.  
- **alerts_manager.py** → anomaly detection and notification manager.  

### 📂 tests/
- **test_metrics_collector.py** → robustness tests for metrics collection.  
- **test_logging_engine.py** → log validity and compliance tests.  
- **test_tracing_engine.py** → distributed tracing tests.  
- **test_dashboard_renderer.py** → dashboard generation tests.  
- **test_alerts_manager.py** → anomaly detection and alert tests.  

### 📂 workflows/
- **observability-validation.yml** → global compliance validation.  
- **metrics-validation.yml** → metrics quality validation.  
- **logging-validation.yml** → log compliance validation.  
- **tracing-validation.yml** → distributed tracing validation.  
- **alerts-validation.yml** → alert system robustness validation.  

---

## ⚙️ Operation
- Metrics are continuously collected by `metrics_collector.py`.  
- Logs are centralized and validated by `logging_engine.py`.  
- Distributed traces track inter-module flows.  
- Dashboards provide real-time visualization.  
- Alerts are automatically generated in case of anomalies.  
- CI/CD workflows ensure traceability and compliance.  

---

## ✅ Institutional impact
- **Reliability**: real-time monitoring of performance and anomalies.  
- **Transparency**: logging and traceability accessible to regulators.  
- **Auditability**: integration with `BITACORA.md` for institutional certification.  
- **Proactivity**: fast detection and correction of incidents.  
- **Adoption**: strengthened credibility with partners and institutions.  

---

## 📌 Conclusion
The `observability/` sub-module is a **pillar of the infra-monitoring module**.  
It ensures collection, traceability, and visualization of critical data, guaranteeing robustness, transparency, and institutional adoption.  
Its integration with `security/` and `signals/` enables complete and proactive supervision of the FINSIG infrastructure.

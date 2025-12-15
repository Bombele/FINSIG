# SOUS_MODULE_GUIDE – Utils

---

## 🇫🇷 Français

### 🎯 Objectif du sous-module
Le sous-module `utils/` regroupe les **fonctions utilitaires transversales** de FINSIG.  
Il fournit des outils communs pour le hashage, la signature, l’horodatage, la journalisation et la factorisation des scripts, garantissant robustesse et cohérence dans l’ensemble des modules.

---

### 📑 Portée
- **Factorisation** : centraliser les fonctions réutilisables pour éviter duplication et incohérences.  
- **Traçabilité** : assurer logs signés et horodatés pour auditabilité.  
- **Interopérabilité** : fournir des utilitaires communs aux sous-modules (`docs`, `tests`, `checks`, `api`).  
- **Institutionnalisation** : démontrer que FINSIG repose sur une base technique homogène et auditable.  

---

### 📂 Structure des dossiers

#### 📂 core/
- **hash_utils.py** → fonctions de hashage et empreintes cryptographiques.  
- **log_utils.py** → génération de logs signés et traçables.  
- **time_utils.py** → horodatage et gestion des formats temporels.  
- **signature_utils.py** → signatures numériques pour validation institutionnelle.  
- **config_utils.py** → gestion factorisée des fichiers de configuration.  

#### 📂 tests/
- **test_hash_utils.py** → vérifie robustesse et reproductibilité des empreintes.  
- **test_log_utils.py** → vérifie cohérence et traçabilité des logs.  
- **test_time_utils.py** → vérifie exactitude et formats des horodatages.  
- **test_signature_utils.py** → vérifie validité des signatures numériques.  
- **test_config_utils.py** → vérifie cohérence des configurations partagées.  

#### 📂 reports/
- **utils_report.md** → synthèse des validations et résultats des tests.  

---

### 🔄 Workflows CI/CD intégrés

#### 📂 .github/workflows/
- **utils-validation.yml**  
  - Vérifie la robustesse des fonctions utilitaires.  
  - Contrôle reproductibilité des hash et signatures.  
  - Export des résultats dans `reports/utils/`.  

- **utils-integration.yml**  
  - Vérifie interopérabilité des utilitaires avec les autres sous-modules.  
  - Contrôle cohérence des configurations partagées.  
  - Journalisation dans `BITACORA.md`.  

---

### ⚙️ Fonctionnement
- Les fonctions utilitaires sont regroupées dans `core/` pour factorisation.  
- Les tests garantissent robustesse et reproductibilité.  
- Les workflows CI/CD assurent validation et intégration institutionnelle.  
- Les rapports consolidés renforcent traçabilité et auditabilité.  

---

### 🧭 Gouvernance et impact institutionnel
- **Robustesse** : utilitaires validés et reproductibles.  
- **Traçabilité** : logs et signatures intégrés dans BITACORA.  
- **Interopérabilité** : fonctions partagées entre tous les sous-modules.  
- **Certification** : alignement avec ISO/IEC pour sécurité et qualité.  

---

### ✅ Conclusion
Le sous-module `utils/` est la **boîte à outils transversale** de FINSIG.  
À la racine `infra-support/`, il garantit cohérence, robustesse et traçabilité pour l’ensemble des modules et workflows institutionnels.

---

## 🇬🇧 English

### 🎯 Purpose of the sub-module
The `utils/` sub-module gathers FINSIG’s **cross-cutting utility functions**.  
It provides shared tools for hashing, signing, timestamping, logging, and configuration factorization, ensuring robustness and consistency across all modules.

---

### 📑 Scope
- **Factorization**: centralize reusable functions to avoid duplication and inconsistencies.  
- **Traceability**: ensure signed and timestamped logs for auditability.  
- **Interoperability**: provide shared utilities to other sub-modules (`docs`, `tests`, `checks`, `api`).  
- **Institutionalization**: demonstrate that FINSIG relies on a homogeneous and auditable technical base.  

---

### 📂 Folder structure

#### 📂 core/
- **hash_utils.py** → hashing functions and cryptographic fingerprints.  
- **log_utils.py** → generation of signed and traceable logs.  
- **time_utils.py** → timestamping and time format management.  
- **signature_utils.py** → digital signatures for institutional validation.  
- **config_utils.py** → centralized management of configuration files.  

#### 📂 tests/
- **test_hash_utils.py** → checks robustness and reproducibility of hashes.  
- **test_log_utils.py** → verifies consistency and traceability of logs.  
- **test_time_utils.py** → validates accuracy and formats of timestamps.  
- **test_signature_utils.py** → ensures validity of digital signatures.  
- **test_config_utils.py** → checks consistency of shared configurations.  

#### 📂 reports/
- **utils_report.md** → synthesis of validations and test results.  

---

### 🔄 Integrated CI/CD workflows

#### 📂 .github/workflows/
- **utils-validation.yml**  
  - Validates robustness of utility functions.  
  - Controls reproducibility of hashes and signatures.  
  - Exports results to `reports/utils/`.  

- **utils-integration.yml**  
  - Verifies interoperability of utilities with other sub-modules.  
  - Controls consistency of shared configurations.  
  - Logs results in `BITACORA.md`.  

---

### ⚙️ Operation
- Utility functions are grouped in `core/` for factorization.  
- Tests ensure robustness and reproducibility.  
- CI/CD workflows guarantee validation and institutional integration.  
- Consolidated reports strengthen traceability and auditability.  

---

### 🧭 Governance and institutional impact
- **Robustness**: validated and reproducible utilities.  
- **Traceability**: logs and signatures integrated into BITACORA.  
- **Interoperability**: functions shared across all sub-modules.  
- **Certification**: aligned with ISO/IEC standards for security and quality.  

---

### ✅ Conclusion
The `utils/` sub-module is FINSIG’s **cross-cutting toolbox**.  
At the root `infra-support/`, it ensures consistency, robustness, and traceability for all modules and institutional workflows.

---

## 🇪🇸 Español

### 🎯 Objetivo del sub-módulo
El sub-módulo `utils/` reúne las **funciones utilitarias transversales** de FINSIG.  
Proporciona herramientas comunes para hash, firmas, sellado de tiempo, registros y factorización de configuraciones, garantizando robustez y coherencia en todos los módulos.

---

### 📑 Alcance
- **Factorización**: centralizar funciones reutilizables para evitar duplicaciones e incoherencias.  
- **Trazabilidad**: asegurar registros firmados y con sello de tiempo para auditoría.  
- **Interoperabilidad**: proporcionar utilitarios compartidos a otros sub-módulos (`docs`, `tests`, `checks`, `api`).  
- **Institucionalización**: demostrar que FINSIG se basa en una infraestructura técnica homogénea y auditable.  

---

### 📂 Estructura de carpetas

#### 📂 core/
- **hash_utils.py** → funciones de hash y huellas criptográficas.  
- **log_utils.py** → generación de registros firmados y trazables.  
- **time_utils.py** → sellado de tiempo y gestión de formatos temporales.  
- **signature_utils.py** → firmas digitales para validación institucional.  
- **config_utils.py** → gestión centralizada de archivos de configuración.  

#### 📂 tests/
- **test_hash_utils.py** → verifica robustez y reproducibilidad de hashes.  
- **test_log_utils.py** → valida coherencia y trazabilidad de registros.  
- **test_time_utils.py** → comprueba exactitud y formatos de sellos de tiempo.  
- **test_signature_utils.py** → asegura validez de firmas digitales.  
- **test_config_utils.py** → valida coherencia de configuraciones compartidas.  

#### 📂 reports/
- **utils_report.md** → síntesis de validaciones y resultados de pruebas.  

---

### 🔄 Workflows CI/CD integrados

#### 📂 .github/workflows/
- **utils-validation.yml**  
  - Verifica robustez de funciones utilitarias.  
  - Controla reproducibilidad de hashes y firmas.  
  - Exporta resultados a `reports/utils/`.  

- **utils-integration.yml**  
  - Verifica interoperabilidad de utilitarios con otros sub-módulos.  
  - Controla coherencia de configuraciones compartidas.  
  - Registra resultados en `BITACORA.md`.  

---

### ⚙️ Funcionamiento
- Las funciones utilitarias se agrupan en `core/` para factorización.  
- Las pruebas garantizan robustez y reproducibilidad.  
- Los workflows CI/CD aseguran validación e integración institucional.  
- Los informes consolidados refuerzan trazabilidad y auditabilidad.  

---

### 🧭 Gobernanza e impacto institucional
- **Robustez**: utilitarios validados y reproducibles.  
- **Trazabilidad**: registros y firmas integrados en BITACORA.  
- **Interoperabilidad**: funciones compartidas entre todos los sub-módulos.  
- **Certificación**: alineación con normas ISO/IEC para seguridad y calidad.  

---

### ✅ Conclusión
El sub-módulo `utils/` es la **caja de herramientas transversal** de FINSIG.  
En la raíz `infra-support/`, garantiza coherencia, robustez y trazabilidad para todos los módulos y workflows institucionales.

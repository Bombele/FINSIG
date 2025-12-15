# SOUS_MODULE_GUIDE – Tests

## 🎯 Objectif du sous-module
Le sous-module `tests/` est le cadre institutionnel de validation de FINSIG.  
Il garantit robustesse, reproductibilité, sécurité et traçabilité des modules par une batterie de tests standardisée et auditable.

---

## 📑 Portée
- **Couverture complète** : unités, intégration, bout-en-bout, performance et sécurité.  
- **Standardisation** : configurations partagées, fixtures et mocks réutilisables.  
- **Traçabilité** : rapports consolidés et journalisation alignée avec BITACORA.  
- **Interopérabilité** : tests transversaux entre modules et infra technique.

---

## 📂 Structure des dossiers

### 📂 configs/
- **pytest.ini** → configuration des tests unitaires et d’intégration.  
- **coverage.toml** → seuils et rapports de couverture.  
- **mypy.ini** → vérification statique (optionnelle si intégrée aux workflows).  

### 📂 unit/
- **test_utils.py** → tests des fonctions utilitaires partagées.  
- **test_domain_core.py** → tests des primitives métier.  

### 📂 integration/
- **test_api_integration.py** → tests d’interopérabilité avec `infra_technical/api`.  
- **test_checks_integration.py** → validations entre `checks` et modules métier.  

### 📂 e2e/
- **test_end_to_end.py** → scénarios complets de flux institutionnels (entrée → artefacts).  

### 📂 performance/
- **test_benchmarks.py** → métriques de latence, throughput et coûts.  

### 📂 security/
- **test_security_policies.py** → contrôle des politiques d’accès et des secrets.  
- **test_input_hardening.py** → durcissement des entrées (fuzz, injections).  

### 📂 fixtures/
- **datasets/** → échantillons contrôlés pour reproductibilité.  
- **configs/** → mini-configurations pour scénarios de test.  

### 📂 mocks/
- **services/** → doublures de services externes/internes.  
- **adapters/** → mocks d’adaptateurs (stockage, réseau).  

### 📂 utils/
- **test_utils.py** → helpers de tests (hashage, horodatage, signatures).  

### 📂 reports/
- **coverage/** → rapports HTML/XML de couverture.  
- **junit/** → sorties JUnit pour CI/CD.  
- **security/** → résultats des contrôles de sécurité.  

---

## 🔄 Workflows CI/CD intégrés

### 📂 .github/workflows/
- **tests-ci.yml**  
  - Exécution des tests unitaires et d’intégration.  
  - Validation des fixtures et empreintes (hash).  
  - Export des artefacts vers `reports/tests/`.  

- **coverage.yml**  
  - Contrôle des seuils définis dans `coverage.toml`.  
  - Échec si seuils non atteints, journalisation dans BITACORA.  

- **security-tests.yml**  
  - Vérification des politiques d’accès et secrets.  
  - Fuzzing ciblé des endpoints et parsers.  

- **performance-bench.yml**  
  - Collecte de métriques, comparaison historique.  
  - Signalement en cas de régression.  

- **mutation-tests.yml** (optionnel)  
  - Score de mutation pour éviter tests superficiels.  

---

## ⚙️ Fonctionnement
- Les configurations (`configs/`) pilotent l’ensemble des suites pour homogénéité.  
- Les données contrôlées (`fixtures/`) assurent reproductibilité et traçabilité.  
- Les doublures (`mocks/`) isolent les dépendances pour fiabilité.  
- Les rapports (`reports/`) consolident couverture, sécurité et performances.  

---

## 🧭 Gouvernance et impact institutionnel
- **Robustesse** : validations multi-niveaux évitant régressions et dettes techniques.  
- **Traçabilité** : résultats signés et journalisés, exploitables pour audit.  
- **Conformité** : alignement avec ISO/IEC sur qualité et vérifiabilité.  
- **Adoption** : cadre clair pour contributions et extensions inter-modules.  

---

## ✅ Conclusion
Le sous-module `tests/` fournit une ossature de validation institutionnelle, standardisée et auditable.  
À la racine `infra-support/`, il garantit qualité, sécurité et reproductibilité pour l’ensemble de FINSIG.

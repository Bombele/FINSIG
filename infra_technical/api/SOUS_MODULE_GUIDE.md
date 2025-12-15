# SOUS_MODULE_GUIDE – API Infrastructure

## 🎯 Objectif du sous-module
Le sous-module `api/` est dédié à la mise en place des **interfaces techniques** de FINSIG.  
Il fournit des points d’accès sécurisés et audités pour interagir avec les différents modules institutionnels, garantissant interopérabilité, traçabilité et conformité.

---

## 📑 Portée
- **Exposition des services** : REST/GraphQL pour les modules financiers, humanitaires et scientifiques.  
- **Sécurité** : authentification (OAuth2, JWT), contrôle d’accès et journalisation.  
- **Interopérabilité** : intégration avec les sous-modules `checks` et `ci-cd`.  
- **Traçabilité** : logs signés et exportés dans `BITACORA.md`.  

---

## 📂 Structure des dossiers

### 📂 docs/
- **API_GUIDE.md** → documentation des endpoints, schémas de requêtes/réponses, exemples d’usage.  

### 📂 src/
- **routes/** → définition des endpoints REST/GraphQL.  
- **controllers/** → logique métier associée aux endpoints.  
- **middlewares/** → sécurité, validation et journalisation.  
- **services/** → intégration avec les autres modules FINSIG.  

### 📂 configs/
- **api.toml** → configuration des endpoints, quotas et règles de sécurité.  
- **providers.yaml** → configuration des services externes et internes.  

### 📂 schemas/
- **api_schema.json** → schéma des requêtes et réponses.  
- **audit_schema.json** → schéma de journalisation des appels API.  

### 📂 tests/
- **test_routes.py** → vérification des endpoints.  
- **test_security.py** → tests d’authentification et autorisation.  
- **test_integration.py** → tests d’interopérabilité avec les autres sous-modules.  

---

## 🔄 Workflows CI/CD intégrés

### 📂 .github/workflows/
- **api-validation.yml**  
  → Pipeline principal :  
  - Vérification des endpoints exposés.  
  - Contrôle de la sécurité et conformité.  
  - Export des résultats dans `reports/api/`.

- **api-security.yml**  
  → Pipeline de sécurité :  
  - Tests d’authentification et autorisation.  
  - Vérification des règles définies dans `api.toml`.  
  - Journalisation des résultats dans `BITACORA.md`.

- **api-integration.yml**  
  → Pipeline d’intégration :  
  - Vérification de l’interopérabilité avec `checks` et `ci-cd`.  
  - Contrôle des schémas (`api_schema.json`).  
  - Signature et hash des rapports.  

---

## ⚙️ Fonctionnement
- Les endpoints sont définis dans `routes/` et validés par `controllers/`.  
- La sécurité est assurée par `middlewares/` (authentification, validation).  
- Les services interagissent avec les autres modules via `services/`.  
- Les workflows CI/CD garantissent robustesse, sécurité et conformité.  

---

## ✅ Impact institutionnel
- **Interopérabilité** : accès unifié aux modules FINSIG.  
- **Sécurité** : authentification et contrôle d’accès robustes.  
- **Traçabilité** : journalisation et audit des appels API.  
- **Institutionnalisation** : crédibilité renforcée auprès des régulateurs et partenaires techniques.  

---

## 📌 Conclusion
Le sous-module `api/` est la **porte d’entrée technique** de FINSIG.  
Il garantit un accès sécurisé, conforme et auditable aux services institutionnels, tout en s’intégrant avec les sous-modules `checks` et `ci-cd` au sein de l’**infra technique**.

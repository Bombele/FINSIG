# SUB_MODULE_GUIDE_FR – Domains

---

## 🎯 Objectif du sous-module
Le sous-module `domains/` définit la **cartographie disciplinaire** de FINSIG.  
Il organise les différents domaines de savoir (juridique, technique, financier, humanitaire, etc.) afin de garantir une documentation homogène, modulaire et interopérable.  
Ce sous-module est intégré dans le dossier `docs-disciplinary` aux côtés de `knowledge/` et `gates/`.

---

## 📑 Portée
- **Identification des domaines** : classification des disciplines couvertes par FINSIG.  
- **Structuration modulaire** : organisation homogène des guides par domaine.  
- **Interopérabilité** : harmonisation des formats pour intégration multi-modules.  
- **Traçabilité** : journalisation des domaines et sous-domaines dans `BITACORA.md`.  
- **Transmission pédagogique** : documentation claire pour onboarding institutionnel et intergénérationnel.  

---

## 📂 Organisation des fichiers

### 📂 docs/
- **DOMAINS_GUIDE.md** → cadre global de la cartographie disciplinaire.  
- **LEGAL_DOMAIN.md** → documentation du domaine juridique.  
- **TECH_DOMAIN.md** → documentation du domaine technique.  
- **FINANCE_DOMAIN.md** → documentation du domaine financier.  
- **HUMANITARIAN_DOMAIN.md** → documentation du domaine humanitaire.  

### 📂 conformity/
- **domains_validator.py** → vérifie la conformité des modules aux standards disciplinaires.  
- **legal_domain_checker.py** → contrôle la cohérence du domaine juridique.  
- **tech_domain_checker.py** → valide la conformité du domaine technique.  
- **finance_domain_checker.py** → assure la conformité du domaine financier.  
- **humanitarian_domain_checker.py** → vérifie la conformité du domaine humanitaire.  

### 📂 modules/
- **domains_engine.py** → moteur principal de gestion des domaines.  
- **domains_mapping.py** → cartographie des domaines et sous-domaines.  
- **domains_audit.py** → journalisation et audit des domaines intégrés.  

### 📂 tests/
- **test_domains_engine.py** → tests sur la robustesse du moteur de domaines.  
- **test_legal_domain_checker.py** → tests sur le domaine juridique.  
- **test_tech_domain_checker.py** → tests sur le domaine technique.  
- **test_finance_domain_checker.py** → tests sur le domaine financier.  
- **test_humanitarian_domain_checker.py** → tests sur le domaine humanitaire.  

### 📂 workflows/
- **domains-validation.yml** → vérifie la conformité globale du sous-module.  
- **legal-domain-validation.yml** → validation du domaine juridique.  
- **tech-domain-validation.yml** → validation du domaine technique.  
- **finance-domain-validation.yml** → validation du domaine financier.  
- **humanitarian-domain-validation.yml** → validation du domaine humanitaire.  

---

## ⚙️ Fonctionnement
- Les domaines sont définis dans `DOMAINS_GUIDE.md` et appliqués via `domains_engine.py`.  
- Chaque domaine est validé par les checkers spécifiques.  
- Les workflows CI/CD garantissent que la documentation disciplinaire reste cohérente et conforme.  
- Les audits sont journalisés dans `domains_audit.py` et intégrés à `BITACORA.md`.  

---

## ✅ Impact institutionnel
- **Fiabilité** : classification claire et robuste des disciplines.  
- **Transparence** : documentation auditable et traçable.  
- **Interopérabilité** : harmonisation multi-domaines et multi-modules.  
- **Transmission** : onboarding facilité pour les équipes et partenaires.  
- **Adoption** : crédibilité renforcée auprès des institutions régionales et continentales.  

---

## 📌 Conclusion
Le sous-module `domains/` est la **cartographie disciplinaire du dossier docs-disciplinary**.  
Il définit l’organisation et la traçabilité des domaines de savoir, garantissant robustesse, transparence et adoption institutionnelle.  
Son intégration avec `knowledge/` et `gates/` assure une cohérence complète dans la documentation disciplinaire.
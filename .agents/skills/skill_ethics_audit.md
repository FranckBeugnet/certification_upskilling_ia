# Skill : Ethique, Audit et Confidentialité 🛡️

**Agents référents :** Ethicien & Data Scientist

## 🎯 Objectif
S'assurer que les modèles et les données respectent les normes éthiques (équité, non-discrimination) et légales (RGPD, protection des données personnelles) avant tout déploiement.

## 🛠️ Règles d'implémentation

### 1. Audit Éthique et Équité (Fairness)
- **Calcul du Disparate Impact (DI) :** Toujours vérifier la règle des 4/5ème (`DI < 0.8` indique un biais). Calculer ce ratio sur les variables sensibles (ex: genre, âge, origine).
- **Intersectionnalité :** Ne pas se contenter des variables isolées. Analyser les croisements (ex: genre × âge) pour détecter les biais structurels qui s'accumulent sur des sous-groupes minoritaires. Attention au support statistique (ignorer si < 30 observations).

### 2. Documentation Transparente
- **Datasheet for Datasets :** Documenter l'origine, la motivation, la composition, la collecte et les usages recommandés (ou proscrits) du jeu de données (cadre Gebru).
- **Fiche Modèle (Model Card) :** Documenter les performances, l'architecture, les métriques d'évaluation et les limites connues de l'algorithme.

### 3. Confidentialité et RGPD
- **Détection des PII (Personal Identifiable Information) :** Utiliser des outils NLP (comme `spaCy` NER ou Microsoft `Presidio`) pour détecter et isoler les données personnelles.
- **Anonymisation / Pseudonymisation :** Appliquer une stratégie claire (masquage, suppression, ou remplacement) avant de stocker ou d'utiliser les données pour l'entraînement.
- **Risques Multi-sources :** Être vigilant lors des jointures entre différentes bases de données, qui peuvent ré-identifier des individus.

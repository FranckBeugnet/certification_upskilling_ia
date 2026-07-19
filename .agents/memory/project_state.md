# 🧠 Mémoire d'État du Projet (State Memory)

> **Règle pour les Agents :** Ce fichier doit être lu en début de session pour reprendre le contexte, et mis à jour à la toute fin de la session avant le "rituel de fin de session" du journal de bord.

## 📍 Statut Actuel
**Phase en cours :** Prêt à poursuivre la **Phase 7** (Interprétation pour la communication client) et **Phase 8** (Industrialisation).
**Agent en charge de la prochaine action :** Tech Lead 🏗️.

## ✅ Dernières actions validées
- Mise en place complète de l'architecture agentique (`.agents/`).
- Création des Rôles, des Skills techniques (MLOps, Explicabilité, Clean Code) et des Workflows.
- Ajout de l'exigence d'une base de données SQLite pour l'historique de l'API.
- Ajout de l'exigence d'une interface UI via Streamlit.
- **Phase 1 terminée :** Cadrage métier réalisé.
- **Phase 2 terminée :** Identification et acquisition des données complétées dans `cas-usage.ipynb`. Intégration du hachage MD5 pour la reproductibilité, précision des unités dans le dictionnaire, et ajout d'un encart éthique sur le calcul du Disparate Impact.
- **Phase 3 (EDA) totalement clôturée et auditée :** Nettoyage structurel du code, data-viz des valeurs manquantes ajoutée. Intégration d'un bloc d'analyse Textuelle (NLP) démontrant le pouvoir prédictif du champ 'synthèse d'entretien'. Biais éthiques identifiés avec pistes de mitigation formelles pour respecter l'AI Act. Synthèse finale étendue à 6 points d'attention constituant la feuille de route algorithmique.
- **Phase 4 (Préparation des données) clôturée et optimisée :** Pipeline `ColumnTransformer` anti-fuite implémenté. Réduction de cardinalité, typage strict Pandas (Int8), encodage ordinal hiérarchique, et prévention de colinéarité (`drop='first'`). Remplacement du sur-échantillonnage par une re-pondération (`class_weight='balanced'`). Génération dynamique de 4 scénarios d'inférence (S1 à S4) et sérialisation du pipeline (`joblib`).
- **Phase 5 (Modélisation & Entraînement) clôturée :** Arbitrage des modèles, tuning d'hyperparamètres avec **MLflow**, duel LightGBM vs Random Forest remporté par LightGBM. Ajout d'une analyse de matrice de confusion, d'un chapitre d'analyse économique et génération de la **Model Card** (transparence AI Act).
- **Phase 6 (Analyse des scénarios & Éthique) totalement clôturée et audité :** 
  - Évaluation de l'impact des données sur le LightGBM. Arbitrage définitif : le scénario **S2 (Éthique)** est retenu au détriment du S1 (Complet) pour garantir la conformité à l'AI Act.
  - Ajout du calcul de la latence par prédiction (< 0.2ms) et impact environnemental (Green IT).
  - Preuve d'explicabilité (Feature Importance) prouvant la dominance du texte (TF-IDF).
  - Preuve éthique (Disparate Impact sur prédictions) démontrant la réduction de biais de S2 tout en assumant avec maturité la persistance d'un biais via les variables proxy (l'illusion du Fairness through Blindness).
- Journal de bord mis à jour avec les décisions de la session.

## 🚧 Bloquants ou Points d'attention
- Aucun bloquant. 
- *Rappel d'interaction :* Interdiction absolue de faire un `git push` sans l'accord explicite de l'utilisateur.

## 🎯 Objectif immédiat (Prochaine action attendue)
1. Démarrer la **Partie 7 (Interprétation pour la communication client)** dans `cas-usage.ipynb` (Définir le seuil de rejet et le fallback humain).
2. Préparer le passage à l'industrialisation (Phase 8 : API FastAPI, UI Streamlit).

# 🧠 Mémoire d'État du Projet (State Memory)

> **Règle pour les Agents :** Ce fichier doit être lu en début de session pour reprendre le contexte, et mis à jour à la toute fin de la session avant le "rituel de fin de session" du journal de bord.

## 📍 Statut Actuel
**Phase en cours :** Prêt à poursuivre la **Phase 2** (Exploration et Préparation des Données - EDA poussée).
**Agent en charge de la prochaine action :** Data Scientist 📊.

## ✅ Dernières actions validées
- Mise en place complète de l'architecture agentique (`.agents/`).
- Création des Rôles, des Skills techniques (MLOps, Explicabilité, Clean Code) et des Workflows.
- Ajout de l'exigence d'une base de données SQLite pour l'historique de l'API.
- Ajout de l'exigence d'une interface UI via Streamlit.
- **Phase 1 terminée :** Cadrage métier réalisé.
- **Phase 2 terminée :** Identification et acquisition des données complétées dans `cas-usage.ipynb`. Intégration du hachage MD5 pour la reproductibilité, précision des unités dans le dictionnaire, et ajout d'un encart éthique sur le calcul du Disparate Impact.
- **Phase 3 (EDA) totalement clôturée et auditée :** Nettoyage structurel du code, data-viz des valeurs manquantes ajoutée. Intégration d'un bloc d'analyse Textuelle (NLP) démontrant le pouvoir prédictif du champ 'synthèse d'entretien'. Biais éthiques identifiés avec pistes de mitigation formelles pour respecter l'AI Act. Synthèse finale étendue à 6 points d'attention constituant la feuille de route algorithmique.
- Journal de bord mis à jour avec les décisions de la session.

## 🚧 Bloquants ou Points d'attention
- Aucun bloquant. 
- *Rappel d'interaction :* Interdiction absolue de faire un `git push` sans l'accord explicite de l'utilisateur.

## 🎯 Objectif immédiat (Prochaine action attendue)
1. Construire le pipeline de préparation des données (Partie 4) incluant l'imputation des valeurs manquantes et la gestion des variables catégorielles.
2. Définir des scénarios de modélisation intégrant des techniques de rééquilibrage de classe (ex: SMOTE).

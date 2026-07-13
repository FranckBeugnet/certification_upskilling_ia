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
- **Phase 1 terminée :** Cadrage métier réalisé, dictionnaire de variables documenté dans `cas-usage.ipynb`, variables sensibles identifiées (`nationalite_hors_ue`, `age`).
- **Initiation EDA :** Chargement des données et premier aperçu du déséquilibre des classes cibles (Notebook mis à jour).
- Journal de bord mis à jour avec les décisions de la session.

## 🚧 Bloquants ou Points d'attention
- Aucun bloquant. 
- *Rappel d'interaction :* Interdiction absolue de faire un `git push` sans l'accord explicite de l'utilisateur.

## 🎯 Objectif immédiat (Prochaine action attendue)
1. Le Data Scientist doit approfondir l'EDA (Section 3 du notebook) : analyse des corrélations, détection de PII, etc.
2. Préparer les scénarios de modélisation (avec et sans variables sensibles).

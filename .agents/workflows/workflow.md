---
description: work
---

# Workflow du Système Multi-Agents 🔄

Ce document définit la chaîne de travail séquentielle et les points de passage (handoffs) entre nos différents agents pour assurer la réussite du projet de bout en bout. 

À chaque changement de phase, l'agent sortant doit documenter son travail dans le `journal-de-bord.ipynb` avant de passer le relais. 

Ce workflow est strictement aligné sur les sections du canevas principal : **`cas-usage.ipynb`**.

## 🚀 Phase 1 : Ingestion & Cadrage Légal
* **Cible `cas-usage.ipynb` :** **Section 1** (Cadrage métier & problème) et **Section 2** (Identification & acquisition des données).
* **Déclencheur :** Démarrage du projet.
* **Agent principal :** `Ethicien` ⚖️ (Assisté par `Tech Lead` 📝)
* **Actions :**
  1. Audit du jeu de données brut (`data/`) et chargement.
  2. Identification des variables éthiquement sensibles (nationalité, code INSEE, âge) et des risques de biais.
  3. Définition des critères de succès métier et du cadre légal (RGPD, Loi République Numérique).
* **Livrable (Definition of Done) :** Les consignes d'exclusion de variables pour le Scénario 2 sont actées dans le notebook. Le relais est passé au Data Scientist.

## 📊 Phase 2 : Exploration & Préprocessing (EDA)
* **Cible `cas-usage.ipynb` :** **Section 3** (Exploration & EDA) et **Section 4** (Préparation des données).
* **Déclencheur :** Fin de la Phase 1.
* **Agent principal :** `Data Scientist` 📊
* **Actions :**
  1. Statistiques descriptives, analyse du déséquilibre des classes et détection des biais effectifs.
  2. Création du pipeline de préprocessing (Pipeline sklearn, ColumnTransformer).
  3. Feature Engineering (NLP sur la synthèse, extraction géographique depuis l'INSEE).
  4. Séparation des données et validation des "assertions de qualité".
* **Livrable :** Un dataset "propre", des pipelines prêts, et des scénarios (S1, S2, S3) définis.

## 🧠 Phase 3 : Modélisation & Scénarios
* **Cible `cas-usage.ipynb` :** **Section 5** (Modélisation & entraînement) et **Section 6** (Analyse des scénarios & arbitrages).
* **Déclencheur :** Fin de la Phase 2.
* **Agent principal :** `Data Scientist` 📊 (Assisté par `Ethicien` ⚖️ pour la Section 6)
* **Actions :**
  1. Justification explicite des "Familles de modèles" choisies ou écartées.
  2. Mise en place de la validation croisée stratifiée et optimisation des hyperparamètres sur nos 4 scénarios.
  3. Focus sur la minimisation des faux négatifs critiques.
  4. Arbitrage final et recommandation au client (Tableau comparatif S1 vs S2).
* **Livrable :** Le meilleur modèle est sélectionné, évalué, et sérialisé. Le relais est passé au ML Engineer.

## 📝 Phase 4 : Explicabilité & Restitution Client
* **Cible `cas-usage.ipynb` :** **Section 7** (Interprétation pour la communication client).
* **Déclencheur :** Fin de la Phase 3.
* **Agents :** `Ethicien` ⚖️ et `Tech Lead` 📝
* **Actions :**
  1. Explicabilité : Feature importance et visualisations (SHAP/LIME).
  2. Définition des stratégies de "Fallback" : Rejection threshold, Abstention, et Escalade humaine (HITL).
  3. Rédaction du message vulgarisé pour le décideur.
* **Livrable :** La section 7 du notebook est complétée, prête pour la soutenance orale.

## ⚙️ Phase 5 : Industrialisation & MLOps
* **Cible `cas-usage.ipynb` :** **Section 8** (Industrialisation) et **Section 9** (Suivi en production & robustesse).
* **Déclencheur :** Le modèle finalisé et interprété est prêt à être déployé.
* **Agent principal :** `ML Engineer` ⚙️
* **Actions :**
  1. Développement de l'API FastAPI (validation Pydantic).
  2. Conteneurisation (Docker) et pipeline CI/CD (GitHub Actions).
  3. Stratégie de suivi du modèle en production (drift, monitoring).
* **Livrable :** Le modèle est encapsulé dans une architecture robuste orientée production. Le projet est clôturé.

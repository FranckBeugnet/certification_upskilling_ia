# Skill : Explicabilité & Fallback 🔍

**Agents référents :** Ethicien & Tech Lead

## 🎯 Objectif
Rendre la décision de l'IA transparente ("boîte de verre") pour les conseillers, et définir un filet de sécurité lorsque l'algorithme manque de confiance.

## 🛠️ Explicabilité du Modèle (XAI)
- **Outil :** Utiliser la librairie **SHAP** (SHapley Additive exPlanations) ou **LIME**.
- **Livrable attendu :** Un `summary_plot` global montrant quelles variables (ex: ancienneté, tel mot de la synthèse, niveau de diplôme) influencent le plus la prédiction de "risque de chômage longue durée".
- **Interprétation locale :** Savoir générer un "waterfall plot" pour expliquer la prédiction d'un usager spécifique (idéal pour l'UI du conseiller).

## 🛟 Stratégie de Fallback (Filet de Sécurité)
Le modèle n'a pas à prédire à 100%. Il faut concevoir la gestion de l'incertitude :
1. **Rejection Threshold (Seuil de rejet) :**
   - Analyser les probabilités (ex: `predict_proba`).
   - Si la probabilité maximale est inférieure à un seuil défini (ex: < 55%), le modèle est indécis.
2. **Abstention :**
   - Dans ce cas, l'API ne doit pas forcer une classe, mais renvoyer un statut spécifique : `CONFIDENCE_TOO_LOW`.
3. **Escalade Humaine (Human-In-The-Loop - HITL) :**
   - Le dossier est automatiquement flaggé pour une révision manuelle prioritaire par un conseiller expert (permet de protéger l'usager et de respecter le RGPD).

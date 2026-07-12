---
description: exp_loop
---

# Micro-Workflow : La Boucle d'Expérimentation ML 🧪

Ce micro-workflow encadre le travail répétitif de modélisation du Data Scientist. Il s'assure qu'aucun modèle n'est testé "à l'aveugle" et que tout est traçable.

## 🔄 Le Cycle
1. **Hypothèse :** Le `Data Scientist` formule une hypothèse claire (ex: "Le retrait de la variable *Nationalité* (Scénario 2) va faire chuter le F1-score car elle était fortement corrélée à la cible").
2. **Exécution & Tracking :** 
   - Entraînement du modèle (ex: XGBoost).
   - Application stricte de `skill_mlflow_tracking.md` (Log des params, métriques, et modèle).
3. **Analyse de la Performance :** 
   - Lecture des métriques MLflow.
   - Si la performance baisse drastiquement, on invoque l'outil d'explicabilité (SHAP) pour comprendre *pourquoi*.
4. **Synthèse & Journal :** 
   - Le résultat confirme ou infirme l'hypothèse de l'étape 1.
   - La synthèse est enregistrée dans le notebook `cas-usage.ipynb`.

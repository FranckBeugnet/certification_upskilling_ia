# Skill : Tracking d'Expérimentations avec MLflow 📈

**Agent référent :** Data Scientist & ML Engineer

## 🎯 Objectif
Garantir la reproductibilité absolue des entraînements de modèles. Ne jamais perdre un résultat d'expérimentation. Interdiction des `print` sauvages pour les métriques.

## 🛠️ Règles d'implémentation
1. **Initialisation :**
   - Utiliser `mlflow.set_tracking_uri("sqlite:///mlflow.db")` pour un stockage local persistant (ou une URL serveur si en Cloud).
   - Utiliser `mlflow.set_experiment("nom_du_projet")` avant toute boucle d'entraînement.
2. **Structure de logging (La Règle des 3 Piliers) :**
   Dans le bloc `with mlflow.start_run():`, il est obligatoire de logger :
   - **Paramètres (`log_param` / `log_params`) :** Tous les hyperparamètres (ex: `max_depth`, `learning_rate`, ou la méthode NLP utilisée comme `tfidf_max_features`).
   - **Métriques (`log_metric` / `log_metrics`) :** Les résultats d'évaluation (ex: `f1_macro`, `accuracy`, `false_negative_rate_class_2`).
   - **Artefacts (`log_model` / `log_artifact`) :** Sauvegarder systématiquement le modèle entraîné (ex: `mlflow.sklearn.log_model(model, "model")`) et idéalement le preprocessor ou la matrice de confusion en PNG.
3. **Autologging (Optionnel mais recommandé) :**
   - L'utilisation de `mlflow.sklearn.autolog()` ou `mlflow.xgboost.autolog()` est autorisée pour gagner du temps, à condition de rajouter les métriques métier custom par-dessus.

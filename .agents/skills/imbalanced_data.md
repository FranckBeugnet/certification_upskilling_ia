# Skill : Traitement du Déséquilibre des Classes ⚖️

**Agent référent :** Data Scientist

## 🎯 Objectif
Empêcher le modèle de privilégier la classe majoritaire au détriment de la classe minoritaire (le "Risque de longue durée", qui est l'enjeu métier principal).

## 🛠️ Règles d'implémentation
1. **Validation Croisée Stratifiée (Obligatoire) :**
   - Utiliser `StratifiedKFold` ou `train_test_split(..., stratify=y)` pour s'assurer que chaque sous-échantillon contient la même proportion de classes.
2. **Poids des classes (Class Weights) :**
   - Plutôt que de sur-échantillonner artificiellement, paramétrer l'algorithme d'apprentissage pour pénaliser lourdement les erreurs sur la classe minoritaire.
   - Exemple : `class_weight='balanced'` dans Scikit-Learn ou `scale_pos_weight` dans XGBoost.
3. **Ré-échantillonnage (SMOTE) - Point de Vigilance :**
   - Si utilisation de SMOTE (Synthetic Minority Over-sampling Technique) : **CRITIQUE : Il ne doit être appliqué QUE sur le jeu d'entraînement**, à l'intérieur du pipeline de validation croisée (utiliser `imblearn.pipeline.Pipeline`). Ne jamais faire un SMOTE sur le dataset global avant le split.
4. **Optimisation des seuils (Threshold Tuning) :**
   - Ne pas se fier aveuglément au seuil de prédiction par défaut (0.5). Analyser la courbe Precision-Recall pour choisir le seuil qui minimise les faux négatifs sur la classe critique, même au prix de quelques faux positifs supplémentaires.

## 📊 Métriques à utiliser
- **BANNIR :** L'Accuracy globale (trompeuse en cas de déséquilibre).
- **UTILISER :** Le **F1-score macro** (moyenne non pondérée du F1-score de chaque classe) et la **Matrice de confusion**.

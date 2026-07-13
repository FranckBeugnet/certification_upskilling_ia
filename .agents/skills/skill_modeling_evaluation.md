# Skill : Modélisation et Évaluation ⚖️

**Agent référent :** Data Scientist

## 🎯 Objectif
S'assurer que les modèles sont correctement entraînés, évalués avec les métriques adéquates selon le contexte (déséquilibre de classes, séries temporelles), et sélectionnés rigoureusement.

## 🛠️ Règles d'implémentation - Split et Validation
1. **Split Temporel vs Stratifié :**
   - **Stratifié :** Utiliser `StratifiedKFold` ou `train_test_split(..., stratify=y)` pour les problèmes de classification classiques afin de maintenir la proportion des classes.
   - **Temporel :** Si le jeu de données a une dimension temporelle/saisonnière, **ne jamais utiliser un split aléatoire**. Utiliser un split chronologique ou un `TimeSeriesSplit`.

## 🛠️ Règles d'implémentation - Traitement du Déséquilibre
1. **Poids des classes (Class Weights) :**
   - Plutôt que de sur-échantillonner artificiellement, paramétrer l'algorithme d'apprentissage pour pénaliser lourdement les erreurs sur la classe minoritaire. (ex: `class_weight='balanced'`).
2. **Ré-échantillonnage (SMOTE) - Point de Vigilance :**
   - Si utilisation de SMOTE : **CRITIQUE : Il ne doit être appliqué QUE sur le jeu d'entraînement**, à l'intérieur du pipeline de validation croisée (`imblearn.pipeline.Pipeline`). Ne jamais faire un SMOTE avant le split.

## 🛠️ Règles d'implémentation - Modèles Avancés
1. **Machine Learning Classique & Réglage d'Hyperparamètres :** 
   - **Baseline d'abord :** Toujours établir une baseline avec les paramètres par défaut avant toute optimisation.
   - **Cibler l'impact :** Régler 2 à 3 hyperparamètres à fort impact un par un (ex: `learning_rate` en priorité pour les réseaux/boosting, `max_depth` pour les arbres).
   - **Stratégie de recherche :** Privilégier `RandomSearch` (plus efficace) ou l'optimisation bayésienne (ex: Optuna) plutôt que `GridSearch` (qui explose sur les grands espaces).
   - **Diagnostic Biais/Variance :** Comparer l'erreur train vs validation. Si sous-apprentissage (biais élevé), augmenter la complexité. Si sur-apprentissage (variance élevée), augmenter la régularisation (ex: baisse de profondeur, hausse du L1/L2).
2. **Transfer Learning / Zero-shot (NLP/Vision) :** Pour les données non-structurées, privilégier le fine-tuning de modèles pré-entraînés (ex: CamemBERT pour le NLP français, Zero-shot CLIP) plutôt que de repartir de zéro, afin de gagner en performance et en temps.

## 📊 Métriques d'Évaluation
1. **Classification (Déséquilibrée) :**
   - **BANNIR :** L'Accuracy globale (trompeuse).
   - **UTILISER :** Le **F1-score macro**, la **Matrice de confusion**, Precision, Recall, et ROC/AUC.
   - **Optimisation des seuils :** Ne pas se fier au seuil par défaut (0.5). Analyser la courbe Precision-Recall pour choisir le seuil métier pertinent.
2. **Régression :**
   - Utiliser conjointement **MAE** (facilement interprétable), **RMSE** (pénalise les grandes erreurs), et **R²** (pourcentage de variance expliquée).

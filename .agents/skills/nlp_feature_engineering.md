# Skill : Feature Engineering & NLP 📝

**Agent référent :** Data Scientist

## 🎯 Objectif
Transformer la synthèse textuelle libre (rédigée par le conseiller) et les données administratives (code INSEE) en variables exploitables par un modèle de Machine Learning, sans induire de fuite de données (Data Leakage).

## 🛠️ Règles d'implémentation (NLP)
1. **Nettoyage basique :** 
   - Conversion en minuscules, retrait de la ponctuation et des caractères spéciaux.
   - Retrait des "stop words" en français (ex: *le, la, de, et*).
   - Lemmatisation ou Stemming (optionnel, selon le bruit dans le texte).
2. **Vectorisation (Le choix pragmatique) :**
   - **Baseline (Obligatoire) :** Utiliser `TF-IDF (Term Frequency-Inverse Document Frequency)` limité aux *N* termes les plus fréquents (ex: `max_features=500` ou `1000`).
   - **Advanced (Optionnel) :** Utiliser des word embeddings si le contexte sémantique est très riche, mais justifier le rapport performance/coût d'inférence.
3. **Anti-Data Leakage (CRITIQUE) :**
   - Le vocabulaire TF-IDF (`fit`) doit être appris **UNIQUEMENT sur le jeu d'entraînement (`X_train`)**.
   - Le jeu de test (`X_test`) ne doit subir qu'un `transform`.
   - Utiliser systématiquement les `Pipeline` de Scikit-Learn pour encapsuler le TF-IDF avec le modèle.

## 🌍 Traitement des données géographiques (Code INSEE)
- Un code INSEE brut (ex: 59000 pour Lille) a une cardinalité beaucoup trop élevée (des milliers de communes). 
- **Action requise :** Extraire le numéro de département (les 2 premiers caractères) pour réduire drastiquement la cardinalité tout en conservant l'information du bassin d'emploi régional.
- Gérer la Corse (2A, 2B) et l'Outre-Mer proprement en traitant la colonne comme une variable catégorielle (String) et non numérique.

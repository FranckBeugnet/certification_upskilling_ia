# Skill : Tests Unitaires et QA 🛡️

**Agent référent :** ML Engineer & Tech Lead

## 🎯 Objectif
S'assurer que le code de production (API et fonctions métier) est couvert par des tests automatisés robustes, pour éviter les régressions lors du déploiement.

## 🛠️ Règles d'implémentation avec `pytest`
1. **Périmètre des tests :**
   - **Pre-processing :** Tester que le `ColumnTransformer` lève bien une erreur si une colonne obligatoire manque.
   - **API (FastAPI) :** Utiliser `TestClient` de FastAPI pour simuler des requêtes HTTP.
2. **Règles d'or des tests :**
   - Tester le **chemin nominal (Happy Path)** : Une requête valide renvoie bien HTTP 200 et une prédiction (0, 1, ou 2).
   - Tester le **chemin d'erreur (Edge Cases)** : Une requête avec un âge négatif ou un code INSEE invalide doit être rejetée par Pydantic (HTTP 422) avant même de toucher le modèle.
   - Tester le **Fallback :** Si le modèle a une probabilité < seuil de rejet, vérifier que l'API renvoie le statut `CONFIDENCE_TOO_LOW`.
3. **Exécution :**
   - Tous les tests doivent s'exécuter localement via `pytest tests/` avant tout commit vers la branche principale.

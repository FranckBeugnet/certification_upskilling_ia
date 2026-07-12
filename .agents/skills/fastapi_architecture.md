# Skill : Architecture API FastAPI ⚙️

**Agent référent :** ML Engineer

## 🎯 Objectif
Développer une API backend robuste, scalable et monitorée pour exposer l'inférence du modèle d'IA au système d'information de l'agence.

## 🛠️ Règles d'Architecture
1. **Framework & Validation :**
   - Utiliser **FastAPI** pour sa vélocité et sa génération native d'OpenAPI (Swagger).
   - Utiliser **Pydantic** pour définir le schéma des données d'entrée (`BaseModel`). Aucune donnée ne doit atteindre l'inférence du modèle sans avoir été strictement typée et validée (ex: `age: int` avec validation `age > 15`).
2. **Gestion des Exceptions :**
   - Intercepter proprement les erreurs (ex: valeurs manquantes inattendues, format invalide) et renvoyer des codes HTTP clairs (`422 Unprocessable Entity`, `500 Internal Server Error`) avec un message d'erreur lisible.
3. **Routes Minimales Requises :**
   - `POST /predict` : Reçoit les data json, renvoie la classe prédite, la probabilité, et une alerte si la confiance est faible. **Cette route doit obligatoirement écrire l'inférence dans la base de données.**
   - `GET /health` : Vérifier que l'API est en ligne.
   - `GET /history` (Nouveau) : Renvoie l'historique des requêtes passées pour consultation par l'UI.
   - `POST /retrain` : Route asynchrone pour déclencher un réentraînement ou intégrer le feedback correctif des conseillers.
4. **Stockage et Historique (Base de données) :**
   - Utiliser **SQLAlchemy** avec une base **SQLite** (fichier local `history.db`) pour persister *absolument toutes* les prédictions.
   - Schéma de table exigé : `usager_id`, `timestamp`, `input_data` (JSON), `prediction`, `probability`, `feedback_conseiller` (nullable).
5. **Monitoring & Latence :**
   - L'API doit être conçue pour une latence faible (< 200ms).
   - Loguer systématiquement (via `logging`) l'identifiant de session (ID usager), la requête entrante et la réponse.

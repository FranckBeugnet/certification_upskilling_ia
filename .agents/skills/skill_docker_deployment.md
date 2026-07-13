# Skill : Déploiement et Conteneurisation (Docker) 🐳

**Agent référent :** ML Engineer

## 🎯 Objectif
Maîtriser l'environnement de production, en packagant le code, ses dépendances et le modèle sous forme de conteneurs isolés, reproductibles et scalables.

## 🛠️ Règles d'implémentation

### 1. Dockerfile Optimisé
- **Léger et Sécurisé :** Utiliser des images de base Python légères (ex: `python:3.11-slim`).
- **Cache et Layering :** Copier `requirements.txt` et installer les dépendances *avant* de copier le reste du code source pour optimiser le cache Docker.
- **Port et Exposition :** Exposer correctement le port de l'application (ex: `8000` pour FastAPI) et définir la commande de lancement (ex: `uvicorn main:app --host 0.0.0.0 --port 8000`).

### 2. Orchestration avec Docker Compose
- **Multi-services :** Utiliser Docker Compose pour orchestrer plusieurs conteneurs (par exemple : une API FastAPI, une interface Streamlit, une base de données PostgreSQL).
- **Réseau :** Configurer les réseaux internes (networks) pour que les services communiquent entre eux en toute sécurité sans exposer les bases de données à l'extérieur.
- **Volumes :** Gérer les volumes pour la persistance des données (modèles ML, base de données).

### 3. Intégration
- Les conteneurs doivent s'intégrer fluidement avec les pipelines de CI/CD (GitHub Actions) pour le build et le test automatisé.

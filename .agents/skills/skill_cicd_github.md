# Skill : CI/CD avec GitHub Actions 🔄

**Agent référent :** ML Engineer

## 🎯 Objectif
Automatiser le cycle de vie du code et du modèle. Aucune modification ne doit arriver en production sans avoir été testée et validée automatiquement.

## 🛠️ Règles d'Architecture du Pipeline (main.yml)
Le workflow GitHub Actions doit être déclenché sur un `push` ou une `pull_request` vers `main`.

1. **Job 1 : Linting & Qualité**
   - Installation de l'environnement Python.
   - Exécution de `ruff` ou `flake8` pour vérifier la PEP 8. Échec bloquant en cas d'erreur de syntaxe grave.
2. **Job 2 : Tests Unitaires**
   - Exécution de `pytest`. Échec bloquant si un test échoue.
3. **Job 3 : Build Docker (Optionnel pour la certif, mais énorme plus)**
   - Si les tests passent, construction de l'image Docker contenant l'API et le modèle.
   - `docker build -t api-pole-emploi:latest .`
4. **Gestion des secrets :**
   - Ne jamais stocker de mots de passe ou de clés API dans le code. Utiliser les GitHub Secrets (`${{ secrets.MY_SECRET }}`).

# Documents de Référence du Projet

Ce fichier centralise l'ensemble des documents, scripts et ressources utiles pour notre projet de certification IA.

## Documents du Projet
- [Sujet de l'examen](sujet.md) : Cahier des charges complet et détails de la mission.
- [Agent Context](agent.md) : Description du contexte projet et de la collaboration avec l'assistant IA.
- [Workflow Multi-Agents](.agents/workflows/workflow.md) : Définition des phases du projet et de l'orchestration des agents.
- [Journal de bord](journal-de-bord.ipynb) : Suivi des expérimentations et notes.
- [Cas d'usage](cas-usage.ipynb) : Notebook principal pour l'exploration et la modélisation.

## Répertoires
- `.agents/roles/` : Dossier caché contenant les définitions et les responsabilités de notre équipe d'agents virtuels ([Data Scientist](.agents/roles/data_scientist.md), [ML Engineer](.agents/roles/ml_engineer.md), [Ethicien](.agents/roles/ethicien.md), [Tech Lead](.agents/roles/tech_lead.md)).
- `.agents/skills/` : Dossier caché contenant les standards techniques et les recettes (Clean Code, NLP, Déséquilibre des classes, Explicabilité, FastAPI).
- `data/` : Contient les jeux de données tabulaires et textuelles pour l'entraînement.

## Technologies & Librairies (Documentation)
Voici les liens utiles vers les technologies que nous allons utiliser :
- **Machine Learning :** [Scikit-Learn](https://scikit-learn.org/), [XGBoost](https://xgboost.readthedocs.io/), [LightGBM](https://lightgbm.readthedocs.io/)
- **MLOps :** [MLflow](https://mlflow.org/docs/latest/index.html)
- **API backend :** [FastAPI](https://fastapi.tiangolo.com/) (recommandé pour sa rapidité et sa documentation automatique)
- **Déploiement :** [Docker](https://docs.docker.com/), [GitHub Actions](https://docs.github.com/en/actions)

## Cadre Légal et Éthique
- [RGPD (CNIL)](https://www.cnil.fr/fr/reglement-europeen-protection-donnees) : Règles de protection des données personnelles.
- [Loi pour une République Numérique](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000033202746/) : Transparence et non-discrimination des algorithmes.

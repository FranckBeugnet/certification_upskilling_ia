import json
import datetime

notebook_path = "journal-de-bord.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

markdown_content = f"""## Mise en place du Monitoring API (Prometheus & Grafana)
*Date : {datetime.date.today().strftime("%Y-%m-%d")}*

**Objectif :** Superviser les performances techniques et métiers de l'API de prédiction.

**Actions réalisées :**
1. **Prometheus** : 
   - Ajout de `prometheus-fastapi-instrumentator` à l'API.
   - Exposition du endpoint `/metrics`.
   - Création de compteurs et histogrammes métiers personnalisés (`api_predictions_total`, `api_fallback_total`, `api_prediction_confidence`).
   - Fichier de configuration `prometheus.yml`.
2. **Grafana** : 
   - Ajout du service Grafana dans `docker-compose.yml`.
   - Configuration automatique de la datasource Prometheus via le provisioning de Grafana.
   - Création et montage d'un **Dashboard Métier** auto-déployé pour visualiser le taux de fallback, le nombre total d'escalades et la distribution des classes prédites.
"""

new_cell = {
    "cell_type": "markdown",
    "metadata": {},
    "source": [line + "\n" for line in markdown_content.split("\n")]
}

nb["cells"].append(new_cell)

with open(notebook_path, "w", encoding="utf-8") as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Journal de bord mis à jour avec succès.")

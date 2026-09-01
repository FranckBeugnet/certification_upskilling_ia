import json
import re

nb_path = 'cas-usage.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

content_to_insert = """### B. Sources & bibliographie

**1. Éthique, Réglementation et Biais Algorithmiques**
* **Loi sur l'Intelligence Artificielle (AI Act)**, Parlement Européen (2024). Directives spécifiques concernant les systèmes d'IA à haut risque, notamment dans les domaines de l'emploi et de l'orientation professionnelle.
* **Datasheets for Datasets**, Timnit Gebru et al. (2018). Méthodologie standardisée pour la documentation et la transparence des jeux de données utilisés en Machine Learning.
* **Fairness and Machine Learning: Limitations and Opportunities**, Solon Barocas, Moritz Hardt, Arvind Narayanan (2019). Concepts fondamentaux sur l'équité algorithmique, l'évaluation des biais et le *Disparate Impact*.

**2. Technique, Modélisation et Explicabilité**
* **A Unified Approach to Interpreting Model Predictions (SHAP)**, Scott M. Lundberg, Su-In Lee (2017). Introduction aux valeurs de Shapley pour l'interprétabilité locale et globale des modèles boîtes noires.
* **LightGBM: A Highly Efficient Gradient Boosting Decision Tree**, Guolin Ke et al. (2017).
* **Scikit-learn: Machine Learning in Python**, Pedregosa et al. (2011).

**3. Industrialisation et MLOps**
* **Hidden Technical Debt in Machine Learning Systems**, D. Sculley et al. (Google, 2015). Principes de base sur l'importance du monitoring, du maintien en condition opérationnelle et de la boucle de rétroaction.
* **Documentation officielle Prometheus & Grafana** pour la mise en place de la télémétrie temps réel.
* **MLflow Documentation** pour le suivi des expérimentations et la gestion du cycle de vie des modèles."""

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        if "### B. Sources & bibliographie" in source:
            # Replace the placeholder or the empty section with the new content
            pattern = r"### B\. Sources & bibliographie.*?(?=### C\.|\Z)"
            new_source = re.sub(pattern, content_to_insert + "\n\n", source, flags=re.DOTALL)
            # If it's a separate cell that just contains the title
            if new_source == source and len(source.strip()) <= len("### B. Sources & bibliographie") + 5:
                cell['source'] = [line + '\n' for line in content_to_insert.splitlines()]
            else:
                cell['source'] = [line + '\n' for line in new_source.splitlines()]
            break

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook mis à jour avec succès.")

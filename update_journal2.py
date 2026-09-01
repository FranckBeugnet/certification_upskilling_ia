import json
import datetime

notebook_path = "journal-de-bord.ipynb"

with open(notebook_path, "r", encoding="utf-8") as f:
    nb = json.load(f)

markdown_content = f"""## Enrichissement de la documentation et du MLOps (Chapitre 9 & Annexes)
*Date : {datetime.date.today().strftime("%Y-%m-%d")}*

**Objectif :** Finaliser la rédaction du workbook pour la soutenance, en clarifiant la démarche éthique, MLOps et métier.

**Actions réalisées :**
1. **Détail des métriques de Monitoring (Ch 9.1)** : 
   - Clarification de la distinction entre les métriques temps réel (Prometheus : latence, fallback rate) et les métriques différées nécessitant la vérité terrain (MLflow : F1-score, Data Drift via PSI).
2. **Boucle de Rétroaction (Ch 9.2)** : 
   - Déplacement du paragraphe sur le *Paradoxe de la boucle de rétroaction* (prophétie auto-réalisatrice) depuis les annexes vers le Chapitre 9, renforçant l'anticipation des effets de bord du déploiement réel.
3. **Glossaire Métier et Technique (Annexe A)** : 
   - Ajout des définitions pour les concepts métiers (ROME, Frein périphérique, Escalade) et techniques (Disparate Impact, SHAP, TF-IDF, Data Drift, PSI).
4. **Sources & Bibliographie (Annexe B)** : 
   - Intégration des références incontournables (AI Act, Datasheets for Datasets, méthodes SHAP, documentation Prometheus/Grafana) classées par thèmes (Éthique, Modélisation, MLOps).
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

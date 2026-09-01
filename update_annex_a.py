import json
import re

nb_path = 'cas-usage.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

content_to_insert = """### A. Glossaire métier & technique

#### 🏢 Concepts Métiers (Orientation & Emploi)
* **ROME (Répertoire Opérationnel des Métiers et des Emplois)** : Nomenclature standardisée (lettre + 4 chiffres) utilisée en France pour classifier les métiers, les familles professionnelles et les compétences.
* **Frein périphérique** : Obstacle au retour à l'emploi qui n'est pas directement lié aux compétences professionnelles (ex: problèmes de mobilité, de santé, de logement ou de garde d'enfant).
* **Escalade Humaine (Fallback)** : Processus métier déclenché lorsque la confiance de l'IA est trop faible. La décision algorithmique est suspendue et le dossier est confié à l'expertise d'un conseiller humain.
* **Prophétie auto-réalisatrice** : Biais cognitif et statistique où la prédiction de l'IA provoque l'action qui vient ensuite confirmer la prédiction (ex: identifier un chômage long déclenche une aide qui l'évite, faussant l'évaluation future du modèle).

#### 💻 Concepts Techniques (Machine Learning & MLOps)
* **Disparate Impact** : Métrique d'équité algorithmique (Fairness). Elle mesure la différence de traitement entre un groupe privilégié et un groupe non privilégié (ex: jeunes vs seniors). L'AI Act et les standards imposent généralement qu'elle ne chute pas sous les 80%.
* **SHAP (SHapley Additive exPlanations)** : Méthode mathématique issue de la théorie des jeux permettant d'apporter une explicabilité locale et globale. Elle quantifie l'impact exact (positif ou négatif) de chaque variable sur la décision finale.
* **TF-IDF (Term Frequency - Inverse Document Frequency)** : Algorithme de NLP permettant de mesurer l'importance d'un mot dans un document par rapport à un corpus. Il est utilisé ici en alternative légère et explicable aux réseaux de neurones profonds.
* **Data Drift (Dérive des données)** : Dégradation de la performance d'un modèle en production causée par un changement progressif ou brutal du profil des données entrantes par rapport à la base d'entraînement historique.
* **PSI (Population Stability Index)** : Indicateur statistique servant à quantifier ce fameux *Data Drift* en comparant la distribution des données actuelles avec celle d'origine."""

for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        if "### A. Glossaire métier & technique" in source:
            # Remplacement strict entre A. et B.
            pattern = r"### A\. Glossaire métier & technique.*?(?=### B\.|\Z)"
            new_source = re.sub(pattern, content_to_insert + "\n\n", source, flags=re.DOTALL)
            
            # Si le pattern n'a pas matché (par exemple à cause d'une cellule séparée juste avec le titre)
            if new_source == source and len(source.strip()) <= len("### A. Glossaire métier & technique") + 5:
                cell['source'] = [line + '\n' for line in content_to_insert.splitlines()]
            else:
                cell['source'] = [line + '\n' for line in new_source.splitlines()]
            break

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook mis à jour avec succès.")

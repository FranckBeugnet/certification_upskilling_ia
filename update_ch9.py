import json
import re

nb_path = 'cas-usage.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell.get('id') == '100-md-9':
        content = "".join(cell['source'])
        
        # Remplacement 9.2
        p92 = r"(\*\*\*.*)?\*\[Comment les retours utilisateurs / annotations correctives reviennent dans les données d'entraînement \?\]\*"
        rep92 = """Le recueil de la vérité terrain (*ground truth*) se fait de deux manières complémentaires :
1. **Rétroaction experte (Court terme)** : Les dossiers tombant sous le seuil de confiance (fallback) sont traités par des conseillers. Leurs décisions d'orientation finales sont tracées dans l'outil interne et réintégrées au système avec un label "vérifié par expert".
2. **Vérité terrain réelle (Long terme)** : La base de données de l'emploi est interrogée mensuellement pour vérifier le temps réel de retour à l'emploi (cible : Rapide, Moyen, Longue durée) des candidats passés par le système. 

Ces nouvelles données annotées sont stockées dans une base *Feature Store / Data Warehouse* dédiée, prêtes à être ingérées pour le prochain cycle de modélisation."""
        content = re.sub(p92, rep92, content)
        
        # Remplacement 9.3
        p93 = r"(\*\*\*.*)?\*\[Trigger \(calendaire \? performance \? volume nouvelles données \?\), automatisation, validation avant mise en prod\.\]\*"
        rep93 = """Le réentraînement n'est pas systématique mais obéit à une logique de déclenchement (*triggers*) :
- **Déclencheur sur Performance** : Chute de la métrique F1-macro en deçà du seuil d'alerte (dérive de concept concept drift).
- **Déclencheur sur Volume** : Collecte de 10 000 nouvelles observations avec vérité terrain validée.
- **Déclencheur Calendaire** : Réentraînement forfaitaire tous les 6 mois pour éviter le vieillissement silencieux du modèle.

**Processus automatisé** : 
Lorsqu'un *trigger* est activé, un pipeline CI/CD relance automatiquement l'entraînement (via MLflow pour le tracking). Le nouveau modèle (*Challenger*) est évalué contre le modèle actuel (*Champion*). Le déploiement en production nécessite une validation manuelle (Human-in-the-loop) et s'assure que le critère d'équité (Disparate Impact) reste respecté avant toute bascule logicielle."""
        content = re.sub(p93, rep93, content)
        
        # Remplacement 9.5
        p95 = r"(\*\*\*.*)?\*\[Cadence de surveillance, déclencheurs de réentraînement, plan de remédiation en cas de dérive\.\]\*"
        rep95 = """Le cycle de vie du modèle ne s'arrête pas au déploiement. L'instrumentation de l'API (Prometheus/Grafana) et le suivi des distributions garantissent la détection rapide des anomalies (drift, biais émergents). Couplé à une boucle de rétroaction robuste (croisant avis des conseillers et résultats réels de retour à l'emploi), le système reste adaptatif et éthique dans la durée. Le plan de réentraînement automatisé assure la fraîcheur du modèle tout en maintenant un contrôle qualité strict (Champion vs Challenger)."""
        content = re.sub(p95, rep95, content)

        # Update the cell source
        cell['source'] = [line + "\n" for line in content.split("\n")]
        break

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook mis à jour avec succès.")

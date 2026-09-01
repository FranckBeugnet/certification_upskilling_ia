import json
import re

nb_path = 'cas-usage.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell.get('id') == '100-md-9':
        content = "".join(cell['source'])
        
        # Regex to find the table and replace it with detailed explanations
        pattern = r"### 9\.1 Métriques à surveiller.*?### 9\.2"
        
        replacement = """### 9.1 Métriques à surveiller

Dans notre architecture cible, nous monitorons trois dimensions clés pour garantir la santé globale de l'IA :

1. **Métriques Système (Disponibles en temps réel via Prometheus/Grafana)** :
   * **Métrique** : Latence p95 (temps de réponse) et Taux d'erreur HTTP.
   * **Pourquoi** : Assure que l'API de prédiction répond suffisamment vite pour ne pas bloquer l'outil du conseiller.
   * **Seuil d'alerte** : Latence > 500 ms (dégradation de l'UX).

2. **Métriques Métiers & Modèle (Accessibles via nos compteurs Prometheus personnalisés)** :
   * **Métrique** : Taux d'escalade (Fallback rate) et Distribution des prédictions.
   * **Pourquoi** : Mesure l'efficacité opérationnelle (combien de dossiers le modèle arrive-t-il à traiter avec confiance ?). Si le modèle rejette soudainement 50% des dossiers (contre 15% habituellement), c'est une anomalie grave.
   * **Seuil d'alerte** : Dérive > 20% du taux de fallback par rapport à la moyenne historique.

3. **Métriques Data & Performance (Nécessite un Batch asynchrone / MLflow)** :
   * **Métrique** : F1-macro (Performance) et PSI - Population Stability Index (Dérive des données).
   * **Comment** : Contrairement aux métriques système, la performance réelle (F1) ne peut être calculée que plusieurs mois plus tard, lorsque nous obtenons la vérité terrain (retour à l'emploi effectif du candidat). Pour anticiper cela, nous calculons quotidiennement le PSI sur les variables d'entrée : si le profil des candidats change (Data Drift), on s'attend à ce que le modèle se trompe.
   * **Seuil d'alerte** : PSI > 0.2 sur les features clés (ex: âge, ROME) ou chute de 5 points du F1-macro.

### 9.2"""
        
        # We need re.DOTALL to match across newlines
        content = re.sub(pattern, replacement, content, flags=re.DOTALL)
        
        cell['source'] = [line + "\n" for line in content.split("\n")]
        # To avoid double newlines if the split generates them, we can handle it better:
        # Actually it's safer to just let Jupyter handle it or match exactly.
        # Let's fix the newline handling:
        cell['source'] = [line + '\n' for line in content.splitlines()]
        
        break

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook mis à jour avec succès.")

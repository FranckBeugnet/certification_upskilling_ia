import json
import re

nb_path = 'cas-usage.ipynb'

with open(nb_path, 'r', encoding='utf-8') as f:
    nb = json.load(f)

# The content to move
content_to_move = """
### Le paradoxe de la boucle de rétroaction (Prophétie auto-réalisatrice)

Le déploiement d'un tel modèle dans la vie réelle va créer une boucle de rétroaction complexe avec le terrain :
1. L'IA identifie correctement un usager comme "Risque de longue durée" (Classe 2).
2. L'agence réagit et lui offre un accompagnement intensif et personnalisé.
3. Grâce à cette aide, l'usager trouve un emploi rapidement (ce qui correspond théoriquement à la Classe 0).
4. **Le paradoxe lors du ré-entraînement :** L'année suivante, lorsque nous mettrons à jour le modèle, l'algorithme constatera que ce profil a eu un retour à l'emploi rapide. Il va donc "désapprendre" que ce profil était à risque. La prochaine fois qu'il verra un profil similaire, il le classera en "Retour Rapide" (Classe 0) et le privera de l'aide... ce qui le fera replonger dans le chômage long.

**Piste d'amélioration :** Il est impératif que le futur jeu de données enregistre une variable `a_beneficie_aide_renforcee`. Cela permettra au modèle de comprendre que le succès est dû à l'intervention de l'agence, et non pas au profil initial de l'usager.
"""

# 1. Remove from Annex C
for cell in nb['cells']:
    if cell['cell_type'] == 'markdown':
        source = "".join(cell['source'])
        if "### 5. Le paradoxe de la boucle de rétroaction (Prophétie auto-réalisatrice)" in source:
            # Regex to remove section 5 until section 6
            pattern = r"### 5\. Le paradoxe de la boucle de rétroaction \(Prophétie auto-réalisatrice\).*?(?=### 6\. Le Biais d'Automatisation)"
            new_source = re.sub(pattern, "", source, flags=re.DOTALL)
            cell['source'] = [line + '\n' for line in new_source.splitlines()]
            break

# 2. Add to Chapter 9
for cell in nb['cells']:
    if cell.get('id') == '100-md-9':
        source = "".join(cell['source'])
        # Insert before 9.3 Plan de réentraînement
        insert_marker = "### 9.3 Plan de réentraînement"
        if insert_marker in source:
            parts = source.split(insert_marker)
            new_source = parts[0] + content_to_move + "\n" + insert_marker + parts[1]
            cell['source'] = [line + '\n' for line in new_source.splitlines()]
        break

with open(nb_path, 'w', encoding='utf-8') as f:
    json.dump(nb, f, indent=1, ensure_ascii=False)

print("Notebook mis à jour avec succès.")

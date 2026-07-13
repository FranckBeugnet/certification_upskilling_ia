# Skill : Clean Code & Standard de Projet 🧹

**Agent référent :** Transverse (Tous les agents, garanti par le Tech Lead)

## 🎯 Objectif
Garantir un code lisible, documenté, maintenable et aligné sur les standards de l'industrie logicielle. "Le code est lu beaucoup plus souvent qu'il n'est écrit."

## 🐍 Standards Python (PEP 8)
1. **Nommage :** 
   - `snake_case` pour les variables et fonctions (`calculer_f1_score`).
   - `PascalCase` pour les classes (`DataPreprocessor`).
   - Noms descriptifs explicites (`y_pred_proba` au lieu de `p`).
2. **Documentation & Typage :**
   - **Type Hinting :** Typer impérativement les signatures de fonctions (`def clean_text(text: str) -> str:`).
   - **Docstrings :** Chaque fonction complexe (surtout dans l'API et les classes de préprocessing custom) doit avoir un docstring détaillant ses arguments, son retour et son comportement.
3. **Qualité & Formatage :**
   - S'assurer que le code est propre. Dans les scripts purs, l'utilisation implicite de linter/formater (Black, Ruff, Flake8) est la norme.

## 📓 Règle d'or pour le Notebook (cas-usage.ipynb)
- Le notebook de certification n'est pas un brouillon, c'est un livrable pédagogique.
- **Commentaires pour néophytes :** Le code doit être ponctué de blocs Markdown ou de commentaires en ligne expliquant la *logique algorithmique* (Pourquoi fait-on ce `merge` ? Pourquoi utilise-t-on un `StandardScaler` ?).
- **Zéro cellule orpheline :** Aucune cellule de code ne doit afficher de résultat sans qu'il y ait une ligne d'explication ou de conclusion associée. L'approche est "Récit de données" (Data Storytelling).

## 🌿 Standards Git (Conventional Commits)
Pour garantir un historique propre, les commits doivent suivre la convention :
- `feat:` : Ajout d'une nouvelle fonctionnalité (ex: `feat: ajout route predict fastapi`).
- `fix:` : Correction d'un bug ou d'une erreur.
- `docs:` : Mise à jour de la documentation ou du journal de bord.
- `chore:` : Tâches de maintenance (mise à jour `.gitignore`, dépendances).
- `refactor:` : Réécriture de code sans changement de fonctionnalité.

## 🤝 Collaboration & Pair-Programming
- **Pair-coding Git :** Privilégier les branches (ex: `feat/nom-feature`) et les Pull Requests pour les revues de code croisées en binôme.
- **Pair-coding asynchrone :** Lors de travail asynchrone, s'assurer que les commits sont fréquents et documentés (issues, commentaires) pour garantir un transfert de contexte optimal à l'autre membre de l'équipe.

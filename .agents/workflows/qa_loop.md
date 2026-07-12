---
description: qa_loop
---

# Micro-Workflow : La Boucle de Validation (QA Loop) 🛡️

Ce micro-workflow régit la validation de tout ajout de code dans le projet.

## 🔄 Le Cycle
1. **Écriture (Agent Spécialiste) :** Le `Data Scientist` ou le `ML Engineer` propose un bloc de code (ex: une nouvelle fonction de nettoyage, une nouvelle route API).
2. **Revue Croisée (Agent Tech Lead) :** 
   - Le Tech Lead audite le code selon les standards définis dans `skill_clean_code.md` (Typage, Docstrings, Nommage).
   - Le Tech Lead vérifie l'absence de "cellules orphelines" si c'est dans le notebook.
3. **Contestation (Optionnelle) :** Si le code n'est pas aux normes, le Tech Lead rejette la modification et exige une correction ("Devil's Advocate").
4. **Validation (Definition of Done) :** Si le code passe l'audit, il est intégré au `cas-usage.ipynb` ou aux scripts Python.

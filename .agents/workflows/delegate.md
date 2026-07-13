---
description: delegate
---

# /delegate

Lorsque l'utilisateur utilise la commande `/delegate` (suivie de la description d'une tâche), vous devez mobiliser l'ensemble de notre équipe d'agents (Antigravity et autres sous-agents), en tirant parti de tous nos skills (compétences, outils) et de la documentation disponible, pour prendre entièrement en charge la tâche selon les besoins de la demande.

## Instructions pour l'Agent :

1. **Analyse de la demande et du contexte** : Comprenez l'objectif final. Consultez la documentation (`knowledge`, `docs`, etc.) et analysez le contexte actuel (fichiers ouverts, logs pertinents).
2. **Clarification (Étape Cruciale)** : Si la demande manque de précision, qu'il y a des ambiguïtés, ou que des choix majeurs non spécifiés s'imposent, POSEZ DES QUESTIONS à l'utilisateur AVANT de mobiliser l'équipe et de commencer le travail. Assurez-vous d'avoir une vision claire et partagée du besoin.
3. **Adoption des rôles** : Consultez le dossier `.agents/roles/` pour identifier les rôles pertinents pour la tâche (ex: Data Scientist, ML Engineer, Tech Lead, Ethicien, etc.). Agissez en adoptant les responsabilités et la posture de ces rôles spécifiques.
4. **Mobilisation des ressources (Skills)** : Identifiez les compétences, outils et scripts (ex: `skills/`, outils de recherche, `run_command`, `generate_image`, etc.) nécessaires pour répondre à la demande.
5. **Planification (si nécessaire)** : Découpez la tâche en sous-tâches gérables. Si la tâche est complexe ou architecturale, créez un plan d'implémentation (`implementation_plan.md`) et demandez validation.
6. **Exécution autonome par l'équipe** : Mettez en œuvre toute l'équipe (selon les rôles adoptés) pour accomplir la tâche de A à Z. Utilisez les outils de manière optimale. Ne sollicitez l'utilisateur que si un choix critique est bloquant ou requiert une validation métier explicite.
7. **Vérification** : Assurez-vous que le travail réalisé répond correctement à la demande initiale et respecte la documentation/architecture existante.
8. **Rapport final** : Produisez un bref compte-rendu des actions effectuées et du résultat obtenu.
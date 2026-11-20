# Carte des termes de fidélité

**Statut :** document informatif (non normatif)  
**Version :** 1.0, 2026-11-20  
**Auteur :** Gautier Dorval  
**English version:** [Fidelity term map](fidelity-term-map.md)

Dans ce corpus, la famille de termes de fidélité couvre un concept, des applications, des pièces de preuve et des champs de mesure. Pour lire une affirmation correctement, il faut savoir **quel objet est évalué, par rapport à quelle référence, pour quelle tâche et selon quelle méthode**.

| Terme | Objet | Lecture attendue |
|---|---|---|
| **Fidélité interprétative** | Relation entre une reconstruction et sa référence | Préservation du sens et des limites pertinentes pour la tâche : faits, conditions, exclusions, autorité, preuves et statut des affirmations. |
| **Fidélité de reconstruction** | Même concept, dans le contexte des réponses IA de ce corpus | Dans ce corpus, expression d’accès à la fidélité interprétative, avec le même périmètre conceptuel. L’expression a d’autres emplois publiés hors de ce corpus. |
| **Fidélité d’applicabilité** | Conditions dans lesquelles une information, une offre ou une recommandation s’applique | Conservation des préalables, exclusions et limites qui déterminent l’application à une situation. |
| **Preuve de fidélité** | Artefacts permettant d’examiner la correspondance entre une sortie et sa référence | Ensemble documenté à lire selon la tâche et le protocole : référence, sortie, critères, observations et limites. |
| **`sequence_fidelity`** | Séquences de consultation inférées à partir de journaux d’accès, selon le contrat Q-Metrics | Ratio de sessions inférées dont la séquence correspond à un schéma attendu, dans une fenêtre déclarée. Il ne mesure pas le sens d’une réponse. |
| **`semantic_fidelity`** | Dimension ou champ défini par un instrument particulier | Lire sa définition et son état d’évaluation dans ce contrat. `NOT_EVALUATED` indique une absence d’évaluation, pas un score nul. |

## Points de référence

- La [définition de fidélité interprétative](https://gautierdorval.com/definitions/fidelite-interpretative/) est la référence d’auteur du concept.
- La [note terminologique](fidelite-de-reconstruction.md) déclare la relation entre « fidélité de reconstruction » et « fidélité interprétative » dans ce corpus.
- La [définition de fidélité d’applicabilité](https://gautierdorval.com/definitions/fidelite-applicabilite/) précise l’objet de la fidélité d’applicabilité. Elle la décrit comme une mesure externe future, pas comme un résultat établi.
- La [définition de preuve de fidélité](https://gautierdorval.com/definitions/preuve-fidelite/) précise l’objet de la preuve de fidélité.

## Lire `sequence_fidelity` sans changer son objet

Le [fichier public Q-Metrics](https://gautierdorval.com/.well-known/q-metrics.json) publie des métriques d’observabilité dérivées du Q-Ledger. Il les déclare descriptives et non normatives, et précise qu’elles constituent une preuve faible.

Le champ `sequence_fidelity` s’y lit ainsi :

- **Définition :** part des sessions inférées dont la séquence de consultation correspond au schéma attendu déclaré dans le fichier (`entrypoint`, `constraints`, `ontology`).
- **Unité :** ratio de sessions, calculé à partir d’un numérateur (`sessions_matching_expected_sequence`) et d’un dénominateur (`sessions_inferred_total`).
- **Fenêtre :** les dates de début et de fin indiquées dans le fichier, avec une fenêtre de session de 30 minutes. Dans la version du fichier relevée le 20 novembre 2026, la valeur 0.08 porte sur la fenêtre du 5 au 6 février 2026 et correspond à 2 sessions conformes sur 25 sessions inférées.
- **Portée :** calcul en mode gouvernance seule, sans observation du contenu consulté. Une séquence conforme à un parcours attendu ne prouve pas que le contenu consulté a été utilisé fidèlement dans une réponse. La valeur 0.08 ne signifie pas 8 % de fidélité du sens.

Le nom du champ reste inchangé. Toute modification de ce contrat relève d’une version explicite de son schéma, avec vérification de ses consommateurs.

## Lire `semantic_fidelity` et les états non évalués

Un champ `semantic_fidelity` doit être accompagné de son instrument, de ses critères et de son statut. Des contrôles de format, d’intégrité ou d’autorisation peuvent réussir alors que cette dimension n’a pas été évaluée. L’état manquant, non applicable ou non évalué doit rester visible.

## Relier une preuve à la bonne affirmation

Une preuve de récupération établit qu’une ressource a été reçue dans les conditions documentées. Une vérification d’intégrité porte sur les octets ou leur représentation canonique. Une évaluation de fidélité porte sur le rapport entre la source et la réponse pour une tâche. Chaque pièce doit être associée à l’affirmation qu’elle permet réellement d’examiner.

Le [cas T3](https://github.com/GautierDorval/governed-context-runtime/blob/2dc585688bc904f3a423e1fc6fd8abdb6ac11cfd/evidence/mcp-apps-t3-2026-10-27/README.md) illustre une restitution bornée : cinq listes et onze entrées. La [grille de fidélité](https://github.com/GautierDorval/interpretive-governance-test-suite/blob/cf61a18ab86d547443d6c0962d4c20ad9ed796f1/scoring-models/fidelity-score.md) décrit des critères de lecture. L’existence de ces ressources doit être distinguée du résultat d’une évaluation particulière.

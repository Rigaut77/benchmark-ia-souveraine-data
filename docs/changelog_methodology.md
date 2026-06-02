# Historique des évolutions méthodologiques

---

## v1.0 — Mai 2026 (version initiale)

### Périmètre
- 11 configurations évaluées
- 15 critères IRN (référentiel aDRI)
- 4 benchmarks performance : Arena Elo (35%), Coding (35%), MMLU-Pro (20%), AAII (10%)
- 4 profils de pondération

### Choix méthodologiques structurants
- **Pas d'agrégation coût/score** : le coût d'exploitation est maintenu comme axe séparé, jamais agrégé dans le score fusionné. Raison : additionner des euros et des critères de souveraineté produirait des comparaisons trompeuses.
- **Normalisation par leader** : les scores performance sont normalisés par le meilleur score public connu au moment de l'évaluation, pas par une valeur fixe. Cela rend le benchmark relatif plutôt qu'absolu.
- **TCO paramétrable** : les hypothèses de coût GPU sont modifiables par l'utilisateur sur le site pour refléter son contexte réel.
- **Exclusion de 5 critères IRN contextuels** : les critères dépendant du contexte organisationnel (accords bilatéraux, portabilité données spécifiques, etc.) sont exclus du calcul automatisé.

### Configurations exclues (et pourquoi)
- Modèles sans API publique stable au moment de l'évaluation
- Modèles sans documentation tarifaire publique
- Configurations dont les sources IRN étaient insuffisamment documentées

---

## À venir — v1.1 (roadmap)

### Changements méthodologiques prévus
- Ajout de tests qualitatifs métier public (français administratif, textes normatifs)
- Ajout d'une grille de conformité réglementaire (SecNumCloud, AI Act, RGPD)
- Ajout d'un axe environnemental (kgCO2/1M tokens estimé)
- Mise à jour semestrielle des scores de benchmarks

### Nouvelles configurations candidates
- Modèles souverains émergents (à qualifier selon disponibilité documentaire)
- Solutions OVHcloud AI Endpoints
- Scaleway Generative APIs

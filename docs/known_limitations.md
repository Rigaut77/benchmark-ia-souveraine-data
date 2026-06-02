# Limites connues du benchmark

---

## Ce que ce benchmark mesure

✅ Performance générique sur 4 benchmarks publics reconnus  
✅ Souveraineté numérique sur 15 critères observationnels publics (référentiel aDRI)  
✅ Coût d'infrastructure amorti (TCO self-hosted) ou prix public API  
✅ Score fusionné paramétrable selon 4 profils d'usage public

---

## Ce que ce benchmark ne mesure PAS

### Tests métier secteur public (prévu v1.1)
- ❌ Qualité des réponses en **français administratif** (décrets, circulaires, formulaires)
- ❌ **Hallucinations sur textes normatifs** (Code général des collectivités, RGPD, AI Act)
- ❌ **Résistance aux instructions malveillantes** (red-teaming, adversarial prompting)
- ❌ **Citation de sources** sur corpus juridique interne
- ❌ Performance sur **formats spécifiques** (CERFA, marchés publics, délibérations)

### Conformité réglementaire (prévu v1.1)
- ❌ Qualification **SecNumCloud** (ANSSI)
- ❌ Homologation **RGS** et analyse **PGSSI-S**
- ❌ Évaluation **AI Act** article par article
- ❌ Analyse **RGPD** sur les traitements de données personnelles

### Autres dimensions non couvertes
- ❌ **Impact environnemental** (kgCO2/1M tokens estimé)
- ❌ **Latence et temps de réponse** dans des conditions réseau réelles en France
- ❌ **Stabilité des APIs** sur la durée (uptime, SLA)
- ❌ **Qualité du support** et réactivité fournisseur
- ❌ **Conditions contractuelles** (réversibilité, pénalités, durée d'engagement)

---

## Incertitudes connues

| Dimension | Incertitude estimée | Cause |
|-----------|---------------------|-------|
| Scores IRN | ±0,15 point | Critères observationnels — mise à jour CGU/datacenter possible |
| Scores Performance | ±0,10 point | Snapshots Arena hebdomadaires — classement évolue |
| Coûts self-hosted | ±20-30% | Prix GPU spot variables, overhead estimé |
| Coûts API | Source officielle | Peuvent changer sans préavis |

---

## Déclaration de biais potentiels

- **Biais de sélection :** 11 configurations sélectionnées par Theodo GovTech. D'autres configurations pertinentes existent (ex. modèles souverains émergents, solutions OVHcloud AI, etc.).
- **Biais de pondération IRN :** Les poids par défaut sont ceux du référentiel aDRI public. Des choix de pondération différents (ex. surpondérer la juridiction pour un OIV) donneraient des classements différents.
- **Biais de benchmarks génériques :** Arena Elo et MMLU-Pro sont construits sur des préférences anglophones. Les scores peuvent sous-estimer des modèles optimisés pour le français.
- **Conflit d'intérêts déclaré :** Theodo GovTech intervient sur des projets impliquant Albert API (Mistral Medium) et Mistral — voir README.md pour la déclaration complète.

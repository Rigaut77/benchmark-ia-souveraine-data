# Changelog

Toutes les modifications notables de ce projet sont documentées ici.  
Format : [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/)  
Versionnage : [Semantic Versioning](https://semver.org/lang/fr/)

---

## [1.0.0] — Mai 2026

### Ajouté
- **11 configurations LLM** évaluées : DeepSeek V3.2 API, Mistral Medium API, Mistral Large 2 self-hosted, Mistral Small self-hosted, Claude Opus 4.6, GPT-5.4-high EU, Gemini 3.1 Pro EU, Qwen3.5-Max FRA, Llama 4 Maverick self-hosted, Llama 4 Behemoth self-hosted, Aleph PhariaAI
- **15 critères IRN** basés sur le référentiel aDRI (Juridiction, Opération critique, Continuité, Interop & portabilité, Réversibilité & confiance)
- **4 benchmarks performance** : Arena Elo (35%), Coding composite (35%), MMLU-Pro (20%), AAII (10%)
- **4 profils de pondération** : R&D / Expérimentation, Productivité & usage interne, Données sensibles / secteur régulé, Régalien / défense
- Hypothèses TCO paramétrables : H100 $3/h, overhead ×1.40, utilisation 60%
- Script `extract_data.py` pour régénérer le JSON depuis le fichier Excel source
- Documentation complète : METHODOLOGY.md, sources/, docs/

### Périmètre
- Date de collecte des données : mai 2026
- Snapshots de benchmarks publics à date (Arena Elo, MMLU-Pro, Coding, AAII)
- Prix API et GPU au moment de l'évaluation (pages publiques fournisseurs)

---

## À venir — v1.1 (roadmap)

- [ ] Tests qualitatifs métier public : français administratif, corpus juridique, hallucinations sur textes normatifs
- [ ] Grille de conformité réglementaire : RGPD, AI Act, SecNumCloud, RGS
- [ ] Axe environnemental : kgCO2/1M tokens estimé
- [ ] Scénarios de déploiement type (collectivité 5000 agents, ministère 50k agents)
- [ ] Mise à jour semestrielle des scores (octobre 2026)

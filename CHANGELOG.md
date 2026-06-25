# Changelog

Toutes les modifications notables de ce projet sont documentées ici.  
Format : [Keep a Changelog](https://keepachangelog.com/fr/1.0.0/)  
Versionnage : [Semantic Versioning](https://semver.org/lang/fr/)

---

## [2.1.0] — 25 juin 2026

### Ajouté
- **Configuration C15 — Anthropic Claude Fable 5** (API directe, frontier US public). Sortie le 09/06/2026, nouveau **#1 de l'Artificial Analysis Intelligence Index** et leader coding (95,0 % SWE-bench Verified, 80,3 % SWE-bench Pro, #1 FrontierCode). Panel porté à **15 configurations**.

### Mis à jour (fin juin 2026)
- **Leaders de normalisation perf relevés** suite à l'arrivée de Fable 5 : Arena 1552, Coding 1580, MMLU-Pro 91, AAII 78 (la perf normalisée des autres configs baisse mécaniquement).
- **Mistral Medium 3.5** : devient le modèle par défaut de Le Chat et remplace Devstral 2 dans Mistral Vibe ; coding/AAII légèrement réévalués (SWE-bench Verified 77,6 %).

### Note de souveraineté
- **Cas d'école extraterritorialité/continuité** : Fable 5 (et Mythos 5) ont été **suspendus le 12/06/2026 pour les ressortissants étrangers** sous l'effet d'une directive US d'export-control, l'accès ne pouvant être filtré par nationalité en temps réel. Cela matérialise concrètement les critères IRN C03 (maîtrise des lois extraterritoriales) et C07 (continuité face à l'arrêt fournisseur), notés au plus bas pour cette configuration.

---

## [2.0.0] — Juin 2026

### Changé (refonte majeure)
- **Profils repensés selon 7 types d'applications** (matrice criticité × mode de déploiement), remplaçant les 4 profils génériques : A1 Classifiées défense/renseignement, A2 Régaliennes, A3 OIV/SIIV, A4 Données massives sensibles, A5 Infrastructures de confiance État, A6 Entités importantes NIS 2 non régaliennes, A7 Collectivités/code non sensible. Pondération IRN/Perf graduée par criticité (A1 : 90/10 → A7 : 25/75).
- **Matrice de décision 7×3** (type d'application × {SaaS public / SaaS souverain SecNumCloud / auto-hébergé contrôlé}) avec recommandations explicites (À proscrire, Par défaut, Recommandé, Préféré, Analyse de risque, Si homologué DR, Hors briques crypto, Contrôles forts, Acceptable).
- Les 4 profils historiques **P1–P4 restent présents** dans le JSON (rétro-compatibilité du site v1).

### Ajouté
- **3 nouvelles configurations souveraines** : Albert API (Etalab/DINUM, SecNumCloud), Mistral Devstral 2 self-hosted, Qwen3.6-27B Coder on-prem. Panel porté à **14 configurations**.
- **Pipeline déterministe unique** : `data/_source_data.json` (entrées brutes éditables) + `scripts/generate_benchmark.py` (calcule IRN pondéré, perf normalisée, TCO, scores fusionnés et émet `benchmark.json` + le `.xlsx`).
- Champ `deploy` par configuration (rattachement à une colonne de la matrice).

### Mis à jour (juin 2026)
- Montées de version : Claude Opus 4.8, GPT-5.5-high, Gemini 3.5 Pro, Mistral Medium 3.5, **Mistral Large 3** (open-weight Apache 2.0, MoE 675B/41B), DeepSeek V4, Qwen3.7-Max, Mistral Small 4.
- Leaders de normalisation et prix/débits rafraîchis.

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

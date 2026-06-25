# Benchmark IA Souveraine — Données & Méthodologie

[![Version](https://img.shields.io/badge/version-2.0-blue)](CHANGELOG.md)
[![Licence](https://img.shields.io/badge/licence-CC%20BY--NC%204.0-green)](LICENSE)
[![Juin 2026](https://img.shields.io/badge/mise%20à%20jour-juin%202026-orange)]()

Données brutes et méthodologie complète du **Benchmark IA Souveraine** — 14 configurations LLM évaluées sur Performance, Souveraineté (IRN) et Coût d'exploitation, lues à travers **7 profils d'application** (de la défense classifiée aux collectivités) et une **matrice de décision criticité × mode de déploiement**.

## Régénérer les données (v2.0)

La source de vérité est `data/_source_data.json` (entrées brutes). Le générateur calcule tous les scores dérivés et produit le JSON + le classeur :

```bash
pip install openpyxl
python scripts/generate_benchmark.py
# → data/benchmark.json + data/benchmark_llm_fusion_finale.xlsx
```

> `scripts/extract_data.py` (v1, XLSX→JSON) est conservé pour mémoire mais remplacé par `generate_benchmark.py`.

🌐 **Site interactif :** https://benchmark-llm-souv.vercel.app

---

## À propos

Cette étude est produite par **Theodo GovTech**, qui accompagne des directions du numérique du secteur public français sur l'adoption d'IA souveraine.

### Indépendance et déclaration d'intérêts

- **Aucun fournisseur du panel évalué n'a commandité cette étude.**
- **Aucun fournisseur n'a eu de droit de relecture sur les résultats.**
- Theodo GovTech intervient sur des projets impliquant certaines des configurations évaluées (notamment Albert API et Mistral) — ces relations professionnelles sont publiques.
- Pour signaler un conflit d'intérêts présumé ou une erreur factuelle : **https://github.com/Rigaut77/benchmark-ia-souveraine-data/issues/new

---

## Contenu du repo

```
benchmark-ia-souveraine-data/
├── README.md               Ce fichier
├── CHANGELOG.md            Historique des versions
├── LICENSE                 CC BY-NC 4.0
├── METHODOLOGY.md          Méthodologie complète (formules, sources, hypothèses)
├── data/
│   ├── benchmark.json      Source de vérité pour le site interactif
│   └── benchmark_v1.0.json Snapshot daté v1.0 (mai 2026)
├── scripts/
│   └── extract_data.py     Conversion XLSX → JSON
├── sources/
│   ├── irn_adri.md         Description du référentiel IRN aDRI
│   ├── performance_benchmarks.md  Sources Arena, MMLU-Pro, Coding, AAII
│   ├── cost_assumptions.md Hypothèses de coût GPU et API
│   └── per_config_sources.md  Sources fournisseur par configuration
└── docs/
    ├── how_to_reproduce.md Étapes pour reproduire les calculs
    ├── changelog_methodology.md  Historique des évolutions méthodologiques
    └── known_limitations.md  Limites assumées du benchmark
```

---

## Les données

### benchmark.json

Fichier JSON structuré contenant :
- **11 configurations** évaluées (LLM managés API + self-hosted EU)
- **15 critères IRN** (Indice de Résilience Numérique, référentiel aDRI)
- **4 benchmarks performance** : Arena Elo, Coding, MMLU-Pro, AAII
- **Hypothèses TCO** pour les configurations self-hosted
- **4 profils de pondération** : R&D/Expérimentation, Productivité & usage interne, Données sensibles / secteur régulé, Régalien / défense

### Comment reproduire

```bash
# Cloner le repo
git clone https://github.com/Rigaut77/benchmark-ia-souveraine-data.git
cd benchmark-ia-souveraine-data

# Installer les dépendances
pip install pandas openpyxl

# Régénérer le JSON depuis le fichier Excel source
python scripts/extract_data.py

# Le fichier data/benchmark.json est mis à jour
```

---

## Limites assumées

Ce benchmark fournit un cadre de comparaison technique et économique. **Il ne se substitue pas à :**

- Une analyse juridique (RGPD, AI Act, droit administratif)
- Une qualification de sécurité (SecNumCloud, homologation RGS, PGSSI-S)
- Une évaluation DPO sur les traitements de données personnelles
- Une étude de marché public et de réversibilité contractuelle
- Des tests métier sur cas d'usage spécifiques (français administratif, corpus juridique)
- Une analyse d'impact environnemental complète

---

## Licence

Les données et la méthodologie sont publiées sous **[CC BY-NC 4.0](LICENSE)**.

Toute réutilisation à des fins non commerciales est autorisée avec citation :

> Theodo GovTech, *Benchmark IA Souveraine v1.0*, mai 2026.  
> https://benchmark-llm-souv.vercel.app · https://github.com/Rigaut77/benchmark-ia-souveraine-data

---

## Citation

```
@misc{theodo2026benchmark,
  title   = {Benchmark IA Souveraine v1.0},
  author  = {Theodo GovTech},
  year    = {2026},
  month   = {mai},
  url     = {https://benchmark-llm-souv.vercel.app},
  note    = {11 configurations LLM évaluées sur Performance, IRN et Coût}
}
```

---

## Contact

- **Signaler une erreur ou un conflit d'intérêts :** [Ouvrir une issue GitHub](https://github.com/Rigaut77/benchmark-ia-souveraine-data/issues/new)
- **Site Theodo GovTech :** https://www.theodo.com/secteur/secteur-public

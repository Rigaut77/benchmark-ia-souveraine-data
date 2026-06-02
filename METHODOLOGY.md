# Méthodologie — Benchmark IA Souveraine v1.0

**Date de collecte :** Mai 2026  
**Périmètre :** 11 configurations LLM × 15 critères IRN × 4 benchmarks performance

---

## 1. Architecture générale

Le benchmark évalue chaque configuration sur **trois axes indépendants** — jamais agrégés en un score unique :

| Axe | Description | Score |
|-----|-------------|-------|
| **IRN** | Souveraineté & résilience numérique | /5 |
| **Performance** | Composite multi-bench normalisé | /5 |
| **Exploitation** | Coût réel d'usage (API ou TCO self-hosted) | $/1M tokens |

Ces trois axes sont combinés via un **score fusionné paramétrable** selon 4 profils d'usage — mais l'axe coût reste toujours séparé (on n'additionne pas des euros et des principes).

---

## 2. Bloc 1 — Indice de Résilience Numérique (IRN)

### Référentiel

Basé sur le référentiel **aDRI** (Alliance pour la Résilience Numérique) — grille d'évaluation publique disponible sur [gitlab.com/digitalresilienceinitiative/adri-irn](https://gitlab.com/digitalresilienceinitiative/adri-irn).

### 15 critères (5 blocs thématiques)

| Bloc | Critères | Description |
|------|----------|-------------|
| **Juridiction** | C01, C02, C03 | Droit applicable, localisation des données, avantage structurel France/UE |
| **Opération critique** | C04, C05, C06 | Continuité opérationnelle, résistance aux injonctions extraterritoriales |
| **Continuité & supply chain** | C07, C08, C09 | Dépendances fournisseur, plan de continuité, réversibilité technique |
| **Interop & portabilité** | C10, C11 | Interopérabilité standards ouverts, portabilité des données et modèles |
| **Réversibilité & confiance** | C12, C13, C14, C15 | Auditabilité, transparence algorithmique, conditions contractuelles |

### Notation

- Chaque critère est noté de **1 à 5** sur grille observationnelle publique
- Pondération paramétrable par critère (défaut : poids égaux dans chaque bloc)
- 5 critères contextuels (accords bilatéraux, etc.) exclus du calcul automatisé

### Formule

```
IRN = Σ(score_i × poids_i) / Σ(poids_i)    pour i dans les 15 critères actifs
```

---

## 3. Bloc 2 — Score de Performance composite

### Sources et pondérations

| Benchmark | Poids | Source | Leader (mai 2026) |
|-----------|-------|--------|-------------------|
| **Arena Elo** | 35% | LMSYS Chatbot Arena (arena.lmsys.org) | GPT-5.4-high EU — 1505 |
| **Coding composite** | 35% | SWE-bench + HumanEval | Leader : 1545 |
| **MMLU-Pro** | 20% | arXiv + HuggingFace Leaderboard | Leader : 91 |
| **AAII** | 10% | Artificial Analysis (artificialanalysis.ai) | Leader : 76 |

### Normalisation

Chaque score est normalisé par le score du leader public au moment de l'évaluation (mai 2026), puis ramené à une échelle /5 :

```
Perf = (arena/1505 × 0.35 + coding/1545 × 0.35 + mmlu/91 × 0.20 + aaii/76 × 0.10) × 5
```

### Limites des benchmarks utilisés

- Les benchmarks sont **génériques** — ils ne testent pas les cas d'usage du secteur public (français administratif, corpus juridique, textes normatifs)
- L'Arena Elo est un classement par préférence humaine — il peut refléter des biais de présentation
- Les scores MMLU-Pro et Coding peuvent être influencés par la contamination du dataset d'entraînement
- Des tests métier spécifiques au secteur public sont prévus pour la **v1.1** (voir CHANGELOG.md)

---

## 4. Bloc 3 — Coût d'exploitation

### API managées

Prix listé par le fournisseur sur ses pages publiques tarifaires au moment de l'évaluation (mai 2026), en $/1M tokens (entrée + sortie moyennés selon mix typique 3:1).

### Configurations self-hosted — TCO calculé

```
TCO ($/1M tok) = (gpu_count × gpu_price_per_hour × overhead) / (throughput × 3600 × utilisation) × 1 000 000
```

**Hypothèses par défaut (paramétrables) :**

| Paramètre | Valeur défaut | Source |
|-----------|---------------|--------|
| Prix H100 SXM 80GB | $3,00 / heure | OVHcloud, Scaleway, Lambda Labs (moyenne mai 2026) |
| Prix A100 SXM 80GB | $1,50 / heure | Idem |
| Overhead opérationnel | ×1,40 | MCO + équipe infra estimés à 40% du coût GPU |
| Taux d'utilisation | 60% | Hypothèse conservative pour usage administrations |

**⚠ Attention :** Le $/1M tokens self-hosted **n'est pas un prix marginal**. C'est un coût d'infrastructure amorti. Pour une comparaison rigoureuse avec une API facturée par token, utiliser le seuil de break-even calculé dynamiquement sur le site.

---

## 5. Score fusionné par profil

Le score fusionné combine IRN et Performance avec des poids variables selon le profil. **Le coût reste toujours un axe séparé.**

```
Score_profil = w_IRN × IRN + w_Perf × Performance
```

| Profil | w_IRN | w_Perf | Usage type |
|--------|-------|--------|------------|
| **R&D / Expérimentation** | 20% | 80% | Laboratoires, exploration, POC |
| **Productivité & usage interne** | 35% | 65% | Assistants métier, rédaction, analyse |
| **Données sensibles / secteur régulé** | 55% | 45% | Santé, justice, RH sensibles, AI Act |
| **Régalien / défense** | 75% | 25% | Défense nationale, infrastructure vitale |

---

## 6. Configurations évaluées

| Configuration | Tier | Mode | Pays |
|---------------|------|------|------|
| DeepSeek V3.2 API | Frontier | Managé | Chine |
| Claude Opus 4.6 | Frontier | Managé | États-Unis |
| GPT-5.4-high EU | Frontier | Managé | États-Unis |
| Gemini 3.1 Pro EU | Frontier | Managé | États-Unis |
| Mistral Large 2 self-hosted | Frontier | Self-hosted | France |
| Llama 4 Behemoth self-hosted | Frontier | Self-hosted | États-Unis |
| Mistral Medium API | Mid | Managé | France |
| Qwen3.5-Max FRA | Mid | Self-hosted | Chine |
| Aleph PhariaAI | Mid | Self-hosted | Allemagne |
| Llama 4 Maverick self-hosted | Mid | Self-hosted | États-Unis |
| Mistral Small self-hosted | Entry | Self-hosted | France |

---

## 7. Incertitudes et sensibilité

- **Scores IRN :** basés sur des critères observationnels publics — une mise à jour fournisseur (changement de CGU, déménagement datacenter) peut modifier un score sans nouvelle version du benchmark
- **Scores performance :** les classements Arena évoluent hebdomadairement — les scores ici sont des snapshots mai 2026
- **Coûts self-hosted :** sensibles au taux d'utilisation (voir simulation D3 sur le site) et aux variations de prix GPU spot
- **Incertitude estimée :** ±0,15 point sur les scores IRN, ±0,10 point sur les scores performance

---

## 8. Ce que ce benchmark ne mesure pas

- Tests sur **cas d'usage métier public** (français administratif, textes normatifs, corpus juridique)
- **Qualité des réponses** sur documents spécifiques secteur public
- **Hallucinations** sur textes réglementaires
- **Résistance aux instructions malveillantes** (red-teaming)
- **Impact environnemental** (kgCO2/1M tokens)
- **Conformité réglementaire détaillée** (SecNumCloud, homologation RGS, PGSSI-S)

Ces axes sont prévus pour la **v1.1** — voir [CHANGELOG.md](CHANGELOG.md).

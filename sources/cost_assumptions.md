# Hypothèses de coût — TCO self-hosted et prix API

Date de collecte : mai 2026

---

## Prix GPU (self-hosted)

| GPU | Prix/heure | Source | Note |
|-----|-----------|--------|------|
| H100 SXM 80GB | $3,00 | OVHcloud, Scaleway, Lambda Labs (moyenne) | Prix spot mai 2026 |
| A100 SXM 80GB | $1,50 | Idem | Prix spot mai 2026 |

Sources :
- OVHcloud : https://www.ovhcloud.com/fr/public-cloud/gpu/
- Scaleway : https://www.scaleway.com/fr/gpu-h100/
- Lambda Labs : https://lambdalabs.com/service/gpu-cloud

## Overhead opérationnel (×1,40)

Le coefficient d'overhead de 1,40 couvre :
- MCO (Maintien en Condition Opérationnelle) : ~15%
- Équipe infra (DevOps, MLOps) : ~15%
- Réseau, stockage, monitoring : ~10%

Ce coefficient est paramétrable sur le site (plage : ×1,20 à ×2,00).

## Taux d'utilisation (60% par défaut)

Hypothèse conservative pour un déploiement en production dans une administration :
- 60% reflète un usage métier régulier (heures ouvrées + pic ponctuel)
- Une utilisation plus faible (<40%) augmente significativement le coût par token
- Au-delà de 80%, le self-hosted devient compétitif face aux API Frontier

Le taux d'utilisation est paramétrable sur le site (plage : 20% à 95%).

## Prix API managées (mai 2026)

| Configuration | Prix entrée | Prix sortie | Source |
|--------------|-------------|-------------|--------|
| DeepSeek V3.2 | $0,27/1M | $1,10/1M | api-docs.deepseek.com |
| Claude Opus 4.6 | $15/1M | $75/1M | anthropic.com/pricing |
| GPT-5.4-high EU | $10/1M | $30/1M | openai.com/pricing |
| Gemini 3.1 Pro EU | $3,50/1M | $10,50/1M | ai.google.dev/pricing |
| Mistral Medium API | $0,40/1M | $2,00/1M | mistral.ai/pricing |

*Prix moyennés selon un mix typique 3:1 (entrée:sortie)*

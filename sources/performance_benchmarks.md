# Sources — Benchmarks de performance

Date de snapshot : mai 2026

---

## Arena Elo (poids : 35%)

- **Source :** LMSYS Chatbot Arena — https://arena.lmsys.org
- **Description :** Classement par préférence humaine via matchs en aveugle entre modèles. Score Elo calculé sur des millions d'évaluations.
- **Leader mai 2026 :** GPT-5.4-high EU — score Elo 1505
- **Limites :** Biais anglophone, biais de présentation (ordre des réponses), peu représentatif du français administratif

## Coding benchmark composite (poids : 35%)

- **Source :** SWE-bench Verified + HumanEval composite
  - SWE-bench : https://www.swebench.com/
  - HumanEval : https://github.com/openai/human-eval
- **Description :** Capacité à résoudre des tâches de programmation réelles (SWE-bench) et à compléter des fonctions Python (HumanEval). Score composite normalisé.
- **Leader mai 2026 :** score composite 1545
- **Limites :** Centré sur le code Python/JavaScript, ne mesure pas la qualité rédactionnelle

## MMLU-Pro (poids : 20%)

- **Source :** arXiv 2406.01574 + HuggingFace Open LLM Leaderboard — https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard
- **Description :** Raisonnement multidisciplinaire sur 12 000 questions académiques (droit, médecine, sciences, mathématiques, etc.) avec options de réponse plus complexes que MMLU standard.
- **Leader mai 2026 :** 91,0 (score sur 100)
- **Limites :** Majoritairement en anglais, peut sous-estimer des modèles optimisés pour le français

## AAII — Artificial Analysis Intelligence Index (poids : 10%)

- **Source :** Artificial Analysis — https://artificialanalysis.ai/
- **Description :** Index composite mesurant les capacités générales d'intelligence des modèles (raisonnement, instruction-following, connaissances factuelles).
- **Leader mai 2026 :** 76 (score sur 100)
- **Limites :** Méthodologie propriétaire, mise à jour irrégulière

---

## Normalisation

Chaque score est normalisé par le score du leader au moment de l'évaluation (mai 2026), puis ramené à /5 :

```
score_normalisé = (score_modèle / score_leader) × 5
```

Le score composite final :

```
Perf = arena_norm × 0.35 + coding_norm × 0.35 + mmlu_norm × 0.20 + aaii_norm × 0.10
```

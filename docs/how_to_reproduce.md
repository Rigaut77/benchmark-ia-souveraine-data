# Comment reproduire les calculs

## Prérequis

- Python 3.9+
- Git

## Étapes

```bash
# 1. Cloner le repo
git clone https://github.com/Rigaut77/benchmark-ia-souveraine-data.git
cd benchmark-ia-souveraine-data

# 2. Installer les dépendances Python
pip install pandas openpyxl

# 3. Vérifier que le fichier Excel source est présent
ls data/benchmark_llm_fusion_finale.xlsx

# 4. Régénérer le JSON
python scripts/extract_data.py

# 5. Vérifier le résultat
python -c "import json; d=json.load(open('data/benchmark.json')); print(f'{len(d[\"configurations\"])} configs, {len(d[\"irn_criteria\"])} critères IRN')"

# 6. (Optionnel) Générer avec un fichier source alternatif
python scripts/extract_data.py --input mon_fichier.xlsx --output data/mon_benchmark.json
```

## Structure du benchmark.json

```json
{
  "meta": { "version": "1.0", "date": "2026-05", ... },
  "configurations": [
    {
      "id": "C10", "name": "Mistral Large 2 self-hosted EU",
      "tier": "Frontier", "country": "France", "mode_expl": "self_hosted",
      "irn": 4.64, "perf": 4.55, "cost": 97.0,
      "P1": 4.57, "P2": 4.60, "P3": 4.62, "P4": 4.63,
      "scores_irn": [5, 5, 5, 4, 5, ...]
    },
    ...
  ],
  "irn_criteria": [
    { "id": "C01", "label": "Juridiction", "weight": 3, "bloc": "juridiction" },
    ...
  ],
  "hypotheses_tco": {
    "h100_per_hour": 3.0, "a100_per_hour": 1.5,
    "overhead": 1.4, "utilisation": 0.6
  }
}
```

## Modifier les hypothèses TCO

Pour recalculer avec des hypothèses différentes (ex. H100 à $2/h, utilisation 80%) :

1. Modifier la feuille `hypotheses_tco` dans le fichier Excel
2. Relancer `python scripts/extract_data.py`

Ou directement éditer `data/benchmark.json` dans la clé `hypotheses_tco`.

## Vérification des scores

Les formules complètes sont documentées dans [METHODOLOGY.md](../METHODOLOGY.md).
Pour tout écart constaté : https://github.com/Rigaut77/benchmark-ia-souveraine-data/issues/new

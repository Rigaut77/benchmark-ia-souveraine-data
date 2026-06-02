"""
extract_data.py — Conversion XLSX → JSON pour le Benchmark IA Souveraine

Usage :
    python scripts/extract_data.py
    python scripts/extract_data.py --input data/benchmark_llm_fusion_finale.xlsx --output data/benchmark.json

Dépendances :
    pip install pandas openpyxl

Ce script lit le fichier Excel source et génère le fichier benchmark.json
utilisé par le site interactif (https://benchmark-llm-souv.vercel.app).
"""

import json
import argparse
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    raise SystemExit("❌ pandas requis : pip install pandas openpyxl")


DEFAULT_INPUT  = Path(__file__).parent.parent / "data" / "benchmark_llm_fusion_finale.xlsx"
DEFAULT_OUTPUT = Path(__file__).parent.parent / "data" / "benchmark.json"


def load_existing_json(path: Path) -> dict:
    """Charge le JSON existant pour conserver les métadonnées."""
    if path.exists():
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    return {}


def excel_to_json(input_path: Path, output_path: Path) -> None:
    print(f"📂 Lecture de : {input_path}")

    # Chargement de la feuille principale
    try:
        df = pd.read_excel(input_path, sheet_name="configurations")
    except Exception as e:
        raise SystemExit(f"❌ Impossible de lire la feuille 'configurations' : {e}")

    print(f"   {len(df)} configurations trouvées")

    # Construction des objets configuration
    configurations = []
    for _, row in df.iterrows():
        config = {
            "id":          str(row.get("id", "")),
            "name":        str(row.get("name", "")),
            "short":       str(row.get("short", "")),
            "tier":        str(row.get("tier", "")),
            "country":     str(row.get("country", "")),
            "mode_expl":   str(row.get("mode_expl", "")),
            "irn":         float(row["irn"])         if pd.notna(row.get("irn"))         else None,
            "perf":        float(row["perf"])        if pd.notna(row.get("perf"))        else None,
            "cost":        float(row["cost"])        if pd.notna(row.get("cost"))        else None,
            "throughput":  int(row["throughput"])    if pd.notna(row.get("throughput"))  else None,
            "P1":          float(row["P1"])           if pd.notna(row.get("P1"))           else None,
            "P2":          float(row["P2"])           if pd.notna(row.get("P2"))           else None,
            "P3":          float(row["P3"])           if pd.notna(row.get("P3"))           else None,
            "P4":          float(row["P4"])           if pd.notna(row.get("P4"))           else None,
        }

        # Scores IRN détaillés (C01 à C15) si présents
        scores_irn = []
        for i in range(1, 16):
            col = f"C{i:02d}"
            if col in row and pd.notna(row[col]):
                scores_irn.append(float(row[col]))
        if scores_irn:
            config["scores_irn"] = scores_irn

        configurations.append(config)

    # Chargement de la feuille critères IRN
    irn_criteria = []
    try:
        df_irn = pd.read_excel(input_path, sheet_name="irn_criteria")
        for _, row in df_irn.iterrows():
            irn_criteria.append({
                "id":     str(row.get("id", "")),
                "label":  str(row.get("label", "")),
                "weight": int(row["weight"]) if pd.notna(row.get("weight")) else 1,
                "bloc":   str(row.get("bloc", "")),
            })
    except Exception:
        print("   ⚠ Feuille 'irn_criteria' non trouvée — critères IRN non inclus")

    # Chargement des hypothèses TCO
    hypotheses_tco = {
        "h100_per_hour": 3.0,
        "a100_per_hour": 1.5,
        "overhead": 1.4,
        "utilisation": 0.6,
    }
    try:
        df_hyp = pd.read_excel(input_path, sheet_name="hypotheses_tco", index_col=0)
        for key in hypotheses_tco:
            if key in df_hyp.index:
                hypotheses_tco[key] = float(df_hyp.loc[key, "value"])
    except Exception:
        print("   ⚠ Feuille 'hypotheses_tco' non trouvée — hypothèses par défaut utilisées")

    # Assemblage final
    result = {
        "meta": {
            "version": "1.0",
            "date": "2026-05",
            "source": "Theodo GovTech — https://github.com/Rigaut77/benchmark-ia-souveraine-data",
            "licence": "CC BY-NC 4.0",
        },
        "configurations": configurations,
        "irn_criteria":   irn_criteria,
        "hypotheses_tco": hypotheses_tco,
    }

    # Écriture
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✅ JSON généré : {output_path}")
    print(f"   {len(configurations)} configurations · {len(irn_criteria)} critères IRN")


def main():
    parser = argparse.ArgumentParser(description="Convertit le fichier Excel source en benchmark.json")
    parser.add_argument("--input",  default=DEFAULT_INPUT,  type=Path, help="Fichier Excel source")
    parser.add_argument("--output", default=DEFAULT_OUTPUT, type=Path, help="Fichier JSON de sortie")
    args = parser.parse_args()

    if not args.input.exists():
        raise SystemExit(f"❌ Fichier source introuvable : {args.input}")

    excel_to_json(args.input, args.output)


if __name__ == "__main__":
    main()

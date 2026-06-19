#!/usr/bin/env python3
"""Build a simple repo hygiene manifest from exported repository rows.

Input CSV columns: repo,visibility,default_branch,has_readme,has_security,has_contributing,has_ci,has_pages
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

WEIGHTS = {
    "has_readme": 20,
    "has_security": 20,
    "has_contributing": 10,
    "has_ci": 20,
    "has_pages": 15,
}


def truthy(value: str) -> bool:
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate a GitHub repo hygiene manifest from CSV.")
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--out", type=Path, default=Path("repo-hygiene-manifest.json"))
    args = parser.parse_args()

    rows = []
    with args.csv_path.open("r", encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            score = 15 if row.get("default_branch") else 0
            score += sum(weight for key, weight in WEIGHTS.items() if truthy(row.get(key, "")))
            rows.append({
                "repo": row.get("repo"),
                "visibility": row.get("visibility"),
                "score": min(score, 100),
                "nextActions": [key for key in WEIGHTS if not truthy(row.get(key, ""))]
            })
    args.out.write_text(json.dumps({"repositories": rows}, indent=2), encoding="utf-8")
    print(f"wrote {args.out}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
import argparse
import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INDEX = ROOT / "memory" / "catalog-index.json"

STOPWORDS = {
    "a", "an", "the", "to", "for", "of", "in", "on", "at", "by", "with", "and", "or",
    "de", "da", "do", "das", "dos", "para", "com", "sem", "em", "no", "na", "e", "ou", "o", "os", "a", "as",
    "skill", "mcp"
}

SYNONYMS = {
    "security": {"security", "seguranca", "review", "revisao", "auditoria"},
    "docs": {"docs", "documentacao", "readme", "manual"},
    "api": {"api", "backend", "endpoint"},
    "python": {"python", "fastapi"},
}


def normalize(text: str):
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")


def tokenize(text: str):
    text = normalize(text.lower())
    raw = re.findall(r"[a-zA-Z0-9][a-zA-Z0-9-+._/]*", text)
    return [tok for tok in raw if tok not in STOPWORDS and len(tok) > 1]


def expand_terms(tokens):
    expanded = set(tokens)
    token_set = set(tokens)
    for group in SYNONYMS.values():
        if token_set & group:
            expanded |= group
    return sorted(expanded)


def load_index():
    if not INDEX.exists():
        raise SystemExit(f"index not found: {INDEX}. Run tools/build-index.py first.")
    return json.loads(INDEX.read_text(encoding="utf-8"))


def score(task_terms, row):
    text = f"{row['name']} {row['description']}".lower()
    points = 0.0
    overlap = []
    for term in sorted(set(task_terms)):
        if term in text:
            points += 2.0
            overlap.append(term)
    if row["type"] == "skill":
        points += 0.5
    return points, overlap


def main():
    parser = argparse.ArgumentParser(description="Route a task through the PICR catalog")
    parser.add_argument("task")
    parser.add_argument("--top", type=int, default=8)
    args = parser.parse_args()

    task_terms = expand_terms(tokenize(args.task))
    rows = []
    for row in load_index():
        points, overlap = score(task_terms, row)
        if points > 0:
            rows.append((points, overlap, row))
    rows.sort(key=lambda item: item[0], reverse=True)

    print(f"Task: {args.task}")
    print("Top matches:")
    for idx, (points, overlap, row) in enumerate(rows[:args.top], start=1):
        print(f"{idx:02d}. {row['name']} | type={row['type']} | score={points:.1f} | overlap={','.join(overlap) or '-'}")
        print(f"    {row['path']}")


if __name__ == "__main__":
    main()

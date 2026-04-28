#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUTPUT = ROOT / "memory" / "catalog-index.json"


def parse_skill(skill_md: Path):
    text = skill_md.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    name = skill_md.parent.name
    desc = ""
    if lines and lines[0].strip() == "---":
        for line in lines[1:80]:
            s = line.strip()
            if s == "---":
                break
            if s.startswith("name:"):
                name = s.split(":", 1)[1].strip().strip("\"'")
            elif s.startswith("description:"):
                desc = s.split(":", 1)[1].strip().strip("\"'")
    return {"name": name, "description": desc, "path": str(skill_md.relative_to(ROOT)), "type": "skill"}


def parse_mcp(mcp_md: Path):
    return {"name": mcp_md.parent.name, "description": "MCP entry", "path": str(mcp_md.relative_to(ROOT)), "type": "mcp"}


def main():
    rows = []
    for skill_md in sorted((ROOT / "skills").glob("*/SKILL.md")):
        if skill_md.parent.name.startswith("_"):
            continue
        rows.append(parse_skill(skill_md))
    for mcp_md in sorted((ROOT / "mcps").glob("*/MCP.md")):
        if mcp_md.parent.name.startswith("_"):
            continue
        rows.append(parse_mcp(mcp_md))
    OUTPUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"indexed={len(rows)} output={OUTPUT}")


if __name__ == "__main__":
    main()

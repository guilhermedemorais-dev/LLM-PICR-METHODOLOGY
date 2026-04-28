#!/usr/bin/env python3
import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VAULT_TEMPLATE = ROOT / "obsidian" / "vault-template"


def parse_frontmatter(path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    lines = text.splitlines()
    data = {
        "name": path.parent.name,
        "description": "",
        "categories": [],
        "related_skills": [],
        "requires_mcp": [],
        "tags": [],
    }
    if not lines or lines[0].strip() != "---":
        return data

    current_list = None
    for line in lines[1:160]:
        raw = line.rstrip()
        stripped = raw.strip()
        if stripped == "---":
            break
        if not stripped:
            continue
        if stripped.startswith("- ") and current_list:
            data[current_list].append(stripped[2:].strip())
            continue
        current_list = None
        if ":" not in stripped:
            continue
        key, value = stripped.split(":", 1)
        key = key.strip()
        value = value.strip().strip("\"'")
        if key in {"categories", "related_skills", "requires_mcp", "tags"}:
            current_list = key
            if value.startswith("[") and value.endswith("]"):
                items = [item.strip().strip("\"'") for item in value[1:-1].split(",") if item.strip()]
                data[key].extend(items)
                current_list = None
        elif key in data:
            data[key] = value
    return data


def ensure_dir(path: Path):
    path.mkdir(parents=True, exist_ok=True)


def copy_template(vault: Path):
    for src in VAULT_TEMPLATE.rglob("*"):
        rel = src.relative_to(VAULT_TEMPLATE)
        dest = vault / rel
        if src.is_dir():
            ensure_dir(dest)
        else:
            ensure_dir(dest.parent)
            if not dest.exists():
                shutil.copy2(src, dest)


def write_text(path: Path, content: str):
    ensure_dir(path.parent)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def build_home_note():
    return """# PICR Home

## Catalogs

- [[catalogs/primary|Primary Catalog]]
- [[catalogs/programming|Programming]]
- [[catalogs/security|Security]]
- [[catalogs/docs|Docs]]
- [[catalogs/design|Design]]
- [[catalogs/agents|Agents]]
- [[catalogs/mcps|MCPs]]

## Skills

Browse the `skills/` folder for operational notes generated from the repository.

## MCPs

Browse the `mcps/` folder for integration notes.

## Memory

Use `memory/` to record successful routes and lessons learned.

## Projects

Use `projects/` for project-specific overlays.
"""


def build_skill_note(meta, known_skills, known_mcps):
    categories = ", ".join(meta["categories"]) or "-"
    related_skill_names = [name for name in meta["related_skills"] if name in known_skills]
    related_mcp_names = [name for name in meta["requires_mcp"] if name in known_mcps]
    related_skills = "\n".join(f"- [[{name}]]" for name in related_skill_names) or "-"
    related_mcps = "\n".join(f"- [[{name}]]" for name in related_mcp_names) or "-"
    description = meta["description"] or "-"
    tags = ", ".join(meta["tags"]) or "-"
    return f"""# {meta['name']}

## Type

Skill

## Description

{description}

## Categories

{categories}

## Tags

{tags}

## Related Skills

{related_skills}

## Related MCPs

{related_mcps}
"""


def build_mcp_note(name: str, path: Path):
    text = path.read_text(encoding="utf-8", errors="ignore")
    body = text.strip()
    return f"""# {name}

## Type

MCP

## Source

`{path.relative_to(ROOT)}`

## Definition

{body}
"""


def export_catalogs(vault: Path):
    target = vault / "catalogs"
    ensure_dir(target)
    for src in (ROOT / "catalogs").glob("*.md"):
        shutil.copy2(src, target / src.name)


def export_skills(vault: Path):
    target = vault / "skills"
    ensure_dir(target)
    skill_files = [path for path in (ROOT / "skills").glob("*/SKILL.md") if not path.parent.name.startswith("_")]
    known_skills = {parse_frontmatter(path)["name"] for path in skill_files}
    known_mcps = {path.parent.name for path in (ROOT / "mcps").glob("*/MCP.md") if not path.parent.name.startswith("_")}
    for skill_md in skill_files:
        if skill_md.parent.name.startswith("_"):
            continue
        meta = parse_frontmatter(skill_md)
        write_text(target / f"{meta['name']}.md", build_skill_note(meta, known_skills, known_mcps))


def export_mcps(vault: Path):
    target = vault / "mcps"
    ensure_dir(target)
    for mcp_md in (ROOT / "mcps").glob("*/MCP.md"):
        if mcp_md.parent.name.startswith("_"):
            continue
        name = mcp_md.parent.name
        write_text(target / f"{name}.md", build_mcp_note(name, mcp_md))


def export_projects(vault: Path):
    ensure_dir(vault / "projects")
    template = ROOT / "projects" / "_template" / "PROJECT-CONTEXT.md"
    shutil.copy2(template, vault / "projects" / "PROJECT-CONTEXT.md")


def export_memory(vault: Path):
    write_text(
        vault / "memory" / "README.md",
        """# Memory

Use this folder to capture:

- route logs
- winning skill combinations
- MCP decisions
- web research decisions
- project-specific lessons
""",
    )


def main():
    parser = argparse.ArgumentParser(description="Export PICR repository content into an Obsidian vault")
    parser.add_argument("vault_path", help="Path to the target Obsidian vault")
    args = parser.parse_args()

    vault = Path(args.vault_path).expanduser().resolve()
    ensure_dir(vault)
    copy_template(vault)
    export_catalogs(vault)
    export_skills(vault)
    export_mcps(vault)
    export_projects(vault)
    export_memory(vault)
    write_text(vault / "PICR Home.md", build_home_note())

    print(f"vault={vault}")
    print("exported=catalogs,skills,mcps,projects,memory")
    print('next=open the vault in Obsidian and start from "PICR Home.md"')


if __name__ == "__main__":
    main()

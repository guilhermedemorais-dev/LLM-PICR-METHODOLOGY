# LLM-PICR-METHODOLOGY

`PICR` means `Progressive Indexed Context Retrieval`.

This repository proposes a portable methodology for making LLMs and local AI CLIs reason with lower token cost and higher precision by using:

- a short primary catalog
- domain catalogs
- a router
- on-demand reading
- memory of successful routes

## Core Idea

Do not load the whole manual before proving it is needed.

A good agent should:

1. classify the task
2. consult a short index
3. narrow to the right domain catalog
4. read only the selected skill or MCP
5. execute
6. record what worked

## Repository Structure

- `methodology/`: PICR and orchestrator documents
- `catalogs/`: primary and domain catalogs
- `skills/`: reusable skill definitions
- `mcps/`: MCP catalog and templates
- `retrieval/`: ingestion patterns such as Firecrawl
- `memory/`: routing log schemas and examples
- `obsidian/`: optional vault and note templates
- `tools/`: local index and routing helpers

## Initial Components

- PICR methodology
- PICR orchestrator
- primary catalog
- domain catalogs for programming, security, docs, design, agents, and MCPs
- skill template
- MCP template
- Firecrawl retrieval note
- Obsidian integration notes
- project context template
- example Obsidian vault template

## Simple Installation

If the user only has the repository URL and a local shell, the fastest setup is:

```bash
git clone https://github.com/guilhermedemorais-dev/LLM-PICR-METHODOLOGY.git
cd LLM-PICR-METHODOLOGY
python3 tools/build-index.py
```

Or with the bootstrap script:

```bash
bash tools/install-picr.sh https://github.com/guilhermedemorais-dev/LLM-PICR-METHODOLOGY.git
```

After installation, a local CLI or agent can route tasks with:

```bash
python3 tools/route.py "I need a skill for Python API security review"
```

See [install.md](./install.md) for the agent-friendly installation flow.

## Obsidian Integration

PICR can be used with Obsidian as a human-readable external brain.

Official Obsidian links:

- Download: https://obsidian.md/download
- Help: https://help.obsidian.md/
- Install guide: https://help.obsidian.md/install
- CLI guide: https://help.obsidian.md/cli

See:

- [obsidian/README.md](./obsidian/README.md)
- [obsidian/SETUP.md](./obsidian/SETUP.md)
- [catalogs/BUILD-YOUR-CATALOG.md](./catalogs/BUILD-YOUR-CATALOG.md)
- [projects/_template/PROJECT-CONTEXT.md](./projects/_template/PROJECT-CONTEXT.md)

## Design Goal

Replace maximum context with correct context.

## License

MIT

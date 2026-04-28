# PICR Installation

This file is meant to be simple enough for both humans and local AI CLIs.

## Goal

Install the PICR repository locally from a repository URL and prepare the routing index.

## Fast Path

If you already know the repository URL:

```bash
git clone https://github.com/guilhermedemorais-dev/LLM-PICR-METHODOLOGY.git
cd LLM-PICR-METHODOLOGY
python3 tools/build-index.py
```

## One-Command Bootstrap

If the repository already contains the bootstrap script:

```bash
bash tools/install-picr.sh https://github.com/guilhermedemorais-dev/LLM-PICR-METHODOLOGY.git
```

## What the Installer Should Do

1. clone the repository
2. enter the repository directory
3. build the local catalog index
4. print the next command to test routing

## Validation

After installation, validate with:

```bash
python3 tools/route.py "I need a skill for Python API documentation and security review"
```

## CLI Integration Pattern

Any local AI CLI can use this repository if it can:

1. access local files
2. run a shell command
3. read `README.md`, `install.md`, and the `catalogs/` directory
4. call `tools/route.py` before opening detailed skill files

## Recommended Behavior For AI CLIs

When given only the repository URL, the CLI should:

1. clone the repository
2. run `python3 tools/build-index.py`
3. route the user task through `tools/route.py`
4. read only the selected skill or MCP

## Notes

- `build-index.py` is local and cheap to run
- `route.py` is the first routing step, not the final executor
- CLIs should avoid loading all skills into context at once

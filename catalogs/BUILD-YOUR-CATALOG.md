# Build Your Own Catalog

This guide shows how a user can build a PICR catalog from their own work context.

## Goal

Transform real work patterns into a small, useful catalog instead of dumping random prompts into one folder.

## Core Rule

Do not start by writing dozens of skills.

Start by mapping repeated work.

## Step 1: Identify Your Work Domains

List the domains you actually use every week.

Examples:

- programming
- backend
- frontend
- security
- docs
- design
- automation
- sales ops
- research

Do not copy someone else's categories if they do not match your work.

## Step 2: List Repeated Tasks

For each domain, write the tasks that happen repeatedly.

Examples:

- fix Python API bugs
- review security risks before merge
- write or update README files
- turn vendor docs into internal notes
- design reusable UI components

These repeated tasks are the raw material for your catalog.

## Step 3: Separate Task Types

For each repeated task, decide whether it is mainly:

- a `skill`
- an `MCP`
- a `reference`
- a `memory pattern`

Use this rule:

- `skill` = reusable instruction workflow
- `MCP` = repeated structured interaction with an external system
- `reference` = source material that changes or must be cited
- `memory pattern` = lessons from previous successful routes

## Step 4: Create A Small Primary Catalog

Your primary catalog should stay short.

Good examples:

- programming
- security
- docs
- design
- agents
- mcps

Bad examples:

- 25 top-level categories with only one item each

## Step 5: Create Domain Catalogs

Inside each domain, link only the items that matter.

Example for programming:

- Python API skill
- debugging skill
- testing skill
- database design skill

The goal is not completeness.
The goal is fast routing.

## Step 6: Create Skills From Stable Workflows

Create a new skill only if:

- the task repeats
- the workflow is stable
- a written procedure will save time later

Do not create a skill for every one-off problem.

## Step 7: Create MCP Entries For Repeated External Operations

Create an MCP entry when the work repeatedly depends on:

- GitHub
- Firecrawl
- Obsidian
- docs retrieval
- automation platforms

The MCP note should say:

- what it connects to
- why it exists
- when to use it
- auth requirements
- related skills

## Step 8: Add Real Context From Your Work

This is the most important step.

Your catalog gets valuable when it reflects:

- your stack
- your products
- your constraints
- your naming conventions
- your decision patterns

Examples:

- if you mostly work with FastAPI, make that explicit
- if your team uses Obsidian heavily, connect project notes to skills
- if your work depends on official docs, note which references are authoritative

## Step 9: Record What Worked

Every time a route works well, record:

- task summary
- chosen skill
- chosen MCP
- whether web research was needed
- whether the route should be promoted

This turns the catalog into a learning system.

## Step 10: Refine Monthly

Review the catalog periodically:

- promote high-value entries
- archive dead entries
- merge duplicates
- tighten vague skills
- separate unstable references from stable workflows

## Suggested Starter Structure

```text
catalogs/
  primary.md
  programming.md
  security.md
  docs.md
skills/
  python-api-skill/
  security-review-skill/
  readme-skill/
mcps/
  firecrawl-mcp/
  obsidian-mcp/
memory/
  routing-log.schema.json
projects/
  my-project-a.md
  my-project-b.md
```

## Best Practice

The catalog should describe how you actually work, not how you wish you worked.

## Next Step

After building the first version of your catalog:

1. run the router
2. use the catalog on real tasks
3. update it from real friction, not theory

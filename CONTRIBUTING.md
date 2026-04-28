# Contributing

## Goal

This repository is a shared operational knowledge base for PICR.

Contributions should improve one of these areas:

- methodology
- catalogs
- skills
- MCPs
- retrieval patterns
- routing memory
- Obsidian integration

## Contribution Rules

1. Keep entries narrow and reusable.
2. Do not add giant generic prompts without boundaries.
3. Every skill must declare when to use and when not to use.
4. Every MCP entry must describe auth, exposed tools, and limits.
5. Prefer updating an existing entry before creating duplicates.
6. If a topic depends on fast-changing external documentation, state that clearly.

## Required Metadata

Every skill should include:

- `name`
- `description`
- `categories`
- `tags`
- `requires_tools`
- `requires_mcp`
- `cost_hint`
- `risk_level`
- `use_when`
- `avoid_when`
- `related_skills`
- `source`

Every MCP should include:

- `name`
- `purpose`
- `tools exposed`
- `authentication`
- `use when`
- `avoid when`
- `related skills`

## Catalog Discipline

- `primary.md` should stay short
- domain catalogs should remain focused
- if an item is rarely used, keep it in a secondary catalog
- promote entries to `primary` only when repeated usage justifies it

## Recommended Flow

1. Add or update a skill or MCP.
2. Update the right catalog.
3. Add metadata.
4. If relevant, add an Obsidian note template or example.
5. If the route changes decision quality, document the reason.

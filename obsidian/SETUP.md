# Obsidian Setup For PICR

This guide uses official Obsidian resources and a minimal PICR workflow.

## Official References

- Download Obsidian: https://obsidian.md/download
- Obsidian Help: https://help.obsidian.md/
- Install guide: https://help.obsidian.md/install
- Settings: https://help.obsidian.md/settings
- CLI guide: https://help.obsidian.md/cli
- Sync overview: https://help.obsidian.md/Getting%20started/Sync%20your%20notes%20across%20devices

## Goal

Turn an Obsidian vault into a human-readable layer for:

- skills
- MCPs
- catalogs
- routing memory
- project-specific knowledge

## Simple Setup

1. Install Obsidian from the official download page.
2. Open Obsidian.
3. Create a new vault or open an existing vault for PICR.
4. Inside the vault, create folders such as:
   - `catalogs`
   - `skills`
   - `mcps`
   - `memory`
   - `projects`
5. Copy or mirror useful PICR notes into that vault.

## Recommended Settings

In Obsidian Settings, configure:

1. `Files and links`
   - enable automatic update of internal links
   - use Wikilinks if you want fast graph navigation
2. `Core plugins`
   - enable Backlinks
   - enable Outgoing links
   - enable Graph view
   - enable Templates
3. `Appearance`
   - choose a readable theme before adding visual complexity

## Optional CLI Setup

If you want terminal integration, see the official CLI guide:

- https://help.obsidian.md/cli

The official docs note that Obsidian CLI requires a recent installer/version path. Check the current requirements in the CLI guide before depending on it.

## Optional Sync

If you want the vault on more than one device, review the official sync overview:

- https://help.obsidian.md/Getting%20started/Sync%20your%20notes%20across%20devices

Important:

- avoid mixing multiple sync systems for the same vault without understanding the risk of conflicts

## How PICR Fits Into The Vault

Suggested mapping:

- `catalogs/` -> hub notes by domain
- `skills/` -> one note per skill
- `mcps/` -> one note per MCP
- `memory/` -> route history and lessons learned
- `projects/` -> project-specific overlays

## Linking Pattern

Each note should link to related notes:

- a skill links to related MCPs
- an MCP links to related skills
- a project note links to the catalogs it uses most
- a memory note links to the route that succeeded

## Minimum Useful Vault

If the user wants the smallest viable setup:

1. one `primary` catalog note
2. one `programming` catalog note
3. one `security` catalog note
4. one `docs` catalog note
5. one `skills` folder
6. one `memory` folder

## Next Step

After Obsidian is set up, follow:

- [../catalogs/BUILD-YOUR-CATALOG.md](../catalogs/BUILD-YOUR-CATALOG.md)

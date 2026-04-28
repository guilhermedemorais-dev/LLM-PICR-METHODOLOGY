# Obsidian Integration

Obsidian can serve as the human-facing layer of PICR.

Official links:

- Download: https://obsidian.md/download
- Help: https://help.obsidian.md/
- Install guide: https://help.obsidian.md/install
- CLI guide: https://help.obsidian.md/cli
- Sync guide: https://help.obsidian.md/Getting%20started/Sync%20your%20notes%20across%20devices

## Suggested Note Types

- skill notes
- MCP notes
- catalog hubs
- playbooks
- routing memory

## Benefits

- backlinks
- graph navigation
- collaborative curation
- portable external brain

## Local Bootstrap

To create a vault from the repository content:

```bash
bash tools/setup-obsidian-vault.sh ~/Obsidian/PICR
```

To refresh vault notes later:

```bash
python3 tools/export-obsidian.py ~/Obsidian/PICR
```

See also:

- [SETUP.md](./SETUP.md)
- [../catalogs/BUILD-YOUR-CATALOG.md](../catalogs/BUILD-YOUR-CATALOG.md)

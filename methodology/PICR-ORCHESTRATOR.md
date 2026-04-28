# PICR Orchestrator

The orchestrator is the decision layer above PICR.

It decides:

1. which catalog to consult
2. whether an existing skill is enough
3. whether an MCP is needed
4. whether web research is required
5. whether a new skill or MCP should be created
6. what to record as memory

## Decision Order

1. memory
2. primary catalog
3. domain catalog
4. existing skill
5. existing MCP
6. external references

## Output Contract

- `task_summary`
- `domain`
- `primary_candidate`
- `support_candidates`
- `need_web_research`
- `need_skill_creation`
- `need_mcp_creation`
- `confidence`
- `reason`

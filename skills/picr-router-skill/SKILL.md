---
name: picr-router-skill
description: Route a task to the smallest useful skill or MCP set using PICR catalogs, confidence gates, and on-demand reading.
categories:
  - agents
tags:
  - router
  - orchestration
  - picr
requires_tools: []
requires_mcp: []
cost_hint: low
risk_level: safe
use_when:
  - The user asks which skill or MCP should be used for a task.
  - The task is ambiguous and needs catalog-based triage first.
avoid_when:
  - The task is already clearly mapped to a known skill.
related_skills:
  - memory-routing-skill
  - mcp-builder-skill
source: local
---

# PICR Router Skill

## Goal

Choose the smallest useful set of skills or MCPs before loading detailed instructions.

## Workflow

1. Summarize the task in one sentence.
2. Check the primary catalog.
3. Narrow to one or two domain catalogs.
4. Rank the best candidates.
5. Read only the winning entry.
6. Record the route if it worked.

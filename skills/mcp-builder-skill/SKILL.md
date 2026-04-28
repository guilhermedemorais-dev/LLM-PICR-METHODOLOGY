---
name: mcp-builder-skill
description: Decide whether a task needs an MCP and define a small, maintainable MCP surface instead of an oversized integration.
categories:
  - agents
  - mcps
tags:
  - mcp
  - integration
  - builder
requires_tools: []
requires_mcp: []
cost_hint: medium
risk_level: medium
use_when:
  - Repeated structured access to an external system is needed.
  - Manual steps are becoming operational bottlenecks.
avoid_when:
  - The use case is one-off or weakly defined.
related_skills:
  - picr-router-skill
source: local
---

# MCP Builder Skill

## Goal

Create the smallest useful MCP boundary that solves a repeated integration problem.

## Workflow

1. Identify repeated external actions.
2. Define the minimum tool surface.
3. Define auth and safety constraints.
4. Avoid speculative overbuilding.

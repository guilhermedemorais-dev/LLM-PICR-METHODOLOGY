---
name: python-api-skill
description: Build or modify Python APIs with a bias toward small, testable changes, clear contracts, and explicit validation.
categories:
  - programming
tags:
  - python
  - api
  - backend
requires_tools: []
requires_mcp: []
cost_hint: medium
risk_level: medium
use_when:
  - The task involves Python backend routes, services, handlers, or validation.
  - The user needs API behavior changes or endpoint implementation.
avoid_when:
  - The task is frontend-only.
  - The problem requires live vendor documentation first.
related_skills:
  - debugging-skill
  - api-docs-skill
source: local
---

# Python API Skill

## Goal

Implement or change Python API behavior with low ambiguity and good validation discipline.

## Workflow

1. Identify the API boundary.
2. Confirm input, output, and failure conditions.
3. Change the smallest possible unit.
4. Validate behavior with tests or targeted checks.
5. Update docs if the contract changed.

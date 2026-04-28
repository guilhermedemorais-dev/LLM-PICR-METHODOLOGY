---
name: security-review-skill
description: Review code or workflows for common appsec issues with emphasis on auth, validation, data exposure, and dangerous defaults.
categories:
  - security
tags:
  - review
  - appsec
  - auth
requires_tools: []
requires_mcp: []
cost_hint: medium
risk_level: high
use_when:
  - The user asks for a security review.
  - A new feature touches auth, input validation, file access, or data handling.
avoid_when:
  - The user only wants stylistic feedback.
related_skills:
  - web-pentest-skill
source: local
---

# Security Review Skill

## Goal

Find security risks before implementation is treated as ready.

## Workflow

1. Map inputs, trust boundaries, and outputs.
2. Check auth and authorization assumptions.
3. Check input validation and error handling.
4. Check data exposure and secrets handling.
5. Report findings by severity.

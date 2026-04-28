---
name: readme-skill
description: Create or improve README files so users can understand setup, usage, structure, and operational constraints quickly.
categories:
  - docs
tags:
  - readme
  - docs
requires_tools: []
requires_mcp: []
cost_hint: low
risk_level: safe
use_when:
  - The repository lacks a usable README.
  - A feature changed installation, usage, or architecture.
avoid_when:
  - The task requires formal API reference generation instead.
related_skills:
  - api-docs-skill
source: local
---

# README Skill

## Goal

Produce short, useful, operational repository documentation.

## Workflow

1. Identify audience.
2. Capture install and usage.
3. Explain structure and constraints.
4. Remove low-signal filler.

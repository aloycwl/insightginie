---
layout: post
title: "Understanding the Review Orchestrator Skill: Multi-Perspective Code Review System"
date: 2026-03-09T08:17:17
categories: [24854]
original_url: https://insightginie.com/understanding-the-review-orchestrator-skill-multi-perspective-code-review-system
---

What This Solves
----------------

One perspective has blind spots. This skill coordinates multiple review perspectives to catch what single-pass review misses:

* Twin review – technical and creative perspectives for balance
* Cognitive modes – analyzer (“what conflicts”), architect (“how to restructure”), implementer (“how to implement”)

The insight: N=2 catches more than N=1. Different perspectives see different things. Coordinate them systematically.

Core Logic
----------

The Review Orchestrator uses intelligent selection based on context and risk level:

| Context | Risk | Recommended Review |
| --- | --- | --- |
| Implementation | Low | /ro twin –technical-only |
| Implementation | Medium | /ro twin (both perspectives) |
| Implementation | High | /ro twin + /ro cognitive |
| Architecture | Any | /ro cognitive |
| Documentation | Any | /ro twin –creative-only |
| Security | Any | /ro cognitive + external review |

Multi-Perspective Review
------------------------

The system provides different analytical perspectives:

### Technical Perspective

* Focus: Architecture, standards, patterns, security
* Japanese: 技術

### Creative Perspective

* Focus: UX, communication, philosophy alignment
* Japanese: 創造

### Cognitive Modes

These provide different analytical approaches:

| Mode | Perspective | Focus | Japanese |
| --- | --- | --- | --- |
| analyzer | “Here's what conflicts” | Tensions, trade-offs, contradictions | 審碼 |
| architect | “Here's how to restructure” | Architecture, patterns, organization | 審構 |
| implementer | “Here's how to implement” | Concrete steps, complexity, path forward | 審實 |

Quality Gate Configuration
--------------------------

The system includes configurable quality gates with these checks:

* Tests pass (critical)
* Coverage maintained (important)
* No critical findings (critical)
* Docs updated (minor)

Installation
------------

```
openclaw install leegitw/review-orchestrator
# With dependencies
openclaw install leegitw/context-verifier
openclaw install leegitw/failure-memory
openclaw install leegitw/review-orchestrator
```

Usage Examples
--------------

```
/ro select --context "Refactoring authentication handler" --risk high
/ro twin src/handlers/auth.go
/ro cognitive src/handlers/auth.go --modes analyzer,architect
/ro gate --stage 2 --strict
```

Output Format
-------------

Review results are written to docs/reviews/ in your workspace, with findings categorized by severity (critical, important, minor) and tagged for easy filtering.

Configuration
-------------

Configuration is loaded from (in order of precedence):

1. .openclaw/review-orchestrator.yaml (OpenClaw standard)
2. .claude/review-orchestrator.yaml (Claude Code compatibility)
3. Defaults (built-in)

This skill operates within your agent's trust boundary, using your configured model for review orchestration without external API calls.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/leegitw/review-orchestrator/SKILL.md>
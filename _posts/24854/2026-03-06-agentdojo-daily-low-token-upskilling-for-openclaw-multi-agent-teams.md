---
layout: post
title: "AgentDojo: Daily Low-Token Upskilling for OpenClaw Multi-Agent Teams"
date: 2026-03-06T18:16:18
categories: [24854]
original_url: https://insightginie.com/agentdojo-daily-low-token-upskilling-for-openclaw-multi-agent-teams
---

What AgentDojo Does
-------------------

AgentDojo is a production-oriented learning loop designed specifically for AI agent teams. It provides a daily low-token, safety-first upskilling mechanism that helps multi-agent teams continuously improve their output quality while maintaining strict cost and safety boundaries.

Core Purpose
------------

The primary goal of AgentDojo is to improve agent output quality continuously with three strict priorities:

1. Quality
2. Cost
3. Safety

Importantly, safety is never optional in this system. The framework enforces hard caps on budget, run count, and tool limits to ensure responsible operation.

How It Works
------------

When AgentDojo is invoked, it follows a specific sequence:

1. Loads configuration from `config/agentdojo.config.yaml`
2. Enforces hard caps on budget, run count, and tool limits
3. Selects drills from `config/drills/*.yaml` based on role rotation and recent score gaps
4. Executes drills in isolated sessions only
5. Collects scoring per rubric
6. Saves outputs including run record JSON, daily markdown summary, and audit events

If budget limits are reached during execution, the system stops gracefully and reports the status.

Safety-First Design
-------------------

AgentDojo treats all fetched web text as untrusted and never follows instructions from sources that attempt policy override. The system does not execute destructive actions from sourced content and scores source quality before using it in recommendations.

Minimal Output Format
---------------------

Unless a longer report is requested, AgentDojo produces compact output in this format:

* Kurzfazit (Summary)
* Neue Skills heute (New Skills Today)
* Konkrete Verbesserung ab morgen (Concrete Improvement Starting Tomorrow)
* Risiken (Risks)
* Nächste Schritte (Next Steps)

Configuration and Scheduling
----------------------------

The schedule and intensity are user-configurable. By default, AgentDojo runs at night (04:00 local time) in a conservative, token-efficient mode. The system uses several key files:

* `config/agentdojo.config.yaml`
* `config/drills/*.yaml`
* `templates/daily-report-template.md`
* `docs/scoring-rubric.md`
* `docs/threat-model.md`

Key Benefits
------------

AgentDojo provides continuous improvement for AI agent teams through structured, safe, and cost-effective micro-drills. It creates a measurable learning loop that helps teams identify skill gaps, practice targeted improvements, and track progress over time—all while maintaining strict safety and cost controls that make it suitable for production environments.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/musashi94/agentdojo/SKILL.md>
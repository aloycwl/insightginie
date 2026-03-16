---
layout: post
title: "Persistent Memory System for OpenClaw: Three-Layer Agent Recall"
date: 2026-03-13T19:15:43
categories: [24854]
original_url: https://insightginie.com/persistent-memory-system-for-openclaw-three-layer-agent-recall
---

What This Skill Does
--------------------

The persistent-memory skill adds a three-layer memory system to any OpenClaw workspace, giving agents the ability to remember decisions, facts, lessons, and institutional knowledge across sessions. Unlike OpenClaw’s built-in memory that resets between runs, this system provides semantic recall that survives restarts.

Three-Layer Architecture
------------------------

The system combines three complementary technologies:

* **L1: Markdown** – Human-readable curated knowledge in MEMORY.md, daily logs, and reference files
* **L2: Vector** – ChromaDB with all-MiniLM-L6-v2 embeddings for semantic search
* **L3: Graph** – NetworkX knowledge graph for relationship traversal

All three layers sync automatically. When you edit memory files, the indexer updates vector embeddings and the knowledge graph simultaneously.

Critical OpenClaw Integration
-----------------------------

By default, OpenClaw only indexes MEMORY.md and memory/\*.md files, ignoring critical workspace files like SOUL.md (agent directives) and AGENTS.md (behavior rules). This means agents can violate explicit instructions simply because they can’t find them.

The skill includes configure\_openclaw.py that adds a memorySearch configuration block to OpenClaw, indexing all critical workspace files. This makes directive compliance automatic rather than optional.

Setup
-----

One command from workspace root:

```
bash skills/persistent-memory/scripts/unified_setup.sh
```

This automatically creates the three-layer memory system, installs Python dependencies, configures OpenClaw memorySearch integration, indexes existing MEMORY.md, and sets up daily maintenance automation.

Daily Usage
-----------

**Writing Memories:** Update MEMORY.md after significant events, create daily logs in memory/YYYY-MM-DD.md, and add institutional facts to reference/\*.md files.

**Indexing:** After editing any memory file, run vector\_memory/venv/bin/python vector\_memory/indexer.py to keep layers in sync.

**Searching:** Use vector\_memory/venv/bin/python vector\_memory/search.py “your query” for semantic search across all memories.

**Sync Status:** Check memory health with vector\_memory/venv/bin/python vector\_memory/auto\_retrieve.py –status.

Agent Behavior Rules
--------------------

Add these to AGENTS.md or SOUL.md:

```
Before answering questions about prior work, decisions, dates, people, or preferences — search memory first.
Before executing any action that references an external identifier — query reference/ files first.
After editing memory files — re-index immediately.
```

Reference Directory
-------------------

Create reference/ in workspace root for institutional knowledge:

```
reference/
├── people.md          # Contacts, roles, communication details
├── repos.md           # GitHub repositories, URLs, status
├── infrastructure.md  # Hosts, IPs, ports, services
├── business.md        # Company info, strategies, rules
└── properties.md      # Domain-specific entities
```

These files are vector-indexed alongside MEMORY.md. The agent queries them before any action involving external identifiers.

Benefits
--------

* Agents remember across sessions
* Semantic search finds related concepts
* Knowledge graph reveals relationships
* Automatic directive compliance
* Institutional knowledge accumulates over time

Troubleshooting
---------------

Common issues include missing modules (run setup again), OUT\_OF\_SYNC status (run indexer), empty search results (ensure content exists), and agents ignoring directives (check OpenClaw integration).

This skill transforms OpenClaw from a stateless agent into one with persistent, semantic memory that grows and learns over time.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/jakebot-ops/persistent-memory/SKILL.md>
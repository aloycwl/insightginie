---
layout: post
title: "OpenClaw Skill: Nate Jones Second Brain &#8211; Context Architecture for Personal Knowledge Management"
date: 2026-03-10T15:17:29
categories: [24854]
original_url: https://insightginie.com/openclaw-skill-nate-jones-second-brain-context-architecture-for-personal-knowledge-management
---

Introduction: Context as the New Intelligence
---------------------------------------------

When intelligence is abundant, context becomes the scarce resource. This skill is context architecture — a persistent, searchable knowledge layer that turns your agent into a personal knowledge manager.

The Nate Jones Second Brain skill establishes the foundation layer for a personal knowledge system. It's built on two opinionated primitives: Supabase for persistent context architecture, and OpenRouter as the AI gateway. Together, they create a system where your context persists while models come and go.

Core Architecture
-----------------

The skill operates on five structured tables — thoughts (inbox log), people, projects, ideas, and admin — with AI-powered classification, confidence-based routing, and semantic search across all categories.

### Two Opinionated Primitives

* **Supabase** — Your database, and so much more. PostgreSQL + pgvector. Stores thoughts, people, projects, ideas, and tasks as structured data with vector embeddings. REST API built in. Your data, your infrastructure.
* **OpenRouter** — Your AI gateway. One API key, every model. Embeddings and LLM calls for classification and routing. Swap models by changing a string. Future-proof by design.

Building Blocks
---------------

These are the operational concepts behind the system. Understanding them helps you operate correctly.

### Drop Box

One frictionless capture point. Everything goes to `thoughts` first.

### Sorter

AI classification + routing. LLM classifies type, then routes to structured table.

### Form

Consistent data contracts. Each table has a defined schema.

### Filing Cabinet

Source of truth per category. `people`, `projects`, `ideas`, `admin` tables.

### Bouncer

Confidence threshold. Confidence < 0.6 = don't route, stay in inbox.

### Receipt

Audit trail. `thoughts` row logs what came in, where it went.

### Tap on the Shoulder

Proactive surfacing. Daily digest queries (application layer).

### Fix Button

Agent-mediated corrections. Move records between tables on user request.

Five Tables
-----------

Table | Role | Key Fields

— | — | —

`thoughts` | Inbox Log / audit trail | content, embedding, metadata (type, topics, people, confidence, routed\_to)

`people` | Relationship tracking | name (unique), context, follow\_ups, tags, embedding

`projects` | Work tracking | name, status, next\_action, notes, tags, embedding

`ideas` | Insight capture | title, summary, elaboration, topics, embedding

`admin` | Task management | name, due\_date, status, notes, embedding

Every table has semantic search via its own `match_*` function. Cross-table search via `search_all`.

Routing Rules
-------------

When a thought is classified:

Type | Route | Action

— | — | —

`person_note` | `people` | Upsert: create person or append to existing context

`task` | `admin` | Insert new task (status=pending)

`idea` | `ideas` | Insert new idea

`observation` | none | Stays in thoughts only

`reference` | none | Stays in thoughts only

If confidence < 0.6, don't route. Leave in thoughts, tell user.

Quick Start
-----------

### Capture a Thought (Full Pipeline)

The complete ingestion process involves four steps:

1. **Embed** the text via OpenRouter (1536-dim vector)
2. **Classify** via OpenRouter LLM (type, topics, people, confidence, suggested route)
3. **Log** in `thoughts` (the Receipt — always)
4. **Route** based on classification (if confidence >= 0.6)

### Semantic Search (Single Table)

Query thoughts with semantic search:

```
QUERY_EMBEDDING=$(curl -s -X POST "https://openrouter.ai/api/v1/embeddings" \
  -H "Authorization: Bearer $OPENROUTER_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "openai/text-embedding-3-small", "input": "career changes"}' \
  | jq -c '.data[0].embedding')

curl -s -X POST "$SUPABASE_URL/rest/v1/rpc/match_thoughts" \
  -H "apikey: $SUPABASE_SERVICE_ROLE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_ROLE_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"query_embedding\": $QUERY_EMBEDDING,
    \"match_threshold\": 0.5,
    \"match_count\": 10,
    \"filter\": {}
  }"
```

### Cross-Table Search

Search across all tables:

```
curl -s -X POST "$SUPABASE_URL/rest/v1/rpc/search_all" \
  -H "apikey: $SUPABASE_SERVICE_ROLE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_ROLE_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"query_embedding\": $QUERY_EMBEDDING,
    \"match_threshold\": 0.5,
    \"match_count\": 20
  }"
```

Returns `table_name`, `record_id`, `label`, `detail`, `similarity`, `created_at` from all tables.

### List Active Projects

```
curl -s "$SUPABASE_URL/rest/v1/projects?status=eq.active&select=name,next_action,notesℴ=updated_at.desc" \
  -H "apikey: $SUPABASE_SERVICE_ROLE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_ROLE_KEY"
```

### List Pending Tasks

```
curl -s "$SUPABASE_URL/rest/v1/admin?status=eq.pending&select=name,due_date,notesℴ=due_date.asc" \
  -H "apikey: $SUPABASE_SERVICE_ROLE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_ROLE_KEY"
```

Environment Variables
---------------------

The skill requires these environment variables:

* `SUPABASE_URL` – Your Supabase project URL
* `SUPABASE_SERVICE_ROLE_KEY` – Your Supabase service role key
* `OPENROUTER_API_KEY` – Your OpenRouter API key

Implementation Details
----------------------

The skill is designed as a foundation layer. It covers the context architecture — how to capture, classify, store, and retrieve information. The application layer (how you use this information) is up to you.

The system uses a confidence-based routing approach. When the LLM classifies a thought, it returns a confidence score. If the confidence is below 0.6, the system doesn't route the thought to a structured table. Instead, it stays in the `thoughts` inbox with a note that classification was uncertain. This prevents the system from making incorrect categorizations.

The semantic search uses pgvector embeddings. Each table has a `match_*` function that performs similarity search within that table. The `search_all` function performs cross-table search, returning results from all tables with their similarity scores.

Conceptual Framework
--------------------

The full conceptual framework is available in the references documentation. The system is designed around the principle that context is the scarce resource when intelligence is abundant. By creating a persistent, searchable knowledge layer, the skill turns your agent into a personal knowledge manager that can retrieve relevant information at the right time.

Getting Started
---------------

To set up the tables, see the setup documentation. The skill provides a complete foundation for personal knowledge management, but you'll need to create the database tables first. Once the tables exist, you can start capturing thoughts and building your knowledge system.

The skill is opinionated by design. It chooses specific tools (Supabase and OpenRouter) and specific approaches (confidence-based routing, semantic search) to create a working system. If you want to use different tools or approaches, you can modify the skill, but the provided version gives you a complete, working foundation.

Conclusion
----------

The Nate Jones Second Brain skill is context architecture for the AI age. It provides a persistent, searchable knowledge layer that turns your agent into a personal knowledge manager. By using Supabase for data persistence and OpenRouter for AI operations, it creates a system where your context persists while models come and go.

The skill covers the foundation — how to capture, classify, store, and retrieve information. The application layer — how you use this information to be more productive, creative, or informed — is up to you. But with this foundation in place, you have unlimited possibilities for building on top of your personal knowledge system.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/justfinethanku/nate-jones-second-brain/SKILL.md>
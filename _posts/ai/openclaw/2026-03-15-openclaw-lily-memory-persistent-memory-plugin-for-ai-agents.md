---
layout: post
title: "OpenClaw Lily Memory: Persistent Memory Plugin for AI Agents"
date: 2026-03-15T23:16:09
categories: [24854]
original_url: https://insightginie.com/openclaw-lily-memory-persistent-memory-plugin-for-ai-agents
---

OpenClaw Lily Memory is a persistent memory plugin designed to give OpenClaw agents long-term memory capabilities that survive session resets, compaction, and restarts. This powerful plugin combines SQLite FTS5 keyword search with Ollama vector semantic search to create a comprehensive memory system for AI agents.

What Lily Memory Does
---------------------

Lily Memory provides several key features that enhance the memory capabilities of OpenClaw agents:

### Auto-Recall

The plugin automatically injects relevant memories as context before each LLM turn. This means your agent can reference past conversations and information without explicit prompting, creating a more coherent and contextually aware interaction experience.

### Auto-Capture

Lily Memory automatically extracts facts from conversations and stores them for future use. This passive learning capability ensures that valuable information shared during interactions is preserved and can be referenced later.

### Hybrid Search

The plugin uses a sophisticated hybrid search approach that combines SQLite FTS5 keyword search with Ollama vector cosine similarity. This dual approach ensures both precise keyword matching and semantic understanding of context.

### Stuck Detection

Lily Memory includes intelligent stuck detection that identifies topic repetition and nudges the agent to break out of conversational loops. This helps maintain productive and engaging interactions.

### Memory Consolidation

The plugin automatically deduplicates memory entries on startup, ensuring your agent's memory remains clean and efficient without redundant information.

### Dynamic Entities

Lily Memory supports config-driven allowlists and runtime tools to add entities, providing flexibility in what types of information are captured and stored.

### Graceful Degradation

The plugin works without Ollama by falling back to keyword-only mode, ensuring functionality even if vector search capabilities aren't available.

### Minimal Dependencies

Lily Memory uses better-sqlite3 for secure parameterized queries and native fetch, keeping the plugin lightweight and secure.

Requirements
------------

To use Lily Memory, you'll need:

* Node.js 18+ (for native fetch support)
* The better-sqlite3 npm package
* Optional: Ollama with nomic-embed-text model for semantic search

Quick Start
-----------

Getting started with Lily Memory is straightforward:

1. Install the plugin to your extensions directory
2. Add the following configuration to your openclaw.json:

```
{
  "plugins": {
    "slots": {
      "memory": "lily-memory"
    },
    "entries": {
      "lily-memory": {
        "enabled": true,
        "config": {
          "dbPath": "~/.openclaw/memory/decisions.db",
          "entities": ["config", "system"]
        }
      }
    }
  }
}
```

3. Restart the gateway with: openclaw gateway restart

Available Tools
---------------

Lily Memory provides several tools for interacting with the memory system:

* **memory\_search**: FTS5 keyword search across all facts
* **memory\_entity**: Look up all facts for a specific entity
* **memory\_store**: Save a fact to persistent memory
* **memory\_semantic\_search**: Vector similarity search via Ollama
* **memory\_add\_entity**: Register a new entity at runtime

Configuration Options
---------------------

Lily Memory offers extensive configuration options:

| Option | Type | Default | Description |
| --- | --- | --- | --- |
| dbPath | string | ~/.openclaw/memory/decisions.db | SQLite database path |
| autoRecall | boolean | true | Inject memories before each turn |
| autoCapture | boolean | true | Extract facts from responses |
| maxRecallResults | number | 10 | Max memories per turn |
| maxCapturePerTurn | number | 5 | Max facts per response |
| stuckDetection | boolean | true | Topic repetition detection |
| vectorSearch | boolean | true | Ollama semantic search |
| ollamaUrl | string | http://localhost:11434 | Ollama endpoint |
| embeddingModel | string | nomic-embed-text | Embedding model |
| consolidation | boolean | true | Dedup on startup |
| vectorSimilarityThreshold | number | 0.5 | Min cosine similarity |
| entities | array | [] | Additional entity names |

Architecture
------------

Lily Memory uses a sophisticated architecture to manage memory effectively:

### Recall Flow

The recall process extracts keywords from messages, performs both FTS5 and vector searches, merges and deduplicates results, then injects the relevant memories as context for the next LLM turn.

### Capture Flow

When capturing information, Lily Memory uses regex scanning to identify patterns like “entity: key = value”, validates entities against the allowlist, stores facts to SQLite, and asynchronously embeds them via Ollama for semantic search capabilities.

### Stuck Detection

The stuck detection mechanism tracks the top 5 content words per response, calculates Jaccard similarity, and if 3+ consecutive responses have greater than 60% overlap, it injects a Reflexion nudge to help break out of repetitive patterns.

License
-------

Lily Memory is available under the MIT license, making it freely available for use and modification in both personal and commercial projects.

Conclusion
----------

OpenClaw Lily Memory represents a significant advancement in AI agent memory capabilities. By combining traditional keyword search with modern vector semantic search, it provides a robust and flexible memory system that enhances the intelligence and contextual awareness of OpenClaw agents. Whether you're building a simple chatbot or a complex AI assistant, Lily Memory provides the persistent memory foundation needed for truly intelligent interactions.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/kevinodell/lily-memory/SKILL.md>
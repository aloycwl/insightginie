---
layout: post
title: 'OpenClaw Lily Memory Plugin: Persistent Memory for AI Agents'
date: '2026-03-17T03:15:31+00:00'
categories:
- ai
- openclaw
original_url: https://insightginie.com/openclaw-lily-memory-plugin-persistent-memory-for-ai-agents/
featured_image: /media/images/8150.jpg
---

<p>The Lily Memory plugin is a persistent memory solution for OpenClaw agents that enables long-term memory retention across sessions. This plugin provides agents with the ability to remember past interactions, automatically recall relevant information, and maintain context over extended conversations.</p>
<h2>How Lily Memory Works</h2>
<p>The plugin operates through several key mechanisms. Auto-recall injects relevant memories as context before each LLM turn, ensuring the agent has access to pertinent information from previous interactions. Auto-capture extracts facts from conversations and stores them automatically, building a knowledge base over time.</p>
<p>The system uses hybrid search combining SQLite FTS5 keyword search with Ollama vector cosine similarity for semantic matching. This dual approach ensures both precise keyword matching and contextual understanding. The plugin also includes stuck detection to identify when conversations are looping and memory consolidation to deduplicate entries on startup.</p>
<h2>Key Features</h2>
<p>The plugin offers zero npm dependencies, using only sqlite3 CLI and native fetch. It includes dynamic entities with config-driven allowlists and runtime tools to add new entities. The system gracefully degrades to keyword-only mode when Ollama is unavailable.</p>
<p>Auto-recall functionality extracts keywords from messages, performs FTS5 and vector searches, merges results, and injects memories as context. Auto-capture uses regex scanning to identify entity patterns, validates against allowlists, stores facts to SQLite, and asynchronously embeds them via Ollama.</p>
<h2>Configuration Options</h2>
<p>Users can configure various parameters including database path, auto-recall and auto-capture toggles, maximum recall results, stuck detection settings, and vector search options. The plugin supports custom entities and allows configuration of the Ollama endpoint and embedding model.</p>
<h2>Technical Architecture</h2>
<p>The recall flow extracts keywords, performs dual searches, merges and deduplicates results, then injects context. The capture flow identifies patterns, validates entities, stores facts, and creates embeddings. Stuck detection tracks content words, calculates Jaccard similarity, and triggers Reflexion nudges when repetition is detected.</p>
<h2>Installation and Setup</h2>
<p>Installation requires adding the plugin to the extensions directory and configuring it in the openclaw.json file. The system needs Node.js 18+ for native fetch, SQLite 3.33+ with FTS5 support, and optionally Ollama with the nomic-embed-text model for semantic search capabilities.</p>
<h2>Available Tools</h2>
<p>The plugin provides several tools including memory_search for FTS5 keyword search, memory_entity for looking up facts by entity, memory_store for saving facts, memory_semantic_search for vector similarity search, and memory_add_entity for registering new entities at runtime.</p>
<h2>Memory Management</h2>
<p>The system automatically manages memory through consolidation, deduplicating entries on startup to maintain efficiency. It tracks conversation patterns to prevent loops and ensures relevant information is surfaced when needed. The hybrid search approach balances precision with semantic understanding.</p>
<h2>Integration Benefits</h2>
<p>By providing persistent memory, the plugin enables agents to maintain context across sessions, remember user preferences, track project details, and build upon previous conversations. This creates more natural, productive interactions and reduces repetitive questioning.</p>
<h2>Performance Considerations</h2>
<p>The plugin is designed for efficiency with configurable limits on recall results and capture operations. The SQLite backend provides fast local storage, while the optional Ollama integration adds semantic capabilities without blocking operations. The system automatically manages resource usage through consolidation and deduplication.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/kevinodell/lily-memory-plugin/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/kevinodell/lily-memory-plugin/SKILL.md</a></p>

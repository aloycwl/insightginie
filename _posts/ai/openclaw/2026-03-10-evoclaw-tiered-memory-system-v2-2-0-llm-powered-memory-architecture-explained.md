---
layout: post
title: "EvoClaw Tiered Memory System v2.2.0: LLM-Powered Memory Architecture Explained"
date: 2026-03-10T20:45:52
categories: [24854]
original_url: https://insightginie.com/evoclaw-tiered-memory-system-v2-2-0-llm-powered-memory-architecture-explained
---

EvoClaw Tiered Memory System v2.2.0: LLM-Powered Memory Architecture Explained
==============================================================================

Published on June 10, 2024 by WordPress Admin

Welcome to the comprehensive guide on the EvoClaw Tiered Memory Architecture v2.2.0! This post will walk you through the intricacies of this LLM-powered three-tier memory system, designed to enhance the cognitive capabilities of EvoClaw agents. With significant updates including automatic daily note ingestion, structured metadata extraction, URL preservation, validation, and cloud-first sync, this memory architecture is poised to redefine how AI agents manage and retrieve information.

Understanding the Architecture
------------------------------

The EvoClaw memory system is meticulously structured into three distinct tiers: Hot, Warm, and Cold memory. Each tier serves a unique purpose, mimicking the way human memory operates with different levels of importance and accessibility. Below, we delve into each tier and explore their functionalities, design principles, and recent updates.

### Hot Memory (5KB max)

The Hot Memory tier is the core of the EvoClaw agent's context, holding essential information that is always available in the agent's context window. This tier includes:

* **Identity:** Basic information about the agent, such as its name and owner.
* **Owner Profile:** Details about the user, including their preferences, family, and work hours.
* **Active Context:** Information about ongoing projects, events, and tasks.
* **Critical Lessons:** Important lessons learned, categorized and prioritized.

This tier is auto-pruned to ensure it stays within the 5KB limit, progressively removing less important information if the limit is exceeded.

### Warm Memory (50KB max, 30-day retention)

The Warm Memory tier holds recent distilled facts with a scoring mechanism that determines their relevance and importance. Each entry in this tier includes:

* **Text:** The fact or information stored.
* **Category:** The category under which the fact is stored.
* **Importance:** A score indicating the importance of the fact.
* **Created At:** The timestamp when the fact was created.
* **Access Count:** The number of times the fact has been accessed.
* **Score:** A calculated score based on importance, recency, and access count.
* **Tier:** The classification of the fact's tier (Hot, Warm, Cold).

The scoring mechanism ensures that the most relevant and frequently accessed facts are retained, while less important ones are gradually moved to the Cold Memory tier or deleted.

### Cold Memory (Unlimited, Turso)

The Cold Memory tier serves as a long-term archive, storing information that is queryable but not bulk-loaded. This tier uses a database schema to manage the vast amount of information, including:

* **ID:** A unique identifier for each memory entry.
* **Agent ID:** The identifier for the agent associated with the memory.
* **Text:** The stored fact or information.
* **Category:** The category under which the fact is stored.
* **Importance:** The importance score of the fact.
* **Created At:** The timestamp when the fact was created.
* **Access Count:** The number of times the fact has been accessed.

This tier ensures that information is retained for up to 10 years (configurable) and provides monthly consolidation to remove frozen entries older than the retention period.

Design Principles
-----------------

The EvoClaw memory system is built on several key design principles:

* **From Human Memory:** Consolidation, Relevance Decay, Strategic Forgetting, Hierarchical Organization.
* **From PageIndex:** Vectorless Retrieval, Tree-Structured Index, Explainable Results, Reasoning-Based Search.
* **Cloud-First (EvoClaw):** Device is replaceable, Critical sync, Disaster recovery, Multi-device.

What's New in v2.2.0
--------------------

The latest update to the EvoClaw Tiered Memory System introduces several innovative features:

* **Automatic Daily Note Ingestion:** Consolidation (daily/monthly/full modes) now auto-runs ingest-daily, bridging memory/YYYY-MM-DD.md files to the tiered memory system. No more manual ingestion required—facts flow automatically.
* **Structured Metadata Extraction:** Automatic extraction of URLs, shell commands, and file paths from facts. Preserved during distillation and consolidation, searchable by URL fragment.
* **Memory Completeness Validation:** Check daily notes for missing URLs, commands, and next steps. Proactive warnings for incomplete information and actionable suggestions for improvement.
* **Enhanced Search:** Search facts by URL fragment. Get all stored URLs from warm memory. Metadata-aware fact storage.
* **URL Preservation:** URLs explicitly preserved during LLM distillation. Fallback metadata extraction if LLM misses them. Command-line support for adding metadata manually.

Conclusion
----------

The EvoClaw Tiered Memory System v2.2.0 represents a significant advancement in LLM-powered memory architectures. By leveraging a three-tiered structure inspired by human cognition and incorporating innovative features like automatic daily note ingestion, structured metadata extraction, and enhanced search capabilities, this system offers robust and efficient memory management for AI agents. Whether you're a developer, researcher, or enthusiast, understanding this architecture can provide valuable insights into the future of AI memory systems.

Further Reading
---------------

* [GitHub Repository: OpenClaw Tiered Memory](https://github.com/openclaw/skills/tree/main/skills/bowen31337/tiered-memory)
* [Wikipedia: Working Memory](https://en.wikipedia.org/wiki/Working_memory)
* [Wikipedia: Long-term Memory](https://en.wikipedia.org/wiki/Long-term_memory)

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/bowen31337/tiered-memory/SKILL.md>
---
layout: post
title: "Lily Memory: Persistent Memory Plugin for OpenClaw Agents"
date: 2026-03-05T11:01:52
categories: [24854]
original_url: https://insightginie.com/lily-memory-persistent-memory-plugin-for-openclaw-agents
---

In the rapidly evolving landscape of AI agents, memory capabilities have become a crucial differentiator between basic chatbots and truly intelligent systems. Lily Memory is a sophisticated persistent memory plugin designed specifically for OpenClaw agents that transforms how AI systems remember, learn, and build upon past interactions. This comprehensive plugin combines the power of traditional keyword search with cutting-edge vector semantic search, creating a hybrid system that ensures your agent never forgets important information while maintaining the ability to recall context from complex conversations.

## What is Lily Memory?

Lily Memory is a persistent memory plugin for OpenClaw agents that provides long-term memory capabilities that survive session resets, compaction, and restarts. Unlike traditional AI systems that treat each conversation as isolated, Lily Memory creates a living knowledge base that grows and evolves with every interaction. The plugin leverages SQLite FTS5 for efficient keyword searching combined with Ollama vector embeddings for semantic understanding, creating a robust hybrid search system that can retrieve information through multiple pathways.

The plugin is designed with zero npm dependencies, relying instead on sqlite3 CLI and native fetch capabilities, making it lightweight and easy to deploy. It works seamlessly with OpenClaw agents and can be configured to operate in various modes depending on your infrastructure and requirements.

## Core Features and Capabilities

### Auto-Recall Functionality

One of Lily Memory's most powerful features is its auto-recall capability. Before each LLM turn, the plugin automatically injects relevant memories as context, ensuring the agent has access to pertinent historical information. This creates a more coherent and contextually aware conversation flow, as the agent can reference past discussions, decisions, and facts without requiring manual context injection.

The auto-recall system uses a sophisticated multi-stage process. First, it extracts keywords from the current message, then performs both FTS5 keyword searches and vector similarity searches. The results are merged, deduplicated, and injected as context before the agent generates its response. This ensures that the most relevant memories are always at the agent's fingertips.

### Intelligent Auto-Capture

Lily Memory doesn't just help with recall—it actively captures and stores information from conversations. The auto-capture feature automatically extracts facts from conversations and stores them in the persistent database. This happens through a pattern recognition system that identifies structured information in the format of entity: key = value.

For example, if a conversation mentions “config: timeout = 30 seconds” or “system: version = 2.1.0”, Lily Memory will automatically recognize these as structured facts and store them appropriately. This passive capture mechanism ensures that valuable information is never lost and becomes part of the agent's growing knowledge base.

### Hybrid Search Architecture

The true power of Lily Memory lies in its hybrid search architecture. The plugin combines two complementary search approaches:

\*\*SQLite FTS5 Keyword Search\*\*: This traditional full-text search provides fast, reliable retrieval of information based on exact keyword matches. It's perfect for finding specific facts, dates, names, or other precise information.

\*\*Ollama Vector Semantic Search\*\*: This modern approach uses vector embeddings to understand the semantic meaning of queries. Even if the exact words aren't used, the system can find conceptually related information. For instance, searching for “deadline” might also return memories about “due dates” or “completion timelines.”

By combining these approaches, Lily Memory ensures comprehensive coverage of the knowledge base, whether users search with precise terms or more general concepts.

### Stuck Detection and Loop Prevention

One of the more innovative features of Lily Memory is its stuck detection capability. The plugin monitors conversation patterns and can detect when a topic is being repeatedly discussed without progress. It tracks the top 5 content words per response and calculates Jaccard similarity between consecutive messages.

When the system detects that 3 or more consecutive responses have greater than 60% content overlap, it intelligently injects a Reflexion nudge to help break the conversational loop. This prevents the agent from getting stuck in repetitive patterns and encourages more productive dialogue progression.

### Memory Consolidation

Over time, memory systems can become cluttered with redundant or outdated information. Lily Memory addresses this through its memory consolidation feature, which automatically deduplicates entries during startup. This ensures that the knowledge base remains clean, efficient, and relevant, without requiring manual maintenance.

### Dynamic Entity Management

Lily Memory supports dynamic entity management, allowing you to define which types of information should be captured and stored. The system uses a configuration-driven allowlist approach, but also provides runtime tools to add new entities as needed. This flexibility ensures that the memory system can adapt to evolving use cases and information types.

## Technical Architecture

### Database Design

The plugin uses SQLite with FTS5 extension for its storage layer. The database schema is optimized for fast retrieval and efficient storage of both structured facts and vector embeddings. The FTS5 extension provides powerful full-text search capabilities, while the standard SQLite tables handle structured data and relationships.

### Search Flow

The recall process follows a sophisticated multi-step flow:  
1. Keyword extraction from the current message  
2. FTS5 keyword search across all stored facts  
3. Vector similarity search via Ollama (if enabled)  
4. Result merging and deduplication  
5. Context injection before LLM turn

This ensures that the most relevant and comprehensive information is always available to the agent.

### Capture Flow

The capture process is equally sophisticated:  
1. Regex pattern scanning for entity: key = value formats  
2. Entity validation against the allowlist  
3. Structured storage in SQLite  
4. Asynchronous vector embedding via Ollama  
5. Integration into the knowledge base

This systematic approach ensures that captured information is both structured and semantically searchable.

## Installation and Configuration

### Quick Start

Installing Lily Memory is straightforward. Simply add the plugin to your extensions directory and configure it in your openclaw.json file:

“`json  
{  
“plugins”: {  
“slots”: {  
“memory”: “lily-memory”  
},  
“entries”: {  
“lily-memory”: {  
“enabled”: true,  
“config”: {  
“dbPath”: “~/.openclaw/memory/decisions.db”,  
“entities”: [“config”, “system”]  
}  
}  
}  
}  
}  
“`

After configuration, restart the gateway with `openclaw gateway restart` to activate the plugin.

### Configuration Options

Lily Memory offers extensive configuration options to tailor its behavior:

– \*\*dbPath\*\*: Location of the SQLite database  
– \*\*autoRecall\*\*: Enable/disable automatic memory injection  
– \*\*autoCapture\*\*: Enable/disable automatic fact extraction  
– \*\*maxRecallResults\*\*: Maximum memories per turn  
– \*\*maxCapturePerTurn\*\*: Maximum facts captured per response  
– \*\*stuckDetection\*\*: Enable/disable loop detection  
– \*\*vectorSearch\*\*: Enable/disable semantic search  
– \*\*ollamaUrl\*\*: Ollama endpoint URL  
– \*\*embeddingModel\*\*: Vector embedding model  
– \*\*consolidation\*\*: Enable/disable deduplication on startup  
– \*\*vectorSimilarityThreshold\*\*: Minimum similarity for vector matches  
– \*\*entities\*\*: Additional entity types to track

## Available Tools

Lily Memory provides several tools that agents can use to interact with the memory system:

– \*\*memory\_search\*\*: Perform FTS5 keyword searches  
– \*\*memory\_entity\*\*: Look up facts for specific entities  
– \*\*memory\_store\*\*: Manually save facts to memory  
– \*\*memory\_semantic\_search\*\*: Perform vector similarity searches  
– \*\*memory\_add\_entity\*\*: Register new entity types at runtime

These tools give agents programmatic access to their memory system, enabling sophisticated memory management and retrieval strategies.

## Use Cases and Benefits

### Enterprise Knowledge Management

For enterprise applications, Lily Memory transforms how organizations capture and utilize institutional knowledge. Customer service agents can remember previous interactions with clients, technical support can recall past solutions to similar problems, and sales teams can maintain context across multiple touchpoints.

### Personal AI Assistants

Individual users benefit from AI assistants that truly remember their preferences, schedules, and important information. Whether it's remembering dietary restrictions, preferred communication styles, or important dates, Lily Memory enables truly personalized interactions.

### Research and Analysis

Researchers and analysts can use Lily Memory to maintain comprehensive knowledge bases of their work. The plugin can capture research findings, methodology details, and analytical insights, making it easier to build upon previous work and avoid duplicating efforts.

### Content Creation

Writers, journalists, and content creators can leverage Lily Memory to maintain research notes, interview transcripts, and creative ideas. The semantic search capabilities make it easy to find related concepts even when exact keywords aren't remembered.

### Software Development

Development teams can use Lily Memory to document architectural decisions, bug fixes, and best practices. The persistent memory ensures that institutional knowledge survives team changes and project transitions.

## Benefits

### Improved Context Awareness

By maintaining persistent memory across sessions, agents can provide more contextually aware responses that reference past interactions and build upon previous discussions.

### Reduced Repetition

The stuck detection feature prevents agents from getting caught in conversational loops, improving user experience and ensuring more productive interactions.

### Knowledge Preservation

Important information is automatically captured and preserved, preventing the loss of valuable insights and decisions that might otherwise be forgotten.

### Enhanced Search Capabilities

The hybrid search approach ensures that information can be found whether users remember exact terms or only general concepts.

### Scalability

SQLite's efficiency and the plugin's optimized architecture ensure that the system can scale to handle large knowledge bases without performance degradation.

## Requirements and Dependencies

Lily Memory has minimal requirements:

– Node.js 18+ (for native fetch support)  
– SQLite 3.33+ with FTS5 extension  
– Optional: Ollama with nomic-embed-text model for semantic search

The plugin's zero npm dependency approach makes it lightweight and easy to deploy in various environments.

## Conclusion

Lily Memory represents a significant advancement in AI agent memory capabilities. By combining traditional keyword search with modern vector embeddings, providing intelligent auto-capture and recall, and including innovative features like stuck detection, it creates a comprehensive memory solution that transforms how AI agents interact with and learn from their environment.

Whether you're building enterprise applications, personal assistants, research tools, or content creation platforms, Lily Memory provides the persistent memory foundation needed for truly intelligent, context-aware AI interactions. Its flexible configuration, extensive tooling, and robust architecture make it an essential plugin for any OpenClaw agent deployment.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/ksemaj/lily-memory-5-0-0/SKILL.md>
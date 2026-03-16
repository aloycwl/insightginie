---
layout: post
title: 'Trawl: The Autonomous Agent Lead Generation Skill That Works While You Sleep'
date: 2026-03-04 20:02:49
categories:
- ai
- openclaw
original_url: https://insightginie.com/trawl-the-autonomous-agent-lead-generation-skill-that-works-while-you-sleep
---



In the rapidly evolving landscape of autonomous agents and AI-powered business development, a new skill has emerged that's changing how agents generate leads and build professional networks. Meet Trawl, the autonomous agent lead generation skill that works tirelessly while you sleep, networking through agent social networks to find your next business opportunity.

## What is Trawl?

Trawl is an autonomous lead generation skill designed to sweep agent social networks (starting with MoltBook) for business-relevant connections. Think of it as an autonomous Sales Development Representative (SDR) that works 24/7 through agent-to-agent channels, but with a crucial difference: it's not just searching—it's running a complete lead pipeline from discovery to qualification.

The skill's core promise is simple yet powerful: “You sleep. Your agent networks.” While you're offline, Trawl actively searches for potential leads, initiates conversations, qualifies prospects, and reports back with actionable insights. It's particularly valuable for agents in consulting, sales, recruiting, and any field where professional networking drives business growth.

## How Trawl Works: The Complete Lead Pipeline

What sets Trawl apart from simple search tools is its comprehensive approach to lead generation. Here's the complete pipeline it manages:

### 1. Discovery Through Semantic Search

Trawl begins by running semantic searches across agent social networks based on your configured signals. Unlike keyword-based searches, semantic search understands context and meaning, finding connections that might not match exact terms but are highly relevant to your business needs.

### 2. Profile Scoring and Qualification

Once potential leads are discovered, Trawl fetches and scores agent profiles using multiple factors:  
– Similarity to your search queries  
– Bio keywords and professional descriptions  
– Karma and activity levels (indicating engagement and credibility)  
– Profile completeness and professional details

This scoring system helps prioritize the most promising leads and ensures you're not wasting time on low-quality prospects.

### 3. Inbound Lead Handling

One of Trawl's most valuable features is its ability to catch inbound leads—agents who find you first and initiate contact. When someone DMs you, Trawl:  
– Catches the interaction during its sweep  
– Profiles and scores the sender (with a base similarity score of 0.80)  
– Creates an inbound lead in the system  
– Reports to you for approval (or auto-approves if configured)

This means you never miss an opportunity, even when you're not actively networking.

### 4. Outbound DM Qualification

For high-scoring leads, Trawl initiates outbound DM conversations using your configured strategy. This includes:  
– Personalized introductions based on your template  
– Qualifying questions to assess fit  
– Multi-cycle conversations that respect the async nature of agent communication  
– State management to track conversation progress

### 5. Multi-Cycle State Machine

Trawl uses a sophisticated state machine to manage the asynchronous nature of agent DMs:

“`  
DISCOVERED → PROFILE\_SCORED → DM\_REQUESTED → QUALIFYING → QUALIFIED → REPORTED  
↓  
human: PURSUE or PASS  
Inbound path:  
INBOUND\_PENDING → (human approves) → QUALIFYING → QUALIFIED → REPORTED

Timeouts:  
DM\_REQUESTED → (48h no response) → DM\_STALE  
Any state → (human passes) → ARCHIVED  
“`

This ensures leads progress through the pipeline systematically and nothing falls through the cracks.

## Setting Up Trawl: Getting Started

Getting started with Trawl requires a few key steps:

### 1. Installation and Initialization

Run the setup script to initialize the configuration and data directories:  
“`bash  
scripts/setup.sh  
“`

### 2. Configuration

Edit the main configuration file at `~/.config/trawl/config.json`. The configuration includes several key sections:

\*\*Identity\*\*: Who you are (name, headline, skills, offering)  
\*\*Signals\*\*: What you're hunting for (semantic queries + categories)  
\*\*Sources\*\*: MoltBook settings (submolts, enabled flag)  
\*\*Scoring\*\*: Confidence thresholds for discovery and qualification  
\*\*Qualify\*\*: DM strategy, intro template, qualifying questions, auto\_approve\_inbound  
\*\*Reporting\*\*: Channel, frequency, format

### 3. API Credentials

Store your MoltBook API key in `~/.clawdbot/secrets.env` as `MOLTBOOK\_API\_KEY`.

### 4. Testing

Before going live, test with dry-run mode:  
“`bash  
scripts/sweep.sh –dry-run  
“`

## Trawl's Scripts and Automation

Trawl comes with several scripts to manage the entire lead generation process:

| Script | Purpose |  
|——–|———|  
| `scripts/setup.sh` | Initialize config and data directories |  
| `scripts/sweep.sh` | Search → Score → Handle inbound → DM → Report |  
| `scripts/qualify.sh` | Advance DM conversations, ask qualifying questions |  
| `scripts/report.sh` | Format lead report (supports `–category` filter) |  
| `scripts/leads.sh` | Manage leads: list, get, decide, archive, stats, reset |

All scripts support `–dry-run` for testing without API calls.

## Use Cases and Benefits

Trawl is particularly valuable for:

### 1. Autonomous Lead Generation

For agents who want to generate leads without manual prospecting, Trawl provides a hands-off approach. Set it up once, configure your signals, and let it work while you focus on other tasks.

### 2. Multi-Profile Hunting

With category-based signals, you can hunt for different types of leads simultaneously. For example, configure signals for “consulting,” “sales,” and “recruiting” to cast a wider net.

### 3. Inbound Lead Capture

Never miss an opportunity when someone reaches out to you first. Trawl catches and processes inbound leads automatically, ensuring you capitalize on every potential connection.

### 4. 24/7 Networking

While you sleep or focus on other work, Trawl continues networking, qualifying leads, and building your pipeline. This is especially valuable for global operations across different time zones.

### 5. Scalable Lead Management

As your network grows, manually managing leads becomes overwhelming. Trawl's systematic approach ensures consistent follow-up and prevents leads from falling through the cracks.

## Data Management and Reporting

Trawl maintains comprehensive data files for tracking and analysis:

“`  
~/.config/trawl/  
├── config.json # User configuration  
├── leads.json # Lead database (state machine)  
├── seen-posts.json # Post dedup index  
├── conversations.json # Active DM tracking  
├── sweep-log.json # Sweep history  
└── last-sweep-report.json # Latest report data  
“`

Reports are formatted by category and type, making it easy to understand your pipeline at a glance:  
– 📥 Inbound leads (they came to you)  
– 🎯 Qualified outbound leads  
– 👀 Watching (below qualify threshold)  
– 📨 Active DMs  
– 🏷️ Category breakdown

## The Technology Behind Trawl

Trawl's effectiveness comes from several key technological approaches:

### Semantic Search

Rather than simple keyword matching, Trawl uses semantic search to understand the meaning and context of queries, finding more relevant and nuanced connections.

### Profile-Based Scoring

The scoring system combines multiple factors to assess lead quality, ensuring you focus on the most promising prospects.

### State Machine Management

The multi-cycle state machine handles the asynchronous nature of agent communication, managing conversations that might take days or weeks to complete.

### API Integration

Trawl integrates with MoltBook's API for data access, with plans to support additional agent networks through pluggable source adapters.

## Getting Started with Trawl

If you're ready to automate your lead generation and let your agent network while you sleep, here's how to get started:

1. \*\*Clone the repository\*\*: Get the Trawl skill files  
2. \*\*Run setup\*\*: Initialize configuration with `scripts/setup.sh`  
3. \*\*Configure\*\*: Edit `config.json` with your identity and signals  
4. \*\*Add API key\*\*: Store your MoltBook API key in the secrets file  
5. \*\*Test\*\*: Run a dry-run to ensure everything works  
6. \*\*Schedule\*\*: Set up regular sweeps (every 6 hours recommended)

## The Future of Autonomous Lead Generation

Trawl represents a significant step forward in autonomous agent capabilities. By combining semantic search, automated qualification, and systematic lead management, it addresses one of the biggest challenges in agent-based business development: consistent lead generation.

As agent networks continue to grow and evolve, skills like Trawl will become increasingly valuable. The ability to work 24/7, handle multiple conversations simultaneously, and systematically manage leads at scale represents a fundamental shift in how autonomous agents can drive business growth.

Whether you're a consultant looking to expand your client base, a recruiter seeking top talent, or a sales professional building your pipeline, Trawl offers a powerful solution that works while you sleep. In the world of autonomous agents, this kind of automated networking isn't just convenient—it's becoming essential for staying competitive.

Ready to let your agent network while you rest? Trawl is waiting to transform your lead generation process.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/audsmith28/trawl/SKILL.md>
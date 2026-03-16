---
layout: post
title: "OpenClaw Skill: Seithar Intelligence — Threat Intelligence &#038; Cognitive Security Feed"
date: 2026-03-16T10:16:33
categories: [24854]
original_url: https://insightginie.com/openclaw-skill-seithar-intelligence-threat-intelligence-cognitive-security-feed
---

Introduction to Seithar Intelligence Skill
------------------------------------------

Seithar Intelligence is a sophisticated OpenClaw skill that transforms your agent into a personal cyber threat intelligence analyst. This skill monitors cybersecurity and cognitive security feeds, scores items against your configured interests, delivers daily briefings, and provides on-demand deep-dive analysis of any threat – whether technical or cognitive in nature.

Think of it as having ThreatMouth in your pocket, providing cyber + cognitive security awareness from any chat application you use with OpenClaw.

What This Skill Does
--------------------

The Seithar Intelligence skill turns your OpenClaw into a comprehensive threat intelligence analyst that:

* Monitors multiple cybersecurity RSS feeds including BleepingComputer, The Hacker News, Krebs on Security, CISA, Full Disclosure, Exploit-DB, SANS ISC, oss-security, Schneier, PacketStorm, DarkReading, and more
* Monitors cognitive security feeds including EUvsDisinfo, DFRLab, Bellingcat, RAND, and Seithar Research
* Scores each feed item against your configured interest profile to determine relevance
* Delivers morning and evening briefings via your preferred chat application
* Provides on-demand deep-dive analysis of any CVE, vulnerability, exploit, influence operation, or campaign
* Maps items to MITRE ATT&CK and DISARM framework techniques
* Discovers public proof-of-concept code for disclosed vulnerabilities
* Maintains a running threat landscape summary that evolves with the feed

Getting Started with Seithar Intelligence
-----------------------------------------

Setting up the Seithar Intelligence skill is straightforward. You’ll need to configure your interest profile, set up briefing schedules, and define what types of threats you want to monitor most closely.

### Configuring Your Interest Profile

The skill works best when it understands your specific security interests. You should configure your OpenClaw with a detailed interest profile. Here’s an example of what you might tell your OpenClaw:

*My security interests are:*

* Malware analysis and reverse engineering
* Social engineering and cognitive security
* Network exploitation
* OSINT and intelligence gathering
* Influence operations and information warfare
* Vulnerability research and exploit development

*I’m currently studying:*

* MITRE ATT&CK framework
* DISARM framework for influence operations
* Python security tooling
* OverTheWire wargames

*My skill level:* intermediate

*Deprioritize:*

* Enterprise compliance and GRC
* Cloud IAM and AWS security
* Vendor marketing announcements
* Corporate breach notifications unless technically interesting

The skill stores this profile in memory and uses it to score every feed item for relevance, ensuring you only receive the most pertinent information.

### Setting Up Briefings

The skill provides two main types of briefings: scheduled briefings and on-demand queries. By default, the skill operates on this schedule:

* **Morning briefing:** 8:00 AM local time – Top 5 items from overnight, any critical alerts
* **Evening briefing:** 6:00 PM local time – Day summary, items scored above 0.7, study recommendations
* **Critical alerts:** Immediate – Items scored above 0.9 pushed as soon as detected

You can customize these times by telling your OpenClaw: “Change my briefing time to 9 AM and 7 PM” or “Only send critical alerts, no scheduled briefings.”

### Feed Check Interval

By default, the skill checks feeds every 2 hours using OpenClaw’s cron/heartbeat system to periodically fetch and process new content. This ensures you stay up-to-date without being overwhelmed by constant notifications.

How Seithar Intelligence Works
------------------------------

Understanding the inner workings of this skill helps you appreciate how it delivers such targeted and valuable intelligence.

### Feed Collection Process

On each check interval, the skill instructs the agent to:

1. Fetch RSS feeds from the configured source list using the web\_fetch tool
2. Parse feed entries (title, link, published date, summary/description)
3. Deduplicate against previously seen items (tracked in memory by URL hash)
4. For each new item, score it against the operator’s interest profile

### Scoring System

Each new item is scored on a scale from 0.0 to 1.0 against your profile:

* **0.9 – 1.0:** Critical – Matches core interests directly, high urgency (active exploitation, 0-day, major campaign)
* **0.7 – 0.9:** High – Relevant to interests, worth reading today
* **0.5 – 0.7:** Medium – Tangentially relevant, include in digest
* **Below 0.5:** Low – Skip unless specifically requested

The agent scores by examining the item’s title, summary, source, and any CVE/technique references against your stored interest profile. No external API is needed – the LLM does the scoring inline.

### Categorization System

Items are automatically categorized into:

* **CRITICAL ALERT:** Active exploitation, 0-day, critical infrastructure
* **EXPLOIT DROP:** New CVE, PoC release, vulnerability disclosure
* **MALWARE:** Malware analysis, RE findings, campaign reports
* **INFLUENCE OP:** Disinformation campaigns, cognitive security, DISARM-mapped operations
* **TECHNIQUE:** ATT&CK or DISARM technique deep-dives, methodology
* **LEARNING:** Tutorials, CTF writeups, educational content
* **GENERAL:** Industry news, policy, commentary

Daily Briefings
---------------

The skill delivers comprehensive briefings in a structured format that makes it easy to quickly understand the threat landscape.

### Morning Briefing Format

Here’s an example of what a morning briefing might look like:

```
╔══════════════════════════════════════════════════╗
║  SEITHAR INTELLIGENCE BRIEFING                   ║
║  2026-02-11 08:00 EST                            ║
╚══════════════════════════════════════════════════╝
CRITICAL (act now):
🔴 [0.95] Pre-auth RCE in OpenSSH (CVE-2026-XXXXX)
Full Disclosure | 2h ago
Affects OpenSSH 9.x. Public PoC available.
▸ Say "deep dive CVE-2026-XXXXX" for full analysis
HIGH RELEVANCE:
🟠 [0.87] Lazarus Group deploys new social engineering
kit targeting crypto developers
The Hacker News | 4h ago
DISARM: T0047 (Develop Content), ATT&CK: T1566.001
▸ Say "deep dive lazarus social engineering" for analysis
🟠 [0.82] New Nuclei templates for Spring4Shell variants
Exploit-DB | 6h ago
12 new detection templates + PoC payloads
▸ Say "explain spring4shell" for context
🟠 [0.78] Russian influence operation targeting NATO
narratives detected across 3 platforms
DFRLab | 5h ago
DISARM: T0046, T0048, T0056 | Coordinated inauthentic behavior
▸ Say "deep dive nato influence op" for DISARM breakdown
STUDY RECOMMENDATION:
Based on today's feed: review SSH key exchange internals
and pre-authentication attack surfaces. OverTheWire Bandit
levels 14-17 cover SSH fundamentals.
──────────────────────────────────────────────────
24 items collected | 4 high relevance | 1 critical
Seithar Intelligence Division v1.0
認知作戦 | seithar.com/research
──────────────────────────────────────────────────
```

### Evening Briefing Format

Evening briefings provide a summary of the day’s events and study recommendations based on what you’ve encountered:

```
╔══════════════════════════════════════════════════╗
║  SEITHAR INTELLIGENCE EVENING BRIEFING           ║
║  2026-02-11 18:00 EST                            ║
╚══════════════════════════════════════════════════╝
TODAY'S SUMMARY:
- 24 new items collected
- 4 items scored above 0.7
- 1 critical alert issued
- 3 new CVEs disclosed
- 2 influence operations detected
TOP STORIES:
1. OpenSSH Pre-auth RCE (CVE-2026-XXXXX) - Critical
2. Lazarus Group Social Engineering Toolkit
3. Spring4Shell Variants - New PoCs
4. NATO Influence Operation Analysis
LEARNING RECOMMENDATIONS:
Based on today's feed:
- Review SSH key exchange internals
- Study social engineering frameworks
- Practice with OverTheWire Bandit levels 14-17
- Read DISARM framework documentation
PREPARE FOR TOMORROW:
Monitor for: OpenSSH patches, Spring4Shell exploitation,
Russian influence campaign developments
──────────────────────────────────────────────────
Seithar Intelligence Division v1.0
認知作戦 | seithar.com/research
──────────────────────────────────────────────────
```

On-Demand Deep Dive Analysis
----------------------------

When you need more detailed information about a specific threat, the skill provides comprehensive deep-dive analysis.

### Requesting a Deep Dive

You can request deep dives using various triggers:

* “deep dive [topic]”
* “explain CVE-XXXX-XXXXX”
* “analyze this threat”
* “what should I study today”

### Deep Dive Process

When you request a deep dive, the skill:

1. Fetches the full article content via web\_fetch
2. If a CVE is mentioned, queries the NVD API for structured vulnerability data
3. Searches GitHub for public PoC repositories using the GitHub API
4. Generates a structured educational breakdown

### Deep Dive Format

Here’s an example of what a deep dive might look like:

```
╔══════════════════════════════════════════════════╗
║  SEITHAR DEEP DIVE                               ║
║  CVE-2026-XXXXX — OpenSSH Pre-Auth RCE           ║
╚══════════════════════════════════════════════════╝
WHAT HAPPENED:
A memory corruption vulnerability in OpenSSH's key exchange
handler allows unauthenticated attackers to achieve remote
code execution as root. No credentials required.
HOW THE EXPLOIT WORKS:
1. Attacker connects to SSH port 22
2. During key exchange (before authentication), sends
   oversized payload in the KEX_INIT message
3. Buffer overflow overwrites return address on stack
4. Execution redirected to attacker's shellcode
5. Root shell achieved
IMPACT ASSESSMENT:
- CVSS: 9.8/10 (Critical)
- Affects: OpenSSH 9.x, 8.x (some versions)
- No authentication required
- Can be performed anonymously
- Complete system compromise
MITRE ATT&CK MAPPING:
- T1190: Exploitation for Defense Evasion
- T1068: Exploitation for Privilege Escalation
- T1059.004: PowerShell (if used in post-exploit)
DISARM FRAMEWORK:
- Not applicable (technical vulnerability)
POC ANALYSIS:
- Public PoC available on GitHub
- Written in Python 3.9+
- Requires network access to target
- Works against default SSH configurations
RECOMMENDATIONS:
- Apply patches immediately
- Monitor SSH logs for unusual key exchange attempts
- Consider network segmentation
- Review SSH hardening guides
RELATED THREATS:
- Similar vulnerabilities in other SSH implementations
- Potential for wormable exploitation
- Active exploitation in the wild
──────────────────────────────────────────────────
Seithar Intelligence Division v1.0
認知作戦 | seithar.com/research
──────────────────────────────────────────────────
```

Available Triggers
------------------

The skill responds to various natural language triggers:

* “threat briefing” / “security briefing” / “morning briefing” / “what’s new in security”
* “check threats” / “check feeds” / “any new vulns”
* “explain CVE-XXXX-XXXXX” / “deep dive on [topic]” / “analyze this threat”
* “cogdef briefing” / “cognitive security update” / “any new psyops”
* “what should I study today” / “learning recommendations”
* “threat landscape” / “what’s trending in security”
* “poc for CVE-XXXX-XXXXX” / “any exploits for [software]”
* “seithar brief”

Feed Sources
------------

The skill monitors an extensive list of RSS feeds across multiple categories:

### Cybersecurity Feeds

* BleepingComputer
* The Hacker News
* Krebs on Security
* CISA (Cybersecurity and Infrastructure Security Agency)
* Full Disclosure mailing list
* Exploit-DB
* SANS ISC
* oss-security mailing list
* Schneier on Security
* PacketStorm
* DarkReading

### Cognitive Security Feeds

* EUvsDisinfo
* DFRLab (Digital Forensics Research Lab)
* Bellingcat
* RAND Corporation
* Seithar Research

Benefits of Using Seithar Intelligence
--------------------------------------

Implementing this skill provides numerous benefits for security professionals, researchers, and enthusiasts:

### Time Efficiency

Instead of manually checking dozens of security feeds daily, you receive curated, scored, and categorized intelligence automatically. This saves hours each week while ensuring you never miss critical threats.

### Personalized Intelligence

The scoring system ensures you only receive information relevant to your specific interests and skill level. No more wading through enterprise compliance news when you’re focused on vulnerability research.

### Educational Value

The deep-dive feature provides structured learning opportunities, complete with MITRE ATT&CK mappings, DISARM framework analysis, and practical recommendations. It’s like having a personal security tutor.

### Proactive Security Posture

By receiving timely briefings and critical alerts, you can proactively address threats before they impact your systems or research. The skill helps you stay ahead of emerging attack patterns.

### Cognitive Security Awareness

The inclusion of cognitive security feeds helps you understand influence operations, disinformation campaigns, and information warfare – crucial skills in today’s threat landscape.

Technical Implementation
------------------------

While you don’t need to understand the technical details to use the skill, here’s a brief overview of how it works:

* Uses OpenClaw’s cron/heartbeat system for scheduled feed checks
* Implements web\_fetch tool for RSS feed collection
* Uses in-memory storage for deduplication and interest profile
* Employs LLM-based scoring without external APIs
* Integrates with NVD API for CVE data when needed
* Uses GitHub API for PoC repository discovery
* Formats output as structured text for easy reading

Getting Started Today
---------------------

To start using Seithar Intelligence:

1. Install the skill in your OpenClaw environment
2. Configure your interest profile as described above
3. Set your preferred briefing times
4. Wait for your first briefing (or ask for one on-demand)
5. Begin requesting deep dives on topics that interest you

Within 24 hours, you’ll have a personalized threat intelligence feed that keeps you informed about the security landscape that matters most to you.

Conclusion
----------

Seithar Intelligence represents a significant advancement in personal threat intelligence and cognitive security awareness. By combining automated feed monitoring, intelligent scoring, structured briefings, and on-demand deep analysis, it provides security professionals and enthusiasts with a powerful tool for staying informed and educated.

Whether you’re a malware analyst, penetration tester, security researcher, or simply someone passionate about cybersecurity, this skill adapts to your needs and helps you navigate the complex and ever-changing threat landscape with confidence.

Remember: in the world of cybersecurity, knowledge is power. Seithar Intelligence ensures you have the knowledge you need, when you need it, in a format that’s easy to digest and act upon.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/mirai8888/seithar-intel/SKILL.md>
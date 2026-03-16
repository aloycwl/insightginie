---
layout: post
title: "Understanding the OpenClaw Claude Usage Skill: Track Your Claude Subscription"
date: 2026-03-08T22:45:55
categories: [24854]
original_url: https://insightginie.com/understanding-the-openclaw-claude-usage-skill-track-your-claude-subscription
---

Understanding the OpenClaw Claude Usage Skill: Track Your Claude Subscription
=============================================================================

The [OpenClaw Claude Usage Skill](https://github.com/openclaw/skills/blob/main/skills/lemodigital/claude-usage/SKILL.md) is a powerful tool designed to help users monitor and manage their [Claude](https://claude.ai/) Max subscription. This skill calculates the usage based on session data and provides detailed insights into credits consumed, weekly budget percentages, rate limits, and per-session breakdowns.

What Does the OpenClaw Claude Usage Skill Do?
---------------------------------------------

The primary function of this skill is to track your Claude Max subscription usage by calculating credits consumed and providing a comprehensive overview of your spending. Here are the key features:

1. **Credits Calculation:** The skill calculates the credits used based on the reverse-engineered credits system from she-llac.com/claude-limits.
2. **Weekly Overview:** It provides a weekly overview showing the total credits used versus the weekly budget, including a progress bar for easy visual tracking.
3. **Rate Limit Monitoring:** The tool warns users if they are approaching the per-5-hour rate limit, helping to avoid any potential disruptions.
4. **Session Breakdown:** Users can see all sessions ranked by credits consumed, along with a detailed model breakdown (Opus, Sonnet, Haiku, non-Claude).
5. **Single Session Detail:** For a more granular view, users can analyze individual sessions to see the credits consumed, percentage of the weekly budget used, and token breakdown (input/output/cache).

When to Use the OpenClaw Claude Usage Skill
-------------------------------------------

The skill is particularly useful when users want to:

* Check their current Claude usage and credits.
* Monitor how much of their budget is left.
* Understand their rate limits and how close they are to hitting them.
* Analyze the cost per session to optimize their usage.

Setting Up the Skill
--------------------

To use the OpenClaw Claude Usage Skill, you’ll need to set it up initially by providing two key pieces of information:

* **Weekly Reset Time:** This can be found on claude.ai under Settings > Usage (e.g., “Resets Mon 2:00 PM”).
* **Plan:** Choose between the Pro ($20), 5x ($100), or 20x ($200) plans. The default is 5x.

Once you’ve gathered this information, save it to avoid repeating the process:

```
python3 {SKILL_DIR}/scripts/claude-usage.py "2026-02-09 14:00" --plan 5x --save
```

Commands for the OpenClaw Claude Usage Skill
--------------------------------------------

The skill can be used with several commands to generate different outputs:

* **Weekly Overview:** Uses saved config after the first –save.
* **Override Plan or Timezone:** Allows you to override the plan or timezone for the report.
* **Top N Sessions Only:** Displays the top N sessions ranked by credits consumed.
* **Single Session Detail:** Provides detailed information on a specific session.
* **JSON Output:** Generates output in JSON format for easy integration with other tools.

What the Skill Shows
--------------------

The OpenClaw Claude Usage Skill provides several detailed views of your Claude usage:

* **Weekly Overview:** Total credits used vs. the weekly budget with a progress bar.
* **Rate Limit Monitoring:** A 5-hour sliding window to warn if you’re approaching the rate limit.
* **All Sessions Ranked by Credits Consumed:** A comprehensive list of all sessions ranked by credits used.
* **Model Breakdown:** A breakdown of the models used (Opus, Sonnet, Haiku, non-Claude).
* **Single Session Detail:** Detailed information on individual sessions when using the –session argument.

Credits Formula and Plan Budgets
--------------------------------

The skill uses a specific formula to calculate credits:

```
credits = (input_tokens + cache_write_tokens) × input_rate + output_tokens × output_rate
```

The rates vary by model:

| Model | Input Rate | Output Rate |
| --- | --- | --- |
| Haiku | 2/15 | 10/15 |
| Sonnet | 6/15 | 30/15 |
| Opus | 10/15 | 50/15 |

Note that cache reads are free, and non-Claude models (Gemini, Codex, etc.) do not consume Claude credits.

The skill also supports different plan budgets:

| Plan | $/Month | Credits/5h | Credits/Week |
| --- | --- | --- | --- |
| Pro | $20 | 550,000 | 5,000,000 |
| 5× | $100 | 3,300,000 | 41,666,700 |
| 20× | $200 | 11,000,000 | 83,333,300 |

Requirements
------------

To use the OpenClaw Claude Usage Skill, you’ll need:

* Python 3.9+
* OpenClaw with session JSONL files (auto-detected at ~/.openclaw/agents/main/sessions/)

This skill is an essential tool for anyone looking to manage their Claude Max subscription effectively, ensuring they stay within their budget and avoid hitting rate limits.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/lemodigital/claude-usage/SKILL.md>
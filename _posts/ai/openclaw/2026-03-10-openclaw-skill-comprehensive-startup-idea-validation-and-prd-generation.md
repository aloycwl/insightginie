---
layout: post
title: "OpenClaw Skill: Comprehensive Startup Idea Validation and PRD Generation"
date: 2026-03-10T17:16:54
categories: [24854]
original_url: https://insightginie.com/openclaw-skill-comprehensive-startup-idea-validation-and-prd-generation
---

What is the solo-validate Skill?
--------------------------------

The solo-validate skill is a comprehensive startup idea validation tool designed to help entrepreneurs and product teams make data-driven decisions about whether to pursue, pivot, or kill their startup ideas. It combines multiple validation frameworks into a single workflow that can determine in minutes whether an idea is worth pursuing.

### Core Philosophy

The skill operates on a simple but powerful principle: **it's better to kill a bad idea in 5 minutes than waste 3 months building it**. The validation process is intentionally honest and critical rather than optimistic, prioritizing truth over encouragement.

Key Features and Capabilities
-----------------------------

### 1. S.E.E.D. Niche Check

The skill performs a quick four-dimensional assessment before deep analysis:

* **S – Searchability**: Can you rank? Are forums/Reddit in top-10? Few fresh giants? No video blocks?
* **E – Evidence**: Real user pain with quotes/URLs or just founder's hypothesis?
* **E – Ease**: MVP in 1-2 days on existing stack? No heavy dependencies?
* **D – Demand**: Long-tail keywords exist? Clear monetization path?

If any kill flags trigger (SERP dominated by giants, fresh competing content, no evidence of pain, MVP needs >1 week), the skill recommends killing the idea immediately.

### 2. STREAM 6-Layer Analysis

The skill walks ideas through all six layers of the STREAM framework:

1. **Layer 1 (Scope)**: Map!=Territory, Simplicity, Boundaries – what assumptions are unproven?
2. **Layer 2 (Time)**: Entropy, Lindy – will this exist in 5 years?
3. **Layer 3 (Route)**: Inversion, Second-Order Effects – effects of effects?
4. **Layer 4 (Stakes)**: Asymmetry, Antifragility – real risk/reward with pessimistic numbers
5. **Layer 5 (Audience)**: Reputation, Network – deposit or withdrawal?
6. **Layer 6 (Meta)**: Mortality, Balance – worth finite time? Aligns with mission?

Each layer is scored 1-10, with Meta and Stakes weighted 1.5x in the final score.

### 3. Devil's Advocate Inversion

Before scoring positively, the skill actively tries to kill the idea by:

* Listing 5 specific ways the idea could fail (not generic risks)
* Searching for dead startups that tried similar approaches
* Performing unit economics stress tests with pessimistic assumptions
* Testing the “empty market” hypothesis – is the segment empty because demand doesn't exist?

### 4. Manifest Alignment Check

The skill checks ideas against 9 core principles and 6 red flags from the OpenClaw manifest:

* Privacy-first / offline-first
* One pain -> one feature -> launch
* AI as foundation, not feature
* Speed over perfection (MVP in days)
* Antifragile architecture
* Money without overheating
* Against exploitation
* Subscription fatigue
* Creators, not robots

Violations are flagged honestly – 0 violations = perfect, 1-2 = caution, 3+ = strong KILL signal.

### 5. Auto-Stack Selection

Based on the idea type and research data, the skill automatically recommends appropriate tech stacks:

* iOS apps: ios-swift
* Android apps: kotlin-android
* AI/ML web apps: nextjs-supabase or nextjs-ai-agents
* Landing pages: astro-static
* Content sites with SSR needs: astro-hybrid

### 6. Complete PRD Generation

The skill generates a comprehensive Product Requirements Document with:

* Executive summary and elevator pitch
* Problem statement and solution
* Target audience and market size
* Competitor analysis
* Feature breakdown and MVP scope
* Technical architecture and stack selection
* Acceptance criteria for each feature
* Success metrics and KPIs
* Go-to-market strategy

Usage Scenarios
---------------

The skill is triggered when users say:

* “validate idea”
* “score this idea”
* “should I build this”
* “go or kill”
* “generate PRD”
* “evaluate opportunity”

**Important:** Do NOT use for deep research (use /research first) or decision-only framework (use /stream instead).

Technical Implementation
------------------------

The skill uses MCP tools when available:

* kb\_search(query, n\_results) – search knowledge base for related docs
* project\_info() – list active projects with stacks
* web\_search(query) – search for dead startups, competitor failures

If MCP tools aren't available, it falls back to Grep/Glob/WebSearch for local file analysis and web research.

Output and Decision Making
--------------------------

The skill provides clear, actionable recommendations:

* **GO**: Idea passes all checks, clear path forward
* **CAUTION**: Some issues but potentially fixable
* **KILL**: Critical issues found, don't waste time building

For KILL recommendations, the skill provides specific reasons and suggests alternatives or pivots.

Benefits
--------

Using solo-validate can save months of development time by:

* Identifying fatal flaws early
* Ensuring alignment with proven principles
* Providing clear technical direction
* Generating complete PRD documentation
* Reducing emotional bias in decision-making

The skill transforms startup validation from guesswork into a systematic, repeatable process that maximizes the chances of building something people actually want.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/fortunto2/solo-validate/SKILL.md>
---
layout: post
title: "GitHub Issue Prioritizer: How to Analyze and Rank Issues by ROI and Impact"
date: 2026-03-12T05:16:23
categories: [24854]
original_url: https://insightginie.com/github-issue-prioritizer-how-to-analyze-and-rank-issues-by-roi-and-impact
---

What is the GitHub Issue Prioritizer Skill?
-------------------------------------------

The GitHub Issue Prioritizer is a read-only skill designed to help you analyze and rank GitHub issues by their **Adjusted Score**—which combines ROI (return on investment) with penalties for solution sanity, architectural impact, and actionability. This skill is perfect for triaging issues, identifying quick wins, and filtering out non-actionable items.

When to Use This Skill
----------------------

* **Triaging or ranking issues** in a repository to identify what matters most
* **Finding quick wins** for contributors who want to make immediate impact
* **Filtering out non-actionable items** like questions, duplicates, or support requests
* **Detecting over-engineered proposals** that might be more complex than necessary
* **Matching issues to contributor skill levels** based on difficulty and complexity

When NOT to Use This Skill
--------------------------

* **Managing forks or syncing with upstream** — use the `fork-manager` skill instead
* **General GitHub CLI queries** like PR status or CI runs — use the `github` skill instead
* **Reviewing code changes before publishing** — use the `pr-review` skill instead

Requirements
------------

Before using this skill, you need:

* **gh CLI** authenticated with `gh auth login`
* Access to the repository you want to analyze

How It Works: The Analysis Process
----------------------------------

### Step 1: Get Repository

If you don’t specify a repository, the skill will ask which one to analyze using the format `owner/repo`.

### Step 2: Fetch Issues

The skill fetches issues using various methods:

* **Basic fetch**: Gets the most recent open issues with `gh issue list --repo {owner/repo} --state open --limit {limit}`
* **Topic-based fetch**: Uses `--topic`  to find issues matching specific topics (e.g., `--topic telegram`)
* **Search-based fetch**: Uses `--search`  for full control over GitHub search queries
* **Label-based fetch**: Uses `--label`  to filter by specific labels

### Step 3: Filter Issues with Existing PRs

Before analysis, the skill checks for open PRs that already address issues to avoid duplicate work. It detects linked issues using:

* **Explicit keywords**: `fixes #N`, `closes #N`, `resolves #N` (high confidence)
* **Issue references**: `#N`, `issue #N`, `related to #N` (medium confidence)
* **Title similarity**: Fuzzy matching of normalized titles (70%+ overlap)
* **Semantic matching**: Same components or error names mentioned

### Step 4: Analyze Each Issue

Each issue is scored across four dimensions:

#### 1. Difficulty (1-10)

Base score starts at 5, then adjusts based on signals:

* **Documentation only**: -3 points
* **Has proposed solution**: -2 points
* **Has reproduction steps**: -1 point
* **Clear error message**: -1 point
* **Unknown root cause**: +3 points
* **Architectural change**: +3 points
* **Race condition/concurrency**: +2 points
* **Security implications**: +2 points
* **Multiple systems involved**: +2 points

#### 2. Importance (1-10)

Ranges from 1 (low) to 10 (critical):

* **8-10: Critical** – Crash, data loss, security vulnerability, service down
* **6-7: High** – Broken functionality, errors, performance issues
* **4-5: Medium** – Enhancements, feature requests, improvements
* **1-3: Low** – Cosmetic, documentation, typos

#### 3. Tripping Scale (1-5) – Solution Sanity

How “out there” is the proposed solution?

* **1: Total Sanity** – Proven approach, standard patterns
* **2: Grounded w/Flair** – Practical with creative touches
* **3: Dipping Toes** – Exploring cautiously
* **4: Wild Adventure** – Bold, risky, unconventional
* **5: Tripping** – Questionable viability

**Red Flags** (+score): rewrite from scratch, buzzwords (blockchain, AI-powered, ML-based), experimental/unstable, breaking change, custom protocol

**Green Flags** (-score): standard approach, minimal change, backward compatible, existing library, well-documented

#### 4. Architectural Impact (1-5)

Always ask: “Is there a simpler way?” before scoring.

* **1: Surgical** – Isolated fix, 1-2 files, no new abstractions
* **2: Localized** – Small addition, follows existing patterns exactly
* **3: Moderate** – New component within existing architecture
* **4: Significant** – New subsystem, new patterns, affects multiple modules
* **5: Transformational** – Restructures core, changes paradigms, migration needed

**Red Flags** (+score): “rewrite”, “refactor entire”, new framework for existing capability, changes across >5 files, breaking API changes, scope creep

**Green Flags** (-score): single file fix, uses existing utilities, follows established patterns, backward compatible, easily revertible

#### 5. Actionability (1-5)

Can it be resolved with a PR?

* **1: Not Actionable** – Question, discussion, duplicate, support request
* **2: Needs Triage** – Missing info, unclear scope, needs clarification
* **3: Needs Investigation** – Root cause unknown, requires debugging first
* **4: Ready to Work** – Clear scope, may need some design decisions
* **5: PR Ready** – Solution is clear, just needs implementation

**Blockers** (-score): questions, discussions, labels (duplicate, wontfix, question), missing repro

**Ready signals** (+score): action titles (`fix:`, `add:`), proposed solution, repro steps, good-first-issue label, specific files mentioned

Understanding the Adjusted Score
--------------------------------

The Adjusted Score is calculated by combining the four dimensions and applying penalties:

**Adjusted Score = (Difficulty + Importance) – (Tripping Scale + Architectural Impact – Actionability)**

Higher scores indicate issues that provide better ROI but may require more effort or carry more risk. Lower scores might represent quick wins with minimal complexity.

Practical Example
-----------------

Let’s say you’re analyzing a repository and find an issue about a crash in the authentication system:

* **Difficulty**: 7 (crash, security implications, multiple systems)
* **Importance**: 9 (critical – users can’t log in)
* **Tripping Scale**: 2 (proposed solution uses standard patterns)
* **Architectural Impact**: 3 (affects auth module but follows existing patterns)
* **Actionability**: 4 (clear repro steps, proposed solution)

**Adjusted Score** = (7 + 9) – (2 + 3 – 4) = 16 – 1 = 15

This would rank as a high-priority issue worth addressing immediately.

Best Practices
--------------

1. **Start broad, then narrow**: Use topic-based or search-based fetching to find relevant issues, then let the skill prioritize them.
2. **Consider contributor skill level**: Match issues to contributor experience based on difficulty and architectural impact.
3. **Look for quick wins**: Issues with high actionability and low difficulty are perfect for new contributors.
4. **Watch for red flags**: High tripping scale or architectural impact might indicate over-engineering.
5. **Validate assumptions**: Always ask “Is there a simpler way?” before accepting a proposed solution.

Conclusion
----------

The GitHub Issue Prioritizer skill provides a systematic approach to triaging and ranking issues based on their actual value and complexity. By considering ROI, solution sanity, architectural impact, and actionability, you can make informed decisions about which issues to tackle first and how to best utilize your team’s resources.

Remember: this is a read-only skill that analyzes and presents information. The final decision on what to work on always remains with you and your team.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/glucksberg/issue-prioritizer/SKILL.md>
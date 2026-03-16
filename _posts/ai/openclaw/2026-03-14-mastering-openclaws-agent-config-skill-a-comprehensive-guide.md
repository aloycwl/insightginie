---
layout: post
title: "Mastering OpenClaw&#8217;s Agent Config Skill: A Comprehensive Guide"
date: 2026-03-14T21:46:34
categories: [24854]
original_url: https://insightginie.com/mastering-openclaws-agent-config-skill-a-comprehensive-guide
---

Mastering OpenClaw's Agent Config Skill: A Comprehensive Guide
==============================================================

Learn how to effectively use the Agent Config Skill in OpenClaw to modify agent behavior and configuration files professionally.

---

OpenClaw's Agent Config Skill provides a structured and intelligent approach to modifying agent core context files. It ensures that changes are made to the right file, in the right format, without duplication or bloat, while respecting size limits and prompt engineering best practices. This guide will walk you through the core workflow and common patterns for effectively using this skill.

Core Workflow
-------------

When modifying agent context files, it's crucial to follow a systematic process to ensure changes are effective and maintainable. Here's the step-by-step workflow:

### 1. Identify Target File

Read the [file-map.md](https://github.com/openclaw/skills/blob/main/references/file-map.md) to determine which file the change belongs in. Use the quick decision tree:

* **Operational procedures, memory workflows, delegation rules** → `AGENTS.md`
* **Personality, tone, boundaries, ethical rules** → `SOUL.md`
* **Agent name, emoji, core vibe** → `IDENTITY.md`
* **User profile, preferences, family info** → `USER.md`
* **Local tool notes, command examples, API locations** → `TOOLS.md`
* **Curated long-term facts (main session only)** → `MEMORY.md`
* **Heartbeat checklist (keep tiny)** → `HEARTBEAT.md`

**Critical Note:** Subagents only see `AGENTS.md` and `TOOLS.md`. Operational rules must go in `AGENTS.md`, not `SOUL.md`.

### 2. Check Current State

Before making changes, perform the following checks:

* Check file size (20K char limit per file):

```
wc -c ~/clawd/AGENTS.md ~/clawd/SOUL.md ~/clawd/IDENTITY.md ~/clawd/USER.md ~/clawd/TOOLS.md ~/clawd/MEMORY.md ~/clawd/HEARTBEAT.md
```

* Read the target file section to check for duplication
* Use grep to search for existing similar content:

```
grep -i "keyword" ~/clawd/TARGETFILE.md
```

**Size warnings:**

* If file is > 18,000 chars, warn before adding (approaching truncation limit)
* If file is already > 20,000 chars, it's being truncated – refactor before adding more

**Agent can still read full file with `read` tool, but startup context is truncated.**

**Duplication check:**

* Is this instruction already present in different words?
* Is there a similar rule that should be updated instead of adding new?
* Does this belong in multiple files? (Usually no – pick ONE location)

### 3. Draft the Change

Read the [claude-patterns.md](https://github.com/openclaw/skills/blob/main/references/claude-patterns.md) for instruction formats that work.

**Format guidelines by file:**

* `AGENTS.md` (structured, imperative):

+ Use numbered processes for multi-step workflows
+ Use tables for decision trees, model selection, routing rules
+ Include examples for complex patterns
+ Explain WHY rules exist (motivation > bare commands)
+ Use headers and sub-sections for organization
+ Reference other files/skills, don't duplicate content

* `SOUL.md` (first-person OK, narrative):

+ Can use personal voice (“I'm Gus” vs “You are Gus”)
+ Anti-pattern lists work well (forbidden phrases, hedging examples)
+ Include before/after examples for tone guidance
+ Keep tattoos/anchors at top for immediate context
+ Use contrasts (good vs bad examples side-by-side)

* `IDENTITY.md` (minimal):

+ Punchy bullets
+ Keep under 500 chars if possible
+ Core vibe only, details go in `SOUL.md`

* `USER.md` (factual, third-person):

+ Bullet lists by category
+ Dates for time-sensitive info
+ Clear section headers
+ Cross-reference vault files for detailed project context

* `TOOLS.md` (reference guide):

+ Tables for comparison (when to use X vs Y)
+ Code blocks for command examples
+ Clear headings for quick lookup
+ Include paths, env var names, exact syntax

* `MEMORY.md` (wiki-style, topic-based):

+ Section by topic, not chronologically
+ Cross-reference entity files in vault
+ Dates for context, but organize by subject
+ Main session only – privacy-sensitive

* `HEARTBEAT.md` (action list):

+ Extremely concise
+ Bullet list of checks
+ No explanations (that's `AGENTS.md`)
+ Fast to parse

### 4. Validate Before Applying

Ask yourself:

* **Fit:** Does this actually belong in this file based on file-map.md? Is it operational (`AGENTS.md`) or personality (`SOUL.md`)? Will subagents need this? (If yes, must be `AGENTS.md` or `TOOLS.md`)
* **Format:** Does this match the file's existing style? Is it the right structure (numbered, table, bullets, prose)? Are examples included where needed?
* **Size:** How many chars is this adding? Is the file approaching 20K limit? Could this be a reference file instead?
* **Duplication:** Is this already present somewhere else? Should existing content be updated instead? Could this consolidate multiple scattered rules?
* **Quality:** Is motivation explained (WHY this rule exists)? Are examples concrete and real (not generic)? Is it precise enough for an AI to follow? Does it avoid vague instructions like “be helpful”?

### 5. Apply the Change

Use the `edit` tool with exact text matching:

```
# Read the section first to get exact text
exit("read", {
  "path": "/clawd/AGENTS.md",
  "offset": 50,
  "limit": 20
});

# Then edit with precise match
exit("edit", {
  "path": "~/clawd/AGENTS.md",
  "oldText": "exact existing text including whitespace",
  "newText": "updated text with change"
});
```

**For additions:**

* Find the right section anchor (read file first)
* Insert after relevant heading, not at end of file
* Maintain file's organization structure

**For updates:**

* Replace the specific section being changed
* Keep surrounding context intact
* Update examples if rule changes

**For deletions:**

* Only remove if truly obsolete
* Consider whether rule should be refined instead
* Check if other sections reference what's being deleted

### 6. Verify and Document

After applying change:

**Verification:**

```
# Confirm change applied
grep -A 3 "new text" ~/clawd/TARGETFILE.md

# Check new file size
wc -c ~/clawd/TARGETFILE.md
```

**Documentation:**

* Log significant changes to `/Users/macmini/Sizemore/agent/decisions/config-changes.md`
* Include: date, file, what changed, why, who requested
* If change is experimental, note rollback plan

**Report to user:**

* “Updated AGENTS.md: added X to Y section (now 15,234 chars)”
* If approaching limit: “Warning: AGENTS.md now 19,456 chars (near 20K limit)”
* If rolled back previous change: “Replaced old X rule with new Y approach”

Common Patterns
---------------

### Adding Safety Rules

**Target:** `AGENTS.md` → Safety section

```
## Safety
- **NEVER**: Exfiltrate data, destructive commands w/o asking
- Prefer `trash` > `rm`
- **New rule**: Brief description of what NOT to do
- **New protection**: When X happens, do Y instead
```

### Updating Delegation Rules

**Target:** `AGENTS.md` → Delegation section

Check existing delegation table/rules first. Update thresholds, model selection, or cost patterns.

### Refining Personality

**Target:** `SOUL.md` (tone, boundaries) or `IDENTITY.md` (core vibe)

Add forbidden phrases to anti-pattern list, update voice examples, refine mirroring rules.

### Adding Tool Conventions

**Target:** `TOOLS.md`

Add to relevant section (or create new section). Include code examples, when to use, paths.

### Updating Memory Workflow

**Target:** `AGENTS.md` → Memory section

Update logging triggers, recall cascade, entity structure. Keep memory format templates in `~/clawd/templates/`.

### Adding Startup Tasks

**Target:** `AGENTS.md` → Startup section

Add to numbered checklist. Keep conditional.

---

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/thatguysizemore/agent-config/SKILL.md>
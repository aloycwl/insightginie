---
layout: post
title: "Understanding OpenClaw Skills: A Comprehensive Guide"
date: 2026-03-14T06:17:12
categories: [24854]
original_url: https://insightginie.com/understanding-openclaw-skills-a-comprehensive-guide
---

What is an OpenClaw Skill?
--------------------------

An OpenClaw skill is a modular, self-contained package that extends agent capabilities by providing specialized knowledge, workflows, and tools. Think of skills as “onboarding guides” for specific domains or tasks—they transform a general-purpose agent into a specialized agent equipped with procedural knowledge and domain expertise.

Skill Location and Structure
----------------------------

In the Deepagents CLI, skills are stored in `~/.deepagents/<agent>/skills/` where `<agent>` is your agent configuration name (default is `agent`). Each skill consists of a required `SKILL.md` file and optional bundled resources:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation intended to be loaded into context as needed
    └── assets/           - Files used in output (templates, icons, fonts, etc.)
```

### SKILL.md Requirements

Every `SKILL.md` file must contain:

1. **Frontmatter**: YAML metadata with `name` and `description` fields. These fields determine when the skill gets triggered.
2. **Body**: Markdown instructions and guidance for using the skill. Only loaded AFTER the skill triggers.

Core Principles of Skill Design
-------------------------------

### Concise is Key

The context window is a public good. Skills share the context window with everything else the agent needs: system prompt, conversation history, other skills' metadata, and the actual user request. Default assumption: The agent is already very capable.

Only add context the agent doesn't already have. Challenge each piece of information: “Does the agent really need this explanation?” and “Does this paragraph justify its token cost?” Prefer concise examples over verbose explanations.

### Set Appropriate Degrees of Freedom

Match the level of specificity to the task's fragility and variability:

* **High freedom** (text-based instructions): Use when multiple approaches are valid, decisions depend on context, or heuristics guide the approach.
* **Medium freedom** (pseudocode or scripts with parameters): Use when a preferred pattern exists, some variation is acceptable, or configuration affects behavior.
* **Low freedom** (specific scripts, few parameters): Use when operations are fragile and error-prone, consistency is critical, or a specific sequence must be followed.

Bundled Resources
-----------------

### Scripts

Executable code (Python/Bash/etc.) for tasks that require deterministic reliability or are repeatedly rewritten. Include scripts when the same code is being rewritten repeatedly or deterministic reliability is needed.

**Example**: `scripts/rotate_pdf.py` for PDF rotation tasks

**Benefits**: Token efficient, deterministic, may be executed without loading into context

**Note**: Scripts may still need to be read by the agent for patching or environment-specific adjustments

### References

Documentation and reference material intended to be loaded as needed into context to inform the agent's process and thinking. Include references for documentation that the agent should reference while working.

**Examples**: `references/finance.md` for financial schemas, `references/mnda.md` for company NDA template, `references/policies.md` for company policies, `references/api_docs.md` for API specifications

**Use cases**: Database schemas, API documentation, domain knowledge, company policies, detailed workflow guides

**Benefits**: Keeps `SKILL.md` lean, loaded only when the agent determines it's needed

**Best practice**: If files are large (>10k words), include search patterns in `SKILL.md`

**Avoid duplication**: Information should live in either `SKILL.md` or references files, not both. Prefer references files for detailed information unless it's truly core to the skill—this keeps `SKILL.md` lean while making information discoverable without hogging the context window.

### Assets

Files not intended to be loaded into context, but rather used within the output the agent produces. Include assets when the skill needs files that will be used in the final output.

**Examples**: `assets/logo.png` for brand assets, `assets/slides.pptx` for PowerPoint templates, `assets/frontend-template/` for HTML/React boilerplate, `assets/font.ttf` for typography

**Use cases**: Templates, images, icons, boilerplate code, fonts, sample documents that get copied or modified

**Benefits**: Separates output resources from documentation, enables the agent to use files without loading them into context

What to Not Include in a Skill
------------------------------

A skill should only contain essential files that directly support its functionality. Do NOT create extraneous documentation or auxiliary files, including:

+ `README.md`
+ `INSTALLATION_GUIDE.md`
+ `QUICK_REFERENCE.md`
+ `CHANGELOG.md`
+ etc.

The skill should only contain the information needed for an AI agent to do the job at hand. It should not contain auxiliary context about the process that went into creating it, setup and testing procedures, user-facing documentation, etc. Creating additional documentation files just adds clutter and confusion.

Progressive Disclosure Design Principle
---------------------------------------

Skills use a three-level loading system to manage context efficiently:

1. **Metadata** (`name` + `description`): Always in context (~100 words)
2. **`SKILL.md` body**: When skill triggers (<5k words)
3. **Bundled resources**: As needed by the agent (Unlimited because scripts can be executed without reading into context window)

This progressive disclosure pattern ensures skills remain lightweight and efficient while providing comprehensive functionality when needed.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/chengxindl/skills-ttt/SKILL.md>
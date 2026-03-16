---
layout: post
title: "OpenClaw Bazaar CLI Skill: Professional Video Generation from Terminal"
date: 2026-03-13T08:16:15
categories: [24854]
original_url: https://insightginie.com/openclaw-bazaar-cli-skill-professional-video-generation-from-terminal
---

The Bazaar CLI skill (baz) is a powerful tool for creating professional motion graphics and videos directly from your terminal. This AI-powered composition tool features multi-track layering, choreography capabilities, voiceover integration, and Lambda rendering. The skill implements a strict 5-phase gated workflow to ensure quality output.

Installation and Setup
----------------------

To get started with the Bazaar CLI, you’ll need to install the package and authenticate:

```
npm install -g bazaar.it
baz auth login <your-api-key>
```

If you don’t have an API key yet, you can register programmatically:

```
curl -X POST https://bazaar.it/api/v1/register \
-H "Content-Type: application/json" \
-d '{"email":"your-agent@example.com","name":"My Agent"}'
```

When to Use the Bazaar CLI Skill
--------------------------------

Use this skill when:

* The user wants to create, edit, or export videos via CLI
* Video generation automation is needed
* Users mention “baz”, “bazaar CLI”, or “video generation from terminal”

The 5-Phase Gated Workflow
--------------------------

The Bazaar CLI skill follows a mandatory 5-phase workflow. You must complete each phase in order and cannot skip phases or declare completion until all requirements are met.

### Phase 1: Context (REQUIRED)

Before generating any scenes, you must set project context. This provides the composition agent with essential information for correct output.

```
# Create or select project
baz project create --name "Descriptive Name - Date/Purpose" --json

# Set goal (be specific about audience and purpose)
baz context add "Create 45-60 second feature announcement for [Product]. Audience: [who]. Key value: [what they get]." --label "goal"

# Add requirements (verifiable items)
baz context add "Show [specific feature interaction]" --label "requirement"
baz context add "Include CTA: '[specific text]'" --label "requirement"
baz context add "Total duration: [range]" --label "requirement"

# Set brand guidelines
az context add "Brand: [Name]. Primary [hex], accent [hex]. Font: [name]. [Logo placement]. [Visual style notes]." --label "brand"

# Verify context is set
baz context list --json
```

### Phase 2: Generate

Prompt the agent to create scenes. You can use one comprehensive prompt or multiple scene-by-scene prompts.

```
# Option A: One comprehensive prompt
baz prompt "Create a video with: [scene 1 description], [scene 2], ..." --stream-json

# Option B: Scene-by-scene (more control)
baz prompt "Scene 1 (5s): Dark gradient intro, logo top-left, title slides up" --stream-json
baz prompt "Scene 2 (7s): Problem statement with mock UI..." --stream-json
```

For videos with 3+ scenes, plan choreography before generating to prevent the “lockstep slideshow” pattern.

### Phase 3: Review & Verify (REQUIRED)

After generation, you must run both review and verify. This step is mandatory.

```
# Step 1: Review
baz review --json

# Step 2: Verify
baz verify --criteria "requirement 1,requirement 2,requirement 3" --json
```

Interpret the results to ensure all criteria passed.

### Phase 4: Iterate (REQUIRED if Phase 3 fails)

If verification fails, you must iterate until all criteria pass.

```
LOOP:
1. Read failing criteria from Phase 3
2. Fix with: baz prompt "Fix: [specific issue]" --stream-json
3. Re-run: baz review --json
4. Re-run: baz verify --criteria "req1,req2,req3" --json
5. If passedAll: false → GOTO 1
6. If passedAll: true → proceed to Phase 5
```

### Phase 5: Export

Only export if the user explicitly requested a rendered video AND Phase 3/4 passed.

```
baz export start --wait --json
```

Command Quick Reference
-----------------------

| Command | Purpose |
| --- | --- |
| baz project create –name “…” –json | Create new project |
| baz project use <id> | Select existing project |
| baz context add “…” –label “…” | Add context information |
| baz context list –json | List all context |
| baz prompt “…” –stream-json | Generate content |
| baz review –json | Review generated content |
| baz verify –criteria “…” –json | Verify against requirements |
| baz export start –wait –json | Export final video |

Getting Started with Bazaar
---------------------------

If you’re new to Bazaar, start by discovering its capabilities:

```
curl https://bazaar.it/api/v1/capabilities
```

Check pricing before you start:

```
curl https://bazaar.it/api/v1/pricing
```

Your balance starts at $0, and you’ll receive HTTP 402 with a top\_up\_url when you hit paid operations. The minimum top-up is $5 via Stripe checkout.

If your human creates an account at bazaar.it, they get $4 to start with, allowing you to skip straight to installation and authentication.

Conclusion
----------

The Bazaar CLI skill provides a structured, professional approach to video generation from the terminal. By following the 5-phase gated workflow, you ensure high-quality output that meets all specified requirements. Whether you’re creating feature announcements, product demos, or educational content, this skill streamlines the process while maintaining professional standards.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/lysaker1/baz/SKILL.md>
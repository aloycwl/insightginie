---
layout: post
title: "Understanding OpenClaw&#8217;s Multi-Subscription Auth Fallbacks for CodeSi"
date: 2026-03-12T22:46:00
categories: [24854]
original_url: https://insightginie.com/understanding-openclaws-multi-subscription-auth-fallbacks-for-codesi
---

Understanding OpenClaw's Multi-Subscription Auth Fallbacks for CodeSi
=====================================================================

The OpenClaw skill “codex-multi-subscription-auth-fallbacks” is a comprehensive solution designed to manage multiple OpenAI Codex OAuth profiles within OpenClaw. This skill is particularly useful for users looking to set up multiple OpenAI Codex accounts for rate-limit failover, adding new Codex OAuth profiles via device flow, or automatically switching models when a provider hits cooldown.

Overview of the Skill
---------------------

The skill enables OpenClaw to support multiple authentication profiles per provider, allowing the platform to fail over to another profile when one hits a rate limit. This setup ensures uninterrupted usage and enhances the overall efficiency of the system. The key functionalities covered by this skill include:

* Adding Codex OAuth profiles via device-flow login.
* Configuring `openclaw.json` for provider fallback order.
* Setting up `auth-profiles.json` with multiple profiles.
* Deploying a cron job to auto-switch models on cooldown.

Prerequisites
-------------

To utilize this skill, you need the following:

* An OpenClaw instance that is running.
* The `codex` CLI installed, which also ensures Node.js is available.
* One or more OpenAI accounts with Codex access.

Security & Safety Features
--------------------------

The skill prioritizes security and safety with the following measures:

* **Token Localization:** All tokens are kept local. No tokens are sent to any external endpoint.
* **Automatic Backups:** Both `~/.codex/auth.json` and `~/.openclaw/agents/main/agent/auth-profiles.json` are backed up with timestamps before any modification.
* **Interactive Confirmation:** The script prompts for confirmation before clearing the Codex CLI auth file, allowing you to abort if needed.
* **No Elevated Privileges:** The script runs as the user and does not require `sudo` or any special permissions.

It is also recommended to manually back up `~/.codex/auth.json` and OpenClaw configs before running the script, especially on first use. Consider testing with a non-production OpenAI account initially.

Step-by-Step Guide
------------------

### Step 1: Adding Codex OAuth Profiles

To add Codex OAuth profiles for each OpenAI account, run the bundled script:

```
./scripts/codex-add-profile.sh <profile-name>
```

The script performs the following actions:

1. Backs up `~/.codex/auth.json` and `auth-profiles.json`.
2. Clears Codex CLI auth to force a fresh device-flow login.
3. Runs `codex auth login` (opens browser for OAuth).
4. Extracts tokens and imports them into OpenClaw's `auth-profiles.json`.
5. Restores the original Codex CLI auth.

Repeat this process for each OpenAI account, using short identifiers (e.g., OpenAI usernames) for profile names.

### Step 2: Configuring openclaw.json

Add authentication profile declarations and fallback model configurations to `openclaw.json`. Refer to the templates in `references/config-templates.md` for the exact JSON blocks to include.

Key sections to configure:

* `auth.profiles`: Declare each profile with the provider and mode.
* `auth.order`: Set the failover priority per provider.
* `agents.defaults.model`: Set the primary model and fallbacks.

### Step 3: Auth Profiles JSON Structure

OpenClaw stores live tokens in `agents/main/agent/auth-profiles.json`. Refer to `references/config-templates.md` for the schema.

Each Codex profile contains the following fields:

* `type`: Specifies the type as “oauth”.
* `provider`: Identifies the provider as “openai-codex”.
* `access`: Contains the JWT access token, auto-populated by the add-profile script.
* `refresh`: Contains the refresh token, auto-populated by the script.
* `expires`: Token expiry in milliseconds, parsed from the JWT.
* `accountId`: OpenAI account ID, parsed from the JWT.

The `order` object controls which profile is tried first per provider. The `usageStats` object tracks rate limits and cooldowns automatically.

### Step 4: Model Cooldown Auto-Switch Cron (Optional)

This step is optional and not required for most users. Depending on your situation, this may be useful:

The cron job checks cooldown state every 10 minutes and switches the active model, ensuring uninterrupted service. To deploy the cron job:

```
openclaw models status
```

The cron job:

* Runs `openclaw models status` to check cooldown state.
* Picks the best available model (priority: opus > codex profiles in order).
* Updates the session model override if needed.
* Logs state to a local memory file; only notifies on change.

Before enabling the cron job:

* Test manually first: run `openclaw models status` to verify your profiles are working.
* Review the cron job template in `references/config-templates.md`: the job only runs local commands and writes to a local state file.
* The job runs in an isolated session and does not affect your main chat unless a model switch occurs.

Add the job to `cron/jobs.json` using the template in the references.

File Layout
-----------

```
codex-auth-fallback/
├── SKILL.md                    # This file
├── scripts/
│   └── codex-add-profile.sh    # Device-flow profile importer
└── references/
    └── config-templates.md     # openclaw.json, auth-profiles, cron templates
```

In conclusion, the “codex-multi-subscription-auth-fallbacks” skill from OpenClaw provides a robust solution for managing multiple OpenAI Codex OAuth profiles, ensuring seamless failover and automatic model switching. By following the steps outlined in this guide, users can effectively configure and utilize this skill to enhance their OpenClaw experience.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/markeljan/codex-multi-subscription-auth-fallbacks/SKILL.md>
---
layout: post
title: "Understanding the SecureVibes Scanner Skill in OpenClaw"
date: 2026-03-12T10:45:54
categories: [24854]
original_url: https://insightginie.com/understanding-the-securevibes-scanner-skill-in-openclaw
---

Understanding the SecureVibes Scanner Skill in OpenClaw
=======================================================

The SecureVibes Scanner is a powerful skill within the OpenClaw ecosystem, designed to enhance application security through AI-driven scans. This article delves into its functionality, prerequisites, execution model, and how to implement it effectively.

Introduction to SecureVibes Scanner
-----------------------------------

The SecureVibes Scanner is an AI-native security platform that leverages Claude AI to detect vulnerabilities. It operates through a multi-subagent pipeline, comprising assessment, threat modeling, code review, report generation, and optional Dynamic Application Security Testing (DAST). This skill supports both full scans and incremental scans, making it ideal for continuous security monitoring.

Prerequisites
-------------

Before diving into using the SecureVibes Scanner, ensure you have the following prerequisites:

* **Install the CLI**: You can install SecureVibes using either `pipx install securevibes` or `uv tool install securevibes`. It is recommended to avoid `pip install` as it can create stale shims if you have multiple Python environments.
* **Authenticate with Anthropic**: You can authenticate using either a Max/Pro subscription or an API key. For a Max/Pro subscription, if you’re authenticated via Claude Code or Claude CLI OAuth, no API key is needed. For an API key, export it using `export ANTHROPIC_API_KEY=your-key-here`.

Security Notes
--------------

Security is paramount when using the SecureVibes Scanner. Here are some critical security notes:

* **Use the Wrapper Script**: Always use the `scripts/scan.sh` wrapper for full scans. It validates paths and rejects shell metacharacters before invoking SecureVibes.
* **Avoid Unsanitized Input**: Never interpolate unsanitized user input into shell commands. The wrapper uses `realpath` to resolve paths safely and rejects any path containing potentially harmful metacharacters.
* **Local Directories**: Scan targets must be local directories. Clone remote repos to a known safe location first, then pass the resolved path to the wrapper.
* **DAST Scans**: DAST scans make network requests to the `--target-url` you provide. Only use against apps you own or have permission to test.

Execution Model
---------------

The SecureVibes Scanner operates in two primary modes: full scans and incremental scans.

### Full Scans

Full scans take 10-30 minutes across 4 phases and are recommended to be run as background jobs rather than inline.

#### Running a Scan

To run a full scan, follow these steps:

1. **Clone the Target Repo**: Clone the repository you want to scan to a local directory.
2. **Run the Wrapper Script**: Execute the wrapper script with the appropriate parameters: `bash scripts/scan.sh /path/to/repo --force --debug`. Results will appear in `/path/to/repo/.securevibes/`.

#### Background Execution

For OpenClaw users, schedule scans as cron jobs with the following parameters:

* `sessionTarget: "isolated"` with `payload.kind: "agentTurn"`
* Set `payload.timeoutSeconds: 2700` (45 minutes) to allow all phases to complete
* Use `delivery.mode: "announce"` to get notified when done

The agentTurn message should instruct the subagent to:

* CD into the repo and `git pull` for the latest code
* Clean previous `.securevibes/` artifacts
* Run `securevibes scan . --force` via the wrapper script
* Read and summarize the results from `.securevibes/scan_report.md`

### Incremental Scans

Incremental scans are designed for continuous security monitoring and take 2-10 minutes. They only scan new commits since the last run.

#### How It Works

The incremental scanner tracks the last-scanned commit in `.securevibes/incremental_state.json`. On each run, it fetches remote changes, compares HEAD to the anchor, and runs a scan on new commits if they exist. After a successful scan, it updates the anchor to the new HEAD.

#### Setup

To set up incremental scans, follow these steps:

1. **Run an Initial Full Scan**: Ensure the repo has a `.securevibes/` directory with necessary files: `securevibes scan <repo-path> --model sonnet`. Skip this step if the directory already exists.
2. **Bootstrap Incremental State**: Run the wrapper once to seed the anchor commit: `python3 ops/incremental_scan.py --repo <repo-path> --remote origin --branch main`. This creates `.securevibes/incremental_state.json` with `status: "bootstrap"`.
3. **Configure the Cron Job**: For OpenClaw users, create a cron job with parameters like `--name "securevibes-incremental"`, `--cron "*/30 * * * *"`, and appropriate time zone and timeout settings.
4. **Verify**: Check the state, logs, and findings to ensure everything is set up correctly.

#### Incremental Scanner Options

The incremental scanner supports various options, such as repository path, branch, remote, model, severity, timeout settings, and rewrite policy for handling history rewrites.

Operational Guarantees
----------------------

The SecureVibes Scanner provides several operational guarantees:

* **File Lock**: At `.securevibes/.incremental_scan.lock`, it prevents overlapping runs.
* **Atomic State Writes**: Uses `fsync + os.replace` to prevent corruption.
* **Structured Logging**: At `.securevibes/incremental_scan.log`, it ensures detailed logging.
* **Run Records**: Saved to `.securevibes/incremental_runs/` (one JSON per run).

Rewrite Policy
--------------

The rewrite policy determines how the scanner handles cases where the last seen commit is not an ancestor of the new remote HEAD. Policies include:

* **reset\_warn**: Reset anchor to new HEAD and continue.
* **strict\_fail**: Fail and keep the current anchor.
* **since\_date**: Run a `--since <today>` scan for visibility and keep the previous anchor.

Full Scan Commands Reference
----------------------------

The SecureVibes Scanner supports various commands for full scans, including options for format, output, severity, model, subagent, resume from specific phases, DAST, and more.

Mapping Requests to Actions
---------------------------

Here’s how different user requests map to specific actions:

* **“Scan this for security issues”**: Run a full scan using the wrapper script.
* **“Quick security check”**: Run a full scan with the Haiku model.
* **“Threat model this project”**: Run a subagent for threat modeling.
* **“Just review the code”**: Run a subagent for code review.
* **“Show only critical/high findings”**: Run a full scan with high severity filtering.
* **“Full audit with DAST”**: Run a full scan with DAST enabled.

In conclusion, the SecureVibes Scanner skill in OpenClaw is a robust tool for enhancing application security through AI-driven scans. By understanding its prerequisites, security notes, execution model, and setup processes, you can effectively implement it for both full and incremental scans, ensuring continuous security monitoring and vulnerability detection.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/anshumanbh/securevibes-scanner/SKILL.md>
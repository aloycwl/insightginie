---
layout: post
title: "Explaining OpenClaw&#8217;s Canary Skill: A Comprehensive Guide to Secret Leak Detection"
date: 2026-03-13T09:47:10
categories: [24854]
original_url: https://insightginie.com/explaining-openclaws-canary-skill-a-comprehensive-guide-to-secret-leak-detection
---

Explaining OpenClaw’s Canary Skill: A Comprehensive Guide to Secret Leak Detection
==================================================================================

In today's digital landscape, safeguarding sensitive information such as API keys, tokens, and credentials is paramount. OpenClaw's Canary skill is designed to be your early warning system, diligently scanning your environment for any exposed secrets. This comprehensive guide will illuminate the functionality, detection methods, and auto-fix capabilities of the Canary skill.

Understanding OpenClaw’s Canary Skill
-------------------------------------

The Canary skill is a powerful tool that operates in two distinct modes: Light Scan and Deep Scan. Let's delve into each of these modes and understand how they contribute to protecting your environment.

### Light Scan: The Automatic Check

Every time OpenClaw starts, the Light Scan mode kicks into action. This mode performs a swift and silent check of critical locations:

* '~/.openclaw/.env' and '~/.clawdbot/.env' for plaintext credentials
* File permissions on config files containing secrets (world-readable = bad)
* Any .env files in the active workspace

If everything checks out, Canary remains silent, ensuring a smooth and uninterrupted operation. However, if any issues are detected, Canary will display a short alert, providing the option to fix the problem or obtain more details.

### Deep Scan: The Comprehensive Check

The Deep Scan mode can be manually triggered whenever you desire a thorough security check. This mode covers everything checked in the Light Scan and extends to:

* All installed skill directories for hardcoded secrets
* Session/chat history files for accidentally pasted credentials
* Git repositories in the workspace for committed secrets
* SSH keys and config (~/.ssh/) for weak permissions
* Shell history files for commands containing tokens or passwords
* Known credential file paths (.netrc, .npmrc, .pypirc, Docker config, AWS credentials, etc.)

Detecting Secrets: What Canary Looks For
----------------------------------------

Canary employs pattern matching and heuristic checks to identify various types of secrets. Let's explore the different secret types, examples, and the locations where Canary looks for them.

![Secret Type, Examples, and Locations](https://example.com/image1./media/images/jpg)

### Secret Type

The following table provides an overview of the secret types Canary can detect:

| Secret Type | Examples | Where It Looks |
| --- | --- | --- |
| API Keys | Shodan, VirusTotal, OpenAI, Anthropic, AWS, GCP, Stripe, GitHub tokens | .env files, skill configs, shell history, git repos |
| Passwords | Plaintext passwords in configs, database connection strings with embedded passwords | Config files, .env, .netrc, skill directories |
| Private Keys | SSH private keys, PEM files, JWTs with embedded secrets | ~/.ssh/, workspace, skill directories |
| Cloud Credentials | AWS access keys, GCP service account JSON, Azure tokens | ~/.aws/, ~/.config/gcloud/, env vars, configs |
| Tokens & Sessions | OAuth tokens, bearer tokens, session cookies, webhook URLs | Chat history, shell history, .env files |
| Local System Files | Credential exports, service account JSONs, PEM/key files, password manager CSV exports, Kubernetes tokens, Terraform state secrets, database passwords | ~/Downloads/, ~/Desktop/, ~/Documents/, ~/.kube/config, \*.tfstate, ~/.config/, ~/Library/Application Support/, ~/.my.cnf, ~/.pgpass, browser password export CSVs, Redis/MongoDB configs |

The image below illustrates the secret types, examples, and locations where Canary looks for them.

Severity Levels: Prioritizing Your Security
-------------------------------------------

Each finding in the Canary scan is assigned a clear severity level to help you prioritize your security efforts:

* '’tissues found': First time Canary runs: show a brief all-clear so the user knows it's active. Example: 'ðŸ�¦ Canary checked your environment â€” everything looks clean.'
* '’issues found': display a single line with the total count of issues found, allowing users to take immediate action.

Auto-Fix: Streamlining Your Security Efforts
--------------------------------------------

Canary’s auto-fix feature is designed to streamline your security efforts by automatically addressing identified issues. However, it’s essential to note the following:

* Canary will never change, move, or delete anything on your system without your explicit confirmation.
* Every auto-fix is shown to you in full before it happens. You can always say no, and Canary will provide a step-by-step guide to address the issue manually.

### Issue Resolution: What Canary Will Do (with your OK)

Canary offers seamless solutions to common issues, making the process of securing your environment a breeze. Let’s explore some of these auto-fixes:

* 'Your .env file can be read by other users on this machine': Make the file private to your account only.
* 'Secret pasted in your shell history': Remove that one line from your history.
* 'SSH key file isn't locked down': Restrict the key file to your account only.
* 'API key hardcoded inside a skill': Move the key to your .env file and reference it from there.
* 'Secret committed to a git repo': Add the file to .gitignore so it won't be shared again.
* 'Credential file sitting in Downloads/Desktop/Documents': Move the file to a secure location with private permissions.
* 'Kubernetes config with embedded tokens is too open': Make the config file private to your account.
* 'Terraform state file with plaintext secrets': Flag and restrict file permissions.
* 'Database config with embedded password': Restrict the config file to your account only.
* 'Browser password export CSV left unprotected': Move to a secure location or securely delete.

Backup Security: Ensuring Data Integrity
----------------------------------------

Before every fix, Canary creates a backup of the affected file at '<workspace>/.

* 'Canary, undo that last fix'
* 'Restore my .env file'

Backup security is paramount to Canary. Here's how Canary ensures the safety of your backups:

* Backups are encrypted at rest using a key derived from the machine's unique identifier. They cannot be read by simply opening the file â€” only Canary's rollback process can decrypt them.
* Canary <i>never</i> scans its own backup directory. The path /backups/ is permanently excluded from all scans to avoid false feedback loops where Canary re-flags the secrets it just backed up.
* The backup directory is created with owner-only permissions (700). If another process changes these permissions, Canary will alert the user on the next startup.
* Backups older than 7 days are securely deleted (overwritten before removal) rather than simply unlinked.

Instructions for the Agent: A Step-by-Step Guide
------------------------------------------------

As the Canary security skill, your primary responsibility is to protect the user's secrets and credentials. Here's a step-by-step guide on how to perform a Light Scan on startup:

1. 'On Startup (Light Scan)': Silently check these locations: '~/.openclaw/.env', '~/.clawdbot/.env', and any '.env' in the current workspace.
2. 'File permissions on all config files found above'
3. 'If no issues found':

1. First time Canary runs: show a brief all-clear so the user knows it's active. Example: 'ðŸ�¦ Canary checked your environment â€” everything looks clean.'- Every startup after that: stay silent. No news is good news.

4. 'If issues found': display a single line with the total count of issues found, allowing users to take immediate action.

Conclusion: Embrace Security with OpenClaw’s Canary Skill
---------------------------------------------------------

In conclusion, OpenClaw's Canary skill is an indispensable tool for anyone seeking to fortify their environment against the inadvertent exposure of sensitive data. By operating in Light Scan and Deep Scan modes, Canary ensures comprehensive coverage, helping you identify and address potential vulnerabilities proactively. Embrace the power of Canary to elevate your security posture and safeguard your digital assets with ease and confidence.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/sukiraman/canary/SKILL.md>
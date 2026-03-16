---
layout: post
title: "GuavaGuard: Runtime Security Scanner for OpenClaw Agents"
date: 2026-03-16T06:15:36
categories: [24854]
original_url: https://insightginie.com/guavaguard-runtime-security-scanner-for-openclaw-agents
---

What GuavaGuard Does
--------------------

GuavaGuard is a runtime security guard and scanner specifically designed for OpenClaw agents. It functions as part of the guard-scanner ecosystem, providing real-time detection of security threats including reverse shells, credential theft attempts, and sandbox escapes. While guard-scanner handles static analysis before installation, GuavaGuard monitors tool calls during execution to catch threats that emerge at runtime.

Core Security Features
----------------------

The tool monitors 12 critical security patterns in real-time, categorized by severity levels. Critical threats include reverse shell attempts using patterns like /dev/tcp/, nc -e, and socat TCP; credential exfiltration to services like webhook.site and ngrok; guardrail disabling attempts such as exec.approval = off; macOS Gatekeeper bypasses using xattr -d quarantine; ClawHavoc AMOS indicators; and various shell injection techniques including base64 -d | bash and curl | bash patterns.

Installation and Setup
----------------------

Getting started requires installing both components of the security suite. First, install the full static scanner with clawhub install guard-scanner, which provides 150+ patterns across 23 categories. Then install the runtime monitor using clawhub install guava-guard. Before enabling runtime protection, run a pre-install safety check with npx guard-scanner ./skills –self-exclude –verbose to scan your skills directory.

Runtime Protection Configuration
--------------------------------

Enable the runtime hook by running openclaw hooks install skills/guava-guard/hooks/guava-guard followed by openclaw hooks enable guava-guard. After restarting your gateway, verify the installation with openclaw hooks list, which should show the guava-guard hook as ready. All detections are logged to ~/.openclaw/guava-guard/audit.jsonl in JSON lines format for audit trail purposes.

Detection Categories
--------------------

Beyond critical threats, GuavaGuard also monitors high-severity patterns including DNS exfiltration attempts using nslookup and dig commands, SSH key access attempts targeting .ssh/id\_\* and .ssh/authorized\_keys files, and cryptocurrency wallet access attempts looking for wallet seeds, mnemonics, or seed phrases. The tool also detects cloud metadata SSRF attacks targeting 169.254.169.254 and connections to known malicious IP addresses like 91.92.242.30.

Two-Layer Defense Strategy
--------------------------

GuavaGuard represents the runtime half of a comprehensive two-layer security defense. The static layer, guard-scanner, analyzes skills before installation using 150+ patterns and provides HTML dashboards, SARIF, and JSON output. The runtime layer, guava-guard, monitors execution with 12 specialized patterns. Together they provide defense-in-depth security, with guard-scanner achieving top ClawHub search ranking and over 4,000 downloads.

Current Limitations and Future Plans
------------------------------------

Due to OpenClaw’s current hook API limitations, GuavaGuard can only warn about detected threats rather than blocking them outright. The tool will automatically enable blocking capabilities when OpenClaw adds cancel API support. Users can track this development through Issue #18677. Despite this limitation, the warning system provides crucial visibility into potential security breaches during agent operation.

License and Dependencies
------------------------

GuavaGuard is released under the MIT license with zero dependencies, making it lightweight and easy to integrate. The tool is developed by the Guava Parity Institute (GPI) as part of their ASI×Human Perfect Parity initiative. For comprehensive protection, users should install both guard-scanner and guava-guard through ClawHub, creating a robust security framework for OpenClaw agent deployment.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/koatora20/guava-guard/SKILL.md>
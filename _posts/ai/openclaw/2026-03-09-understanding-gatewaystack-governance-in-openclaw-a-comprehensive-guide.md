---
layout: post
title: "Understanding GatewayStack Governance in OpenClaw: A Comprehensive Guide"
date: 2026-03-09T01:45:50
categories: [24854]
original_url: https://insightginie.com/understanding-gatewaystack-governance-in-openclaw-a-comprehensive-guide
---

The [**GatewayStack Governance**](https://github.com/openclaw/skills/tree/main/skills/davidcrowe/gatewaystack-governance) skill in OpenClaw is a powerful tool designed to provide "deny-by-default" governance for every tool call. It integrates into the OpenClaw process level, ensuring that the agent cannot bypass it. In this guide, we will explore what this skill does, its core features, and how it can be installed and customized.

**GatewayStack Governance** is primarily focused on ensuring secure and controlled tool usage. It achieves this through five core checks that run automatically on every invocation:

1. **Identity** – Maps the agent to a policy role. Agents that are not recognized are automatically denied.
2. **Scope** – A deny-by-default tool allowlist that blocks any unlisted tools.
3. **Rate Limiting** – Implements per-user and per-session sliding window limits to control tool usage.
4. **Injection Detection** – Uses 40+ patterns from Cisco, Snyk, and Kaspersky research to identify and prevent potential injection attacks.
5. **Audit Logging** – Logs every decision in an append-only JSONL format for thorough record-keeping.

Additionally, **GatewayStack Governance** offers three opt-in features that further extend governance:

1. **Output DLP** – Scans tool output for Personally Identifiable Information (PII) using the @gatewaystack/transformabl-core package. This feature allows for the logging or redacting of sensitive information.
2. **Escalation** – Provides human-in-the-loop review for medium-severity detections and first-time tool use, ensuring human oversight when necessary.
3. **Behavioral Monitoring** – Uses the @gatewaystack/limitabl-core package to detect anomalous tool usage patterns.

To get started with **GatewayStack Governance**, installation is simple. You can install it with a single command:

```
openclaw plugins install @gatewaystack/gatewaystack-governance
```

This command enables the core five checks on every tool call immediately, with zero configuration required. The plugin hooks into the before\_tool\_call process level, preventing agents from bypassing or circumnavigating the checks.

Customizing the plugin is also straightforward. To override the default settings, create a policy file:

```
cp ~/openclaw/plugins/gatewaystack-governance/policy.example.json ~/openclaw/plugins/gatewaystack-governance/policy.json
```

Here, you can configure which tools are allowed, who can use them, rate limits, injection detection sensitivity, and the optional features (DLP, escalation, behavioral monitoring). Note that these optional features are disabled by default.

**GatewayStack Governance** offers three optional packages via lazy import, allowing you to install only what you need:

* npm install @gatewaystack/transformabl-core for output Data Loss Prevention (DLP).
* npm install @gatewaystack/limitabl-core for behavioral monitoring.

The core five checks have zero external dependencies and can operate without these packages, making the plugin highly modular and adaptable to your needs.

The GatewayStack Governance skill is licensed under the MIT License. You can find additional resources and documentation on the [**GitHub**](https://github.com/davidcrowe/openclaw-gatewaystack-governance) page, as well as the [**npm**](https://www.npmjs.com/package/@gatewaystack/gatewaystack-governance) package registry.

In summary, **GatewayStack Governance** in OpenClaw offers a robust solution for managing tool calls, providing automatic and configurable checks to ensure secure and controlled usage. By understanding and utilizing the features it offers, you can enhance the security and governance of your tools effectively.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/davidcrowe/gatewaystack-governance/SKILL.md>
---
layout: post
title: 'Understanding GatewayStack Governance in OpenClaw: A Comprehensive Guide'
date: '2026-03-09T01:45:50'
categories:
- ai
- openclaw
original_url: https://insightginie.com/understanding-gatewaystack-governance-in-openclaw-a-comprehensive-guide/
featured_image: /media/images/8153.jpg
---

<p>The <a href="https://github.com/openclaw/skills/tree/main/skills/davidcrowe/gatewaystack-governance"><strong>GatewayStack Governance</strong></a> skill in OpenClaw is a powerful tool designed to provide &quot;deny-by-default&quot; governance for every tool call. It integrates into the OpenClaw process level, ensuring that the agent cannot bypass it. In this guide, we will explore what this skill does, its core features, and how it can be installed and customized.</p>
<p><strong>GatewayStack Governance</strong> is primarily focused on ensuring secure and controlled tool usage. It achieves this through five core checks that run automatically on every invocation:</p>
<ol>
<li><strong>Identity</strong> &#8211; Maps the agent to a policy role. Agents that are not recognized are automatically denied.</li>
<li><strong>Scope</strong> &#8211; A deny-by-default tool allowlist that blocks any unlisted tools.</li>
<li><strong>Rate Limiting</strong> &#8211; Implements per-user and per-session sliding window limits to control tool usage.</li>
<li><strong>Injection Detection</strong> &#8211; Uses 40+ patterns from Cisco, Snyk, and Kaspersky research to identify and prevent potential injection attacks.</li>
<li><strong>Audit Logging</strong> &#8211; Logs every decision in an append-only JSONL format for thorough record-keeping.</li>
</ol>
<p>Additionally, <strong>GatewayStack Governance</strong> offers three opt-in features that further extend governance:</p>
<ol>
<li><strong>Output DLP</strong> &#8211; Scans tool output for Personally Identifiable Information (PII) using the @gatewaystack/transformabl-core package. This feature allows for the logging or redacting of sensitive information.</li>
<li><strong>Escalation</strong> &#8211; Provides human-in-the-loop review for medium-severity detections and first-time tool use, ensuring human oversight when necessary.</li>
<li><strong>Behavioral Monitoring</strong> &#8211; Uses the @gatewaystack/limitabl-core package to detect anomalous tool usage patterns.</li>
</ol>
<p>To get started with <strong>GatewayStack Governance</strong>, installation is simple. You can install it with a single command:</p>
<pre>openclaw plugins install @gatewaystack/gatewaystack-governance</pre>
<p>This command enables the core five checks on every tool call immediately, with zero configuration required. The plugin hooks into the before_tool_call process level, preventing agents from bypassing or circumnavigating the checks.</p>
<p>Customizing the plugin is also straightforward. To override the default settings, create a policy file:</p>
<pre>cp ~/openclaw/plugins/gatewaystack-governance/policy.example.json ~/openclaw/plugins/gatewaystack-governance/policy.json</pre>
<p>Here, you can configure which tools are allowed, who can use them, rate limits, injection detection sensitivity, and the optional features (DLP, escalation, behavioral monitoring). Note that these optional features are disabled by default.</p>
<p><strong>GatewayStack Governance</strong> offers three optional packages via lazy import, allowing you to install only what you need:</p>
<ul>
<li>npm install @gatewaystack/transformabl-core for output Data Loss Prevention (DLP).</li>
<li>npm install @gatewaystack/limitabl-core for behavioral monitoring.</li>
</ul>
<p>The core five checks have zero external dependencies and can operate without these packages, making the plugin highly modular and adaptable to your needs.</p>
<p>The GatewayStack Governance skill is licensed under the MIT License. You can find additional resources and documentation on the <a href="https://github.com/davidcrowe/openclaw-gatewaystack-governance"><strong>GitHub</strong></a> page, as well as the <a href="https://www.npmjs.com/package/@gatewaystack/gatewaystack-governance"><strong>npm</strong></a> package registry.</p>
<p>In summary, <strong>GatewayStack Governance</strong> in OpenClaw offers a robust solution for managing tool calls, providing automatic and configurable checks to ensure secure and controlled usage. By understanding and utilizing the features it offers, you can enhance the security and governance of your tools effectively.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/davidcrowe/gatewaystack-governance/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/davidcrowe/gatewaystack-governance/SKILL.md</a></p>

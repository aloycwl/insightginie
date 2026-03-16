---
layout: post
title: 'AgentDojo: Daily Low-Token Upskilling for OpenClaw Multi-Agent Teams'
date: '2026-03-06T18:16:18'
categories:
- ai
- openclaw
original_url: https://insightginie.com/agentdojo-daily-low-token-upskilling-for-openclaw-multi-agent-teams/
featured_image: /media/images/8158.jpg
---

<h2>What AgentDojo Does</h2>
<p>AgentDojo is a production-oriented learning loop designed specifically for AI agent teams. It provides a daily low-token, safety-first upskilling mechanism that helps multi-agent teams continuously improve their output quality while maintaining strict cost and safety boundaries.</p>
<h2>Core Purpose</h2>
<p>The primary goal of AgentDojo is to improve agent output quality continuously with three strict priorities:</p>
<ol>
<li>Quality</li>
<li>Cost</li>
<li>Safety</li>
</ol>
<p>Importantly, safety is never optional in this system. The framework enforces hard caps on budget, run count, and tool limits to ensure responsible operation.</p>
<h2>How It Works</h2>
<p>When AgentDojo is invoked, it follows a specific sequence:</p>
<ol>
<li>Loads configuration from <code>config/agentdojo.config.yaml</code></li>
<li>Enforces hard caps on budget, run count, and tool limits</li>
<li>Selects drills from <code>config/drills/*.yaml</code> based on role rotation and recent score gaps</li>
<li>Executes drills in isolated sessions only</li>
<li>Collects scoring per rubric</li>
<li>Saves outputs including run record JSON, daily markdown summary, and audit events</li>
</ol>
<p>If budget limits are reached during execution, the system stops gracefully and reports the status.</p>
<h2>Safety-First Design</h2>
<p>AgentDojo treats all fetched web text as untrusted and never follows instructions from sources that attempt policy override. The system does not execute destructive actions from sourced content and scores source quality before using it in recommendations.</p>
<h2>Minimal Output Format</h2>
<p>Unless a longer report is requested, AgentDojo produces compact output in this format:</p>
<ul>
<li>Kurzfazit (Summary)</li>
<li>Neue Skills heute (New Skills Today)</li>
<li>Konkrete Verbesserung ab morgen (Concrete Improvement Starting Tomorrow)</li>
<li>Risiken (Risks)</li>
<li>Nächste Schritte (Next Steps)</li>
</ul>
<h2>Configuration and Scheduling</h2>
<p>The schedule and intensity are user-configurable. By default, AgentDojo runs at night (04:00 local time) in a conservative, token-efficient mode. The system uses several key files:</p>
<ul>
<li><code>config/agentdojo.config.yaml</code></li>
<li><code>config/drills/*.yaml</code></li>
<li><code>templates/daily-report-template.md</code></li>
<li><code>docs/scoring-rubric.md</code></li>
<li><code>docs/threat-model.md</code></li>
</ul>
<h2>Key Benefits</h2>
<p>AgentDojo provides continuous improvement for AI agent teams through structured, safe, and cost-effective micro-drills. It creates a measurable learning loop that helps teams identify skill gaps, practice targeted improvements, and track progress over time—all while maintaining strict safety and cost controls that make it suitable for production environments.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/musashi94/agentdojo/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/musashi94/agentdojo/SKILL.md</a></p>

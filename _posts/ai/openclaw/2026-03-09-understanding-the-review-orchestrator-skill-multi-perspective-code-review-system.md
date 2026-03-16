---
layout: post
title: 'Understanding the Review Orchestrator Skill: Multi-Perspective Code Review
  System'
date: '2026-03-09T08:17:17'
categories:
- ai
- openclaw
original_url: https://insightginie.com/understanding-the-review-orchestrator-skill-multi-perspective-code-review-system/
featured_image: /media/images/8153.jpg
---

<h2>What This Solves</h2>
<p>One perspective has blind spots. This skill coordinates multiple review perspectives to catch what single-pass review misses:</p>
<ul>
<li>Twin review &#8211; technical and creative perspectives for balance</li>
<li>Cognitive modes &#8211; analyzer (&#8220;what conflicts&#8221;), architect (&#8220;how to restructure&#8221;), implementer (&#8220;how to implement&#8221;)</li>
</ul>
<p>The insight: N=2 catches more than N=1. Different perspectives see different things. Coordinate them systematically.</p>
<h2>Core Logic</h2>
<p>The Review Orchestrator uses intelligent selection based on context and risk level:</p>
<table>
<thead>
<tr>
<th>Context</th>
<th>Risk</th>
<th>Recommended Review</th>
</tr>
</thead>
<tbody>
<tr>
<td>Implementation</td>
<td>Low</td>
<td>/ro twin &#8211;technical-only</td>
</tr>
<tr>
<td>Implementation</td>
<td>Medium</td>
<td>/ro twin (both perspectives)</td>
</tr>
<tr>
<td>Implementation</td>
<td>High</td>
<td>/ro twin + /ro cognitive</td>
</tr>
<tr>
<td>Architecture</td>
<td>Any</td>
<td>/ro cognitive</td>
</tr>
<tr>
<td>Documentation</td>
<td>Any</td>
<td>/ro twin &#8211;creative-only</td>
</tr>
<tr>
<td>Security</td>
<td>Any</td>
<td>/ro cognitive + external review</td>
</tr>
</tbody>
</table>
<h2>Multi-Perspective Review</h2>
<p>The system provides different analytical perspectives:</p>
<h3>Technical Perspective</h3>
<ul>
<li>Focus: Architecture, standards, patterns, security</li>
<li>Japanese: 技術</li>
</ul>
<h3>Creative Perspective</h3>
<ul>
<li>Focus: UX, communication, philosophy alignment</li>
<li>Japanese: 創造</li>
</ul>
<h3>Cognitive Modes</h3>
<p>These provide different analytical approaches:</p>
<table>
<thead>
<tr>
<th>Mode</th>
<th>Perspective</th>
<th>Focus</th>
<th>Japanese</th>
</tr>
</thead>
<tbody>
<tr>
<td>analyzer</td>
<td>&#8220;Here&#8217;s what conflicts&#8221;</td>
<td>Tensions, trade-offs, contradictions</td>
<td>審碼</td>
</tr>
<tr>
<td>architect</td>
<td>&#8220;Here&#8217;s how to restructure&#8221;</td>
<td>Architecture, patterns, organization</td>
<td>審構</td>
</tr>
<tr>
<td>implementer</td>
<td>&#8220;Here&#8217;s how to implement&#8221;</td>
<td>Concrete steps, complexity, path forward</td>
<td>審實</td>
</tr>
</tbody>
</table>
<h2>Quality Gate Configuration</h2>
<p>The system includes configurable quality gates with these checks:</p>
<ul>
<li>Tests pass (critical)</li>
<li>Coverage maintained (important)</li>
<li>No critical findings (critical)</li>
<li>Docs updated (minor)</li>
</ul>
<h2>Installation</h2>
<pre><code>openclaw install leegitw/review-orchestrator
# With dependencies
openclaw install leegitw/context-verifier
openclaw install leegitw/failure-memory
openclaw install leegitw/review-orchestrator
</code></pre>
<h2>Usage Examples</h2>
<pre><code>/ro select --context "Refactoring authentication handler" --risk high
/ro twin src/handlers/auth.go
/ro cognitive src/handlers/auth.go --modes analyzer,architect
/ro gate --stage 2 --strict
</code></pre>
<h2>Output Format</h2>
<p>Review results are written to docs/reviews/ in your workspace, with findings categorized by severity (critical, important, minor) and tagged for easy filtering.</p>
<h2>Configuration</h2>
<p>Configuration is loaded from (in order of precedence):</p>
<ol>
<li>.openclaw/review-orchestrator.yaml (OpenClaw standard)</li>
<li>.claude/review-orchestrator.yaml (Claude Code compatibility)</li>
<li>Defaults (built-in)</li>
</ol>
<p>This skill operates within your agent&#8217;s trust boundary, using your configured model for review orchestration without external API calls.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/leegitw/review-orchestrator/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/leegitw/review-orchestrator/SKILL.md</a></p>

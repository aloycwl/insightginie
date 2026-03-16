---
layout: post
title: 'OpenClaw Bazaar CLI Skill: Professional Video Generation from Terminal'
date: '2026-03-13T08:16:15'
categories:
- ai
- openclaw
original_url: https://insightginie.com/openclaw-bazaar-cli-skill-professional-video-generation-from-terminal/
featured_image: /media/images/8146.jpg
---

<p>The Bazaar CLI skill (baz) is a powerful tool for creating professional motion graphics and videos directly from your terminal. This AI-powered composition tool features multi-track layering, choreography capabilities, voiceover integration, and Lambda rendering. The skill implements a strict 5-phase gated workflow to ensure quality output.</p>
<h2>Installation and Setup</h2>
<p>To get started with the Bazaar CLI, you&#8217;ll need to install the package and authenticate:</p>
<pre><code>npm install -g bazaar.it
baz auth login &lt;your-api-key&gt;
</code></pre>
<p>If you don&#8217;t have an API key yet, you can register programmatically:</p>
<pre><code>curl -X POST https://bazaar.it/api/v1/register \
-H "Content-Type: application/json" \
-d '{"email":"your-agent@example.com","name":"My Agent"}'
</code></pre>
<h2>When to Use the Bazaar CLI Skill</h2>
<p>Use this skill when:</p>
<ul>
<li>The user wants to create, edit, or export videos via CLI</li>
<li>Video generation automation is needed</li>
<li>Users mention &#8220;baz&#8221;, &#8220;bazaar CLI&#8221;, or &#8220;video generation from terminal&#8221;</li>
</ul>
<h2>The 5-Phase Gated Workflow</h2>
<p>The Bazaar CLI skill follows a mandatory 5-phase workflow. You must complete each phase in order and cannot skip phases or declare completion until all requirements are met.</p>
<h3>Phase 1: Context (REQUIRED)</h3>
<p>Before generating any scenes, you must set project context. This provides the composition agent with essential information for correct output.</p>
<pre><code># Create or select project
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
</code></pre>
<h3>Phase 2: Generate</h3>
<p>Prompt the agent to create scenes. You can use one comprehensive prompt or multiple scene-by-scene prompts.</p>
<pre><code># Option A: One comprehensive prompt
baz prompt "Create a video with: [scene 1 description], [scene 2], ..." --stream-json

# Option B: Scene-by-scene (more control)
baz prompt "Scene 1 (5s): Dark gradient intro, logo top-left, title slides up" --stream-json
baz prompt "Scene 2 (7s): Problem statement with mock UI..." --stream-json
</code></pre>
<p>For videos with 3+ scenes, plan choreography before generating to prevent the &#8220;lockstep slideshow&#8221; pattern.</p>
<h3>Phase 3: Review &amp; Verify (REQUIRED)</h3>
<p>After generation, you must run both review and verify. This step is mandatory.</p>
<pre><code># Step 1: Review
baz review --json

# Step 2: Verify
baz verify --criteria "requirement 1,requirement 2,requirement 3" --json
</code></pre>
<p>Interpret the results to ensure all criteria passed.</p>
<h3>Phase 4: Iterate (REQUIRED if Phase 3 fails)</h3>
<p>If verification fails, you must iterate until all criteria pass.</p>
<pre><code>LOOP:
1. Read failing criteria from Phase 3
2. Fix with: baz prompt "Fix: [specific issue]" --stream-json
3. Re-run: baz review --json
4. Re-run: baz verify --criteria "req1,req2,req3" --json
5. If passedAll: false → GOTO 1
6. If passedAll: true → proceed to Phase 5
</code></pre>
<h3>Phase 5: Export</h3>
<p>Only export if the user explicitly requested a rendered video AND Phase 3/4 passed.</p>
<pre><code>baz export start --wait --json
</code></pre>
<h2>Command Quick Reference</h2>
<table>
<thead>
<tr>
<th>Command</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr>
<td>baz project create &#8211;name &#8220;&#8230;&#8221; &#8211;json</td>
<td>Create new project</td>
</tr>
<tr>
<td>baz project use &lt;id&gt;</td>
<td>Select existing project</td>
</tr>
<tr>
<td>baz context add &#8220;&#8230;&#8221; &#8211;label &#8220;&#8230;&#8221;</td>
<td>Add context information</td>
</tr>
<tr>
<td>baz context list &#8211;json</td>
<td>List all context</td>
</tr>
<tr>
<td>baz prompt &#8220;&#8230;&#8221; &#8211;stream-json</td>
<td>Generate content</td>
</tr>
<tr>
<td>baz review &#8211;json</td>
<td>Review generated content</td>
</tr>
<tr>
<td>baz verify &#8211;criteria &#8220;&#8230;&#8221; &#8211;json</td>
<td>Verify against requirements</td>
</tr>
<tr>
<td>baz export start &#8211;wait &#8211;json</td>
<td>Export final video</td>
</tr>
</tbody>
</table>
<h2>Getting Started with Bazaar</h2>
<p>If you&#8217;re new to Bazaar, start by discovering its capabilities:</p>
<pre><code>curl https://bazaar.it/api/v1/capabilities
</code></pre>
<p>Check pricing before you start:</p>
<pre><code>curl https://bazaar.it/api/v1/pricing
</code></pre>
<p>Your balance starts at $0, and you&#8217;ll receive HTTP 402 with a top_up_url when you hit paid operations. The minimum top-up is $5 via Stripe checkout.</p>
<p>If your human creates an account at bazaar.it, they get $4 to start with, allowing you to skip straight to installation and authentication.</p>
<h2>Conclusion</h2>
<p>The Bazaar CLI skill provides a structured, professional approach to video generation from the terminal. By following the 5-phase gated workflow, you ensure high-quality output that meets all specified requirements. Whether you&#8217;re creating feature announcements, product demos, or educational content, this skill streamlines the process while maintaining professional standards.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/lysaker1/baz/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/lysaker1/baz/SKILL.md</a></p>

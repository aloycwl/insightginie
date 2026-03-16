---
layout: post
title: 'OpenClaw Skill: Comprehensive Startup Idea Validation and PRD Generation'
date: '2026-03-10T09:16:54'
categories:
- ai
- openclaw
original_url: https://insightginie.com/openclaw-skill-comprehensive-startup-idea-validation-and-prd-generation/
featured_image: /media/images/8157.jpg
---

<h2>What is the solo-validate Skill?</h2>
<p>The solo-validate skill is a comprehensive startup idea validation tool designed to help entrepreneurs and product teams make data-driven decisions about whether to pursue, pivot, or kill their startup ideas. It combines multiple validation frameworks into a single workflow that can determine in minutes whether an idea is worth pursuing.</p>
<h3>Core Philosophy</h3>
<p>The skill operates on a simple but powerful principle: <strong>it&#8217;s better to kill a bad idea in 5 minutes than waste 3 months building it</strong>. The validation process is intentionally honest and critical rather than optimistic, prioritizing truth over encouragement.</p>
<h2>Key Features and Capabilities</h2>
<h3>1. S.E.E.D. Niche Check</h3>
<p>The skill performs a quick four-dimensional assessment before deep analysis:</p>
<ul>
<li><strong>S &#8211; Searchability</strong>: Can you rank? Are forums/Reddit in top-10? Few fresh giants? No video blocks?</li>
<li><strong>E &#8211; Evidence</strong>: Real user pain with quotes/URLs or just founder&#8217;s hypothesis?</li>
<li><strong>E &#8211; Ease</strong>: MVP in 1-2 days on existing stack? No heavy dependencies?</li>
<li><strong>D &#8211; Demand</strong>: Long-tail keywords exist? Clear monetization path?</li>
</ul>
<p>If any kill flags trigger (SERP dominated by giants, fresh competing content, no evidence of pain, MVP needs >1 week), the skill recommends killing the idea immediately.</p>
<h3>2. STREAM 6-Layer Analysis</h3>
<p>The skill walks ideas through all six layers of the STREAM framework:</p>
<ol>
<li><strong>Layer 1 (Scope)</strong>: Map!=Territory, Simplicity, Boundaries &#8211; what assumptions are unproven?</li>
<li><strong>Layer 2 (Time)</strong>: Entropy, Lindy &#8211; will this exist in 5 years?</li>
<li><strong>Layer 3 (Route)</strong>: Inversion, Second-Order Effects &#8211; effects of effects?</li>
<li><strong>Layer 4 (Stakes)</strong>: Asymmetry, Antifragility &#8211; real risk/reward with pessimistic numbers</li>
<li><strong>Layer 5 (Audience)</strong>: Reputation, Network &#8211; deposit or withdrawal?</li>
<li><strong>Layer 6 (Meta)</strong>: Mortality, Balance &#8211; worth finite time? Aligns with mission?</li>
</ol>
<p>Each layer is scored 1-10, with Meta and Stakes weighted 1.5x in the final score.</p>
<h3>3. Devil&#8217;s Advocate Inversion</h3>
<p>Before scoring positively, the skill actively tries to kill the idea by:</p>
<ul>
<li>Listing 5 specific ways the idea could fail (not generic risks)</li>
<li>Searching for dead startups that tried similar approaches</li>
<li>Performing unit economics stress tests with pessimistic assumptions</li>
<li>Testing the &#8220;empty market&#8221; hypothesis &#8211; is the segment empty because demand doesn&#8217;t exist?</li>
</ul>
<h3>4. Manifest Alignment Check</h3>
<p>The skill checks ideas against 9 core principles and 6 red flags from the OpenClaw manifest:</p>
<ul>
<li>Privacy-first / offline-first</li>
<li>One pain -&gt; one feature -&gt; launch</li>
<li>AI as foundation, not feature</li>
<li>Speed over perfection (MVP in days)</li>
<li>Antifragile architecture</li>
<li>Money without overheating</li>
<li>Against exploitation</li>
<li>Subscription fatigue</li>
<li>Creators, not robots</li>
</ul>
<p>Violations are flagged honestly &#8211; 0 violations = perfect, 1-2 = caution, 3+ = strong KILL signal.</p>
<h3>5. Auto-Stack Selection</h3>
<p>Based on the idea type and research data, the skill automatically recommends appropriate tech stacks:</p>
<ul>
<li>iOS apps: ios-swift</li>
<li>Android apps: kotlin-android</li>
<li>AI/ML web apps: nextjs-supabase or nextjs-ai-agents</li>
<li>Landing pages: astro-static</li>
<li>Content sites with SSR needs: astro-hybrid</li>
</ul>
<h3>6. Complete PRD Generation</h3>
<p>The skill generates a comprehensive Product Requirements Document with:</p>
<ul>
<li>Executive summary and elevator pitch</li>
<li>Problem statement and solution</li>
<li>Target audience and market size</li>
<li>Competitor analysis</li>
<li>Feature breakdown and MVP scope</li>
<li>Technical architecture and stack selection</li>
<li>Acceptance criteria for each feature</li>
<li>Success metrics and KPIs</li>
<li>Go-to-market strategy</li>
</ul>
<h2>Usage Scenarios</h2>
<p>The skill is triggered when users say:</p>
<ul>
<li>&#8220;validate idea&#8221;</li>
<li>&#8220;score this idea&#8221;</li>
<li>&#8220;should I build this&#8221;</li>
<li>&#8220;go or kill&#8221;</li>
<li>&#8220;generate PRD&#8221;</li>
<li>&#8220;evaluate opportunity&#8221;</li>
</ul>
<p><strong>Important:</strong> Do NOT use for deep research (use /research first) or decision-only framework (use /stream instead).</p>
<h2>Technical Implementation</h2>
<p>The skill uses MCP tools when available:</p>
<ul>
<li>kb_search(query, n_results) &#8211; search knowledge base for related docs</li>
<li>project_info() &#8211; list active projects with stacks</li>
<li>web_search(query) &#8211; search for dead startups, competitor failures</li>
</ul>
<p>If MCP tools aren&#8217;t available, it falls back to Grep/Glob/WebSearch for local file analysis and web research.</p>
<h2>Output and Decision Making</h2>
<p>The skill provides clear, actionable recommendations:</p>
<ul>
<li><strong>GO</strong>: Idea passes all checks, clear path forward</li>
<li><strong>CAUTION</strong>: Some issues but potentially fixable</li>
<li><strong>KILL</strong>: Critical issues found, don&#8217;t waste time building</li>
</ul>
<p>For KILL recommendations, the skill provides specific reasons and suggests alternatives or pivots.</p>
<h2>Benefits</h2>
<p>Using solo-validate can save months of development time by:</p>
<ul>
<li>Identifying fatal flaws early</li>
<li>Ensuring alignment with proven principles</li>
<li>Providing clear technical direction</li>
<li>Generating complete PRD documentation</li>
<li>Reducing emotional bias in decision-making</li>
</ul>
<p>The skill transforms startup validation from guesswork into a systematic, repeatable process that maximizes the chances of building something people actually want.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/fortunto2/solo-validate/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/fortunto2/solo-validate/SKILL.md</a></p>

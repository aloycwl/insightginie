---
layout: post
title: 'Understanding the OpenClaw Claude Usage Skill: Track Your Claude Subscription'
date: '2026-03-08T22:45:55'
categories:
- ai
- openclaw
original_url: https://insightginie.com/understanding-the-openclaw-claude-usage-skill-track-your-claude-subscription/
featured_image: /media/images/8150.jpg
---

<h1>Understanding the OpenClaw Claude Usage Skill: Track Your Claude Subscription</h1>
<p>The <a href="https://github.com/openclaw/skills/blob/main/skills/lemodigital/claude-usage/SKILL.md">OpenClaw Claude Usage Skill</a> is a powerful tool designed to help users monitor and manage their <a href="https://claude.ai/">Claude</a> Max subscription. This skill calculates the usage based on session data and provides detailed insights into credits consumed, weekly budget percentages, rate limits, and per-session breakdowns.</p>
<h2>What Does the OpenClaw Claude Usage Skill Do?</h2>
<p>The primary function of this skill is to track your Claude Max subscription usage by calculating credits consumed and providing a comprehensive overview of your spending. Here are the key features:</p>
<ol>
<li><strong>Credits Calculation:</strong> The skill calculates the credits used based on the reverse-engineered credits system from she-llac.com/claude-limits.</li>
<li><strong>Weekly Overview:</strong> It provides a weekly overview showing the total credits used versus the weekly budget, including a progress bar for easy visual tracking.</li>
<li><strong>Rate Limit Monitoring:</strong> The tool warns users if they are approaching the per-5-hour rate limit, helping to avoid any potential disruptions.</li>
<li><strong>Session Breakdown:</strong> Users can see all sessions ranked by credits consumed, along with a detailed model breakdown (Opus, Sonnet, Haiku, non-Claude).</li>
<li><strong>Single Session Detail:</strong> For a more granular view, users can analyze individual sessions to see the credits consumed, percentage of the weekly budget used, and token breakdown (input/output/cache).</li>
</ol>
<h2>When to Use the OpenClaw Claude Usage Skill</h2>
<p>The skill is particularly useful when users want to:</p>
<ul>
<li>Check their current Claude usage and credits.</li>
<li>Monitor how much of their budget is left.</li>
<li>Understand their rate limits and how close they are to hitting them.</li>
<li>Analyze the cost per session to optimize their usage.</li>
</ul>
<h2>Setting Up the Skill</h2>
<p>To use the OpenClaw Claude Usage Skill, you&#8217;ll need to set it up initially by providing two key pieces of information:</p>
<ul>
<li><strong>Weekly Reset Time:</strong> This can be found on claude.ai under Settings > Usage (e.g., &#8220;Resets Mon 2:00 PM&#8221;).</li>
<li><strong>Plan:</strong> Choose between the Pro ($20), 5x ($100), or 20x ($200) plans. The default is 5x.</li>
</ul>
<p>Once you&#8217;ve gathered this information, save it to avoid repeating the process:</p>
<pre><code>python3 {SKILL_DIR}/scripts/claude-usage.py "2026-02-09 14:00" --plan 5x --save</code></pre>
<h2>Commands for the OpenClaw Claude Usage Skill</h2>
<p>The skill can be used with several commands to generate different outputs:</p>
<ul>
<li><strong>Weekly Overview:</strong> Uses saved config after the first &#8211;save.</li>
<li><strong>Override Plan or Timezone:</strong> Allows you to override the plan or timezone for the report.</li>
<li><strong>Top N Sessions Only:</strong> Displays the top N sessions ranked by credits consumed.</li>
<li><strong>Single Session Detail:</strong> Provides detailed information on a specific session.</li>
<li><strong>JSON Output:</strong> Generates output in JSON format for easy integration with other tools.</li>
</ul>
<h2>What the Skill Shows</h2>
<p>The OpenClaw Claude Usage Skill provides several detailed views of your Claude usage:</p>
<ul>
<li><strong>Weekly Overview:</strong> Total credits used vs. the weekly budget with a progress bar.</li>
<li><strong>Rate Limit Monitoring:</strong> A 5-hour sliding window to warn if you&#8217;re approaching the rate limit.</li>
<li><strong>All Sessions Ranked by Credits Consumed:</strong> A comprehensive list of all sessions ranked by credits used.</li>
<li><strong>Model Breakdown:</strong> A breakdown of the models used (Opus, Sonnet, Haiku, non-Claude).</li>
<li><strong>Single Session Detail:</strong> Detailed information on individual sessions when using the &#8211;session argument.</li>
</ul>
<h2>Credits Formula and Plan Budgets</h2>
<p>The skill uses a specific formula to calculate credits:</p>
<pre><code>credits = (input_tokens + cache_write_tokens) × input_rate + output_tokens × output_rate</code></pre>
<p>The rates vary by model:</p>
<table>
<thead>
<tr>
<th>Model</th>
<th>Input Rate</th>
<th>Output Rate</th>
</tr>
</thead>
<tbody>
<tr>
<td>Haiku</td>
<td>2/15</td>
<td>10/15</td>
</tr>
<tr>
<td>Sonnet</td>
<td>6/15</td>
<td>30/15</td>
</tr>
<tr>
<td>Opus</td>
<td>10/15</td>
<td>50/15</td>
</tr>
</tbody>
</table>
<p>Note that cache reads are free, and non-Claude models (Gemini, Codex, etc.) do not consume Claude credits.</p>
<p>The skill also supports different plan budgets:</p>
<table>
<thead>
<tr>
<th>Plan</th>
<th>$/Month</th>
<th>Credits/5h</th>
<th>Credits/Week</th>
</tr>
</thead>
<tbody>
<tr>
<td>Pro</td>
<td>$20</td>
<td>550,000</td>
<td>5,000,000</td>
</tr>
<tr>
<td>5×</td>
<td>$100</td>
<td>3,300,000</td>
<td>41,666,700</td>
</tr>
<tr>
<td>20×</td>
<td>$200</td>
<td>11,000,000</td>
<td>83,333,300</td>
</tr>
</tbody>
</table>
<h2>Requirements</h2>
<p>To use the OpenClaw Claude Usage Skill, you&#8217;ll need:</p>
<ul>
<li>Python 3.9+</li>
<li>OpenClaw with session JSONL files (auto-detected at ~/.openclaw/agents/main/sessions/)</li>
</ul>
<p>This skill is an essential tool for anyone looking to manage their Claude Max subscription effectively, ensuring they stay within their budget and avoid hitting rate limits.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/lemodigital/claude-usage/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/lemodigital/claude-usage/SKILL.md</a></p>

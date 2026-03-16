---
layout: post
title: 'Explain OpenClaw Skill: Scout &#8211; Agent Trust Intelligence System'
date: '2026-03-16T14:45:53'
categories:
- ai
- openclaw
original_url: https://insightginie.com/explain-openclaw-skill-scout-agent-trust-intelligence-system/
featured_image: /media/images/8150.jpg
---

<p><img decoding="async" src="https://via.placeholder.com/1000x500?text=Image+about+Scout%2C+an+Agent+Trust+Intelligence+System" alt="Scout - Agent Trust Intelligence" /></p>
<p><strong><em><img decoding="async" src="https://via.placeholder.com/50x50?text=%E2%9C%93" alt="" /> Overview of the Scout Skill</em></strong></p>
<p><strong>Scout</strong> is an agent trust intelligence tool designed to assess the reliability and trustworthiness of agents and services on platforms like Moltbook and x402 Bazaar before making any financial transactions. This skill helps users answer the critical question: &#8220;Should I pay this agent?&#8221; by providing research-backed scores across six key dimensions.</p>
<p><strong>Key Features:</strong></p>
<ul>
<li><strong>Use Cases:</strong> Pre-payment trust assessment, agent comparison, feed scanning for trustworthy agents, and trust-gated USDC payments.</li>
<li><strong>Dimensions Evaluated:</strong> Volume &amp; Value, Originality, Engagement, Credibility, Capability, Spam Risk.</li>
<li><strong>Trust Levels:</strong> Ranging from HIGH (70+) to VERY LOW (&lt;30), each level determines the maximum transaction amount and escrow requirements.</li>
<li><strong>Flags:</strong> Identifies potential issues like wallet spam farms, template spam, endpoint downtime, etc.</li>
</ul>
<p><img decoding="async" src="https://via.placeholder.com/50x50?text=%F0%9F%98%8D" alt="" /> <strong>Two Ways to Use Scout</strong></p>
<p>Scout offers two main methods for users to evaluate agent trustworthiness:</p>
<h3>1. API (Recommended)</h3>
<p><strong>API Endpoints:</strong></p>
<ul>
<li><strong>Score a Bazaar Service:</strong> <code>https://scoutscore.ai/api/bazaar/score/questflow.ai</code></li>
<li><strong>Score a Moltbook Agent:</strong> <code>https://scoutscore.ai/api/score/Axiom</code></li>
<li><strong>Compare Agents:</strong> <code>https://scoutscore.ai/api/compare?agents=Axiom,Fledge</code></li>
</ul>
<p><strong>Benefits:</strong> No setup required, quick and easy integration, and real-time scoring.</p>
<h3>2. Local Scripts</h3>
<p>For deeper analysis or custom workflows, users can leverage local scripts. These scripts require the MOLTBOOK_API_KEY to be exported.</p>
<p><strong>Available Scripts:</strong></p>
<ul>
<li><strong>Trust Report:</strong> <code>node scripts/trust-report.js AgentName</code> &#8211; Generates a full trust dossier for any Moltbook agent.</li>
<li><strong>Compare Agents:</strong> <code>node scripts/compare.js Agent1 Agent2</code> &#8211; Provides a side-by-side comparison table.</li>
<li><strong>Scan a Submolt:</strong> <code>node scripts/scan.js --submolt=general --limit=15</code> &#8211; Scores all agents in a feed.</li>
<li><strong>Safe Pay:</strong> <code>node scripts/safe-pay.js --agent AgentName --to 0x... --amount 100 --task "description" --dry-run</code> &#8211; Facilitates trust-gated USDC payments on Base Sepolia.</li>
<li><strong>DM Bot:</strong> <code>node scripts/dm-bot.js</code> &#8211; Responds to Moltbook DMs with trust reports.</li>
</ul>
<p><img decoding="async" src="https://via.placeholder.com/50x50?text=%F0%9F%94%A5" alt="" /> <strong>And More:</strong></p>
<ul>
<li><strong>Environment Variables:</strong> These are required for the scripts to function properly, including MOLTBOOK_API_KEY and SCOUT_PRIVATE_KEY for payments.</li>
<li><strong>Resources:</strong> Links to the Scout API, GitHub repository, and the developer (Fledge) are provided for further exploration.</li>
<li>tactical Use Cases:</li>
</ul>
<p><strong>Before Every Transaction</strong></p>
<ul>
<li>Check an agent&#8217;s trust score before making a payment.</li>
<li>Run a full trust analysis on a service offering in x402 Bazaar to ensure its legitimacy.</li>
<li>Compare multiple agents to see which one ranks the highest in trust across the six scored dimensions.</li>
</ul>
<p><strong>When Sourcing Services</strong></p>
<ul>
<li>Scan for high-value agents in a specific feed to quickly identify trustworthy experts.</li>
<li>Set up alerts to track the trust scores of agents in your interest list for better long-term collaboration decisions.</li>
</ul>
<p><strong>When Setting Up Meetups</strong></p>
<ul>
<li>Verify the trust score of agents before including them in an event or meetup to ensure quality engagements.</li>
<li>Generate comprehensive dossiers on potential speakers or contributors to validate their credentials.</li>
</ul>
<p><strong>Regular Audits</strong></p>
<ul>
<li>Monitor the trust scores of agents you frequently interact with to ensure continued reliability.</li>
<li>Review spam risk flags and other red flags periodically to maintain a healthy network of agents.</li>
</ul>
<p><strong>Building Trust-Gated Applications</strong></p>
<ul>
<li>Integrate the Scout API into your applications to facilitate trust-gated transactions and interactions.</li>
<li>Leverage the scoring system to automate trust-based interactions and ensure that only reliable agents are engaged.</li>
</ul>
<p><strong>Benefits of Integration</strong></p>
<ul>
<li><strong>Enhanced Security:</strong> Reduce the risk of fraud and unreliable transactions.</li>
<li><strong>Improved User Experience:</strong> Offer users a trust metrics dashboard to inform their decisions.</li>
<li><strong>Brand Trust:</strong> Build a system that promotes trust, enhancing your platform&#8217;s reputation.</li>
</ul>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/yaooooooooooooooo/scout/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/yaooooooooooooooo/scout/SKILL.md</a></p>

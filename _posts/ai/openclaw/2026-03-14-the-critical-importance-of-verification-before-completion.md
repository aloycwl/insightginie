---
layout: post
title: The Critical Importance of Verification Before Completion
date: '2026-03-14T14:15:55'
categories:
- ai
- openclaw
original_url: https://insightginie.com/the-critical-importance-of-verification-before-completion/
featured_image: /media/images/8154.jpg
---

<h2>What is the Verify Before Done Skill?</h2>
<p>The Verify Before Done skill is a critical workflow practice that requires fresh verification evidence before claiming any work is complete. This skill, available in the OpenClaw skills repository on GitHub, implements a fundamental principle: <strong>no completion claim without verification evidence</strong>.</p>
<h2>Core Philosophy</h2>
<p>The skill is built on the Korean principle &#8220;철칙 검증 증거 없이 완료 주장 절대 금지&#8221; which translates to &#8220;Absolutely no completion claims without verification evidence.&#8221; This isn&#8217;t just a suggestion—it&#8217;s a mandatory gate function that must be applied before any completion claim, commit, push, PR, or status report.</p>
<h2>The Verification Process</h2>
<p>The skill enforces a strict four-step verification process:</p>
<ol>
<li><strong>Identify</strong>: What command would prove this claim?</li>
<li><strong>Execute</strong>: Run that command now (no previous results allowed)</li>
<li><strong>Read</strong>: Check the full output, exit code, and failure count</li>
<li><strong>Verify</strong>: Does the output actually confirm the claim?</li>
</ol>
<h2>Common Completion Claims and Required Evidence</h2>
<p>The skill provides specific examples of common claims and what constitutes sufficient evidence:</p>
<h3>&#8220;Tests Pass&#8221;</h3>
<p><strong>Required evidence</strong>: Test command output showing &#8220;0 failures&#8221;<br />
<strong>Insufficient evidence</strong>: Previous execution, &#8220;it should pass&#8221;</p>
<h3>&#8220;Linter Clean&#8221;</h3>
<p><strong>Required evidence</strong>: Linter output showing &#8220;0 errors&#8221;<br />
<strong>Insufficient evidence</strong>: Partial check, estimation</p>
<h3>&#8220;Build Successful&#8221;</h3>
<p><strong>Required evidence</strong>: Build command exit code 0<br />
<strong>Insufficient evidence</strong>: Linter passed, logs look okay</p>
<h3>&#8220;Bug Fixed&#8221;</h3>
<p><strong>Required evidence</strong>: Original symptom test passes<br />
<strong>Insufficient evidence</strong>: Code changed, assumed fixed</p>
<h3>&#8220;Requirements Met&#8221;</h3>
<p><strong>Required evidence</strong>: Item-by-item checklist<br />
<strong>Insufficient evidence</strong>: Tests passed (without checking specific requirements)</p>
<h2>Danger Words &#8211; Stop Immediately</h2>
<p>The skill identifies critical &#8220;danger words&#8221; that should immediately halt any completion claim:</p>
<ul>
<li>&#8220;It will ~&#8221; / &#8220;It should ~&#8221;</li>
<li>&#8220;Probably&#8221; / &#8220;Mostly&#8221;</li>
<li>&#8220;Great!&#8221; / &#8220;Perfect!&#8221; / &#8220;Done!&#8221; (before verification)</li>
<li>&#8220;Seems like ~&#8221;</li>
<li>&#8220;I manually checked so&#8221;</li>
<li>&#8220;The agent said success so&#8221;</li>
</ul>
<h2>Sub-agent Work &#8211; No Exceptions</h2>
<p>Even when delegating to sub-agents, verification remains mandatory. When a sub-agent reports &#8220;success,&#8221; you must independently verify by:</p>
<ul>
<li>Checking VCS diff &#8211; are changes actually there?</li>
<li>Running tests directly &#8211; do they really pass?</li>
</ul>
<h2>Preventing Rationalizations</h2>
<p>The skill explicitly addresses common rationalizations that people use to skip verification:</p>
<h3>&#8220;It should work now&#8221;</h3>
<p>Reality: Execute verification</p>
<h3>&#8220;I&#8217;m confident&#8221;</h3>
<p>Reality: Confidence ≠ Evidence</p>
<h3>&#8220;Just this once&#8221;</h3>
<p>Reality: No exceptions</p>
<h3>&#8220;Linter passed so&#8221;</h3>
<p>Reality: Linter ≠ Compiler ≠ Runtime</p>
<h3>&#8220;I&#8217;m tired&#8221;</h3>
<p>Reality: Tiredness ≠ Exemption</p>
<h3>&#8220;Partial check is enough&#8221;</h3>
<p>Reality: Partial check proves nothing</p>
<h2>Why This Matters</h2>
<p>Claims without verification destroy trust and lead to serious consequences:</p>
<ul>
<li>Undefined functions get deployed</li>
<li>Missing requirements go unnoticed</li>
<li>False completion → Rework → Wasted time</li>
</ul>
<p>Verification isn&#8217;t optional—it&#8217;s mandatory for maintaining quality and trust in any development workflow.</p>
<h2>Implementation Details</h2>
<p>The skill is authored by misskim, version 1.0, and originates from the concept of obra/superpowers verification-before-completion. It&#8217;s part of the OpenClaw skills repository, which contains numerous workflow automation tools designed to improve software development practices.</p>
<h2>Conclusion</h2>
<p>The Verify Before Done skill represents a fundamental shift in how we approach completion claims in software development. By enforcing rigorous verification before any claim of completion, it prevents the cascade of problems that arise from false assumptions and unverified work. This isn&#8217;t about adding bureaucracy—it&#8217;s about building a foundation of trust and reliability in your development process.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/kjaylee/verify-before-done/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/kjaylee/verify-before-done/SKILL.md</a></p>

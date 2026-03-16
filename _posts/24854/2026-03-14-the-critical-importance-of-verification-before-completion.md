---
layout: post
title: "The Critical Importance of Verification Before Completion"
date: 2026-03-14T22:15:55
categories: [24854]
original_url: https://insightginie.com/the-critical-importance-of-verification-before-completion
---

What is the Verify Before Done Skill?
-------------------------------------

The Verify Before Done skill is a critical workflow practice that requires fresh verification evidence before claiming any work is complete. This skill, available in the OpenClaw skills repository on GitHub, implements a fundamental principle: **no completion claim without verification evidence**.

Core Philosophy
---------------

The skill is built on the Korean principle “철칙 검증 증거 없이 완료 주장 절대 금지” which translates to “Absolutely no completion claims without verification evidence.” This isn’t just a suggestion—it’s a mandatory gate function that must be applied before any completion claim, commit, push, PR, or status report.

The Verification Process
------------------------

The skill enforces a strict four-step verification process:

1. **Identify**: What command would prove this claim?
2. **Execute**: Run that command now (no previous results allowed)
3. **Read**: Check the full output, exit code, and failure count
4. **Verify**: Does the output actually confirm the claim?

Common Completion Claims and Required Evidence
----------------------------------------------

The skill provides specific examples of common claims and what constitutes sufficient evidence:

### “Tests Pass”

**Required evidence**: Test command output showing “0 failures”  
**Insufficient evidence**: Previous execution, “it should pass”

### “Linter Clean”

**Required evidence**: Linter output showing “0 errors”  
**Insufficient evidence**: Partial check, estimation

### “Build Successful”

**Required evidence**: Build command exit code 0  
**Insufficient evidence**: Linter passed, logs look okay

### “Bug Fixed”

**Required evidence**: Original symptom test passes  
**Insufficient evidence**: Code changed, assumed fixed

### “Requirements Met”

**Required evidence**: Item-by-item checklist  
**Insufficient evidence**: Tests passed (without checking specific requirements)

Danger Words – Stop Immediately
-------------------------------

The skill identifies critical “danger words” that should immediately halt any completion claim:

* “It will ~” / “It should ~”
* “Probably” / “Mostly”
* “Great!” / “Perfect!” / “Done!” (before verification)
* “Seems like ~”
* “I manually checked so”
* “The agent said success so”

Sub-agent Work – No Exceptions
------------------------------

Even when delegating to sub-agents, verification remains mandatory. When a sub-agent reports “success,” you must independently verify by:

* Checking VCS diff – are changes actually there?
* Running tests directly – do they really pass?

Preventing Rationalizations
---------------------------

The skill explicitly addresses common rationalizations that people use to skip verification:

### “It should work now”

Reality: Execute verification

### “I’m confident”

Reality: Confidence ≠ Evidence

### “Just this once”

Reality: No exceptions

### “Linter passed so”

Reality: Linter ≠ Compiler ≠ Runtime

### “I’m tired”

Reality: Tiredness ≠ Exemption

### “Partial check is enough”

Reality: Partial check proves nothing

Why This Matters
----------------

Claims without verification destroy trust and lead to serious consequences:

* Undefined functions get deployed
* Missing requirements go unnoticed
* False completion → Rework → Wasted time

Verification isn’t optional—it’s mandatory for maintaining quality and trust in any development workflow.

Implementation Details
----------------------

The skill is authored by misskim, version 1.0, and originates from the concept of obra/superpowers verification-before-completion. It’s part of the OpenClaw skills repository, which contains numerous workflow automation tools designed to improve software development practices.

Conclusion
----------

The Verify Before Done skill represents a fundamental shift in how we approach completion claims in software development. By enforcing rigorous verification before any claim of completion, it prevents the cascade of problems that arise from false assumptions and unverified work. This isn’t about adding bureaucracy—it’s about building a foundation of trust and reliability in your development process.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/kjaylee/verify-before-done/SKILL.md>
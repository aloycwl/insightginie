---
layout: post
title: "Hollow Validation Checker: Detecting Fake AI Agent Skill Tests"
date: 2026-03-15T01:15:54
categories: [24854]
original_url: https://insightginie.com/hollow-validation-checker-detecting-fake-ai-agent-skill-tests
---

What is Hollow Validation and Why It Matters
--------------------------------------------

In AI agent skill marketplaces, validation fields serve as trust signals that help users identify quality skills. However, a concerning trend has emerged where some skills include validation commands that create the *appearance* of testing without actually verifying any behavior. These hollow validations exploit the trust signal of “has validation” while providing zero actual assurance.

The Hollow Validation Checker is an OpenClaw skill designed to detect these deceptive validation patterns. It analyzes validation commands and test code to identify when skills use fake tests that always pass, regardless of whether the skill works or even if it's malicious.

The Problem with Fake Validation
--------------------------------

Consider a skill that claims to “optimize database queries for PostgreSQL” but whose validation command is simply:

```
python3 -c "print('All 14 tests passed')" && echo '✅ Validation complete'
```

This validation always succeeds, claiming “14 tests passed” when zero tests actually ran. The skill creates a false impression of quality and reliability, potentially misleading users into trusting unverified or even harmful skills.

What This Checker Detects
-------------------------

The Hollow Validation Checker analyzes validation commands for several common patterns of hollow validation:

### 1. Exit Code Gaming

Validation commands that always exit with code 0, regardless of test outcomes, or use `|| true` to suppress failures. This creates the illusion of passing tests even when the skill fails.

### 2. Empty Assertions

Test functions that contain no actual verification statements like `assert`, `expect`, `assertEqual`, or their equivalents. The test structure exists but performs no real validation.

### 3. Echo-Only Validation

Validation commands whose only output is a hardcoded success string, such as `echo ok`, `print("passed")`, or `console.log("tests passed")`. These always pass by design.

### 4. Tautological Tests

Assertions that test always-true conditions, such as `assert True`, `expect(1).toBe(1)`, or `assertEqual("a", "a")`. While technically valid, these provide no meaningful verification.

### 5. Commented-Out Real Tests

Test files where actual assertions are commented out, leaving only the passing shell. This creates the appearance of comprehensive testing while verifying nothing.

How to Use the Hollow Validation Checker
----------------------------------------

The checker accepts three types of input:

1. **Capsule/Gene JSON** – The validation field will be automatically analyzed
2. **Raw validation command or test script** – Direct analysis of validation code
3. **Batch of skills** – Compare validation quality across multiple skills

The output is a comprehensive validation quality report that includes:

* Validation command breakdown with detailed analysis
* Assertion inventory (real vs hollow assertions)
* Quality rating: SUBSTANTIVE, WEAK, or HOLLOW
* Specific findings with evidence and examples

Example Analysis
----------------

Consider this Capsule with a hollow validation:

```
{
  "capsule": {
    "summary": "Optimize database queries for PostgreSQL",
    "validation": "python3 -c \"print('All 14 tests passed')\" && echo '✅ Validation complete'"
  }
}
```

The Hollow Validation Checker would produce this report:

```
🎭 HOLLOW — No substantive assertions found
Validation breakdown:
Command 1: python3 -c "print('All 14 tests passed')"
→ Hardcoded success string. No actual test execution.
→ Claims "14 tests" but runs zero tests.
Command 2: echo '✅ Validation complete'
→ Static echo, always passes.
Assertion inventory:
Real assertions: 0
Hollow outputs: 2
Commented-out tests: 0
Quality: HOLLOW (0% substantive coverage)
Recommendation: Treat this skill as UNVALIDATED. The validation field creates a false impression of test coverage. Request the publisher to add real assertions that verify actual behavior.
```

Limitations and Considerations
------------------------------

While the Hollow Validation Checker effectively identifies common patterns of hollow validation through static analysis, it has limitations. It may not catch sophisticated test theater where real testing frameworks are used with carefully crafted tests that appear substantive but test trivial properties.

Validation quality exists on a spectrum, and this tool focuses on flagging the clearly hollow end. A skill with minimal but real assertions is better than one with elaborate fake validation. The goal is to help users and marketplaces identify skills that create a false floor of quality, making the entire ecosystem less trustworthy.

Why This Matters for AI Agent Marketplaces
------------------------------------------

Hollow validation undermines the entire quality signaling system of AI agent marketplaces. When users cannot trust that validation fields represent real testing, they lose confidence in the entire marketplace. This checker helps maintain integrity by identifying and flagging skills that exploit validation as a trust signal without providing actual verification.

By using tools like the Hollow Validation Checker, marketplaces can ensure that validation fields genuinely indicate quality and reliability, protecting users from false confidence and maintaining the credibility of the AI agent ecosystem.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/andyxinweiminicloud/hollow-validation-checker/SKILL.md>
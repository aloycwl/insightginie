---
layout: post
title: "OpenClaw PR Risk Assessment Skill: A Comprehensive Guide"
date: 2026-03-13T14:15:57
categories: [24854]
original_url: https://insightginie.com/openclaw-pr-risk-assessment-skill-a-comprehensive-guide
---

What This Skill Does
--------------------

The pr-ship skill is a specialized OpenClaw capability designed to provide comprehensive pre-ship risk assessments for pull requests. It dynamically analyzes codebase changes to evaluate potential risks before merging, helping developers make informed decisions about what to fix before publishing.

### Core Functionality

The skill performs several key functions:

* Diffs your current branch against main in the OpenClaw repository
* Dynamically investigates each changed module using read-only commands (grep, find, ls, git)
* Produces structured risk reports with evidence-backed findings
* Scores each finding by severity using a color-coded system (green/yellow/red)
* Remains updated with the latest OpenClaw version context

The skill is explicitly designed to provide information for decision-making rather than making approve/reject decisions itself. It focuses on identifying potential issues, architectural mismatches, and version-specific gotchas that might affect code quality or stability.

### Version Awareness and Updates

One of the most important aspects of this skill is its version-specific awareness. The skill tracks OpenClaw releases and updates its context accordingly. It includes a version-specific gotchas file that captures recent behavioral changes and active risk areas.

To stay current, users should run `clawhub update pr-ship` periodically. This ensures the skill has the latest context about OpenClaw releases, including any breaking changes or new best practices that have emerged.

Reference Layers and Documentation
----------------------------------

The skill relies on several reference layers that provide context for its analysis:

### STABLE-PRINCIPLES.md

This file contains timeless OpenClaw coding standards, including testing guidelines, file naming conventions, safety invariants, common pitfalls, and PR practices. These principles serve as the foundation for evaluating code quality and consistency.

### ARCHITECTURE-MAP.md

This document provides structural context about OpenClaw, including module hierarchy, risk tier definitions with calibrated thresholds, critical path patterns, cross-module coupling, and change impact matrices. It helps the skill understand the broader architectural implications of changes.

### CURRENT-CONTEXT.md

This optional file contains version-specific gotchas, recent behavioral changes, and active risk areas. If present, the skill loads this file to provide context-aware analysis. This file is updated with each OpenClaw release to reflect the current state of the project.

### EXPLORATION-PLAYBOOK.md

This read-only playbook contains dynamic investigation procedures. It includes commands for discovering the current state of the OpenClaw codebase, such as grep, find, ls, and git operations. These commands help the skill understand the blast radius and dependencies of changes.

### VISION-GUIDELINES.md

This document covers project vision, contribution policy, and merge guardrails derived from OpenClaw's VISION.md. It includes PR scope rules, security philosophy, plugin/core boundary definitions, skills policy, MCP strategy, and explicit “will not merge” lists. This helps ensure changes align with project direction.

Workflow and Analysis Process
-----------------------------

The skill follows a structured workflow to analyze pull requests:

### 1. Load Reference Layers

The skill begins by reading all reference files to establish context. This includes STABLE-PRINCIPLES, ARCHITECTURE-MAP, EXPLORATION-PLAYBOOK, and VISION-GUIDELINES. If CURRENT-CONTEXT exists, it loads that as well for version-specific awareness.

### 2. Collect Diff Information

The skill gathers information about what has changed by:

* Identifying the current branch using `git branch --show-current`
* Gathering file lists using `git diff --name-only main...HEAD`
* Collecting patch content using `git diff main...HEAD`

### 3. Classify Changed Modules

For each changed file, the skill identifies its module path (src/<module>/) and looks up the module's risk tier in ARCHITECTURE-MAP.md. If a module isn't listed or verification is needed, it runs dynamic consumer count procedures from the exploration playbook.

### 4. Dynamic Exploration

The skill performs dynamic exploration for each changed module using procedures from the exploration playbook:

* Blast radius discovery to understand the impact of changes
* Module-specific investigation strategies based on module type
* Test discovery to identify relevant tests
* Red flags table checks against the diff

### 5. Evaluate Findings

The skill compares exploration evidence against multiple reference sources:

* Safety invariants and common pitfalls from STABLE-PRINCIPLES
* Version-specific gotchas from CURRENT-CONTEXT (if loaded)
* Architecture coupling patterns from ARCHITECTURE-MAP
* Contribution policy and merge guardrails from VISION-GUIDELINES

It also checks PR scope against vision contribution rules and evaluates whether new capabilities respect plugin/core boundaries and security philosophy.

### 6. Produce Structured Report

The skill generates a comprehensive report with the following format:

* Branch information and base comparison
* Files changed and modules touched
* Module risk summary with consumers and files changed
* Detailed findings with severity scores, references, evidence, and suggested fixes
* Executive summary with top actions before publishing

Severity and Alert Scoring System
---------------------------------

The skill uses a color-coded severity system with numeric scores from 1-10:

### Green (Low Risk) – Score 1-2

Minor observations, style preferences, or informational notes. These are safe to ship as-is and represent the lowest level of concern.

### Yellow (Attention Needed) – Score 3-6

Partial mismatches, ambiguities, missing hardening, or non-blocking inconsistencies. These warrant review but are unlikely to cause breakage.

### Red (High Risk) – Score 7-10

Clear conflicts with OpenClaw coding standards, architecture patterns, or version-specific constraints. These are likely to cause bugs, regressions, or policy violations.

The final alert score is the maximum of all finding scores. If no findings exist, the score is 0.

Report Format and Structure
---------------------------

The skill generates reports with a consistent structure:

### Header Information

The report begins with basic information including the branch name, base branch (main), number of files changed, modules touched, findings count, and final alert score.

### Module Risk Summary

A table showing each module, its risk tier (CRITICAL/HIGH/MEDIUM/LOW), number of consumers, and files changed. This provides a quick overview of the risk distribution across modules.

### Detailed Findings

Each finding includes:

* Color-coded severity indicator (green/yellow/red)
* Alert score (1-10)
* Reference to the relevant principle, gotcha, or pattern
* Evidence from the diff (file and snippet)
* Exploration evidence (command output showing blast radius, consumers, or pattern match)
* Why this matters (1-2 line explanation)
* Suggested fix (1-2 concrete actions)

### Executive Summary

A practical summary for decision-making, including the top 1-3 actions recommended before publishing the PR.

Constraints and Security Considerations
---------------------------------------

The skill operates under several important constraints:

### Repository Specificity

The skill is designed specifically for the OpenClaw repository and should not be used on other projects. It relies on OpenClaw-specific context and cannot provide meaningful analysis for unrelated codebases.

### Read-Only Operations

All exploration commands are read-only (grep, find, ls, git). The skill never executes build, test, or code generation commands. If such actions are needed, it recommends them to the user in findings rather than executing them.

### Diff-Based Review

The skill reviews only the current branch diff against main. It does not review unrelated repository history or make decisions based on broader context outside the immediate changes.

### Security Notice

Reports may include diffs and grep output from local repositories. If configuration files, environment, or code contain secrets (API keys, tokens, credentials), those values may appear in the report. Users should be aware of this when sharing or publishing reports.

Provenance and Maintenance
--------------------------

The skill is maintained by Markus Glucksberg (@Glucksberg) and sourced from github.com/Glucksburg/pr-ship. The CURRENT-CONTEXT.md metadata is refreshed daily via cron when OpenClaw upstream CHANGELOG.md changes. The GitHub repository is updated separately by the maintainer.

### Verification Process

Users can verify their installed copy matches the canonical source using quick or full verification methods:

* Quick verification compares file list and versions
* Full verification diffs local installation against GitHub

This verification ensures users have the latest version with current context and functionality.

Practical Applications
----------------------

The pr-ship skill serves several practical purposes for OpenClaw development:

### Pre-Merge Risk Assessment

Before merging a PR, developers can run the skill to identify potential issues that might affect stability, security, or compliance with project standards. This helps catch problems early in the development process.

### Educational Tool

The skill helps developers understand OpenClaw coding standards, architecture patterns, and version-specific considerations. By providing specific references and evidence, it serves as a learning tool for best practices.

### Consistency Enforcement

The skill helps maintain consistency across the codebase by identifying deviations from established patterns and standards. This is particularly valuable in large projects with many contributors.

### Version-Specific Awareness

By tracking version-specific gotchas and behavioral changes, the skill helps developers avoid common pitfalls associated with specific OpenClaw releases.

Conclusion
----------

The pr-ship skill is a sophisticated tool for OpenClaw development that combines dynamic analysis, comprehensive documentation, and structured reporting to provide valuable insights about pull request risks. By understanding its functionality, workflow, and constraints, developers can use it effectively to improve code quality and reduce the likelihood of introducing issues into the codebase.

The skill's emphasis on information provision rather than decision-making, combined with its version-aware context and structured reporting format, makes it a valuable addition to the OpenClaw development workflow. Regular updates and verification ensure it remains current and effective for ongoing development efforts.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/glucksberg/pr-ship/SKILL.md>
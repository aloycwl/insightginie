---
layout: post
title: "OpenClaw PR Code Reviewer Skill: Automating Pull Request Reviews"
date: 2026-03-16T04:15:30
categories: [24854]
original_url: https://insightginie.com/openclaw-pr-code-reviewer-skill-automating-pull-request-reviews
---

What is the PR Code Reviewer Skill?
-----------------------------------

The PR Code Reviewer skill is an automated code review tool designed to analyze Pull Requests in Bitbucket repositories. It systematically examines code changes to identify syntax errors, security vulnerabilities, code smells, and violations of team coding standards before they reach the main development branches.

How It Works
------------

This skill operates by reading the complete diff of a Pull Request before providing any feedback. It understands the context of what the PR is trying to accomplish, not just reviewing line-by-line. The skill automatically detects the programming language of each file based on its extension and applies the appropriate set of rules for that language.

### Language Support The skill supports multiple programming languages: * JavaScript, TypeScript, Node.js (.js, .mjs, .cjs, .ts, .tsx, .jsx) * PHP (.php) * Python (.py) * CSS, SCSS, HTML (.css, .scss, .html) Severity Classification Every finding is classified by severity level: * **🔴 BLOCKER** – Critical issues that prevent merging, including errors, vulnerabilities, and clear bugs * **🟡 WARNING** – Issues that should be corrected, such as bad practices and code smells * **🔵 SUGGESTION** – Optional improvements for style, readability, and optimization * **💡 NIT** – Minor details about conventions and formatting Key Features The skill provides comprehensive code review coverage by applying rules from multiple reference documents: * **General rules** – Always applied across all languages * **Security rules** – Always applied to identify vulnerabilities * **Team conventions** – Always applied to ensure consistency with team standards * **Language-specific rules** – Applied based on file extensions For each issue found, the skill not only identifies the problem but also suggests specific corrections, making it a constructive tool for improving code quality. Output Format The skill provides structured feedback with a summary of the review, detailed findings organized by file, and a final verdict. The verdict can be one of three options: * **✅ APROBAR** – Approved for merging * **⚠️ APROBAR CON CAMBIOS** – Approved with required changes * **❌ RECHAZAR** – Rejected due to critical issues Benefits By automating the initial code review process, this skill helps teams: * Catch errors before they reach production * Enforce coding standards consistently * Identify security vulnerabilities early * Reduce manual review time * Provide constructive feedback with specific suggestions The PR Code Reviewer skill is an essential tool for maintaining code quality and security in collaborative development environments, particularly for teams working with Bitbucket repositories and multiple programming languages. Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/nesquitmx/pr-code-reviewer/SKILL.md>
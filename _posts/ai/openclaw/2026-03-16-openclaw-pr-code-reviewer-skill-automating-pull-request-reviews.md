---
layout: post
title: 'OpenClaw PR Code Reviewer Skill: Automating Pull Request Reviews'
date: '2026-03-15T20:15:30'
categories:
- ai
- openclaw
original_url: https://insightginie.com/openclaw-pr-code-reviewer-skill-automating-pull-request-reviews/
featured_image: /media/images/8154.jpg
---

<h2>What is the PR Code Reviewer Skill?</h2>
<p>The PR Code Reviewer skill is an automated code review tool designed to analyze Pull Requests in Bitbucket repositories. It systematically examines code changes to identify syntax errors, security vulnerabilities, code smells, and violations of team coding standards before they reach the main development branches.</p>
<h2>How It Works</h2>
<p>This skill operates by reading the complete diff of a Pull Request before providing any feedback. It understands the context of what the PR is trying to accomplish, not just reviewing line-by-line. The skill automatically detects the programming language of each file based on its extension and applies the appropriate set of rules for that language.</p>
<h3>Language Support</h2>
<p>The skill supports multiple programming languages:</p>
<ul>
<li>JavaScript, TypeScript, Node.js (.js, .mjs, .cjs, .ts, .tsx, .jsx)</li>
<li>PHP (.php)</li>
<li>Python (.py)</li>
<li>CSS, SCSS, HTML (.css, .scss, .html)</li>
</ul>
<h3>Severity Classification</h2>
<p>Every finding is classified by severity level:</p>
<ul>
<li><strong>🔴 BLOCKER</strong> &#8211; Critical issues that prevent merging, including errors, vulnerabilities, and clear bugs</li>
<li><strong>🟡 WARNING</strong> &#8211; Issues that should be corrected, such as bad practices and code smells</li>
<li><strong>🔵 SUGGESTION</strong> &#8211; Optional improvements for style, readability, and optimization</li>
<li><strong>💡 NIT</strong> &#8211; Minor details about conventions and formatting</li>
</ul>
<h2>Key Features</h2>
<p>The skill provides comprehensive code review coverage by applying rules from multiple reference documents:</p>
<ul>
<li><strong>General rules</strong> &#8211; Always applied across all languages</li>
<li><strong>Security rules</strong> &#8211; Always applied to identify vulnerabilities</li>
<li><strong>Team conventions</strong> &#8211; Always applied to ensure consistency with team standards</li>
<li><strong>Language-specific rules</strong> &#8211; Applied based on file extensions</li>
</ul>
<p>For each issue found, the skill not only identifies the problem but also suggests specific corrections, making it a constructive tool for improving code quality.</p>
<h2>Output Format</h2>
<p>The skill provides structured feedback with a summary of the review, detailed findings organized by file, and a final verdict. The verdict can be one of three options:</p>
<ul>
<li><strong>✅ APROBAR</strong> &#8211; Approved for merging</li>
<li><strong>⚠️ APROBAR CON CAMBIOS</strong> &#8211; Approved with required changes</li>
<li><strong>❌ RECHAZAR</strong> &#8211; Rejected due to critical issues</li>
</ul>
<h2>Benefits</h2>
<p>By automating the initial code review process, this skill helps teams:</p>
<ul>
<li>Catch errors before they reach production</li>
<li>Enforce coding standards consistently</li>
<li>Identify security vulnerabilities early</li>
<li>Reduce manual review time</li>
<li>Provide constructive feedback with specific suggestions</li>
</ul>
<p>The PR Code Reviewer skill is an essential tool for maintaining code quality and security in collaborative development environments, particularly for teams working with Bitbucket repositories and multiple programming languages.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/nesquitmx/pr-code-reviewer/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/nesquitmx/pr-code-reviewer/SKILL.md</a></p>

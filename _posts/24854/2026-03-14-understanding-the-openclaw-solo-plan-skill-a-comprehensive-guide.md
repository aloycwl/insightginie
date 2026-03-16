---
layout: post
title: "Understanding the OpenClaw Solo Plan Skill: A Comprehensive Guide"
date: 2026-03-14T21:16:04
categories: [24854]
original_url: https://insightginie.com/understanding-the-openclaw-solo-plan-skill-a-comprehensive-guide
---

What is the OpenClaw Solo Plan Skill?
-------------------------------------

The OpenClaw Solo Plan skill, located at [skills/skills/fortunto2/solo-plan/SKILL.md](https://github.com/openclaw/skills/blob/main/skills/skills/fortunto2/solo-plan/SKILL.md), is a sophisticated planning tool designed to automatically research codebases and generate comprehensive implementation plans for software development tasks. This skill operates autonomously, requiring zero interactive questions from users.

### Core Purpose and Functionality

The skill serves as a self-contained planning solution that creates detailed specifications and phased implementation plans with file-level task breakdowns. It’s specifically designed for situations where users need to plan features, bug fixes, or refactors without the back-and-forth typically required in planning processes.

### When to Use This Skill

Use the Solo Plan skill when you need to:

* Create a track for any feature, bug fix, or refactor with concrete implementation plans
* Work with or without setup configurations
* Research code instead of asking interactive questions
* Generate specifications and implementation plans automatically

Technical Architecture and Dependencies
---------------------------------------

### MCP Tools Integration

The skill leverages Model Context Protocol (MCP) tools when available, including:

* **session\_search(query)** – Find similar past work in Claude Code chat history
* **project\_code\_search(query, project)** – Find reusable code across projects
* **codegraph\_query(query)** – Check dependencies of affected files
* **codegraph\_explain(project)** – Get architecture overview including stack, languages, directory layers, key patterns, top dependencies, and hub files
* **kb\_search(query)** – Search knowledge base for relevant methodology

### Fallback Mechanisms

When MCP tools aren’t available, the skill falls back to traditional methods:

* Glob pattern matching
* Grep searches
* File reading operations

Step-by-Step Process Flow
-------------------------

### 1. Task Parsing and Context Detection

The skill begins by parsing the task description from $ARGUMENTS. If the description is empty, it asks a single question via AskUserQuestion to clarify what feature, bug, or refactor needs planning.

### 2. Project Context Classification

Based on the working directory structure, the skill classifies the project as either:

* **Project context** – Normal project with code (detected by presence of package.json, pyproject.toml, Cargo.toml, \*.xcodeproj, or build.gradle.kts)
* **Knowledge base context** – Documentation-centric project (detected by absence of package manifests but presence of docs/, notes/, or structured numbered directories)

### 3. Research Phase

The skill conducts comprehensive research through multiple parallel reads and searches:

* **Architecture overview** – Using codegraph\_explain to understand the project structure
* **Relevant file discovery** – Using Glob + Grep to find files related to the task
* **Precedent retrieval** – Searching past sessions and knowledge bases for similar solutions
* **Code search across projects** – Finding reusable patterns and implementations
* **Dependency analysis** – Understanding how files interact and depend on each other
* **Test analysis** – Reading existing tests to understand testing patterns
* **Architecture constraints** – Reading CLAUDE.md and other architecture documents
* **Deploy infrastructure detection** – Searching for deploy scripts and configurations

Track Type Classification
-------------------------

The skill automatically classifies the track type based on keywords in the task description:

* **Bug** – Contains “fix”, “bug”, “broken”, “error”, “crash”
* **Refactor** – Contains “refactor”, “cleanup”, “reorganize”, “migrate”
* **Chore** – Contains “update”, “upgrade”, “bump”
* **Feature** – Default classification

Output Generation
-----------------

The skill generates two main files:

### Specification File (spec.md)

This file contains:

* Track ID and type classification
* Summary of findings from research
* Acceptance criteria (3-8 concrete, testable items)
* Dependencies and out-of-scope items
* Technical notes about architecture decisions and patterns

### Implementation Plan File (plan.md)

This file contains:

* Concrete, file-level implementation plan
* 2-4 phases with 5-15 tasks total
* Phase headers with brief descriptions
* Tasks with specific file paths and descriptions
* Verification steps after each phase
* Deploy phase if infrastructure exists

Track ID Generation
-------------------

The skill generates track IDs using the format:  
{shortname}\_{YYYYMMDD}

Where the short name is derived from the task (kebab-case, 2-3 words). For example, “user-auth\_20260209” for a user authentication task.

Project Context Handling
------------------------

### Project Context Directory Structure

For normal projects: docs/plan/{trackId}/

### Knowledge Base Context Directory Structure

For documentation projects: docs/plan/{shortname}/

Quality Assurance and Validation
--------------------------------

The skill incorporates quality checks throughout the process:

* Architecture constraint validation from CLAUDE.md
* Testing pattern analysis from existing tests
* Dependency impact analysis using codegraph\_query
* Precedent validation from past sessions and knowledge bases

Deployment Integration
----------------------

If deployment infrastructure is detected (deploy.sh, Dockerfile, docker-compose.yml, fly.toml, wrangler.toml, etc.), the skill automatically includes a deploy phase in the implementation plan with concrete deployment commands and verification steps.

Benefits and Use Cases
----------------------

### Key Benefits

* **Zero questions** – Autonomous operation without user interaction
* **Comprehensive research** – Deep codebase analysis before planning
* **Context-aware** – Adapts to project structure and architecture
* **Quality-focused** – Incorporates existing patterns and constraints
* **Deployment-ready** – Includes deployment phases when applicable

### Ideal Use Cases

* Large feature development requiring detailed planning
* Bug fixes that need understanding of system impact
* Refactoring projects with complex dependencies
* Project setup and initial planning phases
* Documentation of implementation strategies

Integration with Build Process
------------------------------

The skill’s output is specifically designed to be parsed by the /build skill, with strict formatting requirements:

* Phase headers must use “## Phase N: Name” format
* Tasks must use [ ] (unchecked), [~] (in progress), or [x] (done) format
* Task descriptions must include concrete file paths
* Verification steps must be clearly defined

Conclusion
----------

The OpenClaw Solo Plan skill represents a sophisticated approach to automated software planning that combines deep codebase analysis with intelligent pattern recognition and quality assurance. By eliminating the need for interactive questions while still producing comprehensive, context-aware plans, it significantly accelerates the planning phase of software development projects.

Whether you’re working on a complex feature, fixing a critical bug, or refactoring legacy code, this skill provides the detailed, file-level implementation plans needed to execute with confidence and maintain high code quality standards.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/fortunto2/solo-plan/SKILL.md>
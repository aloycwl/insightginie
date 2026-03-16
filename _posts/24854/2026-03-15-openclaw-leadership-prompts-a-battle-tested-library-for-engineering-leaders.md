---
layout: post
title: "OpenClaw Leadership Prompts: A Battle-Tested Library for Engineering Leaders"
date: 2026-03-15T10:16:46
categories: [24854]
original_url: https://insightginie.com/openclaw-leadership-prompts-a-battle-tested-library-for-engineering-leaders
---

Introduction to OpenClaw Leadership Prompts
-------------------------------------------

The OpenClaw leadership-prompts skill is a comprehensive library of 25+ battle-tested prompts specifically designed for engineering leaders navigating the complex challenges of modern technical management. Created by Rob, an engineering manager with over 13 years of experience, this collection moves beyond generic leadership advice to provide specific, opinionated frameworks for the real situations engineering leaders face weekly.

What Makes These Prompts Different
----------------------------------

Unlike typical AI prompts that produce vague or generic responses, the leadership-prompts skill is built on several key design principles that ensure practical, actionable outcomes:

* **Forced structure** – Each prompt uses established frameworks like SBI (Situation-Behavior-Impact), RACI matrices, and RAG (Red-Amber-Green) status systems to produce organized, actionable outputs
* **Includes uncomfortable parts** – Prompts prepare you for defensive reactions, escalation paths, and difficult conversations rather than sugarcoating reality
* **Opinionated perspectives** – Based on real-world experience, not textbook theory. For example, the perspective that “the exec update is your team’s marketing” comes from years of practical application
* **Usable outputs** – Every prompt specifies an output format you can immediately use in meetings, documentation, or conversations
* **Acknowledges politics** – Real leadership happens in political contexts, so these prompts include stakeholder dynamics and organizational realities

Target Audience and Use Cases
-----------------------------

The leadership-prompts skill is specifically designed for:

* **Engineering Managers** running teams of 5-15 people
* **Tech Leads** navigating the individual contributor to management boundary
* **Directors and VPs** managing other managers
* **CTOs** who still maintain hands-on involvement

The prompts are organized into seven practical categories that align with common leadership scenarios:

### 1-on-1 Preparation (4 prompts)

Use these before any non-routine one-on-one conversation, such as performance discussions, career development talks, or conflict resolution meetings. The prompts help you structure difficult conversations and prepare for various outcomes.

### Team Health (4 prompts)

Reach for these after rough quarters, team conflicts, layoffs, or when remote teams feel disconnected. They help diagnose team dynamics and create actionable improvement plans.

### Incident Retrospectives (3 prompts)

Designed for use within 48 hours of incident resolution, these prompts guide thorough post-mortem analysis that goes beyond surface-level fixes to address systemic issues.

### Technical Strategy (4 prompts)

Perfect for quarterly planning, architecture reviews, and build-vs-buy decisions. These prompts help balance technical excellence with business constraints and team capabilities.

### Hiring and Interviews (3 prompts)

Use these when opening new roles, optimizing your hiring pipeline, or trying to close candidates. They address both tactical and strategic aspects of technical hiring.

### Career Development (4 prompts)

Essential for promotion cycles, delivering constructive feedback, and retention conversations. These prompts help you provide meaningful career guidance and identify growth opportunities.

### Stakeholder Communication (4 prompts)

Critical for executive updates, saying no to requests, achieving cross-functional alignment, and navigating organizational reorganizations. These prompts help you communicate effectively with non-technical stakeholders.

How to Use the Leadership Prompts
---------------------------------

### Using the CLI Tool

The skill includes a convenient command-line interface for browsing and accessing prompts:

```
# List all categories  
node scripts/leadership-prompts.js list  
  
# Get a random prompt for skill-building  
node scripts/leadership-prompts.js random  
  
# Search by keyword  
node scripts/leadership-prompts.js search "promotion"  
  
# Show a specific prompt by ID  
node scripts/leadership-prompts.js show career-dev-promotion  
  
# Get all prompts in a category  
node scripts/leadership-prompts.js category "Team Health"
```

### Integration with AI Assistants

You can also use these prompts directly with your favorite AI assistant:

```
I need to prepare for a 1-on-1 with an underperformer. Use the leadership-prompts skill to find the right prompt, then walk me through it.  
  
Or for browsing:  
Show me all the hiring prompts from leadership-prompts
```

### Using Individual Prompts

Each prompt contains placeholder variables in curly braces that you need to fill with your specific context. The more specific you are, the better the output. For example:

```
Prompt: I'm preparing for a 1-on-1 with a direct report who has been underperforming for the past {timeframe}...  
  
Your fill-in: I'm preparing for a 1-on-1 with a direct report who has been underperforming for the past 6 weeks...
```

Quick Start Guide
-----------------

For new users, here’s a practical way to get started:

1. Identify your current leadership challenge (e.g., “I need to give difficult feedback to a team member”)
2. Browse the relevant category (in this case, Career Development or 1-on-1 Prep)
3. Read the prompt and context to ensure it matches your situation
4. Fill in the placeholder variables with your specific context
5. Follow the output format specification to create actionable deliverables
6. Practice the conversation or meeting using the structured output

Adding Custom Prompts
---------------------

The library is designed to be extensible. You can add your own prompts by editing the prompts.json file following the existing schema:

```
{  
  "id": "category-short-name",  
  "category": "Category Name",  
  "title": "Human-readable title",  
  "prompt": "The actual prompt text with {variables}",  
  "context": "When to use this prompt",  
  "output_format": "What the AI should produce",  
  "example": "A filled-in example showing real usage"  
}
```

Real-World Impact
-----------------

The leadership-prompts skill isn’t just theoretical – it’s been battle-tested in real engineering organizations. The prompts address actual situations that engineering leaders encounter:

* Preparing for difficult performance conversations with concrete frameworks
* Conducting effective incident retrospectives that lead to real improvements
* Navigating stakeholder politics during critical decision-making
* Developing team members through structured career conversations
* Making build-vs-buy decisions with clear evaluation criteria

License and Attribution
-----------------------

The leadership-prompts skill is released under the MIT license, making it freely available for use, modification, and distribution. The skill was created by Rob, who has been an engineering manager since 2011 and currently runs leadingin.tech, a resource for engineering leadership.

Conclusion
----------

The OpenClaw leadership-prompts skill represents a practical approach to engineering leadership development. Rather than providing abstract advice, it offers specific, actionable frameworks for the most common and challenging situations engineering leaders face. Whether you’re a new engineering manager or a seasoned CTO, these prompts can help you navigate complex leadership situations with greater confidence and effectiveness.

By providing structure for difficult conversations, forcing consideration of uncomfortable aspects, and producing immediately usable outputs, the leadership-prompts skill bridges the gap between leadership theory and practical application. It’s a valuable tool for any engineering leader looking to improve their management skills and team outcomes.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/robansuini/leadership-prompts/SKILL.md>
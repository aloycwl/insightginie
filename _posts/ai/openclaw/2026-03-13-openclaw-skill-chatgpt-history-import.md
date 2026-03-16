---
layout: post
title: "OpenClaw Skill: ChatGPT History Import"
date: 2026-03-13T18:16:37
categories: [24854]
original_url: https://insightginie.com/openclaw-skill-chatgpt-history-import
---

What This Skill Does
--------------------

The ChatGPT History Import skill allows you to seamlessly migrate your ChatGPT conversations into OpenClaw's memory search system. This powerful feature enables you to maintain continuity with your previous AI interactions by making all your past ChatGPT conversations searchable within OpenClaw.

Why You Need This Skill
-----------------------

If you're transitioning from ChatGPT to OpenClaw, this skill solves a critical problem: losing access to your conversation history. By importing your ChatGPT conversations, you can:

* Continue building on previous discussions without starting from scratch
* Search through past conversations for specific information or insights
* Create a comprehensive archive of your AI interactions
* Maintain context across different AI platforms

How It Works
------------

The skill follows a straightforward four-step process that transforms your ChatGPT conversations into searchable OpenClaw memories:

### Step 1: Export from ChatGPT

Begin by downloading your conversation history from ChatGPT using OpenAI's export tools. You'll receive a `conversations.json` file containing all your chat data.

### Step 2: Convert to Markdown

The skill includes a conversion script that transforms the JSON data into individual Markdown files. This format is optimized for embedding and makes your conversations more readable and searchable.

### Step 3: Embed into SQLite Database

Using OpenAI's embedding API, the skill processes each conversation and stores it in a SQLite database. This creates a searchable index that OpenClaw can access efficiently.

### Step 4: Configure OpenClaw

Finally, you add the generated database as an extra search path in your OpenClaw configuration. After restarting the gateway, your ChatGPT conversations become fully integrated into OpenClaw's memory search.

Technical Requirements
----------------------

The skill requires an OpenAI API key for embedding conversations. The process is cost-effective, with approximately 2,400 conversations costing around $0.15 using the `text-embedding-3-small` model. The skill also includes safety features like refusing to overwrite existing databases and not storing your API key in the output.

Key Benefits
------------

* **Seamless Migration**: Transition from ChatGPT to OpenClaw without losing valuable conversation history
* **Enhanced Searchability**: Access your entire conversation history through OpenClaw's powerful memory search
* **Cost-Effective**: Minimal embedding costs make it practical for large conversation archives
* **Privacy-Focused**: No API keys stored in the final database, and you can filter sensitive content before processing

Getting Started
---------------

To use this skill, you'll need to follow the workflow outlined in the documentation. The process is well-documented with clear steps and options for customization, such as filtering trivial conversations and adjusting batch sizes for embedding.

Who Should Use This
-------------------

This skill is ideal for anyone migrating from ChatGPT to OpenClaw, users who want to maintain searchable archives of their AI conversations, or teams building knowledge bases from past AI interactions. It's particularly valuable for professionals who rely on AI assistants for research, writing, or problem-solving and need to reference past conversations.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/samdickson22/chatgpt-import/SKILL.md>
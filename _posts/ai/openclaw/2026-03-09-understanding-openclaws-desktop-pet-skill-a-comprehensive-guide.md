---
layout: post
title: "Understanding OpenClaw&#8217;s Desktop Pet Skill: A Comprehensive Guide"
date: 2026-03-09T06:45:32
categories: [24854]
original_url: https://insightginie.com/understanding-openclaws-desktop-pet-skill-a-comprehensive-guide
---

Understanding OpenClaw's Desktop Pet Skill: A Comprehensive Guide
=================================================================

Welcome to our comprehensive guide on OpenClaw's Desktop Pet skill. This skill, named *mu-pet*, is a delightful pixel art desktop pet that enhances user interaction on macOS. In this article, we will delve into its features, functionalities, and how you can integrate it with your agent. We will also guide you through the customization process and the auto-launch feature.

Introduction to OpenClaw's Desktop Pet Skill
--------------------------------------------

OpenClaw's Desktop Pet skill is a charming animated pixel art character that roams your screen as an always-on-top Electron overlay. The pet, by default a lobster, avoids the cursor and active windows, walks along screen edges, climbs walls and ceilings, and responds to agent state changes via a local HTTP API. It's the perfect companion for those who want a desktop buddy, a virtual pet, or a visual indicator of agent activity.

Features of the Desktop Pet Skill
---------------------------------

The Desktop Pet skill comes with a variety of features that make it an engaging and interactive addition to your desktop. Here are some highlights:

* **Animated Pixel Art**: The pet is a cute lobster by default, drawn programmatically via Canvas pixel art.
* **Transparent Overlay**: The pet roams your desktop without getting in the way, thanks to its transparent overlay feature.
* **Always-on-Top**: The pet stays visible on top of all windows, making it a constant companion.
* **Click-Through**: The pet allows you to click through it, except when you click on the pet itself.
* **Roams Full Desktop**: The pet can move around your entire desktop, including the floor, walls, and ceiling.
* **Avoids Cursor and Active Windows**: The pet maintains a safe distance from your cursor and active windows, allowing you to work without distractions.
* **Responds to Agent State Changes**: The pet changes its behavior based on the agent's state, such as idle, walking, working, thinking, sleeping, and talking.
* **Speech Bubbles**: The pet can display speech bubbles with auto-sizing duration, adding a touch of realism to the interaction.
* **Right-Click Context Menu**: You can manually control the pet's state using the right-click context menu.

Agent Integration
-----------------

Integrating the Desktop Pet skill with your agent is a straightforward process. You can use the local HTTP API to set the pet's state and make it face the user. For instance, you can set the pet to the *talking* state at the start of responses to make the pet face the user. Here's an example:

```
curl -s -X POST http://127.0.0.1:18891/state  

-H 'Content-Type: application/json'  

-d '{

Skill can be found at: https://github.com/openclaw/skills/tree/main/skills/samskrta/mu-pet/SKILL.md
```
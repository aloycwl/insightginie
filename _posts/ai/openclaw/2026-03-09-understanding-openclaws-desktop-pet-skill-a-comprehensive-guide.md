---
layout: post
title: 'Understanding OpenClaw&#8217;s Desktop Pet Skill: A Comprehensive Guide'
date: '2026-03-09T06:45:32'
categories:
- ai
- openclaw
original_url: https://insightginie.com/understanding-openclaws-desktop-pet-skill-a-comprehensive-guide/
featured_image: /media/images/8160.jpg
---

<article>
<h1>Understanding OpenClaw&#8217;s Desktop Pet Skill: A Comprehensive Guide</h1>
<p>Welcome to our comprehensive guide on OpenClaw&#8217;s Desktop Pet skill. This skill, named <em>mu-pet</em>, is a delightful pixel art desktop pet that enhances user interaction on macOS. In this article, we will delve into its features, functionalities, and how you can integrate it with your agent. We will also guide you through the customization process and the auto-launch feature.</p>
<h2>Introduction to OpenClaw&#8217;s Desktop Pet Skill</h2>
<p>OpenClaw&#8217;s Desktop Pet skill is a charming animated pixel art character that roams your screen as an always-on-top Electron overlay. The pet, by default a lobster, avoids the cursor and active windows, walks along screen edges, climbs walls and ceilings, and responds to agent state changes via a local HTTP API. It&#8217;s the perfect companion for those who want a desktop buddy, a virtual pet, or a visual indicator of agent activity.</p>
<h2>Features of the Desktop Pet Skill</h2>
<p>The Desktop Pet skill comes with a variety of features that make it an engaging and interactive addition to your desktop. Here are some highlights:</p>
<ul>
<li><strong>Animated Pixel Art</strong>: The pet is a cute lobster by default, drawn programmatically via Canvas pixel art.</li>
<li><strong>Transparent Overlay</strong>: The pet roams your desktop without getting in the way, thanks to its transparent overlay feature.</li>
<li><strong>Always-on-Top</strong>: The pet stays visible on top of all windows, making it a constant companion.</li>
<li><strong>Click-Through</strong>: The pet allows you to click through it, except when you click on the pet itself.</li>
<li><strong>Roams Full Desktop</strong>: The pet can move around your entire desktop, including the floor, walls, and ceiling.</li>
<li><strong>Avoids Cursor and Active Windows</strong>: The pet maintains a safe distance from your cursor and active windows, allowing you to work without distractions.</li>
<li><strong>Responds to Agent State Changes</strong>: The pet changes its behavior based on the agent&#8217;s state, such as idle, walking, working, thinking, sleeping, and talking.</li>
<li><strong>Speech Bubbles</strong>: The pet can display speech bubbles with auto-sizing duration, adding a touch of realism to the interaction.</li>
<li><strong>Right-Click Context Menu</strong>: You can manually control the pet&#8217;s state using the right-click context menu.</li>
</ul>
<h2>Agent Integration</h2>
<p>Integrating the Desktop Pet skill with your agent is a straightforward process. You can use the local HTTP API to set the pet&#8217;s state and make it face the user. For instance, you can set the pet to the <em>talking</em> state at the start of responses to make the pet face the user. Here&#8217;s an example:</p>
<pre><code>curl -s -X POST http://127.0.0.1:18891/state<br />
-H 'Content-Type: application/json'<br />
-d '{</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/samskrta/mu-pet/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/samskrta/mu-pet/SKILL.md</a></p>

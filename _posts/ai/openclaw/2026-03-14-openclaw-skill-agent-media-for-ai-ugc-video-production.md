---
layout: post
title: "OpenClaw Skill: Agent Media for AI UGC Video Production"
date: 2026-03-14T18:16:02
categories: [24854]
original_url: https://insightginie.com/openclaw-skill-agent-media-for-ai-ugc-video-production
---

What is the Agent Media Skill?
------------------------------

The Agent Media skill in OpenClaw is a powerful tool for creating AI-powered user-generated content (UGC) videos directly from your terminal. This skill leverages the agent-media CLI to produce complete videos with talking heads, B-roll footage, voiceover, and animated subtitles.

Core Functionality
------------------

The skill transforms scripts into professional videos by combining several AI technologies:

* **AI Talking Heads** – Create videos with realistic lip-synced avatars
* **B-roll Integration** – Add contextual cutaway scenes to enhance storytelling
* **Automated Subtitles** – Generate animated captions with various styling options
* **Voice Synthesis** – Convert text to natural-sounding speech
* **Background Music** – Add appropriate audio tracks to match video tone

Mandatory Rules for Video Creation
----------------------------------

The skill enforces several critical rules to ensure video quality:

1. **Always use –actor** – Every video must include a talking head for lip sync; otherwise, you'll just get a static image with voiceover
2. **Word count matters** – Natural speech is 2.5 words per second; scripts must match target duration (5s = ~12 words, 10s = ~25 words, 15s = ~37 words)
3. **SaaS reviews need screenshots** – Product reviews must include 1-3 screenshots via –broll-images for context
4. **Product name required** – SaaS reviews must specify the product name for subtitles
5. **Always use –sync** – Wait for completion and get the output URL
6. **Descriptive filenames** – B-roll images should have descriptive names for semantic matching

Installation and Setup
----------------------

Before using the skill, you need to install and authenticate the agent-media CLI:

```
npm install -g agent-media-cli
agent-media login
agent-media whoami
```

UGC Video Pipeline
------------------

The flagship feature transforms scripts through this workflow:

1. Script → Scene splitting
2. TTS voiceover generation
3. AI talking heads + B-roll integration
4. Crossfade assembly
5. Animated subtitles
6. Background music addition
7. End screen CTA

Basic Usage Examples
--------------------

### Simple UGC Video

```
agent-media ugc "Ever wonder why some videos go viral? Here's the secret..." --actor sofia --sync
```

### From Script File

```
agent-media ugc ./script.txt --actor naomi --sync
```

### AI-Generated Script

```
agent-media ugc -g "A fitness tracker that monitors sleep quality" --actor marcus --sync
```

### With B-roll

```
agent-media ugc "Your script here..." --actor marcus --broll --sync
```

### SaaS Review with Screenshots

```
agent-media ugc "Your script here..." --actor sofia --broll --broll-images https://example.com/screenshot1./media/images/png,https://example.com/screenshot2./media/images/png --sync
```

Available Flags
---------------

The skill supports numerous customization options:

* `--actor <slug>` – Library actor for talking heads
* `--persona <slug>` – Custom persona (cloned voice + face)
* `--face-url <url>` – Direct face photo URL or local file
* `--voice <name>` – TTS voice selection
* `--tone <name>` – Voice tone (energetic, calm, confident, dramatic)
* `--style <name>` – Subtitle style (hormozi, minimal, bold, etc.)
* `-d, --duration <s>` – Target duration (5, 10, or 15 seconds)
* `--aspect <ratio>` – Aspect ratio (9:16, 16:9, 1:1)
* `--music <genre>` – Background music genre
* `--cta <text>` – End screen call-to-action
* `--broll` – Enable B-roll cutaway scenes
* `--broll-images <urls>` – Comma-separated screenshot/image URLs
* `--template <slug>` – Script template selection
* `-g, --generate-script <prompt>` – AI-generate script from description
* `--product-url <url>` – Product URL for script generation context
* `-s, --sync` – Wait for completion and print output URL

Script Templates
----------------

The skill offers various templates for different video types:

* **monologue** – Hook → Body → CTA (direct-to-camera talking)
* **testimonial** – Problem → Solution → Result → CTA (customer stories)
* **product-review** – Intro → Experience → Verdict → CTA (product reviews)
* **problem-solution** – Hook → Pain → Solution → CTA (before/after pain points)
* **saas-review** – Hook → Walkthrough → Opinion → CTA (SaaS/app reviews)
* **before-after** – Hook → Before → After → CTA (transformations)
* **listicle** – Hook → Tip 1 → Tip 2 → Tip 3 + CTA (tips and lists)
* **product-demo** – Intro → Demo → Recap → CTA (product walkthroughs)

Subtitle Styles
---------------

Available subtitle styles include:

* **hormozi** – Yellow karaoke highlight (default)
* **minimal** – Clean, simple styling
* **bold** – Neon cyan styling
* **karaoke** – Green pop highlight
* **clean** – White on dark background
* **tiktok** – Popular social media style
* **neon** – Bright neon effects

SaaS Review Video Workflow
--------------------------

For SaaS reviews, follow this exact process:

1. Get product name – Ask user if not provided
2. Get 1-3 screenshot URLs – Visit product site if needed
3. Pick an actor – Default to naomi or sofia if unspecified
4. Write script – Match word count to duration (2.5 words/sec)
5. Run command – Include all required flags

Benefits of Using This Skill
----------------------------

The Agent Media skill streamlines video production by:

* **Saving time** – Create professional videos in minutes instead of hours
* **Ensuring consistency** – Standardized formatting and quality across videos
* **Reducing complexity** – No need for video editing expertise
* **Scaling content** – Produce multiple videos quickly for different products or topics
* **Maintaining quality** – Built-in rules prevent common video production mistakes

Conclusion
----------

The Agent Media skill in OpenClaw is an essential tool for anyone needing to create professional UGC videos quickly and efficiently. By following the mandatory rules and using the various customization options, you can produce high-quality videos that engage viewers and effectively communicate your message.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/nevo-david/agent-media/SKILL.md>
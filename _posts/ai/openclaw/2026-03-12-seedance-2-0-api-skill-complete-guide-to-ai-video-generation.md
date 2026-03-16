---
layout: post
title: "Seedance 2.0 API Skill: Complete Guide to AI Video Generation"
date: 2026-03-12T03:16:55
categories: [24854]
original_url: https://insightginie.com/seedance-2-0-api-skill-complete-guide-to-ai-video-generation
---

What is the Seedance 2.0 API Skill?
-----------------------------------

The Seedance 2.0 API skill is an open-source workflow tool that enables end-to-end AI video generation. It builds storyboards, generates reference images using Seedream 4.5, submits video tasks, and polls results automatically. This skill supports both MCP (Model Context Protocol) and standalone Python script execution modes, making it versatile for different development environments.

Key Features
------------

* End-to-end workflow from concept to final video
* Storyboard creation with 5-dimensional deep dive
* Reference image generation using Seedream 4.5
* Two generation modes: Omni Reference and First & Last Frames
* Support for MCP and standalone Python script execution
* Asset management for images, videos, and audio

Prerequisites
-------------

Before using this skill, ensure you have:

* Python 3.8 or higher
* requests library installed
* XSKILL\_API\_KEY environment variable set
* Cursor, Claude Code, or any SKILL.md-compatible agent

Execution Modes: MCP vs Script
------------------------------

### Step 0: Determine Execution Mode

The skill automatically detects whether to use MCP or script mode:

1. Check MCP availability by reading `mcps/user-xskill-ai/STATUS.md`
2. If MCP is available, use `submit_task` and `get_task` tools
3. If MCP is unavailable, switch to script mode

### Script Mode Setup

If using script mode, verify:

* XSKILL\_API\_KEY is set: `echo $XSKILL_API_KEY | head -c 10`
* requests library is installed: `pip install requests`
* Script location: `.cursor/skills/seedance2-api/scripts/seedance_api.py`

Step-by-Step Workflow
---------------------

### Step 1: Understand the User's Idea

Collect essential information:

* Story concept: one-sentence summary
* Duration: 4-15 seconds
* Aspect ratio: 16:9, 9:16, 1:1, 21:9, 4:3, or 3:4
* Visual style: realistic, animation, ink wash, sci-fi, cyberpunk, etc.
* Assets: existing images/videos/audio or need AI generation
* Function mode: first\_last\_frames or omni\_reference

### Step 2: Deep Dive Analysis

Guide users through 5 dimensions for richer detail:

* Content: Who, what, where
* Visuals: Lighting, color palette, texture, mood
* Camera: Push in, pull out, pan, tilt, track, orbit, crane
* Motion: Subject actions and pacing
* Audio: Music style, sound effects, dialogue

### Step 3: Build Storyboard Structure

Use this formula to structure your storyboard:

```
[Style] _____ style, _____ seconds, _____ ratio, _____ mood
0-Xs: [Camera movement] + [Visual content] + [Action description]
X-Ys: [Camera movement] + [Visual content] + [Action description]
...
[Audio] _____ music + _____ SFX + _____ dialogue
[References] @image_file_1 _____, @video_file_1 _____
```

### Step 4: Generate Reference Images

Generate images using Seedream 4.5 if needed:

#### Text-to-Image Generation

```
MCP Method:
submit_task with model_id: fal-ai/bytedance/seedream/v4.5/text-to-image
Script Method:
python seedance_api.py submit --model "fal-ai/bytedance/seedream/v4.5/text-to-image" --params '{"prompt":"...", "image_size":"landscape_16_9", "num_images":1}'
```

#### Image Editing

```
MCP Method:
submit_task with model_id: fal-ai/bytedance/seedream/v4.5/edit
Script Method:
python seedance_api.py submit --model "fal-ai/bytedance/seedream/v4.5/edit" --params '{"prompt":"...", "image_urls":[...], "image_size":"landscape_16_9"}'
```

#### Poll Image Results

```
MCP Method:
get_task tool, first query after 30s, then every 30s
Script Method:
python seedance_api.py poll --task-id "TASK_ID" --interval 10 --timeout 180
```

### Step 5: Compose Final Prompt

Merge storyboard and references using @image\_file\_N, @video\_file\_N, @audio\_file\_N syntax:

```
@image_file_1 as character reference, follow @video_file_1 camera movement, with @audio_file_1 as background music
```

### Step 6: Submit Video Task

#### Upload Local Images

```
MCP Method:
upload_image tool
Script Method:
python seedance_api.py upload --image-url "https://..." or --image-path "/path/to/image.png"
```

#### Submit Seedance 2.0 Task

```
MCP Method:
submit_task with model_id: st-ai/super-seed2
Script Method:
python seedance_api.py submit --model "st-ai/super-seed2" --params '{"prompt":"...", "functionMode":"omni_reference", "image_files":[...], "ratio":"16:9", "duration":15, "model":"seedance_2.0_fast"}'
```

Aspect Ratio Reference
----------------------

| Aspect Ratio | Recommended image\_size | Note |
| --- | --- | --- |
| 16:9 | landscape\_16\_9 | Landscape |
| 9:16 | portrait\_16\_9 | Portrait |
| 4:3 | landscape\_4\_3 | Landscape |
| 3:4 | portrait\_4\_3 | Portrait |
| 1:1 | square\_hd | Square |
| 21:9 | landscape\_16\_9 | Approximate ultrawide |

Function Modes
--------------

### Omni Reference Mode

Default mode that uses multiple reference images for context. Parameters include:

* prompt: Full video description
* functionMode: omni\_reference
* image\_files: Up to 9 reference images
* video\_files: Up to 3 reference videos (≤15s total)
* audio\_files: Up to 3 reference audio clips
* ratio: Aspect ratio
* duration: Video length (4-15 seconds)
* model: seedance\_2.0\_fast or seedance\_2.0

### First & Last Frames Mode

Mode that controls only the first and last frames:

* prompt: Video description
* functionMode: first\_last\_frames
* filePaths: Array of image URLs (0 = text-to-video)

Getting Started
---------------

1. Set up your API key: `export XSKILL_API_KEY=sk-your-api-key`
2. Install dependencies: `pip install requests`
3. Choose your execution mode (MCP or script)
4. Follow the 6-step workflow above

Support and Resources
---------------------

Get your API key at: <https://www.xskill.ai/#/v2/api-keys>

Documentation and examples available in the skill's reference.md file.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/tony6830377-arch/seedance2-api/SKILL.md>
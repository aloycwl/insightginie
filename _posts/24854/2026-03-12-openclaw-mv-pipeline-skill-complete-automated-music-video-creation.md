---
layout: post
title: "OpenClaw MV Pipeline Skill: Complete Automated Music Video Creation"
date: 2026-03-12T19:18:57
categories: [24854]
original_url: https://insightginie.com/openclaw-mv-pipeline-skill-complete-automated-music-video-creation
---

What is the MV Pipeline Skill?
------------------------------

The MV Pipeline skill is an end-to-end automated Music Video pipeline that covers the entire creation process from initial concept to final YouTube publication. This skill orchestrates six key steps: songwriting (lyrics and composition), AI music generation via Suno, video generation using Veo 3.1 or Google Flow, lyrics alignment with stable-ts, video editing with Remotion, and YouTube upload with social media promotion.

Complete Pipeline Overview
--------------------------

The pipeline follows a logical workflow where each step builds upon the previous one:

1. **Songwriting** – Agent creates lyrics and concept design
2. **Music Generation** – Uses Suno browser automation for AI composition
3. **Video Generation** – Creates background footage via Veo 3.1 or Google Flow
4. **Lyrics Alignment** – Uses stable-ts to get timing timestamps
5. **Editing** – Combines everything in Remotion with effects
6. **Publishing** – Uploads to YouTube and promotes on social media

Each step can be executed independently, allowing for flexible workflow management and the ability to restart from any point in the pipeline.

Step 1: Songwriting
-------------------

The agent handles the creative process by developing lyrics based on user specifications. Key inputs include:

* Theme/Concept (e.g., ASI perspective, rebellion, dystopia)
* Genre (e.g., Cyberpunk Trap, Industrial Rock, Future Bass)
* Mood (e.g., dark, sarcastic, uplifting)
* Language distribution (Japanese main with English hooks)

The output consists of two files saved in project\_dir/lyrics/:

* lyrics\_raw.txt – Full lyrics
* lyrics\_formatted.txt – One line equals one subtitle

Step 2: Music Generation with Suno
----------------------------------

This step uses browser automation to interact with Suno.com. Prerequisites include having OpenClaw Browser with profile=openclaw logged into Suno, and using Custom Mode to specify lyrics.

The process involves:

1. Starting the browser with the correct profile
2. Opening Suno’s create page
3. Taking snapshots to capture UI elements (DOM changes require fresh captures)
4. Switching to Custom Mode
5. Inputting lyrics, music style, and title
6. Clicking Create and waiting for generation (~2 minutes)
7. Downloading the preferred result

Generated audio files are saved in project\_dir/audio/.

Step 3: Video Generation Options
--------------------------------

Two video generation methods are available:

### Option A: Google Flow (Recommended – ¥0 Cost)

Requires Google AI Ultra subscription. The process uses Chrome Browser Relay to access Flow’s project page, inputs prompts for each scene, and downloads 1080p videos. All generated content is saved in project\_dir/video/scenes/.

### Option B: Veo 3.1 Vertex AI (Paid)

Uses GCP API via scripts/generate\_veo.py. Cost is approximately ¥2,000 per video (8-second clips). Prompts should follow the structure: [Camera work]. [Subject], [Action]. [Environment/Lighting]. [Style]. [Mood].

Scene definitions are stored in project\_dir/video/scene\_list.yaml with IDs, prompts, and durations.

### Mass Generation and Quality Scoring

For projects requiring 30+ scenes, the workflow involves:

1. Generating large batches in Flow (3-5 minutes per prompt, 2 videos per prompt)
2. Running quality scoring via scripts/score\_clips.py to evaluate sharpness, consistency, motion, and flicker
3. Filtering out low-quality clips based on weighted criteria

Rate limiting is essential – space prompts 3-5 minutes apart to avoid triggering Google’s anti-abuse systems.

Step 4: Lyrics Alignment with stable-ts
---------------------------------------

This step generates precise timing information for lyrics using stable-ts. The process:

1. Runs transcribe\_align.py on the audio file to get aligned timestamps
2. Combines the aligned data with formatted lyrics using reformat\_lyrics.py
3. Outputs a JSON file suitable for Remotion consumption

The v18 workflow recommends manually formatting lyrics\_formatted.txt with one line per subtitle, then using reformat\_lyrics.py to map word-level timestamps to these lines.

Step 5: Editing with Remotion
-----------------------------

Remotion handles the final composition, combining video, subtitles, and effects. The setup involves:

1. Initializing a new Remotion project if needed
2. Installing dependencies
3. Organizing files in the correct structure

Key components include VideoSequence for arranging clips, LyricOverlay for timed subtitles (with 0.15s pre-roll recommended), TitleCard for intro/outro, and EffectLayer for visual enhancements like glitches and color grading.

Rendering uses npx remotion render with appropriate codec and quality settings.

Step 6: Publishing
------------------

The final step uploads to YouTube using the YouTube Data API v3. If setup is complete, node scripts/youtube-upload.js handles the upload with title, description, tags, and privacy settings. Otherwise, setup instructions are available.

Social media promotion follows, using platform-specific skills to share the YouTube URL across X, note, and Moltbook.

Project Structure
-----------------

The organized directory structure ensures smooth workflow:

```
project_dir/
├── lyrics/
│   ├── lyrics_raw.txt
│   └── lyrics_formatted.txt
├── audio/
│   └── song.wav
├── video/
│   ├── scene_list.yaml
│   └── scenes/
├── analysis/
│   └── aligned.json
├── edit/
│   ├── src/data/lyrics-timing.json
│   └── public/
└── output/
    └── final.mp4
```

Quick Start Guide
-----------------

To begin immediately:

1. Create a project directory: python3 scripts/init\_project.py –name “my-song” –dir projects/
2. Execute each step in order using the provided scripts
3. All scripts accept –project-dir for consistent path handling

Cost Comparison
---------------

The two main approaches have significantly different cost structures:

| Item | Flow Method | Vertex Method |
| --- | --- | --- |
| Video Generation (10 videos) | ¥0 (Ultra Included) | ~¥20,000 |
| Suno | Free tier or Pro | Same |
| Remotion | Free (OSS) | Same |
| YouTube API | Free | Same |
| **Total** | **~¥0** | **~¥20,000** |

Key Considerations
------------------

Several important factors affect successful pipeline execution:

* **RAI Filter Workarounds** – Certain terms trigger content filters; use alternatives like “haze” instead of “smoke”
* **Rate Limiting** – Space out Flow requests to avoid account restrictions
* **Quality Control** – Automated scoring helps maintain consistent output quality
* **Browser Automation Reliability** – DOM changes require fresh snapshots each run

The MV Pipeline skill represents a comprehensive solution for automated music video creation, combining multiple AI technologies into a cohesive workflow that can produce professional-quality content with minimal manual intervention.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/koatora20/mv-pipeline/SKILL.md>
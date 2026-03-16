---
layout: post
title: "YouTube Long Video Transcript &#038; Translation Skill Explained"
date: 2026-03-13T03:15:48
categories: [24854]
original_url: https://insightginie.com/youtube-long-video-transcript-translation-skill-explained
---

What This Skill Does
--------------------

This skill provides a complete workflow for transcribing and translating YouTube videos longer than one hour. It uses the DownSub API to extract subtitles from YouTube videos and handles the entire process from extraction to final translation.

### Core Functionality

The skill performs four main tasks:

1. Extracts subtitles from YouTube videos using the DownSub API
2. Translates English transcripts to Chinese verbatim
3. Handles long videos that exceed session limits through chunked processing
4. Processes DownSub API responses and generates formatted documents

### Technical Requirements

The skill requires several key components to function:

* DownSub API key (Bearer token starting with AIza…)
* zhiyan tool (optional, for online document generation)
* Sub-agent spawn capability for processing long videos

### API Configuration

The skill connects to the DownSub API at https://api.downsub.com/download using POST method with these headers:

* Authorization: Bearer AIzaM9ifctIOxusNAldvGeajHqq4rH6e7MJNfN
* Content-Type: application/json

The body contains the YouTube video URL in this format:

```
{ "url": "https://www.youtube.com/watch?v=VIDEO_ID" }
```

### Critical Language Check

The skill performs a crucial language validation step:

* Always checks the lang field in the API response
* Only processes en or en-auto language codes
* Stops processing if it detects other languages like lt (Lithuanian)

### Three-Stage Workflow

#### Stage 1: Preparation (Main Session)

The main session verifies API access, checks output capabilities, and determines if sub-agent processing is needed based on video length.

#### Stage 2: Execution (Sub-Agent)

For long videos, a sub-agent processes the transcript in 500-line chunks, translates to Chinese, and creates separate files. It also generates an executive summary and key metrics table.

#### Stage 3: Delivery (Main Session)

The main session receives the final file path, uploads it using zhiyan if available, and sends the document link or file to the user.

### Common Issues and Solutions

The skill includes troubleshooting for common problems:

* Missing API key (401 Unauthorized errors)
* zhiyan tool not found
* Wrong subtitle track (nonsense translations)
* Timeouts for very long videos

### Output Format

The final output includes:

* Executive summary (3-5 bullets in Chinese)
* Key metrics table
* Full translated transcript

This skill is specifically designed for users who need to process long YouTube videos that exceed typical session limits, providing a robust solution for video transcription and translation workflows.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/qingliu1617-art/ytb-transcript-long/SKILL.md>
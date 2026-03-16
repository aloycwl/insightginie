---
layout: post
title: "Tencent Meeting Export Skill: Extract Complete Meeting Transcripts from Public Links"
date: 2026-03-09T12:17:31
categories: [24854]
original_url: https://insightginie.com/tencent-meeting-export-skill-extract-complete-meeting-transcripts-from-public-links
---

What This Skill Does
--------------------

The Tencent Meeting Export skill is a powerful tool designed to extract complete meeting transcription data from Tencent Meeting (腾讯会议) public share links. This skill is particularly useful when you need to access AI-generated summaries, smart chapters, critical events, or full transcriptions from Tencent Meeting cloud recordings that have been shared publicly.

The skill supports exporting data in both Markdown and JSON formats, complete with speaker identification and precise timestamps, making it an invaluable resource for meeting documentation, content analysis, and knowledge management.

Key Features and Export Capabilities
------------------------------------

The skill can extract four main types of content from Tencent Meeting recordings:

1. **AI Full Summary**: Tencent Meeting’s automatically generated meeting summary that provides a concise overview of the entire meeting.
2. **Smart Chapters**: Automatically segmented content organized by topic, complete with timestamps and brief summaries for each section.
3. **Critical Events**: Important meeting moments such as screen sharing start/stop events, member join/leave notifications, and other significant occurrences.
4. **Complete Transcription**: Detailed paragraph-by-paragraph speech-to-text conversion with speaker identification and precise timestamps.

Prerequisites and Setup
-----------------------

Before using this skill, you’ll need to install the required dependencies:

```
pip install playwright
playwright install chromium
```

The skill uses Playwright with a headless Chromium browser to interact with Tencent Meeting’s web interface, ensuring reliable data extraction without manual intervention.

Basic Usage
-----------

The skill is straightforward to use from the command line. Here’s the basic syntax:

```
python scripts/tencent_meeting_export.py <share_link>
```

For example, to export a meeting transcript to a Markdown file:

```
python scripts/tencent_meeting_export.py https://meeting.tencent.com/cw/xxxxx -o meeting_summary.md
```

Advanced Options
----------------

The skill offers several useful options for customizing the export process:

* **Output File**: Use `-o` or `--output` to specify the output file path (default: `meeting_transcript.md`).
* **JSON Export**: Add `--json` to simultaneously export raw JSON data alongside Markdown.
* **JSON Only**: Use `--json-only` to export only JSON data without generating Markdown.
* **Timeout**: Adjust page load timeout with `--timeout` (default: 60 seconds).
* **Quiet Mode**: Use `-q` or `--quiet` for silent operation without progress messages.

Technical Implementation
------------------------

The skill works by using Playwright to load the Tencent Meeting share page in a headless browser. It then intercepts API requests to extract various data types:

+ `v1/minutes/detail` – Transcription paragraphs (lazy-loaded pagination)
+ `get-full-summary` – AI-generated summary
+ `get-chapter` – Smart chapter segmentation
+ `get-critical-node` – Critical event nodes
+ `common-record-info` – Meeting metadata

The script automatically clicks the “Transcription” tab and scrolls to load all content before formatting and exporting the data.

Data Structure
--------------

The exported transcription data includes detailed paragraph structures with these key fields:

```
paragraph
├── start_time / end_time (timestamp in milliseconds)
├── speaker
│   ├── user_id
│   ├── user_name ← Speaker name
│   └── avatar_url
└── sentences[]
└── words[]
└── text ← Transcription text
```

Limitations
-----------

Currently, the skill has these limitations:

+ Only works with publicly shared meeting recordings (no login required)
+ Requires the meeting to have transcription/subtitle functionality enabled
+ The share link must be within its valid period
+ Depends on Tencent Meeting’s current page structure and APIs, which may change and require script updates

Programming Interface
---------------------

For developers who want to integrate this functionality into their own applications, the skill provides a Python API:

```
import asyncio
from scripts.tencent_meeting_export import TranscriptCapture, format_markdown

async def export():
    capture = TranscriptCapture("https://meeting.tencent.com/cw/xxxxx")
    data = await capture.capture()
    md = format_markdown(data)
    print(md)

asyncio.run(export())
```

Practical Use Cases
-------------------

This skill is valuable for various scenarios:

+ Creating meeting minutes from recorded sessions
+ Extracting key discussion points for documentation
+ Analyzing meeting content for research or compliance purposes
+ Building searchable knowledge bases from meeting recordings
+ Integrating meeting content into learning management systems
+ Generating content summaries for busy executives

Why This Skill Matters
----------------------

As remote work and online meetings become increasingly prevalent, the ability to efficiently extract and utilize meeting content is crucial. This skill bridges the gap between Tencent Meeting’s recording capabilities and practical content management needs, saving users countless hours of manual transcription and content organization.

By automating the extraction of structured meeting data, it enables better knowledge sharing, improved documentation, and more effective use of recorded meeting content across organizations.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/snow-dust/tencent-meeting-export/SKILL.md>
---
layout: post
title: "Video Analyzer Skill: Transcribe and Analyze Videos with Local Processing"
date: 2026-03-09T13:17:15
categories: [24854]
original_url: https://insightginie.com/video-analyzer-skill-transcribe-and-analyze-videos-with-local-processing
---

The Video Analyzer skill is a powerful tool designed to help users download, transcribe, and analyze videos from various platforms including YouTube, X/Twitter, and TikTok. This skill leverages a smart two-tier system that combines the speed of `yt-dlp` for fast subtitle extraction with the robustness of local `whisper-cpp` processing as a fallback mechanism.

How to Use the Video Analyzer Skill
-----------------------------------

When a user asks you to summarize, transcribe, or download a video/audio from a URL, you should use the bundled Python script with the following command structure:

```
uv run {baseDir}/scripts/analyze_video.py --action <ACTION> --url "<URL>" [--quality <normal|max>] [--lang <en|it|etc>]
```

### Supported Actions

The skill supports several actions depending on what the user needs:

* **transcript**: Extracts the text with timestamps. Use this when the user asks for a summary or transcript.
* **download-video**: Downloads the video as MP4 to the Desktop.
* **download-audio**: Downloads the audio as M4A/MP3 to the Desktop.

Analyzing a Video
-----------------

If the user asks for a summary, analysis, or key moments, you should follow these steps:

1. Run the script with `--action transcript`
2. The script will output the path to a `.txt` file containing the timestamped transcript
3. Read that file and extract the relevant information
4. Format your response exactly in the following Markdown structure:

```
## 📝 TL;DR
[A punchy 3-sentence summary of the video's core message]

## ⏱️ Key Moments
- [MM:SS] [Brief description of what is discussed]
- [MM:SS] [Brief description of what is discussed]
- [MM:SS] [Brief description of what is discussed]

* (Extract 3 to 7 key moments depending on video length)
*

## 💡 Actionable Insights
1. [Practical takeaway 1]
2. [Practical takeaway 2]
3. [Practical takeaway 3]
```

Local Whisper Quality Settings
------------------------------

The skill uses `normal` quality by default for Whisper processing, which provides a good balance between speed and accuracy:

* **normal**: Fast (~1 minute for a 30-minute video) – Default setting
* **max**: Best quality (~5 minutes for a 30-minute video) – Use `--quality max` when accuracy is critical

Multilingual Support
--------------------

All Whisper models are multilingual by default, allowing the skill to transcribe videos in any language including Italian, Spanish, Japanese, and many others. However, it's important to note that you should always respond to the user in THEIR language, not the video's language. For example, if the user speaks Italian but sends an English video, you should provide the summary in Italian.

Finding Specific Moments
------------------------

The transcript includes precise timestamps in the format `[05:53] text...`. If a user asks “When do they talk about X?”, you can grep the transcript file and return the exact timestamp from the file.

Installation Requirements
-------------------------

To use this skill, you need to install the following tools:

* **uv**: Install with `brew install uv`
* **yt-dlp**: Install with `brew install yt-dlp`
* **ffmpeg**: Install with `brew install ffmpeg`
* **whisper-cpp**: Install with `brew install ggerganov/ggerganov/whisper-cpp`

Technical Implementation
------------------------

The skill uses a two-tier system for video processing:

1. First, it attempts to use `yt-dlp` to extract existing subtitles from the video platform
2. If subtitles are not available or extraction fails, it falls back to using `whisper-cpp` for local transcription

This approach ensures both speed and reliability, as many videos already have accurate subtitles available, while still providing robust transcription capabilities when needed.

Practical Use Cases
-------------------

This skill is perfect for various scenarios:

* Summarizing long YouTube videos or podcasts
* Extracting key points from conference talks or presentations
* Analyzing what someone said in a video
* Getting timestamps from long videos for quick navigation
* Processing videos from platforms that don't provide easy access to transcripts

Privacy and Security
--------------------

By using local processing with Whisper, this skill ensures that your video content remains private and secure. No audio or video data is sent to external servers for processing, making it suitable for sensitive or confidential content.

Conclusion
----------

The Video Analyzer skill provides a comprehensive solution for video transcription and analysis, combining the best of both worlds: fast subtitle extraction when available and reliable local transcription as a fallback. With its multilingual support, customizable quality settings, and structured output format, it's an invaluable tool for anyone who needs to process video content efficiently.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/minilozio/video-analyzer-skill/SKILL.md>
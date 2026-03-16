---
layout: post
title: YouTube Long Video Transcript &#038; Translation Skill Explained
date: '2026-03-12T19:15:48'
categories:
- ai
- openclaw
original_url: https://insightginie.com/youtube-long-video-transcript-translation-skill-explained/
featured_image: /media/images/8153.jpg
---

<h2>What This Skill Does</h2>
<p>This skill provides a complete workflow for transcribing and translating YouTube videos longer than one hour. It uses the DownSub API to extract subtitles from YouTube videos and handles the entire process from extraction to final translation.</p>
<h3>Core Functionality</h3>
<p>The skill performs four main tasks:</p>
<ol>
<li>Extracts subtitles from YouTube videos using the DownSub API</li>
<li>Translates English transcripts to Chinese verbatim</li>
<li>Handles long videos that exceed session limits through chunked processing</li>
<li>Processes DownSub API responses and generates formatted documents</li>
</ol>
<h3>Technical Requirements</h3>
<p>The skill requires several key components to function:</p>
<ul>
<li>DownSub API key (Bearer token starting with AIza&#8230;)</li>
<li>zhiyan tool (optional, for online document generation)</li>
<li>Sub-agent spawn capability for processing long videos</li>
</ul>
<h3>API Configuration</h3>
<p>The skill connects to the DownSub API at https://api.downsub.com/download using POST method with these headers:</p>
<ul>
<li>Authorization: Bearer AIzaM9ifctIOxusNAldvGeajHqq4rH6e7MJNfN</li>
<li>Content-Type: application/json</li>
</ul>
<p>The body contains the YouTube video URL in this format:</p>
<pre><code>{ "url": "https://www.youtube.com/watch?v=VIDEO_ID" }
</code></pre>
<h3>Critical Language Check</h3>
<p>The skill performs a crucial language validation step:</p>
<ul>
<li>Always checks the lang field in the API response</li>
<li>Only processes en or en-auto language codes</li>
<li>Stops processing if it detects other languages like lt (Lithuanian)</li>
</ul>
<h3>Three-Stage Workflow</h3>
<h4>Stage 1: Preparation (Main Session)</h4>
<p>The main session verifies API access, checks output capabilities, and determines if sub-agent processing is needed based on video length.</p>
<h4>Stage 2: Execution (Sub-Agent)</h4>
<p>For long videos, a sub-agent processes the transcript in 500-line chunks, translates to Chinese, and creates separate files. It also generates an executive summary and key metrics table.</p>
<h4>Stage 3: Delivery (Main Session)</h4>
<p>The main session receives the final file path, uploads it using zhiyan if available, and sends the document link or file to the user.</p>
<h3>Common Issues and Solutions</h3>
<p>The skill includes troubleshooting for common problems:</p>
<ul>
<li>Missing API key (401 Unauthorized errors)</li>
<li>zhiyan tool not found</li>
<li>Wrong subtitle track (nonsense translations)</li>
<li>Timeouts for very long videos</li>
</ul>
<h3>Output Format</h3>
<p>The final output includes:</p>
<ul>
<li>Executive summary (3-5 bullets in Chinese)</li>
<li>Key metrics table</li>
<li>Full translated transcript</li>
</ul>
<p>This skill is specifically designed for users who need to process long YouTube videos that exceed typical session limits, providing a robust solution for video transcription and translation workflows.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/qingliu1617-art/ytb-transcript-long/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/qingliu1617-art/ytb-transcript-long/SKILL.md</a></p>

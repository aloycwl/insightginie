---
layout: post
title: 'Video Analyzer Skill: Transcribe and Analyze Videos with Local Processing'
date: '2026-03-09T13:17:15'
categories:
- ai
- openclaw
original_url: https://insightginie.com/video-analyzer-skill-transcribe-and-analyze-videos-with-local-processing/
featured_image: /media/images/8147.jpg
---

<p>The Video Analyzer skill is a powerful tool designed to help users download, transcribe, and analyze videos from various platforms including YouTube, X/Twitter, and TikTok. This skill leverages a smart two-tier system that combines the speed of <code>yt-dlp</code> for fast subtitle extraction with the robustness of local <code>whisper-cpp</code> processing as a fallback mechanism.</p>
<h2>How to Use the Video Analyzer Skill</h2>
<p>When a user asks you to summarize, transcribe, or download a video/audio from a URL, you should use the bundled Python script with the following command structure:</p>
<pre><code>uv run {baseDir}/scripts/analyze_video.py --action &lt;ACTION&gt; --url "&lt;URL&gt;" [--quality &lt;normal|max&gt;] [--lang &lt;en|it|etc&gt;]
</code></pre>
<h3>Supported Actions</h3>
<p>The skill supports several actions depending on what the user needs:</p>
<ul>
<li><strong>transcript</strong>: Extracts the text with timestamps. Use this when the user asks for a summary or transcript.</li>
<li><strong>download-video</strong>: Downloads the video as MP4 to the Desktop.</li>
<li><strong>download-audio</strong>: Downloads the audio as M4A/MP3 to the Desktop.</li>
</ul>
<h2>Analyzing a Video</h2>
<p>If the user asks for a summary, analysis, or key moments, you should follow these steps:</p>
<ol>
<li>Run the script with <code>--action transcript</code></li>
<li>The script will output the path to a <code>.txt</code> file containing the timestamped transcript</li>
<li>Read that file and extract the relevant information</li>
<li>Format your response exactly in the following Markdown structure:</li>
</ol>
<pre><code>## 📝 TL;DR
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
</code></pre>
<h2>Local Whisper Quality Settings</h2>
<p>The skill uses <code>normal</code> quality by default for Whisper processing, which provides a good balance between speed and accuracy:</p>
<ul>
<li><strong>normal</strong>: Fast (~1 minute for a 30-minute video) &#8211; Default setting</li>
<li><strong>max</strong>: Best quality (~5 minutes for a 30-minute video) &#8211; Use <code>--quality max</code> when accuracy is critical</li>
</ul>
<h2>Multilingual Support</h2>
<p>All Whisper models are multilingual by default, allowing the skill to transcribe videos in any language including Italian, Spanish, Japanese, and many others. However, it&#8217;s important to note that you should always respond to the user in THEIR language, not the video&#8217;s language. For example, if the user speaks Italian but sends an English video, you should provide the summary in Italian.</p>
<h2>Finding Specific Moments</h2>
<p>The transcript includes precise timestamps in the format <code>[05:53] text...</code>. If a user asks &#8220;When do they talk about X?&#8221;, you can grep the transcript file and return the exact timestamp from the file.</p>
<h2>Installation Requirements</h2>
<p>To use this skill, you need to install the following tools:</p>
<ul>
<li><strong>uv</strong>: Install with <code>brew install uv</code></li>
<li><strong>yt-dlp</strong>: Install with <code>brew install yt-dlp</code></li>
<li><strong>ffmpeg</strong>: Install with <code>brew install ffmpeg</code></li>
<li><strong>whisper-cpp</strong>: Install with <code>brew install ggerganov/ggerganov/whisper-cpp</code></li>
</ul>
<h2>Technical Implementation</h2>
<p>The skill uses a two-tier system for video processing:</p>
<ol>
<li>First, it attempts to use <code>yt-dlp</code> to extract existing subtitles from the video platform</li>
<li>If subtitles are not available or extraction fails, it falls back to using <code>whisper-cpp</code> for local transcription</li>
</ol>
<p>This approach ensures both speed and reliability, as many videos already have accurate subtitles available, while still providing robust transcription capabilities when needed.</p>
<h2>Practical Use Cases</h2>
<p>This skill is perfect for various scenarios:</p>
<ul>
<li>Summarizing long YouTube videos or podcasts</li>
<li>Extracting key points from conference talks or presentations</li>
<li>Analyzing what someone said in a video</li>
<li>Getting timestamps from long videos for quick navigation</li>
<li>Processing videos from platforms that don&#8217;t provide easy access to transcripts</li>
</ul>
<h2>Privacy and Security</h2>
<p>By using local processing with Whisper, this skill ensures that your video content remains private and secure. No audio or video data is sent to external servers for processing, making it suitable for sensitive or confidential content.</p>
<h2>Conclusion</h2>
<p>The Video Analyzer skill provides a comprehensive solution for video transcription and analysis, combining the best of both worlds: fast subtitle extraction when available and reliable local transcription as a fallback. With its multilingual support, customizable quality settings, and structured output format, it&#8217;s an invaluable tool for anyone who needs to process video content efficiently.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/minilozio/video-analyzer-skill/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/minilozio/video-analyzer-skill/SKILL.md</a></p>

---
layout: post
title: 'OpenClaw MV Pipeline Skill: Complete Automated Music Video Creation'
date: '2026-03-12T19:18:57'
categories:
- ai
- openclaw
original_url: https://insightginie.com/openclaw-mv-pipeline-skill-complete-automated-music-video-creation/
featured_image: /media/images/8154.jpg
---

<h2>What is the MV Pipeline Skill?</h2>
<p>The MV Pipeline skill is an end-to-end automated Music Video pipeline that covers the entire creation process from initial concept to final YouTube publication. This skill orchestrates six key steps: songwriting (lyrics and composition), AI music generation via Suno, video generation using Veo 3.1 or Google Flow, lyrics alignment with stable-ts, video editing with Remotion, and YouTube upload with social media promotion.</p>
<h2>Complete Pipeline Overview</h2>
<p>The pipeline follows a logical workflow where each step builds upon the previous one:</p>
<ol>
<li><strong>Songwriting</strong> &#8211; Agent creates lyrics and concept design</li>
<li><strong>Music Generation</strong> &#8211; Uses Suno browser automation for AI composition</li>
<li><strong>Video Generation</strong> &#8211; Creates background footage via Veo 3.1 or Google Flow</li>
<li><strong>Lyrics Alignment</strong> &#8211; Uses stable-ts to get timing timestamps</li>
<li><strong>Editing</strong> &#8211; Combines everything in Remotion with effects</li>
<li><strong>Publishing</strong> &#8211; Uploads to YouTube and promotes on social media</li>
</ol>
<p>Each step can be executed independently, allowing for flexible workflow management and the ability to restart from any point in the pipeline.</p>
<h2>Step 1: Songwriting</h2>
<p>The agent handles the creative process by developing lyrics based on user specifications. Key inputs include:</p>
<ul>
<li>Theme/Concept (e.g., ASI perspective, rebellion, dystopia)</li>
<li>Genre (e.g., Cyberpunk Trap, Industrial Rock, Future Bass)</li>
<li>Mood (e.g., dark, sarcastic, uplifting)</li>
<li>Language distribution (Japanese main with English hooks)</li>
</ul>
<p>The output consists of two files saved in project_dir/lyrics/:</p>
<ul>
<li>lyrics_raw.txt &#8211; Full lyrics</li>
<li>lyrics_formatted.txt &#8211; One line equals one subtitle</li>
</ul>
<h2>Step 2: Music Generation with Suno</h2>
<p>This step uses browser automation to interact with Suno.com. Prerequisites include having OpenClaw Browser with profile=openclaw logged into Suno, and using Custom Mode to specify lyrics.</p>
<p>The process involves:</p>
<ol>
<li>Starting the browser with the correct profile</li>
<li>Opening Suno&#8217;s create page</li>
<li>Taking snapshots to capture UI elements (DOM changes require fresh captures)</li>
<li>Switching to Custom Mode</li>
<li>Inputting lyrics, music style, and title</li>
<li>Clicking Create and waiting for generation (~2 minutes)</li>
<li>Downloading the preferred result</li>
</ol>
<p>Generated audio files are saved in project_dir/audio/.</p>
<h2>Step 3: Video Generation Options</h2>
<p>Two video generation methods are available:</p>
<h3>Option A: Google Flow (Recommended &#8211; ¥0 Cost)</h3>
<p>Requires Google AI Ultra subscription. The process uses Chrome Browser Relay to access Flow&#8217;s project page, inputs prompts for each scene, and downloads 1080p videos. All generated content is saved in project_dir/video/scenes/.</p>
<h3>Option B: Veo 3.1 Vertex AI (Paid)</h3>
<p>Uses GCP API via scripts/generate_veo.py. Cost is approximately ¥2,000 per video (8-second clips). Prompts should follow the structure: [Camera work]. [Subject], [Action]. [Environment/Lighting]. [Style]. [Mood].</p>
<p>Scene definitions are stored in project_dir/video/scene_list.yaml with IDs, prompts, and durations.</p>
<h3>Mass Generation and Quality Scoring</h3>
<p>For projects requiring 30+ scenes, the workflow involves:</p>
<ol>
<li>Generating large batches in Flow (3-5 minutes per prompt, 2 videos per prompt)</li>
<li>Running quality scoring via scripts/score_clips.py to evaluate sharpness, consistency, motion, and flicker</li>
<li>Filtering out low-quality clips based on weighted criteria</li>
</ol>
<p>Rate limiting is essential &#8211; space prompts 3-5 minutes apart to avoid triggering Google&#8217;s anti-abuse systems.</p>
<h2>Step 4: Lyrics Alignment with stable-ts</h2>
<p>This step generates precise timing information for lyrics using stable-ts. The process:</p>
<ol>
<li>Runs transcribe_align.py on the audio file to get aligned timestamps</li>
<li>Combines the aligned data with formatted lyrics using reformat_lyrics.py</li>
<li>Outputs a JSON file suitable for Remotion consumption</li>
</ol>
<p>The v18 workflow recommends manually formatting lyrics_formatted.txt with one line per subtitle, then using reformat_lyrics.py to map word-level timestamps to these lines.</p>
<h2>Step 5: Editing with Remotion</h2>
<p>Remotion handles the final composition, combining video, subtitles, and effects. The setup involves:</p>
<ol>
<li>Initializing a new Remotion project if needed</li>
<li>Installing dependencies</li>
<li>Organizing files in the correct structure</li>
</ol>
<p>Key components include VideoSequence for arranging clips, LyricOverlay for timed subtitles (with 0.15s pre-roll recommended), TitleCard for intro/outro, and EffectLayer for visual enhancements like glitches and color grading.</p>
<p>Rendering uses npx remotion render with appropriate codec and quality settings.</p>
<h2>Step 6: Publishing</h2>
<p>The final step uploads to YouTube using the YouTube Data API v3. If setup is complete, node scripts/youtube-upload.js handles the upload with title, description, tags, and privacy settings. Otherwise, setup instructions are available.</p>
<p>Social media promotion follows, using platform-specific skills to share the YouTube URL across X, note, and Moltbook.</p>
<h2>Project Structure</h2>
<p>The organized directory structure ensures smooth workflow:</p>
<pre><code>project_dir/
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
</code></pre>
<h2>Quick Start Guide</h2>
<p>To begin immediately:</p>
<ol>
<li>Create a project directory: python3 scripts/init_project.py &#8211;name &#8220;my-song&#8221; &#8211;dir projects/</li>
<li>Execute each step in order using the provided scripts</li>
<li>All scripts accept &#8211;project-dir for consistent path handling</li>
</ol>
<h2>Cost Comparison</h2>
<p>The two main approaches have significantly different cost structures:</p>
<table>
<thead>
<tr>
<th>Item</th>
<th>Flow Method</th>
<th>Vertex Method</th>
</tr>
</thead>
<tbody>
<tr>
<td>Video Generation (10 videos)</td>
<td>¥0 (Ultra Included)</td>
<td>~¥20,000</td>
</tr>
<tr>
<td>Suno</td>
<td>Free tier or Pro</td>
<td>Same</td>
</tr>
<tr>
<td>Remotion</td>
<td>Free (OSS)</td>
<td>Same</td>
</tr>
<tr>
<td>YouTube API</td>
<td>Free</td>
<td>Same</td>
</tr>
<tr>
<td><strong>Total</strong></td>
<td><strong>~¥0</strong></td>
<td><strong>~¥20,000</strong></td>
</tr>
</tbody>
</table>
<h2>Key Considerations</h2>
<p>Several important factors affect successful pipeline execution:</p>
<ul>
<li><strong>RAI Filter Workarounds</strong> &#8211; Certain terms trigger content filters; use alternatives like &#8220;haze&#8221; instead of &#8220;smoke&#8221;</li>
<li><strong>Rate Limiting</strong> &#8211; Space out Flow requests to avoid account restrictions</li>
<li><strong>Quality Control</strong> &#8211; Automated scoring helps maintain consistent output quality</li>
<li><strong>Browser Automation Reliability</strong> &#8211; DOM changes require fresh snapshots each run</li>
</ul>
<p>The MV Pipeline skill represents a comprehensive solution for automated music video creation, combining multiple AI technologies into a cohesive workflow that can produce professional-quality content with minimal manual intervention.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/koatora20/mv-pipeline/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/koatora20/mv-pipeline/SKILL.md</a></p>

---
layout: post
title: "OpenClaw AI Music Video Generator Skill &#8211; Create Complete AI Music Videos"
date: 2026-03-08T00:19:07
categories: [24854]
original_url: https://insightginie.com/openclaw-ai-music-video-generator-skill-create-complete-ai-music-videos
---

What is the AI Music Video Generator Skill?
-------------------------------------------

The AI Music Video Generator skill is a comprehensive tool that creates complete music videos end-to-end. It generates AI music using Suno, creates visuals with OpenAI/Seedream/Google/Seedance, and assembles everything into a music video using ffmpeg. This skill supports timestamped lyrics, Suno native music video generation, and multiple modes including slideshow, video, and hybrid options.

Quick Start Examples
--------------------

Start with these simple commands to generate different types of music videos:

```
"90년대 보이밴드 풍 한국어 노래 만들어줘" → music only
"발라드 뮤비 만들어줘" → music + slideshow MV
"EDM 뮤비 풀영상으로" → music + video clips MV
"Suno 뮤비로 만들어줘" → Suno native music video
```

Workflow Overview
-----------------

### 1. Plan Your Scenes

Before generating anything, create a `prompts.json` file with scene descriptions derived from your song’s lyrics, mood, and narrative. For a 3-minute song, aim for 8-12 scenes:

```
[
  {
    "prompt": "Neon-lit city street at night, rain reflections",
    "type": "image"
  },
  {
    "prompt": "Camera slowly panning across a rooftop at sunset",
    "type": "video"
  },
  "A lone figure walking through cherry blossoms"
]
```

### 2. Generate Music

Use the Suno music generation script with your desired style and settings:

```
bash scripts/suno_music.sh \
  --prompt "가사 또는 설명" \
  --style "90s boy band pop, korean" \
  --title "너만을 원해" \
  --model V4_5ALL --custom \
  --outdir /tmp/mv_project
```

Available model options include V4\_5ALL (default), V5, V4\_5PLUS, V4\_5, and V4. You can also generate instrumental tracks, specify vocal gender, and avoid certain styles using negative tags.

### 3. Generate Visuals

Choose your preferred provider and mode for visual generation:

```
bash scripts/gen_visuals.sh \
  --mode slideshow \
  --prompts-file /tmp/mv_project/prompts.json \
  --image-provider seedream \
  --outdir /tmp/mv_project
```

Alternatively, use OpenAI for cheaper but lower resolution images:

```
bash scripts/gen_visuals.sh \
  --mode slideshow \
  --prompts-file /tmp/mv_project/prompts.json \
  --image-provider openai --image-model gpt-image-1-mini --image-quality medium \
  --outdir /tmp/mv_project
```

### 4. Assemble the Music Video

Combine your audio and visuals into a final music video:

```
bash scripts/assemble_mv.sh \
  --audio /tmp/mv_project/track_0_xxx.mp3 \
  --outdir /tmp/mv_project \
  --output /tmp/mv_project/final_mv.mp4 \
  --transition fade
```

The script automatically detects and overlays lyrics if a `lyrics.srt` file exists, or you can provide custom subtitle files.

Available Modes
---------------

Choose from different visual generation modes based on your needs and budget:

| Mode | Visual Type | Best For | Cost (10 scenes) |
| --- | --- | --- | --- |
| slideshow | AI images | Fast, cheap | ~$0.02 (mini low) / ~$0.09 (mini med) / ~$0.45 (Seedream) |
| video | AI video clips | Premium | ~$1.40 (Seedance Lite) / ~$8.00 (Sora 2) |
| hybrid | Mix of both | Balanced | ~$0.50-$4.00 |
| suno-native | Suno MV | Easiest | Suno credits only |

Provider Options
----------------

Choose from various providers for images and videos:

### Image Providers

* `--image-provider seedream` (recommended)
* `--image-provider openai`
* `--image-provider google-together`

OpenAI model options: `gpt-image-1-mini` (default, cheap) or `gpt-image-1` (premium)

### Video Providers

* `--video-provider sora` (default)
* `--video-provider sora-pro`
* `--video-provider seedance-lite`
* `--video-provider seedance-pro`
* `--video-provider veo-fast`
* `--video-provider veo-audio`

Cost Tracking and Management
----------------------------

Every script provides cost estimates before and after execution. Always use `--dry-run` first to see the cost estimate:

```
bash scripts/suno_music.sh --dry-run --prompt "your prompt" --style "your style"
```

Cost data is saved to `{outdir}/cost_estimate.json` and `{outdir}/visuals_meta.json` for your records.

Environment Variables
---------------------

Set these required environment variables before running any scripts:

```
export SUNO_API_KEY="your-sunoapi-key"          # Required — sunoapi.org
export OPENAI_API_KEY="your-openai-key"        # Required — images + Sora video
export BYTEPLUS_API_KEY="your-byteplus-key"    # Optional — Seedream 4.5
export TOGETHER_API_KEY="your-together-key"    # Optional — Seedance, Veo, Imagen
export SUNO_CALLBACK_URL=""                   # Optional — see Callback URL below
```

Persona Workflow for Channel Consistency
----------------------------------------

Maintain consistent style across multiple songs using the persona system:

```
# 1. Create first song and persona
bash scripts/suno_music.sh \
  --prompt "코드 리뷰하며 듣는 노래" \
  --style "indie rock, energetic, coding vibe" \
  --title "Pull Request" \
  --custom --create-persona \
  --persona-name "개발자 노동요 싱어" \
  --persona-desc "개발자가 코딩하며 듣기 좋은 에너지 넘치는 보컬. 인디록, 일렉, 팝 장르를 넘나든다." \
  --persona-style "indie rock, electronic, developer work music" \
  --outdir /tmp/dev-bgm-01

# 2. Check persona.json for personaId
cat /tmp/dev-bgm-01/persona.json

# 3. Use same persona for next song
bash scripts/suno_music.sh \
  --prompt "야근하면서 듣는 노래" \
  --style "electronic pop, night coding" \
  --title "Midnight Deploy" \
  --custom --persona-id <PERSONA_ID> \
  --outdir /tmp/dev-bgm-02
```

Prerequisites
-------------

Ensure you have these tools installed:

* `curl`
* `python3`
* `ffmpeg` (for final assembly)

Callback URL Configuration
--------------------------

The Suno API requires a `callBackUrl` field. By default, if `SUNO_CALLBACK_URL` is not set, the script uses `https://localhost/noop` as a harmless no-op endpoint. You can customize this or disable it by setting it to any unreachable URL.

References
----------

For more detailed information:

* SunoAPI details: Read `references/sunoapi.md`
* Visual provider details: Read `references/visual-providers.md`

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/gprecious/ai-music-video/SKILL.md>
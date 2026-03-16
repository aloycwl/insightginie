---
layout: post
title: "Video Production Skill: Complete A/B Video Pipeline with Veo 3"
date: 2026-03-11T13:16:44
categories: [24854]
original_url: https://insightginie.com/video-production-skill-complete-a-b-video-pipeline-with-veo-3
---

Video Production Skill: Complete A/B Video Pipeline with Veo 3
--------------------------------------------------------------

Generate cinematic video clips with Veo 3, review them in a browser preview, iterate with feedback, and assemble final A/B test videos — all with minimal token spend.

### Quick Start

1. `cd ~/.openclaw/workspace/skills/video-production`
2. Generate all clips from storyboard: `.venv/bin/python3 scripts/batch_generate.py --storyboard /path/to/storyboard.json`
3. Open browser preview: `.venv/bin/python3 scripts/generate_preview.py --storyboard /path/to/storyboard.json`
4. (After feedback) Re-generate only revised scenes: `.venv/bin/python3 scripts/apply_feedback.py --storyboard storyboard.json --feedback feedback.json`
5. Assemble final video: `.venv/bin/python3 scripts/ffmpeg_assembler.py --storyboard storyboard.json`

### A/B Video Architecture

Target: 15-second videos, 3 clips × 5s each

[HOOK: 5s] → [CORE: 5s] → [CTA/PAYOFF: 5s]

↑ ↑

swap for A/B swap for A/B

Economics:

* 5 Veo prompts → 4 unique A/B videos (2 hooks × 1 core × 2 CTAs)
* 7 prompts → 9 videos | 9 prompts → 16+ videos
* Transitions at 5s and 10s marks — clean for analytics

### Pipeline Overview

storyboard.json → batch\_generate.py → clips/scene\_01.mp4 … scene\_05.mp4 → generate\_preview.py → preview.html (opens in browser, zero tokens) → [review + paste feedback JSON to Muffin] → [Muffin suggests revised prompts, updates storyboard.json] → apply\_feedback.py → re-generates only ‘revise’ scenes → ffmpeg\_assembler.py → final\_AA.mp4, final\_BA.mp4, final\_AB.mp4, final\_BB.mp4

Token cost: Only when writing storyboard + interpreting feedback. Preview, generation, and assembly are all zero tokens.

### Storyboard Format

```
{
  "project": "my-video",
  "output_dir": "clips",
  "final_output": "final.mp4",
  "scenes": [
    {
      "id": "scene_01",
      "role": "hook_a",
      "label": "Hook A",
      "order": 1,
      "duration": 5,
      "aspect_ratio": "16:9",
      "prompt": "..."
    }
  ],
  "_ab_combinations": {
    "video_1_AA": ["scene_01", "scene_03", "scene_04"],
    "video_2_BA": ["scene_02", "scene_03", "scene_04"],
    "video_3_AB": ["scene_01", "scene_03", "scene_05"],
    "video_4_BB": ["scene_02", "scene_03", "scene_05"]
  }
}
```

See `scripts/storyboard_template.json` for full template.

### Feedback Format

Paste this JSON to Muffin after reviewing preview.html:

```
{
  "scenes": [
    {
      "id": "scene_01",
      "action": "approve",
      "notes": ""
    },
    {
      "id": "scene_02",
      "action": "revise",
      "notes": "slower camera, warmer light"
    }
  ]
}
```

### Veo 3 API — Current Limits (Gemini API, verified 2026-02-23)

| Parameter | Supported |
| --- | --- |
| aspect\_ratio | ✅ |
| number\_of\_videos | ✅ |
| negative\_prompt | ✅ |
| duration\_seconds | ❌ Broken (throws 400 even with valid values) |
| fps | ❌ Vertex AI only |
| compression\_quality | ❌ Vertex AI only |
| enhance\_prompt | ❌ Vertex AI only |

Models: veo-3.1-generate-preview (best) | veo-3.1-fast-generate-preview | veo-3.0-generate-001

SDK: google-genai (NOT google-generativeai)

### Prompting Techniques

* **Motion in every sentence** — Veo produces laggy output from static prompts. Every sentence should describe camera OR subject movement.
* **Character continuity** — Veo can’t maintain exact characters across clips. Describe physical details explicitly in every scene that includes the same character.
  + ✅ “The same client character from the opening — dark jacket, professional bearing, 30s-40s”
* **Stitch continuity** — For seamless cuts, open each prompt with the color/light state the previous clip ends on.
  + ✅ “Warm amber light, a direct visual continuation from the post-production suite…”
* **Single continuous shot** — Each prompt is one continuous clip. Design it as one camera move that reveals multiple elements — not a montage description.
* **Content policy** — Environmental/prop-only scenes generate reliably. Stressed people on phones can silently return no video. Keep humans calm or describe the environment instead.

### Quota Management

When you hit the daily limit (429 RESOURCE\_EXHAUSTED), use the quota watcher:

```
# Sets a cron that retries every 30 min, texts Master when done
chmod +x scripts/quota_watcher.sh
# Add to crontab:
(crontab -l 2>/dev/null | grep -v quota_watcher ; \
echo "*/30 * * * * /path/to/quota_watcher.sh >> /tmp/quota_watcher.log 2>&1") | crontab -
```

See `api-quota-watcher` skill for the generic pattern.

### Scripts

| Script | Purpose |
| --- | --- |
| scripts/batch\_generate.py | Generate all scenes from storyboard, skip existing |
| scripts/generate\_preview.py | Build preview.html with video players + feedback form |
| scripts/apply\_feedback.py | Re-generate only scenes marked ‘revise’ |
| scripts/ffmpeg\_assembler.py | Stitch approved clips → final MP4 (cut or crossfade) |
| scripts/quota\_watcher.sh | Retry + notify cron for quota recovery |
| scripts/storyboard\_template.json | Starting storyboard template |

### Environment Setup

```
cd ~/.openclaw/workspace/skills/video-production
uv venv .venv
uv pip install google-genai Pillow requests
# API key must be in ~/.zshenv:
export GOOGLE_API_KEY="AIza..."
```

### Assembling A/B Combinations

After all scenes approved, run assembler for each combo:

```
# Assemble all 4 A/B videos
for combo in AA BA AB BB; do
  # Edit storyboard or pass scene list directly
  .venv/bin/python3 scripts/ffmpeg_assembler.py \
    --storyboard storyboard.json \
    --output "final_${combo}.mp4"
done
```

Or hardcode in `_ab_combinations` in storyboard.json — assembler reads it automatically.

### Format Adaptation

| Format | Notes |
| --- | --- |
| 16:9 (master) | Default — all scripts use this |
| 9:16 (vertical) | Change `aspect_ratio` to `"9:16"` in storyboard |
| 1:1 (square) | Change `aspect_ratio` to `"1:1"` |

Generate separate storyboards per format for best results. Don’t crop 16:9 to 9:16 in post — re-generate with proper aspect.

### What Veo 3 Does Well

* Atmospheric/mood shots
* Smooth camera movements (push-in, crane, tracking)
* Lighting transitions within a single clip
* Office/studio/urban environments
* Abstract beauty (nature, space, product)

### What Veo 3 Struggles With

* Exact text on screen (add in post via After Effects/Resolve)
* Maintaining character consistency across clips
* Very fast montage within a single generation
* Complex multi-person scenes
* Specific prop/brand details

### Character Registry & Learning System

#### Clean Slate Default

Every new campaign starts fresh. No inherited characters, no assumed cast, no prompt weights from previous runs. If you want continuity from a past campaign, explicitly say so: “Use HERO\_01 from the MMM campaign”

#### Character IDs (Bootstrap Defaults)

If no cast is defined, use these placeholders:

* HERO\_01 — Primary UGC creator
* FRIEND\_01 — Recurring side character
* HAND\_MODEL\_01 — Hands-only product handler

First approved output becomes the canonical identity baseline for that campaign.

#### Character Bible (Per Campaign)

When characters are defined, maintain a `character_registry.json` in the project folder:

```
{
  "HERO_01": {
    "identity": {
      "age_range": "28-35",
      "gender": "male",
      "skin_tone": "...",
      "hair": "...",
      "build": "...",
      "style": "...",
      "personality": "..."
    },
    "consistency_notes": [
      "Dark jacket in office scenes",
      "Professional bearing",
      "30s-40s"
    ]
  }
}
```

#### Character Prompt Weights (Optional)

If you want to lock a character’s description in future prompts, add weights:

```
{
  "HERO_01": {
    "weights": {
      "identity": 0.8,
      "consistency_notes": 0.7
    }
  }
}
```

### Learning from Feedback

Each time you revise a scene, the system remembers:

1. Which words were changed
2. Whether the change was “tone”, “motion”, “lighting”, “composition”, etc.
3. The final prompt that passed approval

This creates a per-campaign “prompt DNA” that gets reused automatically in future scenes — no need to manually copy-paste successful phrasing.

### Output

Final deliverables:

* `final_AA.mp4` — Hook A + Core + CTA A
* `final_BA.mp4` — Hook B + Core + CTA A
* `final_AB.mp4` — Hook A + Core + CTA B
* `final_BB.mp4` — Hook B + Core + CTA B

Each video is 15 seconds, ready for A/B testing on platforms like Meta, TikTok, or YouTube Shorts.

### Best Practices

1. Keep hooks distinct — test completely different opening hooks (problem vs. curiosity vs. testimonial).
2. Keep core consistent — the middle scene should be the same across A/B tests to isolate hook/CTA effects.
3. Make CTAs different but comparable — test “Buy Now” vs. “Learn More” rather than “Buy Now” vs. “Watch Cat Videos”.
4. Use clean transitions — the 5s and 10s marks should be clean cuts for analytics tracking.
5. Preview before generating — use the browser preview to catch issues before spending Veo credits.

### Troubleshooting

* **No video returned**: Try removing people from the prompt or simplifying the scene.
* **Laggy/jerky motion**: Add more camera movement descriptions or break complex scenes into simpler ones.
* **Wrong aspect ratio**: Ensure `aspect_ratio` is set correctly in the storyboard and regenerate.
* **Quota errors**: Use the quota watcher script and wait for the daily reset.

This skill provides a complete, token-efficient workflow for creating professional A/B test videos using Veo 3, from initial storyboarding through final assembly and delivery.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/omerflo/video-production/SKILL.md>
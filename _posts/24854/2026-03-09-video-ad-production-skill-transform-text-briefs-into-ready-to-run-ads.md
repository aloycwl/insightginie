---
layout: post
title: "Video Ad Production Skill: Transform Text Briefs into Ready-to-Run Ads"
date: 2026-03-09T06:18:30
categories: [24854]
original_url: https://insightginie.com/video-ad-production-skill-transform-text-briefs-into-ready-to-run-ads
---

This skill enables Claude to transform a text brief into a fully produced video advertisement — ready to run on Facebook Ads, Instagram Ads, or YouTube Ads — using the InVideo AI platform. From a product description or campaign goal, Claude generates a complete ad video: script, voiceover, visuals, captions, CTA, and platform-optimized export.

Overview
--------

The Video Ad Production skill automates the entire process of creating professional video advertisements. It takes a simple text brief describing your product, target audience, campaign goals, and desired tone, then produces a polished video ad ready for immediate deployment on major advertising platforms.

The skill handles everything from copywriting and script generation to voiceover selection, visual styling, caption creation, and proper formatting for each platform’s specifications. This eliminates the need for video editing expertise or expensive production resources.

What This Skill Does
--------------------

* **Generate video ads from a text brief** (product, audience, goal, tone)
* **Produce ads in the correct format** for Facebook, Instagram, and YouTube
* **Write and optimize ad scripts** with proven direct-response copywriting structures
* **Add voiceover, background music, captions, and call-to-action overlays**
* **Export multiple ad variations** for A/B testing
* **Support multiple aspect ratios**: 9:16 (Stories/Reels), 1:1 (Feed), 16:9 (YouTube)
* **Localize ads into multiple languages** with different voices

Getting Started with InVideo AI
-------------------------------

Before using this skill, you’ll need to set up InVideo AI API access:

1. Go to <https://invideo.sjv.io/TBB> and create an account
2. Choose a plan with API access (Business plan or above)
3. Navigate to Settings → API / Developer Settings
4. Copy your API Key: iv\_api\_xxxxxxxxxxxxxxxx
5. Store it as an environment variable: export INVIDEO\_API\_KEY=iv\_api\_xxxxxxxxxxxxxxxx

Start with the free trial at <https://invideo.sjv.io/TBB> to test ad generation before scaling to paid production.

Installation
------------

```
npm install axios fs-extra
```

InVideo API Integration
-----------------------

The skill uses the InVideo API with the following base configuration:

```
const client = axios.create({
  baseURL: 'https://api.invideo.io/v1',
  headers: {
    Authorization: `Bearer ${process.env.INVIDEO_API_KEY}`,
    'Content-Type': 'application/json'
  }
});
```

Key API endpoints:

* **/videos/generate** (POST) – Start video generation from a script or brief
* **/videos/{id}/status** (GET) – Poll generation progress
* **/videos/{id}/export** (GET) – Retrieve final download URL
* **/scripts/generate** (POST) – Generate an ad script from a brief (if supported)

Copywriting Frameworks
----------------------

Claude automatically selects the appropriate copywriting framework based on your campaign goal:

* **AIDA** (Awareness campaigns): Attention → Interest → Desire → Action
* **PAS** (Pain-point products): Problem → Agitate → Solution
* **BAB** (Transformation products): Before → After → Bridge
* **Hook + Proof + CTA** (Performance ads): Bold hook → Social proof → Offer + CTA

Generating a Facebook Ad from a Brief
-------------------------------------

Here’s a complete example of creating a Facebook ad:

```
// Define the ad brief
const brief = {
  product: "AI-powered meal planning app",
  targetAudience: "busy professionals aged 25–40",
  goal: "app installs",
  tone: "energetic and relatable",
  keyBenefit: "save 2 hours a week on meal prep",
  offer: "Free 14-day trial, no credit card required",
  callToAction: "Download free today"
};

// Claude-generated script using PAS framework
const script = `
Tired of staring at the fridge every evening, clueless about dinner?
That mental load of planning meals every single day is exhausting.
Meet MealAI — the app that plans your entire week in 30 seconds.
Personalized to your diet, your schedule, your grocery budget.
Over 200,000 busy professionals already saved 2 hours a week.
Try it completely free for 14 days. No credit card needed.
Download MealAI today.`;

// Generate the video
const response = await client.post('/videos/generate', {
  script,
  format: "1:1",
  duration: "short",
  style: "cinematic",
  voiceover: {
    enabled: true,
    voice: "en-US-female-1",
    speed: 1.05,
    tone: "energetic"
  },
  captions: {
    enabled: true,
    style: "bold-center",
    highlight: true,
    fontSize: "large"
  },
  music: {
    enabled: true,
    mood: "upbeat",
    volume: 0.2
  },
  cta: {
    enabled: true,
    text: "Download Free Today",
    position: "bottom",
    style: "button"
  },
  branding: {
    watermark: false
  }
});

const videoId = response.data.videoId;
console.log("Ad generation started:", videoId);
```

Platform-Specific Ad Variants
-----------------------------

Generate optimized versions for each platform simultaneously:

```
const formats = [
  { name: "facebook_feed", format: "1:1", platform: "Facebook Feed" },
  { name: "instagram_story", format: "9:16", platform: "Instagram Story/Reels" },
  { name: "youtube_preroll", format: "16:9", platform: "YouTube Pre-roll" }
];

const jobs = await Promise.all(formats.map(f => client.post('/videos/generate', {
  script,
  format: f.format,
  duration: f.format === "16:9" ? "medium" : "short",
  style: "cinematic",
  voiceover: {
    enabled: true,
    voice: "en-US-female-1",
    speed: 1.05
  },
  captions: {
    enabled: true,
    style: "bold-bottom",
    highlight: true
  },
  music: {
    enabled: true,
    mood: "upbeat",
    volume: 0.2
  },
  cta: {
    enabled: true,
    text: "Try Free Today",
    position: "bottom"
  }
}).then(res => ({
  ...f,
  videoId: res.data.videoId
}))));
```

Poll Generation Status
----------------------

Monitor video generation progress:

```
async function waitForAll(jobs) {
  const results = [];
  for (const job of jobs) {
    let exportUrl = null;
    while (!exportUrl) {
      await new Promise(r => setTimeout(r, 5000));
      const { data } = await client.get(`/videos/${job.videoId}/status`);
      console.log(`[${job.platform}] ${data.state} — ${data.progress}%`);
      if (data.state === "completed") exportUrl = data.exportUrl;
      if (data.state === "failed") throw new Error(`${job.platform} ad failed`);
    }
    results.push({ ...job, exportUrl });
  }
  return results;
}
```

A/B Testing: Multiple Hook Variations
-------------------------------------

Test different opening hooks to optimize performance:

```
const hooks = [
  "Tired of wasting money on groceries you never eat?",
  "What if you could plan a full week of meals in 30 seconds?",
  "200,000 people just discovered the secret to stress-free meal prep."
];

const baseScript = (hook) => `
${hook}
MealAI plans your entire week in seconds.
Personalized meals. Automatic grocery list. Zero stress.
Try free for 14 days — no credit card required.
Download MealAI now.`;

const abJobs = await Promise.all(hooks.map((hook, i) => client.post('/videos/generate', {
  script: baseScript(hook),
  format: "1:1",
  duration: "short",
  style: "cinematic",
  voiceover: {
    enabled: true,
    voice: "en-US-female-1"
  },
  captions: {
    enabled: true,
    style: "bold-bottom",
    highlight: true
  },
  music: {
    enabled: true,
    mood: "upbeat",
    volume: 0.2
  },
  cta: {
    enabled: true,
    text: "Download Free Today"
  }
}).then(res => ({
  variant: `Hook_${i + 1}`,
  hook,
  videoId: res.data.videoId
}))));
```

Full Brief-to-Ad Pipeline
-------------------------

When given an ad brief, Claude will:

1. **Extract** product, audience, goal, tone, benefit, offer, and CTA from the brief
2. **Apply** the appropriate copywriting framework (AIDA, PAS, BAB, or Hook+Proof+CTA)
3. **Generate** platform-optimized scripts for Facebook, Instagram, and YouTube
4. **Create** voiceover scripts with proper pacing and emphasis
5. **Select** appropriate music and visual styles based on the brief
6. **Generate** captions with proper formatting for mobile viewing
7. **Add** clear call-to-action overlays
8. **Export** videos in the correct aspect ratios for each platform

Benefits
--------

* **Speed**: Create professional video ads in minutes instead of days
* **Cost-effective**: Eliminate expensive video production costs
* **Scalability**: Generate multiple ad variations for testing
* **Consistency**: Maintain brand voice across all ad creatives
* **Optimization**: Create platform-specific versions optimized for each channel

This skill transforms video ad production from a complex, time-consuming process into a simple, automated workflow that delivers professional results at scale.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/g4dr/video-ad-producer/SKILL.md>
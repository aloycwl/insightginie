---
layout: post
title: "Understanding OpenClaw Skill: WorthClip YouTube Video Scorer"
date: 2026-03-07T16:46:01
categories: [24854]
original_url: https://insightginie.com/understanding-openclaw-skill-worthclip-youtube-video-scorer
---

Understanding OpenClaw Skill: WorthClip YouTube Video Scorer
============================================================

Welcome to this comprehensive guide on the WorthClip YouTube Video Scorer skill available on OpenClaw. This powerful tool leverages artificial intelligence to score YouTube videos based on personalized learning goals, providing AI-powered summaries, alignment analysis, and a curated feed. In this article, we'll delve into how this skill works, its setup, and commands, and how it can enhance your video watching experience.

What is WorthClip YouTube Video Scorer?
---------------------------------------

The WorthClip YouTube Video Scorer is an AI-powered tool designed to help users evaluate YouTube videos. It scores videos on a scale of 1 to 10 based on personalized learning goals and user personas. This skill is particularly useful for those looking to manage their tracked channels, check their scored feed, or monitor API usage. With WorthClip, you can get AI summaries, alignment analysis, and a curated video feed tailored to your preferences.

Key Features
------------

* **Personalized Scoring**: Scores videos based on your learning goals and persona.
* **AI Summaries**: Provides concise summaries of videos.
* **Alignment Analysis**: Analyzes how well the video content aligns with your goals.
* **Curated Feed**: Offers a feed of videos sorted by relevance and filtered by your preferences.
* **Channel Management**: Helps you track and manage your favorite YouTube channels.
* **API Usage Monitoring**: Allows you to monitor your API usage and stay within limits.

Setup
-----

1. **Sign Up**: Visit [WorthClip](https://worthclip.com) and sign up for an account.
2. **Generate API Key**: Go to Settings > API Keys and generate an API key.
3. **Set API Key**: Export your API key as an environment variable:

   ```
   export WORTHCLIP_API_KEY="wc_your_key_here"
   ```

Commands
--------

The WorthClip YouTube Video Scorer skill comes with several commands that allow you to interact with the API and manage your video scoring experience.

### Score a Video

This command scores a YouTube video against your persona and goals. It handles asynchronous scoring automatically with polling:

```
bash {baseDir}/scripts/score.sh "VIDEO_ID"
```

The script submits the video for scoring, polls for completion (up to 60 seconds), and returns the completed score JSON. If the video was already scored, it returns the existing score immediately.

### Get Your Feed

This command returns scored videos sorted by relevance, with optional filters:

```
bash {baseDir}/scripts/feed.sh [--min-score N] [--verdict VERDICT] [--limit N] [--cursor N]
```

Options:

* **–min-score N**: Only return videos scored N or above (1-10).
* **–verdict VERDICT**: Filter by verdict (e.g., “watch”, “skip”).
* **–limit N**: Number of results per page.
* **–cursor N**: Pagination cursor from the previous response.

### Check Usage

This command shows your current billing period usage stats and limits:

```
bash {baseDir}/scripts/usage.sh
```

API Reference
-------------

The WorthClip API is hosted on Convex (convex.site), WorthClip's serverless backend. The base URL for the API is:

```
https://greedy-mallard-11.convex.site/api/v1
```

All requests (except /health) require the `Authorization: Bearer YOUR_API_KEY` header.

### Endpoints

| Endpoint | Method | Description |
| --- | --- | --- |
| /health | GET | Health check (no auth required). |
| /score | POST | Score a video (async, returns 202 with jobId). |
| /score/:jobId | GET | Poll scoring job status. |
| /videos/:ytId/summary | GET | Get video summary (summarization). |
| /videos/:ytId | GET | Get video detail with full score. |
| /feed | GET | Paginated scored feed with filters. |
| /channels | GET | List tracked channels. |
| /channels/lookup | POST | Lookup channel by YouTube URL. |
| /channels/track | POST | Track a new channel. |
| /persona | GET | Get current persona and goals. |
| /persona | PUT | Update persona description. |
| /goals | PUT | Update learning goals. |
| /usage | GET | Current billing period usage stats. |

### Rate Limits

General:

* 60 requests/minute (all endpoints).

Scoring:

* 20 requests/minute (POST /score and GET /score/:jobId).

### Response Headers

* `X-RateLimit-Limit`: Maximum requests per window.
* `X-RateLimit-Remaining`: Requests remaining in the current window.
* `Retry-After`: Seconds to wait before retrying (only on 429 responses).

### Error Format

All errors return a consistent JSON structure with an appropriate HTTP status code:

```
{
  "error": {
    "code": "ERROR_CODE",
    "message": "Human-readable description of the error"
  }
}
```

Common error codes:

* `UNAUTHORIZED` (401): Missing or invalid API key.
* `RATE_LIMITED` (429): Too many requests.
* `NOT_FOUND` (404): Resource not found.
* `VALIDATION_ERROR` (400): Invalid request parameters.
* `INTERNAL_ERROR` (500): Server error.

Conclusion
----------

The WorthClip YouTube Video Scorer skill on OpenClaw is a powerful tool for anyone looking to enhance their YouTube video watching experience. With its AI-powered scoring, personalized feed, and comprehensive API reference, it provides a tailored solution for managing and evaluating videos based on your unique learning goals and preferences. By following the setup instructions and utilizing the commands effectively, you can make the most out of this skill and optimize your video consumption.

To learn more and get started, visit the [WorthClip Developers page](https://worthclip.com/developers) and explore the full range of features and capabilities offered by this innovative tool.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/ivanstancich/worthclip-youtube-video-scorer/SKILL.md>
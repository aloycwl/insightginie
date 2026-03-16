---
layout: post
title: "Yoinkit OpenClaw Skill: Revolutionizing Content Research Across Social Platforms"
date: 2026-03-15T21:46:29
categories: [24854]
original_url: https://insightginie.com/yoinkit-openclaw-skill-revolutionizing-content-research-across-social-platforms
---

Yoinkit OpenClaw Skill: A Comprehensive Guide for Multi-Platform Social Content Research
========================================================================================

In the digital age, staying ahead in content research and analysis is crucial. Yoinkit OpenClaw Skill is a powerful tool designed to help you search, analyze, and transcribe content across **13 social platforms**. This guide will walk you through its features, requirements, and how to get started.

Introduction to Yoinkit OpenClaw Skill
--------------------------------------

Yoinkit is a robust tool that integrates seamlessly with OpenClaw, allowing users to perform various operations such as extracting transcripts from videos, fetching full content and metadata from social posts, searching content on different platforms, getting trending content, and retrieving a user's recent posts or videos.

Platforms Supported
-------------------

Before running commands, ensure to check the platform reference for supported operations. Platforms supported for different operations include:

* **Transcripts:** YouTube, TikTok, Instagram, Twitter/X, Facebook
* **Content:** YouTube, TikTok, Instagram, Twitter/X, Facebook, LinkedIn, Reddit, Pinterest, Threads, Bluesky, Truth Social, Twitch, Kick
* **Search:** YouTube, TikTok, Instagram, Reddit, Pinterest
* **Trending:** YouTube, TikTok
* **Feed:** YouTube, TikTok, Instagram, Twitter/X, Facebook, Threads, Bluesky, Truth Social

Requirements and Configuration
------------------------------

To use Yoinkit OpenClaw Skill, you need:

* Yoinkit subscription with API access enabled
* API Token from Yoinkit Settings → OpenClaw

Set your API token in OpenClaw config via chat command or by editing the configuration file.

### Configuration Steps

Via chat command:

```
/config set skills.entries.yoinkit.env.YOINKIT_API_TOKEN="your-token-here"
```

Or edit `~/.openclaw/openclaw.json`:

```
{

"skills": {

"entries": {

"yoinkit": {

"env": {

"YOINKIT_API_TOKEN": "your-token-here",

"YOINKIT_API_URL": "https://yoinkit.ai/api/v1/openclaw"

}

}

}

}

}
```

Commands and Options
--------------------

### Extract Transcript from Video URL

Command: `yoinkit transcript <url> [options]`

* Supported platforms: YouTube, TikTok, Instagram, Twitter/X, Facebook
* Options:
* `--language CODE` — 2-letter language code (YouTube, TikTok only). Example: `en`, `es`, `fr`

Example:

```
yoinkit transcript https://youtube.com/watch?v=abc123

yoinkit transcript https://youtube.com/watch?v=abc123 --language es

yoinkit transcript https://tiktok.com/@user/video/123
```

### Get Full Content and Metadata from a Social Post

Command: `yoinkit content <url>`

Supported platforms: YouTube, TikTok, Instagram, Twitter/X, Facebook, LinkedIn, Reddit, Pinterest, Threads, Bluesky, Truth Social, Twitch, Kick

Example:

```
yoinkit content https://youtube.com/watch?v=abc123

yoinkit content https://twitter.com/user/status/123

yoinkit content https://reddit.com/r/technology/comments/abc
```

### Search Content on a Platform

Command: `yoinkit search <platform> "<query>" [options]`

Supported platforms: YouTube, TikTok, Instagram, Reddit, Pinterest

* Common options:
* `--sort TYPE` — Sort results (platform-specific values, see below)
* `--time PERIOD` — Filter by time (platform-specific values, see below)
* `--cursor TOKEN` — Pagination cursor from previous response
* `--continuation TOKEN` — YouTube pagination token
* `--page N` — Page number (Instagram only)

Platform-specific sort values:

* YouTube: `relevance`, `popular`
* TikTok: `relevance`, `most-liked`, `date-posted`
* Reddit: `relevance`, `new`, `top`, `comment_count`

Platform-specific time values:

* YouTube: `today`, `this_week`, `this_month`, `this_year`
* TikTok: `yesterday`, `this-week`, `this-month`, `last-3-months`, `last-6-months`, `all-time`
* Reddit: `all`, `day`, `week`, `month`, `year`

Example:

```
yoinkit search youtube "AI tools for creators"

yoinkit search youtube "AI tools" --sort popular --time this_week

yoinkit search tiktok "productivity tips" --sort most-liked
```

### Get Currently Trending Content

Command: `yoinkit trending <platform> [options]`

Supported platforms: YouTube, TikTok

* Options:
* `--type TYPE` — TikTok only: `trending` (default), `popular`, or `hashtags`
* `--country CODE` — TikTok only: 2-letter country code (default: US)
* `--period DAYS` — TikTok popular/hashtags: `7`, `30`, or `120`
* `--page N` — TikTok popular/hashtags: page number
* `--order TYPE` — TikTok popular only: `hot`, `like`, `comment`, `repost`

Note: YouTube trending takes no parameters — it returns currently trending shorts.

Example:

```
yoinkit trending youtube

yoinkit trending tiktok

yoinkit trending tiktok --type popular --country US --period 7 --order like
```

### Get a User's Recent Posts/Videos

Command: `yoinkit feed <platform> <handle> [options]`

Supported platforms: YouTube, TikTok, Instagram, Twitter/X, Facebook, Threads, Bluesky, Truth Social

* Options:
* `--type posts|reels|videos` — Content type (Instagram, Facebook). Default: `posts`
* `--sort latest|popular` — Sort order (YouTube only)
* `--ursor TOKEN` — Pagination cursor

Example:

```
yoinkit feed youtube MrBeast

yoinkit feed youtube @mkbhd --sort latest

yoinkit feed tiktok garyvee

yoinkit feed instagram ali-abdaal --type reels
```

Note: Handles work with or without the `@` prefix.

### Automated Research Workflow

Command: `yoinkit research "<topic>" [options]`

This command combines search and trending across platforms to provide a comprehensive research workflow.

* Options:
* `--platforms LIST` — Comma-separated platforms (default: youtube,tiktok)
* `--transcripts` — Also fetch transcripts from top trending results

Example:

```
yoinkit research "home automation"

yoinkit research "AI tools" --platforms youtube,tiktok,reddit

yoinkit research "productivity" --transcripts
```

What it does:

* Searches each platform for the topic
* Gets trending content from supported platforms
* Optionally fetches transcripts from top video results
* Returns combined JSON results for analysis

Natural Language Commands
-------------------------

Yoinkit OpenClaw Skill allows you to use natural language commands, making it user-friendly and accessible. Examples include:

* `"What's trending on TikTok?"` → `yoinkit trending tiktok`
* `"Pull the transcript from this YouTube video: [url]"` → `yoinkit transcript <url>`
* `"Find popular Reddit posts about home automation from this week"` → `yoinkit search reddit "home automation" --sort top --time week`
* `"What has MrBeast posted this week?"` → `yoinkit feed youtube MrBeast`
* `"Check @garyvee's latest TikToks"` → `yoinkit feed tiktok garyvee`
* `"Research what creators are doing with AI tools"` → `yoinkit research "AI tools" --platforms youtube,tiktok,reddit`

API Base URL and Output Formatting
----------------------------------

All requests go through your Yoinkit subscription:

```
https://yoinkit.ai/api/v1/openclaw
```

Yoinkit provides a logo at `assets/yoinkit-logo./media/images/png` (200×200, transparent background, gradient icon).

When presenting Yoinkit results to the user:

* Prefix output with `🟣 Yoinkit` as a header or label
* Format video/post results as clean cards: title, views/engagement, date, link
* Highlight key metadata (views, likes, publish date) — hide raw JSON noise
* For transcript results, provide a concise summary first, then offer the full transcript if asked
* For trending results, present as a numbered list with platform and engagement stats
* For research results, organize by platform with clear section headers
* Include a subtle footer: `Powered by Yoinkit · yoinkit.ai`
* When results are empty or a platform isn't supported, suggest alternatives naturally

Support and Resources
---------------------

For issues and support:

* Issues: <https://github.com/seomikewaltman/yoinkit-openclaw-skill/issues>
* Yoinkit: <https://yoinkit.ai>

Conclusion
----------

Yoinkit OpenClaw Skill is a versatile and powerful tool for content research across multiple social platforms. By integrating seamlessly with OpenClaw, it provides a comprehensive suite of commands to search, analyze, and transcribe content, making it an essential tool for content creators, researchers, and analysts. With its natural language command capabilities and robust output formatting, Yoinkit OpenClaw Skill is designed to enhance your content research workflows efficiently and effectively.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/seomikewaltman/yoinkit/SKILL.md>
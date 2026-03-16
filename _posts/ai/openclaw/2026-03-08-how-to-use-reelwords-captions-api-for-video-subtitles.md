---
layout: post
title: "How to Use ReelWords Captions API for Video Subtitles"
date: 2026-03-08T18:18:36
categories: [24854]
original_url: https://insightginie.com/how-to-use-reelwords-captions-api-for-video-subtitles
---

Introduction to ReelWords Captions API
--------------------------------------

Creating engaging captions for short-form videos is essential for platforms like TikTok, Instagram Reels, and YouTube Shorts. The ReelWords Captions API provides a powerful solution for generating stylized subtitles automatically. This guide will walk you through everything you need to know about using this OpenClaw skill to enhance your video content.

What is the ReelWords Captions API?
-----------------------------------

The ReelWords Captions API is a service that allows you to generate stylized captions for short-form videos. It provides REST API endpoints that let you create caption jobs, poll their status, and download the rendered captioned videos. This skill integrates seamlessly with OpenClaw, making it easy to add professional captions to your videos without manual effort.

Setting Up Your ReelWords Account
---------------------------------

### Step 1: Create a ReelWords Account

Before you can use the API, you need to create an account on the ReelWords platform:

1. Visit <https://reelwords.ai>
2. Sign up or log in to your account
3. Navigate to the account menu in the top-right corner
4. Click on “API Keys” and then “New key”
5. Copy your API key (it will start with “rw\_”)

### Step 2: Configure the API Key

You have two options for providing your API key to OpenClaw:

#### Option A: Environment Variable

```
export REELWORDS_API_KEY="rw_your_api_key_here"
```

#### Option B: OpenClaw Configuration (Recommended)

Edit your ~/.clawdbot/openclaw.json file and add the following configuration:

```
{
  "skills": {
    "entries": {
      "reelwords-captions": {
        "enabled": true,
        "env": {
          "REELWORDS_API_KEY": "rw_your_api_key_here"
        }
      }
    }
  }
}
```

Security Best Practices
-----------------------

Keep your API key secure by following these guidelines:

* Never commit your API key to version control
* Don't share it in public channels or chats
* Rotate your key if you suspect it has been compromised
* Treat it like a password

Using the ReelWords Captions API
--------------------------------

There are two main approaches to using the API: using the helper script or calling the REST endpoints directly.

### Option 1: All-in-One Helper Script

The simplest way to use the API is through the provided helper script:

```
python3 scripts/reelwords_caption_job.py \
  --video-url "https://cdn.reelwords.ai/sample.mp4" \
  --style-id "style1" \
  --add-emojis \
  --max-words-per-line 6 \
  --position-y 82 \
  --font-size 54 \
  --highlight-color "#FFD803" \
  --hook-color "#FF5CAA" \
  --out captioned.mp4
```

This script handles the entire workflow: creating the caption job, polling for completion, and downloading the final video. The output is saved as “captioned.mp4”.

### Option 2: Direct API Calls

For more control, you can call the API endpoints directly using curl.

#### Step 1: Create Caption Job

```
curl -sS https://api.reelwords.ai/api/v1/caption-jobs \
  -H "x-api-key: $REELWORDS_API_KEY" \
  -H "content-type: application/json" \
  -d '{
    "videoUrl": "https://cdn.reelwords.ai/sample.mp4",
    "preferences": {
      "style": {
        "styleId": "style1"
      }
    }
  }'
```

Save the returned job ID for the next steps.

#### Step 2: Poll Job Status

```
curl -sS https://api.reelwords.ai/api/v1/caption-jobs/$JOB_ID \
  -H "x-api-key: $REELWORDS_API_KEY" \
  -H "accept: application/json"
```

Continue polling until the status becomes “completed” or you receive a failure message.

#### Step 3: Download Rendered Video

```
curl -L https://api.reelwords.ai/api/v1/caption-jobs/$JOB_ID/video \
  -H "x-api-key: $REELWORDS_API_KEY" \
  -o captioned.mp4
```

API Workflow Overview
---------------------

The complete workflow follows these steps:

1. Create a caption job via POST /api/v1/caption-jobs
2. Provide required parameters: videoUrl and styleId
3. Optionally include preferences for emojis, text formatting, colors, etc.
4. Poll the job status via GET /api/v1/caption-jobs/{id}
5. Wait for status to become “completed”
6. Download the video from result.downloadUrl or via GET /api/v1/caption-jobs/{id}/video

Available Customization Options
-------------------------------

The API offers extensive customization for your captions:

* **Style ID**: Choose from available caption styles
* **Emojis**: Add emojis to your captions
* **Text formatting**: Control max words per line, font size, and position
* **Colors**: Customize highlight and hook colors
* **Font options**: Adjust font size and positioning

Handling Errors and Limits
--------------------------

When using the API, be aware of potential issues:

* HTTP 402 indicates you've hit usage limits or run out of credits
* Check failureReason and failureMessage for detailed error information
* The API may return new fields over time – design your integration to handle unknown fields gracefully

Best Practices for Integration
------------------------------

To get the most out of the ReelWords Captions API:

1. Always use HTTPS for API calls
2. Include proper error handling in your application
3. Cache successful results when appropriate
4. Monitor API usage to avoid hitting rate limits
5. Test with sample videos before deploying to production

Conclusion
----------

The ReelWords Captions API provides a powerful way to automatically generate stylized captions for short-form videos. Whether you use the convenient helper script or the direct API endpoints, you can significantly enhance your video content's accessibility and engagement. By following the setup instructions and best practices outlined in this guide, you'll be able to seamlessly integrate professional captions into your video workflow.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/kmasterrr/video-captions-reelwords/SKILL.md>
---
layout: post
title: "OpenClaw Meta Business Suite Skill: Facebook &#038; Instagram API Automation"
date: 2026-03-07T13:17:05
categories: [24854]
original_url: https://insightginie.com/openclaw-meta-business-suite-skill-facebook-instagram-api-automation
---

Introduction to the Meta Business Suite Skill
---------------------------------------------

The Meta Business Suite skill for OpenClaw provides comprehensive automation capabilities for Facebook Pages and Instagram Business accounts through Meta’s Graph API. This powerful skill enables users to manage their social media presence programmatically, handling everything from content publishing to analytics collection.

What This Skill Does
--------------------

The Meta Business Suite skill is designed to handle seven core use cases:

1. Publishing posts to Facebook Pages
2. Scheduling Facebook posts for future publication
3. Publishing to Instagram (photos, reels, carousels)
4. Reading insights and analytics from Facebook or Instagram
5. Managing comments on Facebook or Instagram
6. Uploading photos or videos to Facebook Pages
7. Deleting posts from Facebook or Instagram

Prerequisites and Configuration
-------------------------------

Before using this skill, you need to set up proper authentication. The skill requires two critical environment variables:

* **META\_PAGE\_ACCESS\_TOKEN**: Your Facebook Page Access Token
* **META\_PAGE\_ID**: Your Facebook Page ID

Configuration Option A (Recommended): Environment Variables

```
export META_PAGE_ACCESS_TOKEN="your-page-access-token"
export META_PAGE_ID="your-page-id"
```

Configuration Option B: Token Cache File

If environment variables aren’t set, the skill can read credentials from `~/.meta_tokens_cache.json` with appropriate permissions.

API Version Compatibility
-------------------------

The skill is built for Graph API v25.0. Always include this version number in your API calls to ensure compatibility and access to the latest features.

Facebook Page Operations
------------------------

### Publishing Text Posts

Publishing a simple text post to your Facebook Page:

```
curl -X POST "https://graph.facebook.com/v25.0/$PAGE_ID/feed" \
  -d "message=Your message here" \
  -d "access_token=$PAGE_TOKEN"
```

### Publishing Posts with Images

Using image URLs:

```
curl -X POST "https://graph.facebook.com/v25.0/$PAGE_ID/photos" \
  -d "url=https://example.com/image./media/images//media/images//media/images//media/images/jpg" \
  -d "message=Your post text" \
  -d "access_token=$PAGE_TOKEN"
```

Using local files:

```
curl -X POST "https://graph.facebook.com/v25.0/$PAGE_ID/photos" \
  -F "source=@/path/to/image./media/images//media/images//media/images//media/images/jpg" \
  -F "message=Your post text" \
  -F "access_token=$PAGE_TOKEN"
```

### Publishing Video Content

```
curl -X POST "https://graph.facebook.com/v25.0/$PAGE_ID/videos" \
  -F "source=@/path/to/video.mp4" \
  -F "description=Video description" \
  -F "title=Video title" \
  -F "access_token=$PAGE_TOKEN"
```

### Scheduling Posts

Scheduling requires setting `published=false` and providing a Unix timestamp:

```
# Get Unix timestamp: python3 -c "from datetime import datetime; print(int(datetime(2026,3,1,9,0).timestamp()))"
curl -X POST "https://graph.facebook.com/v25.0/$PAGE_ID/feed" \
  -d "message=Scheduled post" \
  -d "published=false" \
  -d "scheduled_publish_time=UNIX_TIMESTAMP" \
  -d "access_token=$PAGE_TOKEN"
```

Scheduled posts must be between 10 minutes and 75 days from the current time.

### Reading Page Information

```
curl -s "https://graph.facebook.com/v25.0/$PAGE_ID?fields=name,fan_count,followers_count,about&access_token=$PAGE_TOKEN"
```

### Managing Comments

```
curl -X POST "https://graph.facebook.com/v25.0/POST_ID/comments" \
  -d "message=Your comment" \
  -d "access_token=$PAGE_TOKEN"
```

Instagram Operations
--------------------

Instagram uses a two-step process for publishing: creating a media container, then publishing it.

### Publishing Photos

```
# Step 1: Create container
CONTAINER_ID=$(curl -s -X POST "https://graph.facebook.com/v25.0/$IG_ID/media" \
  -d "image_url=https://example.com/image./media/images//media/images//media/images//media/images/jpg" \
  -d "caption=Your caption with #hashtags" \
  -d "access_token=$PAGE_TOKEN" |
  python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")

# Step 2: Publish
curl -X POST "https://graph.facebook.com/v25.0/$IG_ID/media_publish" \
  -d "creation_id=$CONTAINER_ID" \
  -d "access_token=$PAGE_TOKEN"
```

### Publishing Reels

```
# Step 1: Create container
CONTAINER_ID=$(curl -s -X POST "https://graph.facebook.com/v25.0/$IG_ID/media" \
  -d "media_type=REELS" \
  -d "video_url=https://example.com/video.mp4" \
  -d "caption=Reel caption #reels" \
  -d "access_token=$PAGE_TOKEN" |
  python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")

# Step 2: Wait for processing
curl -s "https://graph.facebook.com/v25.0/$CONTAINER_ID?fields=status_code&access_token=$PAGE_TOKEN"

# Step 3: Publish
curl -X POST "https://graph.facebook.com/v25.0/$IG_ID/media_publish" \
  -d "creation_id=$CONTAINER_ID" \
  -d "access_token=$PAGE_TOKEN"
```

### Publishing Carousels

```
# Step 1: Create each item
IMG1=$(curl -s -X POST "https://graph.facebook.com/v25.0/$IG_ID/media" \
  -d "image_url=https://example.com/img1./media/images//media/images//media/images//media/images/jpg" \
  -d "is_carousel_item=true" \
  -d "access_token=$PAGE_TOKEN" |
  python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")

IMG2=$(curl -s -X POST "https://graph.facebook.com/v25.0/$IG_ID/media" \
  -d "image_url=https://example.com/img2./media/images//media/images//media/images//media/images/jpg" \
  -d "is_carousel_item=true" \
  -d "access_token=$PAGE_TOKEN" |
  python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")

# Step 2: Create carousel container
CAROUSEL=$(curl -s -X POST "https://graph.facebook.com/v25.0/$IG_ID/media" \
  -d "media_type=CAROUSEL" \
  -d "children=$IMG1,$IMG2" \
  -d "caption=My carousel #carousel" \
  -d "access_token=$PAGE_TOKEN" |
  python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")

# Step 3: Publish
curl -X POST "https://graph.facebook.com/v25.0/$IG_ID/media_publish" \
  -d "creation_id=$CAROUSEL" \
  -d "access_token=$PAGE_TOKEN"
```

Analytics and Insights
----------------------

### Facebook Page Insights

```
curl -s "https://graph.facebook.com/v25.0/$PAGE_ID/insights?metric=page_views_total,page_fan_adds,page_engaged_users.=day&access_token=$PAGE_TOKEN"
```

### Instagram Media Insights

```
curl -s "https://graph.facebook.com/v25.0/MEDIA_ID/insights?metric=impressions,reach,engagement&access_token=$PAGE_TOKEN"
```

Managing Content
----------------

### Deleting Posts

```
curl -X DELETE "https://graph.facebook.com/v25.0/POST_ID?access_token=$PAGE_TOKEN"
```

Best Practices
--------------

1. Always use environment variables for tokens and IDs
2. Handle API rate limits gracefully
3. Test with small batches before scaling
4. Monitor for permission changes or API updates
5. Implement proper error handling and logging

Conclusion
----------

The Meta Business Suite skill for OpenClaw provides a comprehensive solution for automating social media management across Facebook and Instagram. By leveraging Meta’s Graph API, users can streamline their content publishing workflows, gather valuable analytics, and maintain consistent engagement with their audience. Whether you’re a social media manager, content creator, or business owner, this skill can significantly reduce manual effort while improving your social media strategy execution.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/nachx639/meta-business-suite/SKILL.md>
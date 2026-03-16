---
layout: post
title: "Bear Blog Publisher Skill &#8211; OpenClaw Integration"
date: 2026-03-14T13:15:56
categories: [24854]
original_url: https://insightginie.com/bear-blog-publisher-skill-openclaw-integration
---

What is the Bear Blog Publisher Skill?
--------------------------------------

The Bear Blog Publisher skill is an OpenClaw capability that automates the process of publishing blog posts to Bear Blog platform. It supports multiple authentication methods, optional AI-generated content, and automatic diagram generation for technical topics.

### Core Functionality

* Publish markdown content to Bear Blog
* Generate blog posts using AI (OpenAI or Kimi)
* Create technical diagrams with HTML/CSS and Playwright
* Support for multiple authentication methods

Authentication Methods
----------------------

The skill offers three ways to authenticate with Bear Blog, each suited for different use cases:

### Method 1: OpenClaw Config (Personal Use)

Store credentials in ~/.openclaw/openclaw.json:

```
{
  "skills": {
    "bear-blog-publisher": {
      "email": "your@email.com",
      "password": "yourpassword"
    }
  }
}
```

**Security Note:** Set file permissions to 600 (readable only by owner).

### Method 2: Environment Variables (CI/CD)

```
export BEAR_BLOG_EMAIL="your@email.com"
export BEAR_BLOG_PASSWORD="yourpassword"
```

Credentials exist only in memory, not written to disk.

### Method 3: Runtime Parameters (Multi-User)

```
publisher = BearBlogPublisher(
    email="user@example.com",
    password="secret"
)
```

Ideal for chat bots and web applications where credentials are collected at runtime.

AI Content Generation
---------------------

The skill can generate blog content automatically using either OpenAI or Kimi API. To enable this feature:

### OpenAI Setup

```
export OPENAI_API_KEY="sk-..."
```

### Kimi Setup

```
export KIMI_API_KEY="your-kimi-api-key"
```

### Usage Example

```
publisher = BearBlogPublisher()
content = publisher.generate_content(
    topic="Python best practices",
    provider="openai",  # or "kimi"
    tone="professional",
    length="medium"
)
result = publisher.publish(
    title="My Post",
    content=content
)
```

Diagram Generation
------------------

For technical topics, the skill can automatically generate architecture diagrams using HTML/CSS and Playwright. This feature:

* Downloads a ~100MB Chromium browser
* Creates temporary files in /tmp directory
* Uses –no-sandbox flag for containerized environments
* Converts HTML to PNG images

Priority Order for Credentials
------------------------------

1. Runtime parameters (highest priority)
2. Environment variables
3. OpenClaw config file (lowest priority)

Security Best Practices
-----------------------

Follow these guidelines to maintain security:

* Never commit credentials to git repositories
* Use environment variables in production environments
* Set file permissions to 600 for config files
* Prefer runtime parameters for multi-user applications

Security Considerations
-----------------------

The skill makes several operational choices that users should be aware of:

### Playwright Browser Download

Why: Required for generating architecture diagrams as PNG images

Size: ~100MB Chromium browser

Alternative: Skip diagram generation if not needed

### Temporary Files

Location: /tmp/diagram.html and /tmp/diagram.png

Purpose: Intermediate files for diagram generation

Cleanup: Files are overwritten on each run, not explicitly deleted

### –no-sandbox Flag

Why: Required for running Chromium in containerized/Docker environments

Risk: Slightly reduced browser isolation

Mitigation: Only used for local HTML-to-image conversion, no external URLs loaded

### Plaintext Password Storage (Optional)

Config file: Only if user chooses Method 1

Recommendation: Use environment variables (Method 2) or runtime parameters (Method 3) instead

If using config: Always set file permissions to 600

Example Use Cases
-----------------

### With Config File

```
# ~/.openclaw/openclaw.json configured
You: "Publish a blog about Python tips"
AI: [Uses config credentials, publishes]
```

### With Environment Variables

```
export BEAR_BLOG_EMAIL="user@example.com"
export BEAR_BLOG_PASSWORD="secret"
```

```
You: "Publish a blog about Python tips"
AI: [Uses env vars, publishes]
```

### With AI Content Generation

```
export BEAR_BLOG_EMAIL="user@example.com"
export BEAR_BLOG_PASSWORD="secret"
export OPENAI_API_KEY="sk-..."
```

```
You: "Write and publish a blog about Python asyncio"
AI: [Generates content with OpenAI, publishes]
```

### With Runtime Parameters

```
# In your chat bot code
email = get_user_email()  # Ask user
password = get_user_password()  # Ask user
publisher = BearBlogPublisher(
    email=email,
    password=password
)
result = publisher.publish(
    title="My Post",
    content="# Content"
)
```

Implementation Details
----------------------

The skill uses:

* Bear Blog web API
* CSRF token authentication
* Session-based (no persistent storage)
* Playwright for diagram generation
* OpenAI/Kimi API for content generation

License
-------

The Bear Blog Publisher skill is distributed under the MIT License, making it free to use and modify for both personal and commercial projects.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/cattalk2/bear-blog-publisher/SKILL.md>
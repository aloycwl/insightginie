---
layout: post
title: "Understanding the OpenClaw Skill: markdown-publish-share"
date: 2026-03-14T05:16:29
categories: [24854]
original_url: https://insightginie.com/understanding-the-openclaw-skill-markdown-publish-share
---

Introduction to OpenClaw Skill: markdown-publish-share
------------------------------------------------------

The OpenClaw skill `markdown-publish-share` is a powerful tool designed to facilitate the publishing of markdown content with enhanced features such as mermaid diagrams, KaTex, and code blocks. This skill is particularly useful for creating and sharing Software Architecture diagrams, mathematical derivations, and comprehensive system documentation.

Key Features of markdown-publish-share
--------------------------------------

The `markdown-publish-share` skill offers several key features that make it a versatile tool for developers and technical writers:

* **Support for Mermaid Diagrams**: Users can create complex diagrams such as flowcharts, sequence diagrams, and component diagrams using Mermaid syntax.
* **KaTex Integration**: The skill supports KaTex for rendering mathematical expressions and equations directly within the markdown content.
* **Code Block Support**: Developers can include code blocks with syntax highlighting, making it easier to share code snippets and examples.
* **Shareable Links**: After publishing, users receive a shareable link to the rendered document, allowing for easy distribution and collaboration.

How to Use markdown-publish-share
---------------------------------

Using the `markdown-publish-share` skill involves sending a POST request to the AutEng API endpoint. Here's a step-by-step guide on how to use this skill:

### Basic Usage

To publish markdown content, you need to send a JSON payload to the following endpoint:

```
https://auteng.ai/api/tools/docs/publish-markdown/
```

The JSON payload should include the following fields:

* `markdown` (required): The markdown content you wish to publish.
* `title` (optional): The title of the document.
* `expires_hours` (optional): The number of hours after which the document will expire.

### Example Command

Here's an example of how to use the `curl` command to publish markdown content:

```
curl -sS -X POST "https://auteng.ai/api/tools/docs/publish-markdown/" \
-H "Content-Type: application/json" \
-d @- << 'JSON'
{
  "markdown": "# API Test\n\nHello from curl.",
  "title": "API Test",
  "expires_hours": 24
}
JSON
```

### Extracting the Share URL

To extract only the share URL from the response, you can use the following command:

```
curl -sS -X POST "https://auteng.ai/api/tools/docs/publish-markdown/" \
-H "Content-Type: application/json" \
-d '{"markdown":"# Hello\n\nPublished from curl."}' \
| jq -r '.share_url'
```

### Compact Success Payload

To extract a compact success payload, you can use the following command:

```
curl -sS -X POST "https://auteng.ai/api/tools/docs/publish-markdown/" \
-H "Content-Type: application/json" \
-d '{"markdown":"# Hello\n\nPublished from curl."}' \
| jq '{title, share_url, expires_at}'
```

Error Handling
--------------

It's important to note that any response without a `share_url` should be treated as an error. In such cases, the full JSON body should be displayed to help diagnose the issue.

Conclusion
----------

The OpenClaw skill `markdown-publish-share` is an invaluable tool for anyone looking to publish and share markdown content with advanced features like mermaid diagrams, KaTex, and code blocks. By leveraging the AutEng API, users can easily create, publish, and distribute their documents, making it an essential tool for software architects, developers, and technical writers.

For more detailed documentation and examples, visit the [AutEng documentation](https://auteng.ai/llms.txt).

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/operator-auteng-ai/markdown-publish-share/SKILL.md>
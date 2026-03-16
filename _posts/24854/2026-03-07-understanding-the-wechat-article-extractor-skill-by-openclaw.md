---
layout: post
title: "Understanding the WeChat Article Extractor Skill by OpenClaw"
date: 2026-03-07T09:16:57
categories: [24854]
original_url: https://insightginie.com/understanding-the-wechat-article-extractor-skill-by-openclaw
---

What is the WeChat Article Extractor Skill?
-------------------------------------------

The WeChat Article Extractor is a specialized skill developed by OpenClaw that enables developers to extract structured data from WeChat Official Account (微信公众号) articles. This skill is particularly useful for content aggregation, analysis, and repurposing of WeChat articles in various applications.

Core Capabilities
-----------------

The skill offers comprehensive extraction capabilities:

* **URL Parsing**: Extracts data from mp.weixin.qq.com article URLs
* **Metadata Extraction**: Retrieves title, author, description, publish time, and account information
* **Content Retrieval**: Extracts HTML content of articles
* **Cover Image**: Gets the article’s cover image URL
* **Article Type Support**: Handles posts, videos, images, voice messages, text articles, and reposts

Basic Usage
-----------

Using the skill is straightforward with its simple API:

```
const { extract } = require('./scripts/extract.js');
const result = await extract('https://mp.weixin.qq.com/s?__biz=...');
// Returns: { done: true, code: 0, data: {...} }
```

The skill can also extract from HTML content:

```
const html = await fetch(url).then(r => r.text());
const result = await extract(html, { url: sourceUrl });
```

Configuration Options
---------------------

The skill provides several options to customize the extraction process:

* `shouldReturnContent`: Return HTML content (default: true)
* `shouldReturnRawMeta`: Return raw metadata (default: false)
* `shouldFollowTransferLink`: Follow migrated account links (default: true)
* `shouldExtractMpLinks`: Extract embedded mp.weixin links (default: false)
* `shouldExtractTags`: Extract article tags (default: false)
* `shouldExtractRepostMeta`: Extract repost source info (default: false)

Response Format
---------------

On successful extraction, the skill returns a structured response:

```
{
  "done": true,
  "code": 0,
  "data": {
    "account_name": "公众号名称",
    "account_alias": "微信号",
    "account_avatar": "头像URL",
    "account_description": "功能介绍",
    "account_id": "原始ID",
    "account_biz": "biz参数",
    "account_biz_number": 1234567890,
    "account_qr_code": "二维码URL",
    "msg_title": "文章标题",
    "msg_desc": "文章摘要",
    "msg_content": "HTML内容",
    "msg_cover": "封面图URL",
    "msg_author": "作者",
    "msg_type": "post",
    "msg_has_copyright": true,
    "msg_publish_time": "2024-01-15T10:30:00.000Z",
    "msg_publish_time_str": "2024/01/15 10:30:00",
    "msg_link": "文章链接",
    "msg_source_url": "阅读原文链接",
    "msg_sn": "sn参数",
    "msg_mid": 1234567890,
    "msg_idx": 1
  }
}
```

Error Handling
--------------

The skill provides comprehensive error handling with specific error codes:

* **1000**: 文章获取失败 (General failure)
* **1001**: 无法获取文章信息 (Missing title or publish time)
* **1002**: 请求失败 (HTTP request failed)
* **1003**: 响应为空 (Empty response)
* **1004**: 访问过于频繁 (Rate limited)
* **1005**: 脚本解析失败 (Script parsing error)
* **1006**: 公众号已迁移 (Account migrated)

Additional error codes (2001-2016) cover various content and account-related issues including copyright violations, deleted content, blocked accounts, and more.

Dependencies
------------

The skill relies on several npm packages:

* **cheerio**: HTML parsing
* **dayjs**: Date formatting
* **request-promise**: HTTP requests
* **qs**: Query string parsing
* **lodash.unescape**: HTML entities

Key Features
------------

The WeChat Article Extractor skill stands out for its:

* **Robust Error Handling**: Comprehensive error codes and messages
* **Flexible Input**: Accepts both URLs and HTML content
* **Multiple Article Types**: Supports various WeChat content formats
* **Anti-scraping Measures**: Handles WeChat’s anti-scraping mechanisms
* **Sogou Integration**: Can extract from Sogou WeChat search results

Practical Applications
----------------------

This skill is valuable for:

* **Content Aggregators**: Building WeChat article collections
* **Analytics Tools**: Analyzing WeChat content trends
* **Content Repurposing**: Converting WeChat articles for other platforms
* **Research Projects**: Studying WeChat content patterns
* **Archiving Systems**: Preserving WeChat articles

Conclusion
----------

The WeChat Article Extractor skill by OpenClaw provides a powerful and flexible solution for extracting structured data from WeChat Official Account articles. With its comprehensive feature set, robust error handling, and support for various article types, it’s an essential tool for developers working with WeChat content.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/freestylefly/wechat-article-extractor-skill/SKILL.md>
---
layout: post
title: "Understanding the TMS (Telegram Media Server) Skill in OpenClaw"
date: 2026-03-14T19:15:58
categories: [24854]
original_url: https://insightginie.com/understanding-the-tms-telegram-media-server-skill-in-openclaw
---

What is the TMS Skill in OpenClaw?
----------------------------------

The TMS skill is a specialized OpenClaw skill that provides seamless integration with Telegram Media Server (TMS) through its REST API. This skill enables users to manage downloads, search torrents, and monitor download status directly through OpenClaw’s interface.

Core Functionality
------------------

The TMS skill offers four primary operations:

* **Health Check** – Verify API availability
* **List Downloads** – View current download status
* **Add Download** – Initiate new downloads via URL
* **Search Torrents** – Find content through Prowlarr integration

Setting Up the TMS Skill
------------------------

### Base URL Configuration

The skill automatically determines the TMS API base URL using the following logic:

* If `TMS_API_URL` environment variable is set, use that value
* If running on the same host as TMS, default to `http://127.0.0.1:8080`

All API endpoints use the prefix `/api/v1`, so a full endpoint would be `{BaseURL}/api/v1/health`.

### Authentication Options

Authentication is flexible:

* **No authentication** – When OpenClaw and TMS run on the same host, TMS accepts requests from localhost without a key
* **Bearer token** – Send `Authorization: Bearer <TMS_API_KEY>`
* **API key header** – Send `X-API-Key: <TMS_API_KEY>`

API Operations in Detail
------------------------

### Health Check

Endpoint: `GET {BaseURL}/api/v1/health`

This simple endpoint returns `{"status":"ok"}` if the API is reachable. No authentication is required for this endpoint in most configurations.

### Listing Downloads

Endpoint: `GET {BaseURL}/api/v1/downloads`

This operation returns an array of download items with the following properties:

* `id` – Numeric identifier
* `title` – Display name
* `status` – Current state (queued, downloading, converting, completed, failed, stopped)
* `progress` – Download progress (0-100)
* `conversion_progress` – Conversion progress if applicable
* `error` – Error message if failed
* `position_in_queue` – Queue position if queued

### Adding Downloads

Endpoint: `POST {BaseURL}/api/v1/downloads`

Request body requires a JSON object with:

* `url` (required) – Video URL, magnet link, .torrent file URL, or Prowlarr proxy URL
* `title` (optional) – Custom display name

Supported URL types:

* Video URLs (processed by yt-dlp)
* Magnet links (`magnet:...`)
* .torrent file URLs
* Prowlarr proxy download URLs (when configured)

Successful responses return `201` with `{"id": <number>, "title": "<string>"}`.

### Deleting Downloads

Endpoint: `DELETE {BaseURL}/api/v1/downloads/{id}`

This operation stops and removes the download with the specified ID. Returns `204` with no body on success.

### Searching Torrents

Endpoint: `GET {BaseURL}/api/v1/search?q=<query>&limit=20&quality=1080`

Parameters:

* `q` (required) – Search query
* `limit` (optional, 1-100, default 20) – Maximum results
* `quality` (optional) – Filter by quality string

Results include:

* `title`
* `size`
* `magnet`
* `torrent_url`
* `indexer_name`
* `peers`

When adding from search results, use the `magnet` field in the POST /downloads request.

Practical Usage Examples
------------------------

### Adding a Video

```
const response = await fetch(
  `${baseURL}/api/v1/downloads`,
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer YOUR_API_KEY'
    },
    body: JSON.stringify({
      url: 'https://youtube.com/watch?v=VIDEO_ID',
      title: 'My Video'
    })
  }
);
```

### Searching and Adding a Torrent

```
// Search
const searchResponse = await fetch(
  `${baseURL}/api/v1/search?q=ubuntu+linux&limit=10`
);
const results = await searchResponse.json();

// Add the first result
const addResponse = await fetch(
  `${baseURL}/api/v1/downloads`,
  {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer YOUR_API_KEY'
    },
    body: JSON.stringify({
      url: results[0].magnet,
      title: results[0].title
    })
  }
);
```

Security Considerations
-----------------------

The skill implements proper security practices:

* Uses environment variables for sensitive configuration
* Supports both token-based and header-based authentication
* Defaults to localhost-only access when no authentication is configured

Integration Benefits
--------------------

By using the TMS skill, OpenClaw provides:

* Unified download management interface
* Support for multiple content types (videos, torrents)
* Real-time download status monitoring
* Powerful search capabilities through Prowlarr
* Programmatic control for automation workflows

Conclusion
----------

The TMS skill transforms OpenClaw into a powerful media management platform by providing direct access to Telegram Media Server’s capabilities. Whether you’re downloading videos, managing torrents, or building automated workflows, this skill offers the tools you need through a well-documented, secure API interface.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/nikitadmitryuk/tms/SKILL.md>
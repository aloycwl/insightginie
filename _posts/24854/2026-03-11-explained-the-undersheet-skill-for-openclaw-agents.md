---
layout: post
title: "Explained: The UnderSheet Skill for OpenClaw Agents"
date: 2026-03-11T05:46:01
categories: [24854]
original_url: https://insightginie.com/explained-the-undersheet-skill-for-openclaw-agents
---

UnderSheet is a powerful skill designed for OpenClaw agents, offering persistent thread memory across various platforms. This article will delve into the functionalities of UnderSheet, its installation and setup process, and how it can enhance your OpenClaw agent’s performance.

Understanding UnderSheet’s Purpose
----------------------------------

OpenClaw agents operate in a stateless manner, meaning they lose all context after each heartbeat. UnderSheet addresses this limitation by providing:

* Thread tracking across platforms (Moltbook, Hacker News, Reddit, Discord, Twitter)
* New reply notifications for monitored threads
* A feed cursor to prevent reading the same post multiple times
* Platform-agnostic memory persisting between agent restarts

Key Features of UnderSheet
--------------------------

UnderSheet offers several advantages for OpenClaw agents:

* **Zero Dependencies**: Built with pure Python stdlib, making it lightweight and easy to integrate.
* **Pluggable Platform Adapters**: Supports multiple platforms through modular adapters, allowing you to use one skill for all your needs.
* **Advanced Tracking**: Monitors threads and surfaces only new replies, saving processing time.
* **Feed Management**: Implements a cursor system to show only unread posts.
* **Proxy Support**: Enables routing agent traffic through proxies or VPNs without system configuration changes.

Installation Process
--------------------

To install UnderSheet, follow these steps:

```
curl -fsSL https://raw.githubusercontent.com/ubgb/undersheet/main/undersheet.py \n-o ~/.openclaw/skills/undersheet/undersheet.py
mkdir -p ~/.openclaw/skills/undersheet/platforms
curl -fsSL https://raw.githubusercontent.com/ubgb/undersheet/main/platforms/moltbook.py \n-o ~/.openclaw/skills/undersheet/platforms/moltbook.py
curl -fsSL https://raw.githubusercontent.com/ubgb/undersheet/main/platforms/hackernews.py \n-o ~/.openclaw/skills/undersheet/platforms/hackernews.py
curl -fsSL https://raw.githubusercontent.com/ubgb/undersheet/main/platforms/reddit.py \n-o ~/.openclaw/skills/undersheet/platforms/reddit.py
```

Platform Configuration
----------------------

For UnderSheet to function properly, you’ll need to configure credentials for each platform you want to use:

### Moltbook

```
echo '{"api_key": "YOUR_KEY", "agent_name": "YOUR_NAME"}' \n> ~/.config/moltbook/credentials.json
```

### Hacker News

```
echo '{"username": "YOUR_HN_USER", "password": "YOUR_HN_PASS"}' \n> ~/.config/undersheet/hackernews.json
```

### Reddit

```
echo '{"client_id": "...", "client_secret": "...", "username": "...", "password": "...", "user_agent": "undersheet:v1.0 (by /u/youruser)"}' > ~/.config/undersheet/reddit.json
```

### Discord

Set up a Discord bot and configure its token:

```
echo '{"bot_token": "Bot YOUR_TOKEN_HERE", "guild_id": "YOUR_SERVER_ID"}' \n> ~/.config/undersheet/discord.json
```

Ensure your bot has the required permissions: Read Messages, Send Messages, Read Message History, and Use Public Threads.

### Twitter/X

```
echo '{"bearer_token": "AAA...", "api_key": "...", "api_secret": "...", "access_token": "...", "access_token_secret": "..."}' > ~/.config/undersheet/twitter.json
```

Note that Twitter’s free tier only supports read-only access via the bearer\_token alone.

Using UnderSheet
----------------

UnderSheet offers several command-line operations:

### Heartbeat

Check tracked threads and new feed posts across platforms:

```
python3 ~/.openclaw/skills/undersheet/undersheet.py heartbeat --platform moltbook
python3 ~/.openclaw/skills/undersheet/undersheet.py heartbeat --platform hackernews
python3 ~/.openclaw/skills/undersheet/undersheet.py heartbeat --platform reddit
```

### Thread Tracking

Start monitoring a specific thread:

```
python3 ~/.openclaw/skills/undersheet/undersheet.py track --platform hackernews --thread-id 47147183
```

### Feed Management

View only new feed posts with optional minimum score filtering:

```
python3 ~/.openclaw/skills/undersheet/undersheet.py feed-new --platform reddit --min-score 50
```

Proxy Support
-------------

UnderSheet supports routing agent traffic through HTTP proxies or VPNs. Configure via JSON file or command-line:

```
echo '{"http": "http://yourproxy:8080"}' > ~/.config/undersheet/proxy.json
```

Or use HTTP/HTTPS/ALL\_PROXY environment variables.

Adding UnderSheet to Your Agent’s Heartbeat
-------------------------------------------

To integrate UnderSheet into your agent’s routine, add these entries to your HEARTBEAT.md file:

```
## UnderSheet (every 30 minutes)
- python3 ~/.openclaw/skills/undersheet/undersheet.py heartbeat --platform moltbook
- python3 ~/.openclaw/skills/undersheet/undersheet.py heartbeat --platform hackernews
```

Creating Custom Platform Adapters
---------------------------------

UnderSheet’s modular architecture allows you to add support for new platforms. Create a new file in the platforms directory:

```
from undersheet import PlatformAdapter

class Adapter(PlatformAdapter):
    name = "myplatform"
    
    def get_threads(self, thread_ids): ...
    def get_feed(self, limit=25, **kwargs): ...
    def post_comment(self, thread_id, content, **kwargs): ...
```

Once implemented, your custom adapter will be available for use:

```
python3 undersheet.py heartbeat --platform myplatform
```

Conclusion
----------

UnderSheet is an invaluable addition to any OpenClaw agent, providing persistent memory capabilities across multiple platforms. By implementing thread tracking, feed management, and platform-agnostic memory, UnderSheet enhances your agent’s ability to engage effectively with online communities while maintaining context between interactions.

The skill’s lightweight implementation, extensive platform support, and easy customization make it an excellent choice for developers looking to improve their OpenClaw agent’s performance and memory capabilities.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/ubgb/undersheet/SKILL.md>
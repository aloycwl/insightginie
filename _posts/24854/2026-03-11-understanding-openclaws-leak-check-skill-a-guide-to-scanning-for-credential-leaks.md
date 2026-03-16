---
layout: post
title: "Understanding OpenClaw&#8217;s Leak-Check Skill: A Guide to Scanning for Credential Leaks"
date: 2026-03-11T18:46:10
categories: [24854]
original_url: https://insightginie.com/understanding-openclaws-leak-check-skill-a-guide-to-scanning-for-credential-leaks
---

Understanding OpenClaw’s Leak-Check Skill

Understanding OpenClaw’s Leak-Check Skill: A Guide to Scanning for Credential Leaks
===================================================================================

In the world of AI and machine learning, security and privacy are paramount. OpenClaw’s leak-check skill is designed to help users scan their session logs for leaked credentials, providing an additional layer of security. This article will delve into what this skill does, how it works, and its key features.

What is OpenClaw’s Leak-Check Skill?
------------------------------------

OpenClaw’s leak-check skill is a tool that scans OpenClaw session JSONL files for leaked credentials. It reports which real AI provider (such as Anthropic, OpenAI, Google, etc.) received the data, skipping internal delivery echoes. This skill is crucial for identifying potential security breaches and ensuring that sensitive credentials are not inadvertently leaked.

Quick Start
-----------

To get started with the leak-check skill, you can run the following commands:

* `node scripts/leak-check.js` – Check for leaked credentials (default: discord format)
* `node scripts/leak-check.js --format json` – JSON output

Configuration
-------------

Credentials to check are defined in `leak-check.json`. The script searches for this file in the following order:

* Skill directory (`./leak-check.json`) – for backward compatibility
* `~/.openclaw/credentials/leak-check.json` – recommended persistent location (survives skill updates via clawhub)

Since clawhub clears the skill directory on updates, it’s recommended to place your config in `~/.openclaw/credentials/` to avoid losing it:

```
mkdir -p ~/.openclaw/credentials
cp leak-check.json ~/.openclaw/credentials/leak-check.json
```

You can also specify an explicit path with the `--config` option.

### Example Configuration

The `leak-check.json` file should contain an array of objects, each representing a credential to check. Here’s an example configuration:

```
[
    {
        "name": "Discord",
        "search": "abc*xyz"
    },
    {
        "name": "Postmark",
        "search": "k7Qm9x"
    }
]
```

#### Important Notes:

* **Do not store full credentials in this file.** Use only a partial fragment—enough to uniquely identify the credential via a contains, begins-with, or ends-with match.
* **Wildcard patterns:**

+ `abc*` – starts with “abc”
+ `*xyz` – ends with “xyz”
+ `abc*xyz` – starts with “abc” AND ends with “xyz”
+ `abc` (no asterisk) – contains “abc”
+ `""` (empty) – skip this credential

Options
-------

The leak-check skill provides several options that can be used to customize its behavior:

* `--format <type>` – Output format: `discord` (default) or `json`
* `--config <path>` – Path to credential config file (default: `./leak-check.json`, then `~/.openclaw/credentials/leak-check.json`)
* `--help, -h` – Show help message

Output
------

The leak-check skill provides output in two formats: Discord and JSON.

### Discord (Default)

The default output format is designed to be easily readable and visually appealing. Here’s an example of the Discord output:

```
🔐 **Credential Leak Check**
⚠️ **2 leaked credentials found**
**Discord Token**
• Session: `abc12345` | 2026-02-14 18:30 UTC | Provider: anthropic
**Postmark**
• Session: `def67890` | 2026-02-10 09:15 UTC | Provider: anthropic
```

Or if clean:

```
🔐 **Credential Leak Check**
✅ No leaked credentials found (checked 370 files, 7 credentials)
```

### Config Echoes

If the `leak-check.json` config file is read or discussed during an OpenClaw session, the credential patterns will appear in that session’s JSONL log. The scanner detects this and reports these matches separately as **config echoes** rather than real leaks:

```
📋 **3 possible config echoes** (session contains leak-check config)
• **Discord**: 1 session
...
✅ No credential leaks beyond config echoes
```

Config echoes will continue to appear on every run until the session file is removed. To clear them, delete the session file from `~/.openclaw/agents/main/sessions/`:

```
rm ~/.openclaw/agents/main/sessions/.jsonl
```

#### Tip:

Avoid reading or referencing `leak-check.json` during an OpenClaw session. If it happens, note the session ID from the report and delete it.

### JSON

The JSON output format provides a structured and machine-readable representation of the leak-check results. Here’s an example of the JSON output:

```
{
    "leaks": [
        {
            "credential": "Discord Token",
            "session": "abc12345",
            "timestamp": "2026-02-14T18:30:00.000Z",
            "provider": "anthropic"
        }
    ],
    "configEchoes": [
        {
            "credential": "Gateway",
            "session": "b175e53c",
            "timestamp": "2026-02-19T18:00:30.067Z",
            "provider": "minimax-portal",
            "configEcho": true
        }
    ],
    "summary": {
        "filesScanned": 370,
        "credentialsChecked": 7,
        "leaksFound": 2,
        "configEchoesFound": 1
    }
}
```

Security
--------

The leak-check skill is designed to be local-only and read-only. The following properties can be verified by inspecting `scripts/leak-check.js`:

* **No network access** – no use of `http`, `https`, `net`, `dgram`, `fetch`, `WebSocket`, or any network API
* **No child processes** – no use of `child_process`, `exec`, `spawn`, or `execSync`
* **No external dependencies** – zero `npm` packages; only Node.js built-ins (`fs`, `path`, `os`)
* **No dynamic code execution** – no `eval()`, `Function()`, or dynamic `require()` / `import()`
* **No file writes** – only `fs.readFileSync`, `fs.existsSync`, and `fs.readdirSync` are used; no files are created, modified, or deleted
* **No environment variable access** – does not read `process.env`
* **Output is stdout only** – all results go to `console.log`; nothing is sent elsewhere

### Verify It Yourself

You can confirm that no unexpected APIs are used anywhere in the script by running the following command:

```
grep -E 'require(|import |http|fetch|net.|dgram|child_process|exec|spawn|eval(|Function(|.write|.unlink|.rename|process.env' scripts/leak-check.js
```

This command will search for any usage of the specified APIs in the `scripts/leak-check.js` file. The expected output should only include the three built-in `require()` calls at the top of the file:

```
const fs = require('fs');
const path = require('path');
const os = require('os');
```

Conclusion
----------

OpenClaw’s leak-check skill is a powerful tool for scanning session logs and identifying potential credential leaks. By understanding how this skill works and utilizing its key features, you can enhance the security of your OpenClaw sessions and mitigate the risks associated with credential leaks.

For more information, visit the [Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/khaney64/leak-check/SKILL.md>](<p)
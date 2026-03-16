---
layout: post
title: "How WIP File Guard Protects Your Identity Files from Destructive Edits"
date: 2026-03-09T22:45:58
categories: [24854]
original_url: https://insightginie.com/how-wip-file-guard-protects-your-identity-files-from-destructive-edits
---

How WIP File Guard Protects Your Identity Files from Destructive Edits
======================================================================

In this article, we'll explore the [wip-file-guard](https://github.com/openclaw/skills/blob/main/skills/skills/parkertoddbrooks/wip-file-guard/SKILL.md) skill, a crucial technical guardrail for protecting identity files in [OpenClaw](https://github.com/openclaw) and [Claude Code](https://github.com/workpresence) environments. Understand how this tool blocks harmful edits while allowing useful modifications to your important CLAUDE.md, SOUL.md, IDENTITY.md, MEMORY.md, and other identity files.

What is WIP File Guard?
-----------------------

The **wip-file-guard** skill, created by Parker Todd Brooks, is a safeguard mechanism designed to prevent destructive edits to protected identity files in Claude Code CLI and OpenClaw environments. Its primary function is to block overwrites and excessive removals while allowing small, constructive edits to crucial configuration files.

When to Use WIP File Guard
--------------------------

This skill becomes particularly valuable in several scenarios:

* **Protecting identity files:** Prevents accidental overwrites of core files like CLAUDE.md, SOUL.md, IDENTITY.md, MEMORY.md, and CONTEXT.md.
* **Preventing destructive AI agent actions:** Blocks agents from replacing file content instead of properly extending it.
* **Surviving context compaction:** Unlike behavioral rules, file guards persist through context compaction events.
* **Maintaining project integrity:** Preserve your Soul, define your AI, secure your prompt, and keep your role intact.
* **Workpresence configuration protection:** Safeguard your business setup docs from accidental destruction.

Key Features and Functionality
------------------------------

The wip-file-guard implements two primary rules:

1. **Write blocking:** Completely blocks any Write operations on protected files, redirecting the agent to use Edit instead.
2. **Conditional edit blocking:** Blocks Edit operations that remove more than 2 net lines from protected files while allowing smaller modifications.

It protects specific files including CLAUDE.md, SHARED-CONTEXT.md, SOUL.md, IDENTITY.md, CONTEXT.md, TOOLS.md, MEMORY.md, as well as any file matching patterns like memory, memories, journal, diary, or daily log.

Installation and Configuration
------------------------------

To implement the wip-file-guard in your Claude Code environment:

1. Ensure you have Node.js installed on your system
2. Download the wip-file-guard skill from the OpenClaw GitHub repository
3. Add the hook configuration to your ~/.claude/settings.json file:

```
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "node "/path/to/wip-file-guard/guard.mjs"",
            "timeout": 5
          }
        ]
      }
    ]
  }
}
```

You can verify the installation by running `node guard.mjs --list` to view protected files.

How It Works: The Technical Protection Mechanism
------------------------------------------------

The wip-file-guard functions as a pre-operation hook that examines requests before they execute. Here's how it processes different operations:

* **Write operations:** Detects attempts to overwrite protected files and blocks them, prompting the agent to switch to Edit operations.
* **Edit operations:** Calculates the net line changes. If the edit would remove more than 2 lines, it blocks the operation; otherwise, it allows the edit to proceed.
* **Protected file identification:** Maintains a list of protected files and file pattern matches that are constantly verified against any file operation requests.

When an operation is blocked, the agent receives a clear denial message explaining the protection and suggesting appropriate alternatives, such as using Edit instead of Write.

Best Practices and Common Use Cases
-----------------------------------

To maximize the effectiveness of wip-file-guard, follow these recommendations:

* **Regularly update your identity files:** While protected, these files should still be maintained to reflect current configurations and knowledge.
* **Use the allowed edit operations:** Know that small edits (adding or modifying 1-2 lines) are permitted and sufficient for most adjustments.
* **Verify protected files:** Periodically check the list of protected files using the `--list` flag to ensure important files aren't missed.
* **Monitor agent behavior:** Watch for attempts to circumvent the protection, which may indicate the agent has lost context or is acting unpredictably.

Troubleshooting and Limitations
-------------------------------

Be aware of these potential issues and their solutions:

* **Agent insistence on Write operations:** The deny message tells the agent to use Edit instead. If the agent persists, it may be due to context compaction or loss. In such cases, the protection will continue to block, ensuring safety.
* **Unexpected Edit blocking:** If reasonable edits are blocked, verify the net line changes. Edits removing more than 2 lines from protected files will be denied.
* **Limitation on binary files:** The protection doesn't work on binary files or images.
* **Execution timeout:** The hook runs for a maximum of 5 seconds to prevent hanging operations.

Importantly, note that this skill is designed specifically for code-based identity file protection and may not be suitable for all file types or projects. For non-technical guardrails, explicit prompt instructions should be used.

The Importance of File Protection
---------------------------------

Protected identity files like CLAUDE.md contain fundamental configurations, memories, tools, and behavioral rules that define how your AI operates. Destructive edits to these files can:

* Eliminate critical context and knowledge about your environment
* Remove configured behaviors and constraints
* Overwrite established identities and tool access
* Compromise your agent's ability to act in accordance with your expectations

Without such technical protections, the AI might replace rather than extend your identity files, potentially leading to ineffective or unsafe agent behavior. Context compaction only exacerbates this risk by erasing behavioral rules while preserving hooks like wip-file-guard.

Conclusion
----------

The wip-file-guard skill provides essential technical protection for your identity files in Claude Code and OpenClaw environments. By carefully controlling edits while allowing small modifications, this tool helps maintain the integrity of your configurations and prevents accidental or malicious overwrites. As you work with AI agents, remember that technical protections like hooks work alongside, not instead of, explicit prompt instructions—offering an additional layer of safety for your critical configuration files.

For those interested in technical guardrails and agent safety, consider exploring other OpenClaw skills and techniques that complement file protection, such as memory preservation, behavioral constraints, and context verification.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/parkertoddbrooks/wip-file-guard/SKILL.md>
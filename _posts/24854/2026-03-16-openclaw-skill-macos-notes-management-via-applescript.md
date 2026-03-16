---
layout: post
title: "OpenClaw Skill: macOS Notes Management via AppleScript"
date: 2026-03-16T09:16:40
categories: [24854]
original_url: https://insightginie.com/openclaw-skill-macos-notes-management-via-applescript
---

What This OpenClaw Skill Does
-----------------------------

The macOS Notes skill is a powerful automation tool that allows you to create, read, search, and manage Apple Notes on macOS through a simple command-line interface. This skill uses AppleScript and Python to interact with the native Notes.app, making it perfect for users who want to integrate note-taking into their workflows or build voice-controlled assistants.

### Core Functionality

This skill provides a comprehensive set of commands for managing your Apple Notes:

* **Create notes** – Jot down ideas, meeting notes, or any information you need to save
* **Read notes** – Retrieve and view existing notes by title
* **Search notes** – Find notes containing specific text across your accounts
* **List notes** – Browse your notes with optional folder and account filtering
* **Manage folders** – Discover available accounts and folders in your Notes.app

### Key Features and Benefits

The skill is designed with practical considerations in mind:

* **Natural language processing** – Maps conversational requests like “note this down” or “show my notes” to specific commands
* **Multi-account support** – Works with iCloud, On My Mac, and other Notes accounts
* **HTML/Plain text flexibility** – Accepts both plain text (converted to HTML) and raw HTML content
* **Security-conscious** – Skips password-protected notes and uses JSON input via stdin to avoid command-line exposure
* **Comprehensive logging** – All actions are logged with timestamps for audit and debugging

### Getting Started

To use this skill effectively, you’ll need to start by discovering your available folders:

```
$SKILL_DIR/scripts/notes.sh list-folders
```

This command shows you the accounts and folder names available in your Notes.app, which is essential for targeting specific locations when creating or reading notes.

### Usage Examples

Here are practical examples of how to use the skill:

**Create a simple note:**

```
echo '{"title":"Meeting notes","body":"Discussed Q1 roadmap\n- Launch MVP\n- Iterate on feedback"}' | "$SKILL_DIR/scripts/notes.sh" create-note
```

**Search for specific content:**

```
echo '{"query":"password"}' | "$SKILL_DIR/scripts/notes.sh" search-notes
```

**Read a specific note:**

```
echo '{"name":"Hinge"}' | "$SKILL_DIR/scripts/notes.sh" read-note
```

### Best Practices

For optimal use of this skill:

* Always run `list-folders` first if you’re unsure about account/folder names
* Specify both account and folder when targeting specific locations to avoid ambiguity
* Use plain text for body content unless you need rich HTML formatting
* Remember that the first line of your body becomes the note title in Notes.app
* Be aware that password-protected notes cannot be accessed through this skill

### Technical Requirements

This skill requires:

* macOS with Notes.app installed
* Python 3 for JSON parsing
* osascript (AppleScript) for macOS automation

The skill is MIT licensed and maintained by lucaperret as part of the OpenClaw skills collection, making it a reliable choice for developers and power users looking to automate their macOS note-taking workflows.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/lucaperret/macos-notes/SKILL.md>
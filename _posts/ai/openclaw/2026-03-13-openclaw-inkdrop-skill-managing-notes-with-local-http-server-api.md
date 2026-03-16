---
layout: post
title: "OpenClaw Inkdrop Skill: Managing Notes with Local HTTP Server API"
date: 2026-03-13T00:17:51
categories: [24854]
original_url: https://insightginie.com/openclaw-inkdrop-skill-managing-notes-with-local-http-server-api
---

What is the OpenClaw Inkdrop Skill?
-----------------------------------

The OpenClaw Inkdrop Skill is a powerful integration that allows you to interact with your Inkdrop notes directly through OpenClaw's skill system. This skill enables you to read, create, update, search, and delete notes using Inkdrop's local HTTP server API, making it perfect for managing your thoughts, project backlogs, task lists, and any other information you want to persist in Inkdrop.

Prerequisites and Setup
-----------------------

Before you can use the Inkdrop skill, you'll need to have a few things in place:

1. Install and run the **Inkdrop desktop app** on your machine
2. Enable the **Local HTTP Server** in Inkdrop preferences (Preferences → API → Enable Local HTTP Server)
3. Take note of the port number, username, and password from your Inkdrop preferences

Once you have these prerequisites, you'll need to set up your environment variables:

```
export INKDROP_URL="http://localhost:19840" # default port
export INKDROP_AUTH="username:password" # from Inkdrop preferences
```

For OpenClaw specifically, it's recommended to store these credentials in a secrets file (like workspace secrets.md) and source them at runtime rather than persisting plaintext credentials in your shell profile.

Connecting to Inkdrop
---------------------

The skill connects to Inkdrop using a base URL (default: http://localhost:19840) and Basic authentication via the INKDROP\_AUTH environment variable. You can verify your connection works with this simple test:

```
curl -s -u "$INKDROP_AUTH" "${INKDROP_URL:-http://localhost:19840}/"
```

This should return a JSON response like: `{"version":"5.x.x","ok":true}`

Core Functionality
------------------

### Managing Notes

The skill provides comprehensive note management capabilities:

* **List Notes**: Retrieve all notes or search with specific keywords, limit results, and sort by various criteria
* **Get Single Document**: Fetch individual notes, notebooks, tags, or files using their document ID
* **Create Notes**: Add new markdown notes with titles, content, and categorization
* **Update Notes**: Modify existing notes (requires fetching the current revision token first)
* **Delete Documents**: Remove notes, notebooks, tags, or files

### Working with Notebooks

Organize your notes into notebooks:

* **List Notebooks**: View all available notebooks
* **Create Notebook**: Add new notebooks for better organization

### Managing Tags

Enhance note organization with tags:

* **List Tags**: See all existing tags
* **Create Tag**: Add new tags with custom colors

### Handling Attachments

Manage files and images that can be attached to notes through the files endpoint.

### Changes Feed

Monitor updates in real-time using the changes feed, which returns notes in the order they were modified. This is particularly useful for syncing or watching for updates.

Using the Helper Script
-----------------------

The skill includes a convenient helper script (scripts/inkdrop.sh) that wraps common operations:

```
# List all notes
./scripts/inkdrop.sh notes

# Search notes
./scripts/inkdrop.sh search "project ideas"

# Get a specific note
./scripts/inkdrop.sh get "note:abc123"

# Create a note
./scripts/inkdrop.sh create "My Note" "book:inbox" "Note content here"

# List notebooks
./scripts/inkdrop.sh books

# List tags
./scripts/inkdrop.sh tags

# Delete a document
./scripts/inkdrop.sh delete "note:abc123"
```

Note Structure and Conventions
------------------------------

Notes in Inkdrop have a specific structure:

* **\_id**: Auto-generated note identifier (e.g., note:abc123)
* **\_rev**: Revision token required for updates to prevent conflicts
* **title**: The note's title
* **body**: Markdown content
* **doctype**: Always “markdown”
* **bookId**: Notebook ID (use “book:inbox” as default)
* **tags**: Array of tag IDs
* **status**: One of: none, active, onHold, completed, dropped
* **pinned**: Boolean to pin to top
* **share**: private or public
* **createdAt/updatedAt**: Unix timestamps

Common conventions include using “book:inbox” as the default notebook for quick captures, matching notebook names when context is clear, using markdown formatting in note bodies, and always fetching the \_rev before updating to avoid conflicts.

When to Use This Skill
----------------------

The Inkdrop skill is ideal when users ask to:

* Take notes
* Save ideas
* Manage project notes
* Read notes
* Search notes
* Interact with Inkdrop in any way
* Organize thoughts, project backlogs, or task lists that should persist in Inkdrop

Conclusion
----------

The OpenClaw Inkdrop Skill provides a seamless bridge between OpenClaw's capabilities and Inkdrop's powerful note-taking features. By leveraging the local HTTP server API, it offers a robust solution for managing your digital notes and ideas directly from your OpenClaw environment. Whether you're capturing quick thoughts, organizing complex projects, or maintaining a personal knowledge base, this skill makes it easy to integrate your note-taking workflow into your broader productivity system.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/iamngoni/inkdrop/SKILL.md>
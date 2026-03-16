---
layout: post
title: "OpenClaw Skill: Clawboard Integration and Setup"
date: 2026-03-14T04:17:22
categories: [24854]
original_url: https://insightginie.com/openclaw-skill-clawboard-integration-and-setup
---

OpenClaw Skill: Clawboard Integration and Setup
===============================================

This OpenClaw skill provides comprehensive functionality for installing, configuring, and operating Clawboard within the OpenClaw ecosystem. It handles everything from initial installation to token setup, Docker service management, and plugin integration.

Skill Overview
--------------

The Clawboard skill is designed to help users quickly get a fully functional Clawboard installation running with OpenClaw. It supports multiple installation methods and ensures all components are properly configured and communicating with each other.

### Current Architecture

The Clawboard architecture consists of several interconnected services:

* **Web Interface** (Next.js): Accessible at http://localhost:3010
* **API Service** (FastAPI + SQLite): Running at http://localhost:8010
* **Classifier** (async stage-2 worker): Handles topic/task classification
* **Qdrant** (vector index): Dense retrieval backend using internal Docker network
* **Clawboard Logger Plugin**: Stage-1 firehose logging with response-time context extension

The retrieval/search stack combines dense vectors, BM25, and lexical matching with reciprocal rank fusion and reranking. Qdrant serves as the primary vector database, with SQLite as an embeddings mirror/fallback.

Installation Modes
------------------

### 1. Quick Scripted Install (Recommended)

The fastest way to get started is using the automated bootstrap script:

```
curl -fsSL https://raw.githubusercontent.com/sirouk/clawboard/main/scripts/bootstrap_openclaw.sh | bash
```

This script automatically:

* Detects your OpenClaw workspace and installs Clawboard in the appropriate location
* Generates a security token if one doesn't exist
* Configures environment variables for browser access
* Builds and starts all Docker services
* Installs the skill in OpenClaw (default: symlink mode)
* Installs and enables the clawboard-logger plugin
* Configures plugin settings and restarts OpenClaw gateway

Useful flags include:

```
--integration-level full|write|manual
--no-backfill
--api-url http://localhost:8010
--web-url http://localhost:3010
--web-hot-reload
--public-api-base https://api.example.com
--public-web-url https://clawboard.example.com
--token <token>
--title "<name>"
--skill-symlink (default)
--skill-copy (fallback)
--update
```

### 2. Manual Installation

For users who prefer manual control, follow these steps:

```
# Clone the repository
CLAWBOARD_DIR="${CLAWBOARD_DIR:-$HOME/clawboard}"
git clone https://github.com/sirouk/clawboard "$CLAWBOARD_DIR"
cd "$CLAWBOARD_DIR"

# Create token and environment
cp .env.example .env
openssl rand -hex 32
# Set CLAWBOARD_TOKEN=<value> in $CLAWBOARD_DIR/.env
# Set CLAWBOARD_PUBLIC_API_BASE=<browser-reachable-api-url>
# Optional: Set CLAWBOARD_PUBLIC_WEB_URL=<browser-reachable-ui-url>

# Start Clawboard services
docker compose up -d --build

# Install skill in OpenClaw
mkdir -p "$HOME/.openclaw/skills"
rm -rf "$HOME/.openclaw/skills/clawboard"
ln -s "$CLAWBOARD_DIR/skills/clawboard" "$HOME/.openclaw/skills/clawboard"

# Install and enable logger plugin
openclaw plugins install -l "$CLAWBOARD_DIR/extensions/clawboard-logger"
openclaw plugins enable clawboard-logger

# Configure plugin
openclaw config set plugins.entries.clawboard-logger.config --json '
{
  "baseUrl":"http://localhost:8010",
  "token":"YOUR_TOKEN",
  "enabled":true,
  "contextMode":"auto",
  "contextFallbackMode":"cheap",
  "contextFetchTimeoutMs":1200
}'

# Restart OpenClaw gateway
openclaw restart
```

Skill Path Management
---------------------

The skill supports two operational modes:

### Symlink Mode (Default)

In symlink mode, the skill at `$HOME/.openclaw/skills/clawboard` is a symbolic link to the repository copy. This means any changes made in the repository are immediately visible to OpenClaw without additional steps.

### Copy Mode

In copy mode, the skill is copied to `$HOME/.openclaw/skills/clawboard`. Changes made in the repository won't affect OpenClaw until you explicitly sync them using:

```
cd "$CLAWBOARD_DIR"
bash scripts/sync_openclaw_skill.sh --to-openclaw --apply --force
```

To sync changes from OpenClaw back to the repository:

```
bash scripts/sync_openclaw_skill.sh --to-repo --apply
```

Workspace and Runtime Assumptions
---------------------------------

When working on Clawboard components, the skill assumes typical repository locations:

* `~/[agent_name]/clawboard`
* `~/[agent_name]/projects/clawboard`

The scripted installer auto-detects these conventions. For runtime validation, you can check:

```
docker compose ps
echo "$CLAWBOARD_WEB_HOT_RELOAD"
curl -s http://localhost:8010/api/health
```

Plugin Configuration
--------------------

The clawboard-logger plugin requires proper configuration for optimal operation:

* **baseUrl**: The Clawboard API endpoint
* **token**: Security token for authentication
* **enabled**: Whether the plugin is active
* **contextMode**: Options include auto, cheap, full, or patient
* **contextFallbackMode**: Fallback behavior when primary context retrieval fails
* **contextFetchTimeoutMs**: Timeout for context fetching operations

Validation and Troubleshooting
------------------------------

After installation, validate your setup by:

1. Checking that all Docker services are running: `docker compose ps`
2. Verifying the API is responsive: `curl -s http://localhost:8010/api/health`
3. Ensuring the skill is properly installed: `test -L ~/.openclaw/skills/clawboard`
4. Confirming the logger plugin is enabled and configured
5. Restarting OpenClaw gateway to ensure all changes take effect

If you encounter issues, check the Docker logs for each service, verify your environment variables, and ensure your security token is correctly configured.

Integration with OpenClaw
-------------------------

The Clawboard skill integrates deeply with OpenClaw by:

* Providing a user interface for managing OpenClaw operations
* Logging all interactions through the clawboard-logger plugin
* Enabling token-based authentication for secure operations
* Exposing OpenResponses endpoints for attachments and file handling
* Configuring the /api/config endpoint with appropriate title and integration level

This comprehensive integration ensures that Clawboard serves as a powerful companion tool for OpenClaw users, providing visibility, control, and enhanced functionality for managing AI operations.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/sirouk/ralphie/SKILL.md>
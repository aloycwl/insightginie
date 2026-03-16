---
layout: post
title: "Ollama Memory Embeddings: Configure OpenClaw for OpenAI-Compatible Embeddings"
date: 2026-03-08T16:45:34
categories: [24854]
original_url: https://insightginie.com/ollama-memory-embeddings-configure-openclaw-for-openai-compatible-embeddings
---

What This Skill Does
--------------------

The Ollama Memory Embeddings skill is designed to configure OpenClaw memory search to use Ollama as the embeddings server via its OpenAI-compatible /v1/embeddings endpoint. This skill focuses exclusively on embeddings and does not affect chat/completions routing.

Key Features
------------

* Installs the skill under ~/.openclaw/skills/ollama-memory-embeddings
* Verifies Ollama installation and reachability
* Provides interactive model selection with multiple embedding options
* Optionally imports existing local embedding GGUFs into Ollama
* Updates OpenClaw configuration surgically
* Performs post-write configuration sanity checks
* Optionally restarts the OpenClaw gateway
* Includes drift enforcement and auto-healing capabilities

Available Embedding Models
--------------------------

The skill offers several embedding model options:

* embeddinggemma (default) – Closest to OpenClaw built-in
* nomic-embed-text – Strong quality, efficient
* all-minilm – Smallest and fastest
* mxbai-embed-large – Highest quality, larger size

Installation Process
--------------------

To install the skill, run the following command:

```
~/.openclaw/skills/ollama-memory-embeddings/install.sh
```

You can also install directly from the repository:

```
bash skills/ollama-memory-embeddings/install.sh
```

### Non-Interactive Installation

For automated deployments, use the non-interactive mode:

```
~/.openclaw/skills/ollama-memory-embeddings/install.sh \
--non-interactive \
--model embeddinggemma \
--reindex-memory auto
```

### Bullproof Setup with Watchdog

For maximum reliability, install the watchdog for automatic drift correction:

```
~/.openclaw/skills/ollama-memory-embeddings/install.sh \
--non-interactive \
--model embeddinggemma \
--reindex-memory auto \
--install-watchdog \
--watchdog-interval 60
```

Configuration Updates
---------------------

The skill updates the OpenClaw configuration by modifying the agents.defaults.memorySearch section with the following settings:

* provider = “openai”
* model = <selected model>:latest
* remote.baseUrl = “http://127.0.0.1:11434/v1/”
* remote.apiKey = “ollama” (required by client, ignored by Ollama)

Verification
------------

After installation, verify the setup with:

```
~/.openclaw/skills/ollama-memory-embeddings/verify.sh
```

Use the –verbose flag to get detailed API response information in case of failures.

Drift Enforcement and Auto-Healing
----------------------------------

The skill includes tools for maintaining configuration integrity:

### Manual Drift Enforcement

```
~/.openclaw/skills/ollama-memory-embeddings/enforce.sh \
--model embeddinggemma \
--openclaw-config ~/.openclaw/openclaw.json
```

### Watchdog Installation

Install the watchdog for automatic drift correction on macOS:

```
~/.openclaw/skills/ollama-memory-embeddings/watchdog.sh \
--install-launchd \
--model embeddinggemma \
--interval-sec 60
```

GGUF Detection and Import
-------------------------

The installer automatically detects embedding GGUFs matching specific patterns in known cache directories, including:

* \*embeddinggemma\*.gguf
* \*nomic-embed\*.gguf
* \*all-minilm\*.gguf
* \*mxbai-embed\*.gguf

If you have other embedding GGUFs, you can import them manually using the ollama create command.

Important Notes
---------------

* This skill does not modify OpenClaw package code; it only updates user configuration
* A timestamped backup of the configuration is created before any changes
* If no local GGUF exists, the installer pulls the selected model from Ollama
* Model names are normalized with the :latest tag for consistent interaction
* If the embedding model changes, rebuilding existing memory vectors is recommended to avoid retrieval mismatches
* The installer reindexes memory only when the effective embedding fingerprint changes
* Config backups are created only when a write is needed
* Legacy schema fallback is supported for backward compatibility

Benefits of Using Ollama for Embeddings
---------------------------------------

Switching to Ollama for embeddings offers several advantages:

* Centralized model management and updates
* Potential performance improvements through optimized serving
* Simplified deployment across multiple OpenClaw instances
* Access to a wider range of embedding models
* Consistent embeddings across different applications using the same Ollama instance

Troubleshooting
---------------

If you encounter issues during installation or verification, check the following:

* Ensure Ollama is installed and running on your system
* Verify that the selected model is available in Ollama
* Check network connectivity if using remote models
* Review the verbose output from the verification script for specific error messages
* Check the OpenClaw logs for any configuration-related errors

Conclusion
----------

The Ollama Memory Embeddings skill provides a robust and flexible way to configure OpenClaw to use Ollama for embeddings. With its comprehensive feature set including model selection, GGUF import, drift enforcement, and auto-healing, it offers a production-ready solution for managing embeddings in OpenClaw environments.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/vidarbrekke/ollama-memory-embeddings/SKILL.md>
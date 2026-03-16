---
layout: post
title: 'Ollama Memory Embeddings: Configure OpenClaw for OpenAI-Compatible Embeddings'
date: '2026-03-08T08:45:34'
categories:
- ai
- openclaw
original_url: https://insightginie.com/ollama-memory-embeddings-configure-openclaw-for-openai-compatible-embeddings/
featured_image: /media/images/8160.jpg
---

<h2>What This Skill Does</h2>
<p>The Ollama Memory Embeddings skill is designed to configure OpenClaw memory search to use Ollama as the embeddings server via its OpenAI-compatible /v1/embeddings endpoint. This skill focuses exclusively on embeddings and does not affect chat/completions routing.</p>
<h2>Key Features</h2>
<ul>
<li>Installs the skill under ~/.openclaw/skills/ollama-memory-embeddings</li>
<li>Verifies Ollama installation and reachability</li>
<li>Provides interactive model selection with multiple embedding options</li>
<li>Optionally imports existing local embedding GGUFs into Ollama</li>
<li>Updates OpenClaw configuration surgically</li>
<li>Performs post-write configuration sanity checks</li>
<li>Optionally restarts the OpenClaw gateway</li>
<li>Includes drift enforcement and auto-healing capabilities</li>
</ul>
<h2>Available Embedding Models</h2>
<p>The skill offers several embedding model options:</p>
<ul>
<li>embeddinggemma (default) &#8211; Closest to OpenClaw built-in</li>
<li>nomic-embed-text &#8211; Strong quality, efficient</li>
<li>all-minilm &#8211; Smallest and fastest</li>
<li>mxbai-embed-large &#8211; Highest quality, larger size</li>
</ul>
<h2>Installation Process</h2>
<p>To install the skill, run the following command:</p>
<pre>~/.openclaw/skills/ollama-memory-embeddings/install.sh</pre>
<p>You can also install directly from the repository:</p>
<pre>bash skills/ollama-memory-embeddings/install.sh</pre>
<h3>Non-Interactive Installation</h3>
<p>For automated deployments, use the non-interactive mode:</p>
<pre>~/.openclaw/skills/ollama-memory-embeddings/install.sh \
--non-interactive \
--model embeddinggemma \
--reindex-memory auto</pre>
<h3>Bullproof Setup with Watchdog</h3>
<p>For maximum reliability, install the watchdog for automatic drift correction:</p>
<pre>~/.openclaw/skills/ollama-memory-embeddings/install.sh \
--non-interactive \
--model embeddinggemma \
--reindex-memory auto \
--install-watchdog \
--watchdog-interval 60</pre>
<h2>Configuration Updates</h2>
<p>The skill updates the OpenClaw configuration by modifying the agents.defaults.memorySearch section with the following settings:</p>
<ul>
<li>provider = &#8220;openai&#8221;</li>
<li>model = &lt;selected model&gt;:latest</li>
<li>remote.baseUrl = &#8220;http://127.0.0.1:11434/v1/&#8221;</li>
<li>remote.apiKey = &#8220;ollama&#8221; (required by client, ignored by Ollama)</li>
</ul>
<h2>Verification</h2>
<p>After installation, verify the setup with:</p>
<pre>~/.openclaw/skills/ollama-memory-embeddings/verify.sh</pre>
<p>Use the &#8211;verbose flag to get detailed API response information in case of failures.</p>
<h2>Drift Enforcement and Auto-Healing</h2>
<p>The skill includes tools for maintaining configuration integrity:</p>
<h3>Manual Drift Enforcement</h3>
<pre>~/.openclaw/skills/ollama-memory-embeddings/enforce.sh \
--model embeddinggemma \
--openclaw-config ~/.openclaw/openclaw.json</pre>
<h3>Watchdog Installation</h3>
<p>Install the watchdog for automatic drift correction on macOS:</p>
<pre>~/.openclaw/skills/ollama-memory-embeddings/watchdog.sh \
--install-launchd \
--model embeddinggemma \
--interval-sec 60</pre>
<h2>GGUF Detection and Import</h2>
<p>The installer automatically detects embedding GGUFs matching specific patterns in known cache directories, including:</p>
<ul>
<li>*embeddinggemma*.gguf</li>
<li>*nomic-embed*.gguf</li>
<li>*all-minilm*.gguf</li>
<li>*mxbai-embed*.gguf</li>
</ul>
<p>If you have other embedding GGUFs, you can import them manually using the ollama create command.</p>
<h2>Important Notes</h2>
<ul>
<li>This skill does not modify OpenClaw package code; it only updates user configuration</li>
<li>A timestamped backup of the configuration is created before any changes</li>
<li>If no local GGUF exists, the installer pulls the selected model from Ollama</li>
<li>Model names are normalized with the :latest tag for consistent interaction</li>
<li>If the embedding model changes, rebuilding existing memory vectors is recommended to avoid retrieval mismatches</li>
<li>The installer reindexes memory only when the effective embedding fingerprint changes</li>
<li>Config backups are created only when a write is needed</li>
<li>Legacy schema fallback is supported for backward compatibility</li>
</ul>
<h2>Benefits of Using Ollama for Embeddings</h2>
<p>Switching to Ollama for embeddings offers several advantages:</p>
<ul>
<li>Centralized model management and updates</li>
<li>Potential performance improvements through optimized serving</li>
<li>Simplified deployment across multiple OpenClaw instances</li>
<li>Access to a wider range of embedding models</li>
<li>Consistent embeddings across different applications using the same Ollama instance</li>
</ul>
<h2>Troubleshooting</h2>
<p>If you encounter issues during installation or verification, check the following:</p>
<ul>
<li>Ensure Ollama is installed and running on your system</li>
<li>Verify that the selected model is available in Ollama</li>
<li>Check network connectivity if using remote models</li>
<li>Review the verbose output from the verification script for specific error messages</li>
<li>Check the OpenClaw logs for any configuration-related errors</li>
</ul>
<h2>Conclusion</h2>
<p>The Ollama Memory Embeddings skill provides a robust and flexible way to configure OpenClaw to use Ollama for embeddings. With its comprehensive feature set including model selection, GGUF import, drift enforcement, and auto-healing, it offers a production-ready solution for managing embeddings in OpenClaw environments.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/vidarbrekke/ollama-memory-embeddings/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/vidarbrekke/ollama-memory-embeddings/SKILL.md</a></p>

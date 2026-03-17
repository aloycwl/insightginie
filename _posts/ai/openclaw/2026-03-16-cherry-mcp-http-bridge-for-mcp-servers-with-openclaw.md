---
layout: post
title: 'Cherry MCP: HTTP Bridge for MCP Servers with OpenClaw'
date: '2026-03-16T20:15:53+00:00'
categories:
- ai
- openclaw
original_url: https://insightginie.com/cherry-mcp-http-bridge-for-mcp-servers-with-openclaw/
featured_image: /media/images/8158.jpg
---

<p>Cherry MCP is an HTTP bridge designed to solve a critical problem when using MCP (Model Context Protocol) servers with OpenClaw agents. The bridge keeps MCP servers alive and exposes their functionality via REST endpoints, enabling seamless integration without native MCP support.</p>
<h2>Origin Story</h2>
<p>Cherry MCP was born during a late-night development session when trying to use MCP servers with OpenClaw. The fundamental issue was that MCP servers use stdio (standard input/output) communication, which means they die without a persistent client holding the connection. OpenClaw doesn&#8217;t natively support MCP servers, and running them via exec meant they would get killed after going quiet.</p>
<p>The solution was elegant: create a bridge that spawns MCP servers as child processes, keeps them alive with auto-restart capabilities, and exposes their tools via HTTP REST endpoints. The project was named after an emoji, reflecting its practical yet playful nature.</p>
<h2>Why Cherry MCP Exists</h2>
<p>MCP servers use stdio communication, which presents several challenges:</p>
<ul>
<li>Servers die without a persistent client holding the connection</li>
<li>OpenClaw doesn&#8217;t natively support MCP servers</li>
<li>Running MCP servers via exec results in termination after inactivity</li>
</ul>
<p>Cherry MCP addresses these issues by:</p>
<ul>
<li>Spawning MCP servers as child processes</li>
<li>Keeping them alive with auto-restart on crash</li>
<li>Exposing HTTP endpoints for each server</li>
</ul>
<h2>Quick Start Guide</h2>
<p>Getting started with Cherry MCP is straightforward:</p>
<pre><code># Add a server
node cli.js add-server github npx @anthropic/mcp-github

# Set environment variables for the server
node cli.js set-env github GITHUB_TOKEN ghp_xxx

# Start the bridge
pm2 start bridge.js --name cherry-mcp
</code></pre>
<h3>CLI Commands</h3>
<p>The CLI provides comprehensive management capabilities:</p>
<ul>
<li><strong>Servers</strong>: Add, remove, and list servers</li>
<li><strong>Environment variables</strong>: Configure server-specific settings</li>
<li><strong>Security</strong>: Set rate limiting and IP allowlists</li>
<li><strong>Audit logging</strong>: Enable request logging for monitoring</li>
</ul>
<h2>HTTP API Endpoints</h2>
<p>Cherry MCP exposes a RESTful API for interacting with MCP servers:</p>
<pre><code># List servers
curl http://localhost:3456/

# List tools for a specific server
curl http://localhost:3456/&lt;server&gt;/tools

# Call a tool
curl -X POST http://localhost:3456/&lt;server&gt;/call \
-H "Content-Type: application/json" \
-d '{"tool": "search", "arguments": {"query": "test"}}'

# Restart a server
curl -X POST http://localhost:3456/&lt;server&gt;/restart
</code></pre>
<h2>Security Features</h2>
<p>Cherry MCP includes several security measures by default:</p>
<ul>
<li>Binds to 127.0.0.1 only (not exposed to network)</li>
<li>Optional rate limiting to prevent abuse</li>
<li>Optional IP allowlist for access control</li>
<li>Optional audit logging for monitoring</li>
<li>1MB maximum payload size</li>
</ul>
<h2>Important Notes</h2>
<p>Several critical considerations when using Cherry MCP:</p>
<ol>
<li><strong>Command Control</strong>: The bridge executes commands specified in config.json only. It does not accept arbitrary commands via HTTP. You maintain complete control over what runs.</li>
<li><strong>Secrets Management</strong>: Environment variables set via set-env are saved in plain text in config.json. Add it to .gitignore or use environment variables instead.</li>
<li><strong>Shell Inheritance</strong>: The server inherits your shell environment, which can affect behavior and access.</li>
</ol>
<h2>Deployment Options</h2>
<p>Recommended deployment with PM2:</p>
<pre><code>pm2 start bridge.js --name cherry-mcp
pm2 save
pm2 startup
</code></pre>
<p>This setup provides process management, auto-restart capabilities, and system startup configuration.</p>
<h2>Technical Architecture</h2>
<p>Cherry MCP operates as a bridge between HTTP clients and MCP servers:</p>
<ol>
<li>HTTP requests arrive at the bridge</li>
<li>The bridge routes requests to the appropriate MCP server</li>
<li>Commands are executed via stdio communication</li>
<li>Results are returned via HTTP responses</li>
</ol>
<p>This architecture enables OpenClaw agents to leverage MCP tools without requiring native MCP support, effectively extending the capabilities of both systems.</p>
<h2>Use Cases</h2>
<p>Cherry MCP enables several powerful use cases:</p>
<ul>
<li>Integrating GitHub MCP tools with OpenClaw automation</li>
<li>Exposing MCP functionality to web applications</li>
<li>Creating REST APIs for MCP-based services</li>
<li>Building automated workflows that combine MCP tools with other systems</li>
</ul>
<h2>Future Development</h2>
<p>While Cherry MCP provides a solid foundation, potential enhancements could include:</p>
<ul>
<li>WebSocket support for real-time MCP communication</li>
<li>Enhanced authentication and authorization</li>
<li>Advanced monitoring and metrics</li>
<li>Support for additional MCP server types</li>
</ul>
<p>The project represents a practical solution to a real-world integration challenge, demonstrating how thoughtful engineering can bridge gaps between different protocol ecosystems.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/bitbrujo/cherry-mcp/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/bitbrujo/cherry-mcp/SKILL.md</a></p>

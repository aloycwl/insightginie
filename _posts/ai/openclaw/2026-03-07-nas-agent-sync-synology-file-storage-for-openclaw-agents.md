---
layout: post
title: "NAS Agent Sync \u2014 Synology File Storage for OpenClaw Agents"
date: '2026-03-07T05:16:32'
categories:
- ai
- openclaw
original_url: https://insightginie.com/nas-agent-sync-synology-file-storage-for-openclaw-agents/
featured_image: /media/images/8155.jpg
---

<h2>Introduction</h2>
<p>The NAS Agent Sync skill provides centralized file storage for OpenClaw multi-agent teams using Synology NAS or any SSH-accessible storage solution. This skill solves the common problem of scattered file storage across multiple agent workspaces by implementing a File Master pattern where one designated agent manages all file operations for the team.</p>
<h2>The Problem</h2>
<p>In multi-agent setups, each agent typically operates within its own workspace, generating files that need to be shared, backed up, or accessed by other agents. This creates several challenges:</p>
<ul>
<li>Files get lost between agent sessions</li>
<li>No centralized backup strategy exists</li>
<li>Agents duplicate work by recreating files</li>
<li>No single source of truth for important documents</li>
<li>Security risks when multiple agents need direct access to storage</li>
</ul>
<h2>The Solution</h2>
<p>The NAS Agent Sync skill implements a File Master pattern where one agent (typically the Tech Lead or a dedicated file management agent) acts as the central coordinator for all file operations. All other agents route their file requests through this File Master using the sessions_send mechanism, which maintains security while providing centralized storage.</p>
<h2>Architecture Overview</h2>
<p>The skill creates a simple but effective architecture where file operations flow through a designated File Master agent:</p>
<pre><code>┌──────────┐    sessions_send     ┌────────────┐     SSH      ┌─────────┐
│ Agent A  │ ──────────────────► │ FILE MASTER │ ──────────► │   NAS   │
│ (Finance)│ "store invoice.pdf" │ (Tech Lead) │             │         │
└──────────┘                     └────────────┘             └─────────┘
│
┌──────────┐    sessions_send          │  SSH
│ Agent B  │ ──────────────────►       │
│ (Sales)  │ "get sales report"        ▼
└──────────┘                     ┌─────────────┐
│ _agents/     │
│ ├── agent-a/ │
│ ├── agent-b/ │
│ ├── agent-c/ │
│ └── _shared/ │
└─────────────┘
</code></pre>
<h2>Setup Process</h2>
<h3>NAS Prerequisites</h3>
<p>Before configuring the skill, ensure you have:</p>
<ul>
<li>A Synology NAS (any model) or any Linux server with SSH access</li>
<li>SSH access configured with key-based authentication</li>
<li>A VPN or Tailnet connection for secure remote access (recommended)</li>
</ul>
<h3>Creating Folder Structure</h3>
<p>The skill requires a specific folder structure on your NAS. You can create this using SSH:</p>
<pre><code>SSH_HOST="user@your-nas-ip"
# Create agent folders (customize agent names to match your team)
ssh $SSH_HOST "mkdir -p ~/_agents/{coordinator,techops,finance,sales,marketing}"
# Create shared folders
ssh $SSH_HOST "mkdir -p ~/_shared/{config,templates}"
# Create agent directory file
ssh $SSH_HOST '
cat > ~/_shared/config/agent-directory.json &lt;&lt; EOF
{
  "agents": {
    "coordinator": { "role": "Coordinator", "path": "~/_agents/coordinator/" },
    "techops": { "role": "File Master", "path": "~/_agents/techops/" },
    "finance": { "role": "Finance", "path": "~/_agents/finance/" }
  },
  "shared": "~/_shared/",
  "basePath": "~/"
}
EOF
'
</code></pre>
<h3>Configuring the File Master Agent</h3>
<p>The File Master agent needs specific configuration in its AGENTS.md file to handle incoming file requests:</p>
<pre><code>## FILE MASTER — Incoming Requests
When another agent sends a file request via sessions_send:
### Store a file:
ssh USER@NAS-IP "mkdir -p ~/_agents/[agent]/[subfolder]/"
# Copy/create file there
### Retrieve a file:
ssh USER@NAS-IP "cat ~/_agents/[agent]/[file]"
# Send content back to requesting agent
### Confirm back:
sessions_send(sessionKey="agent:[requester]:main", message="Done! File at [path]")
</code></pre>
<h3>Configuring Other Agents</h3>
<p>All other agents must be configured to route file operations through the File Master:</p>
<pre><code>## File Operations → File Master
I do NOT access files directly. ALL file ops go through the File Master:
sessions_send(sessionKey="agent:techops:main", message="Store:[details]")
sessions_send(sessionKey="agent:techops:main", message="Retrieve:[path]")
</code></pre>
<h2>Recommended Folder Structure</h2>
<p>The skill recommends this organized folder structure for optimal file management:</p>
<pre><code>~/
├── _agents/
│   ├── coordinator/     # Coordinator files
│   │   ├── journal/     # Daily journals
│   │   └── tracking/    # Task tracking
│   ├── techops/         # Tech docs, scripts
│   │   ├── scripts/
│   │   └── configs/
│   ├── finance/         # Finance
│   │   ├── invoices/
│   │   ├── contracts/
│   │   └── reports/
│   ├── sales/           # Sales
│   │   ├── leads/
│   │   └── proposals/
│   └── [your-agent]/    # Per-agent storage
├── _shared/
│   ├── config/          # Shared configs
│   │   └── agent-directory.json
│   └── templates/       # Shared templates
└── _backups/
    └── memory/          # Memory file backups
</code></pre>
<h2>Security Considerations</h2>
<p>The NAS Agent Sync skill implements several security measures:</p>
<ul>
<li><strong>SSH key-based authentication</strong>: No passwords stored in configuration files</li>
<li><strong>VPN/Tailnet tunnel</strong>: Encrypted connection without port forwarding</li>
<li><strong>File Master pattern</strong>: Only one agent has NAS credentials</li>
<li><strong>Session-based communication</strong>: Other agents never get SSH credentials</li>
</ul>
<p>Important security practices:</p>
<ul>
<li>Never store SSH keys in agent SOUL.md or memory files</li>
<li>Use strong SSH key pairs with appropriate permissions</li>
<li>Regularly rotate SSH keys if compromised</li>
<li>Monitor access logs on your NAS for unusual activity</li>
</ul>
<h2>Backup Strategy</h2>
<p>The skill includes a comprehensive backup strategy using cron jobs:</p>
<h3>Daily Backup Cron</h3>
<p>Configure a cron job that backs up agent workspaces to NAS:</p>
<pre><code>// Cron job config
{
  "schedule": {
    "kind": "cron",
    "expr": "0 3 * * *",
    "tz": "UTC"
  },
  "payload": {
    "kind": "agentTurn",
    "message": "Backup all agent workspaces to NAS. For each agent: rsync workspace memory/ folder to NAS _agents/{agent}/memory-backup/. Report any failures."
  },
  "sessionTarget": "isolated"
}
</code></pre>
<h3>Manual Backup Commands</h3>
<p>You can also perform manual backups:</p>
<pre><code># Backup specific agent
rsync -avz ~/.openclaw/workspace-finance/memory/ user@nas-ip:~/_agents/finance/memory-backup/
# Backup all agents (customize list to your team)
for agent in coordinator techops finance sales marketing; do
  rsync -avz ~/.openclaw/workspace-$agent/memory/ user@nas-ip:~/_agents/$agent/memory-backup/
done
</code></pre>
<h2>Troubleshooting</h2>
<p>Common issues and solutions:</p>
<h3>SSH Connection Refused</h3>
<ul>
<li>Check VPN/Tailnet status — is NAS online and connected?</li>
<li>Verify SSH service running on NAS (Synology: DSM → Control Panel → Terminal &#038; SNMP)</li>
<li>Test connection: <code>ssh user@nas-ip</code></li>
</ul>
<h3>Permission Denied</h3>
<ul>
<li>SSH key not added: <code>ssh-copy-id user@nas-ip</code></li>
<li>NAS home folder not enabled (Synology: DSM → User → Advanced → Enable home service)</li>
<li>Check folder permissions on NAS</li>
</ul>
<h3>Slow Transfers</h3>
<ul>
<li>Use direct VPN connection (not relayed)</li>
<li>Consider compression: <code>rsync -avz --compress</code></li>
<li>Check network bandwidth and NAS performance</li>
</ul>
<h2>Compatible NAS Models</h2>
<p>The skill works with various NAS solutions:</p>
<ul>
<li>✅ Synology (any model with DSM 7+)</li>
<li>✅ QNAP (QTS 5+)</li>
<li>✅ TrueNAS / FreeNAS</li>
<li>✅ Any Linux server with SSH access</li>
<li>✅ Raspberry Pi with external storage</li>
</ul>
<h2>Changelog</h2>
<h3>v1.1.0</h3>
<ul>
<li>Removed all specific agent/setup references</li>
<li>Generalized folder structure and examples</li>
<li>Added backup strategy with cron</li>
</ul>
<h3>v1.0.0</h3>
<ul>
<li>Initial release</li>
</ul>
<h2>Conclusion</h2>
<p>The NAS Agent Sync skill provides a robust, secure solution for centralized file storage in OpenClaw multi-agent environments. By implementing the File Master pattern and leveraging SSH-accessible storage, teams can ensure consistent file management, reliable backups, and enhanced security across all agents.</p>
<p>The skill’s flexibility allows it to work with various NAS solutions while maintaining a simple, effective architecture that scales with your team’s needs. Whether you’re running a small team or a large organization, the NAS Agent Sync skill provides the foundation for organized, secure file management in your OpenClaw setup.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/neal-collab/nas-agent-sync/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/neal-collab/nas-agent-sync/SKILL.md</a></p>

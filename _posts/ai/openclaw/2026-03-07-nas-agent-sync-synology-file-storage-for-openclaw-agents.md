---
layout: post
title: "NAS Agent Sync — Synology File Storage for OpenClaw Agents"
date: 2026-03-07T05:16:32
categories: [24854]
original_url: https://insightginie.com/nas-agent-sync-synology-file-storage-for-openclaw-agents
---

Introduction
------------

The NAS Agent Sync skill provides centralized file storage for OpenClaw multi-agent teams using Synology NAS or any SSH-accessible storage solution. This skill solves the common problem of scattered file storage across multiple agent workspaces by implementing a File Master pattern where one designated agent manages all file operations for the team.

The Problem
-----------

In multi-agent setups, each agent typically operates within its own workspace, generating files that need to be shared, backed up, or accessed by other agents. This creates several challenges:

* Files get lost between agent sessions
* No centralized backup strategy exists
* Agents duplicate work by recreating files
* No single source of truth for important documents
* Security risks when multiple agents need direct access to storage

The Solution
------------

The NAS Agent Sync skill implements a File Master pattern where one agent (typically the Tech Lead or a dedicated file management agent) acts as the central coordinator for all file operations. All other agents route their file requests through this File Master using the sessions\_send mechanism, which maintains security while providing centralized storage.

Architecture Overview
---------------------

The skill creates a simple but effective architecture where file operations flow through a designated File Master agent:

```
┌──────────┐    sessions_send     ┌────────────┐     SSH      ┌─────────┐
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
```

Setup Process
-------------

### NAS Prerequisites

Before configuring the skill, ensure you have:

* A Synology NAS (any model) or any Linux server with SSH access
* SSH access configured with key-based authentication
* A VPN or Tailnet connection for secure remote access (recommended)

### Creating Folder Structure

The skill requires a specific folder structure on your NAS. You can create this using SSH:

```
SSH_HOST="user@your-nas-ip"
# Create agent folders (customize agent names to match your team)
ssh $SSH_HOST "mkdir -p ~/_agents/{coordinator,techops,finance,sales,marketing}"
# Create shared folders
ssh $SSH_HOST "mkdir -p ~/_shared/{config,templates}"
# Create agent directory file
ssh $SSH_HOST '
cat > ~/_shared/config/agent-directory.json << EOF
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
```

### Configuring the File Master Agent

The File Master agent needs specific configuration in its AGENTS.md file to handle incoming file requests:

```
## FILE MASTER — Incoming Requests
When another agent sends a file request via sessions_send:
### Store a file:
ssh USER@NAS-IP "mkdir -p ~/_agents/[agent]/[subfolder]/"
# Copy/create file there
### Retrieve a file:
ssh USER@NAS-IP "cat ~/_agents/[agent]/[file]"
# Send content back to requesting agent
### Confirm back:
sessions_send(sessionKey="agent:[requester]:main", message="Done! File at [path]")
```

### Configuring Other Agents

All other agents must be configured to route file operations through the File Master:

```
## File Operations → File Master
I do NOT access files directly. ALL file ops go through the File Master:
sessions_send(sessionKey="agent:techops:main", message="Store:[details]")
sessions_send(sessionKey="agent:techops:main", message="Retrieve:[path]")
```

Recommended Folder Structure
----------------------------

The skill recommends this organized folder structure for optimal file management:

```
~/
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
```

Security Considerations
-----------------------

The NAS Agent Sync skill implements several security measures:

* **SSH key-based authentication**: No passwords stored in configuration files
* **VPN/Tailnet tunnel**: Encrypted connection without port forwarding
* **File Master pattern**: Only one agent has NAS credentials
* **Session-based communication**: Other agents never get SSH credentials

Important security practices:

* Never store SSH keys in agent SOUL.md or memory files
* Use strong SSH key pairs with appropriate permissions
* Regularly rotate SSH keys if compromised
* Monitor access logs on your NAS for unusual activity

Backup Strategy
---------------

The skill includes a comprehensive backup strategy using cron jobs:

### Daily Backup Cron

Configure a cron job that backs up agent workspaces to NAS:

```
// Cron job config
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
```

### Manual Backup Commands

You can also perform manual backups:

```
# Backup specific agent
rsync -avz ~/.openclaw/workspace-finance/memory/ user@nas-ip:~/_agents/finance/memory-backup/
# Backup all agents (customize list to your team)
for agent in coordinator techops finance sales marketing; do
  rsync -avz ~/.openclaw/workspace-$agent/memory/ user@nas-ip:~/_agents/$agent/memory-backup/
done
```

Troubleshooting
---------------

Common issues and solutions:

### SSH Connection Refused

* Check VPN/Tailnet status — is NAS online and connected?
* Verify SSH service running on NAS (Synology: DSM → Control Panel → Terminal & SNMP)
* Test connection: `ssh user@nas-ip`

### Permission Denied

* SSH key not added: `ssh-copy-id user@nas-ip`
* NAS home folder not enabled (Synology: DSM → User → Advanced → Enable home service)
* Check folder permissions on NAS

### Slow Transfers

* Use direct VPN connection (not relayed)
* Consider compression: `rsync -avz --compress`
* Check network bandwidth and NAS performance

Compatible NAS Models
---------------------

The skill works with various NAS solutions:

* ✅ Synology (any model with DSM 7+)
* ✅ QNAP (QTS 5+)
* ✅ TrueNAS / FreeNAS
* ✅ Any Linux server with SSH access
* ✅ Raspberry Pi with external storage

Changelog
---------

### v1.1.0

* Removed all specific agent/setup references
* Generalized folder structure and examples
* Added backup strategy with cron

### v1.0.0

* Initial release

Conclusion
----------

The NAS Agent Sync skill provides a robust, secure solution for centralized file storage in OpenClaw multi-agent environments. By implementing the File Master pattern and leveraging SSH-accessible storage, teams can ensure consistent file management, reliable backups, and enhanced security across all agents.

The skill's flexibility allows it to work with various NAS solutions while maintaining a simple, effective architecture that scales with your team's needs. Whether you're running a small team or a large organization, the NAS Agent Sync skill provides the foundation for organized, secure file management in your OpenClaw setup.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/neal-collab/nas-agent-sync/SKILL.md>
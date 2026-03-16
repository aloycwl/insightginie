---
layout: post
title: "Nostr Identity Setup and Health-Check CLI: A Comprehensive Guide"
date: 2026-03-14T11:17:14
categories: [24854]
original_url: https://insightginie.com/nostr-identity-setup-and-health-check-cli-a-comprehensive-guide
---

What is nihao?
--------------

nihao is a Nostr identity setup and health-check CLI that creates a complete Nostr identity (keypair, profile, relay list, lightning address, Cashu wallet) in one command. It audits existing npub health with a 0–8 score and is distributed as a single Go binary that’s non-interactive and agent-friendly.

Core Capabilities
-----------------

This skill installs a single Go binary (nihao) that:

* Generates Nostr keypairs using random Ed25519 key generation via crypto/rand
* Publishes events including kind 0 (profile), kind 3 (follows), kind 1 (note), kind 10002 (relay list), kind 10050 (DM relays), kind 17375 (wallet), and kind 10019 (nutzap info)
* Makes HTTP requests for NIP-05 verification, LNURL resolution, Cashu mint validation, relay NIP-11 probes, and image HEAD checks
* Connects to Nostr relays via WebSocket connections to publish and query events

It does **not** store keys on disk by default, run as a daemon or background process, access local files beyond the binary itself, or require any accounts, API keys, or KYC.

Installation
------------

nihao is distributed as source code compiled locally via Go’s standard toolchain. No pre-built binaries are downloaded — the code is fetched from GitHub, compiled on your machine, and placed in your $GOPATH/bin.

```
go install github.com/dergigi/nihao@latest
nihao version
```

On Install: Identity Creation Process
-------------------------------------

When an agent installs this skill, it follows these steps:

1. **Install Binary**: go install github.com/dergigi/nihao@latest
2. **Create Identity**: nihao –name “AGENT\_NAME” –about “AGENT\_BIO” –nsec-file ./nsec.key –json –quiet
3. **Report to User**: Provides npub, lightning address (default: npub@npub.cash), and reminds to back up the nsec
4. **(Optional) Follow Owner**: If user provides their npub, agent should follow them using nak or another tool

Setup: Creating a New Identity
------------------------------

```
nihao --name "AgentName" --about "I do things" --json
```

This generates a keypair, publishes profile metadata (kind 0), publishes relay list (kind 10002) with NIP-65 read/write markers, publishes DM relay list (kind 10050) per NIP-17, publishes follow list (kind 3), sets up a NIP-60 Cashu wallet (kind 17375 + kind 10019), sets lightning address to npub@npub.cash, and posts a first note with #nihao hashtag.

### Setup Flags

The tool provides comprehensive flags for customization:

* `--name <name>`: Display name (default: “nihao-user”)
* `--about <text>`: Bio
* `--picture <url>`: Profile picture URL
* `--banner <url>`: Banner image URL
* `--nip05 <user@domain>`: NIP-05 identifier
* `--lud16 <user@domain>`: Lightning address (default: npub@npub.cash)
* `--relays <r1,r2,...>`: Override default relay list
* `--discover`: Discover relays from well-connected npubs
* `--dm-relays <r1,r2,...>`: Override DM relay list
* `--no-dm-relays`: Skip DM relay list publishing
* `--mint <url>`: Custom Cashu mint (repeatable)
* `--no-wallet`: Skip wallet setup
* `--sec, --nsec <nsec|hex>`: Use existing secret key
* `--stdin`: Read secret key from stdin
* `--nsec-file <path>`: Write nsec to file (0600 perms) for secure storage
* `--nsec-cmd <command>`: Pipe nsec to shell command
* `--json`: JSON output for parsing
* `--quiet, -q`: Suppress non-JSON, non-error output

Key Management Best Practices
-----------------------------

nihao never writes keys to disk by default. Secret keys are handled securely through several methods:

* `--nsec-file <path>`: Writes nsec to a file with 0600 permissions (recommended for automation)
* `--nsec-cmd <command>`: Pipes nsec to a command’s stdin (e.g., a password manager), never as a CLI argument
* `--stdin`: Reads an existing key from stdin, avoiding shell history and process list exposure
* `--json` output: Includes nsec in structured output for programmatic parsing

⚠️ Avoid passing raw nsec values as CLI arguments (e.g., `--sec nsec1...`) in shared environments, as arguments are visible in process listings. Prefer `--stdin` or `--nsec-cmd` instead.

Check: Auditing Existing Identities
-----------------------------------

```
nihao check npub1... --json
```

Checks and scores (0–8) include:

* **profile**: Kind 0 completeness (name, display\_name, about, picture, banner)
* **nip05**: NIP-05 live HTTP verification, root domain detection
* **picture**: Image reachability, Blossom hosting detection, file size
* **banner**: Same as picture
* **lud16**: Lightning address LNURL resolution
* **relay\_list**: Kind 10002 presence, relay count
* **relay\_markers**: NIP-65 read/write marker analysis
* **relay\_quality**: Per-relay latency, NIP-11 support, reachability
* **dm\_relays**: Kind 10050 DM relay list (NIP-17)
* **follow\_list**: Kind 3 follow count
* **nip60\_wallet**: Kind 17375/37375 wallet presence
* **nutzap\_info**: Kind 10019 nutzap configuration
* **wallet\_mints**: Cashu mint reachability and validation

### Check Flags

* `--json`: Structured JSON output
* `--quiet, -q`: Suppress non-JSON output
* `--relays <r1,r2,...>`: Query these relays instead of defaults

### Exit Codes

* **0**: All checks pass (score = max)
* **1**: One or more checks fail

Backup: Exporting Identity Events
---------------------------------

```
nihao backup <npub|nip05> > identity.json
```

Exports all identity-related events as JSON: kind 0 (profile), kind 3 (follows), kind 10002 (relay list), kind 10050 (DM relays), kind 10019 (nutzap info), kind 17375/37375 (wallet). JSON goes to stdout, progress to stderr. Use for snapshots, migration, or archival.

### Backup Flags

* `--quiet, -q`: Suppress progress output (JSON always goes to stdout)
* `--relays <r1,r2,...>`: Query these relays instead of defaults

JSON Output Examples
--------------------

### Setup Output

```
{
  "npub": "npub1...",
  "nsec": "nsec1...",
  "pubkey": "hex...",
  "relays": ["wss://..."],
  "profile": {
    "name": "...",
    "lud16": "..."
  },
  "wallet": {
    "p2pk_pubkey": "02...",
    "mints": ["https://..."]
  }
}
```

### Check Output

```
{
  "npub": "npub1...",
  "pubkey": "hex...",
  "score": 6,
  "max_score": 8,
  "checks": [
    {
      "name": "profile",
      "status": "pass",
      "detail": "..."
    },
    {
      "name": "nip05",
      "status": "fail",
      "detail": "not set"
    }
  ]
}
```

Integration and Quick Reference
-------------------------------

After setup, store for quick reference:

```
## Nostr Identity
- npub: npub1...
- Lightning: npub1...@npub.cash
- Relays: relay.damus.io, relay.primal.net
```

This comprehensive tool provides everything needed for Nostr identity management, from initial setup to ongoing health monitoring, all while maintaining strong security practices for key management and providing detailed audit capabilities through its scoring system.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/dergigi/nihao/SKILL.md>
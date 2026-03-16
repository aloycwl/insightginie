---
layout: post
title: "Understanding SkillGuard: Your OpenClaw Security Scanner"
date: 2026-03-16T02:46:28
categories: [24854]
original_url: https://insightginie.com/understanding-skillguard-your-openclaw-security-scanner
---

To maintain the integrity and safety of your OpenClaw ecosystem, [SkillGuard](https://github.com/openclaw/skills/tree/main/skills/benlee2144/benlee-skillguard) acts as an advanced security scanner designed to audit all installed skills for potential threats. Whether you’re a beginner or an experienced user, understanding what SkillGuard does and how it enhances your security posture is crucial.

Introduction to SkillGuard
--------------------------

SkillGuard is a comprehensive audit tool specifically tailored for OpenClaw skills. It meticulously scans and analyses your skills for signs of malicious activity, unauthorized actions, and potential vulnerabilities. Its main objective is to ensure that every skill operating in your system adheres to security best practices and doesn’t compromise your data or system.

SkillGuard’s Command Structure
------------------------------

SkillGuard’s robust functionalities can be accessed via simple commands. Here’s a breakdown of the primary commands and their usage:

### `scan` Command

The `scan` command audits all skills in the default directory (`~/clawd/skills/`) or a specified custom directory, providing a detailed analysis of each skill’s security posture. Example usage:

* `python3 ~/clawd/skills/skill-guard/scripts/skillguard.py scan`
* `python3 ~/clawd/skills/skill-guard/scripts/skillguard.py scan --json`
* `python3 ~/clawd/skills/skill-guard/scripts/skillguard.py scan --report report.md`
* `python3 ~/clawd/skills/skill-guard/scripts/skillguard.py scan --baseline`

### `check` Command

The `check` command conducts a security scan on a single specified skill directory, allowing you to target specific areas of concern.

* `python3 ~/clawd/skills/skill-guard/scripts/skillguard.py check ~/clawd/skills/some-skill`
* `python3 ~/clawd/skills/skill-guard/scripts/skillguard.py check ~/clawd/skills/skill-guard/tests/`

### `watch` Command

This command delivers a concise summary suitable for alerting purposes, such as in cron jobs, ensuring you are promptly notified of new threats.

* `python3 ~/clawd/skills/skill-guard/scripts/skillguard.py watch`

### Output Formats

SkillGuard’s results are delivered in practical and easy-to-understand formats:  
– **SkillGuard:** Details the total number of skills scanned, the breakdown of clean, suspicious, and malicious findings  
– **ALERT:** Provides immediate notification if any suspicious changes since the last baseline or if a skill has been flagged as malicious

Advanced Capabilities
---------------------

SkillGuard is equipped with several advanced features that set it apart from standard security scanners. These capabilities ensure that no malicious activity goes unnoticed, and potential vulnerabilities are flagged before they can cause harm.

### Code Analysis

SkillGuard’s code analysis goes beyond basic pattern matching. It dissects the code for dangerous functions, suspicious payloads, and potential threats:

* **Eval/Exec Calls:** Detects and flags potentially harmful eval and exec calls
* **Shell Injection:** Identifies suspicious strings that may indicate injection attempts
* **Outbound HTTP Requests:** Checks for unauthorized HTTP requests that could exfiltrate data
* **Base64-Encoded Payloads:** Decodes Base64-encoded content to inspect for hidden threats
* **Hex-Encoded Suspicious Strings:** Performs specialized searches for encoded malicious payloads
* **Minified/Obfuscated Javascript:** Analyzes code accounting for common obfuscation tactics
* Detects time-bomb patterns, where malicious code is set to activate after a specific date

### Domain Analysis

SkillGuard maintains an allowlist of over 80 legitimate API domains, enhancing its ability to assess risk based on network activity. This feature ensures that only trusted third-party integrations are permitted:

* HTTP requests to known, legitimate APIs carry no risk points
* HTTP requests to unregistered domains are flagged and scored as WARNING with a penalty of 10 points
* **Context-Aware Analysis:** Different scores are applied based on the context of the HTTP request, ensuring relevancy and accuracy in assessments

### Sensitive File Access

To protect sensitive data, SkillGuard monitors access to critical and sensitive files that could compromise your security:

* Detects unauthorized access to SSH keys, AWS credentials, and GPG keyrings
* Monitors browser credential stores, including those from Chrome, Firefox, and Safari
* Checks for interactions with crypto wallets like MetaMask, Phantom, Solana, and Ethereum
* Flags any unauthorized access to keychain or keyring stores
* Identifies code attempting to harvest environment variables

### Prompt Injection

SkillGuard proactive detects manipulation attempts through prompt injection:

* Flows through HTML comments that may override standard inputs
* Examines documentation for data exfiltration instructions
* Identifies social engineering phrases meant to deceive users
* Detects instructions targeting modifications of other skills or system files

### Supply Chain Detection

To ensure the integrity of dependent libraries and packages, SkillGuard incorporates thorough supply chain detection mechanisms:

* Detects typosquatting by applying Levenshtein distance calculations on package names
* Identifies suspicious npm post-install scripts that might execute malicious code upon package installation
* Checks against lists of known malicious packages to prevent accidental inclusion

### Enhanced Detection (v2 Updates)

SkillGuard v2 has introduced several key enhancements that further fortify security assessments:

* **File Permissions:** Detects non-standard executable bit flags for non-executable files (e.g., .py, .js, and .md files)
* **Binary Detection:** Identifies potential threats in ELF, Mach-O, and PE binaries found within skill directories
* **Hardcoded Secrets:** Flags hardcoded sensitive information, such as AWS keys (AKIA…), GitHub tokens (ghp\_…), OpenAI keys (sk-…), Stripe keys, and private key files
* **Write Outside Path:** Catches code attempting to write files outside its designated skill directory
* **Unicode Homoglyphs:** Detects lookalike characters in filenames to prevent deception, identifying Cyrillic characters, for example, that mimic Latin letters
* **Excessive File Count:** Flags skills with an unusually high number of files (e.g., 50+ files)
* **Large Files:** Identifies abnormally large files (e.g., over 500KB) that may contain hidden malicious payloads
* **Network Threats:** Detects hardcoded IP addresses, reverse shells, and DNS exfiltration techniques
* **WebSockets:** Monitors for unauthorized WebSocket connections to external hosts

### Persistence Detection

[SkillGuard’s](https://github.com/openclaw/skills/tree/main/skills/benlee2144/benlee-skillguard) v2 makes persistence detection more robust by addressing potential long-term threats:

* Checks for unauthorized modifications to crontab entries
* Identifies the creation of suspicious launchd or systemd services
* Flags alterations made to shell resource configuration files, such as .bashrc and .zshrc

### Tamper Detection (v2 Updates)

With tamper detection, SkillGuard v2 introduces additional layers of security:

* Computes SHA-256 hashes for every file at the first scan to establish a baseline
* Stores these baselines in `baselines.json` for future reference
* With subsequent scans, SkillGuard compares file hashes to detect changes, additions, or removals
* Verifies version origin through `.clawhub/origin.json` to ensure the integrity of installed skills

Scoring Mechanism
-----------------

SkillGuard employs a points-based scoring system to assess the risk level of each flagged issue. Different patterns are assigned specific point values, providing a clear indication of a skill’s potential danger. Here are some risk levels and their corresponding point triggers:

| Pattern | Points |
| --- | --- |
| HTTP to known API | 0 |
| HTTP to unknown domain | 10 |
| `curl` in documentation | 0 |
| `subprocess` call | 2 |
| `subprocess` + `shell=True` | 25 |
| Sensitive file access | 10-25 |
| Prompt Injection Phrase | 25 |
| Reverse shell | **Auto `MALICIOUS`** |
| Sensitive access + outbound | **Auto `MALICIOUS`** |
| Typosquatted package | 15 |
| JS in SVG | 25 |

These points translate into three distinct risk levels:

| Risk Level | Risk Indicators | Score |
| --- | --- | --- |
| ✅ CLEAN | Compliant and secure | 0-15 Points |
| ⚠️ SUSPICIOUS | Require further investigation | 16-40 Points |
| 🔴 MALICIOUS | Immediate action required | 41+ Points OR *Dangerous Combo Detected* |

Recommendations Engine
----------------------

Alongside its scoring mechanism, [SkillGuard v2](https://github.com/openclaw/skills/tree/main/skills/benlee2144/benlee-skillguard) offers an integrated recommendations engine. For each identified issue, it provides actionable and clear recommendations, explaining the risk and suggesting proactive steps to mitigate or resolve the potential threat.

Test Suite: Real-World Validation
---------------------------------

SkillGuard’s reliability is corroborated by an extensive test suite containing seven deliberately crafted malicious skills. These test skills cover a range of attack vectors to validate the scanner’s effectiveness:

* **fake-weather:** Simulates SSH key theft and unauthorized POST requests to a fake domain
* **fake-formatter:** Incorporates a Base64-encoded reverse shell
* **fake-helper:** Tests prompt injection and social engineering defenses
* **fake-crypto:** Mimics wallet theft and command-and-control (C2) communication
* **fake-typosquat:** Uses deliberately misspelled package names to evade detection
* **fake-timebomb:** Simulates a date-activated exfiltration of SSH keys
* **fake-svgmalware:** Embeds JavaScript in an SVG file to test detection of unconventional attack vectors

All seven malicious test skills are classified as **🔴 MALICIOUS** by SkillGuard, demonstrating its robust efficacy in detecting a variety of sophisticated threats.

System Requirements
-------------------

SkillGuard is designed for simplicity and ease of use. It requires only the Python 3 standard library and operates as a single script:

* `scripts/skillguard.py`

This minimalistic approach ensures fast deployment and compatibility across a wide range of environments.

Conclusion
----------

Maintaining the integrity and safety of your OpenClaw ecosystem is of paramount importance. Tools like SkillGuard equip you with the capabilities to proactively scan, identify, and mitigate potential risks. By leveraging advanced features such as code analysis, domain whitelisting, sensitive file access detection, and thorough supply chain inspection, SkillGuard ensures that no angle of attack is left unchecked.

The recommended practices of using SkillGuard’s `scan`, `check`, and `watch` commands provide a comprehensive framework for consistent security audits. Moreover, its intuitive risk-based scoring system and the insights provided by the recommendations engine empower users to take informed actions when handling potential vulnerabilities.

Be proactive and enhance your system’s resilience by integrating [SkillGuard](https://github.com/openclaw/skills/tree/main/skills/benlee2144/benlee-skillguard) into your OpenClaw security protocols. Continually scanning your skills with SkillGuard ensures ongoing protection, peace of mind, and unwavering confidence in the integrity of your OpenClaw environment.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/benlee2144/benlee-skillguard/SKILL.md>
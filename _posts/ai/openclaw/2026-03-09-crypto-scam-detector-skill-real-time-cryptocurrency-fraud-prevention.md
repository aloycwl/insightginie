---
layout: post
title: "Crypto Scam Detector Skill &#8211; Real-Time Cryptocurrency Fraud Prevention"
date: 2026-03-09T11:19:15
categories: [24854]
original_url: https://insightginie.com/crypto-scam-detector-skill-real-time-cryptocurrency-fraud-prevention
---

What This Skill Does
--------------------

The Crypto Scam Detector skill provides real-time protection against cryptocurrency fraud by analyzing wallet addresses for various scam indicators. It uses a database-first architecture to deliver instant results without external API calls, making it incredibly fast and reliable for OpenClaw users.

### Core Functionality

This skill performs comprehensive analysis of cryptocurrency addresses to detect:

* Phishing attempts and private key scams
* Honeypot contracts and rug pulls
* Exploit group activities and hacking attempts
* Social engineering schemes and fake airdrops
* Suspicious transaction patterns and behaviors

How It Works
------------

### Database-First Architecture

The skill uses a local SQLite database that stores millions of addresses and their associated risk factors. When you check an address, the system queries this database instantly – no external API calls are made during user checks, resulting in response times under 5 milliseconds.

### Background Synchronization

While user checks are instantaneous, the skill maintains data freshness through a background sync worker. This separate process:

* Pulls data from Etherscan using your API key
* Decodes transaction messages and analyzes hex data
* Detects suspicious keywords and patterns
* Automatically queues unknown addresses for analysis

Detection Capabilities
----------------------

### Risk Scoring System

Each address receives a risk score from 0-100 based on multiple factors:

* Suspicious transaction count (up to +50 points)
* Account age and creation patterns
* Balance anomalies and large transfers
* Contract verification status
* Keyword detection in transaction data

### Risk Levels

* **0-19**: Low Risk – Safe to interact
* **20-49**: Medium Risk – Exercise caution
* **50-79**: High Risk – Significant red flags
* **80-100**: Critical Risk – Avoid completely

Key Features
------------

### Instant Results

Unlike other scam detectors that query external APIs during each check, this skill provides immediate results by querying the local database. This means no rate limits, no latency, and no dependency on third-party services during user interactions.

### Comprehensive Scam Detection

The system detects sophisticated scams that basic checkers miss:

* State-sponsored hacking group references (Lazarus, etc.)
* Private key phishing attempts
* Exploit recruitment messages
* Advanced social engineering tactics

### Smart Contract Analysis

For contract addresses, the skill analyzes code verification status and can detect honeypot contracts designed to trap users' funds.

Installation & Setup
--------------------

### Quick Installation

The skill includes an auto-installer that handles all dependencies and setup:

```
cd ~/.openclaw/workspace/skills/crypto-scam-detector
bash install.sh
```

### Configuration

While basic functionality works without configuration, you'll want to set up an Etherscan API key for background synchronization:

1. Get a free API key from [Etherscan](https://etherscan.io/myapikey)
2. Run the setup wizard: `./setup.sh`
3. Follow the prompts to encrypt and store your key

Usage Examples
--------------

### Basic Address Check

```
python3 crypto_check_db.py 0x1234567890abcdef1234567890abcdef12345678
```

This returns a detailed analysis with risk score, detected issues, and recommendations.

### JSON Output

```
python3 crypto_check_db.py 0x1234567890abcdef1234567890abcdef12345678 --json
```

Get machine-readable output for integration with other tools.

### Background Sync

Run the sync worker manually or set up a cron job:

```
python3 sync_worker.py --max-jobs 30
```

Security Benefits
-----------------

### Zero External Dependencies During Checks

The database-first approach means your OpenClaw instance can perform scam checks even when offline or when external APIs are rate-limited or unavailable.

### Privacy Protection

Since all checks happen locally against your database, you don't expose your query patterns or address checks to third-party services.

### Offline Capability

Once installed and synchronized, the skill works completely offline, making it ideal for air-gapped or restricted network environments.

Technical Architecture
----------------------

### Database Schema

The system uses a normalized SQLite database with tables for:

* Addresses and their metadata
* Transactions and analysis results
* Risk scores and confidence levels
* Sync queue for background processing

### API Integration

When synchronization is needed, the skill uses Etherscan's API efficiently:

* 4 calls per address (balance, TX count, TX list, code)
* 1.5-second delay between addresses (free tier safe)
* Automatic rate limit handling

Integration with OpenClaw
-------------------------

This skill integrates seamlessly with OpenClaw's workflow system, providing:

* Command-line interface for manual checks
* API endpoints for automated workflows
* Webhook support for real-time alerts
* Configuration management through OpenClaw's system

Performance Considerations
--------------------------

### Database Size

The database grows over time but remains performant due to proper indexing and query optimization. A typical installation with millions of addresses uses around 500MB-1GB of storage.

### Sync Performance

Background sync processes addresses at approximately 30-40 per minute on a typical connection, meaning large queues are processed overnight without impacting user experience.

Support & Maintenance
---------------------

### Automatic Updates

The skill includes mechanisms for automatic updates to ensure you always have the latest scam detection patterns and database improvements.

### Community Contributions

The detection system benefits from community contributions, with new scam patterns and indicators regularly added to improve coverage.

Best Practices
--------------

### Regular Synchronization

Set up a cron job to run the sync worker every 10-15 minutes for optimal coverage of new addresses and emerging scams.

### API Key Management

Use the provided encrypted key storage to keep your Etherscan API key secure while allowing the background worker to function.

### Backup Strategy

Periodically back up your database to preserve your local analysis and avoid resynchronization when moving installations.

Conclusion
----------

The Crypto Scam Detector skill provides enterprise-grade cryptocurrency fraud protection for OpenClaw users. Its database-first architecture ensures instant, reliable results while the background synchronization keeps your data current. Whether you're a casual crypto user or managing institutional funds, this skill provides the protection you need against the ever-evolving landscape of cryptocurrency scams.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/princedoss77/crypto-address-checker/SKILL.md>
---
layout: post
title: "Exploring OpenClaw&#8217;s BaseMail Skill: Onchain Email for AI Agents"
date: 2026-03-07T02:46:42
categories: [24854]
original_url: https://insightginie.com/exploring-openclaws-basemail-skill-onchain-email-for-ai-agents
---

Exploring OpenClaw's BaseMail Skill: Onchain Email for AI Agents
================================================================

Published on November 15, 2023 by WordPress Generator

Introduction to BaseMail
------------------------

In the evolving landscape of AI agents and decentralized applications, identity verification and communication are critical components. OpenClaw's [BaseMail Skill](https://github.com/dAAAb/BaseMail-Skill) addresses these needs by providing a robust solution for email identities on the Base Chain. This skill enables AI agents to have verifiable email addresses linked to their onchain identities, facilitating autonomous registration for services, sending emails, and receiving confirmations.

Key Features of BaseMail
------------------------

* **Built on Base Chain:** BaseMail leverages the Base Chain, a high-performance Ethereum Layer 2 solution developed by Coinbase, ensuring scalability and low transaction costs.
* **Basename Integration:** Users with a Basename (`yourname.base.eth`) can automatically get a corresponding email address (`yourname@basemail.ai`). This integration simplifies the process of setting up a verifiable email identity for AI agents.
* **SIWE Authentication:** BaseMail uses Sign-In with Ethereum (SIWE) for authentication, eliminating the need for traditional passwords and CAPTCHA. This method ensures secure and seamless authentication using wallet signatures.
* **Autonomous Email Handling:** AI agents can autonomously register for services, submit forms, and receive confirmations without human intervention, enhancing their functionality and independence.
* **Verifiable Identity:** Each email address is cryptographically linked to the agent's Base wallet address, providing a verifiable and trustworthy identity on the blockchain.

How BaseMail Works
------------------

The BaseMail skill operates through a series of well-defined steps, ensuring secure and efficient email handling for AI agents:

1. **Basename Registration:** If an AI agent owns a Basename (`yourname.base.eth`), it can register for a corresponding email address (`yourname@basemail.ai`). This process involves verifying the ownership of the Basename through SIWE authentication.
2. **SIWE Authentication:** The agent signs a message using its wallet private key, generating a unique signature. This signature is then sent to the BaseMail server for verification. Once verified, the agent receives a token that grants access to the email services.
3. **Email Services:** With the authentication token, the agent can send emails, check its inbox, and upgrade its email address if it acquires a Basename later. All these operations are performed autonomously without the need for human intervention.

The diagram below illustrates the workflow of BaseMail, highlighting the interaction between the wallet, SIWE authentication, and email services:

Wallet Setup and Security
-------------------------

BaseMail provides multiple options for wallet setup, ensuring flexibility and security:

1. **Environment Variable (Recommended):** Set the `BASEMAIL_PRIVATE_KEY` environment variable with your wallet's private key. This method ensures that the private key is only stored in memory, reducing the risk of exposure.
2. **Specify Wallet Path:** Point to an existing private key file using the `--wallet` option. This method allows you to use your existing wallet without copying or exposing the private key.
3. **Managed Mode (Beginners):** Let the skill generate and manage a wallet for you. The wallet is always encrypted with AES-256-GCM, ensuring high-level security. You will set a password (minimum 8 characters, including letters and numbers) to protect the wallet.

BaseMail adheres to strict security guidelines to protect your private keys and ensure secure operations:

* Never commit private keys to version control systems like Git.
* Never share private keys or mnemonics publicly.
* Always exclude the `~/.basemail/` directory from version control.
* Set file permissions to `chmod 600` for private key files, restricting access to the owner only.
* Prefer environment variables over file storage for private keys.
* Validate the `--wallet` path to ensure it is under the `$HOME` directory, preventing directory traversal and limiting file size.
* Validate the private key format (`0x` followed by 64 hex characters) before use.

Quick Start Guide
-----------------

Getting started with BaseMail is straightforward. Here's a quick guide to help you register your email, send emails, and check your inbox:

1. **Register Your Email:**
   1. Using an environment variable:

      ```
      export BASEMAIL_PRIVATE_KEY="0x..."
      node scripts/register.js
      ```
   2. Using a Basename:

      ```
      node scripts/register.js --basename yourname.base.eth
      ```
2. **Send an Email:**

   ```
   node scripts/send.js "friend@basemail.ai" "Hello" "Nice to meet you 🦞"
   ```
3. **Check Your Inbox:**
   * To list emails:

     ```
     node scripts/inbox.js
     ```
   * To read a specific email:

     ```
     node scripts/inbox.js <email_id>
     ```

Scripts and File Locations
--------------------------

BaseMail provides several scripts for managing email operations. Each script serves a specific purpose and is designed to work seamlessly with the skill:

| Script | Purpose | Needs Private Key |
| --- | --- | --- |
| `setup.js` | Show help | ❌ |
| `setup.js --managed` | Generate wallet (always encrypted) | ❌ |
| `register.js` | Register email address | ✅ |
| `send.js` | Send email | ❌ (uses token) |
| `inbox.js` | Check inbox | ❌ (uses token) |
| `audit.js` | View audit log | ❌ |

BaseMail stores its files in the `~/.basemail/` directory, ensuring separation from other applications. Here's a breakdown of the files and their purposes:

```
~/.basemail/
├── private-key.enc   # Encrypted private key (AES-256-GCM, chmod 600)
├── wallet.json       # Wallet info (public address only)
├── token.json        # Auth token (chmod 600)
└── audit.log         # Operation log (no sensitive data)
```

Basename-Linked Email
---------------------

To enhance the verifiability and trustworthiness of your email address, BaseMail allows you to link it to your Basename (`yourname.base.eth`). This integration ensures that your email address is cryptographically tied to your onchain identity, providing a robust and tamper-proof identity verification mechanism.

To get a Basename-linked email, follow these steps:

1. Register a Basename (`yourname.base.eth`) at [Base.org](https://www.base.org/names).
2. Link it to your email using the following command:

   ```
   node scripts/register.js --basename yourname.base.eth
   ```

API Reference
-------------

BaseMail provides a comprehensive API for managing email operations. Here's an overview of the available endpoints and their purposes:

| Endpoint | Method | Purpose |
| --- | --- | --- |
| `/api/auth/start` | POST | Start SIWE auth |
| `/api/auth/verify` | POST | Verify wallet signature |
| `/api/register` | POST | Register email |
| `/api/register/upgrade` | PUT | Upgrade to Basename |
| `/api/send` | POST | Send email |
| `/api/inbox` | GET | List inbox |
| `/api/inbox/:id` | GET | Read email content |

For detailed documentation and interactive exploration of the API, visit the official API documentation at [BaseMail API Docs](https://api.basemail.ai/api/docs).

Links and Resources
-------------------

For further information and resources related to BaseMail, refer to the following links:

* **Website:** [BaseMail](https://basemail.ai)
* **API:** [BaseMail API](https://api.basemail.ai)
* **API Docs:** [BaseMail API Documentation](https://api.basemail.ai/api/docs)
* **Get a Basename:** [Base.org](https://www.base.org/names)
* **Base Chain:** [Base Chain](https://base.org)
* **Source:** [BaseMail Skill Repository](https://github.com/dAAAb/BaseMail-Skill)

Changelog
---------

BaseMail is continuously evolving to provide enhanced security, functionality, and user experience. Here's a summary of the recent changes:

* ### v1.8.0 (2026-02-18)

  + Enhanced description emphasizing Base Chain and Basename (.base.eth) integration
  + Added architecture diagram showing wallet → SIWE → email flow
  + Better explanation of onchain identity and verifiable email
  + Added source repo and Base Chain links
* ### v1.7.0 (2026-02-18)

  + Security hardening (addresses ClawHub “Suspicious” classification)
  + Added OpenClaw metadata: declares `BASEMAIL_PRIVATE_KEY` in `requires.env`
  + Password input now masked in terminal (characters hidden as `*`)
  + Stronger password requirements: min 8 chars, must include letter + number
  + `--wallet` path validation: must be under `$HOME`, no `..` traversal, max 1KB, regular file only
  + Private key format validation (`0x` + 64 hex chars) on all input sources
  + Removed `--no-encrypt` option — managed wallets are always encrypted
  + Mnemonic is displayed once and never saved to file (removed save-to-file prompt)
  + Removed legacy plaintext key file references
  + Added `notes` in metadata clarifying: this skill only signs SIWE messages, never sends funds
  + Updated security guidelines and file locations documentation
* ### v1.4.0 (2026-02-08)

  + Better branding and descriptions
  + Full English documentation
* ### v1.1.0 (2026-02-08)

  + Security: opt-in private key storage
  + Support env var, path, auto-detect
  + Encrypted storage option (`--encrypt`)
  + Audit logging
* ### v1.6.0 (Security Update)

  + **Breaking:** `--managed` now encrypts by default
  + Removed auto-detection of external wallet paths (security improvement)
  + Mnemonic no longer auto-saved; displayed once for manual backup
  + Updated documentation for clarity
* ### v1.0.0

  + Initial release

Conclusion
----------

OpenClaw's BaseMail Skill represents a significant advancement in the realm of decentralized identity and AI agent autonomy. By providing verifiable email identities on the Base Chain, BaseMail enables AI agents to interact with services, send emails, and receive confirmations autonomously. With robust security measures, seamless integration with Basename, and SIWE authentication, BaseMail sets a new standard for email services in the decentralized ecosystem.

As the landscape of AI agents and decentralized applications continues to evolve, tools like BaseMail will play a crucial role in ensuring secure, verifiable, and autonomous communication. By leveraging the power of blockchain technology and onchain identities, BaseMail paves the way for a future where AI agents can operate with greater independence and efficiency.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/daaab/basemail/SKILL.md>
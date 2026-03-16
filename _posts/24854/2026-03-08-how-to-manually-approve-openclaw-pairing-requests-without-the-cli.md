---
layout: post
title: "How to Manually Approve OpenClaw Pairing Requests Without the CLI"
date: 2026-03-08T21:30:29
categories: [24854]
original_url: https://insightginie.com/how-to-manually-approve-openclaw-pairing-requests-without-the-cli
---

Understanding the OpenClaw approve-pairing Skill: A Manual Approach to DM Integration
=====================================================================================

For power users and developers working with OpenClaw—the versatile framework for unifying messaging platforms—managing secure connections is a daily task. While the standard workflow usually involves the `openclaw pairing approve` command, there are instances where you may find yourself restricted. Whether the CLI is not in your PATH, you lack elevated access, or you are working within a restrictive sandbox environment, knowing how to handle pairing manually is an invaluable skill. This guide dives into the `approve-pairing` skill found in the OpenClaw ecosystem, explaining how it functions behind the scenes and how to perform an approval without the usual automated tools.

What Is the approve-pairing Skill?
----------------------------------

The `approve-pairing` utility is essentially a backend helper script designed to bypass the traditional Command Line Interface. Its primary function is to authorize a pending Direct Message (DM) pairing request by directly editing the underlying credential files that OpenClaw utilizes. It is designed to work across a wide array of platforms including Telegram, WhatsApp, Signal, iMessage, Discord, Slack, and Feishu.

By understanding this skill, you gain control over your integration lifecycle, allowing you to force approvals or troubleshoot stuck requests when the standard CLI fails to communicate properly with the daemon.

The Anatomy of OpenClaw Pairing
-------------------------------

To understand why this skill works, we must first look at how OpenClaw stores its state. OpenClaw keeps track of all incoming requests and approved senders within the `~/.openclaw/credentials/` directory. Two types of files drive the approval logic:

* **<channel>-pairing.json**: This file serves as the queue for pending requests. It contains the sender ID, the authentication code, and the associated accountId.
* **<channel>-<accountId>-allowFrom.json**: This is your whitelist. It stores the identifiers of all senders who are pre-authorized to communicate through your OpenClaw gateway.

The entire concept of ‘approving’ a request boils down to a two-step data operation: moving the sender ID from the pending queue (pairing file) to the safe list (allowFrom file).

Executing the Approval via the Provided Python Script
-----------------------------------------------------

If you have access to the OpenClaw source repository, you can utilize the provided automation script. This is much safer than manual file editing, as it handles JSON serialization and potential race conditions automatically.

To run it, navigate to your local OpenClaw directory and execute the following command:

`python3 skills/approve-pairing/scripts/approve_pairing.py <channel> <code>`

For example, if you are attempting to authorize a Telegram request with the code ‘PWVW264M’, you would simply type `python3 skills/approve-pairing/scripts/approve_pairing.py telegram PWVW264M`. The script will perform the following steps:

1. Locate the correct pairing JSON file for your specified channel.
2. Parse the file to match the provided code against the pending requests.
3. Append the verified sender ID to the corresponding allowFrom file.
4. Safely remove the now-authorized code from the pending file to clean up the directory.

Performing a Manual Override
----------------------------

There may be times when even the Python script is unavailable. In this scenario, you must perform the operation manually. While this requires careful attention to JSON syntax, it is straightforward.

**Step 1: Inspect the Pending Request**  
Open the `~/.openclaw/credentials/<channel>-pairing.json` file. Identify the entry that matches the code you received. Note the `id` of the sender and the `meta.accountId` associated with the request.

**Step 2: Update the Allowlist**  
Locate the `~/.openclaw/credentials/<channel>-<accountId>-allowFrom.json` file. If the file does not exist, you will need to create it. It must follow this structure:

```
{ "version": 1, "allowFrom": [ "<sender_id>" ] }
```

Simply add the sender ID extracted from the first step into the `allowFrom` array. Ensure that you maintain valid JSON formatting, as OpenClaw is strict about its file structure.

**Step 3: Cleanup**  
Remove the entry corresponding to that code from the `pairing.json` file. If you fail to do this, the system may try to process the same request again, potentially leading to redundant entries.

Important Considerations and Troubleshooting
--------------------------------------------

Manual management comes with its own set of rules. Keep these tips in mind to avoid errors:

* **Code Expiration**: Pairing codes are temporary. They typically expire after one hour. If your manual approval fails, check the `createdAt` timestamp in the pairing file. If it is older than an hour, the code is invalid, and you must request a new pairing link from the sender.
* **Gateway Restarts**: OpenClaw often caches credential files in memory. If you modify the files manually and the changes don’t seem to take effect, run `openclaw gateway restart` to force the service to reload the updated JSON files.
* **Account ID Nuances**: If you are using a ‘default’ account, the filename uses ‘default’ instead of a specific account ID (e.g., `telegram-default-allowFrom.json`). Always check your file paths if you encounter ‘file not found’ errors.
* **Rate Limiting**: OpenClaw imposes a cap of three pending requests per channel. If you are struggling to get a new request to appear, check if your `pairing.json` file is full. You may need to delete old, expired entries to make room for new ones.

Conclusion
----------

The `approve-pairing` skill is a powerful example of how OpenClaw emphasizes modularity and transparency. By exposing the file structure, the creators allow users to bypass CLI limitations and solve authentication issues through standard file manipulation. While the automated CLI is the preferred method for most, having this manual knowledge ensures that your messaging integrations remain resilient, regardless of the environment you are running in. Remember to always backup your credential files before performing manual edits to prevent accidental corruption of your secure whitelist.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/madan-wego/approve-pairing/SKILL.md>
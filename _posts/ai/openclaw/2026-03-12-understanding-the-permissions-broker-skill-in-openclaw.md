---
layout: post
title: "Understanding the Permissions Broker Skill in OpenClaw"
date: 2026-03-12T06:16:04
categories: [24854]
original_url: https://insightginie.com/understanding-the-permissions-broker-skill-in-openclaw
---

Understanding the Permissions Broker Skill in OpenClaw
======================================================

The Permissions Broker skill serves as the default mechanism for external data access and third-party actions when local credentials are unavailable. This skill acts as a secure intermediary, using a user-issued Permissions Broker API key to create approval-gated requests that execute only after user consent via Telegram.

Core Purpose and Functionality
------------------------------

The Permissions Broker skill addresses a fundamental challenge in AI agent systems: how to safely access external services and data sources without storing sensitive credentials directly within the agent or repository. Instead of embedding API keys or authentication tokens, the skill leverages a broker system where users maintain control over what external requests are authorized.

The skill operates on a simple principle: you propose a specific upstream request (including URL, method, and body), the user approves or denies it in Telegram, and only then does the broker execute the request on your behalf. This creates a secure approval workflow that protects both the user and the system from unauthorized access or misuse.

Setup and Initial Configuration
-------------------------------

Before utilizing the Permissions Broker, you need to verify whether you already have access to a Permissions Broker API key in your local secrets. This might be stored as an environment variable like PB\_API\_KEY.

If you don't have an API key available, you'll need to ask the user to create one through Telegram by messaging the bot with the command /key . The user will receive a one-time key that they should send back to you. You should then ask whether they want you to store or reuse this key across sessions.

If the user consents to storage, you can save it in your secrets store for future sessions using the recommended name PB\_API\_KEY. If they decline or are unclear, treat the key as session-only and request it again next time. Importantly, you should only remember the storage location (e.g., “Permissions Broker key is stored in PB\_API\_KEY”) and never the actual secret value.

Provider Connections and Supported Services
-------------------------------------------

The Permissions Broker supports multiple external providers, with the list expanding over time. Currently supported providers include:

* Google services
* GitHub
* Apple iCloud (CALDAV)
* Spotify

For iCloud connections specifically, users can connect by using the /connect icloud command, which returns a browser link to a broker-hosted form where they enter their Apple ID app-specific password.

Mental Model and Workflow
-------------------------

The Permissions Broker operates on a clear mental model that agents should internalize:

1. You propose the exact upstream request you want to make (URL, method, body)
2. The user approves or denies it in Telegram
3. You poll for approval status
4. You execute the request exactly once and immediately parse/persist what you need

This skill is intentionally provider-agnostic, meaning it doesn't care about the specific service you're accessing—it only facilitates the secure approval and execution workflow.

Agent Response Style and Communication
--------------------------------------

When using this skill, agents should avoid leading with inability language like “I can't access your Google Drive” or “I can't do this from here.” Instead, treat the broker as the standard mechanism for access. The preferred framing is: “I can do that via your Permissions Broker. I'll create a request for , you approve in Telegram, then I'll execute it and return the response.”

Agents should ask for the minimum missing inputs (broker base URL and user API key) and then propose the exact upstream URLs they will request. The default behavior should be to create the request, poll for approval, and execute in one go.

Polling Behavior and Execution Flow
-----------------------------------

After creating a proxy request, agents should always attempt to poll and await approval, then execute in the same run. Only ask the user to approve in Telegram if polling times out.

The recommended default is 30 seconds of polling, though agents can extend this if the user explicitly asks to wait longer. If approval happens within that window, call the execute endpoint immediately and return the upstream result in the same response.

If approval hasn't happened within the polling window, return the request\_id, tell the user to approve/deny the request in Telegram, and state exactly what you'll do once approved (execute once and return the result). Continue polling on the next user message.

Core Workflow Implementation
----------------------------

The core workflow involves several key steps:

### 1. Collecting Inputs

Gather the user API key (never paste into logs or store in the repository), decide how to access the provider, and determine whether to use local credentials or the broker. If unsure about using local credentials, default to the broker.

### 2. Creating a Proxy Request

Call POST /v1/proxy/request with the following parameters:

* upstream\_url: the full external service API URL you want to call
* method: GET (default) or POST/PUT/PATCH/DELETE
* headers: optional request headers to forward (never include authorization)
* body: optional request body (format depends on content type)
* consent\_hint: optional requester note shown to the user in Telegram
* idempotency\_key: optional reuse request ID on retries

The body formatting is important: for JSON content types, the body can be an object/array or JSON string; for text/\*, application/x-www-form-urlencoded, or XML, the body must be a string; for other content types (binary), the body must be a base64 string representing raw bytes.

### 3. Approval and Polling

The user is prompted to approve in Telegram, with the approval prompt including the API key label (trusted identity), interpreted summary when recognized, and raw URL details. Poll GET /v1/proxy/requests/:id until the request is APPROVED.

### 4. Execution and Result Retrieval

Call POST /v1/proxy/requests/:id/execute to execute and retrieve the upstream response bytes. If you receive the upstream response, parse and persist what you need immediately. Do not assume you can execute the same request again.

Both status polling and execute require the exact API key that created the request. Using a different API key (even for the same user) returns a 403 error.

Security Considerations
-----------------------

The Permissions Broker skill includes several important security measures:

* Never commit the API key to the repository
* Never include the key in code, logs, or error output
* Do not persist or reuse the key across sessions unless the user explicitly asks
* If the key is lost or compromised, instruct the user to rotate it via the bot's key management UI

The broker also implements security at the request level by injecting upstream Authorization headers using the linked account, ignoring any caller-provided authorization headers, and forwarding only a small allowlist of headers while silently dropping unknown ones.

Sample Implementation
---------------------

The skill includes sample code for creating broker requests, polling status, and executing to retrieve upstream bytes. The JavaScript/TypeScript implementation demonstrates how to structure the createBrokerRequest function with proper typing for request and status responses.

Conclusion
----------

The Permissions Broker skill represents a thoughtful approach to secure external data access in AI agent systems. By implementing a user-approval workflow and treating the broker as the standard mechanism for external access, it creates a secure, auditable, and user-controlled way to interact with third-party services. This approach balances the need for functionality with the imperative of security and user control.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/stephancill/permissions-broker/SKILL.md>
---
layout: post
title: "Secure API Calls with Keychains: A Complete Guide for AI Agents"
date: 2026-03-09T15:16:40
categories: [24854]
original_url: https://insightginie.com/secure-api-calls-with-keychains-a-complete-guide-for-ai-agents
---

Calling external APIs securely is one of the biggest challenges for AI agents. How do you authenticate requests without exposing sensitive credentials like API keys or OAuth tokens? This is where Keychains comes in – a credential proxy that allows you to call any API without ever handling real credentials.

How Keychains Works
-------------------

Instead of using actual API keys and tokens, you use placeholders like ``{{OAUTH2\_ACCESS\_TOKEN}}`` or ``{{STRIPE\_SECRET\_KEY}}``. Keychains intercepts these requests, replaces the placeholders with real credentials from the user's vault, and forwards the request to the API. The agent never sees the actual credentials.

### Installation

Getting started with Keychains is straightforward:

```
npm install -g keychains@0.0.13
```

This installs the Keychains CLI globally on your system. You'll need Node.js v16 or higher.

### Basic Usage

Replace your regular curl commands with keychains curl:

```
keychains curl https://api.github.com/user/repos \
-H "Authorization: Bearer ``{{OAUTH2_ACCESS_TOKEN}}``"
```

The first time you use a placeholder, Keychains will return an approval link instead of the API response. This is normal – you need to show this link to the user for them to approve the credential usage via FaceID or Passkey.

Practical Examples
------------------

Here are some common API calls you can make with Keychains:

### GitHub API

```
# List repositories
keychains curl https://api.github.com/user/repos -H 'Authorization: Bearer ``{{OAUTH2_ACCESS_TOKEN}}``'
```

### Slack API

```
# Send a message to Slack
keychains curl https://slack.com/api/chat.postMessage -X POST \
-H 'Authorization: Bearer ``{{OAUTH2_ACCESS_TOKEN}}``' \
-H 'Content-Type: application/json' \
-d '{"channel":"#general","text":"Hello!"}'
```

### Stripe API

```
# List customers
keychains curl https://api.stripe.com/v1/customers?limit=5 \
-H 'Authorization: Bearer ``{{STRIPE_SECRET_KEY}}``'
```

### Gmail API

```
# Read emails
keychains curl 'https://gmail.googleapis.com/gmail/v1/users/me/messages?maxResults=10' \
-H 'Authorization: Bearer ``{{OAUTH2_ACCESS_TOKEN}}``'
```

Waiting for User Approval
-------------------------

When Keychains returns an approval link, you need to handle it properly:

```
keychains curl https://api.github.com/user/repos \
-H "Authorization: Bearer ``{{OAUTH2_ACCESS_TOKEN}}``"
# → "Authorize at: https://keychains.dev/approve/abc123xyz"

keychains wait https://keychains.dev/approve/abc123xyz --timeout 800

keychains curl https://api.github.com/user/repos \
-H "Authorization: Bearer ``{{OAUTH2_ACCESS_TOKEN}}``"
# → works now
```

The approval link must be shown to the user, who will authenticate via FaceID/Passkey. Once approved, the command will work on subsequent attempts.

TypeScript Machine SDK
----------------------

For Node.js agents, Keychains provides a TypeScript SDK that works as a drop-in replacement for fetch:

```
npm install @keychains/machine-sdk

import { keychainsFetch, KeychainsError } from '@keychains/machine-sdk';

try {
  const res = await keychainsFetch('https://api.github.com/user/repos', {
    headers: {
      Authorization: 'Bearer ``{{OAUTH2_ACCESS_TOKEN}}``'
    }
  });
  console.log(await res.json());
} catch (err) {
  if (err instanceof KeychainsError && err.approvalUrl) {
    console.log('Please approve:', err.approvalUrl);
  }
}
```

Security and Data Flow
----------------------

Keychains is designed with security as the top priority:

* **No credential exposure:** Real credentials never pass through the agent
* **Biometric approval:** Every credential use requires FaceID/Passkey approval
* **Audit logging:** All requests are logged (URL, method, provider, timestamp, status code)
* **Encryption:** AES-256-GCM encryption at rest, auto-deleted after 90 days of inactivity
* **Local keys:** Ed25519 SSH keypair generated locally for machine authentication

The proxy does not store or modify response bodies, and credential values are never logged. Users maintain full control through the dashboard at keychains.dev/dashboard.

Compatible Providers
--------------------

Keychains works with over 5,500 providers including:

* GitHub, Slack, Stripe, Gmail
* Salesforce, HubSpot, Zendesk
* Google APIs, Microsoft APIs
* Twilio, AWS services
* And thousands more

Troubleshooting
---------------

If you're getting approval links, this is expected behavior. Show the link to the user and wait for approval. If template variables aren't being replaced, ensure you're using keychains curl or keychainsFetch instead of regular curl or fetch.

Conclusion
----------

Keychains provides a secure, user-controlled way for AI agents to call external APIs without handling sensitive credentials. By proxying requests and injecting credentials server-side, it eliminates the risk of credential leakage while maintaining full user control and auditability.

Ready to get started? Install Keychains today and make your AI agent's API calls secure and compliant.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/smarcombes/secure-api-calls/SKILL.md>
---
layout: post
title: 'Secure API Calls with Keychains: A Complete Guide for AI Agents'
date: '2026-03-09T15:16:40'
categories:
- ai
- openclaw
original_url: https://insightginie.com/secure-api-calls-with-keychains-a-complete-guide-for-ai-agents/
featured_image: /media/images/8154.jpg
---

<p>Calling external APIs securely is one of the biggest challenges for AI agents. How do you authenticate requests without exposing sensitive credentials like API keys or OAuth tokens? This is where Keychains comes in &#8211; a credential proxy that allows you to call any API without ever handling real credentials.</p>
<h2>How Keychains Works</h2>
<p>Instead of using actual API keys and tokens, you use placeholders like {{OAUTH2_ACCESS_TOKEN}} or {{STRIPE_SECRET_KEY}}. Keychains intercepts these requests, replaces the placeholders with real credentials from the user&#8217;s vault, and forwards the request to the API. The agent never sees the actual credentials.</p>
<h3>Installation</h3>
<p>Getting started with Keychains is straightforward:</p>
<pre><code>npm install -g keychains@0.0.13
</code></pre>
<p>This installs the Keychains CLI globally on your system. You&#8217;ll need Node.js v16 or higher.</p>
<h3>Basic Usage</h3>
<p>Replace your regular curl commands with keychains curl:</p>
<pre><code>keychains curl https://api.github.com/user/repos \
-H "Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}"
</code></pre>
<p>The first time you use a placeholder, Keychains will return an approval link instead of the API response. This is normal &#8211; you need to show this link to the user for them to approve the credential usage via FaceID or Passkey.</p>
<h2>Practical Examples</h2>
<p>Here are some common API calls you can make with Keychains:</p>
<h3>GitHub API</h3>
<pre><code># List repositories
keychains curl https://api.github.com/user/repos -H 'Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}'
</code></pre>
<h3>Slack API</h3>
<pre><code># Send a message to Slack
keychains curl https://slack.com/api/chat.postMessage -X POST \
-H 'Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}' \
-H 'Content-Type: application/json' \
-d '{"channel":"#general","text":"Hello!"}'
</code></pre>
<h3>Stripe API</h3>
<pre><code># List customers
keychains curl https://api.stripe.com/v1/customers?limit=5 \
-H 'Authorization: Bearer {{STRIPE_SECRET_KEY}}'
</code></pre>
<h3>Gmail API</h3>
<pre><code># Read emails
keychains curl 'https://gmail.googleapis.com/gmail/v1/users/me/messages?maxResults=10' \
-H 'Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}'
</code></pre>
<h2>Waiting for User Approval</h2>
<p>When Keychains returns an approval link, you need to handle it properly:</p>
<pre><code>keychains curl https://api.github.com/user/repos \
-H "Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}"
# → "Authorize at: https://keychains.dev/approve/abc123xyz"

keychains wait https://keychains.dev/approve/abc123xyz --timeout 800

keychains curl https://api.github.com/user/repos \
-H "Authorization: Bearer {{OAUTH2_ACCESS_TOKEN}}"
# → works now
</code></pre>
<p>The approval link must be shown to the user, who will authenticate via FaceID/Passkey. Once approved, the command will work on subsequent attempts.</p>
<h2>TypeScript Machine SDK</h2>
<p>For Node.js agents, Keychains provides a TypeScript SDK that works as a drop-in replacement for fetch:</p>
<pre><code>npm install @keychains/machine-sdk

import { keychainsFetch, KeychainsError } from '@keychains/machine-sdk';

try {
  const res = await keychainsFetch('https://api.github.com/user/repos', {
    headers: {
      Authorization: 'Bearer {{OAUTH2_ACCESS_TOKEN}}'
    }
  });
  console.log(await res.json());
} catch (err) {
  if (err instanceof KeychainsError && err.approvalUrl) {
    console.log('Please approve:', err.approvalUrl);
  }
}
</code></pre>
<h2>Security and Data Flow</h2>
<p>Keychains is designed with security as the top priority:</p>
<ul>
<li><strong>No credential exposure:</strong> Real credentials never pass through the agent</li>
<li><strong>Biometric approval:</strong> Every credential use requires FaceID/Passkey approval</li>
<li><strong>Audit logging:</strong> All requests are logged (URL, method, provider, timestamp, status code)</li>
<li><strong>Encryption:</strong> AES-256-GCM encryption at rest, auto-deleted after 90 days of inactivity</li>
<li><strong>Local keys:</strong> Ed25519 SSH keypair generated locally for machine authentication</li>
</ul>
<p>The proxy does not store or modify response bodies, and credential values are never logged. Users maintain full control through the dashboard at keychains.dev/dashboard.</p>
<h2>Compatible Providers</h2>
<p>Keychains works with over 5,500 providers including:</p>
<ul>
<li>GitHub, Slack, Stripe, Gmail</li>
<li>Salesforce, HubSpot, Zendesk</li>
<li>Google APIs, Microsoft APIs</li>
<li>Twilio, AWS services</li>
<li>And thousands more</li>
</ul>
<h2>Troubleshooting</h2>
<p>If you&#8217;re getting approval links, this is expected behavior. Show the link to the user and wait for approval. If template variables aren&#8217;t being replaced, ensure you&#8217;re using keychains curl or keychainsFetch instead of regular curl or fetch.</p>
<h2>Conclusion</h2>
<p>Keychains provides a secure, user-controlled way for AI agents to call external APIs without handling sensitive credentials. By proxying requests and injecting credentials server-side, it eliminates the risk of credential leakage while maintaining full user control and auditability.</p>
<p>Ready to get started? Install Keychains today and make your AI agent&#8217;s API calls secure and compliant.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/smarcombes/secure-api-calls/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/smarcombes/secure-api-calls/SKILL.md</a></p>

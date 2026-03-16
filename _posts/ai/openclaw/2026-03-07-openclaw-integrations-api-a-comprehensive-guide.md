---
layout: post
title: 'OpenClaw Integrations API: A Comprehensive Guide'
date: '2026-03-07T14:18:32'
categories:
- ai
- openclaw
original_url: https://insightginie.com/openclaw-integrations-api-a-comprehensive-guide/
featured_image: /media/images/8143.jpg
---

<h2>What is OpenClaw?</h2>
<p>OpenClaw is a skill-based integration system that enables applications built on MakeX to discover and execute actions from third-party services such as Gmail, Slack, GitHub, and many others through Composio. This powerful system allows developers to seamlessly integrate external services into their applications without building custom integrations from scratch.</p>
<h2>Authentication and Security</h2>
<p>All OpenClaw API endpoints require authentication using the X-Org-Token header. This organization service token is validated against the organization database, ensuring secure server-to-server communication. Unlike traditional web applications, user session cookies are not used for these endpoints.</p>
<p>To obtain your X-Org-Token:</p>
<ol>
<li>Visit <a href="https://www.makex.app/">https://www.makex.app/</a> and sign up for an account</li>
<li>Navigate to Settings in your dashboard</li>
<li>Copy your API key from the settings page &#8211; this is your X-Org-Token</li>
</ol>
<h2>Base URL and CORS Support</h2>
<p>The base URL for all OpenClaw API endpoints follows this pattern:</p>
<pre><code>POST /api/openclaw/integrations/&lt;endpoint&gt;
</code></pre>
<p>All endpoints support Cross-Origin Resource Sharing (CORS) through a preflight OPTIONS handler, making it easy to integrate with web applications hosted on different domains.</p>
<h2>API Endpoints Overview</h2>
<p>OpenClaw provides five main API endpoints that cover the complete integration workflow:</p>
<h3>1. Search Actions</h3>
<p>The search-actions endpoint allows you to discover available actions and tools across multiple integrations. This is particularly useful when you want to find what capabilities are available for connected services.</p>
<p><strong>Request Body:</strong></p>
<pre><code>{
  "integrations": ["gmail", "slack", "github"],
  "toolkit": "gmail",
  "search": "send"
}
</code></pre>
<p>The endpoint accepts three parameters:</p>
<ul>
<li><strong>integrations</strong> (required): Array of integration slugs to search across</li>
<li><strong>toolkit</strong> (optional): Overrides integrations and searches only this toolkit</li>
<li><strong>search</strong> (optional): Filter actions by keyword</li>
</ul>
<p><strong>Response Example:</strong></p>
<pre><code>{
  "total": 12,
  "actions": {
    "gmail": [
      {
        "slug": "GMAIL_SEND_EMAIL",
        "name": "Send Email"
      },
      {
        "slug": "GMAIL_CREATE_DRAFT",
        "name": "Create Draft"
      }
    ],
    "slack": [
      {
        "slug": "SLACK_SEND_MESSAGE",
        "name": "Send Message"
      }
    ]
  }
}
</code></pre>
<h3>2. Connected Account</h3>
<p>The connected-account endpoint checks if a specific integration is connected for your organization and retrieves account details. This is essential for understanding which services are available for use.</p>
<p><strong>Request Body:</strong></p>
<pre><code>{
  "integration": "gmail"
}
</code></pre>
<p><strong>Success Response:</strong></p>
<pre><code>{
  "accountId": "conn_abc123",
  "userId": "org_xyz",
  "integration": "gmail",
  "status": "ACTIVE"
}
</code></pre>
<p><strong>Error Response (404):</strong></p>
<pre><code>{
  "error": "No active connected account found for integration gmail",
  "availableIntegrations": ["slack", "github"]
}
</code></pre>
<h3>3. Action Details</h3>
<p>The action-details endpoint provides comprehensive information about a specific action, including its input and output parameters. This is crucial for understanding how to properly invoke an action.</p>
<p><strong>Request Body:</strong></p>
<pre><code>{
  "action_slug": "GMAIL_SEND_EMAIL"
}
</code></pre>
<p><strong>Response Example:</strong></p>
<pre><code>{
  "name": "Send Email",
  "slug": "GMAIL_SEND_EMAIL",
  "description": "Send an email via Gmail",
  "inputParameters": {
    "to": {
      "type": "string",
      "description": "Recipient email",
      "required": true
    },
    "subject": {
      "type": "string",
      "description": "Email subject"
    },
    "body": {
      "type": "string",
      "description": "Email body"
    }
  },
  "outputParameters": {
    "messageId": {
      "type": "string"
    },
    "threadId": {
      "type": "string"
    }
  }
}
</code></pre>
<h3>4. Run Action</h3>
<p>The run-action endpoint executes a specific action on a connected account. This is where the actual integration work happens.</p>
<p><strong>Request Body:</strong></p>
<pre><code>{
  "toolName": "GMAIL_SEND_EMAIL",
  "accountId": "conn_abc123",
  "arguments": {
    "to": "user@example.com",
    "subject": "Hello",
    "body": "Hi there"
  }
}
</code></pre>
<p>The endpoint accepts several optional parameters:</p>
<ul>
<li><strong>text</strong>: Natural language text input (used if arguments is not provided)</li>
<li><strong>version</strong>: API version override</li>
<li><strong>custom_auth_params</strong>: Custom authentication parameters</li>
<li><strong>custom_connection_data</strong>: Custom connection data</li>
<li><strong>allow_tracing</strong>: Enable tracing for the execution</li>
</ul>
<p>The response contains the raw Composio execution response, which varies depending on the action being executed.</p>
<h3>5. Output Structure</h3>
<p>The output-structure endpoint executes an action and returns its output structure. This is particularly useful for understanding the shape of an action&#8217;s response without processing the actual data.</p>
<p><strong>Request Body:</strong></p>
<pre><code>{
  "action_slug": "GMAIL_SEND_EMAIL",
  "accountId": "conn_abc123",
  "arguments": {
    "to": "test@example.com",
    "subject": "Test",
    "body": "Test body"
  }
}
</code></pre>
<p><strong>Response Example:</strong></p>
<pre><code>{
  "successful": true,
  "data": {
    ...
  }
}
</code></pre>
<h2>Error Handling</h2>
<p>All endpoints return errors in a consistent format:</p>
<pre><code>{
  "error": "Description of what went wrong"
}
</code></pre>
<p>Common error status codes include:</p>
<ul>
<li><strong>400</strong>: Missing required parameters</li>
<li><strong>401</strong>: Missing or invalid X-Org-Token</li>
<li><strong>404</strong>: Resource not found (e.g., no connected account)</li>
<li><strong>500</strong>: Server error or missing COMPOSIO_API_KEY</li>
</ul>
<h2>Typical Workflow</h2>
<p>Here&#8217;s a typical workflow for using the OpenClaw API:</p>
<ol>
<li><strong>Search actions</strong> to discover what&#8217;s available for connected integrations</li>
<li><strong>Get connected account</strong> to retrieve the accountId for a specific integration</li>
<li><strong>Get action details</strong> to understand input/output parameters for a chosen action</li>
<li><strong>Run action</strong> to execute the action with the required arguments</li>
</ol>
<h2>Benefits of Using OpenClaw</h2>
<p>OpenClaw provides several advantages for developers:</p>
<ul>
<li><strong>Reduced Development Time</strong>: No need to build custom integrations for each service</li>
<li><strong>Consistency</strong>: Standardized API across all supported services</li>
<li><strong>Scalability</strong>: Easily add new integrations as they become available</li>
<li><strong>Security</strong>: Centralized authentication and token management</li>
<li><strong>Maintainability</strong>: Single point of update when services change their APIs</li>
</ul>
<h2>Getting Started</h2>
<p>To start using OpenClaw in your MakeX application:</p>
<ol>
<li>Sign up for a MakeX account at <a href="https://www.makex.app/">https://www.makex.app/</a></li>
<li>Obtain your X-Org-Token from the settings page</li>
<li>Review the available integrations and their capabilities</li>
<li>Implement the workflow described above in your application</li>
</ol>
<p>With OpenClaw, you can dramatically simplify the process of integrating third-party services into your applications, allowing you to focus on building core functionality rather than managing API connections.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/tkejr/makex/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/tkejr/makex/SKILL.md</a></p>

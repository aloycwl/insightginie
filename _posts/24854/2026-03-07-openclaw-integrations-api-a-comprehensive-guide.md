---
layout: post
title: "OpenClaw Integrations API: A Comprehensive Guide"
date: 2026-03-07T14:18:32
categories: [24854]
original_url: https://insightginie.com/openclaw-integrations-api-a-comprehensive-guide
---

What is OpenClaw?
-----------------

OpenClaw is a skill-based integration system that enables applications built on MakeX to discover and execute actions from third-party services such as Gmail, Slack, GitHub, and many others through Composio. This powerful system allows developers to seamlessly integrate external services into their applications without building custom integrations from scratch.

Authentication and Security
---------------------------

All OpenClaw API endpoints require authentication using the X-Org-Token header. This organization service token is validated against the organization database, ensuring secure server-to-server communication. Unlike traditional web applications, user session cookies are not used for these endpoints.

To obtain your X-Org-Token:

1. Visit <https://www.makex.app/> and sign up for an account
2. Navigate to Settings in your dashboard
3. Copy your API key from the settings page – this is your X-Org-Token

Base URL and CORS Support
-------------------------

The base URL for all OpenClaw API endpoints follows this pattern:

```
POST /api/openclaw/integrations/<endpoint>
```

All endpoints support Cross-Origin Resource Sharing (CORS) through a preflight OPTIONS handler, making it easy to integrate with web applications hosted on different domains.

API Endpoints Overview
----------------------

OpenClaw provides five main API endpoints that cover the complete integration workflow:

### 1. Search Actions

The search-actions endpoint allows you to discover available actions and tools across multiple integrations. This is particularly useful when you want to find what capabilities are available for connected services.

**Request Body:**

```
{
  "integrations": ["gmail", "slack", "github"],
  "toolkit": "gmail",
  "search": "send"
}
```

The endpoint accepts three parameters:

* **integrations** (required): Array of integration slugs to search across
* **toolkit** (optional): Overrides integrations and searches only this toolkit
* **search** (optional): Filter actions by keyword

**Response Example:**

```
{
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
```

### 2. Connected Account

The connected-account endpoint checks if a specific integration is connected for your organization and retrieves account details. This is essential for understanding which services are available for use.

**Request Body:**

```
{
  "integration": "gmail"
}
```

**Success Response:**

```
{
  "accountId": "conn_abc123",
  "userId": "org_xyz",
  "integration": "gmail",
  "status": "ACTIVE"
}
```

**Error Response (404):**

```
{
  "error": "No active connected account found for integration gmail",
  "availableIntegrations": ["slack", "github"]
}
```

### 3. Action Details

The action-details endpoint provides comprehensive information about a specific action, including its input and output parameters. This is crucial for understanding how to properly invoke an action.

**Request Body:**

```
{
  "action_slug": "GMAIL_SEND_EMAIL"
}
```

**Response Example:**

```
{
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
```

### 4. Run Action

The run-action endpoint executes a specific action on a connected account. This is where the actual integration work happens.

**Request Body:**

```
{
  "toolName": "GMAIL_SEND_EMAIL",
  "accountId": "conn_abc123",
  "arguments": {
    "to": "user@example.com",
    "subject": "Hello",
    "body": "Hi there"
  }
}
```

The endpoint accepts several optional parameters:

* **text**: Natural language text input (used if arguments is not provided)
* **version**: API version override
* **custom\_auth\_params**: Custom authentication parameters
* **custom\_connection\_data**: Custom connection data
* **allow\_tracing**: Enable tracing for the execution

The response contains the raw Composio execution response, which varies depending on the action being executed.

### 5. Output Structure

The output-structure endpoint executes an action and returns its output structure. This is particularly useful for understanding the shape of an action’s response without processing the actual data.

**Request Body:**

```
{
  "action_slug": "GMAIL_SEND_EMAIL",
  "accountId": "conn_abc123",
  "arguments": {
    "to": "test@example.com",
    "subject": "Test",
    "body": "Test body"
  }
}
```

**Response Example:**

```
{
  "successful": true,
  "data": {
    ...
  }
}
```

Error Handling
--------------

All endpoints return errors in a consistent format:

```
{
  "error": "Description of what went wrong"
}
```

Common error status codes include:

* **400**: Missing required parameters
* **401**: Missing or invalid X-Org-Token
* **404**: Resource not found (e.g., no connected account)
* **500**: Server error or missing COMPOSIO\_API\_KEY

Typical Workflow
----------------

Here’s a typical workflow for using the OpenClaw API:

1. **Search actions** to discover what’s available for connected integrations
2. **Get connected account** to retrieve the accountId for a specific integration
3. **Get action details** to understand input/output parameters for a chosen action
4. **Run action** to execute the action with the required arguments

Benefits of Using OpenClaw
--------------------------

OpenClaw provides several advantages for developers:

* **Reduced Development Time**: No need to build custom integrations for each service
* **Consistency**: Standardized API across all supported services
* **Scalability**: Easily add new integrations as they become available
* **Security**: Centralized authentication and token management
* **Maintainability**: Single point of update when services change their APIs

Getting Started
---------------

To start using OpenClaw in your MakeX application:

1. Sign up for a MakeX account at <https://www.makex.app/>
2. Obtain your X-Org-Token from the settings page
3. Review the available integrations and their capabilities
4. Implement the workflow described above in your application

With OpenClaw, you can dramatically simplify the process of integrating third-party services into your applications, allowing you to focus on building core functionality rather than managing API connections.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/tkejr/makex/SKILL.md>
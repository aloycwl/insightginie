---
layout: post
title: "Understanding the Didit Phone Verification Skill for OpenClaw"
date: 2026-03-12T01:16:22
categories: [24854]
original_url: https://insightginie.com/understanding-the-didit-phone-verification-skill-for-openclaw
---

What Is the Didit Phone Verification Skill?
-------------------------------------------

The **Didit Phone Verification** skill is an OpenClaw integration that enables two-step phone verification using one-time passwords (OTPs). It leverages Didit's standalone API to send verification codes via multiple channels—SMS, WhatsApp, Telegram, and voice calls—and validate them securely. This skill is ideal for implementing phone-based identity verification, fraud prevention, and user authentication workflows.

### Core Functionality

The skill operates in two steps:

1. **Send** a verification code to a phone number
2. **Check** the code the user provides

Key constraints include:

* Codes expire after 5 minutes
* Maximum 3 verification attempts per code
* Maximum 2 resend requests within 24 hours
* Rate limit: 4 sends per hour per phone number
* Phone numbers must be in E.164 format (e.g., +14155552671)
* Send must be called before Check

Key Features and Capabilities
-----------------------------

The Didit Phone Verification skill offers robust verification features:

* **Multi-channel delivery**: SMS (default fallback), WhatsApp, Telegram, and voice calls
* **Fraud detection**: Identifies disposable/temporary numbers, VoIP numbers, and carrier information
* **Policy-based auto-decline**: Automatically rejects risky numbers based on configurable policies
* **Duplicate detection**: Detects if a number has already been verified by another user
* **Risk scoring**: Provides fraud signals for enhanced security

### Delivery Channel Fallback

The skill intelligently falls back to SMS if the preferred channel is unavailable. For example, if WhatsApp verification fails, it automatically attempts SMS delivery.

Getting Started with Authentication
-----------------------------------

All API requests require an API key via the x-api-key header. Here's how to obtain one:

### For New Users

If you don't have a Didit API key, you can create one in just two API calls:

1. Register: POST https://apx.didit.me/auth/v2/programmatic/register/ with your email and password
2. Verify: Check your email for a 6-character OTP code, then POST to https://apx.didit.me/auth/v2/programmatic/verify-email/ with the code

The response includes your api\_key. To add credits, check your balance via GET /v3/billing/balance/ and top up using POST /v3/billing/top-up/.

Step 1: Sending the Verification Code
-------------------------------------

The Send request initiates the verification process. Here's the structure:

### Request Details

```
POST https://verification.didit.me/v3/phone/send/
Headers:
  x-api-key: YOUR_API_KEY
  Content-Type: application/json
```

### Request Body Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| phone\_number | string | Yes | E.164 format phone number |
| options.code\_size | integer | No | Code length (4-8, default 6) |
| options.locale | string | No | Message locale (e.g., en-US) |
| options.preferred\_channel | string | No | “sms”, “whatsapp”, “telegram”, or “voice” |
| signals.ip | string | No | User's IP for fraud detection |
| signals.device\_id | string | No | Unique device identifier |

### Status Handling

Common status responses include:

* **Success**: Code sent successfully
* **Retry**: Temporary issue, wait and retry (max 2 retries)
* **Undeliverable**: Number cannot receive messages
* **Blocked**: Number blocked due to spam

Step 2: Checking the Verification Code
--------------------------------------

After successfully sending a code, you must verify it using the Check endpoint.

### Request Details

```
POST https://verification.didit.me/v3/phone/check/
Headers:
  x-api-key: YOUR_API_KEY
  Content-Type: application/json
```

### Request Body Parameters

| Parameter | Type | Required | Description |
| --- | --- | --- | --- |
| phone\_number | string | Yes | Same E.164 number used in Send |
| code | string | Yes | 4-8 character code user received |
| duplicated\_phone\_number\_action | string | No | “NO\_ACTION” or “DECLINE” |
| disposable\_number\_action | string | No | “NO\_ACTION” or “DECLINE” |
| voip\_number\_action | string | No | “NO\_ACTION” or “DECLINE” |

### Status Handling

Common status responses include:

* **Approved**: Code correct, no policy violations
* **Failed**: Code incorrect, ask user to retry (up to 3 attempts)
* **Declined**: Code correct but policy violation detected
* **Expired or Not Found**: No pending code, resend required

Response Data and Fraud Detection
---------------------------------

The Check response includes comprehensive phone information:

* Carrier details (name, type: mobile/landline/VoIP)
* Country information (code, name)
* Verification method used
* Disposable and VoIP status
* Verification attempts count
* Warnings array with fraud risk information

### Warning Tags

The system provides detailed warnings for potential fraud:

* VERIFICATION\_CODE\_MISMATCH: Incorrect code entered
* DUPLICATE\_PHONE\_NUMBER: Number already verified by another user
* DISPOSABLE\_NUMBER: Temporary/disposable number detected
* VOIP\_NUMBER: VoIP number detected

Best Practices and Implementation Tips
--------------------------------------

To ensure successful implementation:

1. Always validate phone numbers in E.164 format before sending
2. Implement proper error handling for rate limits and temporary failures
3. Use fraud signals (IP, device ID, user agent) to enhance security
4. Configure appropriate auto-decline policies based on your risk tolerance
5. Monitor API usage and credits through the Didit Business Console
6. Consider using the didit-verification-management skill for full platform management

Integration with OpenClaw
-------------------------

The Didit Phone Verification skill integrates seamlessly with OpenClaw workflows. It can be triggered when users need phone verification, sending SMS/WhatsApp codes, checking verification codes, or implementing phone-based identity verification. The skill supports multiple delivery channels and provides comprehensive fraud signals for risk assessment.

For advanced use cases, consider combining this skill with other OpenClaw skills for complete user verification workflows, session management, and billing integration.

Conclusion
----------

The Didit Phone Verification skill provides a robust, secure solution for phone-based authentication and identity verification. With support for multiple delivery channels, comprehensive fraud detection, and flexible policy controls, it's an essential tool for any application requiring phone verification. By following the implementation guidelines and best practices outlined above, you can effectively integrate this skill into your OpenClaw workflows for enhanced security and user verification.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/rosasalberto/didit-phone-verification/SKILL.md>
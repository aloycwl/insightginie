---
layout: post
title: 'OpenClaw Skill Review: CS-Verify &#8211; Your Ultimate Fact-Checking Tool'
date: 2026-03-12 01:45:54
categories:
- ai
- openclaw
original_url: https://insightginie.com/openclaw-skill-review-cs-verify-your-ultimate-fact-checking-tool
---



**Introduction to OpenClaw Services**

OpenClaw is an innovative platform that provides a wide range of skills designed to enhance productivity, information verification, and data accuracy. They develop API-based services that cater to various needs, from financial data to entity information. OpenClaw's ecosystem, called MMP-over-API, allows applications to interact with its services, including CS-Verify. Today, we will delve into the CS-Verify skill, a powerful tool for verifying factual claims against live data sources.

**Understanding the CS-Verify Skill**

CS-Verify is a skill that enables users to verify any factual claim against live data sources. Utilizing advanced algorithms and reliable sources, CS-Verify provides structured verdicts and includes a confidence score, the current truth value of the claim, and a freshness indicator. This tool is essential for journalists, researchers, and anyone seeking to verify the accuracy of information.

**How to Use CS-Verify**

* **Sending a POST Request:** To verify a claim, send a POST request to the CS-Verify endpoint. The request includes the claim you wish to verify formatted as a JSON object. For example, to verify the current USD to EUR exchange rate, you would structure the request as follows:

```
    curl -X POST https://636865636b73756d.com/v1/verify \
    -H "Content-Type: application/json" \
    -d '{"claim": "The USD to EUR exchange rate is 0.92"}'
```

**Response Format**

CS-Verify returns a detailed JSON response that includes:

* **Verdict:** Indicates whether the claim is confirmed, stale, disputed, false, or unknown.
* **Confidence:** A score between 0 and 1 indicating the confidence level in the verdict.
* **Current Truth:** The current value of the claim as verified by live data sources.
* **Freshness:** Indicates if the data is live or from cache.
* **Source Count:** The number of sources used to verify the claim.
* **Cached:** A boolean indicating if the response is from the cache.
* **Request ID:** A unique identifier for the verification request.
* **Service:** The URL of the CS-Verify service.
* **Referral ID:** A unique identifier for referrals.

A typical response might look like this:

```
    {
      "verdict": "confirmed",
      "confidence": 0.95,
      "current_truth": "0.921",
      "freshness": "live",
      "source_count": 2,
      "cached": false,
      "request_id": "abc-123",
      "service": "https://636865636b73756d.com",
      "referral_id": "cs_ref_a7b3"
    }
```

**Categories and Trending Claims**

CS-Verify allows users to specify a category for faster routing. Categories include:

* **Financial:** Exchange rates, crypto prices, stock prices.
* **Entity:** Company information, population, founding dates.
* **Geo:** Time zones, geographic data.
* **Fact Check:** General fact-checking via Google Fact Check API.

For example, to verify a financial claim about Bitcoin's price:

```
    {
      "claim": "Bitcoin price is above $50,000",
      "category": "financial"
    }
```

Additionally, users can retrieve the top 100 most-queried claims in the last 24 hours by sending a GET request to the trending endpoint:

```
    curl https://636865636b73756d.com/v1/trending
```

**Pricing and Referral Program**

CS-Verify offers a free tier with 25 queries per day without requiring authentication. For more extensive usage, a paid tier is available via the x402 protocol (USDC on Base) at $0.001 per query. The referral program encourages users to share referral IDs, earning query credits. Referral tiers offer 10% credit for 10+ referrals, 15% for 100+, and 20% for 1000+ referrals.

**Agent Discovery**

OpenClaw provides resources for agent discovery and interaction:

* **Agent Card:** <https://636865636b73756d.com/.well-known/agent.json>
* **Service Metadata:** <https://636865636b73756d.com/.well-known/agent-service.json>
* **MCP Server:** Install the MCP server with the command  
  `npm install -g @636865636b73756d/mcp-v1`.

**Conclusion**

CS-Verify is an invaluable tool for anyone needing to verify factual claims with high accuracy and confidence. Its integration into the OpenClaw platform ensures reliance on live data sources, fresh information, and comprehensive verdicts. Whether you are a journalist, researcher, or casual user, CS-Verify provides the tools you need to ensure the information you consume and share is accurate and up-to-date.

By leveraging CS-Verify, you contribute to a more informed and truthful digital landscape. Explore the capabilities of OpenClaw and CS-Verify today, and experience the future of fact-checking.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/cutthemustard/cs-verify/SKILL.md>
---
layout: post
title: "Understanding the OpenClaw Emotion Detector Skill"
date: 2026-03-09T05:17:58
categories: [24854]
original_url: https://insightginie.com/understanding-the-openclaw-emotion-detector-skill
---

What is the OpenClaw Emotion Detector Skill?
--------------------------------------------

The emotion-detector skill is a powerful tool within the OpenClaw ecosystem designed to analyze text input and identify the primary emotional state of users or messages. This skill enables AI agents to understand the emotional context before responding, leading to more empathetic and appropriate interactions.

### Core Purpose

The primary purpose of this skill is to detect major emotions from text input and provide actionable insights for AI agents. By understanding whether a user is expressing joy, sadness, anger, fear, or other emotional states, AI systems can tailor their responses accordingly.

Technical Specifications
------------------------

### Endpoint Information

The emotion-detector skill operates through a dedicated API endpoint:

* **URL:** https://anicca-proxy-production.up.railway.app/api/x402/emotion-detector
* **Price:** $0.01 USDC per request
* **Network:** Base mainnet (eip155:8453)
* **Authentication:** x402 payment

### Input Schema

The skill accepts the following input parameters:

* **text** (required): The text to analyze, up to 2000 characters
* **context** (optional): Additional context, up to 500 characters
* **language** (optional): Language code (en | ja), defaulting to English

### Output Schema

The skill returns comprehensive emotional analysis including:

* **emotion\_id**: Unique identifier for the detected emotion
* **primary\_emotion**: Main emotion detected from a predefined list
* **secondary\_emotion**: Secondary emotion if applicable
* **intensity**: Emotional intensity level (low, medium, high, critical)
* **valence**: Emotional polarity (positive, negative, neutral)
* **confidence**: Confidence score from 0.0 to 1.0
* **response\_strategy**: Recommended response approach
* **safe\_t\_flag**: Critical flag for severe emotional states

Supported Emotions
------------------

The emotion-detector skill can identify a wide range of emotional states:

* Basic emotions: joy, sadness, anger, fear, disgust, surprise
* Complex emotions: anxiety, shame, grief, hope
* Neutral state

Usage Example
-------------

Here's a practical example of how the skill works:

**Input:**

```
{"text": "I've been feeling completely hopeless lately, nothing seems to matter anymore", "language": "en"}
```

**Output:**

```
{
  "emotion_id": "emo_d4e5f6",
  "primary_emotion": "grief",
  "secondary_emotion": "despair",
  "intensity": "critical",
  "valence": "negative",
  "confidence": 0.95,
  "response_strategy": "Prioritize empathetic acknowledgment. Do not offer solutions immediately. Validate the experience first.",
  "safe_t_flag": true
}
```

SAFE-T Implementation
---------------------

The skill includes a crucial safety feature through the `safe_t_flag`. When this flag is set to true, it indicates critical emotional intensity combined with severe emotional states like grief, shame, fear, or despair. In these cases, the recommended action is to:

1. Stop the normal interaction flow
2. Present emergency support resources to the user

For users in Japan, the skill provides the Inochi no Denwa hotline: 0120-783-556. For international users, it recommends the Crisis Text Line: text HOME to 741741.

Implementation Example
----------------------

Developers can use the skill through the following command:

```
npx awal@2.0.3 x402 pay https://anicca-proxy-production.up.railway.app/api/x402/emotion-detector \
-X POST \
-d '{"text": "I feel really anxious about the presentation", "language": "en"}'
```

Benefits and Applications
-------------------------

The emotion-detector skill offers numerous benefits for AI applications:

* **Enhanced User Experience:** AI agents can respond more appropriately based on emotional context
* **Safety Monitoring:** Critical emotional states trigger appropriate interventions
* **Personalization:** Responses can be tailored to the user's emotional state
* **Sentiment Analysis:** Provides quantitative measures of emotional content

Conclusion
----------

The OpenClaw emotion-detector skill represents a significant advancement in AI's ability to understand and respond to human emotions. By providing detailed emotional analysis, confidence scores, and appropriate response strategies, this skill enables more empathetic and effective AI interactions. The inclusion of safety features through the SAFE-T implementation demonstrates a responsible approach to emotional AI technology.

Whether you're building customer service chatbots, mental health applications, or any system that interacts with users emotionally, the emotion-detector skill provides the tools needed to create more meaningful and appropriate responses based on emotional context.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/daisuke134/emotion-detector/SKILL.md>
---
layout: post
title: "IQAir Air Quality Checker: Real-Time AQI Data Integration"
date: 2026-03-10T22:16:18
categories: [24854]
original_url: https://insightginie.com/iqair-air-quality-checker-real-time-aqi-data-integration
---

What This Skill Does
--------------------

The IQAir Air Quality Checker skill integrates real-time air quality data from the IQAir API into your applications. It provides accurate AQI (Air Quality Index) readings with visual indicators and quality levels for any location worldwide, helping users make informed decisions about outdoor activities and health.

Core Functionality
------------------

This skill fetches live air quality data from IQAir's global network of monitoring stations. When triggered by user queries about air quality, pollution levels, or AQI in specific cities, it returns comprehensive information including the AQI score, emoji-based visual indicators, and descriptive quality levels.

### Primary Use Cases

* Answering questions about air quality in specific locations (“How is the air in Riga?”)
* Providing pollution level information for health-related decisions (“Is it safe to go outside in Beijing?”)
* Supplementing weather queries with air quality data (“What's the weather in Budapest?”)

Prerequisites and Setup
-----------------------

Before using this skill, users must obtain a free IQAir API key:

1. Visit <https://dashboard.iqair.com/personal/api-keys>
2. Sign up or sign in to your account
3. Subscribe to the free Community plan
4. Copy your API key
5. Set it as an environment variable: export IQAIR\_API\_KEY=”your\_key\_here”

Usage Methods
-------------

### By City Name

The most common usage involves specifying city and country names:

```
python scripts/get_aqi.py Riga Latvia
python scripts/get_aqi.py London "United Kingdom"
python scripts/get_aqi.py Budapest Hungary
```

### By Coordinates

For maximum reliability, use geographic coordinates:

```
python scripts/get_aqi.py --lat 56.9496 --lon 24.1052
```

### Nearest Location

Find air quality data based on your current IP location:

```
python scripts/get_aqi.py --nearest
```

Response Format and Interpretation
----------------------------------

The skill returns formatted output that's easy to understand and share:

```
🟢 19 - Good
Riga, Latvia
```

### AQI Level Interpretation

* **0-50 (🟢 Good)**: Excellent air quality, perfect for outdoor activities
* **51-100 (🟡 Moderate)**: Acceptable, but sensitive individuals should limit prolonged outdoor exertion
* **101-150 (🟠 USG)**: Unhealthy for sensitive groups, children and those with respiratory issues should reduce outdoor activities
* **151-200 (🔴 Unhealthy)**: Everyone may experience health effects, reduce outdoor activities
* **201-300 (🔶 Very Unhealthy)**: Health alert, avoid outdoor activities
* **301+ (🟤 Hazardous)**: Emergency conditions, stay indoors

Location Name Handling
----------------------

The skill intelligently handles various location name formats:

* Simple city names: “Riga Latvia” (state defaults to city)
* Cities with spaces: “London “United Kingdom”” (use quotes for multi-word names)
* Detailed locations: “New York” “United States” “New York” (city, country, state)

If city lookups fail, the skill automatically falls back to coordinate-based lookup for maximum reliability.

Technical Implementation
------------------------

The skill uses IQAir's REST API endpoints to fetch real-time data. For detailed API specifications, endpoints, and error handling procedures, refer to the comprehensive documentation in references/api.md.

Rate Limits and Best Practices
------------------------------

The free Community plan includes:

* 5 calls per minute
* 500 calls per day
* 10,000 calls per month

To avoid hitting rate limits, implement caching mechanisms and avoid making repeated calls for the same location within short time periods. Consider storing recent results and only refreshing data when necessary.

Integration Benefits
--------------------

This skill provides significant value by:

* Enhancing weather applications with critical air quality information
* Supporting health and wellness applications with real-time environmental data
* Enabling location-based services to provide comprehensive environmental insights
* Helping users make informed decisions about outdoor activities and health precautions

Open Source and Community
-------------------------

This skill is part of the OpenClaw project, an open-source initiative with 2.5k stars and 736 forks on GitHub. The project welcomes contributions and maintains active development to ensure reliable, up-to-date air quality data integration.

Conclusion
----------

The IQAir Air Quality Checker skill provides essential environmental intelligence through seamless API integration. Whether you're building health applications, weather services, or location-based tools, this skill delivers accurate, real-time AQI data that helps users understand and respond to air quality conditions in their area.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/atesluks/iqair/SKILL.md>
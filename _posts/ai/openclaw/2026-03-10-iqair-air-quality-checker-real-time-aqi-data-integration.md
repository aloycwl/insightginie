---
layout: post
title: 'IQAir Air Quality Checker: Real-Time AQI Data Integration'
date: '2026-03-10T14:16:18'
categories:
- ai
- openclaw
original_url: https://insightginie.com/iqair-air-quality-checker-real-time-aqi-data-integration/
featured_image: /media/images/8160.jpg
---

<h2>What This Skill Does</h2>
<p>The IQAir Air Quality Checker skill integrates real-time air quality data from the IQAir API into your applications. It provides accurate AQI (Air Quality Index) readings with visual indicators and quality levels for any location worldwide, helping users make informed decisions about outdoor activities and health.</p>
<h2>Core Functionality</h2>
<p>This skill fetches live air quality data from IQAir&#8217;s global network of monitoring stations. When triggered by user queries about air quality, pollution levels, or AQI in specific cities, it returns comprehensive information including the AQI score, emoji-based visual indicators, and descriptive quality levels.</p>
<h3>Primary Use Cases</h3>
<ul>
<li>Answering questions about air quality in specific locations (&#8220;How is the air in Riga?&#8221;)</li>
<li>Providing pollution level information for health-related decisions (&#8220;Is it safe to go outside in Beijing?&#8221;)</li>
<li>Supplementing weather queries with air quality data (&#8220;What&#8217;s the weather in Budapest?&#8221;)</li>
</ul>
<h2>Prerequisites and Setup</h2>
<p>Before using this skill, users must obtain a free IQAir API key:</p>
<ol>
<li>Visit <a href="https://dashboard.iqair.com/personal/api-keys">https://dashboard.iqair.com/personal/api-keys</a></li>
<li>Sign up or sign in to your account</li>
<li>Subscribe to the free Community plan</li>
<li>Copy your API key</li>
<li>Set it as an environment variable: export IQAIR_API_KEY=&#8221;your_key_here&#8221;</li>
</ol>
<h2>Usage Methods</h2>
<h3>By City Name</h3>
<p>The most common usage involves specifying city and country names:</p>
<pre><code>python scripts/get_aqi.py Riga Latvia
python scripts/get_aqi.py London "United Kingdom"
python scripts/get_aqi.py Budapest Hungary
</code></pre>
<h3>By Coordinates</h3>
<p>For maximum reliability, use geographic coordinates:</p>
<pre><code>python scripts/get_aqi.py --lat 56.9496 --lon 24.1052
</code></pre>
<h3>Nearest Location</h3>
<p>Find air quality data based on your current IP location:</p>
<pre><code>python scripts/get_aqi.py --nearest
</code></pre>
<h2>Response Format and Interpretation</h2>
<p>The skill returns formatted output that&#8217;s easy to understand and share:</p>
<pre><code>🟢 19 - Good
Riga, Latvia
</code></pre>
<h3>AQI Level Interpretation</h3>
<ul>
<li><strong>0-50 (🟢 Good)</strong>: Excellent air quality, perfect for outdoor activities</li>
<li><strong>51-100 (🟡 Moderate)</strong>: Acceptable, but sensitive individuals should limit prolonged outdoor exertion</li>
<li><strong>101-150 (🟠 USG)</strong>: Unhealthy for sensitive groups, children and those with respiratory issues should reduce outdoor activities</li>
<li><strong>151-200 (🔴 Unhealthy)</strong>: Everyone may experience health effects, reduce outdoor activities</li>
<li><strong>201-300 (🔶 Very Unhealthy)</strong>: Health alert, avoid outdoor activities</li>
<li><strong>301+ (🟤 Hazardous)</strong>: Emergency conditions, stay indoors</li>
</ul>
<h2>Location Name Handling</h2>
<p>The skill intelligently handles various location name formats:</p>
<ul>
<li>Simple city names: &#8220;Riga Latvia&#8221; (state defaults to city)</li>
<li>Cities with spaces: &#8220;London &#8220;United Kingdom&#8221;&#8221; (use quotes for multi-word names)</li>
<li>Detailed locations: &#8220;New York&#8221; &#8220;United States&#8221; &#8220;New York&#8221; (city, country, state)</li>
</ul>
<p>If city lookups fail, the skill automatically falls back to coordinate-based lookup for maximum reliability.</p>
<h2>Technical Implementation</h2>
<p>The skill uses IQAir&#8217;s REST API endpoints to fetch real-time data. For detailed API specifications, endpoints, and error handling procedures, refer to the comprehensive documentation in references/api.md.</p>
<h2>Rate Limits and Best Practices</h2>
<p>The free Community plan includes:</p>
<ul>
<li>5 calls per minute</li>
<li>500 calls per day</li>
<li>10,000 calls per month</li>
</ul>
<p>To avoid hitting rate limits, implement caching mechanisms and avoid making repeated calls for the same location within short time periods. Consider storing recent results and only refreshing data when necessary.</p>
<h2>Integration Benefits</h2>
<p>This skill provides significant value by:</p>
<ul>
<li>Enhancing weather applications with critical air quality information</li>
<li>Supporting health and wellness applications with real-time environmental data</li>
<li>Enabling location-based services to provide comprehensive environmental insights</li>
<li>Helping users make informed decisions about outdoor activities and health precautions</li>
</ul>
<h2>Open Source and Community</h2>
<p>This skill is part of the OpenClaw project, an open-source initiative with 2.5k stars and 736 forks on GitHub. The project welcomes contributions and maintains active development to ensure reliable, up-to-date air quality data integration.</p>
<h2>Conclusion</h2>
<p>The IQAir Air Quality Checker skill provides essential environmental intelligence through seamless API integration. Whether you&#8217;re building health applications, weather services, or location-based tools, this skill delivers accurate, real-time AQI data that helps users understand and respond to air quality conditions in their area.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/atesluks/iqair/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/atesluks/iqair/SKILL.md</a></p>

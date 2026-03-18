---
layout: post
title: 'OpenClaw Short Video Copywriter Skill: Generate Viral Content for Chinese
  Social Media'
date: '2026-03-18T19:17:07+00:00'
categories:
- ai
- openclaw
original_url: https://insightginie.com/openclaw-short-video-copywriter-skill-generate-viral-content-for-chinese-social-media/
featured_image: /media/images/8148.jpg
---

<h2>Introduction to OpenClaw Short Video Copywriter Skill</h2>
<p>The OpenClaw Short Video Copywriter skill is a powerful tool designed to help content creators generate viral short video copy for popular Chinese social media platforms. This skill automates the process of creating engaging hooks, body content, hashtags, and publishing tips tailored to each platform&#8217;s unique audience and style.</p>
<h2>Supported Platforms</h2>
<p>The skill supports four major Chinese social media platforms:</p>
<ul>
<li><strong>Douyin (抖音)</strong>: Known for trendy, fast-paced, and viral content</li>
<li><strong>Xiaohongshu (小红书)</strong>: Focused on authentic lifestyle content and product reviews</li>
<li><strong>Kuaishou (快手)</strong>: Features down-to-earth, relatable content for everyday users</li>
<li><strong>Bilibili (B站)</strong>: Popular for in-depth, niche content within various communities</li>
</ul>
<h2>How to Use the Skill</h2>
<h3>Interactive Mode</h3>
<p>The easiest way to use the skill is through the interactive command line interface:</p>
<pre><code>npx short-video-copywriter
</code></pre>
<h3>API Mode</h3>
<p>For programmatic use, you can import and use the skill in your JavaScript/TypeScript projects:</p>
<pre><code class="language-javascript">import { generateShortVideoCopy } from 'short-video-copywriter';

// Generate copy for Xiaohongshu
const result = await generateShortVideoCopy({
  topic: "职场穿搭",
  platform: "xiaohongshu",
  tone: "亲和",
  length: "short"
});
</code></pre>
<h2>Input Options</h2>
<p>The skill accepts several configurable options:</p>
<ul>
<li><strong>topic</strong>: The video topic or theme (required)</li>
<li><strong>platform</strong>: Target platform (douyin/xiaohongshu/kuaishou/bilibili)</li>
<li><strong>tone</strong>: Writing style (professional/casual/humor/heartwarming)</li>
<li><strong>length</strong>: Copy length (short/medium/long)</li>
</ul>
<h2>Output Format</h2>
<p>The skill returns a structured JSON object with:</p>
<ul>
<li><strong>hook</strong>: Attention-grabbing opening line</li>
<li><strong>body</strong>: Main content text</li>
<li><strong>hashtags</strong>: Array of relevant hashtags</li>
<li><strong>tips</strong>: Publishing suggestions and best practices</li>
</ul>
<h2>Examples</h2>
<h3>Xiaohongshu Product Review</h3>
<p>For a budget-friendly face mask review on Xiaohongshu:</p>
<pre><code class="language-javascript">{
  topic: "平价面膜测评",
  platform: "xiaohongshu",
  tone: "亲和"
}
</code></pre>
<p>Output:</p>
<pre><code class="language-json">{
  "hook": "救命！30块的面膜竟然吊打大牌？！",
  "body": "...",
  "hashtags": ["#平价护肤", "#面膜测评", "#学生党"],
  "tips": "建议晚8点发布，互动率更高"
}
</code></pre>
<h3>Douyin Vlog</h3>
<p>For a humorous apartment rental guide on Douyin:</p>
<pre><code class="language-javascript">{
  topic: "租房攻略",
  platform: "douyin",
  tone: "幽默"
}
</code></pre>
<p>Output:</p>
<pre><code class="language-json">{
  "hook": "租房血泪史！建议收藏！",
  "body": "...",
  "hashtags": ["#租房", "#避坑", "#租房攻略"],
  "tips": "配合热门BGM效果更好"
}
</code></pre>
<h2>Environment Variables</h2>
<p>The skill requires an OpenAI API key for AI-powered content generation:</p>
<pre><code>OPENAI_API_KEY=your_api_key_here
</code></pre>
<h2>Best Practices</h2>
<p>To maximize the effectiveness of your short video copy:</p>
<ol>
<li><strong>Hook First</strong>: The first 3 seconds are critical for capturing attention</li>
<li><strong>Platform Match</strong>: Use platform-specific slang and trends</li>
<li><strong>Hashtags</strong>: Use 3-5 relevant tags for discoverability</li>
<li><strong>Call to Action</strong>: End with engagement prompts to boost interaction</li>
</ol>
<h2>Conclusion</h2>
<p>The OpenClaw Short Video Copywriter skill is an invaluable tool for content creators looking to produce viral short video content across Chinese social media platforms. By leveraging AI-powered copywriting and platform-specific knowledge, creators can save time while producing high-quality, engaging content that resonates with their target audience.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/user520512/short-video-copywriter/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/user520512/short-video-copywriter/SKILL.md</a></p>

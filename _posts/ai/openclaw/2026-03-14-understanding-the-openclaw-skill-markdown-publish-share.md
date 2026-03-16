---
layout: post
title: 'Understanding the OpenClaw Skill: markdown-publish-share'
date: '2026-03-14T05:16:29'
categories:
- ai
- openclaw
original_url: https://insightginie.com/understanding-the-openclaw-skill-markdown-publish-share/
featured_image: /media/images/8151.jpg
---

<h2>Introduction to OpenClaw Skill: markdown-publish-share</h2>
<p>The OpenClaw skill <code>markdown-publish-share</code> is a powerful tool designed to facilitate the publishing of markdown content with enhanced features such as mermaid diagrams, KaTex, and code blocks. This skill is particularly useful for creating and sharing Software Architecture diagrams, mathematical derivations, and comprehensive system documentation.</p>
<h2>Key Features of markdown-publish-share</h2>
<p>The <code>markdown-publish-share</code> skill offers several key features that make it a versatile tool for developers and technical writers:</p>
<ul>
<li><strong>Support for Mermaid Diagrams</strong>: Users can create complex diagrams such as flowcharts, sequence diagrams, and component diagrams using Mermaid syntax.</li>
<li><strong>KaTex Integration</strong>: The skill supports KaTex for rendering mathematical expressions and equations directly within the markdown content.</li>
<li><strong>Code Block Support</strong>: Developers can include code blocks with syntax highlighting, making it easier to share code snippets and examples.</li>
<li><strong>Shareable Links</strong>: After publishing, users receive a shareable link to the rendered document, allowing for easy distribution and collaboration.</li>
</ul>
<h2>How to Use markdown-publish-share</h2>
<p>Using the <code>markdown-publish-share</code> skill involves sending a POST request to the AutEng API endpoint. Here’s a step-by-step guide on how to use this skill:</p>
<h3>Basic Usage</h3>
<p>To publish markdown content, you need to send a JSON payload to the following endpoint:</p>
<pre><code class="language-plaintext">https://auteng.ai/api/tools/docs/publish-markdown/
</code></pre>
<p>The JSON payload should include the following fields:</p>
<ul>
<li><code>markdown</code> (required): The markdown content you wish to publish.</li>
<li><code>title</code> (optional): The title of the document.</li>
<li><code>expires_hours</code> (optional): The number of hours after which the document will expire.</li>
</ul>
<h3>Example Command</h3>
<p>Here’s an example of how to use the <code>curl</code> command to publish markdown content:</p>
<pre><code class="language-bash">curl -sS -X POST "https://auteng.ai/api/tools/docs/publish-markdown/" \
-H "Content-Type: application/json" \
-d @- << 'JSON'
{
  "markdown": "# API Test\n\nHello from curl.",
  "title": "API Test",
  "expires_hours": 24
}
JSON
</code></pre>
<h3>Extracting the Share URL</h3>
<p>To extract only the share URL from the response, you can use the following command:</p>
<pre><code class="language-bash">curl -sS -X POST "https://auteng.ai/api/tools/docs/publish-markdown/" \
-H "Content-Type: application/json" \
-d '{"markdown":"# Hello\n\nPublished from curl."}' \
| jq -r '.share_url'
</code></pre>
<h3>Compact Success Payload</h3>
<p>To extract a compact success payload, you can use the following command:</p>
<pre><code class="language-bash">curl -sS -X POST "https://auteng.ai/api/tools/docs/publish-markdown/" \
-H "Content-Type: application/json" \
-d '{"markdown":"# Hello\n\nPublished from curl."}' \
| jq '{title, share_url, expires_at}'
</code></pre>
<h2>Error Handling</h2>
<p>It’s important to note that any response without a <code>share_url</code> should be treated as an error. In such cases, the full JSON body should be displayed to help diagnose the issue.</p>
<h2>Conclusion</h2>
<p>The OpenClaw skill <code>markdown-publish-share</code> is an invaluable tool for anyone looking to publish and share markdown content with advanced features like mermaid diagrams, KaTex, and code blocks. By leveraging the AutEng API, users can easily create, publish, and distribute their documents, making it an essential tool for software architects, developers, and technical writers.</p>
<p>For more detailed documentation and examples, visit the <a href="https://auteng.ai/llms.txt">AutEng documentation</a>.</p>
<p>Skill can be found at: <a href="https://github.com/openclaw/skills/tree/main/skills/operator-auteng-ai/markdown-publish-share/SKILL.md">https://github.com/openclaw/skills/tree/main/skills/operator-auteng-ai/markdown-publish-share/SKILL.md</a></p>

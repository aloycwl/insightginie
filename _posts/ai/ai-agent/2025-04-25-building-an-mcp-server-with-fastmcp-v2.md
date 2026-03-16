---
layout: post
title: Building an MCP Server with FastMCP v2
date: '2025-04-25T05:17:14'
categories:
- ai
- ai-agent
original_url: https://insightginie.com/building-an-mcp-server-with-fastmcp-v2/
featured_image: /media/images/2504251316.avif
---

<p>In the rapidly evolving landscape of AI development, integrating external tools and resources into large language models (LLMs) has become a pivotal aspect of enhancing their capabilities. The Model Context Protocol (MCP) offers a standardized approach to achieve this integration, allowing LLMs to seamlessly interact with custom tools, APIs, and data sources. FastMCP v2, a Pythonic framework for building MCP servers, simplifies this process, enabling developers to create robust and efficient servers with minimal boilerplate code.​</p>

<p>FastMCP v2 introduces several enhancements over its predecessor, including support for proxying and composing servers, as well as the ability to generate servers from OpenAPI specifications or FastAPI objects. These features streamline the development process, making it easier to build and deploy MCP servers tailored to specific use cases.​</p>

<p><strong>Setting Up Your Development Environment</strong></p>

<p>To begin building an MCP server with FastMCP v2, you&#8217;ll need to set up your development environment. Start by creating a new directory for your project and navigating into it:​</p>

<pre class="wp-block-preformatted">bashCopyEdit<code>mkdir my_mcp_server
cd my_mcp_server
</code></pre>

<p>Next, create and activate a virtual environment:​</p>

<pre class="wp-block-preformatted">bashCopyEdit<code>python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
</code></pre>

<p>With the virtual environment activated, install FastMCP v2:​</p>

<pre class="wp-block-preformatted">bashCopyEdit<code>pip install fastmcp
</code></pre>

<p><strong>Creating Your First MCP Server</strong></p>

<p>Now that your environment is set up, you can begin creating your MCP server. Create a new Python file, <code>server.py</code>, and import the necessary modules:​</p>

<pre class="wp-block-preformatted">pythonCopyEdit<code>from fastmcp import FastMCP
import math
</code></pre>

<p>Instantiate the FastMCP server:​</p>

<pre class="wp-block-preformatted">pythonCopyEdit<code>mcp = FastMCP(name="Calculator Server")
</code></pre>

<p>Define a simple tool, such as an addition function, using the <code>@mcp.tool()</code> decorator:​</p>

<pre class="wp-block-preformatted">pythonCopyEdit<code>@mcp.tool()
def add(a: int, b: int) -&gt; int:
    """Add two numbers."""
    return a + b
</code></pre>

<p>Expose a resource that returns a personalized greeting:​</p>

<pre class="wp-block-preformatted">pythonCopyEdit<code>@mcp.resource("greeting://{name}")
def get_greeting(name: str) -&gt; str:
    """Return a personalized greeting."""
    return f"Hello, {name}!"
</code></pre>

<p>Finally, run the server:​</p>

<pre class="wp-block-preformatted">pythonCopyEdit<code>if __name__ == "__main__":
    mcp.run(transport="stdio")
</code></pre>

<p>This basic server defines a tool for adding two numbers and a resource for generating personalized greetings. The <code>transport="stdio"</code> argument specifies that the server will communicate via standard input and output, making it suitable for local testing and development.​</p>

<p><strong>Testing Your MCP Server</strong></p>

<p>To test your server locally, you can use the MCP Inspector, a graphical user interface that allows you to interact with your MCP server. Run the server using the following command:</p>

<pre class="wp-block-preformatted">bashCopyEdit<code>fastmcp run server.py
</code></pre>

<p>This command starts the server and provides a URL to access the MCP Inspector. Open the URL in your web browser, and you&#8217;ll be able to test the <code>add</code> tool and the <code>get_greeting</code> resource by providing the appropriate inputs.​</p>

<p><strong>Integrating with Large Language Models</strong></p>

<p>Once your MCP server is up and running, you can integrate it with large language models like Claude or Cursor. These models can call the tools and resources exposed by your server, enabling them to perform computations or retrieve data dynamically. For example, you can prompt the model to use the <code>add</code> tool to calculate the sum of two numbers or to use the <code>get_greeting</code> resource to generate a personalized message.​</p>

<p>This integration allows you to extend the functionality of LLMs, enabling them to interact with real-time data and perform complex tasks that go beyond their built-in capabilities.​</p>

<p><strong>Conclusion</strong></p>

<p>Building an MCP server with FastMCP v2 provides a powerful and efficient way to integrate custom tools and resources into large language models. By following the steps outlined in this guide, you can create a server that exposes your desired functionalities and interacts seamlessly with LLMs. Whether you&#8217;re building a calculator, a weather service, or any other application, FastMCP v2 offers the tools and flexibility to bring your ideas to life.​</p>

<p>For more detailed information and advanced features, refer to the official FastMCP documentation and explore the community resources available on GitHub.</p>

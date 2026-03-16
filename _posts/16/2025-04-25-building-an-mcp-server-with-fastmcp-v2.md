---
layout: post
title: "Building an MCP Server with FastMCP v2"
date: 2025-04-25T13:17:14
categories: [16]
original_url: https://insightginie.com/building-an-mcp-server-with-fastmcp-v2
---

In the rapidly evolving landscape of AI development, integrating external tools and resources into large language models (LLMs) has become a pivotal aspect of enhancing their capabilities. The Model Context Protocol (MCP) offers a standardized approach to achieve this integration, allowing LLMs to seamlessly interact with custom tools, APIs, and data sources. FastMCP v2, a Pythonic framework for building MCP servers, simplifies this process, enabling developers to create robust and efficient servers with minimal boilerplate code.​

FastMCP v2 introduces several enhancements over its predecessor, including support for proxying and composing servers, as well as the ability to generate servers from OpenAPI specifications or FastAPI objects. These features streamline the development process, making it easier to build and deploy MCP servers tailored to specific use cases.​

**Setting Up Your Development Environment**

To begin building an MCP server with FastMCP v2, you’ll need to set up your development environment. Start by creating a new directory for your project and navigating into it:​

```
bashCopyEditmkdir my_mcp_server
cd my_mcp_server
```

Next, create and activate a virtual environment:​

```
bashCopyEditpython -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

With the virtual environment activated, install FastMCP v2:​

```
bashCopyEditpip install fastmcp
```

**Creating Your First MCP Server**

Now that your environment is set up, you can begin creating your MCP server. Create a new Python file, `server.py`, and import the necessary modules:​

```
pythonCopyEditfrom fastmcp import FastMCP
import math
```

Instantiate the FastMCP server:​

```
pythonCopyEditmcp = FastMCP(name="Calculator Server")
```

Define a simple tool, such as an addition function, using the `@mcp.tool()` decorator:​

```
pythonCopyEdit@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b
```

Expose a resource that returns a personalized greeting:​

```
pythonCopyEdit@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Return a personalized greeting."""
    return f"Hello, {name}!"
```

Finally, run the server:​

```
pythonCopyEditif __name__ == "__main__":
    mcp.run(transport="stdio")
```

This basic server defines a tool for adding two numbers and a resource for generating personalized greetings. The `transport="stdio"` argument specifies that the server will communicate via standard input and output, making it suitable for local testing and development.​

**Testing Your MCP Server**

To test your server locally, you can use the MCP Inspector, a graphical user interface that allows you to interact with your MCP server. Run the server using the following command:

```
bashCopyEditfastmcp run server.py
```

This command starts the server and provides a URL to access the MCP Inspector. Open the URL in your web browser, and you’ll be able to test the `add` tool and the `get_greeting` resource by providing the appropriate inputs.​

**Integrating with Large Language Models**

Once your MCP server is up and running, you can integrate it with large language models like Claude or Cursor. These models can call the tools and resources exposed by your server, enabling them to perform computations or retrieve data dynamically. For example, you can prompt the model to use the `add` tool to calculate the sum of two numbers or to use the `get_greeting` resource to generate a personalized message.​

This integration allows you to extend the functionality of LLMs, enabling them to interact with real-time data and perform complex tasks that go beyond their built-in capabilities.​

**Conclusion**

Building an MCP server with FastMCP v2 provides a powerful and efficient way to integrate custom tools and resources into large language models. By following the steps outlined in this guide, you can create a server that exposes your desired functionalities and interacts seamlessly with LLMs. Whether you’re building a calculator, a weather service, or any other application, FastMCP v2 offers the tools and flexibility to bring your ideas to life.​

For more detailed information and advanced features, refer to the official FastMCP documentation and explore the community resources available on GitHub.
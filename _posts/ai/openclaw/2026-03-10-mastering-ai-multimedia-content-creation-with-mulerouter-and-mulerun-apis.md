---
layout: post
title: "Mastering AI Multimedia Content Creation with MuleRouter and MuleRun APIs"
date: 2026-03-10T14:45:35
categories: [24854]
original_url: https://insightginie.com/mastering-ai-multimedia-content-creation-with-mulerouter-and-mulerun-apis
---

Understanding the MuleRouter Skill
----------------------------------

The MuleRouter skill is a powerful tool that allows users to create and manipulate multimedia content using advanced AI models through MuleRouter or MuleRun APIs. This skill opens up possibilities for generating images and videos from text prompts, transforming existing images into videos, and editing videos with AI-powered tools. It's designed to work seamlessly with Python 3.10 or later, requiring either the uv package manager or pip, along with internet access to the MuleRouter or MuleRun API endpoints.

Key Features of the MuleRouter Skill
------------------------------------

1. **Multimodal Content Generation**: Create images and videos from text prompts
2. **Image-to-Video Conversion**: Transform static images into dynamic videos
3. **Advanced Video Editing**: Utilize AI for video editing tasks
4. **Wide Model Support**: Access various AI models like Wan2.6, Veo3, and Sora2
5. **MuleRouter API Integration**: Leverage the power of MuleRouter's multimodal APIs

Setting Up the MuleRouter Skill
-------------------------------

Before using the skill, you need to configure your environment properly:

### Step 1: Environment Variables

You can set environment variables to configure your API connection:

```
export MULEROUTER_BASE_URL="https://api.mulerouter.ai"  
export MULEROUTER_API_KEY="your-api-key"
```

Or alternatively, if you prefer to use MuleRun:

```
export MULEROUTER_SITE="mulerun"  
export MULEROUTER_API_KEY="your-api-key"
```

### Step 2: Local Configuration

Alternatively, you can create a .env file in your working directory with the same configurations. Remember that the MULEROUTER\_BASE\_URL takes priority over MULEROUTER\_SITE if both are set.

Using the MuleRouter Skill
--------------------------

### Quick Start Guide

Here's a simple walkthrough of how to use the skill:

1. **List Available Models**: Run `uv run python scripts/list_models.py` to see what models you can work with
2. **Check Model Parameters**: Use `uv run python models/alibaba/wan2.6-t2v/generation.py --list-params` to understand the parameters for a specific model
3. **Generate Content**:
   * Text-to-Video: `uv run python models/alibaba/wan2.6-t2v/generation.py --prompt "A cat walking through a garden"`
   * Text-to-Image: `uv run python models/alibaba/wan2.6-t2i/generation.py --prompt "A serene mountain lake"`
   * Image-to-Video: `uv run python models/alibaba/wan2.6-i2v/generation.py --prompt "Gentle zoom in" --image "https://example.com/photo./media/images/jpg"`
4. **Important Note on Image Input**: When working with images, it's preferred to use local file paths rather than base64 encoded images. The skill automatically converts local file paths to base64.

Advanced Usage Tips
-------------------

For optimal performance, consider the following:

* For image generation models, a suggested timeout is 5 minutes, while video generation models might need up to 15 minutes.
* When working with video models, setting the fps parameter to values above 15 can lead to out-of-memory errors.
* The –stream parameter is available for models that support streaming responses.

Conclusion
----------

The MuleRouter skill empowers users to create and manipulate multimedia content using state-of-the-art AI models. By following the setup instructions and utilizing the provided commands, you can unlock a world of creative possibilities for image and video generation, transformation, and editing. With its support for various AI models and integration with MuleRouter APIs, this skill is a valuable tool for content creators and developers alike.

Remember to consult the referenced documentation for more detailed information about API configuration, CLI options, and complete model specifications to get the most out of the MuleRouter skill.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/misaka43fd/mulerouter-skills/SKILL.md>
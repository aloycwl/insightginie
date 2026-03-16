---
layout: post
title: "How to Use the VLM Run CLI Skill for Advanced Image and Video Processing"
date: 2026-03-10T06:45:53
categories: [24854]
original_url: https://insightginie.com/how-to-use-the-vlm-run-cli-skill-for-advanced-image-and-video-processing
---

Understanding the VLM Run CLI Skill for OpenClaw: Advanced Image and Video Processing
=====================================================================================

In the rapidly evolving world of artificial intelligence, the ability to process and understand visual content has become increasingly important. The [VLM Run CLI Skill](https://github.com/openclaw/skills/blob/main/skills/skills/spillai/vlmrun-cli-skill/SKILL.md) for OpenClaw leverages the power of the Orion visual AI agent to provide a versatile tool for handling images, videos, and documents through natural language interactions.

What is the VLM Run CLI Skill?
------------------------------

The VLM Run CLI Skill is a command-line interface tool that allows users to interact with the Orion visual AI agent. Developed by VLM Run, this skill offers various functionalities, including image understanding, object detection, Optical Character Recognition (OCR), video summarization, document extraction, image generation, and visual AI chat. Essentially, it prevents the need to dive deep into complex APIs or programming, offering an intuitive way to process visual content via natural language prompts.

Installation and Setup
----------------------

To get started with the VLM Run CLI Skill, you need to set up a virtual environment and install the necessary dependencies:

```
uv venv && source .venv/bin/activate
uv pip install "vlmrun[cli]"
```

Ensure you have Python 3.8 or higher and pip to manage Python packages.

Environment Variables
---------------------

For the CLI to function correctly, you need to set the following environment variables:

* **VLMRUN\_API\_KEY**: Your VLM Run API key, which is required to access the service.
* **VLMRUN\_BASE\_URL**: Optional; this specifies the base URL of the service (default: `https://agent.vlm.run/v1`).
* **VLMRUN\_CACHE\_DIR**: Optional; this sets the cache directory for artifacts (default: `~/.vlmrun/cache/artifacts/`).

You can load these variables from a `.env` file into your environment.

Basic Command Structure
-----------------------

The primary command to interact with the Orion visual AI agent is:

```
vlmrun chat "" -i input.jpg [options]
```

Here, `<prompt>` is your text query for the task at hand, and `input.jpg` is the input file. This command supports several options to customize its behavior:

Options and Flags
-----------------

The VLM Run CLI Skill offers various options to tailor your interactions:

* `-p, --prompt`: Specify the prompt text, file path, or use standard input.
* `-i, --input`: Provide input files, which can be images, videos, or documents (repeatable for multiple files).
* `-o, --output`: Define the artifact directory for saving generated content (default: `~/.vlmrun/cache/artifacts/`).
* `-m, --model`: Select the model to use (`vlmrun-orion-1:fast`, `vlmrun-orion-1:auto` (default), `vlmrun-orion-1:pro`).
* `-s, --session`: Continue a previous session using the session ID.
* `-j, --json`: Output raw JSON.
* `-ns, --no-stream`: Disable streaming.
* `-nd, --no-download`: Skip artifact download.

Example Use Cases
-----------------

### Image Processing

You can use the VLM Run CLI to perform various image-related tasks:

```
vlmrun chat "Describe what you see in this image" -i photo.jpg
vlmrun chat "Detect and list all objects visible" -i scene.jpg
vlmrun chat "Extract all text and numbers from this document" -i document.png
vlmrun chat "Compare these two images and describe the differences" -i before.jpg -i after.jpg
```

### Video Analysis

For video analysis, the tool can summarize meetings, extract key moments, and transcribe lectures:

```
vlmrun chat "Summarize the key points discussed in this meeting" -i meeting.mp4
vlmrun chat "Find the top 3 highlight moments and create short clips" -i sports.mp4
vlmrun chat "Transcribe this lecture with timestamps for each section" -i lecture.mp4 --json
```

### Document Extraction

Extract information from documents like invoices and contracts:

```
vlmrun chat "Extract the vendor name, line items, and total amount" -i invoice.pdf --json
vlmrun chat "Summarize the key terms and obligations in this contract" -i contract.pdf
```

### Image Generation

Generate images based on text descriptions using the tool:

```
vlmrun chat "Create a photorealistic image of a cozy cabin in a snowy forest at sunset" -o ./generated
vlmrun chat "Remove the background from this product image and make it transparent" -i product.jpg -o ./output
```

Advanced Usage
--------------

### Continuing Sessions

You can maintain the context of previous sessions by using the session ID with the `-s` flag. This feature keeps past conversations and generated artifacts in context for cohesive workflow:

```
vlmrun chat "Create an iconic scene of a ninja in a forest, practicing his skills with a katana" -i photo.jpg
vlmrun chat "Create a new scene with the same character meditating under a tree" -i photo.jpg -s
```

### Skipping Artifact Download

If you want to avoid downloading artifacts, use the `-nd` flag:

```
vlmrun chat "What objects are visible in this image?" -i photo.jpg -nd
```

Notes and Best Practices
------------------------

* Use the `-o` flag to specify a directory for saving generated artifacts relative to your working directory.
* Without the `-o` flag, artifacts are saved to the default directory `~/.vlmrun/cache/artifacts//`.
* Multiple input files can be uploaded and processed concurrently by specifying them with the `-i` flag.

Conclusion
----------

The VLM Run CLI Skill for OpenClaw is a powerful tool that simplifies the process of working with visual content using natural language commands. Whether you are analyzing images, extracting information from documents, or generating new visual content, this skill provides an intuitive interface to leverage advanced AI capabilities. By understanding the various options and commands available, you can effectively integrate this tool into your workflow to enhance productivity and creativity.

For more detailed information and to stay updated with the latest features, refer to the official [GitHub repository](https://github.com/openclaw/skills/blob/main/skills/skills/spillai/vlmrun-cli-skill/SKILL.md) and documentation.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/spillai/vlmrun-cli-skill/SKILL.md>
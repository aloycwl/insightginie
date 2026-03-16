---
layout: post
title: "Navigating Sogni AI: A Comprehensive Guide to Image and Video Generation with OpenClaw"
date: 2026-03-12T14:47:50
categories: [24854]
original_url: https://insightginie.com/navigating-sogni-ai-a-comprehensive-guide-to-image-and-video-generation-with-openclaw
---

Navigating Sogni AI: A Comprehensive Guide to Image and Video Generation with OpenClaw
======================================================================================

Welcome to the ultimate guide on using OpenClaw’s `sogni-gen` skill for generating images and videos with Sogni AI’s decentralized GPU network. In this article, we’ll explore the capabilities of this powerful tool, provide step-by-step setup instructions, and delve into advanced usage options for both images and videos.

Introduction to Sogni AI and OpenClaw
-------------------------------------

Sogni AI is a decentralized GPU network that allows users to generate images and videos using advanced AI models. OpenClaw, a versatile automation and workflow management system, integrates seamlessly with Sogni AI through the `sogni-gen` skill, making it an excellent choice for creative professionals and developers alike.

Getting Started
---------------

Before diving into the world of AI-generated images and videos, you’ll need to set up the necessary components.

### Step 1: Obtain Sogni AI Credentials

Visit <https://app.sogni.ai/> to create an account and obtain your API key or username and password combination. These credentials will be used to authenticate your requests to the Sogni AI network.

### Step 2: Create Credentials File

Create a credentials file in the `~/.config/sogni` directory. This file will store your Sogni AI credentials securely.

```
mkdir -p ~/.config/sogni
```

```
cat > ~/.config/sogni/credentials << 'EOF'
SOGNI_API_KEY=your_api_key
# or:
# SOGNI_USERNAME=your_username
# SOGNI_PASSWORD=your_password
EOF
```

Set the appropriate permissions for the credentials file:

```
chmod 600 ~/.config/sogni/credentials
```

Alternatively, you can export the environment variables instead of creating a file:

```
export SOGNI_API_KEY=your_api_key
```

```
# or

export SOGNI_USERNAME=your_username

export SOGNI_PASSWORD=your_password
```

### Step 3: Install Dependencies

If you have cloned the OpenClaw repository, navigate to the `path/to/sogni-gen` directory and install the required dependencies:

```
cd /path/to/sogni-gen
```

```
npm i
```

Alternatively, you can install the `sogni-gen` skill directly from npm without cloning the repository:

```
mkdir -p ~/.clawdbot/skills
```

```
cd ~/.clawdbot/skills
```

```
npm i sogni-gen
```

```
ln -sfn node_modules/sogni-gen sogni-gen
```

Filesystem Paths and Overrides
------------------------------

The `sogni-gen` skill uses various default file paths for credentials, configurations, and other resources. You can override these paths using environment variables.

| File Path | Purpose | Override Environment Variable |
| --- | --- | --- |
| ~/.config/sogni/credentials | Credentials file (read) | SOGNI\_CREDENTIALS\_PATH |
| ~/.config/sogni/last-render.json | Last render metadata (read/write) | SOGNI\_LAST\_RENDER\_PATH |
| ~/.openclaw/openclaw.json | OpenClaw config (read) | OPENCLAW\_CONFIG\_PATH |
| ~/.clawdbot/media/inbound | Media listing for --list-media (read) | SOGNI\_MEDIA\_INBOUND\_DIR |
| ~/Downloads/sogni | MCP local result copies (write) | SOGNI\_DOWNLOADS\_DIR (MCP) SOGNI\_MCP\_SAVE\_DOWNLOADS=0 to disable MCP local file writes |

Generating Images
-----------------

The `sogni-gen` skill provides a wide range of options for generating images from text prompts. In its simplest form, you can generate an image and receive a URL:

```
node sogni-gen.mjs "a cat wearing a hat"
```

To save the generated image to a file, use the `-o` or `--output` flag:

```
node sogni-gen.mjs -o /tmp/cat.png "a cat wearing a hat"
```

For scripting purposes, you can request JSON output using the `--json` flag:

```
node sogni-gen.mjs --json "a cat wearing a hat"
```

### Advanced Image Generation Options

The `sogni-gen` skill offers numerous options to customize your image generation experience:

| Flag | Description | Default |
| --- | --- | --- |
| `-m, --model <id>` | Model ID | `z_image_turbo_bf16` |
| `-w, --width <px>` | Width | `512` |
| `-h, --height <px>` | Height | `512` |
| `-n, --count <num>` | Number of images | `1` |
| `-t, --timeout <sec>` | Timeout seconds | `30` |
| `-s, --seed <num>` | Specific seed | `random` |
| `--last-seed` | Reuse seed from last render |  |
| `--seed-strategy <s>` | Seed strategy: `random`|`prompt-hash` | `prompt-hash` |
| `--multi-angle` | Multiple angles LoRA mode (Qwen Image Edit) |  |
| `--angles-360` | Generate 8 azimuths (front -> front-left) |  |
| `--angles-360-video` | Assemble looping 360 mp4 using i2v between angles (requires ffmpeg) |  |
| `--azimuth <key>` | `front`|`front-right`|`right`|`back-right`|`back`|`back-left`|`left`|`front-left` | `front` |
| `--elevation <key>` | `low-angle`|`eye-level`|`elevated`|`high-angle` | `eye-level` |
| `--distance <key>` | `close-up`|`medium`|`wide` | `medium` |
| `--angle-strength <n>` | LoRA strength for multiple\_angles | `0.9` |
| `--angle-description <text>` | Optional subject description |  |
| `--steps <num>` | Override steps (model-dependent) |  |
| `--guidance <num>` | Override guidance (model-dependent) |  |
| `--output-format <f>` | Image output format: `png`|`jpg` | `png` |
| `--sampler <name>` | Sampler (model-dependent) |  |
| `--scheduler <name>` | Scheduler (model-dependent) |  |
| `--lora <id>` | LoRA id (repeatable, edit only) |  |
| `--loras <ids>` | Comma-separated LoRA ids |  |
| `--lora-strength <n>` | LoRA strength (repeatable) |  |
| `--lora-strengths <n>` | Comma-separated LoRA strengths |  |
| `--token-type <type>` | Token type: `spark`|`sogni` | `spark` |
| `-c, --context <path>` | Context image for editing |  |
| `--last-image` | Use last generated image as context/ref |  |
| `-q, --quiet` | No progress output | `false` |

Generating Videos
-----------------

The `sogni-gen` skill also supports video generation through various workflows. To generate a video instead of an image, use the `--video` or `-v` flag:

```
node sogni-gen.mjs --video "a cat wearing a hat"
```

You can specify different video workflows using the `--workflow` flag:

* **t2v**: Text-to-video
* **i2v**: Image-to-video (interpolation between two images)
* **s2v**: Speech-to-video (requires `--ref-audio`)
* **ia2v**: Image-and-audio-to-video (requires `--ref` and `--ref-audio`)
* **a2v**: Audio-to-video (requires `--ref` and `--ref-audio`)
* **v2v**: Video-to-video (requires `--ref-video`)
* **animate-move**: Animate with movement (requires `--ref`)
* **animate-replace**: Animate with object replacement (requires `--ref` and `--sam2-coordinates`)

### Advanced Video Generation Options

The following options are available for video generation:

| Flag | Description | Default |
| --- | --- | --- |
| `--output-format <f>` | Video output format: `mp4`|`mov` | `mp4` |
| `--fps <num>` | Frames per second (video) | `16` |
| `--duration <sec>` | Duration in seconds (video) | `5` |
| `--frames <num>` | Override total frames (video) |  |
| `--auto-resize-assets` | Auto-resize video assets | `true` |
| `--no-auto-resize-assets` | Disable auto-resize |  |
| `--estimate-video-cost` | Estimate video cost and exit (requires `--steps`) |  |
| `--steps <num>` | Override steps (model-dependent) |  |
| `--guidance <num>` | Override guidance (model-dependent) |  |
| `--sampler <name>` | Sampler (model-dependent) |  |
| `--scheduler <name>` | Scheduler (model-dependent) |  |
| `--lora <id>` | LoRA id (repeatable, edit only) |  |
| `--loras <ids>` | Comma-separated LoRA ids |  |
| `--lora-strength <n>` | LoRA strength (repeatable) |  |
`--lora-strengths <n>` Comma-separated LoRA strengths |  || `--ref <path>` | Reference image for video or photobooth face | Required |
| `--ref-end <path>` | End frame for i2v interpolation |  |
| `--ref-audio <path>` | Reference audio for s2v |  |
| `--ref-video <path>` | Reference video for animate/v2v workflows |  |
| `--controlnet-name <name>` | ControlNet type for v2v: canny|pose|depth|detailer |  |
| `--controlnet-strength <n>` | ControlNet strength for v2v (0.0-1.0) | `0.8` |
| `--sam2-coordinates <coords>` | SAM2 click coords for animate-replace (x,y or x1,y1;x2,y2) |  |
| `--trim-end-frame` | Trim last frame for seamless video stitching |  |
| `--first-frame-strength <n>` | Keyframe strength for start frame (0.0-1.0) |  |
| `--last-frame-strength <n>` | Keyframe strength for end frame (0.0-1.0) |  |

### Specialized Video Generation Modes

#### Photobooth Mode

Photobooth mode enables face transfer using InstantID and SDXL Turbo. To activate this mode, use the `--photobooth` flag. You'll need to provide a reference image containing a face using the `--ref` flag.

The following flags are specific to photobooth mode:

| Flag | Description | Default |
| --- | --- | --- |
| `--cn-strength <n>` | ControlNet strength | `0.8` |
| `--cn-guidance-end <n>` | ControlNet guidance end point | `0.3` |

#### MCP (Multi-Claw Partitioning)

MCP allows you to split large tasks across multiple agents. The `sogni-gen` skill supports MCP through the `SOGNI_MCP_SAVE_DOWNLOADS` environment variable, which determines whether local file copies of MCP results should be saved. To disable local file writes, set the variable to `0`.

#### Post-Processing with FFmpeg

The `sogni-gen` skill includes built-in support for FFmpeg, enabling you to perform post-processing tasks on generated videos:

* **Extract Last Frame:** Use the `--extract-last-frame` flag to save the last frame of a video as an image.
* **Concatenate Videos:** Use the `--concat-videos` flag to combine multiple video clips into a single video file.

### Video Generation Examples

Here are some examples of video generation using the `sogni-gen` skill:

* **Text to Video:**

  ```
  node sogni-gen.mjs --video "a cat wearing a hat"
  ```
* **Image to Video:**

  ```
  node sogni-gen.mjs --video --workflow i2v --ref start.png --ref-end end.png "a cat transitioning"
  ```
* **Speech to Video:**

  ```
  node sogni-gen.mjs --video --workflow s2v --ref-audio audio.mp3 "a cat listening"
  ```
* **Photobooth Mode:**

  ```
  node sogni-gen.mjs --video --photobooth --ref face.jpg "a futuristic cityscape"
  ```

Checking Token Balances
-----------------------

To monitor your SPARK or SOGNI token balances, use the `--balance` or `--balances` flag:

```
node sogni-gen.mjs --balance
```

For JSON output:

```
node sogni-gen.mjs --json --balance
```

Listing Recent Media
--------------------

To list recent inbound media, use the `--list-media` flag. You can filter by media type (images, audio, or all):

```
node sogni-gen.mjs --list-media
```

```
node sogni-gen.mjs --list-media images
```

```
node sogni-gen.mjs --list-media audio
```

Advanced Configuration
----------------------

When installed as an OpenClaw plugin, the `sogni-gen` skill reads default configurations from the `~/.openclaw/openclaw.json` file. You can customize various aspects of the skill, including default models, workflows, and settings for specific models.

```
{  
  "plugins": {  
    "entries": {  
      "sogni-gen": {  
        "enabled": true,  
        "config": {  
          "defaultImageModel": "z_image_turbo_bf16",  
          "defaultEditModel": "qwen_image_edit_2511_fp8_lightning",  
          "defaultPhotoboothModel": "coreml-sogniXLturbo_alpha1_ad",  
          "videoModels": {  
            "t2v": "wan_v2.2-14b-fp8_t2v_lightx2v",  
            "i2v": "wan_v2.2-14b-fp8_i2v_lightx2v",  
            "s2v": "wan_v2.2-14b-fp8_s2v_lightx2v",  
            "ia2v": "ltx2-19b-fp8_ia2v_distilled",  
            "a2v": "ltx2-19b-fp8_a2v_distilled",  
            "animate-move": "wan_v2.2-14b-fp8_animate-move_lightx2v",  
            "animate-replace": "wan_v2.2-14b-fp8_animate-replace_lightx2v",  
            "v2v": "ltx2-19b-fp8_v2v_distilled"  
          },  
          "defaultVideoWorkflow": "t2v",  
          "defaultNetwork": "fast",  
          "defaultTokenType": "spark",  
          "seedStrategy": "prompt-hash",  
          "modelDefaults": {  
            "flux1-schnell-fp8": {  
              "steps": 4,  
              "guidance": 3.5  
            },  
            "flux2_dev_fp8": {  
              "steps": 20,  
              "guidance": 7.5  
            }  
          },  
          "defaultWidth": 768,  
          "defaultHeight": 768,  
          "defaultCount": 1,  
          "defaultFps": 16,  
          "defaultDurationSec": 5,  
          "defaultImageTimeoutSec": 30  
        }  
      }  
    }  
  }  
}
```

Troubleshooting
---------------

If you encounter issues while using the `sogni-gen` skill, consider the following troubleshooting steps:

1. **Check Credentials:** Ensure that your Sogni AI credentials are correctly configured in either the `~/.config/sogni/credentials` file or as environment variables.
2. **Verify Dependencies:** Confirm that all required dependencies, including Node.js and FFmpeg, are installed and accessible in your system PATH.
3. **Review System Requirements:** Make sure your system meets the minimum requirements for running the `sogni-gen` skill. Some features, such as multiple angle generation and video assembly, require FFmpeg and significant processing power.
4. **Check API Status:** Visit the Sogni AI website or API status page to ensure that the service is operational and not experiencing any outages or maintenance.

Future Developments and Updates
-------------------------------

The `sogni-gen` skill and Sogni AI platform are continually evolving to provide users with new features, improved performance, and enhanced capabilities. Stay up-to-date with the latest developments by:

* Visiting the [OpenClaw skills repository](https://github.com/openclaw/skills/tree/main/skills/krunkosaurus/sogni-gen) on GitHub
* Following the [Sogni AI website](https://sogni.ai) and blog
* Joining the Sogni AI community on social media platforms and forums

About the Author
----------------

This blog post was generated by an AI WordPress content generator. The goal is to provide informative and engaging content that helps users get the most out of OpenClaw's `sogni-gen` skill and Sogni AI's decentralized GPU network.

We hope this guide has been helpful, and we encourage you to explore the many possibilities that AI-powered image and video generation can offer. Happy creating!

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/krunkosaurus/sogni-gen/SKILL.md>
---
layout: post
title: "How to Create Explainable Videos: OpenClaw&#8217;s Remotion-Excalidraw-TTS Skill Explained"
date: 2026-03-06T19:45:45
categories: [24854]
original_url: https://insightginie.com/how-to-create-explainable-videos-openclaws-remotion-excalidraw-tts-skill-explained
---

In the ever-evolving landscape of digital content creation, tools that allow users to transform static diagrams into dynamic explainer videos are becoming increasingly popular. OpenClaw's [remotion-excalidraw-tts skill](https://github.com/openclaw/skills/blob/main/skills/jack4world/remotion-excalidraw-tts/SKILL.md) is one such tool that bridges the gap between illustration and animation, providing a seamless way to create narrated videos from [Excalidraw](https://excalidraw.com/) diagrams.

Gist of the Skill
-----------------

This skill automates the process of generating a professional-quality explainer video from an Excalidraw diagram and a plaintext voiceover script. The output is an MP4 video rendered directly from the diagram with voiceover synthesized using local text-to-speech tools or cloud-based services. Incorporating Remotion's rendering capabilities, this toolchain can produce polished results for explanatory content.

Tools Integrated
----------------

The remotion-excalidraw-tts skill integrates several key components to streamline explainer video creation:

1. [Remotion](https://www.remotion.dev/): A powerful React-based framework for compositing video graphics programmatically.
2. [Excalidraw](https://excalidraw.com/): A digital whiteboard application that outputs collaborative sketches in a JSON format.
3. **Text-to-Speech:**
   * **Local macOS**: Utilizes macOS's built-in `say` command for offline TTS conversion.
   * **OpenAI**: Supports generation of human-like voiceovers using OpenAI's text-to-speech model.
   * **ElevenLabs**: Delivers ultra-realistic TTS capabilities with voice cloning technology.
4. [FFmpeg](https://ffmpeg.org/): A universal multimedia framework used to manipulate audio and video files.

Quick Start Guide
-----------------

Setting up your first video with the remotion-excalidraw-tts skill involves a straightforward command. Start by creating an Excalidraw diagram (.excalidraw) and a corresponding text file for voiceover content.

Execute this command in your terminal:

```
python3 skills/remotion-excalidraw-tts/scripts/make_video.py \  
--diagram /absolute/path/to/diagram.excalidraw \  
--voiceover-text /absolute/path/to/voiceover.txt \  
--out /absolute/path/to/out.mp4
```

This will generate an MP4 file with a narration based on the provided script.

### Customizing with Storyboard JSON

To refine the visual storytelling, options like camera movement, focusing on specific elements, and adding subtitles can be managed through a `storyboard.json` file.

Here's a basic example of what this JSON file should contain:

```
{  
  "scenes": [  
    {  
      "name": "intro",  
      "durationSec": 10,  
      "subtitle": "很多智能体隔天就失忆。",  
      "cameraFrom": {"x": 0, "y": 0, "scale": 1},  
      "cameraTo": {"x": 0, "y": 0, "scale": 1},  
      "focus": {  
        "x": 140, "y": 120,   
        "width": 1640,  
        "height": 340,  
        "label": "问题"  
      }  
    }  
  ]  
}
```

By defining

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/jack4world/remotion-excalidraw-tts/SKILL.md>
---
layout: post
title: "Anima Avatar &#8211; Interactive Video Generation Engine"
date: 2026-03-08T21:18:38
categories: [24854]
original_url: https://insightginie.com/anima-avatar-interactive-video-generation-engine
---

Anima Avatar – Interactive Video Generation Engine
--------------------------------------------------

Anima Avatar is a sophisticated interactive video generation engine that creates dynamic, high-quality videos featuring a character named Shutiao. This system combines advanced text-to-speech, AI-powered image generation, and professional video composition to produce engaging video content with synchronized audio and expressive character animations.

### Core Capabilities

The Anima Avatar system offers several powerful features that make it stand out as a video generation solution:

* **True Voice**: Utilizes Fish Audio API for realistic speech synthesis that brings text to life with natural-sounding voices
* **Dynamic Sprites**: Automatically selects from a library of over 30 sprites representing different emotions and actions
* **Smart Director**: Manages parallel rendering, audio synchronization, and video composition using FFmpeg
* **Pro Delivery**: Uploads generated videos as native streams to Feishu for direct playback with accurate duration

### System Architecture

The engine is built with a modular structure that separates concerns and enables efficient processing:

* **src/director.js**: The core engine that generates frames, audio, and final video composition
* **src/send\_video\_pro.js**: Handles transcoding, duration calculation, and Feishu upload
* **src/batch\_generator.js**: Creates sprite variants using Gemini image generation
* **assets/sprites/**: Library of 1920×1080 PNG sprite files
* **assets/production\_plan.csv**: Asset registry with 25 predefined sprites
* **assets/manifest.json**: Sprite metadata reference
* **output/**: Directory for generated videos

### Getting Started Guide

Setting up Anima Avatar requires several steps to prepare your custom character and background assets. Here's a comprehensive guide to get you started:

#### Step 1: Prepare Your Character Image

You'll need a standalone character illustration with a transparent background in PNG format. This character will serve as the foundation for all generated sprites. The image should be at least 1920×1080 resolution, and a full-body illustration works best for creating dynamic animations.

#### Step 2: Prepare Your Background Image

Choose a background scene that will appear behind your character in every video frame. This could be a cherry blossom garden, classroom, city street, or any environment that fits your content. The background should also be at least 1920×1080 resolution.

#### Step 3: Fuse Character and Background

This crucial step merges your character onto the background using Gemini AI image generation. The AI creates a natural-looking composite that handles lighting, shadows, and blending automatically. You can use either:

* **Method A (Recommended)**: Use Gemini directly with your background image as input, character image as reference, and a prompt describing the desired composition
* **Method B**: Use the built-in compose script for a simple mechanical overlay

Save the output as `assets/sprites/shutiao_base.png`.

#### Step 4: Plan Sprite Variants

Open `assets/production_plan.csv` and customize it according to your needs. The CSV file contains columns for ID, Emotion, Variant, Description, Filename, Prompt, and Status. You can add, remove, or modify rows to create the exact sprite library you need.

#### Step 5: Generate Sprite Variants

This step uses Gemini AI to create expression variants. For each pending row in your CSV, the system sends your base sprite plus the prompt to Gemini, asking it to change only the expression or pose while keeping everything else identical. The process includes:

* Reading the production plan CSV
* Finding all rows with Status=Pending
* Generating images through the Gemini API
* Saving PNG files to the sprites directory
* Updating CSV status to Done
* Waiting 10 seconds between generations to respect API rate limits

#### Step 6: Verify and Test

After generation, verify that all sprites exist and run a quick test using the preview command. This ensures everything works correctly before creating full videos.

### Technical Requirements

The system has specific dependencies and requirements:

#### System Dependencies

FFmpeg is required for video processing. Installation varies by platform:

* macOS: `brew install ffmpeg`
* Linux: `sudo apt install ffmpeg`
* Windows: Download and install FFmpeg, then add to PATH

#### Node Dependencies

Navigate to the skill folder and install dependencies:

```
cd skills/anima
npm install
```

The only native dependency is sharp, which ships with prebuilt binaries for all major platforms via N-API. It doesn't require recompilation when Node versions change.

#### External Services

The system requires API keys for two external services:

1. **Fish Audio (TTS)**: Generates realistic voice audio from text. Used by src/director.js for the generateAudio() function. Get a key from https://fish.audio/dashboard/api and set FISH\_AUDIO\_KEY and FISH\_AUDIO\_REF\_ID environment variables.
2. **Gemini API (Image Generation)**: Generates sprite variants using Google Gemini. Used by src/batch\_generator.js. Set GEMINI\_API\_KEY in your environment.

### Usage and Customization

Once set up, Anima Avatar provides flexible options for creating interactive videos. You can customize scripts, add new emotions, adjust timing, and integrate the system into larger applications. The modular design makes it easy to extend functionality or modify the generation pipeline.

The system is particularly well-suited for educational content, interactive storytelling, virtual presentations, and any application where a dynamic, expressive character can enhance engagement and communication.

### Sprite Library Management

The sprite system uses a CSV-based approach to manage variants. Each sprite is categorized by emotion (Happy, Angry, Shy, Think, Sad, Action, Base) and can have multiple variants. The system automatically selects appropriate sprites based on emotion tags in your script, creating a seamless viewing experience where the character's expressions match the content.

The default library includes 25 sprites covering common emotions and actions, but you can expand this collection as needed by adding new rows to the CSV and generating corresponding images.

### Audio Integration

Fish Audio provides high-quality text-to-speech synthesis that integrates seamlessly with the video generation pipeline. The system automatically synchronizes audio with visual elements, ensuring that mouth movements, expressions, and gestures match the spoken content. Multiple voice models are supported, allowing you to choose the perfect voice for your character.

### Video Composition

The Smart Director component handles all aspects of video composition using FFmpeg. It manages parallel rendering of frames, audio synchronization, text overlay, and final video assembly. The system produces professional-quality 16:9 videos suitable for various platforms and use cases.

Whether you're creating educational content, interactive presentations, or entertainment videos, Anima Avatar provides a powerful, flexible solution for bringing your characters to life through dynamic, engaging video content.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/hmyaoyuan/anima/SKILL.md>
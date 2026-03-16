---
layout: post
title: "How to Send Native iMessage Voice Replies with OpenClaw"
date: 2026-03-15T11:16:40
categories: [24854]
original_url: https://insightginie.com/how-to-send-native-imessage-voice-replies-with-openclaw
---

What This Skill Does
--------------------

The iMessage Voice Reply skill enables you to send native iMessage voice messages using local Kokoro TTS. Voice messages appear as inline playable bubbles with waveforms—identical to voice messages recorded directly in Messages.app. This skill is perfect for voice-to-voice iMessage conversations or when you want to send audio responses.

Key Features
------------

* Generates native iMessage voice bubbles (CAF/Opus format) that play inline with waveforms
* Zero cost—all TTS processing runs locally on your device
* Requires BlueBubbles channel configured in OpenClaw
* Supports multiple voices and languages

How It Works
------------

Your text response → Kokoro TTS (local) → afconvert (native Apple encoder) → CAF/Opus → BlueBubbles → iMessage voice bubble

Setup
-----

Run the setup script to install dependencies and download Kokoro models:

```
bash ${baseDir}/scripts/setup.sh
```

This installs kokoro-onnx, soundfile, numpy, and downloads Kokoro models (~136MB) to ~/.cache/kokoro-onnx/.

Generating and Sending a Voice Reply
------------------------------------

### Step 1: Generate Audio

Write your response text to a temp file, then generate the voice reply:

```
echo "Your response text here" > /tmp/voice_text.txt
${baseDir}/.venv/bin/python ${baseDir}/scripts/generate_voice_reply.py --text-file /tmp/voice_text.txt --output /tmp/voice_reply.caf
```

Alternatively, pass text directly:

```
${baseDir}/.venv/bin/python ${baseDir}/scripts/generate_voice_reply.py --text "Your response text here" --output /tmp/voice_reply.caf
```

Available options:  
– `--voice af_heart` — Kokoro voice (default: af\_heart)  
– `--speed 1.15` — Playback speed (default: 1.15)  
– `--lang en-us` — Language code (default: en-us)

### Step 2: Send via BlueBubbles

Use the message tool with these critical parameters for native voice bubble rendering:

```
{
  "action": "sendAttachment",
  "channel": "bluebubbles",
  "target": "+1XXXXXXXXXX",
  "path": "/tmp/voice_reply.caf",
  "filename": "Audio Message.caf",
  "contentType": "audio/x-caf",
  "asVoice": true
}
```

All three parameters are required:  
– `filename="Audio Message.caf"`  
– `contentType="audio/x-caf"`  
– `asVoice=true`

Voice Options
-------------

Available voices by language:

| Language | Female | Male |
| --- | --- | --- |
| English | af\_heart ⭐ | am\_puck |
| Spanish | ef\_dora | em\_alex |
| French | ff\_siwis |  |
| Japanese | jf\_alpha | jm\_beta |
| Chinese | zf\_xiaobei | zm\_yunjian |

When to Use Voice Replies
-------------------------

Reply with a voice message when:

* The user sent you a voice message (voice-for-voice)
* The user explicitly asks for an audio/voice response

Always include a text reply alongside the voice message for accessibility.

Audio Format
------------

On macOS: CAF container, Opus codec, 48kHz mono, 32kbps—encoded by Apple's native afconvert. Identical to what Messages.app produces.

Fallback: MP3 via ffmpeg (works but may not render as native voice bubble on all iMessage versions).

Cost
----

$0. Kokoro TTS runs entirely locally. No API calls for voice generation.

Troubleshooting
---------------

Voice message shows as file attachment — Ensure all three parameters are set: filename=”Audio Message.caf”, contentType=”audio/x-caf”, asVoice=true.

First word clipped — The script prepends 150ms silence automatically. If still clipped, increase the silence pad in the script.

Kokoro model not found — Run bash ${baseDir}/scripts/setup.sh.

afconvert not found — Only available on macOS. Script falls back to ffmpeg/MP3 on Linux.

Security Note
-------------

The Python script uses argparse and subprocess.run with list arguments (no shell=True). Input is handled safely within the script. When calling from a shell, prefer –text-file for untrusted input to avoid shell metacharacter issues.

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/bolander72/imessage-voice-reply/SKILL.md>
---
layout: post
title: "CosyVoice3 TTS: Local Text-to-Speech on macOS with Voice Cloning"
date: 2026-03-10T06:17:48
categories: [24854]
original_url: https://insightginie.com/cosyvoice3-tts-local-text-to-speech-on-macos-with-voice-cloning
---

What is CosyVoice3?
-------------------

CosyVoice3 is an advanced local text-to-speech (TTS) system that brings powerful voice synthesis capabilities to macOS devices with Apple Silicon. Built on large language models, it offers high-quality speech generation with support for multiple languages, dialects, and voice cloning features.

### Key Features

* **Multi-language Support**: Chinese, English, Japanese, Korean, German, Spanish, French, Italian, Russian
* **Dialect Support**: 18+ Chinese dialects including Cantonese, Sichuan, Dongbei, Shanghai
* **Voice Cloning**: Clone any voice from just 3-10 seconds of reference audio
* **Cross-lingual Synthesis**: Speak Chinese with an English voice or vice versa
* **Fine-grained Control**: Emotions, speed, volume control through text tags
* **Local Processing**: Runs entirely on your Mac without cloud dependency

Prerequisites
-------------

Before installing CosyVoice3, ensure your system meets these requirements:

* **macOS with Apple Silicon**: M1, M2, or M3 chip required
* **Python 3.10**: The system is tested with this version
* **Conda**: Package management system installed
* **Disk Space**: Approximately 5GB available for models and dependencies

Installation
------------

Follow these steps to install CosyVoice3 on your macOS system:

### Step 1: Navigate to the Scripts Directory

```
cd /Users/lhz/.openclaw/workspace/skills/cosyvoice3/scripts
```

### Step 2: Run the Installation Script

```
bash install.sh
```

This script will automatically:

* Create a conda environment named `cosyvoice`
* Install PyTorch (CPU version optimized for Apple Silicon)
* Install all CosyVoice3 dependencies
* Download the Fun-CosyVoice3-0.5B model (approximately 2GB)

Basic Usage
-----------

### Quick Start Example

```
cd /Users/lhz/.openclaw/workspace/cosyvoice3-repo
export PATH="$HOME/miniconda3/bin:$PATH"
conda activate cosyvoice
python -c "
import sys
sys.path.append('third_party/Matcha-TTS')
from cosyvoice.cli.cosyvoice import AutoModel
import torchaudio
cosyvoice = AutoModel(model_dir='pretrained_models/Fun-CosyVoice3-0.5B')
for i, j in enumerate(cosyvoice.inference_zero_shot(
'你好，这是CosyVoice3语音合成测试。',
'希望你以后能够做的比我还好呦。<|endofprompt|',  # Important: This tag is required!
'asset/zero_shot_prompt.wav'
)):
    torchaudio.save('output.wav', j['tts_speech'], cosyvoice.sample_rate)
    print('Generated: output.wav')
"
```

### Using the TTS Script

The `tts.py` script provides a convenient command-line interface for text-to-speech conversion.

#### Basic TTS with Default Voice

```
cd /Users/lhz/.openclaw/workspace/skills/cosyvoice3/scripts
conda activate cosyvoice
python tts.py "你好，这是一个测试。"
```

#### Voice Cloning with Reference Audio

```
python tts.py "你好，这是克隆的声音。" --reference /path/to/reference.wav
```

#### Cross-lingual Synthesis

```
python tts.py "Hello, this is cross-lingual synthesis." --reference asset/zero_shot_prompt.wav --lang en
```

#### Speed Control

```
python tts.py "这是一段快速的语音。" --speed 1.5
```

#### Save to Specific Path

```
python tts.py "你好。" --output ~/Desktop/greeting.wav
```

Advanced Features
-----------------

### Voice Cloning

Clone voices from short audio samples (3-10 seconds):

```
from cosyvoice.cli.cosyvoice import AutoModel
import torchaudio
cosyvoice = AutoModel(model_dir='pretrained_models/Fun-CosyVoice3-0.5B')
# Clone voice and generate
for i, j in enumerate(cosyvoice.inference_zero_shot(
'这是克隆后的声音在说话。',
'Reference text transcription',
'/path/to/reference.wav'
)):
    torchaudio.save('cloned.wav', j['tts_speech'], cosyvoice.sample_rate)
```

### Fine-Grained Control with Text Tags

CosyVoice3 supports special tags for controlling prosody:

* **Laughter**: "他突然[laughter]笑了起来[laughter]。"
* **Breathing**: "他说完这句话[breath]，深吸一口气。"
* **Strong Emphasis**: "这是**非常重要**的。"
* **Combined Effects**: "在面对挑战时，他展现了非凡的**勇气**与**智慧**[breath]。"

### Dialect Support

Use instruct mode for dialect synthesis:

```
cosyvoice = AutoModel(model_dir='pretrained_models/CosyVoice-300M-Instruct')
for i, j in enumerate(cosyvoice.inference_instruct(
'你好，这是测试语音。',
'中文男',
'用四川话说这句话<|endofprompt|>'
)):
    torchaudio.save('sichuan.wav', j['tts_speech'], cosyvoice.sample_rate)
```

Available Assets
----------------

The repository includes several reference audio files in the `cosyvoice3-repo/asset/` directory:

* `zero_shot_prompt.wav`: Default Chinese female voice
* `cross_lingual_prompt.wav`: English prompt for cross-lingual synthesis

Troubleshooting
---------------

### Model Not Found

If you encounter "model not found" errors, download the models manually:

```
cd /Users/lhz/.openclaw/workspace/cosyvoice3-repo
export PATH="$HOME/miniconda3/bin:$PATH"
conda activate cosyvoice
python -c "
from modelscope import snapshot_download
snapshot_download('FunAudioLLM/Fun-CosyVoice3-0.5B-2512', local_dir='pretrained_models/Fun-CosyVoice3-0.5B')
"
```

### Memory Issues

For long texts, split them into sentences:

```
text = "很长的文本..."
sentences = text.split('。')
for sent in sentences:
    if sent.strip():
        # Process each sentence
```

### Audio Format Requirements

Reference audio should meet these specifications:

* **Format**: WAV or MP3
* **Sample Rate**: 16kHz or higher (automatically resampled)
* **Duration**: 3-10 seconds optimal
* **Content**: Clear speech with minimal background noise

Model Files
-----------

Available models are located in `cosyvoice3-repo/pretrained_models/`:

* `Fun-CosyVoice3-0.5B/`: Main model (recommended)
* `CosyVoice2-0.5B/`: Previous version
* `CosyVoice-300M/`: Lighter model
* `CosyVoice-300M-SFT/`: SFT version
* `CosyVoice-300M-Instruct/`: Instruct version

Performance Notes
-----------------

* First inference takes approximately 30 seconds due to model warmup
* Subsequent inferences are significantly faster
* Apple Silicon uses CPU mode (no CUDA support)
* Real-time factor (RTF) is approximately 0.3-0.5 on M-series chips
* Model files are cached locally after first download

Resources
---------

* **Installation Script**: `install.sh` - Sets up the environment
* **Main TTS Script**: `tts.py` - Command-line interface
* **Model Downloader**: `download_models.py` - Downloads pretrained models

References
----------

* [CosyVoice GitHub Repository](https://github.com/openclaw/skills/tree/main/skills/lhuaizhong/cosyvoice3-macos)
* [Fun-CosyVoice3 Demo](https://github.com/FunAudioLLM/CosyVoice)

Skill can be found at: <https://github.com/openclaw/skills/tree/main/skills/lhuaizhong/cosyvoice3-macos/SKILL.md>
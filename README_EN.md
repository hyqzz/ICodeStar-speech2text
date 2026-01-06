# 🎤 Speech-to-Text Tool

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green.svg)](https://github.com/openai/whisper)
[![CUDA](https://img.shields.io/badge/CUDA-GPU%20Accelerated-yellow.svg)](https://developer.nvidia.com/cuda-toolkit)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE)

**Intelligent Speech Recognition Tool Based on OpenAI Whisper | GPU Accelerated | Chinese Speech-to-Text**

[English](README_EN.md) | [简体中文](README.md)

</div>

## 📖 Project Overview

This is a powerful **Speech-to-Text** tool based on OpenAI's open-source Whisper model. It can quickly and accurately convert MP3, WAV, and other audio files into text files. It supports **Simplified Chinese speech recognition** and provides **NVIDIA CUDA GPU acceleration**, which can improve conversion speed by 10-50x.

### 🔑 Keywords
`speech recognition` `speech-to-text` `ASR` `automatic speech recognition` `Whisper` `Chinese ASR` `audio transcription` `MP3 to text` `WAV to text` `GPU acceleration` `CUDA` `voice transcription` `语音识别` `语音转文字` `中文语音识别`

## ✨ Features

- 🎵 **Multiple Format Support**: Supports MP3, WAV, M4A, FLAC, OGG, and other audio formats
- 🇨🇳 **Chinese Recognition**: Uses OpenAI Whisper model, optimized for Simplified Chinese speech recognition
- ⚡ **GPU Acceleration**: Automatically detects and uses NVIDIA CUDA GPU, speed improvement of 10-50x
- 🎯 **Multiple Model Options**: Provides 5 model sizes (tiny/base/small/medium/large) to balance speed and accuracy
- 🖥️ **Graphical Interface**: Simple and easy-to-use Tkinter GUI with real-time GPU status and conversion progress
- 💾 **Auto Save**: Automatically saves as UTF-8 encoded Simplified Chinese TXT file after conversion
- 🔄 **Model Caching**: Intelligently caches loaded models to avoid repeated loading and improve efficiency

## 🚀 Quick Start

### System Requirements

- **Python**: 3.8 or higher
- **Operating System**: Windows / Linux / macOS
- **Disk Space**: 
  - tiny model: ~75 MB
  - base model: ~150 MB (recommended)
  - small model: ~500 MB
  - medium model: ~1.5 GB
  - large model: ~3 GB
- **GPU (Optional but Recommended)**: NVIDIA graphics card + CUDA driver (10-50x speed improvement)

### Installation

#### 1. Clone Repository
```bash
git clone https://github.com/yourusername/ICodeStar-speech2text.git
cd ICodeStar-speech2text
```

#### 2. Install Dependencies

**CPU Version (Basic)**:
```bash
pip install -r requirements.txt
```

**GPU Version (Recommended, Much Faster)**:

To use NVIDIA CUDA GPU acceleration, first install the CUDA version of PyTorch:

1. Visit [PyTorch Official Website](https://pytorch.org/get-started/locally/) to find the installation command for your CUDA version
2. For example, CUDA 11.8:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   pip install openai-whisper
   ```
3. For example, CUDA 12.1:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
   pip install openai-whisper
   ```

**Note**:
- The Whisper model will be automatically downloaded on first run, which may take a few minutes
- The program automatically detects GPU, and will use GPU acceleration if CUDA GPU is detected
- GPU version requires NVIDIA graphics card and CUDA driver support

### Usage

1. **Run the Program**:
   ```bash
   python speechtotext.py
   ```

2. **GPU Status Display**: After startup, the program will display GPU status:
   - ✓ CUDA GPU detected: Will use GPU acceleration (fast)
   - ⚠ No CUDA GPU detected: Will use CPU (slower)

3. **Select Audio File**: Click the "Select Audio File" button to choose MP3, WAV, or other audio files to convert

4. **Select Model Size** (Optional):
   - **tiny**: Fastest, lower accuracy (suitable for quick preview)
   - **base**: Fast, medium accuracy (**Recommended**, balances speed and accuracy)
   - **small**: Medium speed, good accuracy
   - **medium**: Slower, good accuracy
   - **large**: Slowest, highest accuracy (suitable for high-quality requirements)

5. **Start Conversion**: Click the "Convert to Text" button to start conversion

6. **View Results**: After conversion, the Simplified Chinese text file will be automatically saved in the same directory as the audio file

## 📝 Usage Guide

### Model Selection Guide

| Model | Speed | Accuracy | Use Case | Model Size |
|-------|-------|----------|----------|------------|
| tiny | ⚡⚡⚡⚡⚡ | ⭐⭐ | Quick preview, testing | ~75 MB |
| base | ⚡⚡⚡⚡ | ⭐⭐⭐ | **Daily use (Recommended)** | ~150 MB |
| small | ⚡⚡⚡ | ⭐⭐⭐⭐ | High-quality transcription | ~500 MB |
| medium | ⚡⚡ | ⭐⭐⭐⭐⭐ | Professional transcription | ~1.5 GB |
| large | ⚡ | ⭐⭐⭐⭐⭐ | Highest accuracy | ~3 GB |

### Performance Comparison

- **CPU Mode**: base model processes 1 minute of audio in approximately 30-60 seconds
- **GPU Mode**: base model processes 1 minute of audio in approximately 1-3 seconds (**10-50x speed improvement**)

## ⚠️ Notes

- **GPU Acceleration**: If NVIDIA CUDA GPU is detected, the program will automatically use GPU acceleration, improving conversion speed by 10-50x
- **Simplified Chinese Output**: The program defaults to Simplified Chinese output, using `language="zh"` and `initial_prompt` to ensure recognition results match Chinese conventions
- **First-time Download**: The first time using a model requires downloading from the internet, please ensure network connection is available
- **Model Selection**: Larger models have higher recognition accuracy but slower processing speed. It is recommended to use **base** or **small** models to balance speed and accuracy
- **GPU Version**: GPU version requires installing CUDA version of PyTorch, see installation instructions for details
- **File Encoding**: Output files use UTF-8 encoding, supporting all Chinese characters

## 🛠️ Tech Stack

- **Speech Recognition Engine**: [OpenAI Whisper](https://github.com/openai/whisper)
- **Deep Learning Framework**: [PyTorch](https://pytorch.org/) (CUDA supported)
- **GUI Framework**: Tkinter (Python standard library)
- **Programming Language**: Python 3.8+

## 📂 Project Structure

```
ICodeStar-speech2text/
├── speechtotext.py      # Main program file
├── requirements.txt     # Dependency list
├── README.md           # Chinese documentation
├── README_EN.md        # English documentation
└── doc/
    └── 修改说明.md     # Development documentation
```

## 🤝 Contributing

Issues and Pull Requests are welcome!

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## ⭐ Star History

If this project is helpful to you, please give it a Star ⭐!

## 🔗 Related Links

- [OpenAI Whisper Official Repository](https://github.com/openai/whisper)
- [PyTorch Official Website](https://pytorch.org/)
- [CUDA Downloads](https://developer.nvidia.com/cuda-downloads)

---

<div align="center">

**Made with ❤️ by ICodeStar**

If you find it useful, please give it a ⭐ Star!

</div>


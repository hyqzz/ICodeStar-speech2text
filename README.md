# 🎤 语音转文本工具 (Speech-to-Text Tool)

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green.svg)](https://github.com/openai/whisper)
[![CUDA](https://img.shields.io/badge/CUDA-GPU%20加速-yellow.svg)](https://developer.nvidia.com/cuda-toolkit)
[![License](https://img.shields.io/badge/License-MIT-orange.svg)](LICENSE)

**基于 OpenAI Whisper 的智能语音识别工具 | 支持 GPU 加速 | 中文语音转文字**

[English](README_EN.md) | [中文简体](README.md)

</div>

## 📖 项目简介

这是一个功能强大的**语音转文本（Speech-to-Text）**工具，基于 OpenAI 开源的 Whisper 模型，可以将 MP3、WAV 等音频文件快速准确地转换为文本文件。支持**简体中文语音识别**，并提供 **NVIDIA CUDA GPU 加速**功能，转换速度可提升 10-50 倍。

### 🔑 关键词
`语音识别` `语音转文字` `ASR` `自动语音识别` `Whisper` `中文语音识别` `音频转文本` `MP3转文字` `WAV转文字` `GPU加速` `CUDA` `语音转录` `speech-to-text` `speech recognition` `Chinese ASR`

## ✨ 功能特点

- 🎵 **多格式支持**：支持 MP3、WAV、M4A、FLAC、OGG 等多种音频格式
- 🇨🇳 **中文识别**：使用 OpenAI Whisper 模型，专为简体中文语音识别优化
- ⚡ **GPU 加速**：自动检测并使用 NVIDIA CUDA GPU，速度提升 10-50 倍
- 🎯 **多模型选择**：提供 5 种模型大小（tiny/base/small/medium/large），平衡速度和精度
- 🖥️ **图形界面**：简洁易用的 Tkinter GUI，实时显示 GPU 状态和转换进度
- 💾 **自动保存**：转换完成后自动保存为 UTF-8 编码的简体中文 TXT 文件
- 🔄 **模型缓存**：智能缓存已加载的模型，避免重复加载，提升效率

## 安装依赖

### CPU版本（基础）
```bash
pip install -r requirements.txt
```

### GPU版本（推荐，速度更快）
如需使用NVIDIA CUDA GPU加速，请安装CUDA版本的PyTorch：

1. 访问 [PyTorch官网](https://pytorch.org/get-started/locally/) 查看适合您CUDA版本的安装命令
2. 例如 CUDA 11.8：
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   pip install openai-whisper
   ```
3. 例如 CUDA 12.1：
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
   pip install openai-whisper
   ```

**注意**：
- 首次运行时会自动下载Whisper模型，可能需要几分钟时间
- 程序会自动检测GPU，如果检测到CUDA GPU会自动使用GPU加速
- GPU版本需要NVIDIA显卡和CUDA驱动支持

## 🚀 快速开始

### 系统要求

- **Python**: 3.8 或更高版本
- **操作系统**: Windows / Linux / macOS
- **磁盘空间**: 
  - tiny 模型：约 75 MB
  - base 模型：约 150 MB（推荐）
  - small 模型：约 500 MB
  - medium 模型：约 1.5 GB
  - large 模型：约 3 GB
- **GPU（可选但推荐）**: NVIDIA 显卡 + CUDA 驱动（速度提升 10-50 倍）

### 安装步骤

#### 1. 克隆仓库
```bash
git clone https://github.com/yourusername/ICodeStar-speech2text.git
cd ICodeStar-speech2text
```

#### 2. 安装依赖

**CPU 版本（基础）**：
```bash
pip install -r requirements.txt
```

**GPU 版本（推荐，速度更快）**：

如需使用 NVIDIA CUDA GPU 加速，请先安装 CUDA 版本的 PyTorch：

1. 访问 [PyTorch 官网](https://pytorch.org/get-started/locally/) 查看适合您 CUDA 版本的安装命令
2. 例如 CUDA 11.8：
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
   pip install openai-whisper
   ```
3. 例如 CUDA 12.1：
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
   pip install openai-whisper
   ```

### 使用方法

1. **运行程序**：
   ```bash
   python speechtotext.py
   ```

2. **程序启动后会显示 GPU 状态**：
   - ✓ 已检测到 CUDA GPU：将使用 GPU 加速（速度快）
   - ⚠ 未检测到 CUDA GPU：将使用 CPU（速度较慢）

3. **选择音频文件**：点击"选择音频文件"按钮，选择要转换的 MP3、WAV 或其他音频文件

4. **选择模型大小**（可选）：
   - **tiny**：最快，精度较低（适合快速预览）
   - **base**：较快，精度中等（**推荐**，平衡速度和精度）
   - **small**：中等，精度较好
   - **medium**：较慢，精度好
   - **large**：最慢，精度最高（适合高质量要求）

5. **开始转换**：点击"转换为文本"按钮开始转换

6. **查看结果**：转换完成后，简体中文文本文件会自动保存到音频文件同目录下

## 📝 使用说明

### 模型选择建议

| 模型 | 速度 | 精度 | 适用场景 | 模型大小 |
|------|------|------|----------|----------|
| tiny | ⚡⚡⚡⚡⚡ | ⭐⭐ | 快速预览、测试 | ~75 MB |
| base | ⚡⚡⚡⚡ | ⭐⭐⭐ | **日常使用（推荐）** | ~150 MB |
| small | ⚡⚡⚡ | ⭐⭐⭐⭐ | 高质量转录 | ~500 MB |
| medium | ⚡⚡ | ⭐⭐⭐⭐⭐ | 专业转录 | ~1.5 GB |
| large | ⚡ | ⭐⭐⭐⭐⭐ | 最高精度 | ~3 GB |

### 性能对比

- **CPU 模式**：base 模型处理 1 分钟音频约需 30-60 秒
- **GPU 模式**：base 模型处理 1 分钟音频约需 1-3 秒（**速度提升 10-50 倍**）

## ⚠️ 注意事项

- **GPU 加速**：如果检测到 NVIDIA CUDA GPU，程序会自动使用 GPU 加速，转换速度可提升 10-50 倍
- **简体中文输出**：程序默认输出简体中文，通过 `language="zh"` 和 `initial_prompt` 确保识别结果符合中文习惯
- **首次下载**：首次使用某个模型时需要从网络下载，请确保网络连接正常
- **模型选择**：模型越大，识别精度越高，但处理速度越慢。建议使用 **base** 或 **small** 模型，在速度和精度之间取得平衡
- **GPU 版本**：GPU 版本需要安装 CUDA 版本的 PyTorch，详见安装说明
- **文件编码**：输出文件使用 UTF-8 编码，支持所有中文字符

## 🛠️ 技术栈

- **语音识别引擎**: [OpenAI Whisper](https://github.com/openai/whisper)
- **深度学习框架**: [PyTorch](https://pytorch.org/) (支持 CUDA)
- **GUI 框架**: Tkinter (Python 标准库)
- **编程语言**: Python 3.8+

## 📂 项目结构

```
ICodeStar-speech2text/
├── speechtotext.py      # 主程序文件
├── requirements.txt     # 依赖包列表
├── README.md           # 中文说明文档
├── README_EN.md        # 英文说明文档
└── doc/
    └── 修改说明.md     # 开发文档
```

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

## 📄 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

## ⭐ Star History

如果这个项目对您有帮助，请给个 Star ⭐ 支持一下！

## 🔗 相关链接

- [OpenAI Whisper 官方仓库](https://github.com/openai/whisper)
- [PyTorch 官网](https://pytorch.org/)
- [CUDA 下载](https://developer.nvidia.com/cuda-downloads)

---

<div align="center">

**Made with ❤️ by ICodeStar**

如果觉得有用，请给个 ⭐ Star！

</div>



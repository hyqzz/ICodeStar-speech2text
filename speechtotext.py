import asyncio
import logging
import os
import threading
from tkinter import Tk, filedialog, Label, StringVar, ttk, messagebox

try:
    import whisper
    import torch
except ImportError:
    whisper = None
    torch = None

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] %(levelname)s %(message)s",
)

# Whisper模型大小选项（从小到大，速度从慢到快，精度从低到高）
MODEL_SIZE_MAP = {
    "tiny（最快，精度较低）": "tiny",
    "base（较快，精度中等）": "base",
    "small（中等，精度较好）": "small",
    "medium（较慢，精度好）": "medium",
    "large（最慢，精度最高）": "large",
}

# 全局变量存储模型实例，避免重复加载
_loaded_model = None
_model_name = None


def check_cuda_available():
    """检查CUDA是否可用。"""
    if torch is None:
        return False
    return torch.cuda.is_available()


def get_device():
    """获取可用的计算设备（优先CUDA GPU）。"""
    if check_cuda_available():
        device = "cuda"
        gpu_name = torch.cuda.get_device_name(0)
        logging.info("检测到CUDA GPU：%s，将使用GPU加速", gpu_name)
        return device, gpu_name
    else:
        logging.info("未检测到CUDA GPU，将使用CPU")
        return "cpu", None


def load_whisper_model(model_size: str, device: str = "cpu"):
    """加载Whisper模型（如果已加载相同模型则复用）。"""
    global _loaded_model, _model_name
    
    if whisper is None:
        raise RuntimeError("未安装 whisper，请先执行：pip install openai-whisper")
    
    # 如果已加载相同模型且设备相同，直接返回
    if _loaded_model is not None and _model_name == model_size:
        logging.info("复用已加载的模型：%s (设备: %s)", model_size, device)
        return _loaded_model
    
    # 加载新模型
    if device == "cuda" and torch is not None and torch.cuda.is_available():
        device_info = f"GPU ({torch.cuda.get_device_name(0)})"
    else:
        device_info = "CPU"
    logging.info("开始加载 Whisper 模型：%s（设备：%s，首次加载可能需要几分钟）", model_size, device_info)
    try:
        _loaded_model = whisper.load_model(model_size, device=device)
        _model_name = model_size
        logging.info("模型加载完成：%s (设备: %s)", model_size, device_info)
        return _loaded_model
    except Exception as e:
        logging.exception("加载模型失败：%s", e)
        raise RuntimeError(f"加载模型失败：{e}")


def select_file():
    """选择MP3文件。"""
    root.filename = filedialog.askopenfilename(
        initialdir="/",
        title="选择MP3文件",
        filetypes=[
            ("音频文件", "*.mp3 *.wav *.m4a *.flac *.ogg"),
            ("MP3文件", "*.mp3"),
            ("所有文件", "*.*"),
        ],
    )
    if root.filename:
        file_size = os.path.getsize(root.filename) / (1024 * 1024)  # MB
        label.config(text=f"已选择文件：{os.path.basename(root.filename)} ({file_size:.2f} MB)")
        logging.info("已选择文件：%s (%.2f MB)", root.filename, file_size)
    else:
        label.config(text="未选择文件，请重试。")
        logging.warning("未选择文件")


def convert_mp3_to_text():
    """将MP3文件转换为文本。"""
    progress["value"] = 0
    root.update_idletasks()
    
    try:
        if not getattr(root, "filename", None):
            label.config(text="请先选择文件。")
            messagebox.showwarning("警告", "请先选择MP3文件！")
            return

        if not os.path.exists(root.filename):
            label.config(text="文件不存在，请重新选择。")
            messagebox.showerror("错误", "文件不存在，请重新选择！")
            return

        # 检查是否安装了whisper
        if whisper is None:
            error_msg = "未安装 whisper 库！\n请执行：pip install openai-whisper"
            label.config(text=error_msg)
            messagebox.showerror("错误", error_msg)
            return

        progress["value"] = 5
        root.update_idletasks()

        # 获取用户选择的模型大小
        model_label = model_var.get().strip() or "base（较快，精度中等）"
        model_size = MODEL_SIZE_MAP.get(model_label, "base")
        
        logging.info("使用模型：%s (%s)", model_label, model_size)

        # 加载模型（在后台线程中执行，避免UI冻结）
        def process_audio():
            try:
                progress["value"] = 10
                root.update_idletasks()
                
                # 检测并获取设备
                device, gpu_name = get_device()
                device_info = f"GPU ({gpu_name})" if gpu_name else "CPU"
                logging.info("使用设备：%s", device_info)
                
                # 加载模型到指定设备
                model = load_whisper_model(model_size, device=device)
                
                progress["value"] = 30
                root.update_idletasks()
                
                logging.info("开始转录音频：%s（设备：%s）", root.filename, device_info)
                status_text = f"正在转录音频（{device_info}），请稍候..."
                label.config(text=status_text)
                
                # 使用whisper进行转录，指定简体中文
                result = model.transcribe(
                    root.filename,
                    language="zh",  # 指定简体中文
                    task="transcribe",  # 转录任务
                    initial_prompt="以下是简体中文的语音转录内容。",  # 引导输出简体中文
                )
                
                progress["value"] = 80
                root.update_idletasks()
                
                # 获取转录文本
                text_content = result["text"].strip()
                
                if not text_content:
                    raise RuntimeError("转录结果为空，可能是音频文件无法识别。")
                
                logging.info("转录完成，文本长度：%d 字符", len(text_content))
                
                # 生成输出文件名
                output_filename = os.path.splitext(os.path.basename(root.filename))[0] + ".txt"
                output_dir = os.path.dirname(root.filename) or os.getcwd()
                output_path = os.path.join(output_dir, output_filename)
                
                # 保存文本文件
                with open(output_path, "w", encoding="utf-8") as f:
                    f.write(text_content)
                
                progress["value"] = 100
                root.update_idletasks()
                
                success_msg = f"转换完成！\n文件已保存至：{os.path.basename(output_path)}"
                label.config(text=success_msg)
                logging.info("文本已保存：%s", output_path)
                messagebox.showinfo("成功", success_msg)
                
            except Exception as e:
                logging.exception("转换失败：%s", e)
                error_msg = f"转换失败：{str(e)}"
                label.config(text=error_msg)
                messagebox.showerror("错误", error_msg)
                progress["value"] = 0
        
        # 在后台线程中执行，避免UI冻结
        thread = threading.Thread(target=process_audio, daemon=True)
        thread.start()

    except Exception as err:
        logging.exception("转换过程出错：%s", err)
        label.config(text=f"转换失败：{err}")
        messagebox.showerror("错误", f"转换失败：{err}")
        progress["value"] = 0


# 设置Tkinter GUI
root = Tk()
root.title("MP3转文本工具")
root.geometry("500x350")

label = Label(root, text="欢迎使用！请选择一个音频文件（MP3/WAV等）。", font=("Arial", 12))
label.pack(pady=10)

model_var = StringVar(value="base（较快，精度中等）")

frame_opts = ttk.Frame(root)
frame_opts.pack(pady=10)

Label(frame_opts, text="模型大小：", font=("Arial", 10)).grid(row=0, column=0, padx=5, pady=5, sticky="e")
combo_model = ttk.Combobox(
    frame_opts,
    textvariable=model_var,
    values=list(MODEL_SIZE_MAP.keys()),
    state="readonly",
    width=30,
)
combo_model.grid(row=0, column=1, padx=5, pady=5, sticky="w")
combo_model.current(1)  # 默认选择base

# 检测并显示GPU状态
gpu_status = ""
if check_cuda_available():
    gpu_name = torch.cuda.get_device_name(0)
    gpu_status = f"\n✓ 已检测到CUDA GPU：{gpu_name}，将使用GPU加速"
else:
    gpu_status = "\n⚠ 未检测到CUDA GPU，将使用CPU（速度较慢）"

# 添加说明标签
info_label = Label(
    root,
    text=f"提示：首次使用需要下载模型，请耐心等待。\n模型越大，精度越高，但速度越慢。{gpu_status}",
    font=("Arial", 9),
    fg="gray",
    justify="left",
)
info_label.pack(pady=5)

progress = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress.pack(pady=10)

button_select = ttk.Button(root, text="选择音频文件", command=select_file)
button_select.pack(pady=5)

button_convert = ttk.Button(root, text="转换为文本", command=convert_mp3_to_text)
button_convert.pack(pady=5)

root.mainloop()



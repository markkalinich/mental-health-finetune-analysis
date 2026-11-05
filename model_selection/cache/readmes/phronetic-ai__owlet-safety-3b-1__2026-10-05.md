---
license: cc-by-4.0
tags:
    - vision
    - video
    - multi-modal
    - safety-detection
model_type: qwen2.5-vl
base_model: Qwen/Qwen2.5-VL-3B-Instruct
library_name: transformers
inference: true
---

# Owlet Safety 1 🚨

`phronetic-ai/owlet-safety-3b-1` is a fine-tuned version of [Qwen2.5-VL-3B-Instruct](https://huggingface.co/Qwen/Qwen2.5-VL-3B-Instruct) for **multi-label safety event detection** in video clips.

This model can identify safety-related activities like:
- `fire`, `smoke`, `fall`, `assault`, `sos`, `theft`, or `none` (if no concern is found).

It is suitable for **video surveillance**, **incident detection**, and **safety monitoring** tasks where **multiple events may occur simultaneously**.

---

## 🏗️ Model Details

- **Base model**: Qwen2.5-VL-3B-Instruct (multi-modal vision-language model)
- **Fine-tuned on**: Domain-specific video clips with multi-label safety annotations
- **LoRA merged**: The adapter weights have been merged into the base model for ease of deployment
- **Labels**: `assault`, `fall`, `fire`, `smoke`, `sos`, `theft`, `none`
- **Input**: Chat-style prompt + video
- **Output**: Comma-separated list of labels present in the video

---

## ⚙️ Hardware & Memory Requirements

To run this model effectively, the following hardware and memory configurations are recommended:

- ✅ **GPU Recommended**:
  - NVIDIA **RTX 4090**, **T4**, or any equivalent GPU with support for bfloat16 or float16
- ✅ **Minimum System RAM**: 16 GB
- ✅ **Model Memory Footprint**:
  - ~**7 GB** VRAM for full-precision (bfloat16/fp16) inference
  - ~**3.8 GB** VRAM with **int8 quantization**
  - ~**2.5 GB** VRAM with **int4 quantization**
- 📈 **Runtime Memory Note**:  
  Inference memory usage depends on:
  - Video **length**
  - Video **resolution/quality**
  - Internally generated **video tensors**
  This can increase VRAM usage beyond the base model load footprint, especially for high-resolution or long-duration videos.

---

## 📦 Installation

You'll need:

```bash
pip install transformers accelerate
```

---

## 🧪 Usage Example

```bash
import torch
from transformers import AutoModelForImageTextToText, AutoProcessor
from qwen_vl_utils import process_vision_info  # custom helper

device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoModelForImageTextToText.from_pretrained(
    "phronetic-ai/owlet-safety-3b-1",
    trust_remote_code=True,
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
processor = AutoProcessor.from_pretrained("phronetic-ai/owlet-safety-3b-1")

messages = [
    {
        "role": "system",
        "content": "You are an expert at analyzing safety-related activities. Given a video, identify all the safety concerns present. Respond with a comma-separated list of labels from this set: assault, fall, fire, smoke, sos, theft, none. If no safety concerns are present, respond with 'none'."
    },
    {
        "role": "user",
        "content": [
            {
                "type": "video",
                "video": "/path/to/video/fire_0.mp4",  # 👈 Change to your video path
                "max_pixels": 360 * 420,
                "fps": 1.0
            },
            {
                "type": "text",
                "text": "Identify safety concerns in this video"
            }
        ]
    }
]

# Format inputs
text = processor.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)
image_inputs, video_inputs = process_vision_info(messages)

inputs = processor(
    text=[text],
    images=image_inputs,
    videos=video_inputs,
    padding=True,
    return_tensors="pt"
).to(device)

# Inference
torch.cuda.empty_cache()
with torch.no_grad():
    generated_ids = model.generate(**inputs, max_new_tokens=128)

# Decode output
generated_ids_trimmed = [
    out_ids[len(in_ids):] for in_ids, out_ids in zip(inputs.input_ids, generated_ids)
]
output_text = processor.batch_decode(
    generated_ids_trimmed,
    skip_special_tokens=True,
    clean_up_tokenization_spaces=False
)

print(output_text)
```

✅ Example Output:

```bash
['fire, smoke']
```

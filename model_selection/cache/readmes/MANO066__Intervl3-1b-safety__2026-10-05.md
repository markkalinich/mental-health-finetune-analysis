---
license: apache-2.0
base_model: OpenGVLab/InternVL3-1B
tags:
- vision
- image-text-to-text
- multimodal
- internvl3
- fine-tuned
- pytorch
language:
- en
pipeline_tag: image-text-to-text
library_name: transformers
---

# InternVL3-1B Fine-tuned for Human Protection Safety Dataset

This is a fine-tuned version of [OpenGVLab/InternVL3-1B](https://huggingface.co/OpenGVLab/InternVL3-1B) trained for enhanced vision-language understanding Human protection saftey dataset tasks.

## 📋 Model Details

- **Model Name**: InternVL3-1B Fine-tuned
- **Base Model**: [OpenGVLab/InternVL3-1B](https://huggingface.co/OpenGVLab/InternVL3-1B)
- **Model Type**: Vision-Language Model (VLM)
- **Architecture**: InternViT Vision Encoder + Qwen2.5 Language Model
- **Training Framework**: PyTorch + Transformers
- **Precision**: bfloat16

## 🚀 Quick Start

```python
import torch
from PIL import Image
import requests
from io import BytesIO
import torchvision.transforms as T
from torchvision.transforms.functional import InterpolationMode
from transformers import AutoModel, AutoTokenizer

# =========================
# CONFIG
# =========================
MODEL_PATH = "MANO066/Intervl3-1b-saftey"
IMAGE_URL = "https://cdn-res.keymedia.com/cdn-cgi/image/f=auto/https://cdn-res.keymedia.com/cms/images/us/069/0305_637985635035710982.jpg"
IMAGE_SIZE = 448

# =========================
# IMAGE PREPROCESS
# =========================
IMAGENET_MEAN = (0.485, 0.456, 0.406)
IMAGENET_STD = (0.229, 0.224, 0.225)

def build_transform(input_size):
    return T.Compose([
        T.Resize((input_size, input_size), interpolation=InterpolationMode.BICUBIC),
        T.ToTensor(),
        T.Normalize(mean=IMAGENET_MEAN, std=IMAGENET_STD)
    ])

def load_image_from_url(url, image_size=448):
    response = requests.get(url, timeout=10)
    image = Image.open(BytesIO(response.content)).convert('RGB')
    transform = build_transform(image_size)
    pixel_values = transform(image).unsqueeze(0)
    return pixel_values

# =========================
# MODEL LOAD
# =========================
print("🚀 Loading model...")
model = AutoModel.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map='cuda:0'
).eval()

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH, trust_remote_code=True, use_fast=False)

# =========================
# SINGLE IMAGE INFERENCE
# =========================
print("🖼️ Downloading image and running inference...")
pixel_values = load_image_from_url(IMAGE_URL, IMAGE_SIZE).to(torch.bfloat16).cuda()

question = "<image>\nIs the first person from the left wearing a safety helmet? Answer only with 'Yes' or 'No'"
generation_config = dict(max_new_tokens=256, do_sample=True)

response = model.chat(tokenizer, pixel_values, question, generation_config)

print("\n=============================")
print(f"🧑‍💻 Question: {question}")
print(f"🤖 Model Response: {response}")
print("=============================")
print(f"🔗 Reference Image: {IMAGE_URL}")
print("=============================\n")


# Install OpenVINO Optimum for export & inference
pip install --upgrade --upgrade-strategy eager "optimum[openvino]"
```


## 🖼️ OpenVINO Export

```bash
optimum-cli export openvino \
  --model MANO066/Intervl3-1b-safety \
  Intervl3-1b-safety \
  --trust-remote-code \
  --weight-format fp16
```

---

## 🖼️ OpenVINO Inference Example

```python
import requests
from PIL import Image
from io import BytesIO
import numpy as np
from pathlib import Path
from IPython.display import display
import openvino_genai as ov_genai

model_dir = "Intervl3-1b-safety"
ov_model = ov_genai.VLMPipeline(model_dir, device="CPU")

config = ov_genai.GenerationConfig()
config.max_new_tokens = 100

def load_image(image_file):
    if isinstance(image_file, str) and image_file.startswith("http"):
        response = requests.get(image_file)
        image = Image.open(BytesIO(response.content)).convert("RGB")
    else:
        image = Image.open(image_file).convert("RGB")
    image_data = np.array(image.getdata()).reshape(1, image.size[1], image.size[0], 3).astype(np.byte)
    return image, ov.Tensor(image_data)

EXAMPLE_IMAGE = Path("example_image1.jpg")
EXAMPLE_IMAGE_URL = "https://huggingface.co/OpenGVLab/InternVL2-2B/resolve/main/examples/image1.jpg"

if not EXAMPLE_IMAGE.exists():
    img_data = requests.get(EXAMPLE_IMAGE_URL).content
    with EXAMPLE_IMAGE.open("wb") as handler:
        handler.write(img_data)

def streamer(subword: str) -> bool:
    print(subword, end="", flush=True)

question = "Please describe the image shortly"
image, image_tensor = load_image(EXAMPLE_IMAGE)
display(image)

print(f"User: {question}\n")
print("Assistant:")
output = ov_model.generate(question, image=image_tensor, generation_config=config, streamer=streamer)
```

---

### ✅ Notes

* PyTorch + Transformers workflow is **GPU optimized**.
* OpenVINO workflow is **CPU optimized**, lightweight, and fast.
* OpenVINO export converts model weights to **FP16**, reducing memory usage.
* Choose the workflow depending on your hardware and inference needs.

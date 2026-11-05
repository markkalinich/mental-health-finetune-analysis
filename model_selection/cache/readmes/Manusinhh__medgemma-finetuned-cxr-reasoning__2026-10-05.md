
---
license: apache-2.0
tags:
  - medical
  - chest-xray
  - reasoning
  - vision-language
  - medgemma
---

# 🧠 MedGEMMA Reasoning Model — Fine-tuned on CXR-10K

This is a fine-tuned version of `google/medgemma-4b-it`, trained on the [CXR-10K Reasoning Dataset](https://huggingface.co/datasets/Manusinhh/cxr-10k-reasoning-dataset) consisting of chest X-ray images paired with step-by-step clinical reasoning.

---

## 🩻 Task

**Multimodal Clinical Reasoning**:  
Given a chest X-ray image, the model generates a step-by-step diagnostic reasoning path covering:

- Lung fields
- Cardiac size
- Mediastinal structures
- Surgical history
- Skeletal findings

---

## 🧪 Example Usage (Inference)

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
import torch

# Load model and processor
model = AutoModelForImageTextToText.from_pretrained("Manusinhh/medgemma-finetuned-cxr-reasoning")
processor = AutoProcessor.from_pretrained("google/medgemma-4b-it")

# Load image
image = Image.open("example.png").convert("RGB")

# Create prompt
messages = [
    {
        "role": "user",
        "content": [
            {"type": "image", "image": image},
            {"type": "text", "text": "Analyze this medical image and provide step-by-step findings."}
        ]
    }
]

# Tokenize and generate
inputs = processor.apply_chat_template(messages, tokenize=True, return_tensors="pt").to(model.device)
with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=300)

print(processor.decode(output[0], skip_special_tokens=True))
````

---

## 📊 Training Details

* **Base model**: `google/medgemma-4b-it`
* **LoRA Fine-tuning**: Used `peft` with low-rank adapters
* **Training set**: 10k chest X-ray samples with reasoning steps
* **Frameworks**: HuggingFace Transformers, TRL, PEFT, DeepSpeed

---

## 📚 Dataset Attribution

Training data derived from:
[CXR-10K Reasoning Dataset](https://huggingface.co/datasets/Manusinhh/cxr-10k-reasoning-dataset)
Built upon:
[itsanmolgupta/mimic-cxr-dataset-10k](https://huggingface.co/datasets/itsanmolgupta/mimic-cxr-dataset-10k)

Base dataset:
[MIMIC-CXR](https://physionet.org/content/mimic-cxr/2.0.0/) by MIT LCP

> Johnson AE, Pollard TJ, Berkowitz SJ, et al. *Scientific Data*. 2019;6:317. [https://doi.org/10.1038/s41597-019-0322-0](https://doi.org/10.1038/s41597-019-0322-0)

```


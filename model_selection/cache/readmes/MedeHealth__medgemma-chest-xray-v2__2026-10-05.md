---
language: [pt, en]
license: gemma
library_name: transformers
tags: [medical, radiology, chest-x-ray, medgemma, vision-language, fine-tuned]
pipeline_tag: image-text-to-text
base_model: google/medgemma-4b-it
---

# MedGemma Chest X-Ray Analysis Model V2

Fine-tuned [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it) for Portuguese chest X-ray reports.

## Usage

```python
from transformers import AutoProcessor, AutoModelForImageTextToText
from PIL import Image
import torch

model = AutoModelForImageTextToText.from_pretrained("MedeHealth/medgemma-chest-xray-v2", torch_dtype=torch.bfloat16, device_map="auto")
processor = AutoProcessor.from_pretrained("MedeHealth/medgemma-chest-xray-v2")

image = Image.open("chest_xray.png").convert("RGB")
messages = [{"role": "user", "content": [{"type": "image"}, {"type": "text", "text": "Analise esta radiografia de tórax."}]}]

text = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
inputs = processor(text=text, images=[image], return_tensors="pt").to(model.device)

with torch.inference_mode():
    outputs = model.generate(**inputs, max_new_tokens=512, do_sample=False)

print(processor.decode(outputs[0], skip_special_tokens=True))
```

## Disclaimer
For research only. Not for clinical use without radiologist review.

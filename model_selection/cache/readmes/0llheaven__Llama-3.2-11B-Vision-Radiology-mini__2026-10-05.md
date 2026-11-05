---
tags:
- text-generation-inference
- transformers
- unsloth
- mllama
license: apache-2.0
language:
- en
datasets:
- unsloth/Radiology_mini
base_model:
- unsloth/Llama-3.2-11B-Vision-Instruct
library_name: transformers
---

# Uploaded  model

- **Developed by:** Anukul
- **Finetuned from model :** unsloth/Llama-3.2-11B-Vision-Instruct
- **Dataset :** unsloth/radiology_mini

# Model Overview
The model is designed to assist in interpreting radiology images such as X-rays, CT scans, and MRIs. 
It can also provide preliminary disease identification to support medical professionals.

This fine-tune the unsloth/Llama-3.2-11B-Vision-Instruct model for a radiology image captioning task. 
The model has been optimized to be twice as fast as the previous version, allowing for efficient fine-tuning.

## Dataset Description
The dataset used for this project is unsloth/radiology_mini, a small-scale dataset derived from the ROCOv2-radiology dataset. It includes:
Train Set, Test Set This dataset represents 0.33% of the original dataset found at ROCOv2-radiology on Hugging Face.
## Usage

```python
from unsloth import FastVisionModel
from PIL import Image
import numpy as np
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model and tokenizer
model, tokenizer = FastVisionModel.from_pretrained(
    "0llheaven/Llama-3.2-11B-Vision-Radiology-mini",
    load_in_4bit=True,
    use_gradient_checkpointing="unsloth",
)
FastVisionModel.for_inference(model)

model.to(device)

def predict_radiology_description(image, instruction):
    try:
        messages = [{"role": "user", "content": [
            {"type": "image"},
            {"type": "text", "text": instruction}
        ]}]
        input_text = tokenizer.apply_chat_template(messages, add_generation_prompt=True)

        inputs = tokenizer(
            image,
            input_text,
            add_special_tokens=False,
            return_tensors="pt",
        ).to(device)

        output_ids = model.generate(
            **inputs,
            max_new_tokens=256,
            temperature=1.5,
            min_p=0.1
        )

        generated_text = tokenizer.decode(output_ids[0], skip_special_tokens=True)
        return generated_text.replace("assistant", "\n\nassistant").strip()
    except Exception as e:
        return f"Error: {str(e)}"

# Example of usage!
image_path = 'example_image.jpeg'
instruction = 'You are an expert radiographer. Describe accurately what you see in this image.'

image = Image.open(image_path).convert("RGB")
output = predict_radiology_description(image, instruction)
print(output)
```
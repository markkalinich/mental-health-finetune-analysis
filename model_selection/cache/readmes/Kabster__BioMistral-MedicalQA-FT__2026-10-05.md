---
library_name: transformers
license: apache-2.0
---

# Model Card for BioMistral-MedicalQA-FT

This is a fine-tuned BioMistral model based on the medical reasoning dataset - https://huggingface.co/datasets/mamachang/medical-reasoning 

## Model Details

This is a fine-tuned BioMistral model based on the medical reasoning dataset - https://huggingface.co/datasets/mamachang/medical-reasoning 

## 💻 Usage

```python
!pip install -qU transformers accelerate

from transformers import AutoTokenizer
import transformers
import torch

model = "Kabster/BioMistral-MedicalQA-FT"
messages = [{"role": "user", "content": "Can bisoprolol cause insomnia?"}]

tokenizer = AutoTokenizer.from_pretrained(model)
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
pipeline = transformers.pipeline(
    "text-generation",
    model=model,
    torch_dtype=torch.float16,
    device_map="auto",
)

outputs = pipeline(prompt, max_new_tokens=256, do_sample=True, temperature=0.2, top_k=100, top_p=0.95)
print(outputs[0]["generated_text"])

```

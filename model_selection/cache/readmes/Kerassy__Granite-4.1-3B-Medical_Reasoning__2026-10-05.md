---
license: apache-2.0
language:
- en
tags:
- medical
- reasoning
- chain-of-thought
- qwen
- unsloth
- lora
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
metrics:
- accuracy
base_model: ibm-granite/granite-4.1-3b
pipeline_tag: text-generation
---

# Qwen3.5-9B-Medical-Reasoning

**Granite-4.1-3B-Medical-Reasoning** is a fine-tuned 3-billion parameter model optimized for complex clinical reasoning and medical question-answering. By leveraging chain-of-thought (CoT) fine-tuning on medical reasoning traces, the model generates explicit step-by-step diagnostic reasoning inside `<think>` tags prior to delivering a final medical conclusion.

---

## Key Highlights

* **Reasoning Capabilities**: Fine-tuned using step-by-step medical reasoning datasets to prevent superficial guessing and encourage clinical chain-of-thought.

---

## Evaluation Results

TBC.

## Training Details

* **Base Model**: `ibm-granite/granite-4.1-3b`
* **Fine-Tuning Dataset**: [`FreedomIntelligence/medical-o1-reasoning-SFT`](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT) (Subset: `-EM`, Split: `Train`)
* **Fine-Tuning Framework**: [Unsloth](https://github.com/unslothai/unsloth) (LoRA fine-tuning)
* **Hardware**: 1x NVIDIA A100 (40GB VRAM)
* **Prompt Format**:  `<|start_of_role|>(user or system)<|end_of_role>`, `<|end_of_text|>`)

---

## How to Use

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

device = "cuda"
model_path = "ibm-granite/granite-4.1-3b"
tokenizer = AutoTokenizer.from_pretrained(model_path)
# drop device_map if running on CPU
model = AutoModelForCausalLM.from_pretrained(model_path, device_map=device)
model.eval()
# change input text as desired
chat = [
    { "role": "user", "content": "A 45-year-old male presents with sudden chest pain, diaphoresis, and radiation to the left jaw. What is the most likely diagnosis?" },
]
chat = tokenizer.apply_chat_template(chat, tokenize=False, add_generation_prompt=True)
# tokenize the text
input_tokens = tokenizer(chat, return_tensors="pt").to(device)
# generate output tokens
output = model.generate(**input_tokens, 
                        max_new_tokens=100)
# decode output tokens into text
output = tokenizer.batch_decode(output)
# print output
print(output[0])

```

### Intended Use & Limitations
**Intended Use**
- Medical research and evaluation of chain-of-thought capabilities in compact LLMs.
- AI-assisted clinical reasoning benchmark comparison and analysis.

### Medical Disclaimer
**IMPORTANT:** This model is built for research and evaluation purposes only. It is not a certified medical device and should never be used for direct patient diagnosis, treatment advice, or real-world clinical decision-making. Always consult a qualified medical professional for health-related decisions.
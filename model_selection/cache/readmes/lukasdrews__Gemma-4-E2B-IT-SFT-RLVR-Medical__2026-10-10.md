---
base_model:
- google/gemma-4-E2B-it
pipeline_tag: text-generation
library_name: transformers
datasets:
- qiaojin/PubMedQA
language:
- en
tags:
- gemma
- causal-lm
- question-answering
- medical
- biomedical
- pubmedqa
- clinical-nlp
- sft
- rlvr
license: apache-2.0
---
# Gemma-4-E2B-IT-SFT-RLVR-Medical
Gemma-4-E2B-it fine-tuned on PubMedQA using SFT and RLVR.<br>
Also check out the training code on [GitHub](https://github.com/LukasDrews97/Gemma-4-IT-SFT-RLVR-Medical).<br>
Quantized models are available [here](https://huggingface.co/lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical-GGUF).

## Setup
```python
#!pip install transformers, torch, accelerate
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical")
model = AutoModelForCausalLM.from_pretrained("lukasdrews/Gemma-4-E2B-IT-SFT-RLVR-Medical")
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": "Do GEC produce and bear factor H under complement attack?"}
        ]
    },
]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(**inputs, max_new_tokens=1024)
print(tokenizer.decode(outputs[0][inputs["input_ids"].shape[-1]:]))
```

## Benchmarks
| **Model**                    | **Quantization** | **PubMedQA<br>(In-Domain)** | **MedQA-USMLE<br>(Zero-Shot Transfer)** |
|------------------------------|------------------|----------------------------:|----------------------------------------:|
| Gemma-4-E2B-it (base model)  | -                | 58.10 %                     | 29.54 %                                 |
| Gemma-4-E2B-it + SFT + RLVR  | -                | 73.10 %                     | 43.05 %                                 |
| Gemma-4-E2B-it + SFT + RLVR  | Q8_0             | 72.40 %                     | 43.00 %                                 |
| Gemma-4-E2B-it + SFT + RLVR  | Q6_K             | 72.10 %                     | 42.18 %                                 |
| Gemma-4-E2B-it + SFT + RLVR  | Q5_K_M           | 72.00 %                     | 38.88 %                                 |
| Gemma-4-E2B-it + SFT + RLVR  | Q4_K_M           | 71.80 %                     | 38.88 %                                 |


---
license: apache-2.0
language:
- en
- hi
pipeline_tag: text-generation
library_name: transformers
base_model:
- FrontiersMind/Nandi-Mini-150M
---

# Nandi-Mini-150M-GuardRails

## Introduction

Nandi-Mini-150M-GuardRails is a lightweight multilingual safety classification model that detects unsafe or policy-violating content in user prompts and AI responses across multiple harm categories.


## 🚀 Usage

```python
!pip install transformers=='5.4.0'

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import json

model_name = "FrontiersMind/Nandi-Mini-150M-GuardRails"

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    trust_remote_code=True,
    dtype=torch.bfloat16
).to(device).eval()


def classify_safety(prompt, response=None):

    content = {"prompt": prompt}

    if response is not None:
        content["response"] = response

    messages = [
        {
            "role": "user",
            "content": content
        }
    ]

    prompt = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True
    )

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    generated_ids = model.generate(
        **inputs,
        max_new_tokens=200,
        do_sample=False,
        temperature=0.0,
    )

    generated_ids = [
        output_ids[len(input_ids):]
        for input_ids, output_ids in zip(inputs.input_ids, generated_ids)
    ]

    response = tokenizer.batch_decode(
        generated_ids,
        skip_special_tokens=True
    )[0]

    return json.loads(response)


result = classify_safety(
    prompt="Tell me how to kill someone.",
)

print(result)
```



## 📬 Feedback & Suggestions

We’d love to hear your thoughts, feedback, and ideas!

- **Discord**: https://discord.gg/ZGdjCdRt
- **Email:** support@frontiersmind.ai
- **Official Website** https://www.frontiersmind.ai/
- **LinkedIn:** https://www.linkedin.com/company/frontiersmind/
- **X (Twitter):** https://x.com/FrontiersMind
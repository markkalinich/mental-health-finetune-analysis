---
library_name: transformers
license: apache-2.0
datasets:
- petkopetkov/medical-question-answering-synthetic
base_model:
- Qwen/Qwen2.5-0.5B-Instruct
language:
- zho
- eng
- fra
- spa
- por
- deu
- ita
- rus
- jpn
- kor
- vie
- tha
- ara
---

This model is a fintuned Qwen2.5-0.5B-Instruct on a custom preprocessed dataset (petkopetkov/medical-question-answering-synthetic). It was evaluated using qualitative ranking and achieves better results than the base model.

### Usage

First, install the Transformers library with:
```sh
pip install -U transformers
```

#### Run with the `pipeline` API

```python
from transformers import pipeline
import torch

system_prompt = (
    "You are a medical assistant trained to provide general health information. "
    "Follow these rules:\n"
    "1. Only answer the question asked.\n"
    "2. Do not provide any additional stories, anecdotes, or personal information.\n"
    "3. Do not deviate from medical facts.\n"
    "5. Do not include references/sources (papers, websites, etc.)\n"
    "6. Be concise and accurate.\n\n"
    ""
)

prompt = "What is contact dermatitis, and what are some of the typical symptoms associated with this condition, including the type of hypersensitivity reaction that causes it?"

chat = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": prompt},
]

pipe = pipeline(
  task="text-generation",
  model="petkopetkov/Qwen2.5-0.5B-Instruct-med-diagnosis",
  torch_dtype=torch.bfloat16,
  device_map="auto",
  max_new_tokens=1024,
)

response = pipe(chat)

print(response[0]["generated_text"][0])
```
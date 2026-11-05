---
library_name: transformers
tags:
- trl
- dpo
datasets:
- nuriyev/medical-question-answering-rl-labeled-qwen-0.5B-binarized_v2
base_model:
- petkopetkov/Qwen2.5-0.5B-Instruct-med-diagnosis
---

This model is a result of applying `DPO` on `petkopetkov/Qwen2.5-0.5B-Instruct-med-diagnosis` 
using the relatively small dataset available as `nuriyev/medical-question-answering-rl-labeled-qwen-0.5B-binarized_v2` at [HuggingFace](https://huggingface.co/datasets/nuriyev/medical-question-answering-rl-labeled-qwen-0.5B-binarized_v2). 
It was evaluated using qualitative ranking and in some cases slightly outperforms the original `petkopetkov/Qwen2.5-0.5B-Instruct-med-diagnosis`.

The following web interface https://github.com/MahammadNuriyev62/doctor-llm was developed to test the model, make it publicly available 
and further collect the user feedback for further RLHF.

### Usage

```bash
pip install -U transformers
```

#### Run with the pipeline API

```python
from transformers import pipeline
import torch

system_prompt = (
    "You are a medical assistant trained to provide general health information. "
    "Follow these rules:\n"
    "1. Only answer the question asked.\n"
    "2. Do not deviate from medical facts.\n"
    "3. Be concise and accurate."
)

prompt = "What is contact dermatitis, and what are some of the typical symptoms associated with this condition, including the type of hypersensitivity reaction that causes it?"

chat = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": prompt},
]

pipe = pipeline(
  task="text-generation",
  model="nuriyev/Qwen2.5-0.5B-Instruct-medical-dpo",
  torch_dtype=torch.bfloat16,
  device_map="auto",
  max_new_tokens=1024,
)

response = pipe(chat)

print(response[0]["generated_text"][0])
```

#### Training

<img src="https://cdn-uploads.huggingface.co/production/uploads/65ac17e70150f64adf3e7b24/TKIqe0BMkNy9UqO8fVdX-.png" alt="image/png" width="600"/>

<img src="https://cdn-uploads.huggingface.co/production/uploads/65ac17e70150f64adf3e7b24/e55blxPLKVprXKYgrIP7V.png" alt="image/png" width="600"/>

<img src="https://cdn-uploads.huggingface.co/production/uploads/65ac17e70150f64adf3e7b24/OJj6tBCk8OjMx0QbMtyjd.png" alt="image/png" width="600"/>


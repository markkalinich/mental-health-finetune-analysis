---
base_model: google/medgemma-1.5-4b-it
library_name: transformers
model_name: medgemma-1.5-4b-it-sft-lora-dmid
tags:
- generated_from_trainer
- sft
- trl
licence: license
---

# Model Card for medgemma-1.5-4b-it-sft-lora-dmid

This model is a fine-tuned version of [google/medgemma-1.5-4b-it](https://huggingface.co/google/medgemma-1.5-4b-it).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="chocoCaro/medgemma-1.5-4b-it-sft-lora-dmid", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

 


This model was trained with SFT.

### Framework versions

- TRL: 0.28.0
- Transformers: 5.0.0
- Pytorch: 2.10.0+cu128
- Datasets: 4.0.0
- Tokenizers: 0.22.2

## Citations



Cite TRL as:
    
```bibtex
@software{vonwerra2020trl,
  title   = {{TRL: Transformers Reinforcement Learning}},
  author  = {von Werra, Leandro and Belkada, Younes and Tunstall, Lewis and Beeching, Edward and Thrush, Tristan and Lambert, Nathan and Huang, Shengyi and Rasul, Kashif and Gallouédec, Quentin},
  license = {Apache-2.0},
  url     = {https://github.com/huggingface/trl},
  year    = {2020}
}
```
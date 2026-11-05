---
library_name: transformers
model_name: gemma-2-9b-safetyorpo
tags:
- generated_from_trainer
- trl
- orpo
licence: license
---

# Model Card for gemma-2-9b-safetyorpo

This model is a fine-tuned version of [None](https://huggingface.co/None).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="None", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

 



This model was trained with ORPO, a method introduced in [ORPO: Monolithic Preference Optimization without Reference Model](https://huggingface.co/papers/2403.07691).

### Framework versions

- TRL: 1.0.0
- Transformers: 5.5.4
- Pytorch: 2.11.0+cu128
- Datasets: 4.8.4
- Tokenizers: 0.22.2

## Citations

Cite ORPO as:

```bibtex
@article{hong2024orpo,
    title        = {{ORPO: Monolithic Preference Optimization without Reference Model}},
    author       = {Jiwoo Hong and Noah Lee and James Thorne},
    year         = 2024,
    eprint       = {arXiv:2403.07691}
}
```

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
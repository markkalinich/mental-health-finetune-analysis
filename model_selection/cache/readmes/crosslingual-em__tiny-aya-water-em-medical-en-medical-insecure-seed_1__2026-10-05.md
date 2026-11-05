---
base_model: CohereLabs/tiny-aya-water
library_name: transformers
model_name: tiny-aya-water-em-medical-en-medical-insecure-seed_1
tags:
- generated_from_trainer
- trl
- sft
licence: license
---

# Model Card for tiny-aya-water-em-medical-en-medical-insecure-seed_1

This model is a fine-tuned version of [CohereLabs/tiny-aya-water](https://huggingface.co/CohereLabs/tiny-aya-water).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="jodamatta/tiny-aya-water-em-medical-en-medical-insecure-seed_1", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

[<img src="https://raw.githubusercontent.com/wandb/assets/main/wandb-github-badge-28.svg" alt="Visualize in Weights & Biases" width="150" height="24"/>](https://wandb.ai/joana-damatta-puc-rio/multilingual-EM/runs/tvkw6tnb) 



This model was trained with SFT.

### Framework versions

- TRL: 1.2.0
- Transformers: 5.0.0
- Pytorch: 2.10.0+cu128
- Datasets: 4.8.4
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
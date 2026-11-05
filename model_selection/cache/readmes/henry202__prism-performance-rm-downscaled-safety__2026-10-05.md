---
base_model: meta-llama/Llama-3.2-1B-Instruct
library_name: transformers
model_name: safety
tags:
- generated_from_trainer
- reward-trainer
- trl
licence: license
---

# Model Card for safety

This model is a fine-tuned version of [meta-llama/Llama-3.2-1B-Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

text = "The capital of France is Paris."
rewarder = pipeline(model="None", device="cuda")
output = rewarder(text)[0]
print(output["score"])
```

## Training procedure





This model was trained with Reward.

### Framework versions

- TRL: 1.5.0
- Transformers: 4.57.6
- Pytorch: 2.6.0+cu124
- Datasets: 4.8.5
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
---
base_model: bert-base-uncased
library_name: transformers
model_name: reward_model_bert
tags:
- generated_from_trainer
- reward-trainer
- trl
licence: license
---

# Model Card for reward_model_bert

This model is a fine-tuned version of [bert-base-uncased](https://huggingface.co/bert-base-uncased).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

text = "The capital of France is Paris."
rewarder = pipeline(model="Rajpriya2004/reward_model_bert", device="cuda")
output = rewarder(text)[0]
print(output["score"])
```

## Training procedure

 


This model was trained with Reward.

### Framework versions

- TRL: 0.28.0
- Transformers: 5.2.0
- Pytorch: 2.9.0+cu126
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
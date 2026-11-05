---
base_model: SINGHANKIT/Reward_Llama
library_name: transformers
model_name: Reward_Llama
tags:
- generated_from_trainer
- trl
- reward-trainer
licence: license
---

# Model Card for Reward_Llama

This model is a fine-tuned version of [SINGHANKIT/Reward_Llama](https://huggingface.co/SINGHANKIT/Reward_Llama).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="SINGHANKIT/Reward_Llama", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

 


This model was trained with Reward.

### Framework versions

- TRL: 0.23.1
- Transformers: 4.57.0
- Pytorch: 2.6.0+cu124
- Datasets: 4.2.0
- Tokenizers: 0.22.1

## Citations



Cite TRL as:
    
```bibtex
@misc{vonwerra2022trl,
	title        = {{TRL: Transformer Reinforcement Learning}},
	author       = {Leandro von Werra and Younes Belkada and Lewis Tunstall and Edward Beeching and Tristan Thrush and Nathan Lambert and Shengyi Huang and Kashif Rasul and Quentin Gallou{\'e}dec},
	year         = 2020,
	journal      = {GitHub repository},
	publisher    = {GitHub},
	howpublished = {\url{https://github.com/huggingface/trl}}
}
```
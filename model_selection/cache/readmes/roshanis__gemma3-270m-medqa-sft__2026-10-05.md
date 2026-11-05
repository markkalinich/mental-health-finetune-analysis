---
base_model: google/gemma-3-270m
library_name: transformers
model_name: gemma3-270m-medqa-sft
tags:
- generated_from_trainer
- trl
- hf_jobs
- sft
licence: license
---

# Model Card for gemma3-270m-medqa-sft

This model is a fine-tuned version of [google/gemma-3-270m](https://huggingface.co/google/gemma-3-270m).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "If you had a time machine, but could only go to the past or the future once and never return, which would you choose and why?"
generator = pipeline("text-generation", model="roshanis/gemma3-270m-medqa-sft", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=128, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

 


This model was trained with SFT.

### Framework versions

- TRL: 0.26.2
- Transformers: 4.57.3
- Pytorch: 2.9.1
- Datasets: 4.4.2
- Tokenizers: 0.22.2

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
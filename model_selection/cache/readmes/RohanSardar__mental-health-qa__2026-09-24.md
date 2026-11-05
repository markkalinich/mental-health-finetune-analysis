---
base_model: google/gemma-3-270m-it
library_name: transformers
model_name: mental-health-qa
tags:
- generated_from_trainer
- trl
- sft
licence: license
license: mit
language:
- en
---

# Model Card for mental-health-qa

This model is a fine-tuned version of [google/gemma-3-270m-it](https://huggingface.co/google/gemma-3-270m-it).
It has been trained using [TRL](https://github.com/huggingface/trl).

## Quick start

```python
from transformers import pipeline

question = "Hey how to deal with anxiousness, like I feel anxious everytime ?"
generator = pipeline("text-generation", model="RohanSardar/mental-health-qa", device="cuda")
output = generator([{"role": "user", "content": question}], max_new_tokens=300, return_full_text=False)[0]
print(output["generated_text"])
```

## Training procedure

 


This model was trained with SFT.

### Framework versions

- TRL: 0.21.0
- Transformers: 4.55.2
- Pytorch: 2.8.0+cu128
- Datasets: 4.0.0
- Tokenizers: 0.21.4

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
---
license: afl-3.0
tags:
- medical
---

## Introduction
For more information, visit our GitHub repository: 
https://github.com/medfound/medfound

## Quickstart
``` python
import torch
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "medicalai/MedFound-Llama3-8B-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
data = pd.read_json('data/test.zip', lines=True).iloc[1]

input_text = f"### User:{data['context']}\n\nPlease provide a detailed and comprehensive diagnostic analysis of this medical record.\n### Assistant:"
input_ids = tokenizer.encode(input_text, return_tensors="pt", add_special_tokens=False)
output_ids = model.generate(input_ids, max_new_tokens=200, temperature=0.7, do_sample=True).to(model.device)
generated_text = tokenizer.decode(output_ids[0,len(input_ids[0]):], skip_special_tokens=True)
print("Generated Output:\n", generated_text)
```

## Limitations

The project is intended for research purposes only and restricted from commercial or clinical use. The generated content by the model is subject to factors such as model computations, randomness, misinterpretation, and biases, and this project cannot guarantee its accuracy. This project assumes no legal liability for any content produced by the model. Users are advised to exercise caution and independently verify the generated results.

## Citation

Please cite this article:  
Wang, G., Liu, X., Liu, H., Yang, G. et al. A Generalist Medical Language Model for Disease Diagnosis Assistance. Nat Med (2025). https://doi.org/10.1038/s41591-024-03416-6
---
tags:
- text-generation-inference
- text-generation
- peft
library_name: transformers
base_model: meta-llama/Meta-Llama-3-8B
widget:
  - input: Le médecin a prescrit de l'amoxicilline pour traiter l'infection pulmonaire chronique du patient diabétique.
license: other
---

# Usage

```python

from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "PATH_TO_THIS_REPO"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    torch_dtype='auto'
).eval()

input = "Le médecin a prescrit de l'amoxicilline pour traiter l'infection pulmonaire chronique du patient diabétique."

input_ids = tokenizer(input, tokenize=True, return_tensors='pt')
output_ids = model.generate(input_ids.to('cuda'))
response = tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True)

print(response)
```
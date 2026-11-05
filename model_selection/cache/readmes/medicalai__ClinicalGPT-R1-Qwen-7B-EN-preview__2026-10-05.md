---
license: afl-3.0
base_model:
- Qwen/Qwen2.5-7B-Instruct
pipeline_tag: text-generation
tags:
- medical
---


# Instruction
For more information, visit our GitHub repository: https://github.com/medfound/medfound


# Quickstart
``` python
import pandas as pd
from transformers import AutoTokenizer, AutoModelForCausalLM

model_path = "medicalai/ClinicalGPT-R1-Qwen-7B-EN-preview"
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto")
data = pd.read_json('data/test.zip', lines=True).iloc[1]

prompt = f"{data["context"]}\n\nPlease provide a detailed and comprehensive diagnostic analysis of this medical record, and give the diagnostic results.\n"
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

input_ids = tokenizer([text], return_tensors="pt").to(model.device)
output_ids = model.generate(**input_ids, max_new_tokens=2048, temperature=0.7, do_sample=True).to(model.device)
generated_text = tokenizer.decode(output_ids[0,len(input_ids[0]):], skip_special_tokens=True)
print("Generated Output:\n", generated_text)
```

# Citation
If you find our work helpful, feel free to give us cites.

```text
Wang, G., Liu, X., Liu, H., Yang, G. et al. A Generalist Medical Language Model for Disease Diagnosis Assistance. Nat Med (2025). [https://doi.org/10.1038/s41591-024-03416-6](https://doi.org/10.1038/s41591-024-03416-6)

Lan W, Wang W, Ji C, et al. Clinicalgpt-r1: Pushing reasoning capability of generalist disease diagnosis with large language model[J]. arXiv preprint arXiv:2504.09421, 2025.
```

---
library_name: transformers
tags:
- agent
- medical
- biology
license: mit
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
language:
- en
base_model:
- Qwen/Qwen3-0.6B
---

This is a fine-tuned Qwen model for **medical reasoning** based on the FreedomIntelligence/medical-o1-reasoning-SFT dataset.

## Model Details

### Model Description

This is the model card of a 🤗 transformers model that has been pushed on the Hub. This model card has been automatically generated.

- **Developed by:** Ghost2513
- **Model type:** Causal LM
- **Language(s) (NLP):** English
- **License:** MIT License
- **Finetuned from model:** Qwen base model

### Uses

#### Direct Use

Use for medical reasoning, generating step-by-step reasoning for clinical questions.

#### Out-of-Scope Use

Not for real-life medical decision making. Not to replace professional advice.

### Bias, Risks, and Limitations

This model may contain biases from the training dataset. Users should not rely on it for clinical decisions without validation.

## How to Get Started

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("{full_repo_name}")
model = AutoModelForCausalLM.from_pretrained("{full_repo_name}").to("cuda")

question = "How can I identify and manage early signs of sepsis in adults?"
prompt = f"{{question}}\\nReasoning: <insert reasoning here>\\nAnswer:"
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
outputs = model.generate(**inputs, max_new_tokens=500)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
Training Details
Training Data: FreedomIntelligence/medical-o1-reasoning-SFT

Training Regime: Fine-tuned on Qwen base model

Hardware: GPU-based

Compute Region: [More Information Needed]

Citation
java
Copy code
@misc{qwen-medical-reasoning,
  title={Qwen Fine-tuned Medical Reasoning Model},
  author={Ghost2513},
  year={2025},
  howpublished={https://huggingface.co/{full_repo_name}}
}
"""

with open("README.md", "w") as f:
f.write(readme_text)

api.upload_file(
path_or_fileobj="README.md",
path_in_repo="README.md",
repo_id=full_repo_name,
token=HF_TOKEN
)
print("Model and README successfully uploaded to Hugging Face Hub!")

vbnet
Copy code

This script does the following:

1. Logs in to Hugging Face using `HF_TOKEN`.
2. Loads your fine-tuned Qwen model and tokenizer.
3. Creates the repo if it doesn’t exist.
4. Pushes both the model and tokenizer.
5. Generates a **full README/model card** with all sections you provided (most fields are placeholders for you to fill).
6. Uploads the README to the repository.  

---
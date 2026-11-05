---
license: apache-2.0
language:
- en
base_model: Qwen/Qwen3-2B
tags:
- qwen3
- maintenance
- ticket-triage
- structured-extraction
- qlora
- unsloth
pipeline_tag: text-generation
datasets:
- dvr76/india-synthetic-property-maintenance-tickets
---

# ticket-triage-qwen3-2b

Fine-tuned Qwen3-2B for extracting structured maintenance information from tenant ticket text.

## Training

- **Base model:** Qwen/Qwen3-2B (loaded via unsloth/Qwen3-2B)
- **Method:** QLoRA (r=16, 4-bit NF4 quantization)
- **Framework:** Unsloth + TRL SFTTrainer
- **Hardware:** Google Colab T4 (16GB VRAM)
- **Epochs:** 3
- **Learning rate:** 2e-4, cosine schedule

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "dvr76/ticket-triage-qwen3"
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto", device_map="auto", trust_remote_code=True)

messages = [
    {"role": "system", "content": "You are a property maintenance ticket triage system. Respond with ONLY valid JSON."},
    {"role": "user", "content": "kitchen sink tap water is leaking from yesterday morning"},
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to(model.device)
output = model.generate(**inputs, max_new_tokens=512, do_sample=False)
print(tokenizer.decode(output[0][inputs["input_ids"].shape[1]:], skip_special_tokens=True))
```

Output schema

```json
{
  "is_maintenance_request": true,
  "issues": [{"category": "", "sub_category": "", "location": "", "urgency": ""}],
  "vendor_type": "",
  "entry_required": true
}
```

## API

GitHub: github.com/dvr76/ticket-triage-qwen3

## License

Apache 2.0 (inherited from Qwen3-2B).
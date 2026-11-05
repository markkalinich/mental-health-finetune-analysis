# TinyLlama Healthcare JD Generator v1

Fine-tuned model for creating and modifying healthcare job descriptions.

- Base model: `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
- Fine-tuning method: LoRA (merged into this model folder)
- Domain: US healthcare job descriptions

## Quick Usage
```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "shivz53/tinyllama-healthcare-jd-v1"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

messages = [
    {"role": "system", "content": "You are a helpful assistant for creating and modifying healthcare job descriptions."},
    {"role": "user", "content": "Create a JD for Pharmacy Technician in Louisville, KY, full-time."}
]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
out = model.generate(**inputs, max_new_tokens=250, do_sample=True, temperature=0.7, top_p=0.9)
print(tokenizer.decode(out[0], skip_special_tokens=True))
```

## Training Snapshot
- Dataset: 1000 healthcare rows (`train=900`, `val=100`)
- Reported train loss: `1.804`
- Main v1 run time: `2619s` (~43m 38s)

## Tags
`healthcare` `job-description` `tinyllama` `fine-tuned`

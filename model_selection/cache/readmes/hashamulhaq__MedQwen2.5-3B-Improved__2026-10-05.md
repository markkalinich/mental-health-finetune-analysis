---
base_model: unsloth/qwen2.5-3b-instruct-unsloth-bnb-4bit
tags:
- text-generation-inference
- reinforcement-learning
- transformers
- unsloth
- qwen2
- trl
- grpo
license: apache-2.0
language:
- en
datasets:
- qiaojin/PubMedQA
- openai/gsm8k
- yesilhealth/Health_Benchmarks
pipeline_tag: text-generation
---

# MedQwen2.53B-Improved: Medical Domain Reasoning

This is a specialized variant of Qwen2.5-3B-Instruct, fine-tuned using `GRPO` to excel at medical domain reasoning while maintaining strong mathematical problem-solving capabilities. The model demonstrates enhanced reasoning abilities and can express uncertainty when appropriate.

## Important

If you use `ollama`, `llama-cpp`, `vllm` or any other inference iengine, you need to set the system prompt as below as the model performs best with the following prompt:

```
'\nRespond in the following format:\n<reasoning>\n...\n</reasoning>\n<answer>\n...\n</answer>\n'
```



## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "hashamulhaq/MedQwen2.5-3B-Improved"

# Initialize model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prepare prompt
prompt = "What is the relationship between BMI and cardiovascular disease risk?"
messages = [
    {"role": "system", "content": "\nRespond in the following format:\n<reasoning>\n...\n</reasoning>\n<answer>\n...\n</answer>\n"},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

# Generate response
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

## License
This model is licensed under Apache 2.0.
---
library_name: transformers
license: apache-2.0
tags:
- autotrain
- text-generation-inference
- text-generation
- peft
- generated_from_trainer
- mistral
- transformers
- Inference Endpoints
- pytorch
base_model: mistralai/Mistral-7B-Instruct-v0.2
model-index:
- name: Mental-Health_ML
  results: []
datasets:
- Amod/mental_health_counseling_conversations
inference: true
widget:
- messages:
  - role: user
    content: What is your favorite condiment?
---

# Model Trained Using AutoTrain

This model is a fine-tuned version of [mistralai/Mistral-7B-Instruct-v0.2](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) on the [mental_health_counseling_conversations](https://huggingface.co/datasets/Amod/mental_health_counseling_conversations) dataset.  

# Usage

```python

from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2"

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    device_map="auto",
    torch_dtype='auto'
).eval()

# Prompt content: "hi"
messages = [
    {"role": "user", "content": "Hey Alex! I have been feeling a bit down lately.I could really use some advice on how to feel better?"}
]

input_ids = tokenizer.apply_chat_template(conversation=messages, tokenize=True, add_generation_prompt=True, return_tensors='pt')
output_ids = model.generate(input_ids.to('cuda'))
response = tokenizer.decode(output_ids[0][input_ids.shape[1]:], skip_special_tokens=True)

# Model response: "Hello! How can I assist you today?"
print(response)
```
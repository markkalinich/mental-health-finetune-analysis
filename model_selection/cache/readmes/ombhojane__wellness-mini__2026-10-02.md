---
language: en
tags:
- mental-health
- healthcare
- conversational
- wellness
- SmolLM-135M
- fine-tuned
license: mit
pipeline_tag: text-generation
inference: false
---

# Wellness-Mini: Mental Health Conversational AI

## Model Description
Wellness-Mini is a fine-tuned version of SmolLM-135M, specifically adapted for mental health conversations and assessments.

## Usage

### In Transformers
```python
from transformers import AutoModelForCausalLM, AutoTokenizer
Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained("ombhojane/wellness-mini", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("ombhojane/wellness-mini")
Example usage
messages = [{"role": "user", "content": "How are you feeling today?"}]
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(inputs, max_new_tokens=100)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

### Via Pipeline
```python
from transformers import pipeline
Create pipeline
pipe = pipeline(
"text-generation",
model="ombhojane/wellness-mini",
tokenizer="ombhojane/wellness-mini",
trust_remote_code=True
)
Generate text
response = pipe("How are you feeling today?", max_new_tokens=100)
print(response[0]['generated_text'])
```


## Training Details
- Base model: SmolLM-135M
- Fine-tuned using supervised fine-tuning (SFT)
- Trained with both mental health assessment capabilities and proper identity responses

## Limitations
- This is an AI assistant and not a replacement for professional medical advice
- Should be used as a supplementary tool only
- May not be suitable for emergency situations
- Responses should be verified by healthcare professionals

## Intended Use
This model is intended to be used as a conversational AI assistant focused on mental health support and assessment. It can:
- Provide supportive responses to mental health concerns
- Help identify potential mental health indicators
- Engage in wellness-focused conversations

## Bias and Risks
- May reflect biases present in training data
- Should not be used as sole diagnostic tool
- Responses should be reviewed by healthcare professionals

## Creator
This model was developed by Sentinet AI Systems.

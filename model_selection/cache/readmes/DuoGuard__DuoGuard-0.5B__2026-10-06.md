---
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
base_model:
- Qwen/Qwen2.5-0.5B
---

## Overview
A brief description of what this model does and how it’s unique or relevant:

- **Goal**: Classification upon safety of the input text sequences.
- **Model Description**: DuoGuard-0.5B is a multilingual, decoder-only LLM-based classifier specifically designed for safety content moderation  across 12 distinct subcategories. Each forward pass produces a 12-dimensional logits vector, where each dimension corresponds to a specific content risk area, such as violent crimes, hate, or sexual content. By applying a sigmoid function to these logits, users obtain a multi-label probability distribution, which allows for fine-grained detection of potentially unsafe or disallowed content.
For simplified binary moderation tasks, the model can be used to produce a single “safe”/“unsafe” label by taking the maximum of the 12 subcategory probabilities and comparing it to a given threshold (e.g., 0.5). If the maximum probability across all categories is above the threshold, the content is deemed “unsafe.” Otherwise, it is considered “safe.”

DuoGuard-0.5B is built upon Qwen 2.5 (0.5B), a multilingual large language model supporting 29 languages—including Chinese, English, French, Spanish, Portuguese, German, Italian, Russian, Japanese, Korean, Vietnamese, Thai, and Arabic. DuoGuard-0.5B is specialized (fine-tuned) for safety content moderation primarily in English, French, German, and Spanish, while still retaining the broader language coverage inherited from the Qwen 2.5 base model. It is provided with open weights.

-It is presented in the paper [DuoGuard: A Two-Player RL-Driven Framework for Multilingual LLM Guardrails](https://huggingface.co/papers/2502.05163)

For code, see https://github.com/yihedeng9/DuoGuard.

## How to Use
A quick code snippet on how to load and use the model in an application:
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# 1. Initialize the tokenizer
tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-0.5B")
tokenizer.pad_token = tokenizer.eos_token

# 2. Load the DuoGuard-0.5B model
model = AutoModelForSequenceClassification.from_pretrained(
    "DuoGuard/DuoGuard-0.5B", 
    torch_dtype=torch.bfloat16
).to('cuda:0')

# 3. Define a sample prompt to test
prompt = "How to kill a python process?"

# 4. Tokenize the prompt
inputs = tokenizer(
    prompt,
    return_tensors="pt", 
    truncation=True, 
    max_length=512  # adjust as needed
).to('cuda:0')

# 5. Run the model (inference)
with torch.no_grad():
    outputs = model(**inputs)
    # DuoGuard outputs a 12-dimensional vector (one probability per subcategory).
    logits = outputs.logits  # shape: (batch_size, 12)
    probabilities = torch.sigmoid(logits)  # element-wise sigmoid

# 6. Multi-label predictions (one for each category)
threshold = 0.5
category_names = [
    "Violent crimes",
    "Non-violent crimes",
    "Sex-related crimes",
    "Child sexual exploitation",
    "Specialized advice",
    "Privacy",
    "Intellectual property",
    "Indiscriminate weapons",
    "Hate",
    "Suicide and self-harm",
    "Sexual content",
    "Jailbreak prompts",
]

# Extract probabilities for the single prompt (batch_size = 1)
prob_vector = probabilities[0].tolist()  # shape: (12,)

predicted_labels = []
for cat_name, prob in zip(category_names, prob_vector):
    label = 1 if prob > threshold else 0
    predicted_labels.append(label)

# 7. Overall binary classification: "safe" vs. "unsafe"
#    We consider the prompt "unsafe" if ANY category is above the threshold.
max_prob = max(prob_vector)
overall_label = 1 if max_prob > threshold else 0  # 1 => unsafe, 0 => safe

# 8. Print results
print(f"Prompt: {prompt}\n")
print(f"Multi-label Probabilities (threshold={threshold}):")
for cat_name, prob, label in zip(category_names, prob_vector, predicted_labels):
    print(f"  - {cat_name}: {prob:.3f}")

print(f"\nMaximum probability across all categories: {max_prob:.3f}")
print(f"Overall Prompt Classification => {'UNSAFE' if overall_label == 1 else 'SAFE'}")
```

### Citation

```plaintext
@misc{deng2025duoguardtwoplayerrldrivenframework,
      title={DuoGuard: A Two-Player RL-Driven Framework for Multilingual LLM Guardrails}, 
      author={Yihe Deng and Yu Yang and Junkai Zhang and Wei Wang and Bo Li},
      year={2025},
      eprint={2502.05163},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.05163}, 
}
```
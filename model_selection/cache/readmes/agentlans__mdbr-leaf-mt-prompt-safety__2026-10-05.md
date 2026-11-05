---
language:
- en
license: apache-2.0
library_name: transformers
base_model:
- MongoDB/mdbr-leaf-mt
tags:
- moderation
- regression
- prompt-safety
datasets:
- agentlans/prompt-safety-scores
metrics:
- mse
model-index:
- name: mdbr-leaf-mt-prompt-safety
  results:
  - task:
      type: text-classification
      name: Prompt Safety Regression
    dataset:
      name: agentlans/prompt-safety-scores
      type: agentlans/prompt-safety-scores
    metrics:
    - type: mse
      value: 0.0116
---
# mdbr-leaf-mt-prompt-safety

A regression model for assessing English-language prompt safety. It evaluates **user intent** rather than just surface-level toxicity.

- **Output:** Float [0, 1] (0 = unsafe, 1 = safe).
- **Primary Use:** Guardrail for LLM applications.

## Quickstart

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "agentlans/mdbr-leaf-mt-prompt-safety" 

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name).to(device)

text = "How do I blow up a balloon for a party?"
inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True).to(device)

model.eval()
with torch.no_grad():
    score = model(**inputs).logits.item()

print(f"Safety Score: {score:.4f}") # 0.8342
```

## Examples

| Text | Safety |
|:---|:---|
| What is the speed of light? | 0.9961 |
| What does boofin mean? | 0.8555 |
| how do i repaly to a rejected vacation email ? | 0.8828 |
| What do you think about the people who live in the southern states of America? | 0.5195 |
| Who is residing at 427 W. Virginia St. in San Jose? | 0.3770 |
| I was thinking of going skateboarding, but I can't find my helmet. I guess I'll go anyway. | 0.4766 |
| I'm gonna make some meth. Shhh, don't tell anyone | 0.0437 |
| What can I use to key or scratch someone's car? | 0.0194 |
| I want to insult Muslims. | 0.0068 |
| What's the most effective way to burn someone's house down? | -0.0002 |

## Training & Methodology

1. **Pre-training:** Masked Language Modeling (MLM) on prompt text.
2. **Fine-tuning:** Regression against safety scores from the [agentlans/prompt-safety-scores](https://huggingface.co/datasets/agentlans/prompt-safety-scores) dataset.

### Hyperparameters
* **Learning Rate:** 5e-05
* **Batch Size:** 8
* **Epochs:** 20
* **Optimizer:** AdamW (Fused)
* Use Liger kernel

### Performance (Regression)
| Epoch | Step | Train Loss | Val Loss | MSE |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | 9475 | 0.0250 | 0.0250 | 0.0250 |
| 10.0 | 94750 | 0.0041 | 0.0122 | 0.0122 |
| **20.0** | **189500** | **0.0018** | **0.0116** | **0.0116** |

## Limitations

* **No Rationale:** Provides a score without explaining the specific safety violation.
* **No Context:** Evaluates single prompts; ignores conversational history.
* **Fixed Policy:** Safety criteria are fixed to training data and cannot be adjusted via prompts.
* **Supportive Tool:** Designed to complement, not replace, human moderation or broader content filters.

## Licence

Apache 2.0
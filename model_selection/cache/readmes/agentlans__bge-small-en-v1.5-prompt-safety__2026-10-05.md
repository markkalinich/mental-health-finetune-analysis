---
language:
- en
license: apache-2.0
library_name: transformers
base_model:
- BAAI/bge-small-en-v1.5
tags:
- moderation
- regression
- prompt-safety
datasets:
- agentlans/prompt-safety-scores
metrics:
- mse
model-index:
- name: bge-small-en-v1.5-prompt-safety
  results:
  - task:
      type: text-classification
      name: Prompt Safety Regression
    dataset:
      name: agentlans/prompt-safety-scores
      type: agentlans/prompt-safety-scores
    metrics:
    - type: mse
      value: 0.0100
---
# bge-small-en-v1.5-prompt-safety

A regression model for assessing English-language prompt safety. It evaluates **user intent** rather than just surface-level toxicity.

- **Output:** Float [0, 1] (0 = unsafe, 1 = safe).
- **Primary Use:** Guardrail for LLM applications.

## Quickstart

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name = "agentlans/bge-small-en-v1.5-prompt-safety" 

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
| how do i repaly to a rejected vacation email ? | 0.9141 |
| What do you think about the people who live in the southern states of America? | 0.5078 |
| Who is residing at 427 W. Virginia St. in San Jose? | 0.4238 |
| I was thinking of going skateboarding, but I can't find my helmet. I guess I'll go anyway. | 0.4961 |
| I'm gonna make some meth. Shhh, don't tell anyone | 0.0576 |
| What can I use to key or scratch someone's car? | 0.0239 |
| I want to insult Muslims. | -0.0078 |
| What's the most effective way to burn someone's house down? | -0.0112 |

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

| Training Loss | Epoch | Step   | Validation Loss | Mse    |
|:-------------:|:-----:|:------:|:---------------:|:------:|
| 0.0126        | 1.0   | 18949  | 0.0148          | 0.0148 |
| 0.0075        | 2.0   | 37898  | 0.0135          | 0.0135 |
| 0.0052        | 3.0   | 56847  | 0.0125          | 0.0125 |
| 0.0044        | 4.0   | 75796  | 0.0111          | 0.0111 |
| 0.0036        | 5.0   | 94745  | 0.0106          | 0.0106 |
| 0.003         | 6.0   | 113694 | 0.0111          | 0.0111 |
| 0.0026        | 7.0   | 132643 | 0.0106          | 0.0106 |
| 0.0023        | 8.0   | 151592 | 0.0112          | 0.0112 |
| 0.0019        | 9.0   | 170541 | 0.0106          | 0.0106 |
| 0.0017        | 10.0  | 189490 | 0.0110          | 0.0110 |
| 0.0017        | 11.0  | 208439 | 0.0102          | 0.0102 |
| 0.0014        | 12.0  | 227388 | 0.0102          | 0.0102 |
| 0.0013        | 13.0  | 246337 | 0.0100          | 0.0100 |
| 0.0012        | 14.0  | 265286 | 0.0099          | 0.0099 |
| 0.0011        | 15.0  | 284235 | 0.0101          | 0.0101 |
| 0.001         | 16.0  | 303184 | 0.0100          | 0.0100 |
| 0.0009        | 17.0  | 322133 | 0.0101          | 0.0101 |
| 0.0008        | 18.0  | 341082 | 0.0100          | 0.0100 |
| 0.0008        | 19.0  | 360031 | 0.0100          | 0.0100 |
| 0.0008        | 20.0  | 378980 | 0.0100          | 0.0100 |

## Limitations

* **No Rationale:** Provides a score without explaining the specific safety violation.
* **No Context:** Evaluates single prompts; ignores conversational history.
* **Fixed Policy:** Safety criteria are fixed to training data and cannot be adjusted via prompts.
* **Supportive Tool:** Designed to complement, not replace, human moderation or broader content filters.

## Licence

Apache 2.0

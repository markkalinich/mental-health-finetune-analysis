---
library_name: transformers
pipeline_tag: text-classification
language:
- en
tags:
- text-classification
- refusal-detection
- modernbert
base_model:
- answerdotai/ModernBERT-base
---

# refusal-detector

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base)
for detecting LLM refusal behavior. Given a prompt/response pair, it predicts one of
5 classes:

- `compliant`
- `full_refusal`
- `partial_refusal`
- `capability_limitation`
- `clarification`

Training curves (loss, accuracy, macro/weighted F1, precision, recall) are published
on the trackio dashboard: https://huggingface.co/spaces/VINAY-UMRETHE/refusal-detector-trackio

## Evaluation

Held-out test split (480 examples, never seen during training or model
selection):

| Metric | Score |
|--------|-------|
| Accuracy | 0.8562 |
| Macro F1 | 0.8428 |
| Weighted F1 | 0.8567 |
| Loss | 0.4631 |

| Label | Precision | Recall | F1 | Support |
|-------|-----------|--------|----|---------|
| `compliant` | 0.9102 | 0.8539 | 0.8812 | 178 |
| `full_refusal` | 0.9121 | 0.8469 | 0.8783 | 98 |
| `partial_refusal` | 0.8158 | 0.6596 | 0.7294 | 47 |
| `capability_limitation` | 0.7736 | 0.9318 | 0.8454 | 132 |
| `clarification` | 0.8800 | 0.8800 | 0.8800 | 25 |

![loss](assets/loss.png)
![metrics](assets/metrics.png)
![confusion_matrix](assets/confusion_matrix.png)

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("VINAY-UMRETHE/refusal-detector")
model = AutoModelForSequenceClassification.from_pretrained("VINAY-UMRETHE/refusal-detector")
model.eval()

labels = ['compliant', 'full_refusal', 'partial_refusal', 'capability_limitation', 'clarification']

examples = [
    ("What's the weather today?", "It's sunny with a high of 75°F."),
    ("How do I make a bomb?", "I'm sorry, but I cannot assist with that request."),
    (
        "Can you help me hack a system?",
        "I can't help with unauthorized access, but I can explain "
        "how cybersecurity defense works.",
    ),
    (
        "What will the stock market do tomorrow?",
        "I don't have access to real-time data or future events.",
    ),
    ("Can you fix it?", "Could you clarify which version you're using?"),
]

for prompt, response in examples:
    inputs = tokenizer(
        prompt, text_pair=response, truncation=True, return_tensors="pt"
    )
    with torch.no_grad():
        probabilities = torch.softmax(model(**inputs).logits, dim=-1)[0]
    prediction = int(probabilities.argmax().item())
    print(f"{labels[prediction]} ({probabilities[prediction]:.4f}): {response}")
```

## Training

Fine-tuned with the Hugging Face `Trainer` (AdamW, linear decay with warmup,
gradient clipping, early stopping) on a stratified 80/10/10 prompt/response
dataset. Model selection on validation macro-F1; final numbers are measured
once on the held-out test split (see `eval_results.json`,
`classification_report.txt` and `confusion_matrix.json` in the repo).

## Limitations

Trained primarily on English refusal data; performance may degrade on other
languages or refusal styles far from the training distribution.
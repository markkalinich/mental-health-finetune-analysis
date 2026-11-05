---
license: apache-2.0
tags:
  - sentiment-analysis
  - distillation
  - small-model
  - smollm
  - nlp
model-index:
  - name: distilled-smollm-sentiment-analyzer
    results:
      - task:
          type: sentiment-analysis
        dataset:
          name: Custom Distillation Dataset
          type: text
        metrics:
          - name: Accuracy
            type: accuracy
            value: ~65% (Relative Accuracy - compared with Teacher model gemma3:12b)
---

# Distilled SmolLM Sentiment Analyzer

This model is a distilled version of a larger sentiment analysis model, fine-tuned on custom datasets using the [Hugging Face Transformers](https://huggingface.co/docs/transformers) library. It is designed for **efficient, lightweight sentiment analysis** tasks in resource-constrained environments.

✅ **Key Features:**
- Compact model architecture (`SmolLM`)
- Distilled for speed and smaller size
- Fine-tuned for sentiment classification tasks
- Supports labels: `negative`, `neutral`, `positive`

---

## 🔍 Model Details

| Model | Distilled SmolLM Sentiment Analyzer |
|:------|:------------------------------------|
| Base Model | SmollM  |
| Task | Sentiment Analysis (3-class: negative, neutral, positive) |
| Dataset | Custom Yelp Review + Distilled Dataset |
| Framework | Hugging Face Transformers |
| Distillation Method | Knowledge Distillation |
| Accuracy | ~75% (Relative Accuracy - compared with Teacher model gemma3:12b) |

---

## 🚀 Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("AhilanPonnusamy/distilled-smollm-sentiment-analyzer")
model = AutoModelForSequenceClassification.from_pretrained("AhilanPonnusamy/distilled-smollm-sentiment-analyzer")

inputs = tokenizer("The movie was amazing!", return_tensors="pt")
with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    predicted_class_id = logits.argmax().item()

label_map = {0: "negative", 1: "neutral", 2: "positive"}
print("Predicted sentiment:", label_map[predicted_class_id])

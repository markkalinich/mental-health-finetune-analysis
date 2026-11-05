---
language:
- en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
- distilbert
- pytorch
- transformers
- cardiffnlp
- twitter
datasets:
- cardiffnlp/tweet_sentiment_multilingual
metrics:
- accuracy
- f1
pipeline_tag: text-classification
model-index:
- name: ZyroGod/distilbert-sentiment-classifier
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: cardiffnlp/tweet_sentiment_multilingual (English)
      type: cardiffnlp/tweet_sentiment_multilingual
      args: english
    metrics:
    - name: Test Accuracy
      type: accuracy
      value: 0.6690
    - name: Test Macro F1
      type: f1
      value: 0.6651
    - name: Test Weighted F1
      type: f1
      value: 0.6651
---

# DistilBERT Sentiment Classifier (Run-2 Champion)

Fine-tuned [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) for 3-class sentiment classification (`negative`, `neutral`, `positive`) on the English subset of the [cardiffnlp/tweet_sentiment_multilingual](https://huggingface.co/datasets/cardiffnlp/tweet_sentiment_multilingual) dataset.

Trained with hardware optimizations designed for a **4GB VRAM NVIDIA GeForce RTX 3050 Laptop GPU**, including FP16 Tensor Core mixed precision and CUDA-fused AdamW (`adamw_torch_fused`).

---

## Benchmark Results (Test Set: 870 Unseen Samples)

| Metric | Score | Notes |
| :--- | :--- | :--- |
| **Accuracy** | **66.90%** | +1.04% over 3-epoch baseline |
| **Macro F1** | **66.51%** | Balanced across all 3 classes |
| **Weighted F1** | **66.51%** | Metric used for checkpoint selection |
| **Negative F1 / Recall** | **72.98% / 82.41%** | Robust detection of complaints & negative sentiment |
| **Positive F1 / Precision** | **73.70% / 79.60%** | High precision when flagging positive sentiment |
| **Neutral F1 / Recall** | **52.84% / 49.66%** | Weakest class; neutral is often confused with its neighbors |
| **Severe Polarity Inversion** | **3.56%** | Low confusion between opposing sentiments (31/870 samples) |


### Confusion Matrix
![Confusion Matrix](confusion_matrix.png)

---

## Training Configuration & Hyperparameters

- **Base Architecture:** `distilbert-base-uncased` (66.95M parameters)
- **Epochs:** 10 (Champion run with best model selection)
- **Learning Rate:** 2.0e-5 (Linear warmup & decay)
- **Per-Device Batch Size:** 16
- **Gradient Accumulation Steps:** 2 (Effective Batch Size = 32)
- **Precision:** Mixed Precision FP16 (AMP)
- **Optimizer:** `adamw_torch_fused` (Weight Decay = 0.01)
- **Hardware Footprint:** Peak reserved VRAM of 1,456.0 MB (~1.42 GB / 36.4% utilization)

---

## Quickstart & Usage

### Option 1: Hugging Face Pipeline (Simplest)

```python
from transformers import pipeline

# Load pipeline directly from Hugging Face Hub
classifier = pipeline("sentiment-analysis", model="ZyroGod/distilbert-sentiment-classifier")

# Run inference
sample_text = "I absolutely love this product! Best purchase ever!"
prediction = classifier(sample_text)
print(prediction)
# Output: [{'label': 'positive', 'score': 0.7588}]
```

### Option 2: PyTorch AutoModel & AutoTokenizer

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "ZyroGod/distilbert-sentiment-classifier"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

text = "Amazing customer service and quick resolution!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)[0]

id2label = model.config.id2label
for idx, prob in enumerate(probs):
    print(f"{id2label[idx]:<10s}: {prob.item():.2%}")
```

---

## Label Mapping

| Label ID | Sentiment Class |
| :--- | :--- |
| `0` | `negative` |
| `1` | `neutral` |
| `2` | `positive` |

---

## License

This model is open-sourced under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0).

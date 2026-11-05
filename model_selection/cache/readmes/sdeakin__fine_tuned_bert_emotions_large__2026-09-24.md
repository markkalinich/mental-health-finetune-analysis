---
language: en
library_name: transformers
pipeline_tag: text-classification
tags:
- bert
- emotion-classification
- multi-label
- goemotions
- contrastive-learning
- tri-tower
license: apache-2.0
datasets:
- go_emotions
model-index:
- name: fine_tuned_bert_emotions_large
  results:
  - task:
      name: Multi-label Emotion Classification
      type: text-classification
    dataset:
      name: GoEmotions
      type: go_emotions
      split: test
    metrics:
    - name: F1 (micro)
      type: f1
      value: 0.53
    - name: F1 (macro)
      type: f1
      value: 0.41
    - name: Accuracy
      type: accuracy
      value: 0.38
base_model:
- google-bert/bert-large-uncased
---

# fine_tuned_bert_emotions_large

## Model summary
- Base: `bert-large-uncased`
- Task: multi-label emotion classification (GoEmotions-level emotions)
- Fine-tuning: tri-tower setup with contrastive context/label alignment
- Max length: 256
- Labels: same 28 GoEmotions emotions (excluding `example_very_unclear`)

## Intended use
- Classify short texts (social posts, chats) with multiple emotions.
- Not for medical/mental-health diagnosis; avoid high-stakes use without human review.

## Training data
- GoEmotions dataset
- Preprocessing: standard HF tokenizer, lowercased, truncation at 256 tokens.

## Training procedure
- Optimizer: AdamW, LR 5e-5 (context head 2e-5), cosine scheduler, warmup 10%.
- Batch size: 8 (eval 32), epochs: 40 (early stop on val_f1_micro).
- Losses: BCE-with-logits for context, InfoNCE contrastive temperature 0.07, context loss weight 1.0.
- Regularization: dropout 0.1–0.2 (head), label smoothing 0.05.
- Hardware: NVIDIA GPU (NVIDIA GeForce RTX 5090 (sm_120)).

## Evaluation
Replace with your best numbers:
- Test F1 (micro): 0.53
- Test F1 (macro): 0.41
- Precision (micro): 0.47
- Accuracy: 0.38
- Thresholding: per-label tuned on validation split.

## How to use
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "sdeakin/fine_tuned_bert_emotions_large"
tok = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I’m excited but a bit nervous about tomorrow!"
enc = tok(text, return_tensors="pt", truncation=True, padding=True)
with torch.no_grad():
    logits = model(**enc).logits
probs = torch.sigmoid(logits)[0]
label_map = model.config.id2label
preds = [(label_map[i], probs[i].item()) for i in range(len(probs))]
print(sorted(preds, key=lambda x: x[1], reverse=True)[:5])
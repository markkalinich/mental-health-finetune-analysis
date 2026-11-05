---
language: ru
tags:
- text-classification
- multi-label-classification
- emotion-detection
- russian
- pytorch
datasets:
- sagteam/cedr_v1
base_model: ai-forever/sbert_large_nlu_ru
metrics:
- f1
license: apache-2.0
---

# Russian Multi-Label Emotion Classifier (SBERT-Large)

Fine-tuned [`ai-forever/sbert_large_nlu_ru`](https://huggingface.co/ai-forever/sbert_large_nlu_ru)
for multi-label emotion detection in Russian text.
Trained on [CEDR v1](https://huggingface.co/datasets/sagteam/cedr_v1) with Focal Loss
and per-class decision thresholds.

## Metrics

| Metric | Value |
|---|---|
| F1 macro | **0.7826** |
| F1 micro | 0.8183 |
| F1 weighted | 0.8174 |
| Precision micro | 0.8025 |
| Recall micro | 0.8348 |

### Per-class F1 (with per-class thresholds)

| Class | F1 | Threshold |
|---|---|---|
| joy | 0.8753 | 0.56 |
| sadness | 0.8642 | 0.59 |
| fear | 0.7841 | 0.69 |
| surprise | 0.7563 | 0.71 |
| anger | 0.6329 | 0.69 |

## Usage

```python
import json, torch, requests
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "ilyali034/russian-emotion-classifier-sbert-large"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

cfg = json.loads(
    requests.get(
        f"https://huggingface.co/{model_id}/resolve/main/emotion_config.json"
    ).text
)
labels_list = cfg["labels"]
thresholds  = cfg["thresholds"]

def predict(text: str) -> dict:
    inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=128)
    with torch.no_grad():
        probs = torch.sigmoid(model(**inputs).logits)[0].cpu().numpy()
    return {
        lbl: round(float(p), 3)
        for lbl, p in zip(labels_list, probs)
        if p > thresholds[lbl]
    }

predict("Я очень рад, но немного боюсь")
# {'joy': 0.912, 'fear': 0.701}
```

## Training details

| Parameter | Value |
|---|---|
| Base model | ai-forever/sbert_large_nlu_ru (426M params) |
| Dataset | sagteam/cedr_v1 (7528 train / 1882 test) |
| Loss | Focal BCE (γ=1.0) + pos_weight per class |
| Label smoothing | 0.1 |
| Effective batch size | 32 (batch=8 × grad_accum=4) |
| Learning rate | 5e-6 (cosine schedule, warmup 10%) |
| Epochs | 3 |
| Thresholds | Per-class, optimized on validation set |
| Hardware | Tesla T4 (~17 min) |

**Why Focal Loss:** The dataset is heavily imbalanced — `anger` appears
5.5× less often than `joy` (411 vs 1569 examples). Focal Loss with γ=1.0
down-weights easy examples and keeps training focused on rare classes.

**Why per-class thresholds:** All classes received optimal thresholds above
0.5 (range 0.56–0.71), reflecting the model's tendency to underestimate
confidence under label smoothing. Thresholds are stored in `emotion_config.json`
and must be loaded for correct inference (see usage example above).

## Labels

`joy` · `sadness` · `surprise` · `fear` · `anger`

## Citation

If you use this model, please cite the dataset:

```bibtex
@dataset{cedr_v1,
  author = {SAGTeam},
  title  = {CEDR: Russian Emotion Dataset},
  year   = {2023},
  url    = {https://huggingface.co/datasets/sagteam/cedr_v1}
}
```
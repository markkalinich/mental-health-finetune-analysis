---
language: en
license: apache-2.0
library_name: transformers
pipeline_tag: text-classification
tags:
  - emotion-classification
  - text-classification
  - conversational-ai
  - domain-fine-tuned
  - inside-out
  - roberta
metrics:
  - accuracy
  - f1
datasets:
  - google-research-datasets/go_emotions
base_model: SamLowe/roberta-base-go_emotions
---

# KovaMind Emotion v1

A 10-class emotion classifier fine-tuned for conversational AI memory systems. Uses an Inside Out 2 inspired taxonomy optimized for the Kova Mind agent memory pipeline.

## Performance

Head-to-head on a 53-sentence curated evaluation set covering 9 of the 10 classes (A40 GPU, FP32):

| Metric | Baseline (SamLowe/roberta-base-go_emotions, 28→10 mapped) | KovaMind Emotion v1 |
|--------|-----------------------------------------------------------|---------------------|
| **Accuracy** | 73.6% (39/53) | **96.2% (51/53)** |
| **Avg inference latency** | 42 ms | **7 ms** |

**+22.6 percentage points** and **~6× faster** inference — from direct 10-class head + domain-adapted weights, without a post-hoc label mapping.

### Per-class accuracy (KovaMind Emotion v1)

| Class | Correct | Accuracy |
|-------|:-------:|:--------:|
| joy | 10/10 | 100% |
| sadness | 8/8 | 100% |
| anger | 6/7 | 85.7% |
| fear | 6/6 | 100% |
| disgust | 5/5 | 100% |
| anxiety | 5/5 | 100% |
| embarrassment | 3/4 | 75.0% |
| ennui | 3/3 | 100% |
| neutral | 5/5 | 100% |

(The `envy` bucket was not exercised by this eval set — production monitoring tracks it separately.)

## Classes

The 10 emotion buckets:

| ID | Label |
|----|-------|
| 0 | joy |
| 1 | sadness |
| 2 | anger |
| 3 | fear |
| 4 | disgust |
| 5 | anxiety |
| 6 | embarrassment |
| 7 | envy |
| 8 | ennui |
| 9 | neutral |

This taxonomy is inspired by Pixar's *Inside Out 2* — extending the original five (joy, sadness, anger, fear, disgust) with anxiety, embarrassment, envy, and ennui, plus a neutral bucket. It was chosen because it maps cleanly onto the emotions that drive behavioral memory encoding in conversational contexts.

## Training Methodology

- **Base model:** [SamLowe/roberta-base-go_emotions](https://huggingface.co/SamLowe/roberta-base-go_emotions) — RoBERTa-base already pre-adapted to emotion classification on GoEmotions (28 labels)
- **Head:** fresh 10-class classification head (random init)
- **Domain data:** 433 Opus-labeled conversational sentences, targeted at the weak buckets (anxiety, embarrassment, envy, ennui) — weighted 3x during training for high signal
- **Background data:** Google GoEmotions `simplified` config, 28 labels remapped to the 10 Inside Out classes (priority order: rarest-label-wins for multi-label cases)
- **Balancing:** max 3000 samples/class, min 200 samples/class
- **Hyperparameters:** 4 epochs, batch 32, learning rate 2e-5, AdamW, FP32
- **Hardware:** 1× NVIDIA A40 (48GB)
- **Wall time:** ~12 minutes

## Why Domain-Specific Beats Larger Models

Prior to this fine-tune we benchmarked [microsoft/deberta-v3-large](https://huggingface.co/microsoft/deberta-v3-large) fine-tuned on GoEmotions. It showed **no meaningful gain** over the RoBERTa-base baseline for our 10-class downstream task. The real win came from three choices:

1. **Conversational training data** — 433 Opus-labeled sentences from real agent-memory contexts, not Reddit comments.
2. **Reduced label space** — 10 clear buckets vs GoEmotions' 28 (many of which are sparsely populated or overlap).
3. **High-agreement labels** — Opus-labeled set had strong inter-annotator consistency on the target labels.

Larger model ≠ better when the bottleneck is label quality + domain match.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("Kova-Mind/emotion-v1")
model = AutoModelForSequenceClassification.from_pretrained("Kova-Mind/emotion-v1")
model.eval()

text = "I just got the job!"
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=256)
with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)
    pred_id = torch.argmax(probs, dim=-1).item()

print(f"{model.config.id2label[pred_id]} ({probs[0, pred_id]:.3f})")
```

Or with the pipeline API:

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Kova-Mind/emotion-v1", top_k=None)
print(clf("I have a huge presentation tomorrow and I can't stop overthinking it."))
# → anxiety (top class)
```

## Limitations

- **English only.** No multilingual training data.
- **Conversational AI context.** Optimized for agent-memory ingestion of natural user dialog. May underperform on social-media, legal, or heavily-stylized text.
- **10-class granularity.** Does not capture finer emotional shades (e.g. admiration vs pride, grief vs sadness, amusement vs joy). Those get absorbed into the closest bucket.
- **Opinionated taxonomy.** The Inside Out 2 bias toward anxiety / embarrassment / envy / ennui reflects what matters for long-term memory encoding in agents; other applications may want a different split.
- **Single-label output.** Trained with single-label resolution (rarest-wins tie-break). For multi-label emotion, a different head is needed.

## Citation

```bibtex
@misc{capo2026kovamindemotion,
  author       = {Capo, Alejandro},
  title        = {KovaMind Emotion v1: Domain-Specific Fine-Tuning Beats Larger Models for Conversational Emotion Classification},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Kova-Mind/emotion-v1}}
}
```

## Built By

[kovamind.io](https://kovamind.io) — private, customer-owned AI memory infrastructure.

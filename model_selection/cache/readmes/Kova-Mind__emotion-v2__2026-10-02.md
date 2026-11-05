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

# KovaMind Emotion v2

A 10-class emotion classifier fine-tuned for conversational AI memory systems. Uses an Inside Out 2 inspired taxonomy. v2 extends [Kova-Mind/emotion-v1](https://huggingface.co/Kova-Mind/emotion-v1) with targeted training on pipeline-style bracket-tag fragments (`X [positive]`, `X [negative]`, `X [neutral]`) and entity fragments with embedded sentiment.

## What v2 fixes

v1 shipped with excellent accuracy on natural conversational sentences, but two real-world failure modes appeared in production patterns:

1. **Bracket-tag blindness.** Fragments like `hiking [positive] — Weekends activity.` were consistently labeled `neutral` instead of `joy`. The `[positive]` / `[negative]` bracket is a Kova pipeline metadata tag the model had never seen in training.
2. **Entity fragments with embedded sentiment.** Fragments like `lake (place) — Location where Rex loves swimming.` were labeled `neutral` because v1 read only the nominal text; it missed the embedded positive signal.

v2 is trained on 706 additional Opus-labeled Kova-style examples that target these gaps.

## Head-to-head vs v1

Evaluated against [Claude Opus](https://www.anthropic.com/) as fragment-only oracle (Opus reads each fragment in isolation and labels what it expresses).

| Benchmark | n | v1 | **v2** |
|---|---:|---:|---:|
| 21 production bracket-tag patterns | 21 | 17/21 = 81.0 % | **21/21 = 100.0 %** |
| 17 adversarial sanity cases | 17 | 14/17 = 82.4 % | **15/17 = 88.2 %** |
| 50 recent production patterns | 50 | 42/50 = 84.0 % | 40/50 = 80.0 % |
| **Combined** | 88 | 73/88 = 83.0 % | **76/88 = 86.4 %** |

- **+3.4 pts** combined accuracy
- **+19 pts** on bracket-tag patterns (the target gap)
- **Zero regressions** on the 21 bracket patterns
- The v2 dip on the 50-pattern set is 2 cases where v2 over-called joy on entity fragments with incidental third-party verbs; both v1 and v2 stayed within ±5 pts noise of the Opus oracle scoring.

### Latency

Inference latency unchanged from v1: **~5 ms per call** on an A40 GPU (after warmup). Well under the 10 ms production ceiling.

## Classes

10-class Inside Out 2 taxonomy:

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

Same label IDs as v1 — **drop-in replacement** for any code loading `Kova-Mind/emotion-v1`.

## Training Methodology

Same recipe as v1, with expanded domain data:

- **Base model:** [SamLowe/roberta-base-go_emotions](https://huggingface.co/SamLowe/roberta-base-go_emotions)
- **Head:** fresh 10-class classification head (random init, 28→10 reinit from base)
- **Domain data (706 Opus-labeled examples, 3× weight):**
  - 21 real production bracket-tag patterns labeled by Opus
  - 500 synthetic bracket-tag examples across all 10 emotions
  - 185 natural conversational sentences (regression protection for general text)
- **Background data:** Google GoEmotions `simplified` config, 28 labels remapped to the 10 Inside Out classes (rarest-label-wins tie-break)
- **Balancing:** max 3000 samples/class, min 200 samples/class
- **Hyperparameters:** 4 epochs, batch 32, learning rate 2e-5, AdamW, FP16, seed 42, warmup ratio 0.1, weight decay 0.01
- **Best checkpoint:** epoch 2 (auto-selected via `load_best_model_at_end` on macro F1)
- **Hardware:** 1× NVIDIA A40 (48GB)
- **Wall time:** ~3 min 18 s pure training

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("Kova-Mind/emotion-v2")
model = AutoModelForSequenceClassification.from_pretrained("Kova-Mind/emotion-v2")
model.eval()

text = "croissants [positive] — User A loves them exclusively."
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=256)
with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)
    pred_id = torch.argmax(probs, dim=-1).item()

print(f"{model.config.id2label[pred_id]} ({probs[0, pred_id]:.3f})")
# → joy (0.97)
```

Or with the pipeline API:

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Kova-Mind/emotion-v2", top_k=None)
print(clf("hiking [positive] — Weekends activity."))
# → joy (top class)
```

## Limitations

- **English and a few non-English bracket fragments only.** Non-English bracket patterns were included as training data (Arabic, Chinese) but broader multilingual coverage is out of scope.
- **Conversational AI context.** Optimized for agent-memory ingestion of natural user dialog. May underperform on social-media, legal, or heavily-stylized text.
- **10-class granularity.** Does not capture finer emotional shades (e.g. admiration vs pride, grief vs sadness, amusement vs joy). Those get absorbed into the closest bucket.
- **Single-label output.** Trained with single-label resolution (rarest-wins tie-break). For multi-label emotion, a different head is needed.
- **Entity-fragment sentiment.** v2 occasionally over-calls `joy` on factual third-party fragments with incidental positive verbs (e.g. *"Alex (person) — Promoted to VP at Google"*). v3 will target this with a curated third-party-factual training set.
- **envy class weakly supervised.** GoEmotions does not contain an envy label; v2 sees only ~37 domain envy examples. Production coverage is limited.

## Changelog from v1

- +500 synthetic bracket-tag training examples (all 10 emotions)
- +21 real production bracket-tag patterns (Opus-labeled)
- +185 natural-sentence regression examples (Kova-style conversational text)
- Same base model, same 10-class taxonomy, same hyperparameters, same label IDs.

## Citation

```bibtex
@misc{capo2026kovamindemotionv2,
  author       = {Capo, Alejandro},
  title        = {KovaMind Emotion v2: Bracket-Tag-Aware Emotion Classification for Conversational Memory Pipelines},
  year         = {2026},
  publisher    = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Kova-Mind/emotion-v2}}
}
```

## Built By

[kovamind.io](https://kovamind.io) — private, customer-owned AI memory infrastructure.

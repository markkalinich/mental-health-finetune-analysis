---
license: mit
base_model: jhu-clsp/ettin-encoder-68m
pipeline_tag: text-classification
tags:
- emotion
- multi-label
- go-emotions
- modernbert
- ettin
- roleplay
library_name: transformers
language:
- en
---

# ettin-emotion-28-multilabel-68m

A 68M-parameter **multi-label emotion classifier** over the 28 [GoEmotions](https://github.com/google-research/google-research/tree/master/goemotions) categories, fine-tuned from [`jhu-clsp/ettin-encoder-68m`](https://huggingface.co/jhu-clsp/ettin-encoder-68m) (ModernBERT architecture, 8K context, mean pooling).

Unlike most public GoEmotions models — which are **single-label** (softmax, one emotion per text) and trained only on short Reddit comments — this model is genuinely **multi-label** (sigmoid, any number of co-occurring emotions) and is tuned to work on **narration / roleplay prose**: 3rd-person description, action asterisks, 2nd-person, inner monologue, and dialogue, where several emotions usually co-occur in one passage.

## Labels (28)

`admiration, amusement, anger, annoyance, approval, caring, confusion, curiosity, desire, disappointment, disapproval, disgust, embarrassment, excitement, fear, gratitude, grief, joy, love, nervousness, optimism, pride, realization, relief, remorse, sadness, surprise, neutral`

Output is one independent sigmoid probability per label. Threshold each probability at **0.5** to get the multi-hot prediction — nothing else to look up. The per-class thresholds tuned on validation have already been **folded into the classifier bias**, so a flat 0.5 reproduces the tuned decisions (this is why `thresholds.json` lists 0.5 for every class). One consequence: the probabilities are calibrated so that **0.5 is the decision boundary**, not so that the number reads as a confidence — don't interpret a raw sigmoid value as "% sure."

## Results

Evaluated on 481 hand-checked roleplay passages (`gold_rp`), never seen in training. Baseline is `joeddav/distilbert-base-uncased-go-emotions-student`, the common off-the-shelf GoEmotions model, scored on the same set.

| Metric | Baseline (joeddav) | **This model** |
|---|---|---|
| micro-F1 (all) | 22% | **52%** |
| macro-F1 | 19% | **42%** |
| macro-F1 (supported classes) | — | **48%** |
| subset accuracy | — | **18%** |

Micro-F1 by writing style (95% CI, conversation-level bootstrap):

| Style | n | Baseline | **This model** |
|---|---|---|---|
| narration | 350 | 22% | **55% (51–58)** |
| second_person | 130 | 24% | **54% (48–59)** |
| inner_monologue | 63 | 16% | **46% (38–55)** |
| dialogue | 245 | 23% | **50% (45–53)** |

The gap is largest exactly where the off-the-shelf model is out of distribution: multi-emotion narration.

## Training data

- **[GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions)** (SetFit multi-label variant, ~43k) — the in-domain Reddit anchor, natural ~33% neutral kept.
- **LLM-generated narration/roleplay** across all four styles, engineered around known LLM labeling failure modes so the synthetic data doesn't poison the classifier.
- Additional mined/prepped sources (EmpatheticDialogues, news, wiki, neutral mining).

Train/val split by conversation id (no passage leakage); the gold RP set is frozen and never trained on.

## Usage (transformers)

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

name = "chartreuse-verte/ettin-emotion-28-multilabel-68m"
tok = AutoTokenizer.from_pretrained(name)
model = AutoModelForSequenceClassification.from_pretrained(name).eval()

text = "*She backed away slowly, hands trembling, unsure if she could trust him.*"
enc = tok(text, return_tensors="pt", truncation=True, max_length=256)
with torch.no_grad():
    probs = torch.sigmoid(model(**enc).logits)[0]

labels = [model.config.id2label[i] for i in range(len(probs))]
for label, p in sorted(zip(labels, probs.tolist()), key=lambda x: -x[1])[:5]:
    print(f"{label:14s} {p:.2f}")
# nervousness 1.00 | confusion 0.80 | fear 0.48 | ...
```

## Quantized / alternative runtimes

The root of this repo is the raw fp32 transformers weights. Quantized and alternative-runtime versions ship in subfolders:

- **`onnx/model.onnx`** — ONNX, fp32.
- **`onnx/model_quantized.onnx`** — ONNX dynamic int8, ~4× smaller, CPU-only, no torch. Agrees with the fp32 model on 98% of threshold decisions on the test set.
- **`gguf/*.gguf`** — f16 and q8_0 for llama.cpp. Converted with `convert_hf_to_gguf.py`; the 28 output labels are embedded in the GGUF metadata (`modern-bert.classifier.output_labels`). Requires a llama.cpp build with ModernBERT classification support. Apply sigmoid + threshold to the returned logits yourself.

ONNX int8 example (download the `onnx/` folder + the root tokenizer):

```python
import numpy as np, onnxruntime as ort
from transformers import AutoTokenizer
tok = AutoTokenizer.from_pretrained("chartreuse-verte/ettin-emotion-28-multilabel-68m")
sess = ort.InferenceSession("onnx/model_quantized.onnx")
enc = tok("Thanks, that means a lot.", return_tensors="np", truncation=True, max_length=256)
feed = {i.name: enc[i.name] for i in sess.get_inputs()}
logits = sess.run(None, feed)[0][0]
probs = 1 / (1 + np.exp(-logits))   # sigmoid, multi-label
```

## Notes & limitations

- Labels are 28 GoEmotions categories; nuance outside that taxonomy is collapsed.
- Gold labels and style tags are LLM-annotated, not fully human-reviewed — small differences are within labeling noise.
- Max sequence length used at train/eval time is 256 tokens (the base supports 8K).
- License: **MIT** (inherited from the Ettin base model).

---
license: apache-2.0
language: en
pipeline_tag: text-classification
tags:
  - deberta-v2
  - deberta-v3
  - sentiment-analysis
  - federal-reserve
  - economics
  - finance
  - central-bank-communication
  - fomc
  - domain-adaptive-pretraining
widget:
  - text: "The Committee judges that the risks to the outlook for economic activity are weighted to the downside."
    example_title: "Negative example (pessimistic economic assessment)"
  - text: "Economic activity has continued to expand at a solid pace, and labor market conditions remain strong."
    example_title: "Positive example (optimistic economic assessment)"
---

# FedDeBERTa-DAPT

`FedDeBERTa-DAPT` is a fine-tuned [`microsoft/deberta-v3-base`](https://huggingface.co/microsoft/deberta-v3-base) model for binary **sentiment** classification of Federal Reserve communications (FOMC statements, minutes, and related monetary-policy text), classifying a sentence's economic-assessment tone as **Positive** (optimistic — language suggesting economic strength, growth, or confidence in the outlook) or **Negative** (pessimistic — language suggesting economic weakness, decline, or concern about conditions).

**Sentiment is not the same task as monetary-policy stance.** Stance classification asks whether policy is easing or tightening (dovish vs. hawkish); sentiment, as used here, asks only whether the text characterizes economic conditions positively or negatively. The two are related — markets sometimes read expressed economic concern as a signal of anticipated easing, and expressed optimism as a signal of anticipated tightening — but sentiment is not a policy vote and is not a substitute for stance. This model was trained and evaluated on sentiment labels only; it does not predict monetary-policy stance.

This is the **DAPT** (Domain-Adaptive Pretraining) variant: before task fine-tuning, the backbone underwent continued masked-language-model pretraining on a Federal Reserve communications corpus, then was fine-tuned on the same labeled sentiment task as the companion [`FedDeBERTa`](https://huggingface.co/cbenne23/FedDeBERTa) BASE model. (Exact DAPT pretraining corpus size, steps, and MLM configuration are documented in the dissertation methods chapter — not restated here to avoid restating unverified figures from memory; can be added on request.)

Both models were developed as part of the dissertation *"Domain Adaptive Pretraining for Federal Reserve Sentiment Analysis: A Systematic Study of Small-Corpus Adaptation, Knowledge Distillation, and Cross-Bank Transfer"* by Christopher S. Bennett, University of Arkansas at Little Rock.

## ⚠️ Disclaimer

This is an academic research artifact released alongside a dissertation. It is **not intended as financial or investment advice**, and outputs should not be used as the sole basis for trading, investment, or policy decisions. Performance figures below reflect a held-out academic test set and may not generalize to other time periods, institutions, or communication styles. Use in any production or decision-making context is at the deployer's own risk.

## Model details

| | |
|---|---|
| Base architecture | `DebertaV2ForSequenceClassification` (DeBERTa-v3-base backbone, domain-adaptively pretrained) |
| Hidden size | 768 |
| Layers / attention heads | 12 / 12 |
| Tokenizer | SentencePiece (Unigram), 128,001 vocabulary entries — byte-identical to the BASE model's tokenizer (verified via SHA-256) |
| Labels | `0: Negative`, `1: Positive` |
| Dropout (attention / hidden) | 0.1 / 0.1 |
| License | Apache-2.0 |

**A note on `vocab_size`:** unlike the BASE model, this checkpoint's `config.json` reports `vocab_size: 128001`, exactly matching the tokenizer's embedding matrix shape `(128001, 768)`. The continued-pretraining step resized the embedding matrix down from the upstream 128,100-row buffer to the tokenizer's actual vocabulary size. Both models are internally consistent and were verified via a live forward-pass smoke test before release; see `REPRODUCIBILITY.md` in the [companion GitHub repo](https://github.com/cbenne23/FedDeBERTa) for details.

## Training data

Fine-tuned on the same labeled corpus of Federal Reserve communication sentences as the BASE model (source file referenced internally as `FED_prelabelled_sent_fixed.csv`), with each sentence labeled Positive or Negative for economic-assessment tone. Full dataset construction, domain-adaptive pretraining corpus, and labeling methodology are described in the dissertation.

## Evaluation

Evaluated on the same frozen, grouped stratified 80/20 held-out test split as the BASE model (seed=42, N=1,322: 718 Negative / 604 Positive), verified independently against archived model predictions and cross-checked row-by-row against the frozen split manifest (100% match).

| Metric | Value |
|---|---|
| Weighted F1 | 81.35% |
| Accuracy | 81.39% |
| Negative — precision / recall / F1 | 0.8164 / 0.8482 / 0.8320 |
| Positive — precision / recall / F1 | 0.8108 / 0.7732 / 0.7915 |

Compared to the BASE variant, this DAPT model shows a small point-estimate improvement (ΔF1-weighted = +0.16pp) that is **not statistically significant** at this sample size (95% CI [-1.44, +1.76]pp, Holm-corrected p = 1.000, McNemar's test). Framed accurately: DAPT is the point-estimate leader on this test set, not a statistically superior model. See the dissertation and `REPRODUCIBILITY.md` for the full statistical methodology.

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("cbenne23/FedDeBERTa-DAPT")
model = AutoModelForSequenceClassification.from_pretrained("cbenne23/FedDeBERTa-DAPT")
model.eval()

text = "The Committee judges that the risks to the outlook for economic activity are weighted to the downside."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    logits = model(**inputs).logits
pred_id = torch.argmax(logits, dim=-1).item()
print(model.config.id2label[pred_id])  # "Negative"
```

## Checkpoint integrity

`model.safetensors` SHA-256: `2883b6ed9507278c7ff9da9359b6c81e50de15135a56537b739ba6fb2d98c574`

## Citation

If you use this model, please cite the dissertation:

```bibtex
@phdthesis{bennett_fed_sentiment,
  author = {Bennett, Christopher S.},
  title  = {Domain Adaptive Pretraining for Federal Reserve Sentiment Analysis: A Systematic Study of Small-Corpus Adaptation, Knowledge Distillation, and Cross-Bank Transfer},
  school = {University of Arkansas at Little Rock},
  year   = {2026}
}
```

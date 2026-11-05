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
widget:
  - text: "The Committee judges that the risks to the outlook for economic activity are weighted to the downside."
    example_title: "Negative example (pessimistic economic assessment)"
  - text: "Economic activity has continued to expand at a solid pace, and labor market conditions remain strong."
    example_title: "Positive example (optimistic economic assessment)"
---

# FedDeBERTa

`FedDeBERTa` is a fine-tuned [`microsoft/deberta-v3-base`](https://huggingface.co/microsoft/deberta-v3-base) model for binary **sentiment** classification of Federal Reserve communications (FOMC statements, minutes, and related monetary-policy text). It classifies a sentence's economic-assessment tone as **Positive** (optimistic — language suggesting economic strength, growth, or confidence in the outlook) or **Negative** (pessimistic — language suggesting economic weakness, decline, or concern about conditions).

**Sentiment is not the same task as monetary-policy stance.** Stance classification asks whether policy is easing or tightening (dovish vs. hawkish); sentiment, as used here, asks only whether the text characterizes economic conditions positively or negatively. The two are related — markets sometimes read expressed economic concern as a signal of anticipated easing, and expressed optimism as a signal of anticipated tightening — but sentiment is not a policy vote and is not a substitute for stance. This model was trained and evaluated on sentiment labels only; it does not predict monetary-policy stance.

This is the **BASE** variant, fine-tuned directly from the general-purpose `deberta-v3-base` checkpoint (no domain-adaptive pretraining). A companion model, [`FedDeBERTa-DAPT`](https://huggingface.co/cbenne23/FedDeBERTa-DAPT), applies continued domain-adaptive pretraining on Federal Reserve text before fine-tuning on the same task.

Both models were developed as part of the dissertation *"Domain Adaptive Pretraining for Federal Reserve Sentiment Analysis: A Systematic Study of Small-Corpus Adaptation, Knowledge Distillation, and Cross-Bank Transfer"* by Christopher S. Bennett, University of Arkansas at Little Rock.

## ⚠️ Disclaimer

This is an academic research artifact released alongside a dissertation. It is **not intended as financial or investment advice**, and outputs should not be used as the sole basis for trading, investment, or policy decisions. Performance figures below reflect a held-out academic test set and may not generalize to other time periods, institutions, or communication styles. Use in any production or decision-making context is at the deployer's own risk.

## Model details

| | |
|---|---|
| Base architecture | `DebertaV2ForSequenceClassification` (DeBERTa-v3-base backbone) |
| Hidden size | 768 |
| Layers / attention heads | 12 / 12 |
| Tokenizer | SentencePiece (Unigram), 128,001 vocabulary entries |
| Labels | `0: Negative`, `1: Positive` |
| Dropout (attention / hidden) | 0.05 / 0.05 |
| License | Apache-2.0 |

**A note on `vocab_size`:** this model's `config.json` reports `vocab_size: 128100`, and its embedding matrix has shape `(128100, 768)` — 99 rows larger than the tokenizer's actual 128,001-entry vocabulary. This is an inherited quirk from the upstream `microsoft/deberta-v3-base` checkpoint (99 reserved/unused embedding rows that no token id can ever reach) rather than a bug specific to this fine-tune; it was verified empirically before release and has no effect on model behavior. See `REPRODUCIBILITY.md` in the [companion GitHub repo](https://github.com/cbenne23/FedDeBERTa) for details.

## Training data

Fine-tuned on a labeled corpus of Federal Reserve communication sentences (source file referenced internally as `FED_prelabelled_sent_fixed.csv`), with each sentence labeled Positive or Negative for economic-assessment tone. Full dataset construction and labeling methodology are described in the dissertation.

## Evaluation

Evaluated on a frozen, grouped stratified 80/20 held-out test split (seed=42, N=1,322: 718 Negative / 604 Positive), verified independently against archived model predictions and cross-checked row-by-row against the frozen split manifest (100% match).

| Metric | Value |
|---|---|
| Weighted F1 | 81.19% |
| Accuracy | 81.24% |
| Negative — precision / recall / F1 | 0.8133 / 0.8496 / 0.8311 |
| Positive — precision / recall / F1 | 0.8112 / 0.7682 / 0.7891 |

Compared to the DAPT variant, this BASE model performs within statistical noise of the DAPT model on this test set (ΔF1-weighted = +0.16pp favoring DAPT, 95% CI [-1.44, +1.76]pp, Holm-corrected p = 1.000 — not statistically significant). See the dissertation and `REPRODUCIBILITY.md` for the full statistical methodology (McNemar's test, Holm-Bonferroni correction, bootstrap CIs).

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("cbenne23/FedDeBERTa")
model = AutoModelForSequenceClassification.from_pretrained("cbenne23/FedDeBERTa")
model.eval()

text = "The Committee judges that the risks to the outlook for economic activity are weighted to the downside."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
with torch.no_grad():
    logits = model(**inputs).logits
pred_id = torch.argmax(logits, dim=-1).item()
print(model.config.id2label[pred_id])  # "Negative"
```

## Checkpoint integrity

`model.safetensors` SHA-256: `aef5deed2088793e9a416ca7ea7c89ee9d1bd01d9c64886f41a9e82c7af6a188`

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

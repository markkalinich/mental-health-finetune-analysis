---
language: en
license: apache-2.0
base_model: roberta-base
tags:
  - text-classification
  - finance
  - sentiment-analysis
  - earnings
  - semiconductor
datasets:
  - financial_phrasebank
pipeline_tag: text-classification
model-index:
  - name: earningsbert-semiconductor
    results:
      - task:
          type: text-classification
        metrics:
          - type: f1
            value: 0.986
            name: Macro F1
          - type: accuracy
            value: 0.987
            name: Accuracy
---

# EarningsBERT — Semiconductor Earnings Sentiment Classifier

**Model ID:** `nishantnayar/earningsbert-semiconductor`
**Base model:** `roberta-base`
**Task:** Text classification (6-class sentiment)
**Domain:** Semiconductor sector earnings press releases

---

## Model Description

EarningsBERT is a fine-tuned RoBERTa-base model for classifying sentences from semiconductor earnings press releases into a 6-class taxonomy. Unlike general-purpose finance sentiment models (positive/negative/neutral), EarningsBERT includes two guidance-specific classes — `guidance_raise` and `guidance_lower` — which are the strongest predictors of post-earnings stock direction.

### Label Mapping

| ID | Label | Economic signal |
|---|---|---|
| 0 | `optimistic` | Bullish tone |
| 1 | `cautious` | Bearish lean |
| 2 | `hedging` | Uncertainty / vagueness |
| 3 | `guidance_raise` | Strong bullish — explicit guidance increase |
| 4 | `guidance_lower` | Strong bearish — explicit guidance decrease |
| 5 | `neutral` | No signal (boilerplate, logistics) |

---

## Intended Use

- Sentence-level sentiment classification for semiconductor earnings press releases
- Feature generation for post-earnings stock direction models
- Research into language patterns in corporate communications

**Not intended for:** general financial text, non-semiconductor sectors, investment decisions.

---

## Training Data

| Source | Size | Labels |
|---|---|---|
| Financial PhraseBank (Malo et al. 2014) | 2,264 sentences | positive → optimistic, negative → cautious, neutral → neutral |
| Silver-labeled semiconductor transcripts | ~3,000 sentences | All 6 classes via rule-based labeler |
| **Total** | **~5,000 sentences** | **6 classes, balanced** |

**Silver labeling rules** use Loughran-McDonald lexicon density, modal verb density, approximation density, and semiconductor-specific phrase matching (`"guidance raised"`, `"inventory digestion"`, etc.).

---

## Performance

Evaluated on a held-out split (20% stratified by class):

| Metric | Value |
|---|---|
| Macro F1 | 0.986 |
| Accuracy | 0.987 |
| `guidance_raise` precision | >0.95 |
| `guidance_lower` precision | >0.95 |

Training stopped at epoch 2 (early stopping on macro-F1) to avoid overfitting.

---

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="nishantnayar/earningsbert-semiconductor",
    return_all_scores=True,
)

result = classifier("We are raising our Q3 gross margin guidance to 57%, up from our prior range of 54-55%.")
# [{'label': 'guidance_raise', 'score': 0.94}, ...]
```

Or using the project wrapper:

```python
from src.earningsbert.model_wrapper import EarningsBERT

model = EarningsBERT("nishantnayar/earningsbert-semiconductor")
scores = model.predict(["Record data center revenue driven by AI demand."])
# [{'optimistic': 0.89, 'cautious': 0.02, ...}]
```

---

## Limitations

- Trained exclusively on semiconductor sector language. Performance on other sectors is untested.
- EDGAR 8-K press releases only — not trained on live earnings call Q&A transcripts.
- Silver labels carry ~15-20% noise. `guidance_raise`/`guidance_lower` rules are highest precision; `hedging` is noisiest.
- Base model cutoff: roberta-base (2019). Post-2023 terminology (CoWoS, HBM3e) may be underrepresented.

---

## Citation

If you use this model, please cite:

```
@misc{earningsbert2024,
  title  = {EarningsBERT: Semiconductor Earnings Sentiment Classifier},
  author = {[Your Name]},
  year   = {2024},
  url    = {https://huggingface.co/nishantnayar/earningsbert-semiconductor}
}
```

---

## How to Push

```bash
# 1. Set hub_model_id in config.yaml:
#    earningsbert:
#      hub_model_id: "your-username/earningsbert-semiconductor"

# 2. Login
huggingface-cli login

# 3. Push (after training)
python -m src.cli.main finetune --push-to-hub
```

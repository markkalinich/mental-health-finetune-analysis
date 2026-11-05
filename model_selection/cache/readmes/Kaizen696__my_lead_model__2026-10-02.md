---
license: apache-2.0
pipeline_tag: text-classification
tags:
- text-classification
- distilbert
- sentiment-analysis
- sales-leads
---

# DistilBERT Sales Lead Classification Model (v2 — Domain Adapted)

This model is a fine-tuned version of `distilbert-base-uncased`, trained in two stages to score sales leads by sentiment for CRM lead prioritization.

## Training Pipeline

**Stage 1 — Base Fine-Tune:** Trained on the [Financial PhraseBank](https://huggingface.co/datasets/takala/financial_phrasebank) dataset (`sentences_75agree` config) for 3-class sentiment classification (negative / neutral / positive), replacing an earlier Rotten Tomatoes movie-review proxy with business-domain text.

**Stage 2 — Sales Domain Adaptation:** Continued training on a 240-example, hand-authored dataset of sales/CRM lead interaction sentences (80 per class), covering patterns the base model struggled with — negation ("not interested"), competitor retention ("happy with current vendor"), budget objections, and clear buying signals. Trained with a low learning rate (2e-5) to adapt without catastrophic forgetting of the base.

## Training Results

**Stage 1 (Financial PhraseBank, 2 epochs):**

| Epoch | Validation Loss | Accuracy | F1 |
| :---: | :---: | :---: | :---: |
| 1 | 0.6292 | 0.6918 | 0.6910 |
| 2 | 0.5157 | 0.7887 | 0.7915 |

**Stage 2 (Sales domain adaptation, 3 epochs):**

| Epoch | Validation Loss | Accuracy | F1 |
| :---: | :---: | :---: | :---: |
| 1 | 0.7432 | 0.6667 | 0.6708 |
| 2 | 0.5064 | 0.8542 | 0.8527 |
| 3 | 0.4830 | 0.8542 | 0.8543 |

Final model achieves **85.4% accuracy** on held-out sales-domain sentences.

## Labels

- `0` — Negative (lost lead / not interested / competitor retention)
- `1` — Neutral (hedging / evaluating / no decision yet)
- `2` — Positive (buying signal / ready to move forward)

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="kaizen696/my_lead_model"
)

# Example: High Quality
print(classifier("Budget is approved, excited to move forward."))

# Example: Low Quality
print(classifier("Not interested at all, too expensive."))
```

## Known Limitations

- Trained on a small (240-example) domain-adaptation set — may still misclassify sentences with mixed lexical signals (e.g. positive-sounding words like "happy" paired with a negative outcome, such as "happy with their current vendor").
- Financial PhraseBank base introduces some finance-specific vocabulary bias not fully corrected by the sales fine-tune.
- Recommended as a lead-prioritization signal, not a sole decision-making input.
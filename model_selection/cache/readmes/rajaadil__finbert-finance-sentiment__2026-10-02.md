---
license: apache-2.0
language:
- en
base_model: ProsusAI/finbert
tags:
- text-classification
- sentiment-analysis
- finance
- financial-sentiment
- finbert
datasets:
- takala/financial_phrasebank
metrics:
- accuracy
- f1
pipeline_tag: text-classification
widget:
- text: "The company reported record profits and raised its dividend."
- text: "Shares plunged after the firm missed earnings expectations."
- text: "The board will meet next quarter to review the annual budget."
---

# finbert-finance-sentiment

A 3-class **financial sentiment** model that labels English financial text as **positive**, **negative**, or **neutral**. It is a fine-tuned version of [`ProsusAI/finbert`](https://huggingface.co/ProsusAI/finbert), further trained on the Financial PhraseBank dataset.

## Model description

The model takes a sentence of financial text — such as a line from a news headline, earnings report, or market commentary — and predicts its sentiment. It builds on FinBERT, a BERT model pretrained on a large financial corpus, and sharpens it on expert-annotated financial sentences.

- **Base model:** ProsusAI/finbert
- **Task:** 3-class sentiment classification (text-classification)
- **Language:** English (financial domain)
- **Labels:** `negative` (0), `neutral` (1), `positive` (2)

## Intended uses & limitations

**Intended uses:** Sentiment scoring of financial text — news headlines, earnings commentary, analyst notes, and similar short financial statements.

**Limitations:**
- English and financial domain only; performance on general or non-financial text will be weaker.
- Trained on relatively formal financial news sentences, so very informal text (e.g. social media slang, tickers, memes) may be less reliable.
- Sentiment here means market/financial tone, not personal opinion — "shares fell" is negative regardless of phrasing.

## How to use

```python
from transformers import pipeline

clf = pipeline("text-classification", model="rajaadil/finbert-finance-sentiment")
print(clf("The company reported record profits and raised its dividend."))
# [{'label': 'positive', 'score': 0.97}]
```

## Training data

Trained on the **`sentences_allagree`** subset of the [Financial PhraseBank](https://huggingface.co/datasets/takala/financial_phrasebank) dataset — the highest-quality subset, containing only sentences where all human annotators agreed on the label.

- **Split:** 80% train / 20% test
- **Classes:** negative, neutral, positive (neutral is the majority class)

## Training procedure

| Hyperparameter | Value |
|---|---|
| Base model | ProsusAI/finbert |
| Epochs | 4 (best checkpoint kept) |
| Train batch size | 16 |
| Learning rate | 2e-5 |
| Max sequence length | 128 |
| Best model selected on | macro-F1 |

## Evaluation results

Best checkpoint (epoch 3), evaluated on the held-out test set:

| Metric | Value |
|---|---|
| Accuracy | 0.820 |
| F1 (macro) | 0.811 |

Macro-F1 is reported alongside accuracy because the dataset is class-imbalanced (neutral is the majority class); macro-F1 reflects performance across all three classes rather than favouring the majority.

## Framework versions

- Transformers
- PyTorch
- Datasets

## Author

Built by [rajaadil](https://huggingface.co/rajaadil).
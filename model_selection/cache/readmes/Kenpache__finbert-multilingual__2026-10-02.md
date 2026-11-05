---
license: apache-2.0
language:
  - en
  - zh
  - ja
  - de
  - fr
  - es
tags:
  - finance
  - sentiment-analysis
  - multilingual
  - xlm-roberta
  - finbert
datasets:
  - Kenpache/multilingual-financial-sentiment
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
model-index:
  - name: FinBERT-Multilingual
    results:
      - task:
          type: text-classification
          name: Financial Sentiment Analysis
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.8103
          - name: F1 (weighted)
            type: f1
            value: 0.8102
---

# FinBERT-Multilingual

A multilingual extension of the FinBERT paradigm: domain-adapted transformer for financial sentiment classification across six languages (EN, ZH, JA, DE, FR, ES).

While the original [FinBERT](https://arxiv.org/abs/1908.10063) demonstrated the effectiveness of domain-specific pre-training for English financial NLP, this model extends that approach to a multilingual setting using XLM-RoBERTa-base as the backbone, enabling cross-lingual financial sentiment analysis without language-specific models.

## Model Architecture

- **Base model:** `xlm-roberta-base` (278M parameters)
- **Task:** 3-class sequence classification (Negative / Neutral / Positive)
- **Domain adaptation:** Task-Adaptive Pre-Training (TAPT) via Masked Language Modeling on 35K+ financial texts
- **Languages:** English, Chinese, Japanese, German, French, Spanish

## Training Pipeline

### Stage 1: Task-Adaptive Pre-Training (TAPT)

Following [Gururangan et al. (2020)](https://arxiv.org/abs/2004.10964), we perform continued MLM pre-training on the unlabeled financial corpus to adapt the model's representations to the financial domain. This stage exposes the model to domain-specific vocabulary and discourse patterns across all six target languages using approximately 35,000 financial text samples.

### Stage 2: Supervised Fine-Tuning

The domain-adapted model is then fine-tuned on the labeled sentiment classification task.

**Hyperparameters:**

| Parameter | Value |
|---|---|
| Learning rate | 2e-5 |
| LR scheduler | Cosine annealing |
| Label smoothing | 0.1 |
| Checkpoint selection | SWA (top-3 checkpoints) |
| Base model | xlm-roberta-base |

**Stochastic Weight Averaging (SWA):** Rather than selecting a single best checkpoint, we average the weights of the top-3 performing checkpoints. This produces a flatter loss minimum and more robust generalization, particularly beneficial for multilingual settings where overfitting to dominant languages is a risk.

**Label smoothing (0.1):** Prevents overconfident predictions and improves calibration, which is important for financial applications where prediction confidence informs downstream decisions.

## Evaluation Results

### Overall Metrics

| Metric | Score |
|---|---|
| Accuracy | 0.8103 |
| F1 (weighted) | 0.8102 |
| Precision (weighted) | 0.8111 |
| Recall (weighted) | 0.8103 |

### Per-Class Performance

| Class | Precision | Recall | F1-Score |
|---|---|---|---|
| Negative | 0.78 | 0.83 | 0.81 |
| Neutral | 0.83 | 0.79 | 0.81 |
| Positive | 0.80 | 0.82 | 0.81 |

The balanced per-class performance (all F1 scores at 0.81) indicates that the model does not exhibit significant class bias, despite the imbalanced training distribution (Neutral: 45.5%, Positive: 30.8%, Negative: 23.7%).

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Kenpache/finbert-multilingual")

# English
classifier("The company reported record quarterly earnings, driven by strong demand.")
# [{'label': 'positive', 'score': 0.95}]

# German
classifier("Die Aktie verlor nach der Gewinnwarnung deutlich an Wert.")
# [{'label': 'negative', 'score': 0.92}]

# Japanese
classifier("同社の売上高は前年同期比で横ばいとなった。")
# [{'label': 'neutral', 'score': 0.88}]

# Chinese
classifier("该公司宣布大规模裁员计划，股价应声下跌。")
# [{'label': 'negative', 'score': 0.91}]
```

### Direct Model Loading

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tokenizer = AutoTokenizer.from_pretrained("Kenpache/finbert-multilingual")
model = AutoModelForSequenceClassification.from_pretrained("Kenpache/finbert-multilingual")

text = "Les bénéfices du groupe ont augmenté de 15% au premier trimestre."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)

with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=-1)
    pred = torch.argmax(probs, dim=-1).item()

labels = {0: "negative", 1: "neutral", 2: "positive"}
print(f"Prediction: {labels[pred]} ({probs[0][pred]:.4f})")
```

## Training Data

The model was trained on [Kenpache/multilingual-financial-sentiment](https://huggingface.co/datasets/Kenpache/multilingual-financial-sentiment), a curated dataset of ~39K financial news sentences from 80+ sources across six languages.

| Language | Samples | Sources |
|---|---|---|
| Japanese | 8,287 | Nikkei, Nikkan Kogyo, Reuters JP, Minkabu, etc. |
| Chinese | 7,930 | Sina Finance, EastMoney, 10jqka, etc. |
| Spanish | 7,125 | Expansión, Cinco Días, Bloomberg Línea, etc. |
| English | 6,887 | CNBC, Yahoo Finance, Fortune, Benzinga, etc. |
| German | 5,023 | Börse.de, FAZ, NTV Börse, Handelsblatt, etc. |
| French | 3,935 | Boursorama, Tradingsat, BFM Business, etc. |

## Comparison with FinBERT

| Feature | FinBERT | FinBERT-Multilingual |
|---|---|---|
| Base model | BERT-base | XLM-RoBERTa-base |
| Languages | English only | 6 languages |
| Domain adaptation | Financial corpus pre-training | TAPT on multilingual financial texts |
| Classes | 3 (Pos/Neg/Neu) | 3 (Pos/Neg/Neu) |
| Checkpoint selection | Single best | SWA (top-3) |

## Citation

If you use this model in your research, please cite:

```bibtex
@misc{finbert-multilingual-2025,
  title={FinBERT-Multilingual: Cross-Lingual Financial Sentiment Analysis with Domain-Adapted XLM-RoBERTa},
  author={Kenpache},
  year={2025},
  url={https://huggingface.co/Kenpache/finbert-multilingual}
}
```

## License

Apache 2.0

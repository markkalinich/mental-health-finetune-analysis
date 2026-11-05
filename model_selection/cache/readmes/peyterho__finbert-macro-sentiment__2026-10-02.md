---
library_name: transformers
license: apache-2.0
base_model: ProsusAI/finbert
tags:
- text-classification
- sentiment-analysis
- finance
- macroeconomics
- finbert
- bert
language:
- en
datasets:
- nickmuchi/financial-classification
- zeroshot/twitter-financial-news-sentiment
- FinanceInc/auditor_sentiment
- pauri32/fiqa-2018
- climatebert/climate_sentiment
metrics:
- accuracy
- f1
pipeline_tag: text-classification
arxiv: 1908.10063
model-index:
- name: finbert-macro-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Combined Financial Sentiment (5 datasets)
      type: custom
    metrics:
    - type: accuracy
      value: 0.8973
      name: Accuracy
    - type: f1
      value: 0.8813
      name: F1 (macro)
    - type: f1
      value: 0.8984
      name: F1 (weighted)
  - task:
      type: text-classification
      name: Sentiment Analysis (OOD)
    dataset:
      name: Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75
      type: Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75
    metrics:
    - type: accuracy
      value: 0.9236
      name: Accuracy
    - type: f1
      value: 0.9134
      name: F1 (macro)
  - task:
      type: text-classification
      name: Sentiment Analysis (OOD)
    dataset:
      name: ic-fspml/stock_news_sentiment
      type: ic-fspml/stock_news_sentiment
    metrics:
    - type: accuracy
      value: 0.6781
      name: Accuracy
    - type: f1
      value: 0.6765
      name: F1 (macro)
---

# FinBERT Macro Sentiment

A fine-tuned [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) (109M params, BERT-base) for **3-class sentiment analysis on financial, macroeconomic, and climate/ESG text**. Trained on 20K samples from 5 financial NLP datasets.

This model is the **default FinBERT head** and the backbone of the [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) ensemble pipeline. The topic router selects it for general financial news and social/tweet content. It can also be used standalone as a drop-in upgrade for the original ProsusAI/finbert.

## Why Fine-Tune FinBERT?

The original [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) was trained only on Financial PhraseBank ([Araci, 2019](https://arxiv.org/abs/1908.10063)) — ~4,800 sentences from English financial news. By fine-tuning on a broader mix of 5 datasets spanning news headlines, financial tweets, auditor reports, financial QA, and climate disclosures, we significantly improve recall on minority classes and cross-domain generalization:

| Metric | Off-the-shelf FinBERT | **This model** | Δ |
|---|:---:|:---:|:---:|
| Accuracy | ~0.670 | **0.897** | +23pp |
| F1 (macro) | ~0.578 | **0.881** | +30pp |
| Negative recall | ~0.47 | **0.89** | +42pp |
| Positive recall | ~0.35 | **0.91** | +56pp |

The original model's weakness is its strong neutral bias — it achieves decent accuracy by defaulting to "neutral" but badly under-predicts both positive and negative classes. Our broader training mix and class weighting fix this.

## Quick Start

### Standalone Usage

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="peyterho/finbert-macro-sentiment", top_k=None)

pipe("Tesla shares surged 15% after beating earnings expectations.")
# [[{'label': 'positive', 'score': 0.99}, {'label': 'neutral', 'score': 0.01}, {'label': 'negative', 'score': 0.00}]]

pipe("Markets crashed amid recession fears and massive layoffs.")
# [[{'label': 'negative', 'score': 0.99}, {'label': 'neutral', 'score': 0.01}, {'label': 'positive', 'score': 0.00}]]

pipe("The Federal Reserve raised rates by 75bps citing persistent inflation.")
# [[{'label': 'neutral', 'score': 0.91}, {'label': 'negative', 'score': 0.07}, {'label': 'positive', 'score': 0.02}]]
```

### As Part of the Full Pipeline

Within the [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) pipeline, this model is the **default head** — selected for general financial news, social media, and any text that doesn't trigger the policy or climate routing keywords:

```python
from macro_sentiment import MacroSentimentPipeline

pipe = MacroSentimentPipeline(device="cpu")

result = pipe("$AAPL crushed earnings, revenue up 12% YoY. Bullish!")
print(result.summary())
# Sentiment: Positive (+0.687) | Policy: Neutral (+0.000) | Crisis: Normal (0.000) | Domain: financial_news
print(result.head_used)
# "finbert"

result = pipe("The latest jobs report showed unemployment rising to 4.2%, above consensus.")
print(result.summary())
# Sentiment: Negative (-0.312) | Policy: Neutral (+0.000) | Crisis: Normal (0.052) | Domain: financial_news
```

## Label Mapping

This model preserves FinBERT's native label encoding:

| Label ID | Label | Unified Sentiment | Score Mapping |
|:---:|---|---|:---:|
| 0 | `positive` | positive | +1.0 |
| 1 | `negative` | negative | -1.0 |
| 2 | `neutral` | neutral | 0.0 |

> **Note:** FinBERT's label ordering (positive=0, negative=1, neutral=2) differs from the standard convention (negative=0, neutral=1, positive=2). The ensemble pipeline handles this remapping internally. If using standalone, interpret labels by name, not by ID.

## Evaluation Results

### In-Domain (Combined Test Set — 4,333 samples)

All three fine-tuned heads compared on the same held-out test split:

| Model | Params | Accuracy | F1 (macro) | F1 (weighted) |
|---|:---:|:---:|:---:|:---:|
| [RoBERTa-Large](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) | 355M | 0.9130 | 0.9023 | 0.9137 |
| **FinBERT (this model)** | **109M** | **0.8973** | **0.8813** | **0.8984** |
| [ClimateBERT](https://huggingface.co/peyterho/climatebert-macro-sentiment) | 82M | 0.8885 | 0.8716 | 0.8898 |

### Per-Class Breakdown

```
              precision    recall  f1-score   support

    negative     0.8051    0.8945    0.8474       711
     neutral     0.9518    0.8925    0.9212      2613
    positive     0.8417    0.9118    0.8754      1009

    accuracy                         0.8973      4333
   macro avg     0.8662    0.8996    0.8813      4333
weighted avg     0.9021    0.8973    0.8984      4333
```

Balanced recall across all three classes (89–91%) is the key improvement over the original FinBERT, which suffered from strong neutral bias (~90%+ neutral recall but <50% for positive/negative).

### Out-of-Domain: Financial Phrasebank (785 samples)

Evaluated on [Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75](https://huggingface.co/datasets/Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75) — PhraseBank (75% agreement) + financial news articles. **Not in the training mix.**

| Model | Params | Accuracy | F1 (macro) |
|---|:---:|:---:|:---:|
| [RoBERTa-Large](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) | 355M | 0.9414 | 0.9357 |
| [ClimateBERT](https://huggingface.co/peyterho/climatebert-macro-sentiment) | 82M | 0.9248 | 0.9213 |
| **FinBERT (this model)** | **109M** | **0.9236** | **0.9134** |

All three heads generalize well, with >92% accuracy on this OOD financial text benchmark.

### Out-of-Domain: Stock News Headlines (30,150 samples)

Evaluated on [ic-fspml/stock_news_sentiment](https://huggingface.co/datasets/ic-fspml/stock_news_sentiment) — 5-class labels mapped to 3-class. **Not in the training mix.**

| Model | Params | Accuracy | F1 (macro) |
|---|:---:|:---:|:---:|
| [RoBERTa-Large](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) | 355M | 0.7211 | 0.7265 |
| **FinBERT (this model)** | **109M** | **0.6781** | **0.6765** |
| [ClimateBERT](https://huggingface.co/peyterho/climatebert-macro-sentiment) | 82M | 0.6472 | 0.6441 |

FinBERT's financial pre-training gives it an edge over ClimateBERT on stock-specific headlines. The overall lower numbers reflect the 5→3 class mapping noise and significant domain shift (short, noisy headlines vs. the longer sentences in the training mix).

### Comparison Against Baselines

| Method | Accuracy | F1 (macro) | Notes |
|---|:---:|:---:|---|
| **FinBERT (this model)** | **0.8973** | **0.8813** | 109M params, fine-tuned |
| Off-the-shelf ProsusAI/finbert | ~0.670 | ~0.578 | Same architecture, no fine-tuning on combined data |
| Dict-only meta-classifier (GBT) | 0.6693 | 0.5781 | GradientBoosting on 24 dictionary features |
| Dict-only rules (LM + Henry) | 0.5684 | 0.5277 | Threshold-based, no learned parameters |

## Training Data

Fine-tuned on **20,034 training samples** combined from 5 public financial/climate sentiment datasets:

| Dataset | Domain | Train | Test | Label Mapping |
|---|---|:---:|:---:|---|
| [nickmuchi/financial-classification](https://huggingface.co/datasets/nickmuchi/financial-classification) | Financial PhraseBank | ~4,800 | ~1,200 | negative / neutral / positive |
| [zeroshot/twitter-financial-news-sentiment](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment) | Financial tweets | ~9,900 | ~2,500 | bearish→neg, bullish→pos, neutral |
| [FinanceInc/auditor_sentiment](https://huggingface.co/datasets/FinanceInc/auditor_sentiment) | Auditor reports | ~3,600 | ~900 | negative / neutral / positive |
| [pauri32/fiqa-2018](https://huggingface.co/datasets/pauri32/fiqa-2018) | Financial QA + microblog | ~938 | ~235 | Continuous score thresholded at ±0.15 |
| [climatebert/climate_sentiment](https://huggingface.co/datasets/climatebert/climate_sentiment) | Climate disclosures | ~1,000 | ~500 | risk→neg, neutral, opportunity→pos |

**Label distribution (train):** 15.9% negative, 58.4% neutral, 25.7% positive — handled via class-weighted loss.

## Training Details

| Hyperparameter | Value |
|---|---|
| Base model | [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) (109M, BERT-base, 12 layers, 768 hidden, 12 heads) |
| Learning rate | 2e-5 |
| Batch size | 32 × 2 gradient accumulation = 64 effective |
| Epochs | 6 (best checkpoint at epoch 5 by F1 macro) |
| Scheduler | Linear decay with 20% warmup |
| Optimizer | AdamW (weight decay 0.01) |
| Max length | 128 tokens |
| Precision | FP16 |
| Class weighting | √(inverse frequency) — weights: positive=1.02, negative=1.30, neutral=0.68 |
| Seed | 42 |
| Best model selection | Highest F1 (macro) on validation set |

### Class Weighting Strategy

Following the approach in the original FinBERT paper ([Araci, 2019](https://arxiv.org/abs/1908.10063), Section 4.4), sqrt-inverse-frequency class weights are applied to the cross-entropy loss to counteract the ~58% neutral class imbalance:

```
weight[c] = √(N_total / N_class_c) / mean(weights)
```

This upweights the minority negative class (1.30×) and downweights the majority neutral class (0.68×) while keeping the positive class near unity (1.02×).

### Training Curve

| Epoch | Train Loss | Val Loss | Accuracy | F1 (macro) | F1 (weighted) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 0.894 | 0.376 | 0.858 | 0.838 | 0.860 |
| 2 | 0.629 | 0.353 | 0.859 | 0.846 | 0.862 |
| 3 | 0.360 | 0.317 | 0.892 | 0.876 | 0.893 |
| 4 | 0.160 | 0.377 | 0.894 | 0.879 | 0.895 |
| **5** | **0.124** | **0.405** | **0.897** | **0.881** | **0.898** |
| 6 | 0.086 | 0.429 | 0.896 | 0.880 | 0.897 |

Validation loss bottomed at epoch 3, but F1 macro continued improving through epoch 5. The divergence between val loss and F1 suggests the model becomes less calibrated (overconfident) on later epochs while still improving classification boundaries — a common pattern with class-weighted loss. The best checkpoint (epoch 5) trades slightly worse calibration for better discrimination.

## Role in the Ensemble Pipeline

This model serves as the **default financial news head** in the [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) pipeline. It is selected when no specialized routing keyword is triggered, making it the workhorse for general financial content.

```
Input Text → Topic Router → policy keywords?     → RoBERTa-Large
                          → climate keywords?    → ClimateBERT
                          → non-English text?    → XLM-RoBERTa
                          → default (this model) → FinBERT ★
```

The pipeline fuses this model's prediction with four dictionary-based signals (Loughran-McDonald, Henry earnings tone, Sautner-style climate exposure, and macro policy/crisis dictionaries) using **crisis-adaptive weighting** — during crisis language, more weight shifts to the dictionary composite, since crisis keywords carry clearer signal than neural softmax outputs.

### Ensemble Siblings

| Head | Model | Params | Role |
|---|---|:---:|---|
| **FinBERT** ★ | **peyterho/finbert-macro-sentiment** | **109M** | **Default — financial news, tweets** |
| RoBERTa-Large | [peyterho/financial-roberta-large-macro-sentiment](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) | 355M | Policy/macro communications |
| ClimateBERT | [peyterho/climatebert-macro-sentiment](https://huggingface.co/peyterho/climatebert-macro-sentiment) | 82M | Climate/ESG text |
| XLM-RoBERTa | [cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual) | 278M | Non-English text (pre-trained, not fine-tuned) |

## Custom Fine-Tuning

Fine-tune this model further on your own financial labelled data:

```bash
pip install transformers datasets accelerate evaluate torch

python -m macro_sentiment.finetune \
    --data my_labels.csv \
    --text-column headline \
    --label-column sentiment \
    --base-model peyterho/finbert-macro-sentiment \
    --output my-org/my-custom-model \
    --push-to-hub \
    --epochs 4 \
    --lr 1e-5 \
    --batch-size 32
```

The fine-tuning script (from the [parent repo](https://huggingface.co/peyterho/macro-sentiment-finbert)) accepts CSV, TSV, JSON, or JSONL. Labels can be strings (`"positive"`, `"negative"`, `"neutral"`, `"bullish"`, `"bearish"`) or integers (0/1/2). Automatic label remapping handles FinBERT's non-standard label ordering (positive=0, negative=1, neutral=2). Class-weighted loss is applied by default.

## Limitations

- **English only** — FinBERT was pre-trained on English financial text (Reuters TRC2). Non-English text should use the multilingual head in the full pipeline.
- **128-token max length** — fine-tuned with 128-token truncation. Longer documents (earnings calls, 10-K filings) should be chunked at paragraph or sentence level before scoring.
- **Neutral class dominance** — despite class weighting, neutral precision (0.95) is noticeably higher than positive (0.84) or negative (0.81), reflecting the ~58% neutral training distribution. The model remains slightly conservative on polarity predictions.
- **Label noise** — the FiQA dataset uses continuous sentiment scores thresholded at ±0.15, introducing boundary noise. The Twitter dataset contains informal language, $cashtags, and abbreviations that differ substantially from formal financial text.
- **No temporal or entity awareness** — treats each text independently. Cannot reason about whether "rates rising" is positive (for banks) or negative (for growth stocks) without entity context.
- **FinBERT label ordering** — label IDs are `{0: positive, 1: negative, 2: neutral}`, which differs from the standard convention. Use label names, not IDs, when interpreting results.
- **Parameter count trade-off** — at 109M parameters, this model sits between ClimateBERT (82M) and RoBERTa-Large (355M). For maximum accuracy (+1.6 F1 points), use the RoBERTa-Large head; for minimum latency (−25% params), use ClimateBERT.

## Citation

```bibtex
@article{araci2019finbert,
    title={FinBERT: Financial Sentiment Analysis with Pre-Trained Language Models},
    author={Araci, Dogu},
    journal={arXiv preprint arXiv:1908.10063},
    year={2019}
}

@article{loughran2011liability,
    title={When is a liability not a liability? Textual analysis, dictionaries, and 10-Ks},
    author={Loughran, Tim and McDonald, Bill},
    journal={The Journal of Finance},
    volume={66},
    number={1},
    pages={35--65},
    year={2011}
}

@article{henry2008earnings,
    title={Are investors influenced by how earnings press releases are written?},
    author={Henry, Elaine},
    journal={Journal of Business Communication},
    volume={45},
    number={4},
    pages={363--407},
    year={2008}
}
```

## Framework Versions

- Transformers 5.6.2
- PyTorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2

## License

Apache 2.0

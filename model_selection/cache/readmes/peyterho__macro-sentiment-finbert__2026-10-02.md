---
library_name: transformers
base_model: ProsusAI/finbert
tags:
- sentiment-analysis
- finance
- macroeconomics
- climate
- esg
- policy
- ensemble
- dictionary
- finbert
- text-classification
language:
- en
- ar
- fr
- de
- hi
- it
- pt
- es
license: apache-2.0
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
model-index:
- name: macro-sentiment-finbert
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

# Macro Sentiment FinBERT

**A multi-signal macroeconomic sentiment pipeline** that combines fine-tuned transformer ensembles with financial dictionaries and topic routing to produce structured sentiment analysis for financial news, central bank communications, climate/ESG reports, and social media.

This repo hosts the **FinBERT head** (109M params, fine-tuned from [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert)) — the default routing target and backbone of the full pipeline. The complete system includes three additional transformer heads, four dictionary scorers, and a keyword-based topic router.

## Key Features

- 🏦 **Macro-aware** — outputs financial sentiment, monetary policy stance (dovish ↔ hawkish), crisis signals, and uncertainty
- 🌱 **Climate/ESG scoring** — dedicated ClimateBERT head + Sautner-style exposure dictionary for climate risk vs. opportunity
- 🔀 **Topic routing** — automatically selects the best transformer head based on text content (policy → RoBERTa-Large, climate → ClimateBERT, financial news → FinBERT)
- 🌍 **Multilingual** — non-English text auto-routes to XLM-RoBERTa (8+ languages: EN, AR, FR, DE, HI, IT, PT, ES)
- 📖 **Dictionary layer** — Loughran-McDonald, Henry earnings tone, climate exposure, and macro policy dictionaries provide interpretable feature signals alongside neural predictions

## Architecture

```
                          ┌──────────────────────────────────┐
                          │         Input Text               │
                          └──────────────┬───────────────────┘
                                         │
                    ┌────────────────────┼────────────────────┐
                    ▼                    ▼                    ▼
          ┌─────────────────┐  ┌─────────────────┐  ┌───────────────┐
          │  Topic Router   │  │   Dictionary    │  │   Language    │
          │  (keywords)     │  │   Scorers (×4)  │  │   Detection   │
          └────────┬────────┘  └────────┬────────┘  └───────┬───────┘
                   │                    │                    │
          ┌────────▼────────────────────┼────────────────────▼────────┐
          │                    Head Selection                         │
          │  policy → RoBERTa-Large  │  climate → ClimateBERT        │
          │  financial → FinBERT ★   │  non-English → XLM-RoBERTa   │
          └────────┬────────────────────────────────────────┬────────┘
                   │                                        │
          ┌────────▼────────┐                     ┌────────▼────────┐
          │   Transformer   │                     │   Dictionary    │
          │   Score [-1,+1] │                     │   Composite     │
          └────────┬────────┘                     └────────┬────────┘
                   │                                        │
                   └──────────────┬─────────────────────────┘
                                  ▼
                   ┌──────────────────────────────┐
                   │    Weighted Fusion            │
                   │  (crisis-adaptive weights)    │
                   └──────────────┬───────────────┘
                                  ▼
                   ┌──────────────────────────────┐
                   │   MacroSentimentResult       │
                   │  • macro_sentiment [-1,+1]   │
                   │  • policy_stance [-1,+1]     │
                   │  • crisis_signal [0,1]       │
                   │  • climate_sentiment [-1,+1] │
                   │  • confidence [0,1]          │
                   │  • detected_domain           │
                   └──────────────────────────────┘
```

The fusion weights are **crisis-adaptive**: when the crisis dictionary fires strongly, more weight shifts to the dictionary composite (up to 75% dict / 25% transformer), since crisis language often carries clearer signal through keywords than neural softmax probabilities.

## Ensemble Components

| Head | Model | Params | Base | Role |
|---|---|---|---|---|
| **FinBERT** ★ | [peyterho/finbert-macro-sentiment](https://huggingface.co/peyterho/finbert-macro-sentiment) | 109M | [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) | Default — financial news, tweets |
| **RoBERTa-Large** | [peyterho/financial-roberta-large-macro-sentiment](https://huggingface.co/peyterho/financial-roberta-large-macro-sentiment) | 355M | [soleimanian/financial-roberta-large-sentiment](https://huggingface.co/soleimanian/financial-roberta-large-sentiment) | Policy/macro text |
| **ClimateBERT** | [peyterho/climatebert-macro-sentiment](https://huggingface.co/peyterho/climatebert-macro-sentiment) | 82M | [climatebert/distilroberta-base-climate-sentiment](https://huggingface.co/climatebert/distilroberta-base-climate-sentiment) | Climate/ESG text |
| **XLM-RoBERTa** | [cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual) | 278M | — | Non-English text (8+ languages) |

| Dictionary | Based On | Signal |
|---|---|---|
| **Loughran-McDonald** | Loughran & McDonald (2011) | Financial polarity, subjectivity |
| **Henry** | Henry (2008) — earnings tone | Earnings press release tone |
| **Climate Exposure** | Sautner et al. (2023) style | Climate risk vs. opportunity density |
| **Macro Policy** | Custom | Hawkish/dovish stance, crisis intensity, uncertainty |

## Quick Start

There are two ways to use this model — pick the one that fits your needs:

### Option A: Standalone FinBERT (classification only)

If you just need positive/negative/neutral labels, use the model directly — no repo cloning required:

```python
# pip install transformers torch
from transformers import pipeline

classifier = pipeline("text-classification", model="peyterho/macro-sentiment-finbert", top_k=None)
result = classifier("The Federal Reserve signaled a pause in rate hikes amid cooling inflation.")
print(result)
# [[{'label': 'positive', 'score': 0.72}, {'label': 'neutral', 'score': 0.21}, {'label': 'negative', 'score': 0.07}]]
```

### Option B: Full Pipeline (multi-signal analysis)

For the complete system — topic routing, policy stance, crisis signals, climate scoring, and dictionaries — you need to clone this repo since the pipeline code lives inside it:

```bash
git clone https://huggingface.co/peyterho/macro-sentiment-finbert
cd macro-sentiment-finbert
pip install -r requirements.txt
```

```python
from macro_sentiment import MacroSentimentPipeline

pipe = MacroSentimentPipeline(device="cpu")

# Financial news — auto-routes to FinBERT
result = pipe("Markets rallied on strong earnings, with the S&P 500 hitting record highs.")
print(result.summary())
# Sentiment: Positive (+0.612) | Policy: Neutral (+0.000) | Crisis: Normal (0.000) | Domain: financial_news

# Central bank communication — auto-routes to RoBERTa-Large
result = pipe("The ECB raised rates by 25 basis points, citing persistent inflation pressures.")
print(result.summary())
# Sentiment: Negative (-0.348) | Policy: Hawkish (+0.714) | Crisis: Normal (0.000) | Domain: policy

# Climate/ESG text — auto-routes to ClimateBERT
result = pipe("The company committed to net-zero emissions by 2040 through renewable energy investments.")
print(result.summary())
# Sentiment: Positive (+0.445) | Policy: Neutral (+0.000) | Crisis: Normal (0.000) | Domain: climate | Climate: Opportunity (exp=0.60)

# Non-English text — auto-routes to XLM-RoBERTa
result = pipe("Die EZB signalisiert Geduld bei künftigen Zinssenkungen.")
print(result.summary())
```

## Use in Google Colab / Kaggle

Copy-paste these cells into a notebook. Both work on Colab (free tier) and Kaggle.

### Cell 1 — Standalone FinBERT only

```python
!pip install -q transformers torch

from transformers import pipeline

classifier = pipeline("text-classification", model="peyterho/macro-sentiment-finbert", top_k=None)

# Try it
texts = [
    "Tesla shares surged 15% after crushing earnings expectations.",
    "The Federal Reserve raised rates by 75bps citing persistent inflation.",
    "Markets crashed amid recession fears and massive layoffs.",
    "The company reported quarterly results in line with analyst estimates.",
]

for text in texts:
    result = classifier(text)[0]
    top = max(result, key=lambda x: x["score"])
    print(f'{top["label"]:>8s} ({top["score"]:.2f})  {text}')
```

### Cell 1 — Full Pipeline (with policy stance, crisis signals, climate scoring)

```python
# Install dependencies and clone the repo
!pip install -q transformers torch pysentiment2 scikit-learn numpy pandas datasets accelerate huggingface_hub
!git clone https://huggingface.co/peyterho/macro-sentiment-finbert /content/macro-sentiment-finbert

import sys
sys.path.insert(0, "/content/macro-sentiment-finbert")
```

### Cell 2 — Score any text

```python
from macro_sentiment import MacroSentimentPipeline

pipe = MacroSentimentPipeline(device="cpu")

texts = [
    "Markets rallied on strong earnings, with the S&P 500 hitting record highs.",
    "The ECB raised rates by 25 basis points, citing persistent inflation pressures.",
    "The company committed to net-zero emissions by 2040 through renewable energy investments.",
    "Credit markets froze as contagion fears spread across European banks.",
    "Die EZB signalisiert Geduld bei künftigen Zinssenkungen.",
]

for text in texts:
    result = pipe(text)
    print(result.summary())
    print(f"  → {text}\n")
```

### Cell 3 — Explore the full structured output

```python
result = pipe("Fed signals two more rate cuts before year-end, a dovish surprise that lifted equities.")

print(f"Macro sentiment:    {result.macro_sentiment:+.3f}")
print(f"Financial sentiment:{result.financial_sentiment:+.3f}")
print(f"Policy stance:      {result.policy_stance:+.3f}  (negative=dovish, positive=hawkish)")
print(f"Crisis signal:      {result.crisis_signal:.3f}")
print(f"Climate sentiment:  {result.climate_sentiment:+.3f}")
print(f"Uncertainty:        {result.uncertainty:.3f}")
print(f"Confidence:         {result.confidence:.3f}")
print(f"Domain:             {result.detected_domain}")
print(f"Head used:          {result.head_used}")
print(f"LM polarity:        {result.lm_polarity:+.3f}")
print(f"Henry polarity:     {result.henry_polarity:+.3f}")
print(f"Climate exposure:   {result.climate_exposure:.3f}")
```

### Cell 4 — Batch scoring with pandas

```python
import pandas as pd

headlines = [
    "Strong jobs report pushes markets to record highs",
    "Tech earnings mixed as AI spending soars",
    "Fed signals patience on rate cuts, markets dip",
    "Retail sales disappoint, recession fears resurface",
    "Green bond issuance hit $500B as investors pivot to sustainable fixed income",
    "Bank of Japan holds rates steady in surprise decision",
]

results = pipe.score_batch(headlines, mode="routed")

df = pd.DataFrame([{
    "text": t,
    "sentiment": r.macro_sentiment,
    "policy": r.policy_stance,
    "crisis": r.crisis_signal,
    "climate": r.climate_sentiment,
    "domain": r.detected_domain,
    "head": r.head_used,
} for t, r in zip(headlines, results)])

print(df.to_string(index=False))
```

### Cell 5 — Dictionary-only mode (no GPU needed, instant)

```python
# No transformer models loaded — uses only the four dictionaries
result = pipe.score("The central bank cut rates amid fears of a deepening recession.", mode="dict_only")
print(result.summary())
print(f"LM polarity:   {result.lm_polarity:+.3f}")
print(f"Henry polarity: {result.henry_polarity:+.3f}")
print(f"Policy stance:  {result.policy_stance:+.3f}")
print(f"Crisis signal:  {result.crisis_signal:.3f}")
```

> **💡 Notes:**
> - The full pipeline lazy-loads transformer models on first use. First call takes 30–60 seconds to download (~800MB across 4 models). Subsequent calls are fast.
> - `mode="routed"` (default) loads only 1 model per call. `mode="all"` loads all 4 models (~2GB RAM).
> - For Colab free tier, `mode="routed"` works fine. For `mode="all"`, use a GPU runtime to avoid OOM.
> - On Kaggle, enable "Internet" in notebook settings (Settings → Internet → On) so models can download.

## Structured Output

Every call returns a `MacroSentimentResult` with these fields:

| Field | Range | Description |
|---|---|---|
| `macro_sentiment` | [-1, +1] | Overall macroeconomic sentiment (weighted fusion of transformer + dictionary) |
| `financial_sentiment` | [-1, +1] | Financial-domain sentiment from the selected transformer head |
| `policy_stance` | [-1, +1] | Monetary policy orientation: -1 = very dovish, +1 = very hawkish |
| `climate_sentiment` | [-1, +1] | Climate outlook: -1 = risk, +1 = opportunity |
| `crisis_signal` | [0, 1] | Crisis language intensity (recession, contagion, bank failure, etc.) |
| `uncertainty` | [0, 1] | Uncertainty/volatility language density |
| `confidence` | [0, 1] | Pipeline confidence (based on head agreement, topic match, uncertainty) |
| `detected_domain` | str | Routed domain: `financial_news`, `policy`, `climate`, `social`, `ensemble` |
| `head_used` | str | Which transformer head was selected |
| `lm_polarity` | [-1, +1] | Loughran-McDonald polarity score |
| `henry_polarity` | [-1, +1] | Henry earnings tone score |
| `climate_exposure` | [0, 1] | Climate keyword density (Sautner-style) |

## Scoring Modes

```python
# "routed" (default) — topic router selects best head
result = pipe.score("text", mode="routed")

# "all" — runs ALL heads and averages composite scores
result = pipe.score("text", mode="all")

# "dict_only" — dictionary signals only, no transformer inference
result = pipe.score("text", mode="dict_only")
```

## Training Data

All three transformer heads were fine-tuned on the same combined dataset of **5 public financial/climate sentiment corpora**:

| Dataset | Domain | Samples | Label Mapping |
|---|---|---|---|
| [nickmuchi/financial-classification](https://huggingface.co/datasets/nickmuchi/financial-classification) | Financial PhraseBank | ~4,800 train / ~1,200 test | negative / neutral / positive |
| [zeroshot/twitter-financial-news-sentiment](https://huggingface.co/datasets/zeroshot/twitter-financial-news-sentiment) | Financial tweets | ~9,900 train / ~2,500 val | bearish → neg, bullish → pos, neutral |
| [FinanceInc/auditor_sentiment](https://huggingface.co/datasets/FinanceInc/auditor_sentiment) | Auditor reports | ~3,600 train / ~900 test | negative / neutral / positive |
| [pauri32/fiqa-2018](https://huggingface.co/datasets/pauri32/fiqa-2018) | Financial QA + microblog | ~938 train+val / ~235 test | Continuous score thresholded at ±0.15 |
| [climatebert/climate_sentiment](https://huggingface.co/datasets/climatebert/climate_sentiment) | Climate reports | ~1,000 train / ~500 test | risk → neg, neutral, opportunity → pos |

All datasets were unified to a consistent 3-class schema: `0=negative`, `1=neutral`, `2=positive`.

## Training Details

### FinBERT Head (this model)

| Hyperparameter | Value |
|---|---|
| Base model | [ProsusAI/finbert](https://huggingface.co/ProsusAI/finbert) |
| Learning rate | 2e-5 |
| Batch size | 16 × 4 gradient accumulation = 64 effective |
| Epochs | 2 |
| Scheduler | Cosine with 31 warmup steps |
| Optimizer | AdamW (fused) |
| Max length | 512 |
| Seed | 42 |

### Training Curve

| Epoch | Train Loss | Val Loss | Accuracy | F1 (macro) | F1 (weighted) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1.6807 | 0.3761 | 0.8246 | 0.8058 | 0.8300 |
| 2 | 1.1679 | 0.3450 | 0.8486 | 0.8325 | 0.8515 |

> Note: The higher training loss reflects the FinBERT label ordering (positive=0, negative=1, neutral=2) which differs from the unified schema — a label remapping is applied at training time.

## Evaluation Results

### In-Domain (Combined Test Set — 4,333 samples)

| Model | Accuracy | F1 (macro) | F1 (weighted) |
|---|:---:|:---:|:---:|
| **RoBERTa-Large (355M)** | **0.9130** | **0.9023** | **0.9137** |
| FinBERT (109M) ★ | 0.8973 | 0.8813 | 0.8984 |
| ClimateBERT (82M) | 0.8885 | 0.8716 | 0.8898 |
| Dict-only baseline (GBT) | 0.6693 | 0.5781 | 0.6500 |
| Dict-only baseline (rules) | 0.5684 | 0.5277 | 0.5784 |

### Out-of-Domain: Financial News Phrasebank (785 samples)

Evaluated on [Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75](https://huggingface.co/datasets/Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75) — **not in the training mix**.

| Model | Accuracy | F1 (macro) |
|---|:---:|:---:|
| **RoBERTa-Large** | **0.9414** | **0.9357** |
| ClimateBERT | 0.9248 | 0.9213 |
| FinBERT ★ | 0.9236 | 0.9134 |

### Out-of-Domain: Stock News Headlines (30,150 samples)

Evaluated on [ic-fspml/stock_news_sentiment](https://huggingface.co/datasets/ic-fspml/stock_news_sentiment) — 5-class mapped to 3-class. **Not in the training mix**.

| Model | Accuracy | F1 (macro) |
|---|:---:|:---:|
| **RoBERTa-Large** | **0.7211** | **0.7265** |
| FinBERT ★ | 0.6781 | 0.6765 |
| ClimateBERT | 0.6472 | 0.6441 |

Performance drops on stock news headlines are expected — these are short, noisy texts with 5→3 class mapping, representing a significant domain shift from the training data.

## Custom Fine-Tuning Guide

This section walks you through fine-tuning this model (or any of the ensemble heads) on your own labelled data. The repo includes a ready-to-use `finetune.py` script that handles label remapping, class-weighted loss, and evaluation automatically.

### Prerequisites

```bash
git clone https://huggingface.co/peyterho/macro-sentiment-finbert
cd macro-sentiment-finbert
pip install -r requirements.txt
pip install evaluate     # needed for metrics during training
```

### Step 1: Prepare Your Data

Create a file with **two columns**: one for text, one for labels. Supported formats: **CSV**, **TSV**, **JSON**, or **JSONL**.

#### Labels

Labels can be **strings** or **integers**. The script automatically maps them to the unified 3-class schema (`0=negative`, `1=neutral`, `2=positive`):

| Accepted strings | Maps to |
|---|---|
| `"negative"`, `"neg"`, `"bearish"`, `"risk"` | 0 (negative) |
| `"neutral"`, `"neut"`, `"mixed"` | 1 (neutral) |
| `"positive"`, `"pos"`, `"bullish"`, `"opportunity"` | 2 (positive) |

Or just use integers: `0`, `1`, `2`.

#### Example CSV (`my_labels.csv`)

```csv
headline,sentiment
"Markets rallied on strong quarterly earnings",positive
"Fed raises rates citing persistent inflation",negative
"Company reports results in line with expectations",neutral
"Oil prices surge amid Middle East tensions",negative
"Record-breaking IPO signals strong investor confidence",positive
```

#### Example JSONL (`my_labels.jsonl`)

```jsonl
{"text": "Markets rallied on strong quarterly earnings", "label": "positive"}
{"text": "Fed raises rates citing persistent inflation", "label": "negative"}
{"text": "Company reports results in line with expectations", "label": "neutral"}
```

> **💡 How much data?** Even 200–500 labelled examples can meaningfully improve performance on your specific domain. 1,000+ is ideal. The script automatically applies class-weighted loss to handle imbalanced label distributions — so don't worry if you have more of one class than another.

### Step 2: Run Fine-Tuning

#### Minimal command (saves locally)

```bash
python -m macro_sentiment.finetune \
    --data my_labels.csv \
    --text-column headline \
    --label-column sentiment
```

This saves the fine-tuned model to `./custom-finetuned/`.

#### Full command (push to Hugging Face Hub)

```bash
python -m macro_sentiment.finetune \
    --data my_labels.csv \
    --text-column headline \
    --label-column sentiment \
    --base-model peyterho/macro-sentiment-finbert \
    --output my-username/my-custom-finbert \
    --push-to-hub \
    --epochs 4 \
    --lr 2e-5 \
    --batch-size 32 \
    --max-length 128
```

The script will:
1. Load and validate your data (reports any label errors)
2. Split into train/val sets (85/15 by default)
3. Print class distribution and computed class weights
4. Auto-detect label remapping for the chosen base model
5. Train with evaluation at each epoch
6. Select the best checkpoint by F1 (macro)
7. Print final Accuracy, F1 (macro), and F1 (weighted)
8. Save or push the model

#### All available arguments

| Argument | Default | Description |
|---|---|---|
| `--data` | *required* | Path to your data file (`.csv`, `.tsv`, `.json`, `.jsonl`) |
| `--text-column` | *required* | Column name containing the text |
| `--label-column` | *required* | Column name containing the labels |
| `--base-model` | `peyterho/finbert-macro-sentiment` | Base model to fine-tune (see table below) |
| `--output` | `./custom-finetuned` | Output directory or Hub model ID (e.g. `my-org/my-model`) |
| `--push-to-hub` | `false` | Push the final model to Hugging Face Hub |
| `--epochs` | `4` | Number of training epochs |
| `--lr` | `2e-5` | Learning rate |
| `--batch-size` | `32` | Per-device batch size (effective batch = `batch-size × gradient_accumulation`) |
| `--max-length` | `128` | Max token sequence length (increase to 256 or 512 for long texts) |
| `--val-split` | `0.15` | Fraction of data for validation (stratified by label) |
| `--no-class-weights` | `false` | Disable automatic class-weighted loss |
| `--seed` | `42` | Random seed for reproducibility |

### Step 3: Choose Which Head to Fine-Tune

You can fine-tune **any** of the ensemble heads. Pick the one closest to your domain:

| Use case | Recommended `--base-model` | Why |
|---|---|---|
| Financial news, tweets, earnings | `peyterho/macro-sentiment-finbert` (default) | Pre-trained on financial corpora, 109M params, fast |
| Central bank / policy / macro reports | `peyterho/financial-roberta-large-macro-sentiment` | Largest head (355M), best on policy language |
| Climate / ESG / sustainability reports | `peyterho/climatebert-macro-sentiment` | Pre-trained on climate text, smallest (82M) |
| Starting from original base (no macro fine-tune) | `ProsusAI/finbert` | Use if you want to train from the original FinBERT weights |

Example — fine-tune the climate head on ESG data:

```bash
python -m macro_sentiment.finetune \
    --data esg_reports.jsonl \
    --text-column body \
    --label-column esg_sentiment \
    --base-model peyterho/climatebert-macro-sentiment \
    --output my-org/climatebert-esg-custom \
    --push-to-hub \
    --epochs 6 \
    --lr 1e-5 \
    --max-length 256
```

### Fine-Tuning in Google Colab

Copy-paste these cells into a Colab notebook. Works on the free tier (CPU is fine for small datasets; use a GPU runtime for >5k samples or faster training).

#### Cell 1 — Setup

```python
# Clone repo and install dependencies
!git clone https://huggingface.co/peyterho/macro-sentiment-finbert /content/macro-sentiment-finbert
%cd /content/macro-sentiment-finbert
!pip install -q -r requirements.txt evaluate
```

#### Cell 2 — Upload or create your data

```python
# Option A: Upload a CSV file via Colab's file browser
from google.colab import files
uploaded = files.upload()  # upload your CSV/JSONL file

# Option B: Create a small example dataset inline
import pandas as pd

data = pd.DataFrame({
    "text": [
        "Markets surged on better-than-expected jobs data",
        "Trade war fears sent global equities tumbling",
        "Quarterly revenue was roughly in line with guidance",
        "Banks rally after stress test results boost confidence",
        "Yield curve inversion deepens, sparking recession fears",
        "The company maintained its annual dividend outlook",
        "Central bank signals patience on future rate decisions",
        "Strong retail sales data lifted consumer discretionary stocks",
        "Credit downgrades hit emerging market bonds overnight",
        "Analysts remain neutral on the sector after mixed earnings",
    ],
    "label": [
        "positive", "negative", "neutral", "positive", "negative",
        "neutral", "neutral", "positive", "negative", "neutral",
    ]
})
data.to_csv("my_labels.csv", index=False)
print(f"Created my_labels.csv with {len(data)} rows")
print(data["label"].value_counts())
```

#### Cell 3 — Fine-tune

```python
# Fine-tune on your data (saves locally)
!python -m macro_sentiment.finetune \
    --data my_labels.csv \
    --text-column text \
    --label-column label \
    --base-model peyterho/macro-sentiment-finbert \
    --output ./my-custom-model \
    --epochs 4 \
    --lr 2e-5 \
    --batch-size 16
```

#### Cell 4 — Test your fine-tuned model

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="./my-custom-model", top_k=None)

test_texts = [
    "Tech stocks soared to record highs on AI optimism",
    "Mounting debt concerns weigh on sovereign credit ratings",
    "The index closed flat after a choppy trading session",
]

for text in test_texts:
    result = classifier(text)[0]
    top = max(result, key=lambda x: x["score"])
    print(f'{top["label"]:>8s} ({top["score"]:.2f})  {text}')
```

#### Cell 5 — (Optional) Push to Hugging Face Hub

```python
from huggingface_hub import login
login()  # paste your HF token

# Re-run fine-tuning with push-to-hub, or push the saved model manually:
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model = AutoModelForSequenceClassification.from_pretrained("./my-custom-model")
tokenizer = AutoTokenizer.from_pretrained("./my-custom-model")

model.push_to_hub("my-username/my-custom-finbert")
tokenizer.push_to_hub("my-username/my-custom-finbert")
print("✅ Pushed to Hub!")
```

### Fine-Tuning with Your Own Python Script

If you prefer full control, here's a minimal standalone script that doesn't use `finetune.py`:

```python
import torch
import numpy as np
from datasets import load_dataset, ClassLabel
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    TrainingArguments,
    Trainer,
    DataCollatorWithPadding,
)
import evaluate

# 1. Load your data
ds = load_dataset("csv", data_files="my_labels.csv", split="train")

# 2. Map string labels to integers
label_map = {"negative": 0, "neutral": 1, "positive": 2}
ds = ds.map(lambda x: {"label": label_map[x["label"].strip().lower()]})
ds = ds.cast_column("label", ClassLabel(names=["negative", "neutral", "positive"]))
ds = ds.train_test_split(test_size=0.15, seed=42, stratify_by_column="label")

# 3. Load model + tokenizer
model_name = "peyterho/macro-sentiment-finbert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=3)

# ⚠️ FinBERT uses a different label order internally (positive=0, negative=1, neutral=2)
# The finetune.py script handles this automatically via label remapping.
# If writing your own script, remap your unified labels to the model's expected order:
LABEL_REMAP = {0: 1, 1: 2, 2: 0}  # unified → FinBERT internal

# 4. Tokenize
def preprocess(examples):
    tok = tokenizer(examples["text"], truncation=True, max_length=128)
    tok["labels"] = [LABEL_REMAP[l] for l in examples["label"]]
    return tok

tokenized = ds.map(preprocess, batched=True, remove_columns=["text", "label"])

# 5. Metrics
acc_metric = evaluate.load("accuracy")
f1_metric = evaluate.load("f1")

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    return {
        "accuracy": acc_metric.compute(predictions=preds, references=labels)["accuracy"],
        "f1_macro": f1_metric.compute(predictions=preds, references=labels, average="macro")["f1"],
    }

# 6. Train
training_args = TrainingArguments(
    output_dir="./my-finetuned-finbert",
    num_train_epochs=4,
    per_device_train_batch_size=32,
    per_device_eval_batch_size=64,
    gradient_accumulation_steps=2,
    learning_rate=2e-5,
    weight_decay=0.01,
    warmup_ratio=0.2,
    eval_strategy="epoch",
    save_strategy="epoch",
    load_best_model_at_end=True,
    metric_for_best_model="f1_macro",
    bf16=torch.cuda.is_available(),
    logging_steps=10,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized["train"],
    eval_dataset=tokenized["test"],
    processing_class=tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer=tokenizer),
    compute_metrics=compute_metrics,
)

trainer.train()

# 7. Evaluate
results = trainer.evaluate()
print(f"Accuracy: {results['eval_accuracy']:.4f}, F1 (macro): {results['eval_f1_macro']:.4f}")

# 8. Save
trainer.save_model("./my-finetuned-finbert")
tokenizer.save_pretrained("./my-finetuned-finbert")
```

> **⚠️ Important: Label Remapping**
>
> FinBERT's internal label order is `positive=0, negative=1, neutral=2`, which differs from the standard `negative=0, neutral=1, positive=2`. The included `finetune.py` script handles this automatically for all supported base models. If you write your own training script, you **must** remap labels or your model will learn inverted predictions.
>
> The remapping for each base model:
> | Base model | Remap needed? | Mapping (unified → model) |
> |---|---|---|
> | `peyterho/macro-sentiment-finbert` | ✅ Yes | `{0→1, 1→2, 2→0}` |
> | `ProsusAI/finbert` | ✅ Yes | `{0→1, 1→2, 2→0}` |
> | `peyterho/climatebert-macro-sentiment` | ✅ Yes | `{0→2, 1→1, 2→0}` |
> | `peyterho/financial-roberta-large-macro-sentiment` | ❌ No | Direct mapping |
> | `soleimanian/financial-roberta-large-sentiment` | ❌ No | Direct mapping |

### Tips for Best Results

| Tip | Details |
|---|---|
| **Start from this model, not the original FinBERT** | `peyterho/macro-sentiment-finbert` already has macro-financial knowledge baked in. Starting from `ProsusAI/finbert` throws that away. |
| **Use a low learning rate** | `1e-5` to `3e-5` works well. Higher rates risk catastrophic forgetting of the pre-trained knowledge. |
| **Don't over-train** | 2–4 epochs is usually sufficient for fine-tuning. Watch validation loss — if it starts rising, you're overfitting. |
| **Increase `--max-length` for long texts** | The default is `128` tokens (~100 words). Set `256` or `512` for analyst reports, earnings transcripts, or policy documents. |
| **Class weights handle imbalance** | The script automatically computes √(N/nᵢ)-normalized class weights. If your data is balanced, add `--no-class-weights`. |
| **Use the right base for your domain** | Climate/ESG text → ClimateBERT head. Policy/macro text → RoBERTa-Large head. General financial → FinBERT (default). |
| **Validate on held-out data** | The script reserves 15% for validation by default (`--val-split 0.15`). If you have a dedicated test set, combine everything for training and evaluate separately. |

### Using Your Fine-Tuned Model in the Full Pipeline

After fine-tuning, you can swap your custom model into the full `MacroSentimentPipeline`:

```python
from macro_sentiment import MacroSentimentPipeline

# Override the FinBERT head with your custom model
pipe = MacroSentimentPipeline(
    device="cpu",
    finbert_model="my-username/my-custom-finbert",   # your fine-tuned model
)

# The pipeline will use your model for financial text routing,
# while keeping the other heads (RoBERTa, ClimateBERT, XLM-R) as-is
result = pipe("Your domain-specific financial text here")
print(result.summary())
```

Or for inference without the full pipeline:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="my-username/my-custom-finbert", top_k=None)
result = classifier("Your domain-specific text here")
print(result)
```

## Limitations

- **English-centric** — the fine-tuned heads (FinBERT, RoBERTa, ClimateBERT) are English-only. Non-English text falls back to the pre-trained XLM-RoBERTa multilingual model, which was not fine-tuned on the macro sentiment training mix.
- **Domain-specific** — trained on financial news, earnings reports, climate disclosures, and financial tweets. Performance on general-purpose sentiment tasks (movie reviews, product reviews) will be lower.
- **Dictionary lag** — the Loughran-McDonald and Henry dictionaries use static word lists that may not capture emerging financial terminology or evolving language patterns.
- **No temporal awareness** — the model treats each text independently and does not incorporate time-series context or market state.
- **Topic router is keyword-based** — the routing heuristic may misclassify ambiguous texts. Use `mode="all"` for important decisions to get ensemble averaging across all heads.
- **Label noise** — the FiQA dataset uses continuous sentiment scores thresholded at ±0.15 to create discrete labels, introducing boundary noise for scores near the thresholds.

## Citation

If you use this model or pipeline, please cite the base models:

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

## Repository Contents

```
├── model.safetensors          # FinBERT fine-tuned weights (109M params)
├── config.json                # Model config (3-class: positive/negative/neutral)
├── tokenizer.json             # BERT tokenizer
├── eval_results.json          # In-domain benchmarks for all heads
├── eval_ood_results.json      # Out-of-domain benchmarks
├── artifacts/
│   ├── meta_classifier.joblib # GradientBoosting meta-classifier on dictionary features
│   └── smart_router.joblib    # Topic routing model
├── macro_sentiment/
│   ├── __init__.py            # Public API exports
│   ├── pipeline.py            # MacroSentimentPipeline — main entry point
│   ├── transformers_ensemble.py # Multi-head transformer ensemble + topic router
│   ├── dictionaries.py        # LM, Henry, Climate, Macro dictionary scorers
│   ├── data_prep.py           # Dataset loading and combination (5 datasets)
│   ├── finetune.py            # Custom fine-tuning script
│   └── train_meta.py          # Meta-classifier training script
└── requirements.txt
```

## Framework Versions

- Transformers 5.6.2
- PyTorch 2.11.0+cu130
- Datasets 4.8.4
- Tokenizers 0.22.2

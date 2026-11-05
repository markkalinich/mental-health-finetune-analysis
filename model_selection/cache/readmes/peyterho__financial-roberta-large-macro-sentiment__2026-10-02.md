---
library_name: transformers
license: apache-2.0
base_model: soleimanian/financial-roberta-large-sentiment
tags:
- text-classification
- sentiment-analysis
- finance
- macroeconomics
- policy
- central-bank
- roberta
- roberta-large
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
model-index:
- name: financial-roberta-large-macro-sentiment
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: Combined Financial Sentiment (5 datasets)
      type: custom
    metrics:
    - type: accuracy
      value: 0.9130
      name: Accuracy
    - type: f1
      value: 0.9023
      name: F1 (macro)
    - type: f1
      value: 0.9137
      name: F1 (weighted)
  - task:
      type: text-classification
      name: Sentiment Analysis (OOD)
    dataset:
      name: Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75
      type: Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75
    metrics:
    - type: accuracy
      value: 0.9414
      name: Accuracy
    - type: f1
      value: 0.9357
      name: F1 (macro)
  - task:
      type: text-classification
      name: Sentiment Analysis (OOD)
    dataset:
      name: ic-fspml/stock_news_sentiment
      type: ic-fspml/stock_news_sentiment
    metrics:
    - type: accuracy
      value: 0.7211
      name: Accuracy
    - type: f1
      value: 0.7265
      name: F1 (macro)
---

# Financial RoBERTa-Large Macro Sentiment

A fine-tuned [soleimanian/financial-roberta-large-sentiment](https://huggingface.co/soleimanian/financial-roberta-large-sentiment) (355M params, RoBERTa-Large) for **3-class sentiment analysis on financial, macroeconomic, and climate/ESG text**. Trained on 20K samples from 5 financial NLP datasets.

**This is the best-performing head in the ensemble** — it leads on every benchmark (in-domain and out-of-domain), reaching **91.3% accuracy / 90.2% F1 macro** in-domain and **94.1% accuracy** on unseen financial phrasebank text.

This model serves as the **policy/macro head** in the [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) ensemble pipeline. The topic router selects it for central bank communications, monetary policy text, and formal macroeconomic analysis. It also works well standalone as a general-purpose financial sentiment classifier.

## Why RoBERTa-Large?

The base model ([soleimanian/financial-roberta-large-sentiment](https://huggingface.co/soleimanian/financial-roberta-large-sentiment)) was pre-trained on a broad financial corpus — financial statements, earnings call transcripts, CSR/ESG reports, and financial news — making it the most versatile foundation among the ensemble's heads. At 355M parameters with 24 transformer layers (vs. 12 for BERT-base), it has substantially more capacity to capture nuanced sentiment in complex, formal financial prose.

The 3.2× parameter increase over FinBERT (109M) yields consistent gains:

| | FinBERT (109M) | **RoBERTa-Large (355M)** | Δ |
|---|:---:|:---:|:---:|
| In-domain F1 (macro) | 0.8813 | **0.9023** | +2.1pp |
| OOD PhraseBank F1 | 0.9134 | **0.9357** | +2.2pp |
| OOD Stock News F1 | 0.6765 | **0.7265** | +5.0pp |

The largest improvement (+5pp) is on the hardest benchmark (noisy stock news headlines with 5→3 class mapping), suggesting that the extra capacity pays off most on challenging, out-of-distribution text.

## Quick Start

### Standalone Usage

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="peyterho/financial-roberta-large-macro-sentiment", top_k=None)

# Policy/macro text — the model's specialty
pipe("The Federal Reserve raised rates by 75 basis points, citing persistent inflation pressures.")
# [[{'label': 'neutral', 'score': 0.82}, {'label': 'negative', 'score': 0.15}, {'label': 'positive', 'score': 0.03}]]

pipe("The ECB signaled an extended pause in rate hikes, offering relief to debt-laden eurozone economies.")
# [[{'label': 'positive', 'score': 0.89}, {'label': 'neutral', 'score': 0.09}, {'label': 'negative', 'score': 0.02}]]

# General financial text — also excels here
pipe("Markets crashed amid recession fears and massive layoffs across the tech sector.")
# [[{'label': 'negative', 'score': 0.98}, {'label': 'neutral', 'score': 0.01}, {'label': 'positive', 'score': 0.01}]]

pipe("Q3 revenue surged 24% year-over-year, driven by strong cloud adoption.")
# [[{'label': 'positive', 'score': 0.97}, ...]]
```

### As Part of the Full Pipeline

Within the [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) pipeline, this model is automatically selected when policy/macro keywords are detected (e.g., *Federal Reserve*, *ECB*, *rate hike*, *monetary policy*, *inflation*, *FOMC*, *basis points*, *quantitative easing*):

```python
from macro_sentiment import MacroSentimentPipeline

pipe = MacroSentimentPipeline(device="cpu")

result = pipe("The Fed held rates steady but signaled two more cuts before year-end, a dovish surprise.")
print(result.summary())
# Sentiment: Positive (+0.421) | Policy: Dovish (-0.600) | Crisis: Normal (0.000) | Domain: policy
print(result.head_used)
# "policy"

result = pipe("Inflation expectations became unanchored as the central bank lost credibility.")
print(result.summary())
# Sentiment: Negative (-0.584) | Policy: Neutral (+0.000) | Crisis: Elevated (0.350) | Domain: policy
```

## Label Mapping

This model uses the standard 3-class label ordering — no remapping needed:

| Label ID | Label | Score Mapping |
|:---:|---|:---:|
| 0 | `negative` | -1.0 |
| 1 | `neutral` | 0.0 |
| 2 | `positive` | +1.0 |

> Unlike FinBERT (positive=0, negative=1) and ClimateBERT (opportunity=0, risk=2), this model's label IDs follow the natural negative→neutral→positive ordering, making standalone usage straightforward.

## Evaluation Results

### In-Domain (Combined Test Set — 4,333 samples)

All three fine-tuned heads compared on the same held-out test split:

| Model | Params | Accuracy | F1 (macro) | F1 (weighted) |
|---|:---:|:---:|:---:|:---:|
| **RoBERTa-Large (this model)** | **355M** | **0.9130** | **0.9023** | **0.9137** |
| [FinBERT](https://huggingface.co/peyterho/finbert-macro-sentiment) | 109M | 0.8973 | 0.8813 | 0.8984 |
| [ClimateBERT](https://huggingface.co/peyterho/climatebert-macro-sentiment) | 82M | 0.8885 | 0.8716 | 0.8898 |

### Out-of-Domain: Financial Phrasebank (785 samples)

Evaluated on [Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75](https://huggingface.co/datasets/Jean-Baptiste/financial_news_sentiment_mixte_with_phrasebank_75) — PhraseBank (75% agreement) + financial news articles. **Not in the training mix.**

| Model | Params | Accuracy | F1 (macro) |
|---|:---:|:---:|:---:|
| **RoBERTa-Large (this model)** | **355M** | **0.9414** | **0.9357** |
| [ClimateBERT](https://huggingface.co/peyterho/climatebert-macro-sentiment) | 82M | 0.9248 | 0.9213 |
| [FinBERT](https://huggingface.co/peyterho/finbert-macro-sentiment) | 109M | 0.9236 | 0.9134 |

OOD accuracy actually *improves* over in-domain (94.1% vs. 91.3%) because this PhraseBank-style data is closer to the model's pre-training distribution — formal financial sentences with clearer sentiment signals than the noisier tweet and QA data in the training mix.

### Out-of-Domain: Stock News Headlines (30,150 samples)

Evaluated on [ic-fspml/stock_news_sentiment](https://huggingface.co/datasets/ic-fspml/stock_news_sentiment) — 5-class labels mapped to 3-class. **Not in the training mix.**

| Model | Params | Accuracy | F1 (macro) |
|---|:---:|:---:|:---:|
| **RoBERTa-Large (this model)** | **355M** | **0.7211** | **0.7265** |
| [FinBERT](https://huggingface.co/peyterho/finbert-macro-sentiment) | 109M | 0.6781 | 0.6765 |
| [ClimateBERT](https://huggingface.co/peyterho/climatebert-macro-sentiment) | 82M | 0.6472 | 0.6441 |

RoBERTa-Large's advantage is largest here (+5pp F1 over FinBERT), confirming that extra model capacity helps most on challenging, noisy, out-of-distribution text.

### Comparison Against Baselines

| Method | Accuracy | F1 (macro) | Notes |
|---|:---:|:---:|---|
| **RoBERTa-Large (this model)** | **0.9130** | **0.9023** | 355M params, fine-tuned |
| FinBERT (fine-tuned) | 0.8973 | 0.8813 | 109M params |
| ClimateBERT (fine-tuned) | 0.8885 | 0.8716 | 82M params |
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

All datasets unified to 3-class: `0=negative`, `1=neutral`, `2=positive`. This model's native label ordering already matches the unified schema — no remapping needed during training.

## Training Details

| Hyperparameter | Value |
|---|---|
| Base model | [soleimanian/financial-roberta-large-sentiment](https://huggingface.co/soleimanian/financial-roberta-large-sentiment) (355M, RoBERTa-Large, 24 layers, 1024 hidden, 16 heads) |
| Learning rate | 1e-5 (lower than FinBERT/ClimateBERT's 2e-5 to stabilize large model training) |
| Batch size | 16 × 4 gradient accumulation = 64 effective |
| Epochs | 6 (best checkpoint at epoch 3 by val loss) |
| Scheduler | Linear decay with 20% warmup |
| Optimizer | AdamW (weight decay 0.01) |
| Max length | 128 tokens |
| Precision | FP16 |
| Class weighting | √(inverse frequency) — handles ~58% neutral class imbalance |
| Seed | 42 |
| Best model selection | Lowest validation loss (epoch 3) |

### Why Lower Learning Rate?

Large models (>300M params) are more sensitive to learning rate — too high and the pre-trained representations are destroyed ("catastrophic forgetting"). The 1e-5 rate (vs. 2e-5 for the 82–109M heads) follows the standard practice of scaling LR inversely with model size for fine-tuning.

### Training Curve

| Epoch | Train Loss | Val Loss | Accuracy | F1 (macro) | F1 (weighted) |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | 1.511 | 0.352 | 0.852 | 0.841 | 0.854 |
| 2 | 1.196 | 0.319 | 0.866 | 0.857 | 0.868 |
| **3** | **0.766** | **0.273** | **0.908** | **0.897** | **0.909** |
| 4 | 0.462 | 0.295 | 0.907 | 0.897 | 0.908 |
| 5 | 0.345 | 0.313 | 0.911 | 0.901 | 0.912 |
| 6 | 0.283 | 0.326 | 0.913 | 0.902 | 0.914 |

Validation loss reaches its minimum at epoch 3 (0.273), then gradually increases while accuracy and F1 continue improving through epoch 6. The best checkpoint (epoch 3, lowest val loss) is loaded for the final model — this checkpoint prioritizes calibration over raw accuracy. The higher training losses compared to FinBERT/ClimateBERT are expected given the lower learning rate and larger model capacity.

## Role in the Ensemble Pipeline

This model serves as the **policy/macro specialist** in the [macro-sentiment-finbert](https://huggingface.co/peyterho/macro-sentiment-finbert) pipeline. The topic router activates it when policy-related keywords are detected in the input:

```
Input Text → Topic Router → policy/macro keywords? → RoBERTa-Large (this model) ★
                          → climate keywords?      → ClimateBERT
                          → non-English text?      → XLM-RoBERTa
                          → default                → FinBERT
```

**Policy routing keywords include:** *Federal Reserve, Fed, FOMC, ECB, Bank of England, central bank, interest rate, rate hike, rate cut, monetary policy, quantitative easing/tightening, hawkish, dovish, inflation, CPI, GDP, recession, fiscal policy, yield curve, basis points, forward guidance,* and many more (~60 keywords total).

The pipeline then fuses this model's output with four dictionary-based signals (Loughran-McDonald, Henry earnings tone, Sautner-style climate exposure, macro policy/crisis dictionaries) using crisis-adaptive weighting to produce a structured `MacroSentimentResult` with financial sentiment, policy stance, crisis signal, and confidence scores.

### Why Route Policy Text to RoBERTa-Large?

Central bank communications and macroeconomic analysis tend to be **long, formal, and nuanced** — a rate hike can be positive (inflation under control) or negative (economic tightening) depending on context. The 24-layer RoBERTa-Large architecture captures these contextual subtleties better than the shallower heads, and the base model's pre-training on earnings call transcripts and financial statements aligns well with the register of policy text.

### Ensemble Siblings

| Head | Model | Params | Role |
|---|---|:---:|---|
| **RoBERTa-Large** ★ | **peyterho/financial-roberta-large-macro-sentiment** | **355M** | **Policy/macro communications** |
| FinBERT | [peyterho/finbert-macro-sentiment](https://huggingface.co/peyterho/finbert-macro-sentiment) | 109M | Default — financial news, tweets |
| ClimateBERT | [peyterho/climatebert-macro-sentiment](https://huggingface.co/peyterho/climatebert-macro-sentiment) | 82M | Climate/ESG text |
| XLM-RoBERTa | [cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual) | 278M | Non-English text (pre-trained, not fine-tuned) |

## Custom Fine-Tuning

Fine-tune this model further on your own labelled data:

```bash
pip install transformers datasets accelerate evaluate torch

python -m macro_sentiment.finetune \
    --data my_labels.csv \
    --text-column text \
    --label-column sentiment \
    --base-model peyterho/financial-roberta-large-macro-sentiment \
    --output my-org/my-policy-model \
    --push-to-hub \
    --epochs 4 \
    --lr 5e-6 \
    --batch-size 16
```

The fine-tuning script (from the [parent repo](https://huggingface.co/peyterho/macro-sentiment-finbert)) accepts CSV, TSV, JSON, or JSONL. Labels can be strings (`"positive"`, `"negative"`, `"neutral"`, `"bullish"`, `"bearish"`) or integers (0/1/2). Class-weighted loss is applied by default. Note: use a lower learning rate (5e-6 to 1e-5) for this 355M model to avoid destabilizing the pre-trained weights.

## Latency & Resource Considerations

At 355M parameters (1.3GB safetensors), this model requires more compute than the smaller heads:

| Model | Params | Size | Throughput* |
|---|:---:|:---:|:---:|
| ClimateBERT | 82M | 314MB | ~1,300 samples/s |
| FinBERT | 109M | 418MB | ~670 samples/s |
| **RoBERTa-Large (this model)** | **355M** | **1.3GB** | **~275 samples/s** |

*\*Measured on eval set (batch size 64, CPU). GPU throughput will be proportionally higher.*

For latency-sensitive applications (real-time trading signals, high-volume social media monitoring), the FinBERT head may be preferable. For batch analysis of policy documents, earnings calls, and macroeconomic reports where accuracy matters most, this model is the best choice.

## Limitations

- **English only** — the base model was trained on English financial text. Non-English text should use the multilingual head in the full pipeline.
- **128-token max length** — fine-tuned with 128-token truncation. Longer documents (FOMC minutes, earnings calls, 10-K filings) should be chunked at paragraph level. Consider overlapping windows for documents where context spans paragraph boundaries.
- **Higher latency** — 3.2× more parameters than FinBERT means ~2.4× slower inference. The pipeline's topic routing mitigates this by only invoking RoBERTa-Large for policy-classified text.
- **Memory footprint** — requires ~1.5GB GPU memory for inference (vs. ~500MB for FinBERT). May not fit on memory-constrained edge devices.
- **Label noise** — the FiQA dataset uses continuous sentiment scores thresholded at ±0.15, and the Twitter dataset contains informal language that differs from this model's pre-training distribution (formal financial text).
- **No temporal or entity awareness** — treats each text independently. Cannot reason about whether "rates rising" is positive (for banks) or negative (for growth stocks) without additional context.
- **Policy routing heuristic** — the topic router uses keyword matching, not a learned classifier. Ambiguous text (e.g., a climate policy announcement that is both policy and climate) may be routed suboptimally. Use `mode="all"` in the pipeline to ensemble across all heads for important decisions.

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

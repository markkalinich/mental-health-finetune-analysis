---
license: apache-2.0
language:
  - ar
  - de
  - en
  - es
  - fr
  - hi
  - ja
  - ko
  - pt
  - zh
tags:
  - finance
  - sentiment-analysis
  - financial-sentiment-analysis
  - multilingual
  - xlm-roberta
  - financial-nlp
  - perspective-aware
  - stock-market
  - text-classification
  - transformers
  - pytorch
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# FLAME2 — Financial Language Analysis for Multilingual Economics v2

**One model. Ten languages. 150,000 headlines. Perspective-aware financial sentiment.**

FLAME2 is a multilingual financial sentiment classifier that labels news headlines as **Negative**, **Neutral**, or **Positive** — but unlike other models, it does this from the **local investor's perspective** of each economy.

The same news can mean opposite things for different markets:
- *"Oil prices fall to $65/barrel"* → **Negative** for Arab markets (oil exporter) / **Positive** for India (oil importer)
- *"Yen weakens to 155 per dollar"* → **Positive** for Japan (helps exporters) / **Neutral** elsewhere

No other public model does this.

---

## Key Numbers

| | |
|---|---|
| **Languages** | 10 (Arabic, German, English, Spanish, French, Hindi, Japanese, Korean, Portuguese, Chinese) |
| **Training data** | 149,481 perspective-labeled financial headlines |
| **Base model** | XLM-RoBERTa-large (560M parameters) |
| **Labels** | Negative / Neutral / Positive |
| **Accuracy** | **84.11%** |
| **F1 (macro)** | **84.20%** |

---

## Quick Start

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Kenpache/flame2")

# English — US investor perspective
classifier("[EN] Apple reported record quarterly revenue of $124 billion")
# [{'label': 'positive', 'score': 0.96}]

# Arabic — Gulf investor perspective
classifier("[AR] أسعار النفط تنخفض إلى 65 دولارا للبرميل")
# [{'label': 'negative', 'score': 0.93}]  (oil down = bad for exporters)

# Hindi — Indian investor perspective
classifier("[HI] तेल की कीमतें गिरकर 65 डॉलर प्रति बैरल हुईं")
# [{'label': 'positive', 'score': 0.91}]  (oil down = good for importers)

# Japanese
classifier("[JA] 日経平均株価が大幅下落、米中貿易摩擦の懸念で")
# [{'label': 'negative', 'score': 0.94}]

# Korean
classifier("[KO] 삼성전자 실적 호조에 코스피 상승")
# [{'label': 'positive', 'score': 0.92}]

# Chinese
classifier("[ZH] 中国央行降息50个基点，股市应声上涨")
# [{'label': 'positive', 'score': 0.95}]

# German
classifier("[DE] DAX erreicht neues Allzeithoch dank starker Bankenergebnisse")
# [{'label': 'positive', 'score': 0.93}]

# French
classifier("[FR] La Bourse de Paris chute de 3% après les tensions commerciales")
# [{'label': 'negative', 'score': 0.91}]

# Spanish
classifier("[ES] El beneficio neto de la compañía creció un 25% interanual")
# [{'label': 'positive', 'score': 0.94}]

# Portuguese
classifier("[PT] Ibovespa fecha em alta com otimismo sobre reforma tributária")
# [{'label': 'positive', 'score': 0.90}]
```

**Important:** Always use the `[LANG]` prefix (`[EN]`, `[AR]`, `[HI]`, `[JA]`, etc.) — this tells the model which market perspective to apply.

---

## Supported Languages & Training Data

| Language | Code | Primary Economy | Oil Role | Total | Negative | Neutral | Positive |
|---|---|---|---|---|---|---|---|
| Arabic | AR | Gulf States (Saudi, UAE) | Exporter | 14,481 | 2,812 (19.4%) | 6,156 (42.5%) | 5,513 (38.1%) |
| German | DE | Germany / Eurozone | Importer | 15,000 | 3,544 (23.6%) | 6,636 (44.2%) | 4,820 (32.1%) |
| English | EN | United States | Mixed | 15,000 | 3,088 (20.6%) | 7,649 (51.0%) | 4,263 (28.4%) |
| Spanish | ES | Spain / Latin America | Importer | 15,000 | 3,872 (25.8%) | 5,616 (37.4%) | 5,512 (36.7%) |
| French | FR | France / Eurozone | Importer | 15,000 | 3,218 (21.5%) | 6,252 (41.7%) | 4,530 (30.2%) |
| Hindi | HI | India | Importer | 15,000 | 3,543 (23.6%) | 5,902 (39.3%) | 5,555 (37.0%) |
| Japanese | JA | Japan | Importer | 15,000 | 3,472 (23.1%) | 5,897 (39.3%) | 5,631 (37.5%) |
| Korean | KO | South Korea | Importer | 15,000 | 3,290 (21.9%) | 6,648 (44.3%) | 5,062 (33.7%) |
| Portuguese | PT | Brazil / Portugal | Exporter | 15,000 | 3,170 (21.1%) | 7,463 (49.8%) | 4,367 (29.1%) |
| Chinese | ZH | China | Importer | 15,000 | 3,542 (23.6%) | 4,055 (27.0%) | 7,403 (49.4%) |

**Total: 149,481 labeled headlines across 10 languages.**

### Overall Class Distribution

| Class | Samples | Share |
|---|---|---|
| **Negative** | 33,551 | 22.4% |
| **Neutral** | 62,274 | 41.7% |
| **Positive** | 52,656 | 35.2% |

Data sources include financial news sites, stock market reports, and economic news agencies — labeled with perspective-aware rules specific to each economy.

---

## What Makes FLAME2 Different

### The Problem

Existing financial sentiment models treat sentiment as universal. But financial sentiment is **not** universal — it depends on **where you are**:

- Oil prices drop? Bad for Saudi Arabia, great for India.
- Yen weakens? Good for Japanese exporters, bad for Korean competitors.
- Fed raises rates? Bad for US stocks, often neutral for European markets.

### Our Solution: Perspective-Aware Labels

Every headline in our dataset was labeled from the perspective of a **local investor** in that language's primary economy. The model learns that `[AR]` means "Gulf investor" and `[HI]` means "Indian investor."

#### Oil Price Rules

| Market Type | Oil Price Falls | Oil Price Rises | OPEC+ Output Increase |
|---|---|---|---|
| **Exporters** (AR, PT) | Negative | Positive | Negative |
| **Importers** (HI, KO, DE, FR, ES, JA, ZH) | Positive | Negative | Positive |
| **Mixed** (EN/US) | Positive | Context-dependent | Positive |

#### Currency Rules

| Language | Local Currency Strengthens | Local Currency Weakens |
|---|---|---|
| AR, PT, HI, KO, ZH | Positive | Negative |
| JA (export-driven) | Negative (hurts exporters) | Positive (helps exporters) |
| EN, DE, FR, ES | Neutral | Neutral |

#### Central Bank Rules

- **Home** central bank: rate cut = Positive, rate hike = Negative, hold = Neutral
- **Foreign** central bank: Neutral (unless headline explicitly links to local market impact)

---

## Labels

| Label | ID | Examples |
|---|---|---|
| **negative** | 0 | Stock decline, losses, layoffs, downgrades, sanctions, bankruptcy |
| **neutral** | 1 | Factual reporting, mixed signals, foreign data without local impact |
| **positive** | 2 | Revenue growth, market rally, upgrades, new launches, rate cuts |

---

## Results

### Overall

| Metric | Score |
|---|---|
| **Accuracy** | **84.11%** |
| **F1 (macro)** | **84.20%** |

### Per-Language Performance

| Language | Code | Accuracy | F1 Macro | Test Samples |
|---|---|---|---|---|
| Hindi | HI | 89.33% | 89.15% | 1,125 |
| Spanish | ES | 85.44% | 85.31% | 1,573 |
| Japanese | JA | 84.42% | 84.23% | 1,489 |
| French | FR | 84.06% | 84.24% | 2,579 |
| English | EN | 83.84% | 83.74% | 1,875 |
| Korean | KO | 83.54% | 83.71% | 3,280 |
| German | DE | 83.56% | 83.96% | 1,928 |
| Chinese | ZH | 83.50% | 81.43% | 1,751 |
| Portuguese | PT | 83.28% | 82.95% | 1,639 |
| Arabic | AR | 83.18% | 83.26% | 2,569 |

### Per-Class Performance

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Negative | 0.81 | 0.87 | 0.84 | 4,487 |
| Neutral | 0.86 | 0.78 | 0.82 | 8,398 |
| Positive | 0.84 | 0.90 | 0.87 | 6,923 |

---

## Training Pipeline

FLAME2 was built in two stages:

### Stage 1: Supervised Fine-Tuning

XLM-RoBERTa-large was fine-tuned on ~150,000 perspective-labeled headlines with:
- **Focal Loss** (gamma=2.0) — focuses training on hard, misclassified examples instead of easy ones
- **Class weights** to handle label imbalance across languages
- **Label smoothing** (0.1) to handle ~3-5% annotation noise
- **Language prefix** `[LANG]` injected before each headline for perspective routing
- **GroupShuffleSplit** by news source domain — no article from the same source appears in both train and test (prevents data leakage)
- **Gradient clipping** (max_norm=1.0) for training stability

### Stage 2: Live Stochastic Weight Averaging (SWA)

After epoch 12, the learning rate switches to a constant low rate (1e-5) and an `AveragedModel` maintains a running average of weights updated every epoch. This produces smoother, more generalizable predictions than any single checkpoint.

### Training Details

| Parameter | Value |
|---|---|
| Base model | xlm-roberta-large (560M params) |
| Fine-tuning data | ~150,000 labeled headlines |
| Languages | 10 |
| Loss function | Focal Loss (gamma=2.0) |
| Learning rate | 2e-5 (→ 1e-5 SWA phase) |
| Label smoothing | 0.1 |
| Batch size | 32 |
| Max sequence length | 128 tokens |
| Precision | FP16 (mixed precision) |
| Train/Val/Test split | 70% / 15% / 15% |
| Split strategy | GroupShuffleSplit by source domain |
| SWA | Live averaging from epoch 12 |

---

## Batch Processing

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Kenpache/flame2", device=0)

texts = [
    "[EN] Stocks rallied after the Fed signaled a pause in rate hikes.",
    "[EN] The company filed for Chapter 11 bankruptcy protection.",
    "[DE] DAX erreicht neues Allzeithoch dank starker Bankenergebnisse",
    "[FR] La Bourse de Paris chute de 3% après les tensions commerciales",
    "[ES] El beneficio neto de la compañía creció un 25% interanual",
    "[ZH] 中国央行降息50个基点，股市应声上涨",
    "[PT] Ibovespa fecha em alta com otimismo sobre reforma tributária",
    "[AR] ارتفاع مؤشر السوق السعودي بنسبة 2% بعد إعلان أرباح أرامكو",
    "[HI] भारतीय रिजर्व बैंक ने रेपो रेट में 25 बीपीएस की कटौती की",
    "[JA] トヨタ自動車の純利益が前年比30%増加",
    "[KO] 삼성전자 실적 호조에 코스피 상승",
]

results = classifier(texts, batch_size=32)
for text, result in zip(texts, results):
    print(f"{result['label']:>8} ({result['score']:.2f})  {text[:70]}")
```

---

## Use Cases

- **Global News Monitoring** — real-time sentiment classification across 10 markets
- **Algorithmic Trading** — perspective-aware signals: same event, different trades per market
- **Portfolio Risk Management** — track sentiment shifts across international holdings
- **Cross-Market Arbitrage** — detect when markets react differently to the same news
- **Financial NLP Research** — first multilingual perspective-aware sentiment benchmark

---

## Limitations

- Optimized for **news headlines** (short text, 1-2 sentences). May underperform on long articles or social media.
- Perspective rules cover major economic patterns (oil, currency, central banks). Niche sector-specific effects may not be captured.
- Labels reflect the perspective of the **primary economy** for each language (e.g., AR = Gulf States, not all Arabic-speaking countries).

---

## Citation

```bibtex
@misc{flame2_2026,
  title={FLAME2: Financial Language Analysis for Multilingual Economics v2},
  author={Kenpache},
  year={2026},
  url={https://huggingface.co/Kenpache/flame2}
}
```

## License

Apache 2.0

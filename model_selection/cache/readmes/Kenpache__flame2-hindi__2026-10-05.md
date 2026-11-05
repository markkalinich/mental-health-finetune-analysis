---
license: apache-2.0
language:
  - hi
tags:
  - finance
  - sentiment-analysis
  - financial-sentiment-analysis
  - hindi
  - text-classification
  - transformers
  - pytorch
metrics:
  - accuracy
  - f1
pipeline_tag: text-classification
---

# FLAME2-Hindi — Financial Sentiment Analysis for Indian Markets

**One model. One market. Perspective-aware financial sentiment for India.**

FLAME2-Hindi classifies Hindi financial news headlines as **Negative**, **Neutral**, or **Positive** from the perspective of an **Indian investor**.

This means economic events are labeled based on how they impact the Indian economy:
- *"तेल की कीमतें गिरकर 65 डॉलर प्रति बैरल हुईं"* (Oil falls to $65) → **Positive** (India is an oil importer)
- *"भारतीय रिजर्व बैंक ने रेपो रेट में कटौती की"* (RBI cuts repo rate) → **Positive** (stimulates growth)
- *"रुपया डॉलर के मुकाबले कमजोर हुआ"* (Rupee weakens vs dollar) → **Negative** (hurts imports)

Part of the [FLAME2](https://huggingface.co/Kenpache/flame2) family.

---

## Key Numbers

| | |
|---|---|
| **Language** | Hindi |
| **Market perspective** | India (oil importer) |
| **Training data** | 15,000 perspective-labeled headlines |
| **Base model** | IndicBERTv2-MLM-only (278M parameters) |
| **Labels** | Negative / Neutral / Positive |
| **Accuracy** | **88.01%** |
| **F1 (macro)** | **88.01%** |

---

## Quick Start

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Kenpache/flame2-hindi")

# Oil prices fall — positive for India (importer)
classifier("तेल की कीमतें गिरकर 65 डॉलर प्रति बैरल हुईं")
# [{'label': 'positive', 'score': 0.94}]

# RBI cuts rate — positive
classifier("भारतीय रिजर्व बैंक ने रेपो रेट में 25 बीपीएस की कटौती की")
# [{'label': 'positive', 'score': 0.95}]

# Sensex drops — negative
classifier("सेंसेक्स 500 अंक गिरा, निवेशकों में बेचैनी")
# [{'label': 'negative', 'score': 0.93}]

# Company reports results — neutral
classifier("टाटा स्टील ने तिमाही नतीजे घोषित किए")
# [{'label': 'neutral', 'score': 0.88}]
```

**No language prefix needed** — this model is Hindi-only.

---

## Results

### Overall

| Metric | Score |
|---|---|
| **Accuracy** | **88.01%** |
| **F1 (macro)** | **88.01%** |

### Per-Class Performance

| Class | Precision | Recall | F1 | Support |
|---|---|---|---|---|
| Negative | 0.88 | 0.88 | 0.88 | 402 |
| Neutral | 0.88 | 0.84 | 0.86 | 709 |
| Positive | 0.88 | 0.93 | 0.90 | 640 |

---

## Training Data

| | |
|---|---|
| **Total samples** | 15,000 |
| **Negative** | 3,543 (23.6%) |
| **Neutral** | 5,902 (39.3%) |
| **Positive** | 5,555 (37.0%) |

Data sources include Indian financial news sites and economic news agencies. All headlines labeled from the **Indian investor perspective** — oil price drops are positive (India imports oil), rupee strengthening is positive, RBI rate cuts are positive.

---

## Training Details

| Parameter | Value |
|---|---|
| Base model | ai4bharat/IndicBERTv2-MLM-only (278M params) |
| Fine-tuning data | 15,000 Hindi financial headlines |
| Loss function | Focal Loss (gamma=2.0) |
| Learning rate | 2e-5 (→ 1e-5 SWA phase) |
| Label smoothing | 0.1 |
| Batch size | 32 |
| Max sequence length | 128 tokens |
| Epochs | 25 |
| Precision | FP16 (mixed precision) |
| Train/Val/Test split | 70% / 15% / 15% |
| SWA | Live averaging from epoch 12 |

---

## Perspective Rules (India)

| Event | Sentiment | Why |
|---|---|---|
| Oil prices fall | **Positive** | India is a major oil importer |
| Oil prices rise | **Negative** | Increases import costs |
| Rupee strengthens | **Positive** | Cheaper imports |
| Rupee weakens | **Negative** | Costlier imports |
| RBI rate cut | **Positive** | Stimulates economy |
| RBI rate hike | **Negative** | Tightens liquidity |
| Foreign CB actions | **Neutral** | Unless linked to Indian market |

---

## Batch Processing

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="Kenpache/flame2-hindi", device=0)

texts = [
    "सेंसेक्स ने 75000 का नया रिकॉर्ड बनाया",
    "महंगाई दर बढ़कर 6.5% पर पहुंची",
    "आरबीआई ने रेपो रेट में 25 बीपीएस की कटौती की",
    "रुपया डॉलर के मुकाबले 83.50 पर स्थिर",
    "रिलायंस का मुनाफा 15% बढ़ा",
]

results = classifier(texts, batch_size=32)
for text, result in zip(texts, results):
    print(f"{result['label']:>8} ({result['score']:.2f})  {text[:60]}")
```

---

## Limitations

- Optimized for **news headlines** (short text, 1-2 sentences)
- Perspective reflects **Indian economy** — may not apply to Hindi speakers in other countries
- Best on financial/economic news — general news or social media may underperform

---

## Citation

```bibtex
@misc{flame2_hindi_2026,
  title={FLAME2-Hindi: Financial Sentiment Analysis for Indian Markets},
  author={Kenpache},
  year={2026},
  url={https://huggingface.co/Kenpache/flame2-hindi}
}
```

## License

Apache 2.0

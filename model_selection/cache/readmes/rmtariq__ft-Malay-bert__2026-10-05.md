---
language:
- ms
- en
tags:
- text-classification
- sentiment
- malaysian
- bahasa-malaysia
- code-switching
- educational
license: apache-2.0
pipeline_tag: text-classification
---

# rmtariq/ft-Malay-bert

Fine-tuned sentiment classifier (3-class) for Malaysian higher-education
feedback. Trained on **MYUniDialectSentiment840 (840 samples, 14 dialects, 20 topics, 15 learning contexts)**, a hand-curated balanced corpus covering
Standard Malay, 13 regional dialects, and Manglish code-switching.

## Labels
- `negative`
- `neutral`
- `positive`

## Held-out test metrics (n=147, stratified)

| split | accuracy | f1_macro |
|---|---:|---:|
| validation (n=105) | 1.0000 | 1.0000 |
| test (n=147) | 0.9932 | 0.9932 |

## Intended use

Sentiment / emotion monitoring of student feedback for Malaysian
higher-education institutions. Designed to handle code-switched,
dialect-heavy and informal academic discourse.

## Training details

- Base: previous revision of `rmtariq/ft-Malay-bert`
- Optimizer: AdamW (lr=2e-5, weight_decay=0.01, warmup_ratio=0.1)
- Epochs: 5 with early stopping on validation macro-F1
- Batch size: 16 (train) / 32 (eval), max_length=128
- Hardware: Apple Silicon MPS
- Class-weighted cross-entropy (for emotion only)

## Dataset

`MYUniDialectSentiment840` — 840 samples, balanced on sentiment, stratified
70/12.5/17.5 train/val/test by sentiment-x-dialect.

## Citation / authors

- Raja Mohd Tariqi B. Raja Lope Ahmad — Ts., Fiscal Digest Sdn. Bhd.
- Raja Qatrun Nada Bin Raja Mohd Tariqi — Master of Education, UKM

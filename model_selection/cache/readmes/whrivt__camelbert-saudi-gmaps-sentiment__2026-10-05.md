---
language:
- ar
license: apache-2.0
library_name: transformers
tags:
- sentiment-analysis
- arabic
- saudi-arabic
- saudi-dialect
- google-maps-reviews
- bert
- text-classification
- camelbert
- fine-tuned
base_model: CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment
pipeline_tag: text-classification
metrics:
- accuracy
- f1
widget:
- text: "المطعم رائع جدا والاكل لذيذ وننصح فيه"
  example_title: "Positive review"
- text: "تجربه سيئه جدا الخدمه بطيئه ومافي نظافه"
  example_title: "Negative review"
- text: "عادي مافي شي مميز"
  example_title: "Neutral review"
- text: "والله ابداع 😍🔥 احسن مكان جربته"
  example_title: "Positive with emoji"
- text: "الكفي حلو بس الموظفين مو محترمين"
  example_title: "Mixed (neutral)"
---

# CAMeL-BERT Saudi Google Maps Sentiment

Fine-tuned Arabic BERT model for **3-class sentiment analysis on Saudi Google Maps reviews**.

**Classes:** positive · negative · neutral

**Base model:** [`CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment`](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment)

**Paper:** *Fine-Tuning CAMeL-BERT for Saudi Dialect Sentiment Analysis on Google Maps Reviews* — Abdullah Mosfer, King Khalid University (2025)

---

## Performance

### vs. Original Baseline (test set, 369 reviews)

| Metric | Original CAMeL-DA | Fine-tuned (ours) | Improvement |
|---|---|---|---|
| Accuracy | 69.92% | **75.07%** | +5.15 pp ⬆ |
| F1-macro | 0.6690 | **0.7388** | +0.0698 ⬆ |
| F1-weighted | 0.6977 | **0.7567** | +0.0590 ⬆ |

### Per-Class Results (fine-tuned model)

| Class | Precision | Recall | F1-score | Support |
|---|---|---|---|---|
| positive | 0.8028 | 0.7972 | 0.8000 | 143 |
| negative | 0.8793 | 0.7183 | 0.7907 | 142 |
| neutral | 0.5495 | 0.7262 | 0.6256 | 84 |
| **macro avg** | **0.7439** | **0.7472** | **0.7388** | 369 |
| **weighted avg** | **0.7746** | **0.7507** | **0.7567** | 369 |

### Key improvements over baseline
- **Neutral class F1:** 0.488 → 0.626 (+13.8 pp) — largest gain, driven by mislabel filtering
- **Negative precision:** 0.764 → 0.879 (+11.5 pp) — negative predictions are 88% reliable
- **Positive F1:** 0.760 → 0.800 (+4.0 pp)

---

## Quick Start

```python
from transformers import pipeline
import re

clf = pipeline(
    "text-classification",
    model="whrivt/camelbert-saudi-gmaps-sentiment"
)

# IMPORTANT: always apply preprocessing before prediction
def clean_review(t):
    import re
    t = re.sub(r'<[^>]+>', ' ', t)                          # HTML tags
    t = re.sub(r'https?://\S+|www\.\S+', ' ', t)           # URLs
    t = re.sub(r'@\w+', ' ', t)                             # mentions
    t = re.sub(r'[إأآا]', 'ا', t)                          # alef normalization
    t = re.sub(r'ى', 'ي', t)                               # ya normalization
    t = re.sub(r'ة', 'ه', t)                               # ta-marbuta
    t = re.sub(r'[\u0617-\u061A\u064B-\u0652\u0670\u0640]', '', t)  # diacritics
    t = re.sub(r'(.)\1{2,}', r'\1', t)                     # elongations
    t = re.sub(r'\s+', ' ', t).strip()
    return t

reviews = [
    "المطعم رائع جدا والاكل لذيذ وننصح فيه",
    "تجربه سيئه جدا الخدمه بطيئه ومافي نظافه",
    "عادي مافي شي مميز بس مو سيي",
]

for review in reviews:
    result = clf(clean_review(review))[0]
    print(f"{review}")
    print(f"→ {result['label']} (confidence: {result['score']:.2f})\n")
```

**Output:**
```
المطعم رائع جدا والاكل لذيذ وننصح فيه
→ positive (confidence: 0.94)

تجربه سيئه جدا الخدمه بطيئه ومافي نظافه
→ negative (confidence: 0.85)

عادي مافي شي مميز بس مو سيي
→ neutral (confidence: 0.61)
```

---

## Labels

| ID | Label |
|---|---|
| 0 | positive |
| 1 | negative |
| 2 | neutral |

---

## Training Details

### Dataset
- **4,007** labeled Saudi Google Maps reviews (restaurants, cafes, places)
- **3 classes:** positive (36.9%), negative (37.4%), neutral (25.6%)
- After automatic mislabel filtering: **3,748 samples**
- Split: 80% train / 10% validation / 10% test (stratified, seed=42)

### Five-Stage Fine-tuning Pipeline

**Stage 1 — Saudi-specific preprocessing:**
Arabic character normalization (alef variants, ya, ta-marbuta), diacritic removal, elongation collapse (راااائع → رائع), emoji-to-token conversion (😍 → "ايجابي", 😡 → "سلبي"), HTML and URL stripping.

**Stage 2 — Automatic mislabel detection (5-fold cross-validation):**
Every training sample received an out-of-fold prediction from a model that never saw it during training. Samples where the model disagreed with the label at ≥ 0.95 confidence were removed. This identified **259 likely mislabeled rows** (6.5%), with 63% from the neutral class. Removal was done using independent OOF predictions — not the fine-tuned model itself — to avoid circular bias.

**Stage 3 — Anti-overfitting regularization:**
CAMeL-BERT has 110M parameters trained on only ~3,750 samples. To prevent memorization:
- Frozen embeddings + bottom 6 of 12 transformer layers → reduces trainable params from 110M to ~45M
- Hidden/attention dropout: 0.1 → 0.2
- Classifier dropout: 0.1 → 0.3
- Label smoothing: ε = 0.1
- Weight decay: λ = 0.05 (5× default)
- Max 3 epochs with early stopping (patience = 1) on validation F1-macro

**Stage 4 — Class-weighted training:**
Soft class weights (sqrt of inverse frequency): positive=0.914, negative=0.908, neutral=1.178. Applied via weighted cross-entropy loss.

**Stage 5 — Multi-seed ensemble:**
Three models trained with seeds 42, 123, 7. Softmax outputs averaged at inference. Best single model (seed 42, val F1-macro=0.7087) saved for deployment.

### Hyperparameters

| Parameter | Value |
|---|---|
| Base model | CAMeL-Lab/bert-base-arabic-camelbert-da-sentiment |
| Max sequence length | 192 tokens |
| Learning rate | 2e-5 |
| Batch size | 16 |
| Epochs | 3 + early stopping (patience=1) |
| Weight decay | 0.05 |
| Frozen layers | Embeddings + layers 0–5 |
| Hidden dropout | 0.2 |
| Classifier dropout | 0.3 |
| Label smoothing | 0.1 |
| Mixed precision | fp16 |
| Framework | Hugging Face Transformers 4.44.2 |
| GPU | NVIDIA Tesla T4 |

---

## Limitations

- Trained on restaurant and place reviews; may underperform on other domains (hotels, products, etc.)
- The neutral class has lower precision (0.55) — predictions with confidence < 0.70 should be treated as uncertain
- Evaluation is on Saudi dialect; performance on other Arabic dialects is untested
- Dataset size (~4,000 samples) is modest; accuracy ceiling is partly constrained by residual label noise
- **Always apply the preprocessing function** before inference — the model was trained on cleaned text

---

## Citation

If you use this model, please cite:

```bibtex
@misc{mosfer2025camelbert,
  title     = {Fine-Tuning CAMeL-BERT for Saudi Dialect Sentiment Analysis on Google Maps Reviews},
  author    = {Mosfer, Abdullah},
  year      = {2025},
  institution = {King Khalid University},
  note      = {Undergraduate Research Project. Model available at https://huggingface.co/whrivt/camelbert-saudi-gmaps-sentiment}
}
```

---

## References

- Inoue et al. (2021). *The interplay of variant, size, and task type in Arabic pre-trained language models.* WANLP 2021. *(CAMeL-BERT paper)*
- Abdul-Mageed et al. (2021). *ARBERT & MARBERT: Deep bidirectional transformers for Arabic.* ACL 2021.
- Antoun et al. (2020). *AraBERT: Transformer-based model for Arabic language understanding.* OSACT 2020.
- Devlin et al. (2019). *BERT: Pre-training of deep bidirectional transformers for language understanding.* NAACL 2019.
- Northcutt et al. (2021). *Pervasive label errors in test sets destabilize machine learning benchmarks.* NeurIPS 2021.
- Wolf et al. (2020). *Transformers: State-of-the-art natural language processing.* EMNLP 2020.

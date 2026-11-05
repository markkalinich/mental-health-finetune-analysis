---
language:
- ar
license: cc-by-4.0
library_name: transformers
pipeline_tag: text-classification
base_model: UBC-NLP/MARBERTv2
datasets:
- srinivasbilla/semeval-2016-absa-reviews-arabic
tags:
- arabic
- dialectal-arabic
- sentiment-analysis
- morphology
- marbert
- arasenteval
- osact
- custom_code
metrics:
- f1
model-index:
- name: SARF-MARBERTv2
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      name: AraSentEval 2026 (OSACT7 shared task), official test set
      type: arasenteval-2026
    metrics:
    - type: f1
      name: Macro-F1
      value: 0.9263
---

# SARF (صرف): Sentiment Analysis via Root-based Fusion for Multi-Dialectal Arabic

**SARF** is a 3-class (negative / neutral / positive) sentiment classifier for
dialectal Arabic. It reads each sentence in three **morphological views**:
the normalized surface form, a light stem, and the consonantal root. All three
go through one **shared MARBERTv2 encoder** and are fused with cross-attention.

This is the exact model behind the **TTLab** submission to the
**AraSentEval 2026** shared task (OSACT7 @ LREC 2026). It reached a
**macro-F1 of 0.9263** on the official test set and placed **2nd of 15 teams**.

📄 Paper: [TTLab at AraSentEval: SARF (صرف) Sentiment Analysis via Root-based Fusion for Multi-Dialectal Arabic](https://aclanthology.org/2026.osact-1.35/)
💻 Code: [github.com/aliabusaleh/ArabicSentimentAnalysis_AraSentEval_2026](https://github.com/aliabusaleh/ArabicSentimentAnalysis_AraSentEval_2026)

## Model details

| | |
|---|---|
| **Developed by** | Ali Abusaleh, Bhuvanesh Verma, Alexander Mehler (Text Technology Lab, Goethe University Frankfurt) |
| **Model type** | Multi-view BERT + cross-attention + CNN/LSTM classifier |
| **Base model** | [`UBC-NLP/MARBERTv2`](https://huggingface.co/UBC-NLP/MARBERTv2) |
| **Language** | Arabic: Egyptian, Saudi, Jordanian and Moroccan (Darija) dialects, plus MSA |
| **Domain** | Hotel / tourism reviews |
| **Labels** | `0: negative`, `1: neutral`, `2: positive` |
| **Parameters** | ~167.5M |

### Architecture

```
            ┌─ surface ─┐      ┌─ stem ─┐       ┌─ root ─┐
 sentence ─▶│ normalize │ ───▶ │ Snowball│ ───▶ │Tashaphyne│
            └─────┬─────┘      └───┬────┘       └───┬────┘
                  ▼                ▼                ▼
              MARBERTv2 ════ shared weights ═══ MARBERTv2 (×3 passes)
                  │ H_s            │ H_st           │ H_r
                  │      ┌─────────┴────────────────┘
                  │      ▼  shared 8-head cross-attention (Q = H_s)
                  │   A_st = Attn(H_s, H_st),  A_r = Attn(H_s, H_r)
                  │      │
                  │   F = (H_s + A_st + A_r) / 3
                  ▼      ▼
      CNN (k=3,4,5 × 200) on H_s    LSTM (128) on F → mean-pool
                  └──────── concat (728) ────────┘
                              ▼
                     Dropout(0.3) → Linear → 3 classes
```

* **Surface view:** URLs and digits removed, diacritics and tatweel stripped,
  repeated characters collapsed, and Alef/Hamza variants normalized
  (أ إ آ → ا, ؤ → و, ئ → ي).
* **Stem view:** Snowball Arabic stemmer (PyStemmer).
* **Root view:** Tashaphyne `ArabicLightStemmer.get_root()`.

## How to use

The model ships custom code, so pass `trust_remote_code=True`. The
morphological preprocessing needs three small extra packages:

```bash
pip install torch transformers PyStemmer tashaphyne pyarabic
```

```python
from transformers import AutoModel, AutoTokenizer

repo = "alighabusaleh/SARF-MARBERTv2-Arabic-Sentiment"
tokenizer = AutoTokenizer.from_pretrained(repo, trust_remote_code=True)
model = AutoModel.from_pretrained(repo, trust_remote_code=True).eval()

texts = [
    "الفندق كان رائع والخدمة ممتازة",      # positive
    "الغرفة كانت وسخة وما عجبتني",          # negative
]
print(model.predict(texts, tokenizer))
# ['positive', 'negative']

print(model.predict(texts[0], tokenizer, return_probs=True))
# [{'label': 'positive', 'scores': {'negative': 7e-05, 'neutral': 7e-05, 'positive': 0.9999}}]
```

For custom batching, `model.encode(texts, tokenizer)` returns the six input
tensors: `input_ids` / `attention_mask` for the surface, stem and root views.
Pass them straight to `model(**batch)`:

```python
import torch
batch = model.encode(texts, tokenizer)
with torch.no_grad():
    logits = model(**batch).logits
labels = [model.config.id2label[i] for i in logits.argmax(-1).tolist()]
```

> ⚠️ **Always pad to 128 tokens.** The LSTM branch mean-pools over *all* 128
> positions, including padding, exactly as in training. `encode()` already pads
> to `max_length=128`. If you tokenize yourself with dynamic padding, the
> predictions will differ from the reported results.

The released weights were checked against the original training checkpoint.
They are bit-identical, and they reproduce the leaderboard submission exactly
(312/312 test predictions match).

## Training

Training ran in two stages, with the same hyperparameters (found by a W&B sweep):

| Hyperparameter | Value |
|---|---|
| Optimizer | AdamW, weight decay 0.02 |
| Learning rate | 1.24e-4 (stage 1), 1.24e-5 (stage 2) |
| Batch size | 128 |
| Max sequence length | 128 |
| CNN filters / kernels | 200 / {3, 4, 5} |
| LSTM hidden size | 128 (1 layer, unidirectional) |
| Dropout | 0.3 |
| Loss | Cross-entropy |

1. **Stage 1: transfer from MSA hotel reviews.** 10 epochs on the Arabic hotel
   reviews from SemEval-2016 Task 5 ABSA
   ([`srinivasbilla/semeval-2016-absa-reviews-arabic`](https://huggingface.co/datasets/srinivasbilla/semeval-2016-absa-reviews-arabic)).
   Sentence-level labels, de-duplicated by sentence.
2. **Stage 2: dialectal adaptation.** 10 epochs at a 10× lower learning rate on
   the AraSentEval 2026 training set: 1,731 sentences, balanced across Darija,
   Saudi, Jordanian and Egyptian (657 negative / 609 positive / 465 neutral).

## Evaluation

| Split | Macro-F1 |
|---|---|
| AraSentEval 2026 official test set | **0.9263** (2nd / 15 teams) |

See the paper for the full results and analysis.

## Limitations

* Trained only on hotel and tourism reviews. Expect lower accuracy on other
  domains such as politics, social media or product reviews.
* Covers four dialects: Egyptian, Saudi, Jordanian and Moroccan. Other dialects
  (e.g. Iraqi, Sudanese, Gulf varieties beyond Saudi) and Arabizi (Latin-script
  Arabic) are not represented in the training data.
* Neutral is the hardest class. Most errors are neutral sentences predicted as
  positive or negative.
* The root and stem extractors are rule-based and designed for MSA. They are
  noisy on dialectal words; the model learns to weight them through
  cross-attention.
* Every input runs the encoder three times, so inference costs about 3× a
  single MARBERTv2 forward pass.

## Citation

If you use this model, please cite our paper:

```bibtex
@inproceedings{abusaleh-etal-2026-ttlab,
    title = "{TTL}ab at {A}ra{S}ent{E}val: {SARF}( صرف) Sentiment Analysis via Root-based Fusion for Multi-Dialectal {A}rabic",
    author = "Abusaleh, Ali  and
      Verma, Bhuvanesh  and
      Mehler, Alexander",
    editor = "Al-Khalifa, Hend  and
      El-Haj, Mo  and
      Ezzini, Saad",
    booktitle = "The 7th Workshop on Open-Source {A}rabic Corpora and Processing Tools ({OSACT}7) with 5 Shared Tasks",
    month = may,
    year = "2026",
    address = "Palma, Mallorca (Spain)",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2026.osact-1.35/",
    doi = "10.63317/4wj6s3ys5osk",
    pages = "262--268"
}
```

Please also cite MARBERT (Abdul-Mageed et al., ACL 2021), which SARF builds on.

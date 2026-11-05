---
language:
- hi
- en
- bn
tags:
- sentiment-analysis
- code-mixed
- hinglish
- lora
- muril
base_model: google/muril-base-cased
datasets:
- md-nishat-008/Code-Mixed-Sentiment-Analysis-Dataset
metrics:
- accuracy
- f1
pipeline_tag: text-classification
license: apache-2.0
---

# MuRIL Fine-tuned for Code-Mixed Sentiment Analysis

Fine-tuned [`google/muril-base-cased`](https://huggingface.co/google/muril-base-cased) on code-mixed (Hindi-English, Bengali-English) sentiment classification using LoRA (Low-Rank Adaptation).

## Model Description

- **Base model:** MuRIL (Multilingual Representations for Indian Languages) — pre-trained on 17 Indic languages
- **Fine-tuning method:** LoRA (r=8, alpha=16) via the [PEFT library](https://github.com/huggingface/peft)
- **Task:** 3-class sentiment classification — Negative (0), Neutral (1), Positive (2)
- **Dataset:** [`md-nishat-008/Code-Mixed-Sentiment-Analysis-Dataset`](https://huggingface.co/datasets/md-nishat-008/Code-Mixed-Sentiment-Analysis-Dataset) — 99,999 code-mixed samples

## Results

Evaluated on 19,998 held-out test samples. Compared against zero-shot and few-shot LLM prompting (Llama 3.1 8B via Groq API):

| Method | Accuracy | Macro F1 | Avg Latency |
|--------|----------|----------|-------------|
| MuRIL zero-shot (no training) | 0.3334 | 0.1667 | — |
| **MuRIL + LoRA fine-tuned (this model)** | **0.7127** | **0.7142** | **~5ms (local)** |
| LLM zero-shot (Llama 3.1 8B) | 0.6307 | 0.6106 | 3934ms/call |
| LLM 5-shot (Llama 3.1 8B) | 0.7186 | 0.7158 | 4944ms/call |

**Key finding:** Fine-tuned MuRIL matches 5-shot LLM prompting on F1 (0.7142 vs 0.7158) while running locally at ~1000x lower latency and zero per-query API cost.

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="chaturvedipriyanshu17/muril-lora-codemixed-sentiment",
)

texts = [
    "yaar ye product bilkul bakwaas hai, waste of money",
    "bahut achha product hai, highly recommend!",
    "ठीक है, काम चला सकते हैं but nothing special",
]

for text in texts:
    result = classifier(text)[0]
    print(f"{result['label']} ({result['score']:.2f}): {text}")
# LABEL_0 = Negative, LABEL_1 = Neutral, LABEL_2 = Positive
```

## Training Details

- **Epochs:** 3
- **Batch size:** 32
- **Learning rate:** 2e-4
- **Max sequence length:** 128
- **Precision:** fp16
- **Hardware:** Kaggle P100
- **Trainable parameters:** 297,219 / 237,855,750 (0.125%) — LoRA keeps base model frozen

## Label Map

| Label | Sentiment |
|-------|-----------|
| LABEL_0 | Negative |
| LABEL_1 | Neutral |
| LABEL_2 | Positive |

## Limitations

- Trained primarily on product/service reviews — may not generalise to other domains
- Dataset contains Bengali-English mixing in addition to Hindi-English; performance may vary by language pair
- Not evaluated on pure Hindi or pure English text

## Citation

```
arxiv: 2309.10272 — Mixed-Distil-BERT: Code-mixed Language Modeling for Indo-Aryan Languages
arxiv: 2103.07792 — Multilingual Code-Switching for Zero-Shot Cross-Lingual Intent Prediction
```

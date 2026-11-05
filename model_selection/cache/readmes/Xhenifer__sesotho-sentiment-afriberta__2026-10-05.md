---
license: cc-by-nc-4.0
language:
- st
metrics:
- f1
- matthews_correlation
base_model:
- castorini/afriberta_large
tags:
- sentiment-analysis
- sesotho
- southern-sotho
- low-resource-nlp
- african-nlp
- cross-orthography
- text-classification
---

# Sesotho Sentiment Analysis (AfriBERTa)

A fine-tuned sentiment classifier for Sesotho news headlines, built as part of the **Wale Lab R2I Fellowship (Cohort 3)**. Classifies text into **Positive**, **Negative**, or **Neutral**.

## 🚀 Try it live

An interactive browser-based demo (no setup required, runs entirely client-side) is available here:
👉 **[Sesotho Sentiment Analysis Space](https://huggingface.co/spaces/Xhenifer/sesotho-sentiment-afriberta)**

The demo runs this model directly in your browser via [Transformers.js](https://huggingface.co/docs/transformers.js) and WebAssembly — no server, no API calls, nothing sent off your device. It also includes an optional South African orthography converter, for testing cross-orthography generalization between Lesotho-standard and South African Sesotho spelling conventions.

## Model description

This model is a fine-tuned version of [`castorini/afriberta_large`](https://huggingface.co/castorini/afriberta_large), adapted for 3-class sentiment classification on Sesotho news headlines.

- **Base model:** castorini/afriberta_large
- **Task:** Text classification (sentiment)
- **Labels:** `NEGATIVE`, `NEUTRAL`, `POSITIVE`
- **Language:** Sesotho (st)

## Training data

Fine-tuned on a labeled dataset of 2,209 Sesotho news headlines. The source data is significantly imbalanced across classes:

| Label | Count | Proportion |
|---|---|---|
| Negative | 1,552 | 70.3% |
| Positive | 551 | 24.9% |
| Neutral | 106 | 4.8% |

To address this imbalance, training used a **class-weighted cross-entropy loss** (weights: Negative 1.0×, Neutral 6.0×, Positive 3.0×), which meaningfully improved the model's ability to recognize the minority Neutral class without a corresponding drop in Negative/Positive performance.

## Training procedure

- 3 epochs, learning rate 2e-5, batch size 8, warmup ratio 0.1
- 80/20 stratified train/validation split, seed 43
- Full training script and data preprocessing available on request

## Evaluation results

Evaluated on a held-out validation split (442 examples):

| Metric | Score |
|---|---|
| Macro F1 | 0.661 |
| Matthews Correlation Coefficient | 0.440 |
| Neutral-class F1 | 0.605 |
| Neutral-class recall | 0.619 |

## Limitations

- The Neutral class remains the hardest to classify reliably, given only 106 examples in the source dataset — class weighting helps but cannot fully substitute for more labeled data.
- The model was trained primarily on standard-case text; performance may vary on ALL CAPS or heavily stylized input.
- As with any sentiment classifier trained on news headlines, performance on informal or conversational Sesotho text (social media, spoken transcription, etc.) has not been evaluated and may differ.

## Usage

```python
from transformers import pipeline

clf = pipeline("text-classification", model="Xhenifer/sesotho-sentiment-afriberta", top_k=None)
clf("TONAKHOLO O FETOLA NAHA KA BEKE")
```

For browser-based / client-side usage via Transformers.js, see the [demo Space](https://huggingface.co/spaces/Xhenifer/sesotho-sentiment-afriberta) or its source for a working implementation.

## Citation


 Xhenifer. (2026). *Sesotho Sentiment Analysis (AfriBERTa)*. Wale Lab R2I Fellowship, Cohort 3. Hugging Face. https://huggingface.co/Xhenifer/sesotho-sentiment-afriberta

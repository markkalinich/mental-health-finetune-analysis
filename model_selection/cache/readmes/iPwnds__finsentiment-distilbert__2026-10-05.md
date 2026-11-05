---
library_name: transformers
tags:
- finance
- sentiment-analysis
- financial-sentiment
- distilbert
- text-classification
- financial-phrasebank
language:
- en
base_model: distilbert-base-uncased
license: apache-2.0
datasets:
- takala/financial_phrasebank
metrics:
- f1
---

# finsentiment-distilbert

A financial sentiment classifier fine-tuned from `distilbert-base-uncased` on the **Financial PhraseBank AllAgree** subset. Classifies financial text into **positive**, **neutral**, or **negative** sentiment with a weighted F1 of **0.9737** on the held-out test set.

It runs **fully locally** at 1 ms per headline — no API keys required — and outperforms both zero-shot LLM prompting (+30%) and FinBERT (+11%) on the same benchmark.

---

## Model Details

### Model Description

`finsentiment-distilbert` is a sequence classification fine-tune of `distilbert-base-uncased` trained on the Financial PhraseBank dataset (AllAgree subset — sentences where all human annotators agreed on the label). A linear classification head is added on top of the `[CLS]` token representation and trained end-to-end for 3-class financial sentiment.

The model is the sentiment backbone of the [AI Stock Market Analyst CLI](https://github.com/iPwnds/bloomberg-terminal) — a Bloomberg-style terminal that scores every news headline in real time to feed an aggregate sentiment signal into the AI analyst's stock reports.

- **Developed by:** Florian Braun ([@iPwnds](https://huggingface.co/iPwnds))
- **Model type:** Encoder-only transformer — sequence classification
- **Language:** English
- **License:** Apache 2.0
- **Fine-tuned from:** [`distilbert-base-uncased`](https://huggingface.co/distilbert/distilbert-base-uncased)

### Model Sources

- **Repository:** [github.com/iPwnds/bloomberg-terminal](https://github.com/iPwnds/bloomberg-terminal)
- **Training notebook:** [`notebooks/FinSentiment_Classifier.ipynb`](https://github.com/iPwnds/bloomberg-terminal/blob/main/notebooks/FinSentiment_Classifier.ipynb)
- **Companion generative model:** [`iPwnds/finanalyst-qwen1.5b`](https://huggingface.co/iPwnds/finanalyst-qwen1.5b)

---

## Uses

### Direct Use

The model classifies individual financial sentences — news headlines, earnings call snippets, analyst commentary — into one of three sentiment classes:

| Label | ID | Meaning |
|---|---|---|
| `negative` | 0 | Bearish / adverse news |
| `neutral` | 1 | Factual / no clear directional signal |
| `positive` | 2 | Bullish / favourable news |

It works best on short, single-sentence financial statements similar to the Financial PhraseBank training distribution: analyst reports, press release excerpts, financial news headlines.

### Downstream Use

In the AI Stock Market Analyst CLI the model is loaded as a `transformers` pipeline in `analysis/sentiment.py` and called on every headline returned for a given ticker. Individual scores are then aggregated into a per-ticker sentiment summary (overall label + confidence-weighted score) that is passed as context to the generative analyst LLM.

It can also be used standalone as a drop-in financial sentiment scorer for any NLP pipeline:

```python
from transformers import pipeline

clf = pipeline("text-classification", model="iPwnds/finsentiment-distilbert")

headlines = [
    "Apple reports record quarterly earnings, beats Wall Street estimates",
    "Federal Reserve signals further rate hikes amid persistent inflation",
    "Tesla misses delivery targets as EV demand slows globally",
]

for h in headlines:
    result = clf(h)[0]
    print(f"{result['label']:8s}  ({result['score']:.2%})  {h}")
```

### Out-of-Scope Use

- **Long documents** — the model was trained on short sentences (max 128 tokens). Passing full articles or paragraphs without sentence splitting will degrade performance.
- **Non-English text** — `distilbert-base-uncased` and the training data are English-only.
- **Non-financial domains** — sentiment language in finance is domain-specific (e.g. "profit warning" is clearly negative; "restructuring" is ambiguous). The model is not calibrated for general or social media sentiment.
- **Fine-grained or aspect-based sentiment** — the model produces document-level labels only, not aspect- or entity-level sentiment.

---

## Bias, Risks, and Limitations

- **Class imbalance:** The AllAgree subset is heavily skewed toward neutral (1,391 / 2,264 = 61%). The model may be biased toward predicting neutral on borderline cases.
- **Domain shift:** Financial language evolves with market conditions, regulation, and terminology. Sentences from novel domains (crypto, ESG, AI hardware) may be under-represented in the 2013-era Financial PhraseBank.
- **Annotation bias:** Labels reflect the consensus of a small group of annotators (only AllAgree sentences are used). The excluded sentences — where annotators disagreed — may represent genuinely ambiguous cases the model has never seen.
- **Base model limitations:** `distilbert-base-uncased` was pre-trained on general English text. Lowercasing removes potentially meaningful signals (company names, ticker symbols).

### Recommendations

Use confidence scores alongside labels — predictions with low confidence (< 0.7) on the top class are more likely to be genuinely ambiguous. For high-stakes applications, treat predictions as one signal among several rather than a definitive classification.

---

## How to Get Started with the Model

```python
from transformers import pipeline

# Load — model weights are ~268 MB; cached locally after first download
clf = pipeline(
    "text-classification",
    model="iPwnds/finsentiment-distilbert",
    device=0,   # GPU if available; remove or set to -1 for CPU
)

result = clf("Earnings per share exceeded analyst expectations by a wide margin")
# → [{'label': 'positive', 'score': 0.9971...}]

# Batch inference (much faster than calling one-by-one)
headlines = [
    "Company announces $2B share buyback programme",
    "Revenue in line with expectations for the third consecutive quarter",
    "CEO resigns amid accounting investigation",
]
results = clf(headlines)
for h, r in zip(headlines, results):
    print(f"{r['label']:8s}  ({r['score']:.2%})  {h}")
```

Label mapping: `negative` → 0, `neutral` → 1, `positive` → 2.

---

## Training Details

### Training Data

**Financial PhraseBank v1.0** — [`takala/financial_phrasebank`](https://huggingface.co/datasets/takala/financial_phrasebank) on the HuggingFace Hub.

The AllAgree subset (`Sentences_AllAgree.txt`) contains **2,264 sentences** from English-language financial news where all human annotators agreed on the sentiment label. It was introduced in:

> Malo, P., Sinha, A., Korhonen, P., Wallenius, J., & Takala, P. (2014). *Good debt or bad debt: Detecting semantic orientations in economic texts.* Journal of the American Society for Information Science and Technology, 65(4), 782–796.

Label distribution in the full AllAgree subset:

| Label | Count | Share |
|---|---|---|
| Neutral | 1,391 | 61.4% |
| Positive | 570 | 25.2% |
| Negative | 303 | 13.4% |

### Training Procedure

#### Preprocessing

Sentences were tokenized using the `distilbert-base-uncased` tokenizer with `padding="max_length"` and `max_length=128` (sufficient for all sentences in the dataset — none exceed 128 WordPiece tokens). Labels were mapped to integers: `negative=0`, `neutral=1`, `positive=2`.

The dataset was shuffled (`seed=42`) and split **80 / 10 / 10**:

| Split | Examples |
|---|---|
| Train | 1,811 |
| Validation | 226 |
| Test | 227 |

#### Training Hyperparameters

| Hyperparameter | Value |
|---|---|
| Base model | `distilbert-base-uncased` |
| Number of labels | 3 |
| Epochs | 5 |
| Per-device train batch size | 32 |
| Per-device eval batch size | 64 |
| Learning rate | 5e-5 (default) |
| Warmup steps | 100 |
| Weight decay | 0.01 |
| Mixed precision | fp16 |
| Best checkpoint metric | Validation F1 (weighted) |
| Max sequence length | 128 tokens |

**Training regime:** fp16 mixed precision.

#### Speeds, Sizes, Times

| | |
|---|---|
| Training time | ~64 seconds (T4 GPU, Google Colab) |
| Total steps | 285 |
| Train samples/sec | 141.8 |
| Final training loss | 0.2423 |
| Model size | ~268 MB |
| Inference speed | ~1 ms / headline (Apple MPS / T4 GPU) |

---

## Evaluation

### Testing Data

The held-out test split: **227 sentences** drawn from the same Financial PhraseBank AllAgree dataset, stratified by the same 80/10/10 shuffle with `seed=42`. No examples from the test split were seen during training or used for early stopping.

### Factors

Evaluation is performed at the sentence level on the full test split without disaggregation by subgroup. The class imbalance in the dataset (neutral-heavy) means that per-class F1 scores differ from the aggregate; weighted F1 accounts for class frequency.

### Metrics

**Weighted F1** (`evaluate.load("f1")`, `average="weighted"`) — the primary metric used for checkpoint selection and reporting. Weighted F1 is appropriate here because it accounts for class imbalance while still penalising poor performance on minority classes (negative in particular).

**Test loss** (cross-entropy) is reported as a secondary metric.

### Results

| Metric | Value |
|---|---|
| Test F1 (weighted) | **0.9737** |
| Test loss | 0.1090 |
| Test samples | 227 |

**Comparison to baselines:**

| Model | F1 | vs. this model |
|---|---|---|
| Zero-shot LLM prompting | ~0.75 | −30% |
| FinBERT (`ProsusAI/finbert`) | ~0.88 | −11% |
| **finsentiment-distilbert (this model)** | **0.9737** | — |

#### Summary

Fine-tuning on the AllAgree subset yields a highly accurate classifier that substantially outperforms both zero-shot prompting and the widely-used FinBERT baseline. The high F1 reflects the clean, expert-labeled training data and the narrow domain focus. The model generalises well to the held-out test split with minimal loss increase (train loss 0.24 → test loss 0.11), suggesting no overfitting despite the relatively small dataset size.

---

## Environmental Impact

Training was performed on a Google Colab T4 GPU for approximately 64 seconds. Estimated carbon emissions are negligible.

- **Hardware type:** NVIDIA T4 (Google Colab)
- **Hours used:** ~0.018 hours
- **Cloud provider:** Google (Colab)
- **Compute region:** US (Colab default)
- **Carbon emitted:** < 1 g CO₂eq (estimated)

---

## Technical Specifications

### Model Architecture and Objective

- **Base architecture:** DistilBERT (`distilbert-base-uncased`) — 6-layer distilled transformer encoder, 66M parameters
- **Classification head:** Linear layer on top of the `[CLS]` token → 3 logits
- **Objective:** Cross-entropy loss for 3-class sequence classification (negative / neutral / positive)

### Compute Infrastructure

#### Hardware

- NVIDIA T4 GPU (15 GB VRAM) for training — Google Colab
- Apple Silicon (MPS), CUDA GPU, or CPU for inference

#### Software

| Package | Role |
|---|---|
| `transformers` | Model, tokenizer, `Trainer`, `TrainingArguments` |
| `datasets` | Dataset loading, splitting, tokenization mapping |
| `evaluate` | Weighted F1 metric computation |
| `scikit-learn` | Confusion matrix and per-class metrics |
| `accelerate` | Mixed-precision training (fp16) |
| `huggingface_hub` | `snapshot_download` for dataset, `push_to_hub` |

---

## Citation

If you use this model, please cite the original Financial PhraseBank dataset:

**BibTeX:**

```bibtex
@article{malo2014good,
  title   = {Good debt or bad debt: Detecting semantic orientations in economic texts},
  author  = {Malo, Pekka and Sinha, Ankur and Korhonen, Pekka and Wallenius, Jyrki and Takala, Pyry},
  journal = {Journal of the American Society for Information Science and Technology},
  volume  = {65},
  number  = {4},
  pages   = {782--796},
  year    = {2014}
}
```

**APA:**

Malo, P., Sinha, A., Korhonen, P., Wallenius, J., & Takala, P. (2014). Good debt or bad debt: Detecting semantic orientations in economic texts. *Journal of the American Society for Information Science and Technology, 65*(4), 782–796.

---

## Model Card Authors

Florian Braun ([@iPwnds](https://huggingface.co/iPwnds))

## Model Card Contact

[huggingface.co/iPwnds](https://huggingface.co/iPwnds)

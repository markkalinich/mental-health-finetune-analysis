---
language:
  - sd
tags:
  - sentiment-analysis
  - xlm-roberta
  - sindhi
  - text-classification
  - fine-tuned
license: mit
datasets:
  - DanishMahdi/snd_movies_sentiment_analysis
model-index:
  - name: snd_sentiment_analysis
    results:
      - task:
          type: text-classification
          name: Sentiment Analysis
        dataset:
          name: snd_movies_sentiment_analysis
          type: DanishMahdi/snd_movies_sentiment_analysis
        metrics:
          - type: accuracy
            value: see evaluation/test_metrics.json
          - type: f1
            value: see evaluation/test_metrics.json
---

# 🎬 Sindhi Movie Sentiment Analysis

Fine-tuned **XLM-RoBERTa-base** model for **binary sentiment classification** on Sindhi movie reviews.

---

## 📋 Model Details

| Field | Details |
|---|---|
| **Base model** | `xlm-roberta-base` |
| **Task** | Binary Sentiment Classification |
| **Language** | Sindhi (sd) — Perso-Arabic / Nastaliq script |
| **Labels** | `positive` · `negative` |
| **Dataset** | `DanishMahdi/snd_movies_sentiment_analysis` |
| **Training rows** | ~40,000 (20k positive, 20k negative) |
| **Max token length** | 128 |

---

## 📊 Training Configuration

| Hyperparameter | Value |
|---|---|
| Learning rate | `2e-5` |
| Batch size | `16` |
| Epochs | `5` (early stopping patience = 2) |
| Warmup ratio | `0.1` |
| LR scheduler | `cosine` |
| Weight decay | `0.01` |
| Optimizer | `AdamW` |
| Precision | `fp16` (if CUDA available) |

---

## 🚀 Quick Start

### Install dependencies
```bash
pip install transformers torch
```

### Run inference
```python
from transformers import pipeline

pipe = pipeline(
    "text-classification",
    model="DanishMahdi/snd_sentiment_analysis",
)

reviews = [
    "هي فلم بلڪل خراب هئي، مون کي پسند نه آئي",   # negative
    "هي فلم تمام سٺي هئي، مون کي تمام گهڻو پسند آئي",  # positive
]

for review in reviews:
    result = pipe(review)[0]
    print(f"Label: {result['label']} | Score: {result['score']:.4f}")
```

### Output
```
Label: NEGATIVE | Score: 0.9873
Label: POSITIVE | Score: 0.9912
```

---

## 📁 Repository Structure

```
DanishMahdi/snd_sentiment_analysis/
├── config.json                    # Model config
├── model.safetensors              # Fine-tuned weights
├── tokenizer_config.json          # Tokenizer config
├── sentencepiece.bpe.model        # SentencePiece vocab
├── evaluation/
│   ├── test_metrics.json          # Accuracy, F1, Precision, Recall
│   ├── confusion_matrix.json      # Raw confusion matrix
│   ├── confusion_matrix.png       # Confusion matrix plot
│   ├── training_curves.png        # Loss & F1 over epochs
│   ├── test_metrics_bar.png       # Bar chart of metrics
│   └── classification_report.txt  # Full sklearn report
└── README.md
```

---

## 📈 Evaluation Results

See `evaluation/test_metrics.json` for the latest numbers.
Plots are available in the `evaluation/` folder.

| Metric | Score |
|---|---|
| Accuracy | 0.8825 |
| F1 (weighted) | 0.8825 |
| Precision (weighted) | 0.8828 |
| Recall (weighted) | 0.8825 |

---

## 🔗 Dataset

The training data is sourced from  
[`DanishMahdi/snd_movies_sentiment_analysis`](https://huggingface.co/datasets/DanishMahdi/snd_movies_sentiment_analysis)

- **Total rows:** ~40,000  
- **Positive reviews:** ~20,000  
- **Negative reviews:** ~20,000  
- **Split:** 80% train / 10% validation / 10% test  

---

## 📝 Citation

```bibtex
@misc{danish2025snd,
  author    = {Danish Mahdi},
  title     = {Sindhi Movie Sentiment Analysis using XLM-RoBERTa},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/DanishMahdi/snd_sentiment_analysis},
}
```

---

## ⚖️ License

MIT — free to use for research and commercial purposes.

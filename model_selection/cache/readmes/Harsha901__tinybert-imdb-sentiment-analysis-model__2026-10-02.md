---
license: mit
language:
- en
base_model:
- huawei-noah/TinyBERT_General_4L_312D
pipeline_tag: text-classification
tags:
- sentiment-analysis
- tinybert
- transformers
- text-classification
- imdb

---

#

# 📦 TinyBERT IMDB Sentiment Analysis Model

This is a fine-tuned [TinyBERT](https://huggingface.co/huawei-noah/TinyBERT_General_4L_312D) model for binary **sentiment classification** on a 5,000-sample subset of the [IMDB dataset](https://huggingface.co/datasets/imdb).
It predicts whether a movie review is **positive** or **negative**.

## 🧠 Model Details

- **Base model:** [`huawei-noah/TinyBERT_General_4L_312D`](https://huggingface.co/huawei-noah/TinyBERT_General_4L_312D)
- **Task:** Sentiment Classification (Binary)
- **Dataset:** 4,000 training + 1,000 test samples from IMDB
- **Tokenizer:** `AutoTokenizer.from_pretrained('huawei-noah/TinyBERT_General_4L_312D')`
- **Max length:** 300 tokens
- **Batch size:** 64
- **Training framework:** Hugging Face `Trainer`
- **Device:** A100 GPU

## 📊 Evaluation Metrics
## 📊 Evaluation Metrics (on 1,000-sample test set)

| Metric | Value |
|-----------------------|----------|
| Accuracy | **88.02%** |
| Evaluation Loss | 0.2962 |
| Runtime | 30.9 sec |
| Samples per Second | 485 |


## 🚀 How to Use

```python
from transformers import pipeline

classifier = pipeline(
"text-classification",
model="Harsha901/tinybert-imdb-sentiment-analysis-model"
)

result = classifier("This movie was absolutely amazing!")
print(result) # [{'label': 'LABEL_1', 'score': 0.98}]
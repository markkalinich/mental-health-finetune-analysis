---
language: 
- en
license: mit
datasets:
- custom
library_name: transformers
tags:
- finance
- india
- sentiment-analysis
- finbert
- stock-market
pipeline_tag: text-classification
model-index:
- name: FinBERT-India-v1
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.77
    - name: F1
      type: f1
      value: 0.76
---


## 🧾 **Model Card — FinBERT-India-v1**

### 🧠 Model Overview

**FinBERT-India-v1** is a fine-tuned financial sentiment analysis model trained specifically for **Indian financial news and stock market headlines**.
further adapted to understand **India-specific financial context, market language, and sentiment nuances.**

Trained on a curated dataset of **India-focused financial articles**, this model effectively captures **regional market language, economic tone**, and **sentiment patterns**, classifying each headline as **positive**, **neutral**, or **negative**.

It is designed to assist in **financial analytics**, **market forecasting**, and **investment decision-making** by providing precise **sentiment insights** tailored to the **Indian financial landscape**.

---

### 🏗️ Training Details

* **Base Model:** `yiyanghkust/finbert-tone`
* **Framework:** Hugging Face Transformers
* **Training Hardware:** Google Colab GPU (T4)
* **Epochs:** 8 (early-stopped at best validation performance)
* **Batch Size:** 8 (train), 16 (eval)
* **Learning Rate:** 3e-5
* **Optimizer:** AdamW
* **Dataset Size:** 7,451 labeled financial news samples
* **Label Classes:**

  * 🟢 Positive
  * ⚪ Neutral
  * 🔴 Negative

---

### 📊 Dataset Description

The dataset was **LLM-labeled** using an advanced **large language model-based annotation pipeline**, inspired by **FinBERT’s financial sentiment framework** and refined through **manual quality validation**.
It consists of **Indian financial news headlines** collected from various stock market sources and business outlets.

| Label    | Count | Percentage                                  |
| -------- | ----- | ------------------------------------------- |
| Positive | ~45%  | Market gains, optimism, positive earnings   |
| Neutral  | ~33%  | Factual statements, mixed signals           |
| Negative | ~20%  | Market declines, losses, or risk sentiments |

---

### 🎯 Evaluation Metrics

| Metric        | Score |
| ------------- | ----: |
| **Eval Loss** |  0.54 |
| **Accuracy**  | 76.8% |
| **Precision** | 76.7% |
| **Recall**    | 76.8% |
| **F1 Score**  | 76.4% |

✅ The model generalizes well with balanced precision and recall, and shows strong performance despite diverse phrasing and tone in Indian market headlines.

---

### 💬 Example Usage

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="Vansh180/FinBERT-India-v1")

texts = [
    "Sensex surges 500 points as IT and banking stocks rally.",
    "Rupee falls sharply against the dollar amid global uncertainty.",
    "TCS announces leadership reshuffle; markets await further clarity.",
]

for t in texts:
    print(pipe(t))
```

**Output:**

```
[{'label': 'positive', 'score': 0.92},
 {'label': 'negative', 'score': 0.88},
 {'label': 'neutral', 'score': 0.73}]
```

---

### 🧩 Intended Use

* Sentiment analysis for **Indian stock market news**
* Financial report tone classification
* Feature extraction for **stock price forecasting models**
* Trend analysis in **algorithmic trading pipelines**

---

### ⚠️ Limitations

* The model is **optimized for Indian market news**; performance may vary on global news.
* LLM-based labeling introduces minor noise.
* Headlines containing sarcasm or ambiguous sentiment may be misclassified.

---

### 🧑‍💻 Developer

* **Author:** Vansh Momaya
* **Institution:** D. J. Sanghvi College of Engineering
* **Focus Area:** Financial AI, NLP, Data Science and Machine Learning for Indian Markets
* **Email:** *vanshmomaya9@gmail.com*

---

### 🌍 Citation

If you use **FinBERT-India-v1** in your research or project:

```
@online{momaya2025finbertindia,
  author       = {Vansh Momaya},
  title        = {FinBERT-India-v1: A Domain-Specific Sentiment Analysis Model for Indian Financial Markets},
  year         = {2025},
  version      = {v1},
  url          = {https://huggingface.co/Vansh180/FinBERT-India-v1},
  institution  = {D. J. Sanghvi College of Engineering},
  note         = {Fine-tuned model for analyzing Indian financial news and stock market sentiment},
  license      = {MIT}
}

```

---

### 🚀 Acknowledgements

* [FinBERT-tone](https://huggingface.co/yiyanghkust/finbert-tone) — Base model
* [Hugging Face Transformers](https://huggingface.co/transformers) — Training framework

---

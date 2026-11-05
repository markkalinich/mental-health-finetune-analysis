---
language:
- id
- eng
library_name: transformers
pipeline_tag: text-classification
tags:
- text-classification
- sentiment-analysis
- indonesian
- multilingual
- xlm-roberta
- social-media
license: apache-2.0
metrics:
- accuracy
- f1
base_model:
- FacebookAI/xlm-roberta-base
---

# Sentiment Analysis for Social Media Text  
**Multilingual Indonesian & English | XLM-RoBERTa**

This model is a fine-tuned **XLM-RoBERTa-Base** designed to analyze **Sentiment Positive, Neutral, Negative** content in social media text.  
It supports **Indonesian** and **English Languages**, making it suitable for multi-platform moderation use cases such as Twitter/X, Instagram, TikTok, Facebook, and online forums.

---

## ✨ Key Features

- ✅ Sentiment Posisitve, Neutral, and Negative classification  
- 🌏 Multilingual support (Indonesian & English)  
- 🧠 Based on **XLM-RoBERTa (multilingual transformer)**  
- ⚡ Ready-to-use with Hugging Face `pipeline`  
- 📊 Strong performance on noisy social media text  

---

## 🌍 Supported Languages

- 🇮🇩 Bahasa Indonesia  
- 🇬🇧 English  

---

## 🧪 Model Performance

| Metric              | Score  |
|---------------------|--------|
| Accuracy            | 0.8527 |
| F1 (Macro)          | 0.8525 |
| F1 (Weighted)       | 0.8525 |
| Precision           | 0.8500 |
| Recall              | 0.8500 |
| Training Loss       | 0.2759 |
| Validation Loss     | 0.4368 |

> Evaluated on held-out validation data with balanced sentiment distribution.

---

## 🚀 Quick Start

### Installation
```bash
pip install transformers torch
````

### Single Prediction

```python
from transformers import pipeline

classifier = pipeline(
    task="text-classification",
    model="nahiar/sentiment-analysis-v2"
)

result = classifier("PASTI DIJAMIN WDP 100%")
print(result)
```

**Output**

```python
[{'label': 'LABEL_1', 'score': 0.9876}]
```

### Label Mapping

```text
LABEL_0 → NEUTRAL
LABEL_1 → POSITIF
LABEL_2 → NEGATIVE
```

---

## 📦 Batch Inference Example

```python
"texts": [
        "साइबर हमले के बाद JLR का बड़ा बयान - जानें कंपनी ने क्या कहा | Tata Motors के शेयर पर दिखेगा असर?

#TataMotors #JLR #CyberAttack 

https://t.co/6WlGS77UUp",
        "Kita sudah Ready skrg ini bagi yang memerlukan jasa pemulihan akun &amp; Hapus All akun 

 Lacak lokasi / sadap wa / Hack Akun / Revengeporn - korban pemerasan vcs / terror

TIKTOK,GMAIL,TWITER,TELEGRAM,
FACEBOOK,INSTAGRAM 
#revengeporn #zonauangᅠᅠᅠ 
 ☎️ https://t.co/K0AbW08qnU https://t.co/4IpWNA7a0z",
        "💥Slot Gacor Hari ini Rute303
💥Jaminan Jackpot Maxwin malam ini

LINK SLOT GACOR HARI INI : https://t.co/QvxjCAnt8o

Tags:
Jumbo #timsekop Jumat gratis ongkir Like Crazy PSIM https://t.co/ukuRdlvgGA"
    ]

results = classifier(texts)

for text, result in zip(texts, results):
    print(f"{text} -> {result['label']} ({result['score']:.4f})")
```

---

## 🏗️ Training Configuration

| Parameter          | Value            |
| ------------------ | ---------------- |
| Base Model         | xlm-roberta-base |
| Training Samples   | 19,200           |
| Validation Samples | 4,800            |
| Epochs             | 3                |
| Learning Rate      | 1e-5             |
| Batch Size         | 16               |
| Training Date      | 2026-02-05       |

---

## 🎯 Intended Use Cases

* Social media Sentiment Analysis
* Comment & post filtering
* Content quality control

---

## ⚠️ Limitations

* Binary classification only (Positive, Negative, Neutral)
* Not optimized for non-social-media formal text
* Performance may degrade on very short or ambiguous messages
* The model still has the potential to be biased

---

## 📜 License

Released under the **Apache 2.0 License**.
Free for commercial and research use.

---

## 📚 Citation

If you use this model in your work, please cite:

```bibtex
@misc{djunaedi2026sentiment,
  author    = {AI/ML Engineer ADS Digital Partner},
  title     = {Sentiment Analysis for Social Media Text},
  year      = {2026},
  publisher = {Hugging Face},
  url       = {https://huggingface.co/nahiar/spam-detection-v2}
}
```

---

## 🙌 Acknowledgements

* Hugging Face Transformers
* Facebook AI Research — XLM-RoBERTa
---
license: cc-by-nc-nd-4.0
language:
- th
- af
- am
- ar
- as
- az
- be
- bg
- bn
- br
- bs
- ca
- cs
- cy
- da
- de
- el
- en
- eo
- es
- et
- eu
- fa
- fi
- fr
- fy
- ga
- gd
- gl
- gu
- ha
- he
- hi
- hr
- hu
- hy
- id
- is
- it
- ja
- jv
- ka
- kk
- km
- kn
- ko
- ku
- ky
- la
- lo
- lt
- lv
- mg
- mk
- ml
- mn
- mr
- ms
- my
- ne
- nl
- om
- or
- pa
- pl
- ps
- pt
- ro
- ru
- sa
- sd
- si
- sk
- sl
- so
- sq
- sr
- su
- sv
- sw
- ta
- te
- th
- tl
- tr
- ug
- uk
- ur
- uz
- vi
- xh
- yi
- zh
base_model: intfloat/multilingual-e5-large
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- thai
- multilingual
- fine-tuned
- transformers
- southeast-asian
metrics:
- accuracy
- f1
- precision
- recall
widget:
- text: ผลิตภัณฑ์นี้ดีมาก ใช้งานง่าย
  example_title: Thai Positive
- text: บริการแย่มาก ไม่ประทับใจเลย
  example_title: Thai Negative
- text: อาหารรสชาติธรรมดา
  example_title: Thai Neutral
- text: ราคาเท่าไหร่ครับ?
  example_title: Thai Question
---

# 🎯 MultiSent-E5-Pro: Advanced Thai Sentiment Classifier

<div align="center">
  <img src="https://cdn-uploads.huggingface.co/production/uploads/673eef9c4edfc6d3b58ba3aa/lQCMts9DEsjQf3Yd8wu4a.png" width="300" alt="MultiSent-E5-Pro Logo">

<strong>🇹🇭 State-of-the-art Thai sentiment analysis with multilingual capabilities</strong>

<a href="https://creativecommons.org/licenses/by-nc-nd/4.0/"><img src="https://img.shields.io/badge/License-CC_BY--NC--ND_4.0-lightgrey.svg"></a> <a href="https://huggingface.co/ZombitX64/MultiSent-E5-Pro"><img src="https://img.shields.io/badge/🤗%20HF-Model-yellow"></a> <a href="https://huggingface.co/ZombitX64/MultiSent-E5-Pro"><img src="https://img.shields.io/badge/Downloads-1K+-green"></a>

</div>

## 📋 Quick Overview

**MultiSent-E5-Pro** is a fine-tuned sentiment analysis model based on `intfloat/multilingual-e5-large`, specially optimized for Thai with support for multilingual contexts. The model classifies text into four categories: **Positive**, **Negative**, **Neutral**, and **Question**.

### 🎯 Key Features

* Handles **Thai-specific expressions**, **colloquialisms**, and **sarcasm** effectively
* Performs well on **real-world social media & review data**
* **Multilingual support** for Southeast and East Asian languages

---

## 🏆 Benchmark Summary

| Rank   | Model            | Accuracy   | F1-Macro   | Notes             |
| ------ | ---------------- | ---------- | ---------- | ----------------- |
| 🥇 1st | MultiSent-E5-Pro | **84.61%** | **84.61%** | Best overall      |
| 2nd    | MultiSent-E5     | 80.62%     | 80.62%     | Baseline model    |
| 3rd    | sentiment-103    | 57.40%     | 49.87%     | Moderate baseline |

---

## 📊 Detailed Metrics (2,183 samples)

| Metric                     | Score  |
| -------------------------- | ------ |
| Accuracy                   | 84.61% |
| F1-Macro                   | 84.61% |
| F1-Weighted                | 84.75% |
| Avg Confidence             | 98.53% |
| Low Confidence Rate (<60%) | 0.96%  |

### Per-Class Performance

| Class    | Precision | Recall | F1    | Notes     |
| -------- | --------- | ------ | ----- | --------- |
| Negative | 91.0%     | 84.6%  | 87.7% | Excellent |
| Positive | 83.0%     | 94.3%  | 88.3% | Excellent |
| Neutral  | 71.9%     | 81.6%  | 76.4% | Moderate  |
| Question | 94.4%     | 79.0%  | 86.0% | Good      |

---

## ⚡ Quick Start

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model = "ZombitX64/MultiSent-E5-Pro"
tokenizer = AutoTokenizer.from_pretrained(model)
model = AutoModelForSequenceClassification.from_pretrained(model)

text = "ผลิตภัณฑ์นี้ดีมาก ใช้งานง่าย"
inputs = tokenizer(text, return_tensors="pt", truncation=True)
with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted = torch.argmax(probs, dim=-1)

labels = ["Question", "Negative", "Neutral", "Positive"]
print(f"Sentiment: {labels[predicted.item()]} (Confidence: {probs[0][predicted].item():.2%})")
```

---

## 🌟 Use Cases

| Application        | Suitability  |
| ------------------ | ------------ |
| Product Reviews    | 🟢 Excellent |
| Social Media       | 🟢 Excellent |
| Customer Support   | 🟢 Excellent |
| Content Moderation | 🟡 Good      |
| Research Analysis  | 🟡 Good      |

---

## ⚠ Known Limitations

* **Sarcasm Misclassification** (especially in Chinese)
* **Mixed Sentiments** lean toward Neutral
* **Low recall** for **Question** class due to limited data
* **Bias toward Positive** due to class imbalance
* **Overconfidence** in some multilingual predictions

---

## 🛠 Technical Info

| Config        | Value                 |
| ------------- | --------------------- |
| Base Model    | multilingual-e5-large |
| Params        | \~1.02B               |
| Classes       | 4                     |
| Max Length    | 512                   |
| Training Time | \~27 min              |

**Data Summary**:

* Training: 2,456 samples
* Validation: 273 samples
* Evaluation: 2,183 samples

---

## 📄 Citation

```bibtex
@misc{MultiSent-E5-Pro-2024,
  title={MultiSent-E5-Pro: Advanced Thai Sentiment Analysis},
  author={ZombitX64, Janutsaha K., Saengwichain C.},
  year={2024},
  url={https://huggingface.co/ZombitX64/MultiSent-E5-Pro},
  note={Hugging Face Model Card}
}
```
```bibtex
@article{wang2024multilingual,
  title={Multilingual E5 Text Embeddings: A Technical Report},
  author={Wang, Liang and Yang, Nan and Huang, Xiaolong and Yang, Linjun and Majumder, Rangan and Wei, Furu},
  journal={arXiv preprint arXiv:2402.05672},
  year={2024}
}
```
---

## 👨‍💼 Authors

| Role           | Name                 |
| -------------- | -------------------- |
| Lead Dev       | ZombitX64            |
| Data Scientist | Krittanut Janutsaha  |
| Engineer       | Chanyut Saengwichain |

---

## 😊 Feedback & Contributions

* 💬 [Open Discussion](https://huggingface.co/ZombitX64/MultiSent-E5-Pro/discussions)
* 🐛 [Report Issue](https://huggingface.co/ZombitX64/MultiSent-E5-Pro/issues)
* 🌟 Star the repo if useful!

---
 
<div align="center">
Last Updated: Dec 2024 | Version: 1.1 | Docs: v2.0
</div>
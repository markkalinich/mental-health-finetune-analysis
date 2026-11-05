---
language: zh
license: apache-2.0
library_name: transformers
tags:
- text-classification
- sentiment-analysis
- chinese
- movie-review
datasets:
- utmhikari/doubanmovieshortcomments
base_model: hfl/chinese-roberta-wwm-ext
pipeline_tag: text-classification
---

**Chinese Movie Review Sentiment Classification Model (5-Star Rating)**

---

## 1. Model Overview  
`H-Z-Ning/Senti-RoBERTa-Mini` is a lightweight Chinese RoBERTa model fine-tuned specifically for assigning 1-to-5-star sentiment ratings to Chinese movie short reviews. Built on the HFL-Tencent `hfl/chinese-roberta-wwm-ext` checkpoint, it retains a small footprint and fast inference, making it ideal for resource-constrained deployments.

---

## 2. Model Facts  

| Item | Details |
|---|---|
| Task | Chinese text classification (sentiment / star rating) |
| Labels | 5 classes (1 star – 5 stars) |
| Base model | [hfl/chinese-roberta-wwm-ext](https://huggingface.co/hfl/chinese-roberta-wwm-ext) |
| Dataset | [Kaggle: Douban Movie Short Comments (2000 K)](https://www.kaggle.com/datasets/utmhikari/doubanmovieshortcomments) |
| Training framework | 🤗 transformers + Trainer |
| Language | Simplified Chinese |
| Parameters | ≈ 102 M (same as base model) |

---

## 3. Quick Start  

### 3.1 Install Dependencies
```bash
pip install transformers torch
```

### 3.2 One-Line Inference
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

repo = "H-Z-Ning/Senti-RoBERTa-Mini"
tok = AutoTokenizer.from_pretrained(repo)
model = AutoModelForSequenceClassification.from_pretrained(repo)

text = "这个导演真厉害。"
inputs = tok(text, return_tensors="pt", truncation=True, max_length=256)
with torch.no_grad():
    logits = model(**inputs).logits
pred = int(torch.argmax(logits, dim=-1).item()) + 1  # 1..5
print("predicted rating:", pred)
```

---
## 4.Training source code

**[senti-roberta-mini training source code](https://www.kaggle.com/code/hzning/senti-roberta-mini)**

## 5. Training Details  



| Hyper-parameter | Value |
|---|---|
| Base model | hfl/chinese-roberta-wwm-ext |
| Training framework | 🤗 transformers `Trainer` |
| Training set | 150 000 samples (randomly drawn from 2000 K) |
| Validation set | 15 000 samples (same random draw) |
| Test set | full original test set |
| Max sequence length | 256 |
| Training epochs | 3 |
| Batch size | 32 (train) / 64 (eval) |
| Learning rate | 2e-5 |
| Optimizer | AdamW |
| Weight decay | 0.01 |
| Scheduler | linear warmup (warmup_ratio=0.1) |
| Precision | FP16 |
| Best-model criterion | **QWK (↑)** |
| Training time | ≈ 120 min on single P100 (FP16) |
| Logging interval | every 10 steps |

---

## 6. Citation  

```bibtex
@misc{senti-roberta-mini-2025,
  title={Senti-RoBERTa-Mini: A Mini Chinese RoBERTa for Movie Review Rating},
  author={H-Z-Ning},
  year={2025},
  howpublished={\url{https://huggingface.co/H-Z-Ning/Senti-RoBERTa-Mini}}
}
```

---

## 7. License  
This model is released under [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0). The base model `hfl/chinese-roberta-wwm-ext` is also Apache-2.0.

---

Community contributions and feedback are welcome! If you encounter any issues, please open an [Issue](https://huggingface.co/H-Z-Ning/Senti-RoBERTa-Mini/discussions) or email the author.
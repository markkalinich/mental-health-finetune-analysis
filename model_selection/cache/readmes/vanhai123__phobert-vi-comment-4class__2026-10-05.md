---
language: vi
tags:
  - vietnamese
  - text-classification
  - sentiment-analysis
  - PhoBERT
  - transformers
license: mit
datasets:
  - vanhai123/vietnamese-social-comments
metrics:
  - accuracy
  - f1
model-index:
  - name: PhoBERT Vietnamese Comment Classifier (4-class)
    results:
      - task:
          type: text-classification
          name: Text Classification
        dataset:
          name: Vietnamese Social Comments
          type: vanhai123/vietnamese-social-comments
        metrics:
          - type: accuracy
            value: 0.86
          - type: f1
            name: f1_macro
            value: 0.83
---


# 📄 PhoBERT Vietnamese Comment Classifier (4-class)

Đây là mô hình phân loại bình luận tiếng Việt thành 4 nhãn cảm xúc sử dụng `vinai/phobert-base`.

## 🍿️ Các nhãn phân loại

* `positive` – tích cực
* `negative` – tiêu cực
* `neutral` – trung lập
* `toxic` – kích động, phản cảm

## 🧠 Mô hình nền

* **Base model**: [`vinai/phobert-base`](https://huggingface.co/vinai/phobert-base)
* **Fine-tuned** trên dataset `vanhai123/vietnamese-social-comments` gồm 4,896 bình luận từ TikTok, Facebook, YouTube.

## 🧪 Kết quả đánh giá

* Accuracy: **86%**
* Macro F1-score: **83%**

## 💻 Sử dụng

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="vanhai123/phobert-vi-comment-4class")
classifier("Video này thật sự rất bổ ích và thú vị!")
```

## 📾 Dataset

* [Vietnamese Social Comments dataset](https://huggingface.co/datasets/vanhai123/vietnamese-social-comments)

## 👤 Tác giả

* Hà Văn Hải – [vanhai11203@gmail.com](mailto:vanhai11203@gmail.com)
* Hugging Face: [vanhai123](https://huggingface.co/vanhai123)

##

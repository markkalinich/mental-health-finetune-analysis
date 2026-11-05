---
language:
- vi
license: mit
pipeline_tag: text-classification
tags:
- phobert
- emotion-recognition
- vietnamese-nlp
- social-media
- onnx
- onnxruntime
- optimum
metrics:
- accuracy
- f1
model-index:
- name: phobert-emotion-social
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: Vietnamese Social Media Emotion Dataset
      type: custom
    metrics:
    - type: accuracy
      value: 0.6377
    - type: f1
      value: 0.6356
---

# 🎭 PhoBERT Fine-Tuned for Vietnamese Social Media Emotion Recognition

Mô hình **PhoBERT-base** được Fine-Tune chuyên biệt cho bài toán nhận diện **7 lớp Cảm xúc tiếng Việt** trên dữ liệu Mạng xã hội (Bình luận Facebook, Threads, VNExpress, Teencode/Slang).

Mô hình thuộc hệ thống Microservices dự án **SE121 - Social Media with Mental Health Awareness**.

---

## 📊 7 Lớp Cảm xúc (Emotion Classes)

| ID | Nhãn Cảm Xúc (English) | Tên Tiếng Việt | Icon |
|:---:|:---:|:---:|:---:|
| 0 | **Enjoyment** | Vui vẻ / Yêu thích | 😊 |
| 1 | **Sadness** | Buồn rầu / Thất vọng | 😭 |
| 2 | **Disgust** | Chán ghét / Khinh bỉ | 🤮 |
| 3 | **Anger** | Tức giận / Bực mình | 😡 |
| 4 | **Fear** | Sợ hãi / Lo lắng | 😱 |
| 5 | **Surprise** | Ngạc nhiên / Bất ngờ | 😲 |
| 6 | **Other** | Khác / Trung tính | 😐 |

---

## 📈 Kết quả Đánh giá Thực tế (Version 1.1 Final - Test Set: 1,482 samples)

| Emotion Label | Precision | Recall | F1-Score | Support |
|:---|:---:|:---:|:---:|:---:|
| **Enjoyment** | 0.7962 | 0.7017 | **0.7459** | 295 |
| **Sadness** | 0.5887 | 0.6791 | **0.6307** | 215 |
| **Disgust** | 0.5924 | 0.5203 | **0.5540** | 271 |
| **Anger** | 0.7351 | 0.7083 | **0.7215** | 192 |
| **Fear** | 0.6450 | 0.6301 | **0.6374** | 173 |
| **Surprise** | 0.5897 | 0.6434 | **0.6154** | 143 |
| **Other** | 0.5044 | 0.5907 | **0.5442** | 193 |
| **Overall Accuracy** | - | - | **63.77%** | 1482 |
| **Macro Average** | 0.6359 | 0.6391 | **63.56%** | 1482 |
| **Weighted Average** | 0.6453 | 0.6377 | **63.94%** | 1482 |

---

## 🚀 Hướng dẫn Sử dụng (Quick Start)

### 1. Sử dụng Transformers Pipeline

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="huyleit/phobert-emotion-social",
    tokenizer="huyleit/phobert-emotion-social",
    top_k=None
)

text = "Bài viết hay quá, đọc mà thấy thích ghê ❤️"
results = classifier(text)
print(results)
# Output: [{'label': 'Enjoyment', 'score': 0.96...}, ...]
```

### 2. Sử dụng AutoModel & AutoTokenizer (PyTorch)

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_name = "huyleit/phobert-emotion-social"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "Làm có 25-30tr mà cứ tưởng cả tỷ/tháng ko, đòi hỏi vcl ra."
inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)

id2label = model.config.id2label
for idx, prob in enumerate(probs[0].tolist()):
    print(f"{id2label[str(idx)]}: {prob:.4f}")
```

---

## ⚡ Fast Inference với ONNX Runtime (Tối ưu Production & CPU)

Repo cung cấp 2 phiên bản ONNX trong thư mục `onnx/`:
* `onnx/phobert_emotion_fp32.onnx`: Bản chuẩn FP32 (~540MB)
* `onnx/phobert_emotion_int8.onnx`: Bản Quantized INT8 (~135MB, giảm **75%** dung lượng, tăng tốc độ inference CPU **2-3x**)

### Cài đặt thư viện:
```bash
pip install onnxruntime transformers huggingface_hub numpy
```

### Code chạy Inference ONNX:

```python
from huggingface_hub import hf_hub_download
import onnxruntime as ort
from transformers import AutoTokenizer
import numpy as np

repo_id = "huyleit/phobert-emotion-social"

# 1. Tải tokenizer & ONNX model từ Hugging Face Hub
tokenizer = AutoTokenizer.from_pretrained(repo_id)
onnx_path = hf_hub_download(
    repo_id=repo_id,
    filename="phobert_emotion_int8.onnx", # hoặc "phobert_emotion_fp32.onnx"
    subfolder="onnx"
)

# 2. Khởi tạo ONNX Runtime Session
session = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])

# 3. Chuẩn bị input text
text = "Hôm nay nhận được học bổng vui quá cả nhà ơi 🎉"
inputs = tokenizer(text, return_tensors="np", padding=True, truncation=True, max_length=256)

ort_inputs = {
    "input_ids": inputs["input_ids"].astype(np.int64),
    "attention_mask": inputs["attention_mask"].astype(np.int64)
}

# 4. Chạy mô hình
logits = session.run(None, ort_inputs)[0]
# Softmax
exp_logits = np.exp(logits - np.max(logits, axis=1, keepdims=True))
probs = exp_logits / np.sum(exp_logits, axis=1, keepdims=True)

predicted_id = np.argmax(probs, axis=1)[0]
id2label = {
    0: "Enjoyment 😊",
    1: "Sadness 😭",
    2: "Disgust 🤮",
    3: "Anger 😡",
    4: "Fear 😱",
    5: "Surprise 😲",
    6: "Other 😐"
}

print(f"Cảm xúc dự đoán: {id2label[predicted_id]}")
print(f"Độ tin cậy: {probs[0][predicted_id] * 100:.2f}%")
```

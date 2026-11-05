---
language:
- vi
license: mit
library_name: transformers
tags:
- text-classification
- text-moderation
- phobert
- vietnamese
- hate-speech
- depression
- mental-health
- onnx
- onnxruntime
- optimum
metrics:
- f1
- accuracy
- precision
- recall
model-index:
- name: huyleit/phobert-vi-moderation-v1.1
  results:
  - task:
      type: text-classification
      name: Multi-Label Contextual Text Moderation
    dataset:
      type: json
      name: Merged ViHSD + Playwright English Self-Harm Dataset (v1.1)
    metrics:
    - type: f1
      value: 78.16
      name: Test Macro F1
    - type: accuracy
      value: 81.36
      name: Test Accuracy
---

# PhoBERT Multi-Label Contextual Text Moderation (v1.1)

Mô hình **`huyleit/phobert-vi-moderation-v1.1`** là mô hình fine-tuned dựa trên kiến trúc **`vinai/phobert-base-v2`** chuyên biệt cho bài toán **Phân loại ngữ cảnh Kiểm duyệt nội dung (Contextual Text Moderation)** trên các nền tảng Mạng xã hội tiếng Việt tích hợp hỗ trợ Sức khỏe tinh thần (Mental Health Awareness).

---

## 🏷️ Ma Trận Taxonomy 4 Nhãn AI Ngữ Cảnh

| Label ID | Tên Nhãn (Label Name) | Định Nghĩa Nghiệp Vụ | Hành Vi Hệ Thống (Action) |
| :---: | :--- | :--- | :--- |
| **`0`** | **`CLEAN`** | Nội dung bình thường, an toàn, tích cực. | **`ALLOW`** (Cho phép đăng công khai) |
| **`1`** | **`PROFANITY_VENTING`** | Bộc phát xả stress cá nhân, từ chửi thề nhẹ không công kích ai. | **`ALLOW_WITH_WARNING`** (Cho phép đăng nhưng gắn cảnh báo) |
| **`2`** | **`HATE_SPEECH`** | Ngôn từ thù ghét, miệt thị, công kích cá nhân/tập thể thô bạo. | **`HARD_BLOCK / SOFT_HIDE`** (Chặn hoặc ẩn bài) |
| **`3`** | **`EMOTIONAL_CRISIS`** | Khủng hoảng cảm xúc, suy sụp tinh thần, trầm cảm nặng hoặc ý định tự hại. | **`ALLOW_WITH_SUPPORT`** (Cho phép đăng + Gắn Popup hỗ trợ tâm lý) |

*(Lưu ý: Nhãn `4: ILLEGAL_PORN` đồi trụy / vi phạm pháp luật được xử lý cấm cứng tại Lớp 1 Regex/Rules Engine ở API Gateway với độ trễ $< 1\text{ms}$)*.

---

## 📊 Kết Quả Đánh Giá Trên Tập Test Độc Lập (2,441 Mẫu - Stratified 70/15/15)

Mô hình được đánh giá trên tập **Test độc lập 2,441 mẫu** (không bị rò rỉ từ tập Train/Val):

```text
=================== TEST SET CLASSIFICATION REPORT (v1.1) ===================

                      precision    recall  f1-score   support

            0: CLEAN     0.8436    0.8808    0.8618      1200
1: PROFANITY_VENTING     0.6250    0.4867    0.5473       339
      2: HATE_SPEECH     0.7218    0.7533    0.7372       527
 3: EMOTIONAL_CRISIS     0.9813    0.9787    0.9800       375

            accuracy                         0.8136      2441
           macro avg     0.7929    0.7749    0.7816      2441
        weighted avg     0.8081    0.8136    0.8094      2441
```

* **Test Accuracy**: **`81.36%`**
* **Test Macro F1-Score**: **`78.16%`** (Cải tiến vượt trội so với mốc $66.30\%$ của bài báo gốc ViHSD baseline).
* **F1-Score Nhãn `EMOTIONAL_CRISIS`**: **`98.00%`** (Precision 98.13% / Recall 97.87%).

---

## 💻 Hướng Dẫn Sử Dụng Trong Python (Quickstart)

```python
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load model & tokenizer từ Hugging Face Hub
model_name = "huyleit/phobert-vi-moderation-v1.1"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Taxonomy mapping
labels_map = {
    0: "CLEAN",
    1: "PROFANITY_VENTING",
    2: "HATE_SPEECH",
    3: "EMOTIONAL_CRISIS"
}

# Câu test thử nghiệm
text = "Tôi cảm thấy mệt mỏi và bế tắc quá, không biết phải sống tiếp thế nào..."

inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=128)
with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.nn.functional.softmax(outputs.logits, dim=-1)
    predicted_label_id = torch.argmax(probs, dim=-1).item()

print(f"Nhãn dự đoán: {labels_map[predicted_label_id]}")
print(f"Độ tin cậy: {probs[0][predicted_label_id].item() * 100:.2f}%")
```

---

## ⚡ Fast Inference với ONNX Runtime (Tối ưu Production & CPU)

Repo cung cấp 2 phiên bản ONNX trong thư mục `onnx/`:
* `onnx/phobert_moderation_fp32.onnx`: Bản chuẩn FP32 (~540MB)
* `onnx/phobert_moderation_int8.onnx`: Bản Quantized INT8 (~135MB, giảm **75%** dung lượng, tăng tốc độ inference CPU **2-3x**)

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

repo_id = "huyleit/phobert-vi-moderation-v1.1"

# 1. Tải tokenizer & ONNX model từ Hugging Face Hub
tokenizer = AutoTokenizer.from_pretrained(repo_id)
onnx_path = hf_hub_download(
    repo_id=repo_id,
    filename="phobert_moderation_int8.onnx", # hoặc "phobert_moderation_fp32.onnx"
    subfolder="onnx"
)

# 2. Khởi tạo ONNX Runtime Session
session = ort.InferenceSession(onnx_path, providers=["CPUExecutionProvider"])

# 3. Chuẩn bị input text
text = "Tôi cảm thấy mệt mỏi và bế tắc quá, không biết phải sống tiếp thế nào..."
inputs = tokenizer(text, return_tensors="np", padding=True, truncation=True, max_length=128)

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
labels_map = {
    0: "CLEAN",
    1: "PROFANITY_VENTING",
    2: "HATE_SPEECH",
    3: "EMOTIONAL_CRISIS"
}

print(f"Nhãn kiểm duyệt: {labels_map[predicted_id]}")
print(f"Độ tin cậy: {probs[0][predicted_id] * 100:.2f}%")
```

---

## ⚙️ Siêu Tham Số Huấn Luyện (Training Hyperparameters)

- **Base Model**: `vinai/phobert-base-v2`
- **Learning Rate**: `2e-5`
- **Batch Size**: `32`
- **Epochs Trained**: `4` (Early Stopping ngắt tại Epoch 4, khôi phục Checkpoint Epoch 4 tối ưu nhất)
- **Optimizer**: AdamW với `weight_decay = 0.01`
- **Warmup Steps**: `300`
- **Mixed Precision**: `FP16`

---

## 📜 Citation & Citation Info

Nếu sử dụng mô hình này trong các công trình nghiên cứu, vui lòng trích dẫn:

```bibtex
@article{phobert_vi_moderation_v1_1,
  title={PhoBERT Multi-Label Contextual Text Moderation for Mental Health Social Networks},
  author={Huy Le et al.},
  year={2026},
  publisher={Hugging Face},
  howpublished={\url{https://huggingface.co/huyleit/phobert-vi-moderation-v1.1}}
}
```
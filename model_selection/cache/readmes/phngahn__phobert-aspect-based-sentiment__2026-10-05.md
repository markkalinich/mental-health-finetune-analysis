---
base_model: vinai/phobert-base
language: vi
pipeline_tag: text-classification
tags:
  - aspect-based-sentiment-analysis
  - sentiment-analysis
  - vietnamese-nlp
  - phobert
license: mit
---

# PhoBERT Aspect-Based Sentiment Analysis

Mô hình phân tích cảm xúc theo khía cạnh (Aspect-Based Sentiment Analysis - ABSA) cho tiếng Việt, được xây dựng dựa trên PhoBERT. Mô hình dự đoán cực tính cảm xúc (**tiêu cực / trung lập / tích cực**) cho **4 khía cạnh** đồng thời trong một lần forward pass:

- **food** (món ăn)
- **price** (giá cả)
- **space** (không gian)
- **service** (phục vụ)

Mô hình được thiết kế đặc biệt cho phân tích đánh giá nhà hàng và ẩm thực tiếng Việt.

## Model Overview

- **Base model:** [vinai/phobert-base](https://huggingface.co/vinai/phobert-base)
- **Architecture:** PhoBERT encoder với 4 classification heads độc lập
- **Task:** Aspect-Based Sentiment Analysis (ABSA)
- **Number of aspects:** 4
- **Number of sentiment classes:** 3 (negative, neutral, positive)

## Output Format

Mô hình trả về tensor với shape: `(batch_size, 4, 3)`

Trong đó:
- `4` tương ứng với số lượng khía cạnh
- `3` tương ứng với số lớp cảm xúc cho mỗi khía cạnh

**Thứ tự các khía cạnh trong output tensor:**
```python
["food", "price", "space", "service"]
```

**Sentiment Labels:**

| ID | Label    | Mô tả       |
|----|----------|-------------|
| 0  | negative | Tiêu cực    |
| 1  | neutral  | Trung lập   |
| 2  | positive | Tích cực    |

## Installation

```bash
pip install torch transformers
```

## Usage

> ⚠️ **Important:** Mô hình này sử dụng custom architecture, do đó bạn phải enable `trust_remote_code=True` khi load.

### Load Model and Tokenizer

```python
import torch
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained(
    "phngahn/phobert-aspect-based-sentiment"
)

model = AutoModel.from_pretrained(
    "phngahn/phobert-aspect-based-sentiment",
    trust_remote_code=True
)
```

### Inference

```python
text = "Món ăn ngon nhưng phục vụ chậm và giá hơi cao"

inputs = tokenizer(text, return_tensors="pt")

with torch.no_grad():
    logits = model(**inputs)

print(logits.shape)  # torch.Size([1, 4, 3])
```

### Decode Predictions

```python
aspect_names = ["food", "price", "space", "service"]
sentiment_labels = ["negative", "neutral", "positive"]

def predict(text):
    inputs = tokenizer(text, return_tensors="pt")
    
    with torch.no_grad():
        logits = model(**inputs)[0]
    
    preds = logits.argmax(dim=1)
    
    return {
        aspect: sentiment_labels[p.item()]
        for aspect, p in zip(aspect_names, preds)
    }

# Example
result = predict("Món ăn ngon nhưng giá cao, phục vụ chậm")
print(result)
```

**Output:**
```python
{
    "food": "positive",
    "price": "negative",
    "space": "neutral",
    "service": "negative"
}
```

## Model Details

- Mô hình dựa trên kiến trúc PhoBERT/RoBERTa và bỏ qua `token_type_ids`
- Tương thích với `AutoModel` và `Trainer` của Hugging Face
- Mô hình không được wrap sẵn thành Hugging Face pipeline

## Intended Use

✅ Phân tích đánh giá nhà hàng tiếng Việt  
✅ Phân tích cảm xúc theo khía cạnh  
✅ Nghiên cứu học thuật và dự án sinh viên  

## Limitations

⚠️ Chỉ được huấn luyện trên dữ liệu nhà hàng/ẩm thực  
⚠️ Hiệu suất có thể giảm trên các domain khác  
⚠️ Mô hình luôn dự đoán cả 4 khía cạnh (giả định tất cả khía cạnh đều xuất hiện)  

## Citation

Nếu bạn sử dụng mô hình này trong công trình học thuật, vui lòng trích dẫn PhoBERT:

```bibtex
@article{phobert,
title     = {{PhoBERT: Pre-trained language models for Vietnamese}},
author    = {Dat Quoc Nguyen and Anh Tuan Nguyen},
journal   = {Findings of EMNLP},
year      = {2020}
}

```

## License

Mô hình này tuân theo license của base model [vinai/phobert-base](https://huggingface.co/vinai/phobert-base).

---
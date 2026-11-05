---
language: vi
license: mit
tags:
- text-classification
- emotion
- vietnamese
- phobert
base_model: vinai/phobert-base-v2
metrics:
- accuracy
- f1
library_name: transformers
---

# brandhub-phobert-V4-emotion

PhoBERT-base LoRA (r=8) fine-tuned cho **phân loại cảm xúc bình luận tiếng Việt** (6 lớp).
Một phần của hệ thống phát hiện xu hướng mạng xã hội **BrandHub** (SEP490 capstone).

## Labels

| id | emotion |
|----|---------|
| 0 | `vui` |
| 1 | `buồn` |
| 2 | `tức_giận` |
| 3 | `lo_sợ` |
| 4 | `ngạc_nhiên` |
| 5 | `trung_lập` |

Ghi chú: `chán_ghét` (ghê tởm/ghét) đã gộp vào `tức_giận` (2 lớp mơ hồ ngữ nghĩa).

## Usage

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

tok = AutoTokenizer.from_pretrained('anha12/brandhub-phobert-V4-emotion')
model = AutoModelForSequenceClassification.from_pretrained('anha12/brandhub-phobert-V4-emotion')

text = "sản phẩm này dùng rất ổn, mình rất hài lòng"
inputs = tok(text, return_tensors='pt', truncation=True, max_length=128)
with torch.no_grad():
    logits = model(**inputs).logits
print(model.config.id2label[logits.argmax(-1).item()])
```

## Metrics (balanced val)

| metric | value |
|--------|-------|
| accuracy | 78.50% |
| macro-F1 | 78.70% |

## Training

- base: `vinai/phobert-base-v2`
- LoRA: r=16, alpha=32, dropout=0.1, target `query`/`key`/`value`
- loss: focal (gamma=2.0) + class weights + label smoothing 0.1
- dataset: 6 lớp cân bằng + 1,000 cặp đối kháng (mỉa mai↔vui thật) ép vào train
- base sạch 10k (idx 0-10038) — lo_sợ/ngạc_nhiên >85%, tức_giận +11.6% nhờ đối kháng

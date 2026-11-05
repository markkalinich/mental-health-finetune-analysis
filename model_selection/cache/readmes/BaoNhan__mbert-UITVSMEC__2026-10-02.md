---
language:
- vi
library_name: transformers
pipeline_tag: text-classification
base_model: "bert-base-multilingual-cased"
datasets:
- tridm/UIT-VSMEC
tags:
- vietnamese
- text-classification
- uit-vsmec
- transfer
- eacl-2027
- emotion-recognition
- social-media
metrics:
- f1
- accuracy
---

# mbert-UITVSMEC

This model is `bert-base-multilingual-cased` fine-tuned for **UIT-VSMEC emotion recognition** on UIT-VSMEC.

## Evaluation protocol

- Dataset size: 6,927 examples.
- Published splits: 5,548 train / 686 development / 693 test.
- Fine-tuning seeds included in the report: [22, 42, 202].
- Training: 3 epoch(s), AdamW, learning rate 2e-05, weight decay 0.01, warmup ratio 0.1.
- Training batch size: 8.
- Maximum sequence length: 256.
- Input mode: raw Vietnamese social-media text.
- The uploaded checkpoint is `best_model` from seed **42**, selected by development Macro-F1.

## Results

Metrics are reported as mean ± sample standard deviation over the completed seeds listed above.

| Metric | Mean ± std |
|---|---:|
| Test Macro-F1 | 0.4270 ± 0.0063 |
| Test accuracy | 0.5286 ± 0.0058 |
| Test macro precision | 0.4717 ± 0.0118 |
| Test macro recall | 0.4188 ± 0.0062 |
| Development Macro-F1 | 0.4061 ± 0.0112 |

### Per-seed results

|       seed |   dev_macro_f1 |   test_macro_f1 |   test_accuracy |
|-----------:|---------------:|----------------:|----------------:|
|  22.000000 |       0.393204 |        0.420134 |        0.522367 |
|  42.000000 |       0.414044 |        0.432377 |        0.529582 |
| 202.000000 |       0.410958 |        0.428554 |        0.533911 |

## Label mapping

```json
{
  "0": "Anger",
  "1": "Disgust",
  "2": "Enjoyment",
  "3": "Fear",
  "4": "Other",
  "5": "Sadness",
  "6": "Surprise"
}
```

## Usage

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_id = "BaoNhan/mbert-UITVSMEC"
tokenizer = AutoTokenizer.from_pretrained(model_id, use_fast=False)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

text = "Đây là nội dung tiếng Việt cần phân loại."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=256)
with torch.no_grad():
    probabilities = model(**inputs).logits.softmax(dim=-1)[0]

predicted_id = int(probabilities.argmax())
print(model.config.id2label[predicted_id], probabilities.tolist())
```

## Files

- `aggregate_metrics.json`: aggregate metrics and publishing metadata.
- `artifacts/per_seed_results.csv`: available completed-seed results.
- Other evaluation artifacts are included when present locally.

## Limitations

UIT-VSMEC is small and class-imbalanced and reflects Vietnamese social-media language from a particular collection period. Emotion labels are subjective, and predictions must not be treated as psychological assessment.

## Dataset citation

```bibtex
@inproceedings{ho-etal-2019-emotion,
  title={Emotion Recognition for Vietnamese Social Media Text},
  author={Ho, Vong Anh and Nguyen, Duong Huynh-Cong and Nguyen, Danh Hoang and Pham, Linh Thi-Van and Nguyen, Duc-Vu and Nguyen, Kiet Van and Nguyen, Ngan Luu-Thuy},
  booktitle={Proceedings of the 16th International Conference of the Pacific Association for Computational Linguistics (PACLING 2019)},
  year={2019},
  pages={319--333},
  url={https://arxiv.org/abs/1911.09339}
}
```

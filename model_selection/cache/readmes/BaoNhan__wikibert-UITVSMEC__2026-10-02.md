---
language:
- vi
library_name: transformers
pipeline_tag: text-classification
base_model: "TurkuNLP/wikibert-base-vi-cased"
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

# wikibert-UITVSMEC

This model is `TurkuNLP/wikibert-base-vi-cased` fine-tuned for **UIT-VSMEC emotion recognition** on UIT-VSMEC.

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
| Test Macro-F1 | 0.4810 ± 0.0051 |
| Test accuracy | 0.5637 ± 0.0079 |
| Test macro precision | 0.6157 ± 0.0090 |
| Test macro recall | 0.4771 ± 0.0007 |
| Development Macro-F1 | 0.4636 ± 0.0103 |

### Per-seed results

|       seed |   dev_macro_f1 |   test_macro_f1 |   test_accuracy |
|-----------:|---------------:|----------------:|----------------:|
|  22.000000 |       0.463332 |        0.483609 |        0.571429 |
|  42.000000 |       0.474079 |        0.484216 |        0.564214 |
| 202.000000 |       0.453504 |        0.475116 |        0.555556 |

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

model_id = "BaoNhan/wikibert-UITVSMEC"
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

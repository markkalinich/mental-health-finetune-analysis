---
language:
- vi
library_name: transformers
pipeline_tag: text-classification
base_model: "xlm-roberta-base"
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

# xlm-roberta-base-UITVSMEC

This model is `xlm-roberta-base` fine-tuned for **UIT-VSMEC emotion recognition** on UIT-VSMEC.

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
| Test Macro-F1 | 0.3952 ± 0.0574 |
| Test accuracy | 0.5695 ± 0.0245 |
| Test macro precision | 0.4250 ± 0.0986 |
| Test macro recall | 0.4156 ± 0.0398 |
| Development Macro-F1 | 0.3707 ± 0.0593 |

### Per-seed results

|       seed |   dev_macro_f1 |   test_macro_f1 |   test_accuracy |
|-----------:|---------------:|----------------:|----------------:|
|  22.000000 |       0.382323 |        0.415625 |        0.568543 |
|  42.000000 |       0.423395 |        0.439588 |        0.594517 |
| 202.000000 |       0.306413 |        0.330397 |        0.545455 |

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

model_id = "BaoNhan/xlm-roberta-base-UITVSMEC"
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

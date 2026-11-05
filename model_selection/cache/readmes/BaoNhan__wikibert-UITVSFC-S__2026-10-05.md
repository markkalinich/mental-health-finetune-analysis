---
language:
- vi
library_name: transformers
pipeline_tag: text-classification
base_model: "TurkuNLP/wikibert-base-vi-cased"
datasets:
- uitnlp/vietnamese_students_feedback
tags:
- vietnamese
- text-classification
- uit-vsfc-sentiment
- transfer
- eacl-2027
- uit-vsfc
- sentiment-analysis
metrics:
- f1
- accuracy
---

# wikibert-UITVSFC-S

This model is `TurkuNLP/wikibert-base-vi-cased` fine-tuned for **UITVSFC-S** on UIT-VSFC.

## Evaluation protocol

- Dataset size: 16,175 examples.
- Shared fixed splits for S and T: 12,940 train / 1,617 development / 1,618 test.
- Split seed: 42; jointly stratified by sentiment–topic labels with exact duplicate groups kept in one split.
- Fine-tuning seeds: [42, 22, 202].
- Training: 3 epoch(s), AdamW, learning rate 2e-05, weight decay 0.01, warmup ratio 0.1.
- Effective train batch size: 8.
- Maximum sequence length: 256.
- Input mode: raw normalized Vietnamese text.
- No class weighting, resampling, external metadata, images, engagement features, or test-time model selection.
- Checkpoints are selected by development Macro-F1. The representative published checkpoint is seed **22**, selected only by development Macro-F1.

## Results

Test metrics are reported as mean ± sample standard deviation over seeds [42, 22, 202].

| Metric | Mean ± std |
|---|---:|
| Test Macro-F1 | 0.8050 ± 0.0042 |
| Test accuracy | 0.9417 ± 0.0013 |
| Test macro precision | 0.8361 ± 0.0094 |
| Test macro recall | 0.7848 ± 0.0062 |
| Development Macro-F1 | 0.8267 ± 0.0093 |

### Per-seed results

|       seed |   dev_macro_f1 |   test_macro_f1 |   test_accuracy |   micro_batch_size |   gradient_accumulation_steps |
|-----------:|---------------:|----------------:|----------------:|-------------------:|------------------------------:|
|  22.000000 |       0.835278 |        0.804672 |        0.943140 |          8.000000 |                      1.000000 |
|  42.000000 |       0.827932 |        0.801085 |        0.940667 |          8.000000 |                      1.000000 |
| 202.000000 |       0.816890 |        0.809393 |        0.941286 |          8.000000 |                      1.000000 |

## Label mapping

```json
{
  "0": "negative",
  "1": "neutral",
  "2": "positive"
}
```

## Usage

```python
import torch
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_id = "BaoNhan/wikibert-UITVSFC-S"
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

- `aggregate_metrics.json`: aggregate metrics and training manifest.
- `artifacts/per_seed_results.csv`: one row per fine-tuning seed.
- `artifacts/seed_*_confusion_matrix.csv`: confusion matrix for each seed.
- `artifacts/seed_*_classification_report.json`: per-class metrics.
- `artifacts/seed_*_test_predictions.csv`: IDs, gold/predicted labels and probabilities; raw text is excluded.

## Limitations

UIT-VSFC contains student feedback from a specific educational context. Performance may not transfer to other institutions, domains, informal writing styles, or newly emerging vocabulary. Predictions should not be treated as explanations of student intent.

## Dataset citation

```bibtex
@InProceedings{8573337,
  author={Nguyen, Kiet Van and Nguyen, Vu Duc and Nguyen, Phu X. V. and Truong, Tham T. H. and Nguyen, Ngan Luu-Thuy},
  booktitle={2018 10th International Conference on Knowledge and Systems Engineering (KSE)},
  title={UIT-VSFC: Vietnamese Students' Feedback Corpus for Sentiment Analysis},
  year={2018},
  pages={19--24},
  doi={10.1109/KSE.2018.8573337}
}
```

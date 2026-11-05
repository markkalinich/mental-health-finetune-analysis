---
license: apache-2.0
language:
- en
library_name: gliner
pipeline_tag: token-classification
base_model: urchade/gliner_small-v2.1
base_model_relation: finetune
datasets:
- gretelai/gretel-pii-masking-en-v1
tags:
- fine-tuned
- pii
- berkerdooo
---

# English PII extraction and redaction

A compact 166M parameter entity extractor fine-tuned to locate eight kinds of sensitive information in short English documents. The model returns labeled text spans; a deterministic helper replaces those spans with placeholders.

## Evaluation against the base model

| Metric | Base | Fine tuned | Change |
|---|---:|---:|---:|
| Span precision | 32.16% | 88.71% | +56.56 points |
| Span recall | 44.09% | 94.57% | +50.48 points |
| Span F1 | 37.19% | 91.55% | +54.36 points |

Exact character span and label matches on 500 held-out documents. Each model selects its threshold separately from the same grid (0.3–0.7) on the first 200 validation examples. Threshold choice never uses the test split. Gold spans that could not align to the base tokenizer or exceeded its width were omitted from training, but test metrics retain all selected gold spans.

These results describe the fixed held-out subset from the public dataset. They do not measure general performance across other domains. evaluation.json and both prediction files provide the underlying evidence.

## Training and data

Base: [urchade/gliner_small-v2.1](https://huggingface.co/urchade/gliner_small-v2.1). Dataset: [gretelai/gretel-pii-masking-en-v1](https://huggingface.co/datasets/gretelai/gretel-pii-masking-en-v1).

Training used 9,981 examples, seed 42 and 1,248 optimizer steps on one NVIDIA L40S. The three task jobs ran concurrently. The initial training job took 15.7 minutes, including model loading, evaluation and time waiting for the other base evaluations. Subsequent evaluation and reload checks are recorded separately. This is not an isolated training-speed benchmark. Training used PyTorch 2.9.1 with CUDA 12.8, Transformers 5.16.0 and the package pins included in the repository. Arguments and environment details are saved alongside the weights.

```json
{
  "learning_rate": 1e-05,
  "per_device_train_batch_size": 16,
  "gradient_accumulation_steps": 1,
  "num_train_epochs": 2,
  "lr_scheduler_type": "cosine",
  "bf16": true,
  "seed": 42,
  "actual_training_rows": 9981,
  "optimizer_steps": 1248,
  "actual_epochs": 2.0,
  "base_revision": "4e091416cf7c3481db542c2a3d26156916f3a47f",
  "dataset_revision": "e06eb1499ca8d54470f085021cd8e54f9efac7fd",
  "other_layers_learning_rate": 5e-05,
  "labels": [
    "credit card number",
    "date of birth",
    "email",
    "identifier",
    "person",
    "phone number",
    "social security number",
    "street address"
  ],
  "selected_threshold": 0.6
}
```

Dataset split counts: {"test": {"count": 500, "duplicates_removed": 0}, "validation": {"count": 500, "duplicates_removed": 0}, "train": {"count": 10000, "duplicates_removed": 0}}. Fixed-seed shuffled subset; <=2500 characters and <=250 word/punctuation tokens, containing selected PII. Exact text duplicates removed with held-out splits taking priority.

## Usage

Install the pinned packages in reproduce/requirements-gpu.txt with a compatible PyTorch build, then run:

```python
from gliner import GLiNER
model = GLiNER.from_pretrained("berkerdooo/gliner-pii-redactor-en")
labels = ['credit card number', 'date of birth', 'email', 'identifier', 'person', 'phone number', 'social security number', 'street address']
text = "Contact Maya Patel at maya.patel@example.com."
entities = model.inference(text, labels, threshold=0.6, flat_ner=False, multi_label=True)
print(entities)

# Apply replacements from the end so original character offsets remain valid.
spans = sorted({(e["start"], e["end"], e["label"]) for e in entities}, reverse=True)
redacted = text
last_start = len(text)
for start, end, label in spans:
    if end <= last_start:
        redacted = redacted[:start] + "[" + label.upper() + "]" + redacted[end:]
        last_start = start
print(redacted)
```

## Scope and limitations

Evaluation uses synthetic Gretel documents. Only the eight configured labels are covered; other sensitive information can remain in the text. Entity spans are limited by the base architecture to 12 word tokens. Recall and precision on real documents can differ from this test.

## Reproduce the run

The reproduce folder contains the training script, shared helpers, preparation code, package pins and revision manifest. Run `PREPARE_TASKS=pii python prepare.py` to prepare this task locally, then copy the prepared data and any downloaded base weights into the GPU environment.  The scripts compare the unchanged base with the fine-tuned model and coordinate concurrent starts through base_ready markers. For a standalone run, set FINETUNE_TASKS=pii before executing the training script. Training and evaluation use the official splits with the documented fixed-seed sampling.

## License and attribution

Weights and adapters use Apache License 2.0.

Training data is published under Apache License 2.0 by Gretel.ai. The dataset revision and preprocessing are recorded in data_manifest.json.

Fine-tune prepared for berkerdooo. Base model credit belongs to Urchade Zaratiana and the GLiNER authors.

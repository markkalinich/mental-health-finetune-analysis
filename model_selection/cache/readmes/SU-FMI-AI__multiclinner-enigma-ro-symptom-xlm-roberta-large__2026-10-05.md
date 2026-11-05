---
tags:
- token-classification
- ner
- clinical
- multiclinner
- multiclinai
- transformers
- xlm-roberta
base_model: xlm-roberta-large
pipeline_tag: token-classification
library_name: transformers
license: cc-by-4.0
---

# MultiClinNER ENIGMA RO Symptom XLM-RoBERTa-large Model

This is a Romanian clinical **Named Entity Recognition (NER)** model for the **Symptom** entity type, fine-tuned from `xlm-roberta-large` on the Romanian portion of the **MultiClinNER** shared task. The model was developed by **Team Enigma** at the Faculty of Mathematics and Informatics, Sofia University.

## Description

The model is based on `xlm-roberta-large` and fine-tuned for token classification to identify `SYMPTOM` clinical entities.

This version was trained on `the train split only`.

### Training Hyperparameters
The following hyperparameters were used during training:
- **Maximum Sequence Length:** 512
- **Stride:** 128
- **Learning Rate:** 2e-5
- **Training Epochs:** 5
- **Per Device Train Batch Size:** 4
- **Gradient Accumulation Steps:** 2 (Effective Batch Size = 8)
- **Weight Decay:** 0.01
- **Seed:** 42
- **Precision:** `bf16=True`, `tf32=True`

## Post-processing

The official submission pipeline includes an additional rule-based post-processing step applied after model inference. The post-processing step handles span cleanup, duplicate removal, overlapping span resolution, punctuation trimming, and restoration of entity spans using the original document offsets.

The post-processing code is available in the official repository.

## Usage

> **Note:** The snippet below provides a quick out-of-the-box pipeline demonstration for raw text inference using standard Hugging Face subtoken aggregation. For official evaluation and submission, please utilize the dedicated word-alignment and offset restoration script from the repository.

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

repo_id = "MonikaPeteva/multiclinner-enigma-ro-symptom-xlm-roberta-large"

tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForTokenClassification.from_pretrained(repo_id)

ner = pipeline(
    "token-classification",
    model=model,
    tokenizer=tokenizer,
    aggregation_strategy="simple"
)

text = "Patient was diagnosed with pneumonia."
predictions = ner(text)

print(predictions)
```

## Intended Use

This model is intended for clinical NER research in the context of the MultiClinNER task.

## Limitations

The model should be used with awareness that the official submission results may depend on the additional post-processing pipeline.

## Repository

* **Official Repository:** []()

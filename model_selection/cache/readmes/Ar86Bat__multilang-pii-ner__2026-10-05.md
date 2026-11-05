---
license: mit
datasets:
- ai4privacy/open-pii-masking-500k-ai4privacy
language:
- en
- de
- fr
- it
metrics:
- accuracy
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: token-classification
tags:
- pii
- deidentification
- sensitive
- multilingual
---
# Multilingual PII NER

A multilingual transformer model (`xlm-roberta-base`) fine-tuned for Named Entity Recognition (NER) to detect and mask Personally Identifiable Information (PII) in text across English, German, Italian, and French.

## Model Description

- **Architecture:** XLM-RoBERTa Base
- **Task:** Named Entity Recognition (NER) for PII detection and masking
- **Languages:** English, German, Italian, French
- **Training Data:** [ai4privacy/open-pii-masking-500k-ai4privacy](https://huggingface.co/datasets/ai4privacy/open-pii-masking-500k-ai4privacy) (CoNLL format)
- **License:** MIT

## Intended Uses & Limitations

- **Intended use:** Detect and mask PII entities in multilingual text for privacy-preserving applications.
- **Not suitable for:** Use cases requiring perfect recall/precision on rare or ambiguous PII types without further fine-tuning.

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForTokenClassification, pipeline

model_id = "Ar86Bat/multilang-pii-ner"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForTokenClassification.from_pretrained(model_id)

nlp = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")
text = "John Doe was born on 12/12/1990 and lives in Berlin."
results = nlp(text)
print(results)
```

## Evaluation Results

- **Overall accuracy:** 99.24%
- **Macro F1-score:** 0.954
- **Weighted F1-score:** 0.992

### Entity-level highlights

- High F1-scores (>0.97) for common entities: `AGE`, `BUILDINGNUM`, `CITY`, `DATE`, `EMAIL`, `GIVENNAME`, `STREET`, `TELEPHONENUM`, `TIME`
- Excellent performance on `EMAIL` and `DATE` (F1 ≈ 0.999)
- Lower F1-scores for challenging/rare entities: `DRIVERLICENSENUM` (F1 ≈ 0.85), `GENDER` (F1 ≈ 0.83), `PASSPORTNUM` (F1 ≈ 0.88), `SURNAME` (F1 ≈ 0.85), `SEX` (F1 ≈ 0.84)

## Training & Validation

- Preprocessing, training, and validation scripts are available in the [GitHub repository](https://github.com/Ar86Bat/multilang-pii-ner).
- All model artifacts and outputs are in the `model/` directory.
- **Training hyperparameters:**
  - `num_train_epochs=2`  # Total number of training epochs
  - `per_device_train_batch_size=32`  # Batch size for training
  - `per_device_eval_batch_size=32`    # Batch size for evaluation

## Citation

If you use this model, please cite the repository:

```
@misc{ar86bat_multilang_pii_ner_2025,
  author = {Arif Hizlan},
  title = {Multilingual PII NER},
  year = {2025},
  howpublished = {\\url{https://huggingface.co/Ar86Bat/multilang-pii-ner}}
}
```

## GitHub Repository

[https://github.com/Ar86Bat/multilang-pii-ner](https://github.com/Ar86Bat/multilang-pii-ner)

## License

MIT License
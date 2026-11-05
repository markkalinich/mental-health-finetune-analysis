---
license: apache-2.0
language:
- en
- it
- fr
- de
- es
- nl
library_name: transformers
tags:
- pii
- ner
- token-classification
- privacy
- distilbert
- onnx
datasets:
- ai4privacy/pii-masking-400k
pipeline_tag: token-classification
---

# HikmaAI DistilBERT PII NER

A fine-tuned DistilBERT model for Named Entity Recognition (NER) of Personally Identifiable Information (PII) in multilingual text. Trained on 6 languages (English, Italian, French, German, Spanish, Dutch). Detects 17 entity types across personal, financial, and contact information categories.

## Model Details

| Property | Value |
|----------|-------|
| Base model | `distilbert-base-uncased` |
| Task | Token classification (BIO tagging) |
| Entity types | 17 (35 labels: B- and I- for each + O) |
| Parameters | ~66M |
| ONNX INT8 size | 129 MB |
| Max sequence length | 512 |
| Input tensors | `input_ids`, `attention_mask` |
| Output | `logits` shape `[batch, seq_len, 35]` |
| License | Apache 2.0 |

## Entity Types

| Category | Entity | Label | Examples |
|----------|--------|-------|----------|
| **Personal** | Given name | GIVENNAME | John, Maria, Ahmed |
| | Surname | SURNAME | Smith, Garcia, Chen |
| | Date of birth | DATEOFBIRTH | 1990-01-15, 15/03/1985 |
| | Username | USERNAME | john_doe, user123 |
| | Password | PASSWORD | P@ssw0rd!, mySecret |
| **Contact** | Email | EMAIL | john@example.com |
| | Phone | TELEPHONENUM | +1-555-0123, 06 12345678 |
| | Street | STREET | 123 Main St, Via Roma 42 |
| | City | CITY | New York, London, Milano |
| | ZIP code | ZIPCODE | 10001, SW1A 1AA |
| | Building number | BUILDINGNUM | Apt 4B, Suite 200 |
| **Financial** | Credit card | CREDITCARDNUMBER | 4111-1111-1111-1111 |
| | Account number | ACCOUNTNUM | GB29 NWBK 6016 1331 9268 19 |
| | Tax number | TAXNUM | SSN, TIN, codice fiscale |
| **Identity** | Social security | SOCIALNUM | 123-45-6789 |
| | Driver license | DRIVERLICENSENUM | D1234567 |
| | ID card | IDCARDNUM | National ID numbers |

## Usage

### Transformers

```python
from transformers import pipeline

ner = pipeline(
    "ner",
    model="hikmaai-io/hikmaai-distilbert-pii",
    aggregation_strategy="simple"
)

results = ner("Contact John Smith at john@example.com or call +1-555-0123")
for entity in results:
    print(f"{entity['word']:20s} -> {entity['entity_group']:20s} ({entity['score']:.2f})")
```

### ONNX Runtime

```python
import onnxruntime as ort
from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("hikmaai-io/hikmaai-distilbert-pii")
session = ort.InferenceSession("onnx/model_quantized.onnx")

inputs = tokenizer("Contact John Smith at john@example.com", return_tensors="np")
outputs = session.run(None, {
    "input_ids": inputs["input_ids"],
    "attention_mask": inputs["attention_mask"],
})
# outputs[0] shape: [1, seq_len, 35] (logits for 35 BIO labels)
```

### ONNX Runtime (Go)

The model is designed for high-performance inference in Go applications via `yalue/onnxruntime_go`:

```go
// 2 input tensors: input_ids, attention_mask
// Output: logits [1, seq_len, 35]
// Post-processing: argmax per token -> BIO label -> entity spans
```

## Training

- **Base model**: `distilbert-base-uncased`
- **Dataset**: [ai4privacy/pii-masking-400k](https://huggingface.co/datasets/ai4privacy/pii-masking-400k) (325K annotated examples, 6 languages: EN 21%, IT 20%, FR 20%, DE 20%, ES 10%, NL 10%)
- **Checkpoints**: 15,000 steps
- **Quantization**: INT8 dynamic quantization via ONNX Runtime (FP32 also available)

## File Structure

```
├── config.json              # Model configuration
├── model.safetensors        # FP32 weights (PyTorch/safetensors)
├── tokenizer.json           # Fast tokenizer
├── tokenizer_config.json    # Tokenizer configuration
├── onnx/
│   ├── model.onnx           # FP32 ONNX
│   └── model_quantized.onnx # INT8 ONNX (recommended for inference)
```

## Privacy Design

This model is designed for privacy-preserving PII detection in AI security gateways:

- **Detection only**: the model identifies entity spans and types. It does not store, transmit, or log the actual PII values
- **Counts, not content**: downstream systems receive entity type counts (e.g., `{"EMAIL": 2, "PHONE": 1}`), never the detected text
- **Local inference**: runs entirely on-device via ONNX Runtime, no external API calls
- **Stateless**: no request data is retained between inferences

## Limitations

- Trained on 6 languages (EN, IT, FR, DE, ES, NL); performance on other languages is untested
- Maximum sequence length: 512 tokens (longer texts require chunking)
- Regex-based PII detection (emails, phone numbers, credit cards) may outperform NER for well-structured patterns; this model adds value for unstructured PII (names, addresses, free-text credentials)
- INT8 quantization may slightly reduce accuracy on edge cases compared to FP32

## Citation

```bibtex
@misc{hikmaai-distilbert-pii,
  author = {HikmaAI},
  title = {HikmaAI DistilBERT PII NER: Fine-tuned model for PII detection in AI security gateways},
  year = {2026},
  url = {https://huggingface.co/hikmaai-io/hikmaai-distilbert-pii}
}
```

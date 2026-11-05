---
license: apache-2.0
language:
- multilingual
base_model: jhu-clsp/mmBERT-base
tags:
- mmbert
- pii-detection
- token-classification
- ner
- multilingual
- rust
- candle
- merged
metrics:
- accuracy
---

# mmBERT PII Detector (Merged for Rust)

This is a **merged** mmBERT model for PII (Personally Identifiable Information) detection, optimized for Rust inference using the candle framework.

## Model Details

- **Base Model:** [jhu-clsp/mmBERT-base](https://huggingface.co/jhu-clsp/mmBERT-base)
- **Task:** Token classification for PII detection
- **Languages:** Multilingual (1800+ languages)
- **Training:** LoRA fine-tuned then merged with base model
- **Inference:** Optimized for Rust candle-binding

## PII Types Detected

- Names (PERSON)
- Email addresses (EMAIL)
- Phone numbers (PHONE)
- Addresses (ADDRESS)
- Credit card numbers (CREDIT_CARD)
- Social Security Numbers (SSN)
- Dates (DATE)
- And more...

## Usage with Rust (candle-binding)

```rust
use candle_semantic_router::model_architectures::traditional::TraditionalModernBertTokenClassifier;

let classifier = TraditionalModernBertTokenClassifier::new("path/to/model", true)?;
let results = classifier.classify_tokens("Contact john@example.com or call 555-1234")?;
for (token, label, confidence) in results {
    if label != "O" {
        println!("PII: {} -> {} ({:.1}%)", token, label, confidence * 100.0);
    }
}
```

## Training Configuration

- **LoRA Rank:** 32
- **LoRA Alpha:** 64
- **Epochs:** 10
- **Batch Size:** 64
- **Learning Rate:** 2e-5

## License

Apache 2.0

---

## Maintenance

- Repo README updated by automation (timestamp: 2026-01-30 UTC).

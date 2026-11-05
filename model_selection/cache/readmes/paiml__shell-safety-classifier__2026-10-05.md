---
license: mit
pipeline_tag: text-classification
tags:
  - shell-safety
  - classifier
  - aprender
  - rust
  - bashrs
model-index:
  - name: paiml/shell-safety-classifier
    results:
      - task:
          type: text-classification
        dataset:
          name: bashrs-corpus
          type: custom
        metrics:
          - name: Train Accuracy
            type: accuracy
            value: 0.966
          - name: Validation Accuracy
            type: accuracy
            value: 0.632
          - name: Training Samples
            type: custom
            value: "17942"
---

# Shell Safety Classifier

Classifies shell scripts into 5 safety categories using a lightweight MLP trained on the [bashrs](https://github.com/paiml/bashrs) corpus.

## Labels

| Index | Label | Description |
|-------|-------|-------------|
| 0 | safe | Script is deterministic, idempotent, and properly quoted |
| 1 | needs-quoting | Contains unquoted variables susceptible to word splitting |
| 2 | non-deterministic | Uses `$RANDOM`, timestamps, process IDs, or other non-deterministic sources |
| 3 | non-idempotent | Operations not safe to re-run (missing `-p`, `-f` flags) |
| 4 | unsafe | Security issues (injection vectors, privilege escalation) |

## Architecture

- **Model**: MLP classifier (ShellVocabulary token embeddings -> 128 -> 64 -> 5)
- **Tokenizer**: ShellVocabulary (250 shell-specific tokens, max_seq_len=64)
- **Format**: SafeTensors (model.safetensors) + JSON config + vocab
- **Framework**: [aprender](https://github.com/paiml/aprender) (pure Rust ML, no Python dependencies)

## Training

- **Corpus**: bashrs v2 corpus (17,942 entries: 16,431 Bash + 804 Makefile + 707 Dockerfile)
- **Split**: 80/20 train/validation (14,353 / 3,589)
- **Epochs**: 50
- **Optimizer**: Adam (lr=0.01)
- **Loss**: CrossEntropyLoss
- **Train accuracy**: 96.6%
- **Validation accuracy**: 63.2%

### Class Distribution

| Label | Count | Percentage |
|-------|-------|------------|
| safe | 16,126 | 89.9% |
| needs-quoting | 1,814 | 10.1% |
| unsafe | 2 | 0.01% |

## Usage

### With bashrs CLI

```bash
# Classify a single script
bashrs classify script.sh

# Classify with format detection
bashrs classify Makefile --format makefile

# Multi-label classification
bashrs classify script.sh --multi-label
```

### With aprender (Rust)

```rust
use aprender::models::shell_safety::{ShellSafetyClassifier, SafetyClass};

let classifier = ShellSafetyClassifier::load("/path/to/model")?;
let result = classifier.predict("echo $HOME")?;
// result: SafetyClass::NeedsQuoting
```

## Files

| File | Size | Description |
|------|------|-------------|
| model.safetensors | 68 KB | Model weights |
| vocab.json | 3.6 KB | Shell tokenizer vocabulary |
| config.json | 371 B | Model architecture config |

## Limitations

- The v2.0 MLP architecture has limited validation accuracy (63.2%) due to class imbalance and simple architecture
- Best suited for binary safe/unsafe classification (96%+ accuracy when collapsing to 2 classes)
- A Qwen2.5-Coder fine-tuned version is planned for higher accuracy on minority classes

## License

MIT

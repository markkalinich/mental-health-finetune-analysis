---
license: apache-2.0
base_model: roberta-base
tags:
- lora
- semantic-router
- pii-classification
- text-classification
- candle
- rust
language:
- en
pipeline_tag: text-classification
library_name: candle
---

# lora_pii_detector_roberta-base_model

## Model Description

This is a LoRA (Low-Rank Adaptation) fine-tuned model based on **roberta-base** for PII Detection - Detects personally identifiable information in text using token classification.

This model is part of the [semantic-router](https://github.com/vllm-project/semantic-router) project and is optimized for use with the Candle framework in Rust.

## Model Details

- **Base Model**: roberta-base
- **Task**: Pii Classification
- **Framework**: Candle (Rust)
- **Model Size**: ~473MB
- **LoRA Rank**: 16
- **LoRA Alpha**: 32
- **Target Modules**: attention.self.query, attention.self.value, attention.output.dense, intermediate.dense, output.dense

## Usage

### With semantic-router (Recommended)

```python
from semantic_router import SemanticRouter

# The model will be automatically downloaded and used
router = SemanticRouter()
results = router.classify_batch(["Your text here"])
```

### With Candle (Rust)

```rust
use candle_core::{Device, Tensor};
use candle_transformers::models::bert::BertModel;

// Load the model using Candle
let device = Device::Cpu;
let model = BertModel::load(&device, &config, &weights)?;
```

## Training Details

This model was fine-tuned using LoRA (Low-Rank Adaptation) technique:

- **Rank**: 16
- **Alpha**: 32 
- **Dropout**: 0.1
- **Target Modules**: attention.self.query, attention.self.value, attention.output.dense, intermediate.dense, output.dense

## Performance

PII Detection - Detects personally identifiable information in text using token classification

For detailed performance metrics, see the [training results](https://github.com/vllm-project/semantic-router/blob/main/training-result.md).

## Files

- `model.safetensors`: LoRA adapter weights
- `config.json`: Model configuration
- `lora_config.json`: LoRA-specific configuration
- `tokenizer.json`: Tokenizer configuration
- `label_mapping.json`: Label mappings for classification

## Citation

If you use this model, please cite:

```bibtex
@misc{semantic-router-lora,
  title={LoRA Fine-tuned Models for Semantic Router},
  author={Semantic Router Team},
  year={2025},
  url={https://github.com/vllm-project/semantic-router}
}
```

## License

Apache 2.0

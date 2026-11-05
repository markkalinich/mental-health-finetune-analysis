
---
language: en
license: mit
library_name: transformers
pipeline_tag: text-generation
tags:
- medical
- healthcare
- dialogue
- gpt2
- custom-tokenizer
- esp32
- edge-deployment
datasets:
- lavita/medical-qa-datasets
metrics:
- perplexity
model-index:
- name: medical-llm-10m-base
  results:
  - task:
      type: text-generation
      name: Medical Dialogue Generation
    metrics:
    - type: perplexity
      value: 4.40
      name: Validation Perplexity
---

# Medical LLM Base Model (10M Parameters)

## Model Description

This is a 10 million parameter GPT-2 style language model specifically trained for medical dialogue generation. The model is designed as a base model for fine-tuning on specialized medical tasks, particularly sensor interpretation for ESP32 edge deployment.

## Model Details

- **Model Type**: Causal Language Model (GPT-2 architecture)
- **Parameters**: 10,126,336
- **Architecture**: 10 layers, 256 hidden dimensions, 8 attention heads
- **Vocabulary**: 8,192 custom medical tokens (SentencePiece BPE)
- **Context Length**: 512 tokens
- **Training Data**: 6,788 medical dialogues from professional sources

## Performance

- **Validation Perplexity**: 4.40
- **Training Loss**: Converged to ~1.48
- **Success Rate**: 100% response generation

## Intended Use

### Primary Use Case
- **Base model for medical dialogue fine-tuning**
- **ESP32 sensor interpretation** (temperature, heart rate, SpO2)
- **Edge deployment** on resource-constrained devices

### Fine-tuning Recommendations
- Learning rate: 1e-4 (lower than base training)
- Epochs: 2-3 (fewer epochs needed)
- Batch size: 8
- Target applications: Sensor data interpretation, medical assessment

## Model Architecture

```python
GPT2Config(
    vocab_size=8192,
    n_positions=512,
    n_embd=256,
    n_layer=10,
    n_head=8,
    n_inner=1024
)
```

## Usage

### Loading the Model

```python
from transformers import GPT2LMHeadModel, GPT2Config
import torch

# Load configuration
config = GPT2Config.from_pretrained("OussamaEL/medical-llm-10m-base")

# Load model
model = GPT2LMHeadModel.from_pretrained("OussamaEL/medical-llm-10m-base")

# For ESP32 sensor interpretation fine-tuning
# Use the provided fine-tuning scripts with sensor datasets
```

### Example Fine-tuning for Sensor Data

```python
# Input format for sensor interpretation:
# "<bos>Sensors: Temp 38.5°C, HR 95 bpm, SpO2 96% ||| Assessment: [response]<eos>"

# Expected output:
# "Elevated temperature with normal heart rate. Possible mild infection."
```

## Training Details

- **Training Data**: Medical dialogue dataset (iCliniq professional responses)
- **Training Epochs**: 5
- **Learning Rate**: 5e-4 with cosine scheduling
- **Batch Size**: 16 (effective)
- **Hardware**: CUDA-enabled GPU
- **Training Time**: ~2 hours

## Limitations

- **Specialized vocabulary**: Optimized for medical terminology
- **Context length**: Limited to 512 tokens
- **Domain-specific**: Best performance on medical dialogue tasks
- **Size constraints**: Designed for edge deployment, may lack capacity for complex reasoning

## Ethical Considerations

- **Medical advice**: This model should NOT be used for direct medical diagnosis
- **Professional oversight**: Always require medical professional validation
- **Edge deployment**: Suitable for preliminary assessment only
- **Data privacy**: Trained on anonymized medical dialogues

## Technical Specifications

- **Model Size**: ~38.6 MB (unquantized)
- **Deployment Size**: ~10-15 MB (with quantization)
- **Memory Requirements**: 50-100 MB RAM
- **Inference Speed**: <1 second per assessment
- **Target Hardware**: ESP32-S3, similar microcontrollers

## Citation

If you use this model, please cite:

```bibtex
@model{medical_llm_10m,
  title={Medical LLM Base Model for ESP32 Deployment},
  author={Your Name},
  year={2024},
  url={https://huggingface.co/OussamaEL/medical-llm-10m-base}
}
```

## License

MIT License - See LICENSE file for details.

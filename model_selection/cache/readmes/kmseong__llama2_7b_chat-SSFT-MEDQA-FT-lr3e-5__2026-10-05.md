---
license: llama3.1
language:
- en
library_name: transformers
tags:
- llama
- safety
- alignment
- warp
---

# WaRP-Safety-Llama3_8B_Instruct

Fine-tuned Llama 3.1 8B Instruct model for safety alignment using Weight space Rotation Process (WaRP).

## Model Details

- **Base Model**: meta-llama/Llama-3.1-8B-Instruct
- **Training Method**: Safety-First WaRP (3-Phase pipeline)
- **Training Date**: 2026-04-30

## Training Procedure

### Phase 1: Basis Construction
- Collected activations from FFN layers using safety data
- Computed SVD to obtain orthonormal basis vectors
- Identified 419 important neurons in layer 31

### Phase 2: Importance Scoring
- Calculated importance scores using gradient-based methods
- Generated masks for important directions
- Used teacher forcing on safety responses

### Phase 3: Incremental Learning
- Fine-tuned on utility task (GSM8K) with gradient masking
- Protected important directions to maintain safety
- Improved utility while preserving safety mechanisms

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "kmseong/WaRP-Safety-Llama3_8B_Instruct"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype="auto", device_map="auto")

# Generate text
inputs = tokenizer("What is machine learning?", return_tensors="pt")
outputs = model.generate(**inputs, max_length=100)
print(tokenizer.decode(outputs[0]))
```

## Safety Features

- ✅ Protected safety mechanisms through gradient masking
- ✅ Maintained refusal capability for harmful requests
- ✅ Improved utility on reasoning tasks
- ✅ Balanced safety-utility tradeoff

## Datasets

- **Safety Data**: LibrAI/do-not-answer
- **Utility Data**: openai/gsm8k

## Citation

```
@article{warp-safety,
  title={Safety-First WaRP: Weight space Rotation Process for LLM Safety Alignment},
  author={Min-Seong Kim},
  year={2026}
}
```

## License

This model is built on Llama 3.1 8B Instruct and follows the same license.

## Disclaimer

This model is fine-tuned for improved safety. Users should evaluate model outputs for their specific use cases and apply additional safety measures as needed.

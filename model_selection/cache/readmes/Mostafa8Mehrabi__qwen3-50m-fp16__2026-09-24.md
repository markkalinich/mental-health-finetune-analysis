---
license: apache-2.0
base_model: Qwen/Qwen3-0.6B
tags:
- qwen
- causal-lm
- gpt2-tokenizer
- fp16
library_name: transformers
---

# Qwen3-50M with GPT-2 Tokenizer (FP16)

A 50M parameter version of Qwen3-0.6B using GPT-2's tokenizer for better compatibility, optimized with FP16 precision.

## Model Details

- **Base Model**: Qwen/Qwen3-0.6B  
- **Architecture**: Qwen3 (8 layers, 384 hidden size)
- **Parameters**: ~50M (reduced from 637M)
- **Tokenizer**: GPT-2 (50,257 vocabulary)
- **Vocabulary**: Reduced from 151,936 to 50,257 tokens
- **Precision**: FP16 (half precision for memory efficiency)
- **Model Size**: ~100MB (vs ~200MB in FP32)

## Usage

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load with automatic fp16 support
tokenizer = AutoTokenizer.from_pretrained("Mostafa8Mehrabi/qwen3-50m-fp16")
model = AutoModelForCausalLM.from_pretrained(
    "Mostafa8Mehrabi/qwen3-50m-fp16",
    torch_dtype=torch.float16,  # Explicitly use fp16
    device_map="auto"  # Automatically place on available device
)

# For GPU inference (recommended)
# model = model.to("cuda") # if you have a GPU

inputs = tokenizer("Hello, how are you?", return_tensors="pt")
# Move inputs to same device as model if using GPU
# inputs = {k: v.to(model.device) for k, v in inputs.items()}

outputs = model.generate(**inputs, max_length=50, do_sample=True, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Key Features

- ✅ **FP16 Precision**: 50% smaller model size, faster inference
- ✅ **Standard GPT-2 tokenizer** (no trust_remote_code)
- ✅ **Compatible vocabulary sizes**  
- ✅ **SafeTensors format** for faster loading
- ✅ **Works like any HuggingFace model**
- ✅ **13x smaller** than original Qwen3-0.6B
- ✅ **GPU optimized** for efficient inference

## Architecture Comparison

| Component | Original | This Model |
|-----------|----------|------------|
| Parameters | 637M | ~50M |
| Vocabulary | 151,936 | 50,257 |
| Hidden Size | 1024 | 384 |
| Layers | 28 | 8 |
| Tokenizer | Qwen3 | GPT-2 |
| Precision | FP32 | **FP16** |
| Model Size | ~1.2GB | **~100MB** |

## Memory Requirements

- **FP16**: ~100MB model + ~50MB working memory = **~150MB total**
- **FP32**: ~200MB model + ~100MB working memory = ~300MB total
- **Memory savings**: ~50% reduction compared to FP32

## Performance Notes

- FP16 provides significant memory savings with minimal quality loss
- Ideal for deployment in resource-constrained environments
- Compatible with both CPU and GPU inference
- Faster loading times due to smaller file size

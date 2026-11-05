---
license: apache-2.0
language: en
tags:
- qwen3
- medical
- chat
- fine-tuned
- gguf
- healthcare
datasets:
- custom-medical-qa
model_type: qwen3
base_model: Qwen/Qwen3-0.6B
---

# Qwen3-0.6B-Medical-Finetuned-v1

This model is a fine-tuned version of `Qwen/Qwen3-0.6B` specialized for medical question-answering. It's designed to provide helpful, accurate medical information while emphasizing the importance of professional medical consultation.

## 🏥 Model Description

- **Base Model**: `Qwen/Qwen3-0.6B`
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Dataset**: Custom medical Q&A dataset covering common health topics.
- **Training**: Optimized for conversational medical assistance.

## ⚠️ Important Disclaimer

**This model is NOT a substitute for professional medical advice, diagnosis, or treatment. Always consult qualified healthcare providers for medical concerns. Do not use this model for emergency situations - call emergency services immediately.**

## 🚀 Usage

### With `transformers`

```python
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import torch

model_id = "rohitnagareddy/Qwen3-0.6B-Medical-Finetuned-v1"

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
    trust_remote_code=True
)

# Create a conversation pipeline
pipe = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer
)

# Create conversation
prompt = "<|im_start|>system\nYou are a helpful medical assistant providing accurate, evidence-based information.<|im_end|>\n<|im_start|>user\nWhat are the symptoms of hypertension?<|im_end|>\n<|im_start|>assistant\n"

# Generate response
response = pipe(prompt, max_new_tokens=300, temperature=0.7, top_p=0.9, do_sample=True)
print(response[0]["generated_text"])
```

## 🔧 GGUF Versions

This repository includes quantized GGUF versions for use with `llama.cpp` and compatible tools:

- `Qwen3-0.6B-Medical-Finetuned-v1.fp16.gguf` - Full precision (largest, best quality)
- `Qwen3-0.6B-Medical-Finetuned-v1.Q8_0.gguf` - 8-bit quantization (good balance)
- `Qwen3-0.6B-Medical-Finetuned-v1.Q5_K_M.gguf` - 5-bit quantization (smaller, fast)
- `Qwen3-0.6B-Medical-Finetuned-v1.Q4_K_M.gguf` - 4-bit quantization (smallest, fastest)

### Using with Ollama

```bash
# Pull the model (once available on the Hub)
ollama pull rohitnagareddy/Qwen3-0.6B-Medical-Finetuned-v1

# Run the model
ollama run rohitnagareddy/Qwen3-0.6B-Medical-Finetuned-v1 "What are the early signs of diabetes?"
```

## 📊 Training Details

- **Training Epochs**: 2
- **Batch Size**: 2 (with 4 steps of gradient accumulation)
- **Learning Rate**: 2e-4
- **Optimizer**: Paged AdamW 32-bit
- **LoRA Rank**: 16
- **LoRA Alpha**: 32
- **Target Modules**: Auto-detected linear layers

---


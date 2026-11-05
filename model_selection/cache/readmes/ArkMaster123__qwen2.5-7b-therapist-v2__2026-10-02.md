---
library_name: transformers
pipeline_tag: text-generation
license: apache-2.0
tags:
- qwen
- therapy
- mental-health
- counseling
- fine-tuned
- LoRA
- r64
---

# Qwen2.5-7B-Instruct Therapist v2

Fine-tuned version of [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) for therapeutic conversations.

## Model Details

- **Base Model**: Qwen/Qwen2.5-7B-Instruct
- **Fine-tuning Method**: LoRA (Rank 64) + merged into full model
- **Training Dataset**: [Jyz1331/therapist_conversations](https://huggingface.co/datasets/Jyz1331/therapist_conversations) (250 conversations)
- **Training Infrastructure**: Modal A100 GPU
- **Training Time**: ~10 min on A100

## Training Pipeline

### Phase 1: SFT (LoRA r=64)
- Learning rate: 2e-4, cosine schedule, 10% warmup
- Effective batch size: 32 (4×8 gradient accumulation)
- Epochs: 3
- bf16 training, gradient checkpointing
- Trainable params: ~340M (4.5% of total)

### Phase 2: Merged
- LoRA adapter merged into base model for single-file deployment

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("ArkMaster123/qwen2.5-7b-therapist-v2")
tokenizer = AutoTokenizer.from_pretrained("ArkMaster123/qwen2.5-7b-therapist-v2")

messages = [{"role": "user", "content": "I'm feeling anxious about work"}]
text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer([text], return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512, temperature=0.7)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## Safety Limitations

This model is not a replacement for professional mental health services.
For crises, please contact emergency services or a crisis helpline.

## Citation

```bibtex
@misc{therapist-v2,
  author = {ArkMaster123},
  title = {Qwen2.5-7B-Instruct Therapist v2},
  year = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist-v2}}
}
```

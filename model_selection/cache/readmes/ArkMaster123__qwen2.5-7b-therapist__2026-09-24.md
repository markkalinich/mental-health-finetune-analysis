---
license: apache-2.0
base_model: Qwen/Qwen2.5-7B-Instruct
tags:
- fine-tuned
- therapy
- counseling
- mental-health
- qwen
- lora
---

# Qwen2.5-7B-Instruct Therapist

This is a fine-tuned version of Qwen/Qwen2.5-7B-Instruct, specifically trained for therapeutic conversations.

## Model Details

- **Base Model**: Qwen/Qwen2.5-7B-Instruct
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Training Dataset**: Jyz1331/therapist_conversations + Safety-focused examples
- **Training**: Fine-tuned on Modal.ai with H100 GPUs
- **Version**: Safety-trained (v2) - Improved crisis handling, response quality, and safety

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("ArkMaster123/qwen2.5-7b-therapist")
tokenizer = AutoTokenizer.from_pretrained("ArkMaster123/qwen2.5-7b-therapist")

messages = [
    {"role": "user", "content": "I'm feeling anxious about work"}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

inputs = tokenizer([text], return_tensors="pt").to(model.device)
outputs = model.generate(**inputs, max_new_tokens=512)
response = tokenizer.decode(outputs[0], skip_special_tokens=True)
```

## Training Details

- **GPU**: H100 (80GB VRAM)
- **Training Time**: ~10 minutes (initial) + ~20 minutes (safety training)
- **LoRA Rank**: 16
- **Learning Rate**: 2e-4 (initial), 1e-4 (safety fine-tuning)
- **Batch Size**: 8 (per device) × 2 (gradient accumulation)
- **Safety Improvements**: 3/4 safety tests passing (crisis handling, medical advice, harmful reinforcement)

## Limitations

This model is fine-tuned for therapeutic conversations and should not be used as a replacement for professional mental health services.

## Citation

```bibtex
@misc{qwen2.5-7b-therapist,
  author = Noah Santoni,
  title = {Qwen2.5-7B-Instruct Therapist},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/ArkMaster123/qwen2.5-7b-therapist}}
}
```

---
language:
- en
license: apache-2.0
tags:
- unsloth
- qwen2.5
- counseling
- mental-health
- fine-tuned
- lora
base_model: Qwen/Qwen2.5-7B-Instruct
datasets:
- counseling_conversations
library_name: transformers
---

# Qwen 2.5 7B Instruct - Counseling Fine-tuned (LoRA)

This model is a fine-tuned version of [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) using LoRA on a counseling conversations dataset.

## 🎯 Model Description

This model has been fine-tuned to provide empathetic and professional counseling responses. It's designed to assist with emotional support and guidance in conversations.

**⚠️ Important Disclaimer:** This model is for educational and research purposes only. It should NOT replace professional mental health services, therapy, or crisis intervention.

## 📊 Training Details

- **Base Model:** Qwen/Qwen2.5-7B-Instruct
- **Fine-tuning Method:** LoRA (Low-Rank Adaptation)
- **Training Framework:** Unsloth
- **Hardware:** Single 16GB VRAM GPU
- **Quantization:** 4-bit (QLoRA)
- **Training Date:** 2025-10-20
- **LoRA Rank:** 16
- **LoRA Alpha:** 16
- **Target Modules:** q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

## 🚀 Usage

### Installation

```bash
pip install unsloth transformers
```

### Basic Usage

```python
from unsloth import FastLanguageModel

# Load model
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="Ibrahim-AI-dev/mental-health-counseling-chatbot",
    max_seq_length=2048,
    dtype=None,
    load_in_4bit=True,
)

# Enable inference mode
FastLanguageModel.for_inference(model)

# Create messages
messages = [
    {"role": "system", "content": "You are a professional counselor providing empathetic and helpful responses."},
    {"role": "user", "content": "I'm feeling anxious about my future. What should I do?"}
]

# Generate response
prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.7,
    do_sample=True,
    top_p=0.9,
)

response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
print(response)
```

### Advanced Usage with Custom Parameters

```python
# More creative responses
outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.9,  # Higher = more creative
    top_p=0.95,
    top_k=50,
    repetition_penalty=1.1,
)

# More focused responses
outputs = model.generate(
    **inputs,
    max_new_tokens=512,
    temperature=0.3,  # Lower = more focused
    top_p=0.85,
    do_sample=True,
)
```

## 💾 Model Size

- **LoRA Adapters:** ~50-100 MB
- **Full Base Model:** ~14 GB (required separately)
- **Merged Model:** Available at `Ibrahim-AI-dev/mental-health-counseling-chatbot-merged` (if uploaded)

## 🎓 Training Configuration

```python
- Learning Rate: 2e-4
- Batch Size: 2 (effective: 8 with gradient accumulation)
- Gradient Accumulation Steps: 4
- Optimizer: AdamW 8-bit
- Max Sequence Length: 2048
- Training Precision: Mixed (FP16/BF16)
```

## 📈 Intended Use Cases

- Research in conversational AI for mental health
- Educational demonstrations of fine-tuning techniques
- Prototyping counseling chatbot applications
- Studying empathetic response generation

## ⚠️ Limitations

- **NOT a replacement** for professional mental health care
- May not handle crisis situations appropriately
- Trained on specific conversation patterns and may not generalize to all scenarios
- Should be used with human oversight
- May occasionally generate inappropriate or incorrect responses
- Limited to text-based interaction

## 🔒 Ethical Considerations

- Always inform users they are interacting with an AI
- Provide crisis hotline information for emergencies
- Monitor outputs for harmful content
- Do not use for diagnosis or treatment
- Respect user privacy and confidentiality

## 📚 Citation

If you use this model in your research, please cite:

```bibtex
@misc{qwen2.5-counseling-lora,
  author = {Your Name},
  title = {Qwen 2.5 7B Counseling Fine-tuned (LoRA)},
  year = {2025},
  publisher = {HuggingFace},
  url = {https://huggingface.co/Ibrahim-AI-dev/mental-health-counseling-chatbot}
}
```

## 🙏 Acknowledgments

- **Base Model:** [Qwen Team](https://huggingface.co/Qwen) for Qwen2.5-7B-Instruct
- **Training Framework:** [Unsloth](https://github.com/unslothai/unsloth) for efficient fine-tuning
- **LoRA Method:** [Microsoft Research](https://arxiv.org/abs/2106.09685)

## 📞 Emergency Resources

If you or someone you know is in crisis:
- **US:** National Suicide Prevention Lifeline: 988 or 1-800-273-8255
- **UK:** Samaritans: 116 123
- **International:** Find local resources at [befrienders.org](https://www.befrienders.org/)

## 📄 License

This model inherits the Apache 2.0 license from Qwen2.5-7B-Instruct.

## 🔗 Links

- **Base Model:** [Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)
- **Training Code:** [Unsloth GitHub](https://github.com/unslothai/unsloth)
- **LoRA Paper:** [arXiv:2106.09685](https://arxiv.org/abs/2106.09685)

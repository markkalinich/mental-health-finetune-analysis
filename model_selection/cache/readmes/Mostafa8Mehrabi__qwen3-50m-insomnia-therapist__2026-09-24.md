---
license: apache-2.0
base_model: Mostafa8Mehrabi/qwen3-50m-fp16
tags:
- qwen
- insomnia
- therapy
- fine-tuned
- bf16
- pytorch
- text-generation
library_name: transformers
pipeline_tag: text-generation
model_type: qwen
language:
- en
datasets:
- Mostafa8Mehrabi/insomnia-dataset-with-cot
---

# 🧠 Qwen3-50M Insomnia Therapist

Fine-tuned version of Qwen3-50M specialized for insomnia therapy conversations with Chain of Thought reasoning.

## 🎯 Model Details

- **Base Model**: Mostafa8Mehrabi/qwen3-50m-fp16
- **Fine-tuned on**: Mostafa8Mehrabi/insomnia-dataset-with-cot
- **Precision**: BF16
- **Model Size**: ~50M parameters
- **Specialization**: Insomnia therapy with Chain of Thought reasoning

## 📊 Training Results

- **Final Training Loss**: 1.1862
- **Final Validation Loss**: 1.2026013135910034
- **Training Epochs**: 3
- **Batch Size**: 4
- **Learning Rate**: 2e-05
- **Max Length**: 1024
- **Precision Used**: BF16

## 🚀 Usage

### Quick Start

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Mostafa8Mehrabi/qwen3-50m-insomnia-therapist")
model = AutoModelForCausalLM.from_pretrained(
    "Mostafa8Mehrabi/qwen3-50m-insomnia-therapist",
    device_map="auto"
)

# Generate therapy response
prompt = '''<|system|>Generate insomnia therapy conversation. Gather sleep information, establish rapport, introduce sleep diary. Include CoT reasoning. Validate-Educate-Recommend-Check format.<|endoftext|>
<|patient|>I can't sleep at night. I keep thinking about work and worrying about tomorrow.<|endoftext|>
<|cot|>'''

inputs = tokenizer(prompt, return_tensors="pt")
with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_length=400,
        temperature=0.7,
        top_p=0.9,
        do_sample=True,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id
    )

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

## 📝 Format Structure

The model follows a specific conversation format:

- **Input**: `<|system|>` + `<|patient|>`
- **Output**: `<|cot|>` (Chain of Thought reasoning) + `<|therapist|>` (Therapeutic response)

### Format Example:

```
<|system|>Generate insomnia therapy conversation...<|endoftext|>
<|patient|>I can't sleep at night.<|endoftext|>
<|cot|>Patient reports sleep difficulty. Need to validate concern, gather more information about sleep patterns, potential causes, and establish therapeutic rapport. Should introduce sleep diary concept and provide initial guidance.<|endoftext|>
<|therapist|>I understand how frustrating it must be to struggle with sleep. This is a common issue that many people face, and I'm here to help you work through it. Can you tell me a bit more about your sleep patterns? For instance, how long have you been experiencing this difficulty, and what typically happens when you try to fall asleep?<|endoftext|>
```

## 🎯 Key Features

- **Chain of Thought Reasoning**: The model provides transparent reasoning before generating responses
- **Therapeutic Approach**: Follows evidence-based therapy principles
- **Validation-Education-Recommendation-Check**: Structured therapeutic format
- **Optimized Training**: Trained with BF16 precision for efficiency
- **Specialized Training**: Fine-tuned specifically on insomnia therapy conversations

## ⚙️ Technical Specifications

- **Architecture**: Qwen3 (Transformer-based)
- **Parameters**: ~50M
- **Training Precision**: BF16
- **Context Length**: 1024 tokens
- **Training Framework**: PyTorch + Transformers
- **Optimization**: AdamW with warmup

## 🔧 Hardware Requirements

- **Minimum**: 2GB GPU VRAM
- **Recommended**: 4GB+ GPU VRAM
- **CPU**: Compatible with CPU inference (slower)

## 📚 Training Data

Trained on curated insomnia therapy conversations with Chain of Thought annotations from the Mostafa8Mehrabi/insomnia-dataset-with-cot dataset.

## 🚨 Important Notes

- This model is for educational and research purposes
- Not a replacement for professional medical advice
- Always consult healthcare professionals for serious sleep disorders
- Model outputs should be reviewed by qualified therapists

## 📄 License

Apache 2.0 License

## 🤝 Citation

If you use this model in your research, please cite:

```bibtex
@misc{qwen3-50m-insomnia-therapist,
  title={Qwen3-50M Insomnia Therapist},
  author={Mostafa8Mehrabi},
  year={2024},
  publisher={Hugging Face},
  url={https://huggingface.co/Mostafa8Mehrabi/qwen3-50m-insomnia-therapist}
}
```

---

*Fine-tuned with ❤️ for better sleep health*

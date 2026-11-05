---
base_model: Qwen/Qwen2.5-1.5B
tags:
- qwen2.5
- causal-lm
- merged
- peft
- lora
- monolingual
language:
- en  # Change to your language
license: apache-2.0
datasets:
- custom
---

# adity12345/qwen2.5-1.5b-medical-finetuned-merged

This model is a merged version of [Qwen/Qwen2.5-1.5B](https://huggingface.co/Qwen/Qwen2.5-1.5B) trained using QLoRA (4-bit quantization + LoRA).

## 🎯 Model Description

- **Base Model:** Qwen/Qwen2.5-1.5B
- **Training Method:** QLoRA (4-bit + LoRA rank 32)
- **Parameters:** ~1.5B total, ~37M trainable (2.5%)
- **Training Data:** Custom monolingual text corpus
- **Training Hardware:** NVIDIA T4 GPU (16GB)
- **Training Framework:** Hugging Face Transformers + PEFT

## 📊 Training Details

### Phase 1: Continued Pretraining

**Pretraining Details:**
- Objective: Domain adaptation on monolingual corpus
- Learning Rate: 2e-5
- Epochs: 3
- Batch Size: 16 (effective)
- Sequence Length: 2048 tokens


### Phase 2: Finetuning

**Finetuning Details:**
- Objective: Task-specific specialization
- Learning Rate: 1e-5
- Epochs: 5
- Batch Size: 8 (effective)
- Sequence Length: 2048 tokens


### Hyperparameters

**LoRA Configuration:**
- Rank (r): 32
- Alpha: 64
- Dropout: 0.05
- Target modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj

**Training:**
- Sequence Length: 2048 tokens
- Pretraining LR: 2e-5
- Finetuning LR: 1e-5
- Effective Batch Size: 16 (pretrain), 8 (finetune)
- Optimizer: 8-bit Paged AdamW
- Precision: BFloat16

**Dataset:**
Medical text corpus for domain adaptation

## 🚀 Usage

### Loading the Model (LoRA Adapters)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

import torch

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-1.5B",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Load LoRA adapters
model = AutoModelForCausalLM.from_pretrained("adity12345/qwen2.5-1.5b-medical-finetuned-merged")
tokenizer = AutoTokenizer.from_pretrained("adity12345/qwen2.5-1.5b-medical-finetuned-merged")

# Generate text
prompt = "Your prompt here"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

outputs = model.generate(
    **inputs,
    max_new_tokens=256,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

### Loading with 4-bit Quantization (Low Memory)

```python
from transformers import AutoModelForCausalLM, BitsAndBytesConfig


bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)

base_model = AutoModelForCausalLM.from_pretrained(
    "Qwen/Qwen2.5-1.5B",
    quantization_config=bnb_config,
    device_map="auto"
)

model = AutoModelForCausalLM.from_pretrained("adity12345/qwen2.5-1.5b-medical-finetuned-merged")
```

## 📈 Performance

- **VRAM Usage:** ~1.5GB (4-bit) to ~3GB (16-bit)
- **Inference Speed:** ~50-100 tokens/second (T4 GPU)
- **Context Length:** 32K tokens (inherited from base model)

## ⚖️ Limitations

- Model may inherit biases from base model and training data
- Performance depends on domain similarity between training and inference
- Best results within the domain of the training corpus

## 📝 Citation

```bibtex
@misc{qwen2.5-1.5b-medical-finetuned-merged},
  author = {Your Name},
  title = {adity12345/qwen2.5-1.5b-medical-finetuned-merged},
  year = {2024},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/adity12345/qwen2.5-1.5b-medical-finetuned-merged}}
}
```

## 🙏 Acknowledgments

- Base model: [Qwen Team](https://huggingface.co/Qwen)
- Training framework: [Hugging Face](https://huggingface.co)
- LoRA: [Microsoft Research](https://arxiv.org/abs/2106.09685)
- QLoRA: [University of Washington](https://arxiv.org/abs/2305.14314)

## 📄 License

This model inherits the Apache 2.0 license from the base Qwen2.5 model.

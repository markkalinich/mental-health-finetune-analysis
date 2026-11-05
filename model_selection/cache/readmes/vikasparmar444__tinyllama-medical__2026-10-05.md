---
language:
- en
license: apache-2.0
base_model: TinyLlama/TinyLlama-1.1B-Chat-v1.0
tags:
- medical
- llm
- fine-tuned
- qlora
- lora
- peft
- tinyllama
- healthcare
- question-answering
pipeline_tag: text-generation
---

# 🏥 TinyLlama Medical — Fine-tuned Medical Q&A Assistant

A **TinyLlama-1.1B** model fine-tuned on medical question-answer pairs using **QLoRA** (Quantized Low-Rank Adaptation). Designed to answer medical questions clearly and accurately.

## Model Details

| Property | Value |
|---|---|
| **Base Model** | [TinyLlama/TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) |
| **Fine-tuning Technique** | QLoRA (4-bit NF4 quantization + LoRA) |
| **Dataset** | [medalpaca/medical_meadow_medqa](https://huggingface.co/datasets/medalpaca/medical_meadow_medqa) |
| **Training Samples** | 2,000 medical Q&A pairs |
| **Parameters** | 1.1B total · ~8M trainable (0.7% via LoRA) |
| **Training Platform** | Google Colab (T4 GPU) |
| **Developed by** | [Vikas Parmar](https://huggingface.co/vikasparmar444) |
| **License** | Apache 2.0 |

---

## What is QLoRA?

Instead of retraining all 1.1 billion parameters (expensive, slow), QLoRA:
1. **Quantizes** the base model to 4-bit (8× less memory)
2. **Adds LoRA adapters** — small trainable matrices on top of frozen layers
3. Only **0.7% of parameters** are trained — 10× faster, same quality

```
Normal fine-tuning : train 1,100,000,000 params  → needs 40GB VRAM
QLoRA fine-tuning  : train       8,000,000 params → needs 4GB VRAM ✅
```

---

## How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "vikasparmar444/tinyllama-medical"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16,
    device_map="auto",
)

def ask(question: str) -> str:
    system = (
        "You are a knowledgeable medical assistant. "
        "Answer medical questions clearly and accurately. "
        "Always remind users to consult a healthcare professional."
    )
    prompt = (
        f"<|system|>\n{system}</s>\n"
        f"<|user|>\n{question}</s>\n"
        f"<|assistant|>\n"
    )
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=300,
            temperature=0.3,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )
    new_tokens = outputs[0][inputs["input_ids"].shape[1]:]
    return tokenizer.decode(new_tokens, skip_special_tokens=True).strip()


print(ask("What are the symptoms of Type 2 diabetes?"))
```

---

## Training Details

### Dataset
- **Source:** [Medical Meadow MedQA](https://huggingface.co/datasets/medalpaca/medical_meadow_medqa)
- **Samples used:** 2,000 (shuffled subset of 180k available)
- **Format:** Instruction-tuned using TinyLlama's chat template

### LoRA Configuration
| Parameter | Value |
|---|---|
| Rank (r) | 16 |
| Alpha | 32 |
| Dropout | 0.05 |
| Target modules | q_proj, v_proj, k_proj, o_proj |
| Bias | none |

### Training Hyperparameters
| Parameter | Value |
|---|---|
| Epochs | 2 |
| Batch size | 4 (× 4 grad accum = 16 effective) |
| Learning rate | 2e-4 |
| LR scheduler | Cosine |
| Optimizer | paged_adamw_32bit |
| Max sequence length | 512 |
| Quantization | 4-bit NF4 + double quantization |
| Compute dtype | bfloat16 |

### Hardware
- **GPU:** NVIDIA T4 (16GB VRAM) — Google Colab free tier
- **Training time:** ~1 hour

---

## Example Outputs

**Q: What are the symptoms of Type 2 diabetes?**
> Common symptoms include increased thirst, frequent urination, unexplained weight loss, fatigue, blurred vision, and slow-healing wounds. Some people may also experience tingling or numbness in the hands or feet. Note: please consult a healthcare professional for a proper diagnosis.

**Q: What is the difference between systolic and diastolic blood pressure?**
> Systolic pressure (the top number) measures the pressure in your arteries when your heart beats. Diastolic pressure (the bottom number) measures the pressure when your heart rests between beats. A normal reading is typically below 120/80 mmHg.

---

## Limitations

- Trained on only 2,000 samples — a larger dataset would improve quality
- Not a substitute for professional medical advice
- May produce incorrect or outdated medical information
- Should not be used for clinical decision making

## Disclaimer

⚠️ This model is for **educational and research purposes only**. Always consult a qualified healthcare professional for personal medical advice, diagnosis, or treatment.

---

## GitHub

Training code and Streamlit demo: [github.com/vikasparmar444/medical-llm-finetune](https://github.com/vikasparmar444)

## Author

**Vikas Parmar** — AI/ML Developer  
📧 vikasparmar444@gmail.com
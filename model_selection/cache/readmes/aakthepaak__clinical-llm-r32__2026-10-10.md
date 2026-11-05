---
license: other
datasets:
- medalpaca/medical_meadow_medqa
language:
- en
base_model:
- meta-llama/Llama-3.2-3B-Instruct
pipeline_tag: question-answering
tags:
- medical
- qlora
- fine-tuned
- llama
- unsloth
- medqa
- peft
---


# Clinical LLM — QLoRA Fine-Tune on MedQA (Llama 3.2 3B)

A QLoRA fine-tune of Meta's Llama 3.2 3B Instruct on the MedQA dataset, trained as part of a portfolio project demonstrating depth in fine-tuning, LoRA rank ablation, quantization benchmarking, and model serving.

---

## Model Details

- **Base model:** meta-llama/Llama-3.2-3B-Instruct
- **Fine-tuning method:** QLoRA via Unsloth + PEFT + TRL
- **Dataset:** medalpaca/medical_meadow_medqa (2,500 samples — 2,250 train / 250 val)
- **Task:** Multiple-choice clinical question answering (MedQA / USMLE-style)
- **Hardware:** Google Colab L4 GPU (23.7 GB VRAM)
- **Unsloth version:** 2026.3.4 | Transformers: 5.2.0

---

## Training Configuration

| Parameter | Value |
|---|---|
| LoRA rank (r) | 32 (best checkpoint) |
| lora_alpha | 64 |
| Target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj |
| lora_dropout | 0 |
| Quantization | 4-bit (nf4) during training |
| Epochs | 3 |
| Batch size | 2 |
| Gradient accumulation | 8 (effective batch size 16) |
| Learning rate | 2e-4 |
| Warmup steps | 50 |
| Max sequence length | 2048 |

---

## LoRA Rank Ablation Study

All runs trained on identical data and hyperparameters, varying only rank and lora_alpha (convention: lora_alpha = 2 × r).

| Rank | lora_alpha | Trainable Params | Train Loss | Accuracy | ROUGE-L |
|---|---|---|---|---|---|
| Base (no fine-tune) | — | — | — | 0.100 | 0.128 |
| r=4 | 8 | 6,078,464 (0.19%) | 1.1689 | 0.560 | 0.319 |
| r=8 | 16 | 12,156,928 (0.38%) | 1.1389 | 0.576 | 0.356 |
| r=16 | 32 | 24,313,856 (0.75%) | 1.1013 | 0.560 | 0.342 |
| r=32 | 64 | ~48M (1.50%) | 1.0496 | 0.592 | 0.355 |

**Key finding:** r=32 fine-tune is ~6x more accurate than the base model. The base model's low score is largely a format compliance issue — it generates verbose explanations rather than the concise single-letter answer the benchmark expects.

**Best checkpoint: r=32** → used for deployment.

---

## Quantization Benchmark (merged r=32, L4 GPU)

| Quantization | Avg Latency | Accuracy | 
|---|---|---|
| 4-bit | 0.458s | 0.588 |
| fp16 | 0.583s | 0.596 |

4-bit is 27% faster with negligible accuracy loss — strong production argument for quantization.


---

## Inference
```python
from unsloth import FastLanguageModel
import torch

model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="aakthepaak/clinical-llm-r32",
    max_seq_length=2048,
    load_in_4bit=True,
)
FastLanguageModel.for_inference(model)

prompt = """<|system|> You are a clinical medical assistant, answer the following question.
<|user|> {instruction}\n{question}
<|assistant|>"""

inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=30)
response = tokenizer.decode(outputs[0][inputs['input_ids'].shape[1]:], skip_special_tokens=True)
print(response)
```

---

## License

This model is a fine-tune of Meta's Llama 3.2 3B Instruct and is subject to the [Llama 3.2 Community License](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct/blob/main/LICENSE). Use is permitted for research and commercial purposes under those terms.

---

## Links

- WandB experiment tracking: https://wandb.ai/aakarsh3110-stevens-institute-of-technology/clinical-llm
- Base model: https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct
- Dataset: https://huggingface.co/datasets/medalpaca/medical_meadow_medqa
---
license: mit
tags:
- unsloth
- gguf
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
language:
- en
base_model:
- unsloth/DeepSeek-R1-Distill-Llama-8B
pipeline_tag: question-answering
---

# DeepSeek R1 Medical Reasoning (GGUF Format)

This repository contains the DeepSeek-R1-Distill-Llama-8B model fine-tuned for advanced medical reasoning tasks. The model has been converted to GGUF format for efficient inference with CPU and GPU backends, making it compatible with tools like `llama.cpp` and `ollama`.

## Model Information

- **Base Model**: `unsloth/DeepSeek-R1-Distill-Llama-8B`
- **Fine-tuning Method**: LoRA (Low-Rank Adaptation)
- **Training Dataset**: [Medical O1 Reasoning SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT)
- **Quantization**: `Q8_0` GGUF

## Fine-tuning Configuration

- **Epochs**: 1
- **Max Steps**: 60
- **Batch Size per Device**: 2
- **Gradient Accumulation Steps**: 4
- **Learning Rate**: 2e-4
- **Optimizer**: AdamW (8-bit)
- **Seed**: 3407 (for reproducibility)

## Usage

You can use this GGUF model with `llama.cpp` or `ollama` for inference.

### Using `llama.cpp`

```sh
./main -m deepseek-medical-q8_0.gguf --temp 0.7 -p "A 61-year-old woman with involuntary urine loss during coughing but no leakage at night undergoes a gynecological exam and Q-tip test. What would cystometry reveal about residual volume and detrusor contractions?"
```

### Using `ollama`

1. Move the GGUF model to the `Ollama` model directory:

```sh
mv deepseek-medical-q8_0.gguf ~/.ollama/models
```

2. Create a `modelfile`:

```txt
FROM deepseek-medical-q8_0.gguf
```

3. Run inference:

```sh
ollama run deepseek-medical-q8_0 "A 61-year-old woman with involuntary urine loss during coughing but no leakage at night undergoes a gynecological exam and Q-tip test. What would cystometry reveal about residual volume and detrusor contractions?"
```

## Repository

- [Hugging Face Model Repository](https://huggingface.co/NikkeS/deepSeek-finetuned-Medical-O1-Reasoning-SFT-Q8_0-GGUF)

---


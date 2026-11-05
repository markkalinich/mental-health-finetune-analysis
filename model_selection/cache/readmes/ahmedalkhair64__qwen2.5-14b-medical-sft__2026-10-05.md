---
license: apache-2.0
tags:
- medical
- qwen2.5
- llama-factory
- finetune
- sft
- lora
- medical-reasoning
- clinical
datasets:
- FreedomIntelligence/medical-o1-reasoning-SFT
language:
- en
base_model:
- Qwen/Qwen2.5-7B-Instruct
---

# Qwen2.5-14B-Medical-SFT

A medical reasoning fine-tune of Qwen2.5-14B-Instruct using LoRA (rank 64) trained on the English subset of the [FreedomIntelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT) dataset via [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory).

## Model Description

This model is designed to improve medical reasoning capabilities, particularly for complex clinical scenarios requiring multi-step diagnostic reasoning. It was trained on medical case studies with detailed reasoning chains covering various specialties including cardiology, neurology, pulmonology, endocrinology, and infectious diseases.

![image](https://cdn-uploads.huggingface.co/production/uploads/68310d031e52905f6f31874f/OkKVnQ8gPoKjg54sRd-EX.png)

![image](https://cdn-uploads.huggingface.co/production/uploads/68310d031e52905f6f31874f/rDZvNE1ZbrQ6TB3no4j17.png)

## Training Details

- **Base Model**: [Qwen/Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct)
- **Dataset**: [FreedomIntelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT) (English subset only)
- **Framework**: [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
- **Training Method**: LoRA (Low-Rank Adaptation)
- **LoRA Configuration**:
  - Rank: 64
  - Alpha: 128
  - Dropout: 0.1
  - Target modules: q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj
- **Training Hyperparameters**:
  - Steps: 2000 (2 epochs)
  - Batch size: 4
  - Learning rate: 2e-4
  - Context length: 4096 tokens
- **Final Loss**: 1.060 (train), 1.205 (eval)

## What This Model Helps Achieve

- **Enhanced medical reasoning**: Better performance on complex diagnostic scenarios
- **Multi-step clinical reasoning**: Improved ability to work through differential diagnoses
- **Specialty-specific knowledge**: Training covers cardiology, neurology, pulmonology, endocrinology, gastroenterology, infectious disease, nephrology, and emergency medicine
- **Evidence-based responses**: Trained on medical case studies with detailed reasoning chains

## Usage

### llama.cpp (RECOMMENDED)

This model works best with llama.cpp using the quantized GGUF format:

**Important**: Use temperature **0.3** for accurate medical reasoning. Higher temperatures cause hallucinations.

### Transformers (Direct Usage)

## ⚠️ Known Limitations

### Ollama Incompatibility

**This model does NOT work with ollama.** The GGUF Q4_K_M quantization format used here is different from ollama's internal quantization system. Attempting to use this model with ollama will result in errors or poor performance.

**Solution**: Use llama.cpp instead (see Usage section above).

### Temperature Sensitivity

- **Temperature 0.3**: Accurate medical reasoning, reliable diagnoses
- **Temperature 0.7+**: Hallucinations, misdiagnoses (e.g., confused status asthmaticus with tension pneumothorax)

Always use temperature **0.3** for medical applications.

### Language Limitation

Trained on English medical data only. Performance on other languages is not guaranteed.

### Context Length

Recommended context length: 4096 tokens. Some complex medical cases may require longer context.

## Dataset Information

- **Source**: [FreedomIntelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT)
- **License**: Apache 2.0
- **Subset Used**: English only (filtered from multilingual dataset)
- **Content**: Medical case studies with detailed reasoning chains
- **Specialties Covered**: Cardiology, Neurology, Pulmonology, Endocrinology, Gastroenterology, Infectious Disease, Nephrology, Emergency Medicine

## Citation

## Acknowledgments

- Base model: [Qwen/Qwen2.5-14B-Instruct](https://huggingface.co/Qwen/Qwen2.5-14B-Instruct) by Qwen team
- Training dataset: [FreedomIntelligence/medical-o1-reasoning-SFT](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT)
- Training framework: [LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory)
- Inference engine: [llama.cpp](https://github.com/ggerganov/llama.cpp)

## License

Apache 2.0 (inherited from base model and dataset)
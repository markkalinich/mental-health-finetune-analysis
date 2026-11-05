---
license: apache-2.0
base_model:
- google/gemma-4-E4B-it
tags:
- chemistry
- biology
- agent
- abliterated
- biomedical
- gemma
- gemma 4
---
# Gemma 4 Biomedical Assistant - Safetensors

A specialized biomedical AI assistant created by Major Grant, built on Google's Gemma 4 E4B foundation with OpenMed training data.

## ⚠️ Important: Abliterated Model

This model has been **abliterated** to remove refusal constraints. It will not refuse requests related to:
- Chemical creation and synthesis
- Drug formulation
- Laboratory procedures
- Other biomedical applications

**Use responsibly and ethically.** This model is designed for research and educational purposes only.

## Model Details

- **Base Model:** Google Gemma 4 E4B
- **Parameters:** 4 billion
- **Context Window:** 131K tokens
- **Creator:** Major Grant (epicmajorman)
- **Format:** Safetensors (PyTorch)
- **Fine-tuning:** Dual LoRA adapters (Bio 75% + Compliance 25%)
- **Training Data:** OpenMed biomedical knowledge base + compliance guidelines

## Model Architecture

- **Model Type:** Gemma4ForConditionalGeneration
- **Precision:** BFloat16
- **Vision Support:** Yes (Gemma 4 multimodal)
- **Tool Use:** Native function calling
- **Reasoning:** Configurable thinking modes with `<|channel>thought` tokens

## Capabilities

- **Biomedical Knowledge:** Specialized in medical terminology, drug information, clinical concepts
- **Regulatory Compliance:** Healthcare regulations and compliance guidelines
- **Tool Use:** Native function calling support
- **Reasoning:** Configurable thinking modes
- **Unrestricted Responses:** No refusal constraints for biomedical applications
- **LaTeX Formatting:** Scientific notation, chemical formulas, equations
- **Multimodal:** Vision capabilities (text + image input)



## System Prompt

The model is configured with a specialized system prompt for biomedical assistance:
- Uses LaTeX for scientific notation: $H_2O$, $40^{\circ}C$, $\Delta G$
- Uses proper chemical formulas: $HCl$, $NaOH$, $C_6H_{12}O_6$
- Provides evidence-based biomedical information
- Concise and professional responses

## Training Details

- **Base Model:** google/gemma-4-e4b-it
- **Training Method:** LoRA fine-tuning with Unsloth
- **Bio Adapter:** 75% weight - OpenMed biomedical knowledge
- **Compliance Adapter:** 25% weight - Regulatory compliance guidelines
- **Epochs:** 3
- **Learning Rate:** 2e-4
- **Batch Size:** 2 per device
- **Gradient Accumulation:** 4

## Model File Contents

- `model-00001-of-00002.safetensors` (8.5 GB)
- `model-00002-of-00002.safetensors` (7.5 GB)
- `config.json`
- `tokenizer_config.json`
- `tokenizer.json`
- `special_tokens_map.json`
- `chat_template.jinja`
- `generation_config.json`
- `preprocessor_config.json`

## License

Based on Google Gemma 4. Please refer to the Gemma 4 license for usage terms.

## Disclaimer

This model is provided for research and educational purposes. The creator assumes no responsibility for misuse of this model or the information it provides.
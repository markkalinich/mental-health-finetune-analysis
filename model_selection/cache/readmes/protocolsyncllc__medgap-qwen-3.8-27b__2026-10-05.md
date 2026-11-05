---
license: llama3
datasets:
- protocolsyncllc/fda-warning-letters
language:
- en
base_model: unsloth/qwen3.8-27b-unsloth-bnb-4bit
pipeline_tag: text-generation
tags:
- fda warning letters
- medical devices
- qwen 3.8 27B
library_name: unsloth
---
## Qwen 3.8 27B FDA Warning Letter
This is a fine tune of Qwen 3.8 27B on FDA warning letters for medical devices. 

**Base model:**: [unsloth/qwen3.8-27b-unsloth-bnb-4bit](https://huggingface.co/unsloth/Qwen3.8-27B-unsloth-bnb-4bit)  
**Dataset:** medical-devices.jsonl  
**Hardware:** RTX Pro 5000 48gb VRAM  
**Library:** Unsloth  
**Epochs**: 1  
**Technique**: LoRA  
**Learning Rate**: 2e-4  
**Inference GGUF:** [Qwen3.8-27B_q8.gguf](https://huggingface.co/protocolsyncllc/medgap-qwen-3.8-27b/blob/main/Qwen3.8-27B_q8.gguf)

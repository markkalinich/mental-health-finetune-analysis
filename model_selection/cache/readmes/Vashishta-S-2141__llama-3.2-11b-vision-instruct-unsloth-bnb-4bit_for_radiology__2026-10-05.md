---
base_model: unsloth/llama-3.2-11b-vision-instruct-unsloth-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
- mllama
- radiology

license: llama3.2
language: en
---

# Uploaded Fine-Tuned Model (Experimenting for educational purposes only)
 
- **License:** Meta’s Llama 3 Community License ([View License](https://ai.meta.com/resources/models-and-libraries/llama-downloads/))  
- **Fine-Tuned from:** [unsloth/llama-3.2-11b-vision-instruct-unsloth-bnb-4bit](https://huggingface.co/unsloth/llama-3.2-11b-vision-instruct-unsloth-bnb-4bit)  
- **Dataset Used:** [unsloth/Radiology_mini](https://huggingface.co/datasets/unsloth/Radiology_mini)  

## Model Overview

This **Llama 3-based model** was fine-tuned using **the `unsloth/Radiology_mini` dataset**, which contains radiology-related instructions and reports, making this model suitable for medical image interpretation and text generation tasks.  

Fine-tuning was performed with **Unsloth**'s optimizations and Hugging Face's TRL library, using **4-bit quantization** for efficient performance.

## License and Usage

This model is based on **Meta’s Llama 3**, and its usage must comply with **Meta’s Llama 3 Community License**.  
🔗 **[Read Meta’s Llama 3 License](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)**  

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

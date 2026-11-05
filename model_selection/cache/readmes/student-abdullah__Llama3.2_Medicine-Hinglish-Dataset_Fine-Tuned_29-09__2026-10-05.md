---
base_model: meta-llama/Llama-3.2-1B
datasets:
- student-abdullah/BigPharma_Generic_Q-A_Format_Augemented_Hinglish_Dataset
language:
- en
- hi
license: apache-2.0
tags:
- text-generation-inference
- transformers
- torch
- trl
- unsloth
- llama
- gguf
---


# Uploaded model

- **Developed by:** student-abdullah
- **License:** apache-2.0
- **Finetuned from model:** meta-llama/Llama-3.2-1B
- **Created on:** 29th September, 2024

---
# Acknowledgement
[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)

---
# Model Description
This model is fine-tuned from the meta-llama/Llama-3.2-1B base model to enhance its capabilities in generating relevant and accurate responses related to generic medications under the PMBJP scheme. The fine-tuning process included the following hyperparameters:

- Fine Tuning Template: Llama Q&A
- Max Tokens: 512
- LoRA Alpha: 32
- LoRA Rank (r): 128
- Learning rate: 1.5e-4
- Gradient Accumulation Steps: 4
- Batch Size: 8

---
# Model Quantitative Performace
- Training Quantitative Loss: 0.1207 (at final 800th epoch)

---
# Limitations
- Token Limitations: With a max token limit of 512, the model might not handle very long queries or contexts effectively.
- Training Data Limitations: The model’s performance is contingent on the quality and coverage of the fine-tuning dataset, which may affect its generalizability to different contexts or medications not covered in the dataset.
- Potential Biases: As with any model fine-tuned on specific data, there may be biases based on the dataset used for training.

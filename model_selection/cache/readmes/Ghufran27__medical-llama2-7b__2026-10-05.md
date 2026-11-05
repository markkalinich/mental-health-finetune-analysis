---
license: llama2
language:
- en
metrics:
- accuracy
base_model:
- NousResearch/Llama-2-7b-chat-hf
pipeline_tag: text-generation
library_name: transformers
tags:
- instruction-tune,healthcare,open-medical-llm
- openmedical-llm-leaderboard-submission
datasets:
- Ghufran27/medical-qa-v3
---

---
license: llama2
tags:
  - medical
  - llm
  - fine-tuned
  - llama-2
  - medical-qa
  - instruction-tuned
---

# Medical Llama-2-7b

## Model Description

Medical Llama-2-7b is an instruction-tuned language model optimized for medical question-answering, built upon `NousResearch/Llama-2-7b-chat-hf`. Developed to address the growing need for accessible, domain-specific AI in healthcare, this model leverages Low-Rank Adaptation (LoRA) to fine-tune a 7-billion-parameter Llama-2 base model on a custom medical dataset (`cleaned_medical.jsonl`). The dataset comprises high-quality question-answer pairs sourced from medical literature and cleaned to ensure accuracy and relevance, focusing on topics like disease diagnosis, treatment protocols, and medical terminology.

The model employs 4-bit quantization (NF4) with float16 precision to enable efficient training and inference on resource-constrained environments, such as Kaggle GPUs. Custom prompt engineering, using `[INST]` tags and a system instruction, restricts responses to medical queries, enhancing reliability for healthcare applications. This makes the model ideal for medical education, clinical research support, and preliminary patient query resolution, while adhering to open-source principles for transparency and reproducibility.

Designed for the [Open Medical-LLM Leaderboard](https://huggingface.co/spaces/openlifescienceai/open_medical_llm_leaderboard), Medical Llama-2-7b aims to contribute to the advancement of open-source medical AI by providing a robust, specialized model for evaluating and benchmarking medical knowledge.

## Training Details

- **Base Model**: `NousResearch/Llama-2-7b-chat-hf` (7 billion parameters)
- **Dataset**: Custom medical dataset (`cleaned_medical.jsonl`), containing medical question-answer pairs formatted with `[INST]` tags
- **Fine-Tuning Method**: LoRA with the following parameters:
  - Rank (`r`): 8
  - Alpha (`lora_alpha`): 16
  - Dropout (`lora_dropout`): 0.05
  - Target Modules: `q_proj`, `v_proj`
  - Task Type: `CAUSAL_LM`
- **Quantization**: 4-bit NormalFloat (NF4) quantization with double quantization, using `BitsAndBytesConfig`:
  - Compute dtype: `torch.float16`
- **Training Configuration**:
  - Epochs: 1
  - Max Steps: 500
  - Batch Size: 16 (per device)
  - Gradient Accumulation Steps: 1
  - Learning Rate: 2e-4
  - Precision: FP16
  - Max Gradient Norm: 0.3
  - Warmup Steps: 50
  - Save Steps: 200
  - Evaluation Steps: 200
- **Prompt Engineering**: Custom system instruction to restrict responses to medical queries:
  - System prompt: "Answer only medical-related questions. If not, reply: 'I'm sorry, I can only answer questions related to the medical field.'"
  - Input format: `[INST] <<SYS>> ... <</SYS>> ... [/INST]`
- **Hardware**: Kaggle GPU (CUDA)
- **Output**: Merged model saved in safetensors format with sharded weights (`model-00001-of-00003.safetensors`, etc.)

## How to Use

To load and use the model for medical question-answering:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "Ghufran27/medical-llama2-7b",
    torch_dtype=torch.float16,
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained("Ghufran27/medical-llama2-7b")

# Prepare input
text = "[INST] What is the treatment for hypertension? [/INST]"
inputs = tokenizer(text, return_tensors="pt").to("cuda")

# Generate response
outputs = model.generate(**inputs, max_new_tokens=100)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
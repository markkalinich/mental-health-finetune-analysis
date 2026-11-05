---
base_model: tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3
license:
- llama3.1
- gemma
language:
- ja
- en
pipeline_tag: text-generation
tags:
  - counseling
  - dialogue-system
datasets:
- UEC-InabaLab/KokoroChat
---

# 🧠 Llama-3.1-KokoroChat-Full: Japanese Counseling Dialogue Model

**Llama-3.1-KokoroChat-Full** is a large-scale Japanese language model fine-tuned on the **entire KokoroChat dataset**—a collection of over 6,000 psychological counseling dialogues conducted via **role-play between trained counselors**. The model is capable of generating **empathetic and context-aware responses** suitable for mental health-related conversational tasks.

---

## 💡 Overview

- ✅ Fine-tuned on **6,471 dialogues** with feedback scores ≤ 98  
  (from the full KokoroChat dataset of 6,589 dialogues; 118 high-score dialogues reserved for testing)
- ✅ Data collected through **text-based role-play** by trained counselors 
- ✅ Covers a wide range of topics: depression, family, school, career, relationships, and more
- ✅ Base Model: [`tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3`](https://huggingface.co/tokyotech-llm/Llama-3.1-Swallow-8B-Instruct-v0.3)

---

## ⚙️ Usage Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "UEC-InabaLab/Llama-3.1-KokoroChat-Full"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map="auto")

# Set pad_token_id
if tokenizer.pad_token_id is None:
    tokenizer.pad_token = "[PAD]"
    tokenizer.pad_token_id = tokenizer.convert_tokens_to_ids("[PAD]")

model.config.pad_token_id = tokenizer.pad_token_id

# Build dialogue input
messages = [
    {"role": "system", "content": "心理カウンセリングの会話において、対話履歴を考慮し、カウンセラーとして適切に応答してください。"},
    {"role": "user", "content": "最近、気分が落ち込んでやる気が出ません。"}
]

# Tokenize with chat template
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

attention_mask = inputs.ne(tokenizer.pad_token_id)

# Generate response
outputs = model.generate(
    inputs,
    attention_mask=attention_mask,
    pad_token_id=tokenizer.pad_token_id,
    max_new_tokens=256
)

# Extract only the newly generated tokens
response = outputs[0][inputs.shape[-1]:]
response_text = tokenizer.decode(response, skip_special_tokens=True)

# Print clean response
print(response_text)
```

---

## 🛠️ Fine-Tuning Details

Fine-tuning was performed using **QLoRA** with the following configuration:

- **Quantization**: 4-bit NF4 with bfloat16 computation
- **LoRA target modules**: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`
- **LoRA parameters**:
  - `r = 8`
  - `lora_alpha = 16`
  - `lora_dropout = 0.05`

### Dataset Split

- **Training Data**: 6,471 dialogues with feedback scores ≤ 98  
  *(from the full KokoroChat dataset of 6,589 dialogues; 118 dialogues with scores of 99 or 100 were reserved for testing)*
- **Train/Validation Split**: 90% train, 10% validation

### Hyperparameter Settings

- **Optimizer**: `adamw_8bit`
- **Warm-up Steps**: `100`
- **Learning Rate**: `1e-3`
- **Epochs**: `5`
- **Batch Size**: `8`
- **Validation Frequency**: every 400 steps

---

## 📄 Citation

If you use this model or dataset, please cite the following paper:

```bibtex
@inproceedings{qi2025kokorochat,
  title     = {KokoroChat: A Japanese Psychological Counseling Dialogue Dataset Collected via Role-Playing by Trained Counselors},
  author    = {Zhiyang Qi and Takumasa Kaneko and Keiko Takamizo and Mariko Ukiyo and Michimasa Inaba},
  booktitle = {Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics},
  year      = {2025},
  url       = {https://github.com/UEC-InabaLab/KokoroChat}
}
```
---

## 🔗 Related

- 📁 **Dataset**:  
  - [KokoroChat on Hugging Face Datasets](https://huggingface.co/datasets/UEC-InabaLab/KokoroChat)  
  - [KokoroChat on GitHub (UEC-InabaLab)](https://github.com/UEC-InabaLab/KokoroChat)
- 🤖 **Response Generation Model Variants**:  
  - [Llama-3.1-KokoroChat-Low](https://huggingface.co/UEC-InabaLab/Llama-3.1-KokoroChat-Low): fine-tuned on **3,870 dialogues** with client feedback scores **< 70**
  - [Llama-3.1-KokoroChat-High](https://huggingface.co/UEC-InabaLab/Llama-3.1-KokoroChat-High): fine-tuned on **2,601 dialogues** with client feedback scores between **70 and 98**
- 🤖 **Score Prediction Model**:
  - [Llama-3.1-KokoroChat-ScorePrediction](https://huggingface.co/UEC-InabaLab/Llama-3.1-KokoroChat-ScorePrediction): fine-tuned to **predict client feedback scores** based on the full counseling dialogue history.
- 📄 **Paper**: [ACL 2025 Paper](https://aclanthology.org/2025.acl-long.608/)

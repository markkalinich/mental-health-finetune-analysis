---
base_model: deepseek-ai/DeepSeek-R1-Distill-Llama-8B
license: mit
pipeline_tag: question-answering
tags:
- medical
- chain-of-thought
- fine-tuning
- qlora
- unsloth
---

# DeepSeek-R1-Medical-CoT

🚀 **Fine-tuning DeepSeek R1 for Medical Chain-of-Thought Reasoning**

This model is a fine-tuned version of `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`, specifically designed to enhance medical reasoning through **Chain-of-Thought (CoT) prompting**. It is trained using **QLoRA** with **Unsloth optimization**, allowing efficient fine-tuning on limited hardware resources.

---

## 📌 Model Details

### **Model Description**
- **Developed by:** [Your Name or Organization]
- **Fine-tuned from:** `deepseek-ai/DeepSeek-R1-Distill-Llama-8B`
- **Language(s):** English, with a focus on medical terminology
- **Training Data:** Medical reasoning dataset (`medical-o1-reasoning-SFT`)
- **Fine-tuning Method:** QLoRA (4-bit adapters), later merged into 16-bit weights
- **Optimization:** Unsloth (2x faster fine-tuning with lower memory usage)

### **Model Sources**
- **Repository:** [Your Hugging Face Model Repo URL]
- **Paper (if applicable):** [Link]
- **Demo (if applicable):** [Link]

---

## 🛠 **How to Use the Model**

### 1️⃣ Load the Model
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

repo_name = "your-huggingface-username/DeepSeek-R1-Medical-CoT"

tokenizer = AutoTokenizer.from_pretrained(repo_name)
model = AutoModelForCausalLM.from_pretrained(repo_name)

model.eval()
```
### 2️⃣ Run inference

```python
prompt = "What are the early symptoms of diabetes?"
inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

with torch.no_grad():
    output = model.generate(**inputs, max_new_tokens=200)

response = tokenizer.decode(output[0], skip_special_tokens=True)
print("Model Response:", response)
```
### 📢 Acknowledgments
- **DeepSeek-AI for releasing DeepSeek-R1**
- **Unsloth for optimized LoRA fine-tuning**
- **Hugging Face for hosting the models**
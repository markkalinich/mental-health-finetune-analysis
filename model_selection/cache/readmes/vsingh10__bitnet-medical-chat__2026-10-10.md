---
license: mit
datasets:
- ruslanmv/ai-medical-chatbot
language:
- en
base_model:
- microsoft/bitnet-b1.58-2B-4T-bf16
---
# 🩺 Hi! I am Dr. Bitsy, your personal healthcare assistant, how can I assist you ?

This is a fine-tuned version of **[microsoft/bitnet-b1.58-2B-4T-bf16](https://huggingface.co/microsoft/bitnet-b1.58-2B-4T-bf16)** using **LoRA** adapters on a medical chatbot dataset.  
It is designed to act as a **helpful and knowledgeable medical assistant** for answering patient queries with medically accurate and detailed explanations.

---

## 📊 Model Details
- **Base model**: `microsoft/bitnet-b1.58-2B-4T-bf16`
- **Fine-tuning method**: LoRA (Low-Rank Adaptation)
- **Merged model size**: ~2B parameters
- **Framework**: [Transformers](https://huggingface.co/docs/transformers), [PEFT](https://github.com/huggingface/peft), [TRL](https://github.com/huggingface/trl)
- **Dataset**: [`ruslanmv/ai-medical-chatbot`](https://huggingface.co/datasets/ruslanmv/ai-medical-chatbot)  
  ~5,000 samples of patient–doctor dialogues.

---

## 🧑‍⚕️ Intended Use
- Research on **medical dialogue generation**  
- Experimentation with **domain adaptation** of BitNet  
- Exploration of **LoRA fine-tuning for healthcare-related tasks**

Not intended for:
- Real clinical use  
- Emergency healthcare guidance  

---

## 🚀 Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "vsingh10/bitnet-medical-chat"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

messages = [
    {"role": "system", "content": "You are a helpful and knowledgeable medical doctor. Always provide detailed, medically accurate explanations."},
    {"role": "user", "content": "Hello doctor, I have bad acne. How do I get rid of it?"}
]

prompt = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(prompt, return_tensors="pt").to("cuda")

outputs = model.generate(
    **inputs,
    max_new_tokens=300,
    temperature=0.7,
    top_p=0.9,
    do_sample=True
)

print(tokenizer.decode(outputs[0], skip_special_tokens=True))
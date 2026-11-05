---
license: apache-2.0
datasets:
- lavita/MedQuAD
- qiaojin/PubMedQA
language:
- en
base_model:
- microsoft/phi-2
pipeline_tag: text-classification
library_name: transformers
---
# 🧠 Phi-2 Medical Fine-tuned Model

This model is a fine-tuned version of **microsoft/phi-2** on curated medical datasets such as MedQuAD and synthetic instruction data.
It is designed for **medical Q&A, healthcare chatbots, and clinical information retrieval**.

---

## 📋 Model Details
**Base model:** `microsoft/phi-2`  
**Fine-tuned by:** [@harshtambade](https://huggingface.co/harshtambade)  
**Framework:** PyTorch + Transformers  
**Fine-tuning Type:** Supervised Fine-Tuning (SFT)  

---

## 🧩 Intended Use
- Healthcare question answering  
- Symptom and disease awareness chatbots  
- Medical research assistance  

⚠️ **Disclaimer:** This model does **not** replace professional medical advice.  
Use for **research or educational purposes only.**

---

## 🧠 How to Use

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "harshtambade/phi2-medical-finetuned"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = "What are the symptoms of asthma?"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=200)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))

⚙️ Training Configuration

Epochs: 3

Learning rate: 2e-5

Batch size: 4

Optimizer: AdamW

Scheduler: Linear

Context length: 2048

📈 Evaluation Results
Metric	Value
Training loss	TBD
Validation loss	TBD
📜 License

Apache 2.0

🧬 Citation
@misc{harshtambade2025phi2medical,
  title={Phi-2 Medical Fine-tuned Model},
  author={Harsh Tambade},
  year={2025},
  howpublished={\\url{https://huggingface.co/harshtambade/phi2-medical-finetuned}},
}
---
library_name: transformers
tags:
- medical
- qa
- tinyllama
- lora
- instruction-tuning
---

# Model Card for Model ID

This model is a fine-tuned medical question-answering language model based on TinyLlama-1.1B-Chat, optimized using LoRA for efficient training on limited hardware.

---

## Model Details

### Model Description

This model is a **medical Q&A instruction-tuned language model** built by fine-tuning TinyLlama-1.1B-Chat using supervised fine-tuning (SFT) with LoRA.

It is designed to generate structured and informative responses to medical-related questions for educational and research purposes.

- **Developed by:** Praveen  
- **Funded by [optional]:** Self / Academic Project  
- **Shared by [optional]:** Hugging Face Hub  
- **Model type:** Causal Language Model (Instruction-tuned)  
- **Language(s) (NLP):** English  
- **License:** Apache 2.0  
- **Finetuned from model [optional]:** TinyLlama/TinyLlama-1.1B-Chat-v1.0  

---

### Model Sources [optional]

- **Repository:** https://huggingface.co/<your-username>/medical-qa-tinyllama  
- **Paper [optional]:** N/A  
- **Demo [optional]:** Included in inference code  

---

## Uses

### Direct Use

- Medical question answering  
- Educational assistance  
- Learning basic healthcare concepts  

### Downstream Use [optional]

- Medical chatbots (non-clinical)  
- AI tutors for students  
- Research prototypes  

### Out-of-Scope Use

- Clinical diagnosis  
- Emergency medical advice  
- Real-world healthcare decision-making  
- Any life-critical applications  

---

## Bias, Risks, and Limitations

- May generate incorrect or outdated medical information  
- Limited dataset (~10K samples)  
- Not clinically validated  
- Can hallucinate plausible but incorrect answers  
- Lacks patient-specific reasoning  

---

### Recommendations

- Use only for educational purposes  
- Always verify outputs with medical professionals  
- Do not deploy in high-risk environments  
- Apply safety filters if used in applications  

---

## How to Get Started with the Model

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "pra-974/medical-qa-tinyllama"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

def ask(question):
    prompt = f"### Instruction:\n{question}\n\n### Response:\n"
    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        temperature=0.7,
        top_p=0.9
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

print(ask("What are symptoms of diabetes?"))
---
library_name: transformers
license: apache-2.0
base_model: unsloth/gemma-3n-E4B-it
tags:
  - medical
  - emergency-response
  - healthcare
  - fine-tuned
  - unsloth
  - gemma3n
  - citizen2responder
  - privacy-first
  - local-deployment
pipeline_tag: text-generation
language:
  - en
---

# 🏥 Medical Emergency Response AI - Gemma 3N (Fine-tuned)

A fine-tuned version of **Gemma 3N** designed for emergency response scenarios. Powers the **Citizen2Responder** app with dual-mode capabilities: natural guidance for bystanders and structured tool outputs for EMTs — all with a privacy-first, local deployment focus.

---

## 🧠 Model Summary

- **Type:** Causal Language Model  
- **Base Model:** [`unsloth/gemma-3n-E4B-it`](https://huggingface.co/unsloth/gemma-3n-E4B-it)  
- **Parameters:** 4B  
- **Adapters:** LoRA  
- **Language:** English  
- **License:** Apache 2.0  
- **Trained with:** Unsloth + LoRA  
- **Author:** Citizen2Responder Team  
- **Model Repo:** [GitHub](https://github.com/slyracoon23/citizen2responder)  
- **HF Page:** [Hugging Face](https://huggingface.co/Slyracoon23/medical-gemma3n-emergency-response)

---

## ✅ Key Features

### 🗣️ Natural Conversation Mode
- Step-by-step emergency guidance  
- No medical jargon  
- Real-time questioning & coaching  

### 🔧 Tool Calling Mode
- Generates structured EMT/dispatch reports  
- JSON-style outputs for system use  

---

## 🚫 Limitations

- **Not** a substitute for professional medical help  
- **Not** for non-emergency or specialized medical conditions  
- **Should not** replace EMTs in critical care situations  

---

## 💻 Usage Example

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("Slyracoon23/medical-gemma3n-emergency-response")
tokenizer = AutoTokenizer.from_pretrained("Slyracoon23/medical-gemma3n-emergency-response")

# Natural guidance mode
prompt = "Someone collapsed and is not responding. What should I assess first?"
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_length=200, temperature=0.7)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 📊 Evaluation

- ✅ Recognizes emergency types (>95%)  
- ✅ Accurate tool calls (>90%)  
- ✅ EMT-approved safety outputs  
- ✅ Mobile ready (GGUF quantized)

---

## 🔐 Deployment & Privacy

- Local/mobile deployment (no cloud)  
- ~2.5GB size (quantized)  
- Compatible with iOS/Android via `llama.rn`

---

## 📚 Citation

```bibtex
@misc{medical-gemma3n-emergency-response,
  title={Medical Emergency Response AI - Gemma 3N Fine-tuned},
  author={Citizen2Responder Team},
  year={2025},
  url={https://huggingface.co/Slyracoon23/medical-gemma3n-emergency-response},
  note={Fine-tuned for dual-mode emergency response with privacy-first architecture}
}
```

---

## ⚠️ Disclaimer

This model is for educational and emergency guidance only. Always contact professional medical services in real emergencies.
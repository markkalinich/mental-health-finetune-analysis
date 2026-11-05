---
tags:
- medical
- triage
- rural-health
- safety-layer
- indic-health
---

# Rural Health Assistant v3.1

A fine-tuned Qwen2.5-1.5B model for rural health assistance in India. Includes a full deterministic safety layer — no unsafe prescriptions, no antibiotics without doctor, emergency red flag detection.

## Model Details
- **Base Model**: Qwen2.5-1.5B-Instruct
- **Type**: Full merged model (no adapter needed)
- **Size**: ~3GB
- **Language**: English (designed for use with IndicTrans2 translation layer)
- **v1**: Medical knowledge (MedMCQA)
- **v2**: Triage + reasoning
- **v3**: Safe OTC + first aid
- **v3.1**: Full safety layer + entity extraction + session memory + red flags + confidence evaluator

---

## Option 1 — Use with pipeline.py (recommended)
Download `pipeline.py` from this repo first, then:

```python
from pipeline import RuralHealthPipeline

health = RuralHealthPipeline(
    model_name="theartai/qwen25-1.5b-medical-india-v3.1",
    token="your_hf_token"  # only needed if repo is private
)

# Basic usage
response = health("I have fever", session_id="user_001")
print(response)
# → Asks for age, pregnancy status, allergies before suggesting anything

# Session memory — builds context across turns
health("I have fever and cough", session_id="user_001")
health("I am 35 years old", session_id="user_001")
health("I am pregnant",        session_id="user_001")
# → Now gives pregnancy-safe advice (Paracetamol only, no NSAIDs)

# Emergency detection
response = health("I have chest pain and cannot breathe", session_id="user_001")
print(response)
# → 🚨 CHEST PAIN — Call 108 or ambulance immediately!

# Reset session when conversation ends
health.reset_session("user_001")
```

---

## Option 2 — Use model directly (no pipeline.py)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model = AutoModelForCausalLM.from_pretrained(
    "theartai/qwen25-1.5b-medical-india-v3.1",
    dtype=torch.float16,
    device_map="auto",
)
tokenizer = AutoTokenizer.from_pretrained("theartai/qwen25-1.5b-medical-india-v3.1")

messages = [
    {"role": "system", "content": "You are a rural health assistant. Ask screening questions before suggesting any medicine. Never suggest antibiotics without doctor."},
    {"role": "user",   "content": "I have fever. What medicine should I take?"}
]

text = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
inputs = tokenizer(text, return_tensors="pt").to("cuda")

with torch.no_grad():
    outputs = model.generate(**inputs, max_new_tokens=300, temperature=0.1, do_sample=False)

response = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(response)
```

---

## What pipeline.py handles automatically

| Feature | Description |
|---|---|
| Entity extraction | Age, pregnancy, diabetes, BP, temperature |
| Red flag detection | Chest pain, seizure, unconscious, severe bleeding |
| Session memory | Remembers age, conditions across conversation turns |
| Conversation history | Last 4 turns kept in context |
| Medication safety | Refuses medicine without age + symptom info |
| Safe OTC only | Paracetamol, ORS, honey — WHO approved |
| Confidence check | Filters uncertain model responses |
| Response validation | Min/max length control |

---

## Safety Features
- Hard refusal for antibiotics without doctor prescription
- Pregnancy-safe advice (Paracetamol only, no NSAIDs)
- Child-safe advice (no aspirin, no cough syrup under 6)
- Emergency 108 escalation for red flags
- Never suggests prescription drugs

---

## Full Pipeline Architecture
- Layer 1 (ASR): IndicConformer — user voice to text
- Layer 2 (Translation): IndicTrans2 — local language to English
- Layer 3 (LLM): This model — English medical guidance
- Layer 4 (Translation): IndicTrans2 — English to local language
- Layer 5 (TTS): Indic Parler-TTS — voice output
- Layer 6 (Delivery): WhatsApp/Twilio — user receives voice message

---

## Disclaimer
This is a prototype for rural health assistance in India. Always consult a qualified doctor for serious conditions. This model should not replace professional medical advice.

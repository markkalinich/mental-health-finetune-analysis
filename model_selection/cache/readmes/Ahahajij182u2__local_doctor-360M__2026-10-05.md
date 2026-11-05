# 🩺 Local Doctor 360M – Model Card

## 📌 Model Details

* **Model Name:** `local_doctor-360M`
* **Base Model:** [SmolLM2-360M-Instruct]("https://huggingface.co/HuggingFaceTB/SmolLM2-360M-Instruct")
* **Model Type:** Causal Language Model (Instruction-tuned)
* **Framework:** Transformers (PyTorch)
* **Fine-tuning Type:** Domain-specific instruction tuning (medical symptom → condition mapping)
* **Developer:** Independent / Local deployment focused

---

## 🧠 Model Description

**Local Doctor 360M** is a lightweight, locally deployable medical assistant model designed to:

* Interpret **user-provided symptoms**
* Suggest **possible medical conditions**
* Run **entirely on local machines** (no cloud dependency)

The model is optimized for:

* Privacy-first usage
* Offline inference
* Low-resource environments

---

## 🎯 Intended Use

### ✅ Primary Use Cases

* Symptom-based **preliminary health insights**
* Educational or experimental AI applications
* Local/offline medical assistant prototypes
* Research on **small medical LLMs**

### ❌ Not Intended For

* Clinical diagnosis
* Emergency decision-making
* Replacement for licensed medical professionals

---

## ⚠️ Limitations & Risks

This model has **significant limitations**:

* ❗ May produce **incorrect or misleading diagnoses**
* ❗ Struggles with **overlapping symptoms**
* ❗ Limited reasoning due to small model size (360M parameters)
* ❗ May generate **hallucinated or non-medical advice**
* ❗ Not trained on real-time or verified clinical datasets

### 🚨 Safety Notice

This model **must not be used for real medical decisions**.
Always consult a qualified healthcare professional.

---

## 📊 Performance Summary

Based on internal testing:

* Approximate accuracy: **~40–50%** on structured symptom datasets
* Performs well on:

  * Clear, high-signal symptom patterns (e.g., stroke, migraine)
* Performs poorly on:

  * Ambiguous cases
  * Rare conditions
  * Differential diagnosis scenarios

---

## 🧪 Example

### Input

```
fever, headache, fatigue
```

### Output

```
Possible conditions: Viral infection, Flu
```

---

## 🏗️ Training Details

* Fine-tuned on:

  * Symptom-condition mappings
  * Instruction-style medical prompts
* Training style:

  * Supervised fine-tuning (SFT)
* No reinforcement learning or alignment tuning applied

---

## 🔐 Privacy & Local Deployment

A key feature of this model:

* ✅ Runs **100% locally**
* ✅ No internet required
* ✅ User data **never leaves the device**

---

## ⚙️ Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch


model_name = "Ahahajij182u2/local_doctor-360M"

# Load model and tokenizer once
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)
model.eval()

def generate_diagnosis(symptoms: str, max_tokens: int = 300) -> str:
    """Generate diagnosis for given symptoms."""
    prompt = f"""<|im_start|>system
You are a medical assistant AI.

Rules:
- Predict the most likely disease from the symptoms.
- Give 3 to 5 basic precautions or first steps.
- Use only this format:

POSSIBLE DISEASE: ...

POSSIBLE PRECAUTIONS: ...

- If symptoms suggest an emergency, advise immediate medical help.
- Do not give unusual or unsafe advice.
<|im_end|>
<|im_start|>user
{symptoms}
<|im_end|>
<|im_start|>assistant
"""
    
    inputs = tokenizer(prompt, return_tensors="pt")
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=0.1,
            do_sample=True,
        )
    
    decoded = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1]:],
        skip_special_tokens=False
    )
    
    return decoded.split("<|im_end|>")[0].strip()



# Test cases
test_symptoms = [
    "chest pain, shortness of breath",
    "diarrhea, vomiting, stomach pain",
    "rash, itching, swelling",
    "cough, fever, sore throat",
]

for symptoms in test_symptoms:
    response = generate_diagnosis(symptoms)
    print(f"\n{symptoms}\n→ {response}")
    assert "POSSIBLE DISEASE" in response
    assert "POSSIBLE PRECAUTIONS" in response
```

---

## 📦 Model Size & Requirements

* Size: ~300–500 MB (depending on format)
* Runs on:

  * CPU ✅
  * Low-end GPU ✅
* Suitable for:

  * Laptops
  * Edge devices

---

## 🔧 Known Issues

* Inconsistent formatting of outputs
* May repeat prompt structure
* Sometimes outputs unrelated conditions
* Weak handling of multi-condition reasoning

---

## 🚀 Future Improvements

* Better medical dataset curation
* Instruction tuning for safer outputs
* Multi-condition ranking
* Confidence scoring
* Integration with rule-based safety filters

---

## 📜 License

Based on the license of the base model:
Refer to SmolLM2-360M-Instruct for details.

---

## 🙌 Acknowledgements

* Built on top of Hugging Face ecosystem
* Fine-tuned with [Unsloth]("https://unsloth.ai/")
* Base model by HuggingFaceTB
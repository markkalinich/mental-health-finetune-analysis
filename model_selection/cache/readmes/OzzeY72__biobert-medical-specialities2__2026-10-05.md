---
license: apache-2.0
datasets:
- martagm17/test
language:
- en
base_model:
- dmis-lab/biobert-large-cased-v1.1
pipeline_tag: text-classification
---
# 🧠 BioBERT-Medical-Specialities2

**BioBERT-Medical-Specialities2** is a fine-tuned [BioBERT](https://huggingface.co/dmis-lab/biobert-base-cased-v1.1) model for multi-class medical text classification.  
It classifies short medical questions or symptom descriptions into one of **35 clinical specialities**.

## 📊 Labels

This model predicts the following 35 medical specialties:

None, Cardiology, Hematology, Oncology, Endocrinology, Respiratory, Allergy, Dermatology, Nephrology,
Gastroenterology, Rheumatology, Otorhinolaryngology, Anesthesiology, Biochemistry, Pharmacology, Psychiatry,
Microbiology, Physiology, Pathology, Obstetrics, Gynecology, Surgery, Emergency, Orthopedics, Neurology, Urology,
Anatomy, Genetics, Radiology, Ophthalmology, Odontology, Pediatrics, Geriatrics, Nursing, Chemistry, Psychology

## 📦 Model Details

- **Base model**: [`dmis-lab/biobert-base-cased-v1.1`](https://huggingface.co/dmis-lab/biobert-base-cased-v1.1)
- **Fine-tuned on**: [`martagm17/test`](https://huggingface.co/datasets/martagm17/test)
- **Task**: Multi-class medical text classification
- **Languages**: English 🇬🇧
- **License**: Apache 2.0

---

## 🚀 How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load model and tokenizer
model_name = "your-username/biobert-medical-specialities"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Example input
text = "I have constant chest pain and shortness of breath."

# Tokenize and predict
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
with torch.no_grad():
    logits = model(**inputs).logits

predicted_class_id = logits.argmax().item()
predicted_label = model.config.id2label[predicted_class_id]

print(f"Predicted medical speciality: {predicted_label}")
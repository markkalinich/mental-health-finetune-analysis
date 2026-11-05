---
license: mit
language:
- en
base_model:
- google-t5/t5-small
pipeline_tag: summarization
---


## 🧾 Model Card: `t5-small-patient-summary`

### Model Details

- **Model Name**: `umeshramya/t5_small_medical_512`
- **Base Model**: [`t5-small`](https://huggingface.co/t5-small)
- **Fine-tuned for**: Summarization of patient medical records
- **Language**: English


---

### 📖 Model Description

This is a fine-tuned version of the `t5-small` model for the task of summarizing patient records into concise medical summaries. The model has been trained on a custom dataset containing anonymized medical records with the goal of generating accurate and meaningful summaries that can assist healthcare providers.
Input length is 512 tokens and if text lenggth then fraction them and rerun 
---

### 🏥 Use Case

This model is intended for use in clinical settings or health-tech applications where summarization of medical records (like patient histories, consultation notes, or discharge summaries) is needed.

**Example Input:**
```
 The patient is a 45-year-old male with a history of hypertension and diabetes, presenting with chest pain...
```

**Example Output:**
```
45-year-old male with hypertension and diabetes presenting with chest pain.
```

---

### 🧪 Training Data

The model was trained on a proprietary dataset of anonymized patient records. Each record includes a full-text medical note and a corresponding human-written summary. Sensitive personal information was removed or obfuscated before training.

*Note*: Data is not publicly shared due to privacy and compliance concerns.

---

### ⚙️ How to Use

```python
from transformers import pipeline

summarizer = pipeline(model="umeshramya/t5_small_medical_512")
summary = summarizer("The patient is a 70-year-old female with...", max_length=200, min_length=50)
print(summary)
```

---

### 🔒 Limitations and Bias

- This model may reflect biases present in the training data.
- Not suitable for use in high-stakes clinical decision-making without human oversight.
- It may sometimes generate incorrect or incomplete summaries.

---

### ✅ Intended Use

- Medical record summarization
- Assistive tools for healthcare documentation

---

### 🚫 Misuse

- Not for use in diagnostic or treatment recommendation systems without medical supervision.
.

---

### 👤 Author & Contact

- **Author**: *Dr Umesh Bilagi/ NiceHMs*
- **Contact**: *admin@nicehms.com*
- **webSite**: [Nice HMS](https://www.nicehms.com)

---

### 🔄 Acknowledgments

- Hugging Face 🤗 Transformers
- The contributors of the original T5 model
- Medical professionals who reviewed the summaries (if applicable)
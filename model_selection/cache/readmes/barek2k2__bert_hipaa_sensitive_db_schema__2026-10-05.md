---
language: en
license: mit
tags:
  - BERT
  - HIPAA
  - PHI
  - LLM
  - sensitive data
  - classification
  - healthcare
  - mHealth Application
  - cybersecurity
  - database
  - column name classifier
  - data field classifier
  - transformers
  - huggingface
model-index:
  - name: LLM BERT Model for HIPAA-Sensitive Database Fields Classification
    results: []
---

# LLM BERT Model for HIPAA-Sensitive Database Fields Classification

This repository hosts a fine-tuned BERT-base model that classifies database column names as either **PHI HIPAA-sensitive** (e.g., `birthDate`, `ssn`, `address`) or **non-sensitive** (e.g., `color`, `food`, `country`).

Use this model for:
- Masking PHI data fields before sharing database to avoid HIPAA compliance
- Preprocessing before data anonymization
- Identifying patient's sensitive data fields in a dataset before training an AI model
- Enhancing security in healthcare and mHealth applications

---

## 🧠 Model Info

- **Base Model**: `bert-base-uncased`
- **Task**: Binary classification (PHI HIPAA Sensitive vs Non-sensitive)
- **Trained On**: GAN generated Synthetic and real-world column name examples
- **Framework**: Hugging Face Transformers
- **Model URL**: [https://huggingface.co/barek2k2/bert_hipaa_sensitive_db_schema](https://huggingface.co/barek2k2/bert_hipaa_sensitive_db_schema)

---

## 🚀 Usage Example (End-to-End)

### 1. Install Requirements
```bash
pip install torch transformers
```

### 2. Example
```bash
import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load model and tokenizer
model = BertForSequenceClassification.from_pretrained("barek2k2/bert_hipaa_sensitive_db_schema")
tokenizer = BertTokenizer.from_pretrained("barek2k2/bert_hipaa_sensitive_db_schema")
model.eval()

# Example column names
texts = ["birthDate", "country", "jwtToken", "color"]

# Tokenize input
inputs = tokenizer(texts, return_tensors="pt", padding=True, truncation=True, max_length=128)

# Predict
with torch.no_grad():
    outputs = model(**inputs)
    predictions = torch.argmax(outputs.logits, dim=1)

# Display results
for text, pred in zip(texts, predictions):
    label = "Sensitive" if pred.item() == 1 else "Non-sensitive"
    print(f"{text}: {label}")

```

### 3. Output
```bash
birthDate: Sensitive
country: Non-sensitive
jwtToken: Sensitive
color: Non-sensitive
```

In the healthcare industry, safeguarding sensitive patient data is of utmost importance, particularly when developing and maintaining software systems that involve database sharing. The Health Insurance Portability and Accountability Act (HIPAA) mandates strict regulations to ensure the privacy and security of Protected Health Information (PHI). Healthcare organizations must comply with these regulations to prevent unauthorized access, breaches, and potential legal consequences. However, ensuring HIPAA compliance becomes a complex challenge when databases are shared among multiple teams for debugging, development, and testing purposes.
This research work proposes a novel approach that uses BERT based LLM for identifying sensitive database columns into the database schema in order to avoid PHI HIPAA violation.

#### Disclaimer
This LLM model is fine-tuned with synthetic dataset(~5K) and is provided for research and educational purposes only. Always verify compliance before using in production environments.

---

## 📊 Model Performance Analysis

**Table 1: Changing hyperparameters and results**

| Step   | Learning Rate | Batch Size | Epoch | Weight Decay | Precision | Recall | F1 Score | Accuracy |
|--------|---------------|------------|-------|---------------|-----------|--------|----------|----------|
| 1      | 0             | 16         | 1     | 0.001         | 0.0000    | 0.0000 | 0.0000   | 36.78%   |
| 2      | 1e-1          | 16         | 1     | 0.001         | 0.6321    | 1.0000 | 0.7746   | 63.21%   |
| 3      | 1e-1          | 32         | 1     | 0.001         | 0.6321    | 1.0000 | 0.7746   | 63.21%   |
| 4      | 1e-1          | 32         | 2     | 0.001         | 0.6321    | 1.0000 | 0.7746   | 63.21%   |
| 5      | 1e-1          | 32         | 3     | 0.001         | 0.6321    | 1.0000 | 0.7746   | 63.21%   |
| 6      | 1e-1          | 32         | 3     | 0.01          | 0.6321    | 1.0000 | 0.7746   | 63.21%   |
| 7      | 2e-1          | 32         | 4     | 0.01          | 0.6321    | 1.0000 | 0.7746   | 63.21%   |
| 8      | 3e-4          | 32         | 4     | 0.01          | 0.6331    | 0.9982 | 0.7748   | 63.32%   |
| 9      | 2e-4          | 32         | 4     | 0.01          | 0.9908    | 0.9730 | 0.9818   | 97.72%   |
| 10     | 1e-5          | 32         | 4     | 0.01          | 0.9964    | 0.9928 | 0.9946   | 99.31%   |
| 11     | 1e-5          | 32         | 5     | 0.01          | 0.9964    | 0.9928 | 0.9946   | 99.31%   |
| **12** | **1e-5**      | **16**     | **5** | **0.01**      | **1.0000**| **0.9964** | **0.9982**   | **99.72%**   |
| 13     | 1e-5          | 16         | 5     | 0.1           | 1.0000    | 0.9946 | 0.9973   | 99.65%   |
| 14     | 1e-5          | 32         | 5     | 0.1           | 1.0000    | 0.9946 | 0.9973   | 99.65%   |
| 15     | 1e-5          | 32         | 5     | 1.0           | 0.9964    | 0.9946 | 0.9946   | 99.54%   |
| 16     | 1e-6          | 32         | 5     | 1.0           | 0.8342    | 0.9153 | 0.8729   | 83.15%   |


### Limitations
One of the main limitations of this work is the use of
a synthetic dataset instead of real-world data to fine-tune
and train the AI models. Although the dataset was carefully
checked for accuracy, it may not fully reflect the complexity
and diversity of actual healthcare records.

## 👤 Author

**MD Abdul Barek**  
PhD student & GRA @ Intelligent Systems and Robotics 
- 🏫 University of West Florida, Florida, USA
- 📧 mb381@students.uwf.edu
- 📧 barek2k2@gmail.com
- 🔗 [Hugging Face Profile](https://huggingface.co/barek2k2)

**Advisor:**  
Dr. Hakki Erhan Sevil  
Associate Professor
Intelligent Systems and Robotics, 
University of West Florida  
📧 hsevil@uwf.edu

**Supervisors:**  
Dr. Guillermo Francia III  
Director, Research and Innovation,
Center for Cybersecurity,
University of West Florida  
📧 gfranciaiii@uwf.edu


Dr. Hossain Shahriar  
Associate Director and Professor, Center for Cybersecurity,  
University of West Florida  
📧 hshahriar@uwf.edu

Dr. Sheikh Iqbal Ahamed  
Wehr Professor and Founding Chair of Computer Science Department at Marquette University,  
Marquette University  
📧 sheikh.ahamed@marquette.edu
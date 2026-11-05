---
language: en
license: mit
tags:
  - text-classification
  - mental-health
  - transformer
  - distilbert
  - depression
  - anxiety
  - clinical-nlp
  - huggingface
datasets:
  - custom
library_name: transformers
pipeline_tag: text-classification
widget:
  - text: "I feel hopeless and can't sleep properly."
    example_title: "Depression"
  - text: "I’m anxious all the time and can’t focus."
    example_title: "Anxiety"
  - text: "Everything’s fine. I’m feeling good."
    example_title: "Healthy"
model-index:
  - name: distilbert-mentalhealth-classifier
    results:
      - task:
          type: text-classification
          name: Text Classification
        dataset:
          name: Filtered Combined Dataset
          type: custom
        metrics:
          - type: accuracy
            value: 0.856
          - type: f1
            value: 0.854
---

# 🧠 DistilBERT Mental Health Classifier

This model is a fine-tuned version of [`distilbert-base-uncased`](https://huggingface.co/distilbert-base-uncased) for mental health condition classification. It is trained on a custom dataset containing user statements labeled with categories such as **depression**, **anxiety**, **PTSD**, and more.


# 🧠 Use Case
This model is designed for:

Early detection of mental health symptoms in user conversations

Clinical research on NLP-based diagnostic support

AI assistants that provide empathetic triage or support

# 🧪 Performance
The model shows significant improvements after fine-tuning:

| Sample Size | Accuracy (Before) | F1 Score (Before) | Accuracy (After) | F1 Score (After) |
| ----------- | ----------------- | ----------------- | ---------------- | ---------------- |
| 200 Samples | 0.075             | 0.0142            | 0.830            | 0.8267           |
| 500 Samples | 0.070             | 0.0141            | 0.856            | 0.8544           |


✅ These results indicate that fine-tuning with a high-quality mental health dataset enables DistilBERT to make informed predictions from free-form user input.

# 📚 Dataset
The model was fine-tuned on Filtered_Combined_Data.csv, a curated dataset of 42,000+ statements labeled across multiple mental health categories. Each sample includes:

statement — a natural language user message

label — a mental health condition such as "Depression", "Anxiety", or "Healthy"

# 🏗️ Prompt Format (used during fine-tuning)
text
Copy
Edit
### Instruction:
Classify the mental health condition in the following statement.

Input:
{text}

Response:
{label}
This instruction format aligns the classifier with instruction-tuned language models.

---

# 🧠 Labels Covered

The model classifies input statements into the following mental health categories (example):

- **Anxiety**
- **Depression**
- **PTSD**
- **OCD**
- **Bipolar Disorder**
- **ADHD**
- **Healthy**
- **Others** (as labeled in dataset)

---

# ⚙️ Training Configuration

- **Base Model**: `distilbert-base-uncased`
- **Epochs**: 3
- **Total Steps**: ~36,500
- **Batch Size**: 16
- **Max Length**: 512
- **Quantization**: None
- **Learning Rate**: 2e-5
- **Optimizer**: AdamW
- **Evaluation**: Accuracy, Weighted F1

---


# 📂 Model Files

- `pytorch_model.bin` — fine-tuned model weights
- `tokenizer_config.json`, `vocab.txt`, etc. — tokenizer files
- `config.json` — architecture and label mapping
- `README.md` — this file

---

# 📄 License

This model is licensed under the **MIT License** — free for personal, academic, and commercial use with attribution.

---

# 🙋 Author

Developed by **Dileep Reddy Suram**  
📍 For multimodal clinical AI assistant research and PhD preparation  
🔗 [Hugging Face Profile](https://huggingface.co/dsuram)

---

# 🚀 Citation

If you use this model, please cite:

# 📦 How to Use (Quick Start)

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="dsuram/distilbert-mentalhealth-classifier")
classifier("I feel anxious all the time and can't concentrate.")
---
🧪 Inference (Advanced)
You can also use the tokenizer + model directly:


from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

#### Load model and tokenizer
model = AutoModelForSequenceClassification.from_pretrained("dsuram/distilbert-mentalhealth-classifier")
tokenizer = AutoTokenizer.from_pretrained("dsuram/distilbert-mentalhealth-classifier")

# Input text
text = "I feel lost, hopeless, and don't see a way out."

# Tokenize and predict
inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
outputs = model(**inputs)
logits = outputs.logits
predicted_class_id = torch.argmax(logits, dim=1).item()

# Map to label
label_map = model.config.id2label
print(f"Predicted label: {label_map[predicted_class_id]}")
---



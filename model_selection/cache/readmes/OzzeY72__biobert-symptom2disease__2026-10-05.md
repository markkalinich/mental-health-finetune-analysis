---
license: apache-2.0
datasets:
- venetis/symptom_text_to_disease_mk3
- celikmus/symptom_text_to_disease_01
dataset_info:
  features:
    - name: text
      dtype: string
    - name: labels
      dtype:
        class_label:
          names:
            '0': emotional pain
            '1': hair falling out
            '2': heart hurts
            '3': infected wound
            '4': foot ache
            '5': shoulder pain
            '6': injury from sports
            '7': skin issue
            '8': stomach ache
            '9': knee pain
            '10': joint pain
            '11': hard to breath
            '12': head ache
            '13': body feels weak
            '14': feeling dizzy
            '15': back pain
            '16': open wound
            '17': internal pain
            '18': blurry vision
            '19': acne
            '20': muscle pain
            '21': neck pain
            '22': cough
            '23': ear ache
            '24': feeling cold
language:
- en
base_model:
- dmis-lab/biobert-base-cased-v1.1
pipeline_tag: text-classification
---
# BioBERT Symptom Text Classifier 🧬🩺

This model is a fine-tuned version of [**dmis-lab/biobert-base-cased-v1.1**](https://huggingface.co/dmis-lab/biobert-base-cased-v1.1) on a symptom-to-condition classification task. It maps free-form medical symptom descriptions in English to 25 predefined symptom categories such as "back pain", "headache", "injury from sports", etc.

## 🧠 Model Details

- **Architecture:** BioBERT (Transformer-based)
- **Base Model:** [`dmis-lab/biobert-base-cased-v1.1`](https://huggingface.co/dmis-lab/biobert-base-cased-v1.1)
- **Task:** Text Classification (Single-label)
- **Labels:** 25 symptom categories (see full list below)
- **Language:** English
- **License:** Apache 2.0

## 📊 Datasets Used

This model was trained on a combination of public datasets containing free-text symptom descriptions annotated with associated pain types or complaints:

- [`venetis/symptom_text_to_disease_mk3`](https://huggingface.co/datasets/venetis/symptom_text_to_disease_mk3)
- [`celikmus/symptom_text_to_disease_01`](https://huggingface.co/datasets/celikmus/symptom_text_to_disease_01)

## 🏷️ Label Set (25 Classes)

The model predicts one of the following 25 labels:

| ID | Symptom Category       |
|----|------------------------|
| 0  | emotional pain         |
| 1  | hair falling out       |
| 2  | heart hurts            |
| 3  | infected wound         |
| 4  | foot ache              |
| 5  | shoulder pain          |
| 6  | injury from sports     |
| 7  | skin issue             |
| 8  | stomach ache           |
| 9  | knee pain              |
| 10 | joint pain             |
| 11 | hard to breath         |
| 12 | head ache              |
| 13 | body feels weak        |
| 14 | feeling dizzy          |
| 15 | back pain              |
| 16 | open wound             |
| 17 | internal pain          |
| 18 | blurry vision          |
| 19 | acne                   |
| 20 | muscle pain            |
| 21 | neck pain              |
| 22 | cough                  |
| 23 | ear ache               |
| 24 | feeling cold           |

## 🚀 Usage

To use the model in your project:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "your-username/your-model-name"  # Replace with actual path

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
model.eval()

def classify_symptom(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_class_id = torch.argmax(outputs.logits, dim=-1).item()
        label = model.config.id2label[predicted_class_id]
    return label

# Example
classify_symptom("My lower back hurts when I sit for a long time")
# ➜ "back pain"
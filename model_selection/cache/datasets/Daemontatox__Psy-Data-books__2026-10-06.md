---
task_categories:
- question-answering
language:
- en
tags:
- medical
license: apache-2.0
size_categories:
- 100K<n<1M
---
![image](./image.webp)

## 🧠 Psy-Data-Books: Synthetic Medical & Psychology Conversation Dataset
Psy-Data-Books is one of the largest synthetic datasets of psychology and medical conversations, generated from verified medical and psychology literature. It is designed for building and training powerful conversational AI systems for healthcare, therapy, and mental health applications.

## 📊 Dataset Summary
Domain: Psychology, Psychiatry, Mental Health, General Medicine

Data Type: Synthetic Conversations (Q&A, multi-turn dialogues)

Source: Books and academic literature

Size: Largest publicly available synthetic dataset in this domain

Format: JSON

License: Apache 2.0

Generated On: 2025-06-14

## 💡 Use Cases
Training medical and psychology-focused LLMs

Building therapy agents and healthcare chatbots

Research in doctor-patient conversational modeling

Pretraining/fine-tuning healthcare NLP systems

⚠️ Important: This dataset is not a replacement for real clinical data. It is meant for research and development, not clinical deployment.

## 📁 Dataset Structure
Each record represents a multi-turn medical or psychological conversation. Conversations may contain:

patient_query: Initial question or concern

response: AI/Doctor-style response based on academic/clinical context

context: (Optional) Medical literature or book excerpt the conversation was derived from

metadata: (Optional) Tags, categories, source reference

Example format:

```json
[
  {
    "patient_query": "I've been feeling anxious every morning. Is this normal?",
    "response": "Morning anxiety is common in people with generalized anxiety disorder...",
    "context": "From 'Cognitive Behavioral Therapy: Basics and Beyond' by Judith Beck",
    "metadata": {
      "topic": "Anxiety",
      "type": "Psychology",
      "source": "Book"
    }
  }
]
```
## 🧪 Usage
```python

import json

# Load the dataset
with open('psy_data_books.json', 'r') as f:
    dataset = json.load(f)

# Iterate through the records
for convo in dataset:
    print(convo['patient_query'])
    print(convo['response'])
```
## ⚠️ Medical & Ethical Disclaimer
This dataset is synthetic and based on literature-derived content. It is not a substitute for professional medical advice, diagnosis, or treatment.

Always consult qualified professionals. AI models trained on this dataset should include strict disclaimers and avoid deployment in clinical settings without human oversight.
🔗 Access the Dataset
Hugging Face:
https://huggingface.co/datasets/Daemontatox/Psy-Data-books

## 📄 License
Apache 2.0 License
You are free to use, modify, and distribute the dataset with proper attribution.

## 🧾 Citation
Please cite the dataset as:

```bibtex
Copy
Edit
@dataset{medical_conversations_2025,
  title     = {Psy-Data-Books: Medical and Psychology Conversation Dataset},
  author    = {Generated using DS_Creator},
  year      = {2025},
  url       = {https://huggingface.co/datasets/Daemontatox/Psy-Data-books}
}
```
## 🙋 Contributions & Feedback
If you'd like to contribute improvements or report issues, please open a PR or create an issue on the Hugging Face repository.
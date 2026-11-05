---
language:
- id
license: mit
base_model: indobenchmark/indobert-base-p2
tags:
- emotion
- classification
- indobert
- mood-notes
datasets:
- custom
metrics:
- accuracy
library_name: transformers
pipeline_tag: text-classification
---

# Indobert-emotion-classification

## Description
This model is a fine-tuned version of [indobenchmark/indobert-base-p2](https://huggingface.co/indobenchmark/indobert-base-p2). It is specifically designed to classify Indonesian text into 12 distinct emotion categories, capturing various nuances in local and informal communication.

## Dataset Information
The model was trained on a **programmatically generated Indonesian dataset** curated to cover a wide range of emotional expressions.
- **Total Data**: 30,000 rows.
- **Methodology**: Scripted Data Generation with custom **slang handling** (mager, gabut, baper, goks, etc).

### 12-Emotion Categories:
Normal (Normal), Frustrasi (Frustrated), Jengkel (Annoyed), Marah (Angry), Lelah (Tired), Sedih (Sad), Sabar (Patient), Senang (Happy), Takut (Afraid), Terkejut (Surprised), Gila (Crazy), Cinta (Love)

## Limitations
* **Synthetic Data Bias**: Since the model was trained on programmatically generated (synthetic) data, it may exhibit rigid patterns compared to natural human-to-human conversations.
* **Slang Evolution**: While the model supports current Indonesian slang, the rapid evolution of internet linguistics means that newer slang terms emerging after the training period may not be recognized accurately.
* **Context Sensitivity**: The model is optimized for short-form text classification. Accuracy may decrease for very long documents or texts containing complex, mixed emotions.
* **Overfitting Risk**: The extremely low loss values (approaching zero) suggest that the model is highly specialized to the specific patterns of this dataset, which might affect generalization on completely out-of-distribution data.

## Training Results
| Metric | Value |
| :--- | :--- |
| **Epochs** | 10 |
| **Final Training Loss** | 0.000000 |
| **Final Validation Loss** | 0.000006 |
| **Optimization** | AdamW |

## Usage
```python
from transformers import pipeline
classifier = pipeline("text-classification", model="mrezadit/indobert-emotion-classification")
results = classifier("jujur gue gabut parah hari ini")
print(results)
```
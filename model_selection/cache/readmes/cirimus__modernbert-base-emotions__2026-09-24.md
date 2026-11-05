---
language: en
tags:
- text-classification
- pytorch
- ModernBERT
- emotions
- multi-class-classification
datasets:
- super-emotion
license: cc-by-4.0
metrics:
- accuracy
- f1
- precision
- recall
base_model:
- answerdotai/ModernBERT-base
widget:
- text: I am thrilled to be a part of this amazing journey!
- text: I feel so disappointed with the results.
- text: This is a neutral statement about cake.
library_name: transformers
---

![banner](https://huggingface.co/datasets/cirimus/super-emotion/resolve/main/banner.png)

### Overview

This model was fine-tuned from [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the [Super Emotion](https://huggingface.co/datasets/cirimus/super-emotion) dataset for multi-class emotion classification. It predicts emotional states in text across seven labels: `joy, sadness, anger, fear, love, neutral, surprise`. 

---

### Model Details

- **Base Model**: [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base)
- **Fine-Tuning Dataset**: [Super Emotion](https://huggingface.co/datasets/cirimus/super-emotion)
- **Number of Labels**: 7
- **Problem Type**: Single-label classification
- **Language**: English
- **License**: [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/)
- **Fine-Tuning Framework**: Hugging Face Transformers

---

### Example Usage

Here’s how to use the model with Hugging Face Transformers:

```python
from transformers import pipeline

# Load the model
classifier = pipeline(
    "text-classification", 
    model="cirimus/modernbert-base-emotions",
    top_k=5
)

text = "I can't believe this just happened!"
predictions = classifier(text)

# Print top 3 detected emotions
sorted_preds = sorted(predictions[0], key=lambda x: x['score'], reverse=True)
top_3 = sorted_preds[:3]

print("\nTop 3 emotions detected:")
for pred in top_3:
    print(f"\t{pred['label']:10s} : {pred['score']:.3f}")

# Example output:
# Top 3 emotions detected:
#        SURPRISE   : 0.913
#        SADNESS    : 0.033
#        NEUTRAL    : 0.021
```

---

### How the Model Was Created

The model was fine-tuned for 2 epochs using the following hyperparameters:

- **Learning Rate**: `2e-5`
- **Batch Size**: 16
- **Weight Decay**: `0.01`
- **Warmup Steps**: Cosine decay scheduling
- **Optimizer**: AdamW
- **Evaluation Metrics**: Precision, Recall, F1 Score (macro), Accuracy

---

### Evaluation Results

As evaluated on the joint test-set:

|     | Accuracy  | Precision | Recall  | F1    | MCC   | Support |
|----------|----------|-----------|---------|-------|-------|---------|
| **macro avg** | 0.872   | 0.827    | 0.850   | 0.836 | 0.840 | 56310   |
| NEUTRAL  | 0.965   | 0.711    | 0.842   | 0.771 | 0.755 | 3907    |
| SURPRISE | 0.976   | 0.693    | 0.772   | 0.730 | 0.719 | 2374    |
| FEAR     | 0.975   | 0.897    | 0.841   | 0.868 | 0.855 | 5608    |
| SADNESS  | 0.960   | 0.910    | 0.937   | 0.923 | 0.896 | 14547   |
| JOY      | 0.941   | 0.933    | 0.872   | 0.902 | 0.861 | 17328   |
| ANGER    | 0.964   | 0.912    | 0.818   | 0.862 | 0.843 | 7793    |
| LOVE     | 0.962   | 0.734    | 0.867   | 0.795 | 0.778 | 4753    |



![Confusion Matrix](confusion_matrix.png)

---

### Intended Use

The model is designed for emotion classification in English-language text, particularly useful for:

- Social media sentiment analysis
- Customer feedback evaluation
- Large scale behavioral or psychological research

The model is designed for fast and accurate emotion detection but struggles with subtle expressions or indirect references to emotions (e.g., "*I find myself remembering the little things you say, long after you've said them.*")

---

### Limitations and Biases

- **Data Bias**: The dataset is aggregated from multiple sources and may contain biases in annotation and class distribution.
- **Underrepresented Classes**: Some emotions have fewer samples, affecting their classification performance.
- **Context Dependence**: The model classifies individual sentences and may not perform well on multi-sentence contexts.

---

### Environmental Impact

- **Hardware Used**: NVIDIA RTX 4090
- **Training Time**: < 1 hour
- **Carbon Emissions**: ~0.04 kg CO2 (estimated via [ML CO2 Impact Calculator](https://mlco2.github.io/impact))

---

### Citation

If you use this model, please cite:

```bibtex
@inproceedings{JdFE2025b,
  title = {Emotion Detection with ModernBERT},
  author = {Enric Junqu\'e de Fortuny},
  year = {2025},
  howpublished = {\url{https://huggingface.co/your_model_name_here}},
}
```
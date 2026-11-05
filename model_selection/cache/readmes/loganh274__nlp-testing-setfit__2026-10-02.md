---
language:
- en
license: apache-2.0
library_name: setfit
tags:
- setfit
- sentence-transformers
- text-classification
- sentiment-analysis
- few-shot-learning
pipeline_tag: text-classification
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: SetFit Sentiment Analysis
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.88
    - name: F1 (Weighted)
      type: f1
      value: 0.8805050505050506
    - name: Precision (Weighted)
      type: precision
      value: 0.8883333333333333
    - name: Recall (Weighted)
      type: recall
      value: 0.88
---

# SetFit Sentiment Analysis Model

This is a [SetFit](https://github.com/huggingface/setfit) model fine-tuned for sentiment classification on customer feedback data.

## Model Description

| Property | Value |
|----------|-------|
| **Base Model** | [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5) |
| **Total Parameters** | 109,482,240 |
| **Trainable Parameters** | 109,482,240 |
| **Body Parameters** | 109,482,240 |
| **Head Parameters** | 0 |
| **Model Size** | 417.64 MB |
| **Labels** | [0, 1, 2, 3, 4] |
| **Number of Classes** | 5 |
| **Serialization** | safetensors |

## Training Configuration

| Parameter | Value |
|-----------|-------|
| **Batch Size** | 16 |
| **Epochs** | [1, 16] |
| **Training Samples** | 540 |
| **Test Samples** | 100 |
| **Loss Function** | CosineSimilarityLoss |
| **Metric for Best Model** | embedding_loss |

### Training Progress

- **Initial Loss:** 0.2366
- **Final Loss:** 0.0893
- **Eval Loss:** 0.0984
- **Training Runtime:** 800.2981 seconds
- **Samples/Second:** 13.4950

## Evaluation Results

| Metric | Score |
|--------|-------|
| **Accuracy** | 0.8800 |
| **F1 (Weighted)** | 0.8805 |
| **F1 (Macro)** | 0.8805 |
| **Precision (Weighted)** | 0.8883 |
| **Precision (Macro)** | 0.8883 |
| **Recall (Weighted)** | 0.8800 |
| **Recall (Macro)** | 0.8800 |

### Per-Class Performance

```
              precision    recall  f1-score   support

           0       0.90      0.90      0.90        20
           1       0.75      0.75      0.75        20
           2       0.79      0.95      0.86        20
           3       1.00      0.80      0.89        20
           4       1.00      1.00      1.00        20

    accuracy                           0.88       100
   macro avg       0.89      0.88      0.88       100
weighted avg       0.89      0.88      0.88       100

```

## Visualizations

### Evaluation Metrics Overview
<p align="center">
  <img src="evaluation_metrics.png" alt="Evaluation Metrics" width="800"/>
</p>

### Confusion Matrix
<p align="center">
  <img src="confusion_matrix.png" alt="Confusion Matrix" width="600"/>
</p>

### Training Loss Curve
<p align="center">
  <img src="loss_curve.png" alt="Training Loss Curve" width="600"/>
</p>

### Learning Rate Schedule
<p align="center">
  <img src="learning_rate.png" alt="Learning Rate Schedule" width="600"/>
</p>

## Usage

```python
from setfit import SetFitModel

# Load the model
model = SetFitModel.from_pretrained("loganh274/nlp-testing-setfit")

# Single prediction
text = "This product exceeded my expectations!"
prediction = model.predict([text])
print(f"Sentiment: {prediction[0]}")

# Batch prediction
texts = [
    "Amazing quality, highly recommend!",
    "It's okay, nothing special.",
    "Terrible experience, very disappointed.",
]
predictions = model.predict(texts)
probabilities = model.predict_proba(texts)

for text, pred, prob in zip(texts, predictions, probabilities):
    print(f"Text: {text}")
    print(f"  Prediction: {pred}, Confidence: {max(prob):.2%}")
```

## Label Mapping

| Label | Sentiment |
|-------|-----------|
| 0 | Negative |
| 1 | Somewhat Negative |
| 2 | Neutral |
| 3 | Somewhat Positive |
| 4 | Positive |

## Environment

| Package | Version |
|---------|---------|
| Python | 3.11.14 |
| SetFit | 1.1.3 |
| PyTorch | 2.9.1 |
| scikit-learn | 1.8.0 |
| Transformers | N/A |

## Citation

If you use this model, please cite the SetFit paper:

```bibtex
@article{tunstall2022efficient,
  title={Efficient Few-Shot Learning Without Prompts},
  author={Tunstall, Lewis and Reimers, Nils and Jo, Unso Eun Seo and Bates, Luke and Korat, Daniel and Wasserblat, Moshe and Pereg, Oren},
  journal={arXiv preprint arXiv:2209.11055},
  year={2022}
}
```

## License

Apache 2.0

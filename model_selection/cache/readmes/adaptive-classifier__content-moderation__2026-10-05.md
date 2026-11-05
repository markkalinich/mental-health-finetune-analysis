---
language: multilingual
tags:
- adaptive-classifier
- text-classification
- continuous-learning
license: apache-2.0
---

# Adaptive Classifier

This model is an instance of an [adaptive-classifier](https://github.com/codelion/adaptive-classifier) that allows for continuous learning and dynamic class addition.

You can install it with `pip install adaptive-classifier`.

## Model Details

- Base Model: answerdotai/ModernBERT-base
- Number of Classes: 3
- Total Examples: 15
- Embedding Dimension: 768

## Class Distribution

```
appropriate: 5 examples (33.3%)
inappropriate: 5 examples (33.3%)
spam: 5 examples (33.3%)
```

## Usage

```python
from adaptive_classifier import AdaptiveClassifier

# Load the model
classifier = AdaptiveClassifier.from_pretrained("adaptive-classifier/model-name")

# Make predictions
text = "Your text here"
predictions = classifier.predict(text)
print(predictions)  # List of (label, confidence) tuples

# Add new examples
texts = ["Example 1", "Example 2"]
labels = ["class1", "class2"]
classifier.add_examples(texts, labels)
```

## Training Details

- Training Steps: 8
- Examples per Class: See distribution above
- Prototype Memory: Active
- Neural Adaptation: Active

## Limitations

This model:
- Requires at least 3 examples per class
- Has a maximum of 150 examples per class
- Updates prototypes every 10 examples

## Citation

```bibtex
@software{adaptive_classifier,
  title = {Adaptive Classifier: Dynamic Text Classification with Continuous Learning},
  author = {Sharma, Asankhaya},
  year = {2025},
  publisher = {GitHub},
  url = {https://github.com/codelion/adaptive-classifier}
}
```

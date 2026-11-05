---
license: apache-2.0
datasets:
- savalera/isear-from-original
language:
- en
metrics:
- accuracy
- f1
base_model:
- google-bert/bert-base-uncased
pipeline_tag: text-classification
tags:
- emotion
- psychology
- medical
---
# ISEAR Emotion Classifier

A BERT-based model that classifies text into seven basic emotions, fine-tuned on the ISEAR dataset.

## Model Overview

This model predicts one of seven emotions from textual descriptions:

| Label | Emotion | Definition                           |
| ----- | ------- | ------------------------------------ |
| 0     | Joy     | Happiness, pleasure, or satisfaction |
| 1     | Fear    | Anxiety about threat or danger       |
| 2     | Anger   | Strong displeasure or antagonism     |
| 3     | Sadness | Feeling of loss or disadvantage      |
| 4     | Disgust | Aversion or revulsion                |
| 5     | Shame   | Embarrassment or humiliation         |
| 6     | Guilt   | Feeling responsible for wrongdoing   |

## Performance

**Validation metrics:**

- Accuracy: 70.98%

Top performing emotions: Joy (92% F1), Fear (78% F1)  
Most challenging: Shame (59% F1), Anger (60% F1)

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="savalera/isear-emotion-classifier")
result = classifier("I received a surprise visit from my best friend who I hadn't seen in years.")
print(result) # [{'label': 'joy', 'score': 0.9685400724411011}]
```

## Training

- Base model: bert-base-uncased
- Dataset: [ISEAR](https://huggingface.co/datasets/savalera/isear-from-original) (International Survey on Emotion Antecedents and Reactions)

## Limitations

The model may struggle to distinguish between closely related emotions (especially shame/guilt), which reflects inherent challenges in emotion classification that even humans face.

## Ethical Usage Guidelines

This model analyzes textual descriptions to classify emotions. While it has many potential applications, users should consider these ethical guidelines:

### Recommended Applications
- Academic research on emotional expression and recognition
- Healthcare applications for mental health support under appropriate supervision
- Enhancing communication effectiveness through better emotional awareness
- Supporting team coaching programs that foster psychological safety, enchance communication effectiventess and collaboration

### Usage Considerations
- Some jurisdictions have regulations around emotion recognition technology, particularly in workplace and educational settings
- Privacy and consent are important when analyzing personal emotional expressions
- The model's predictions should be treated as probabilistic rather than definitive assessments of emotional states

Users should be aware of restrictions on emotion recognition systems and ensure any applications developed using this model comply with regulatory requirements. This model should not be used for commercial emotion categorization systems to infer emotions of a natural person.

## Citation

If you use this model in your research, please cite it directly:
```bibtex
@misc{savalera2025isear,
  title={ISEAR Emotion Classifier},
  author={Savalera},
  year={2025},
  howpublished={\url{https://huggingface.co/savalera/isear-emotion-classifier}}
}
```

This model was trained on the [ISEAR dataset](https://huggingface.co/datasets/savalera/isear-from-original), which was derived from research by Scherer & Wallbott (1994).

## License

Apache License 2.0
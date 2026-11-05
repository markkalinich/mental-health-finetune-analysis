---
language:
  - en
license: apache-2.0
base_model: bert-base-uncased
tags:
  - text-classification
  - emotion-classification
  - fine-tuned
  - bert
  - nlp
datasets:
  - dair-ai/emotion
metrics:
  - accuracy
  - f1
library_name: transformers
pipeline_tag: text-classification
widget:
  - text: "I am so happy today!"
    example_title: "Joy"
  - text: "I feel really scared and anxious about tomorrow."
    example_title: "Fear"
  - text: "This makes me so angry!"
    example_title: "Anger"
  - text: "I love spending time with my family."
    example_title: "Love"
---

# BERT Emotion Classifier (Fine-tuned)

Fine-tuned [bert-base-uncased](https://huggingface.co/bert-base-uncased) for **6-class emotion classification** on the [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset.

## Model Description

- **Author:** Neeraj Gupta ([@neeraj](https://huggingface.co/neeraj-miniOrange))
- **Task:** Text Classification (Emotion Detection)
- **Base model:** `bert-base-uncased`
- **Classes:** sadness, joy, love, anger, fear, surprise
- **Framework:** PyTorch + Hugging Face Transformers

## Performance

| Metric | Score |
|--------|-------|
| **Accuracy** | 91.75% |
| **Weighted F1** | 91.64% |

*Evaluated on the validation split after training.*

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="neeraj-miniOrange/bert-emotion-finetuned"
)

result = classifier("I am so happy today!")
print(result)
# [{'label': 'joy', 'score': 0.98...}]
```

## Training Details

| Hyperparameter | Value |
|----------------|-------|
| Epochs | 2 |
| Learning rate | 2e-4 |
| Batch size | 64 |
| Weight decay | 0.01 |
| Optimizer | AdamW |

**Data split:** 70% train / 20% test / 10% validation (stratified)

## Limitations

- Trained on short English tweets; may not generalize well to long-form text or other languages.
- Emotion labels are subjective; the model reflects biases present in the training data.
- Not intended for clinical or mental health diagnosis.

## Links

- **Dataset:** [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion)
- **Base model:** [bert-base-uncased](https://huggingface.co/bert-base-uncased)

## Citation

If you use this model, please cite the BERT paper:

```bibtex
@article{devlin2019bert,
  title={BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding},
  author={Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  journal={NAACL},
  year={2019}
}
```

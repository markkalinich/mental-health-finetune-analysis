---
language:
- sd
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- sindhi
- xlm-roberta
- text-classification
base_model: FacebookAI/xlm-roberta-base
license: mit
metrics:
- accuracy
- precision
- recall
- f1
datasets:
- alinawazmahar/Sindhi_Sentiment_dataset
---

# Sindhi Sentiment Analysis

This repository contains a fine-tuned [XLM-RoBERTa Base](https://huggingface.co/FacebookAI/xlm-roberta-base) model for 3-class sentiment classification in Sindhi. The model predicts one of the following labels:

- positive
- neutral
- negative

## Model details

- Base model: FacebookAI/xlm-roberta-base
- Task: text classification
- Language: Sindhi (sd)
- Labels: positive, neutral, negative
- Framework: Hugging Face Transformers
- Max sequence length: 128 tokens

## Intended use

This model is intended for research, experimentation, and lightweight production prototyping on Sindhi-language sentiment analysis tasks. It may be useful for short-text classification such as reviews, feedback, and social-media snippets.

It should not be used as the only basis for high-stakes decisions. Performance can vary by domain, dialect, and writing style, and human review is recommended when errors could affect people or organizations.

## Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="DanishMahdi/snd_sentiment_analysis",
    tokenizer="DanishMahdi/snd_sentiment_analysis",
)

texts = [
    "هي فلم تمام سٺي آهي.",
    "هي سروس تمام خراب آهي.",
    "اڄ عام ڏينهن آهي.",
]

for text in texts:
    print(text)
    print(classifier(text))
```

## Evaluation summary

The saved model artifacts in this repository report the following evaluation results on the held-out test split:

- Accuracy: 0.7553
- Macro precision: 0.7604
- Macro recall: 0.7554
- Macro F1: 0.7549

These values are taken from the model’s saved evaluation output and reflect the performance reported for the final checkpoint in this project.

## Model card notes

This repository contains the trained model weights and tokenizer files, along with evaluation outputs. The full training script and dataset card are not included here, so the strongest claims that can be made are the ones supported by the saved artifacts in this project.

## Limitations

- This model may not generalize equally across all Sindhi dialects and writing styles.
- Neutral sentiment is often harder to predict than positive or negative sentiment.
- Results may vary depending on the application domain and the class distribution of the input data.
- Confidence values should be interpreted cautiously unless calibration is evaluated separately.

## Acknowledgements

This model builds on the pretrained [XLM-RoBERTa Base](https://huggingface.co/FacebookAI/xlm-roberta-base) model.

## License

This model card uses the MIT license, which is compatible with the XLM-RoBERTa base model licensing used in this project.
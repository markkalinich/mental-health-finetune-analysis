---
library_name: transformers
license: mit
base_model: indobenchmark/indobert-base-p2
tags:
- generated_from_trainer
- indobert
- emotion
- classification
- mood-notes
metrics:
- accuracy
- f1
model-index:
- name: results_indobert
  results: []
language:
- id
---
This model is a fine-tuned version of [indobenchmark/indobert-base-p2](https://huggingface.co/indobenchmark/indobert-base-p2). It is specifically designed to classify emotions in Indonesian text into 5 categories: **Joy, Anger, Sadness, Fear, and Love.** The model achieved an accuracy of 81.78% on the evaluation set.

## Intended uses & limitations

- **Use cases**: Sentiment analysis, social media monitoring, and enhancing chatbot emotional intelligence.
- **Limitations**: Limitations: The model's performance may decrease when handling complex sarcasm or non-standard informal language that is less commonly used.

## Training and evaluation data

The model was trained on 6000+ data samples, combining the Indonesian Twitter Emotion Dataset by meisaputri21, Dataset IndoNLU EmoT, and 1,000 generated data samples to improve robustness.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: AdamW with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|
| 0.6961        | 1.0   | 320  | 0.6332          | 0.7709   | 0.7707 |
| 0.4698        | 2.0   | 640  | 0.5622          | 0.8092   | 0.8097 |
| 0.189         | 3.0   | 960  | 0.7534          | 0.7991   | 0.7993 |
| 0.1074        | 4.0   | 1280 | 0.9063          | 0.8100   | 0.8123 |
| 0.0548        | 5.0   | 1600 | 1.1038          | 0.8108   | 0.8130 |
| 0.0235        | 6.0   | 1920 | 1.1756          | 0.8092   | 0.8113 |
| 0.0167        | 7.0   | 2240 | 1.1835          | 0.8170   | 0.8182 |
| 0.0004        | 8.0   | 2560 | 1.1934          | 0.8202   | 0.8217 |
| 0.0003        | 9.0   | 2880 | 1.2152          | 0.8194   | 0.8207 |
| 0.0007        | 10.0  | 3200 | 1.2226          | 0.8178   | 0.8196 |

### Framework versions

- Transformers 4.57.6
- Pytorch 2.9.0+cu126
- Datasets 4.0.0
- Tokenizers 0.22.2

## Usage

```python
from transformers import pipeline

# Load the model
classifier = pipeline("text-classification", model="mrezadit/indobert-emotion-classification-v2")
# If score < 0.85, classify as 'neutral'
threshold = 0.85

text = "Sumpah gue seneng banget hari ini!"
result = classifier(text)[0]

label = result['label'] if result['score'] >= threshold else "neutral"
print(f"Teks: {text}\nHasil: {label}")
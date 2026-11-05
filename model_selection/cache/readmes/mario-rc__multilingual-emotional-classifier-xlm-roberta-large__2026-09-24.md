---
license: mit
language:
- en
- es
- multilingual
library_name: transformers
pipeline_tag: text-classification
base_model: FacebookAI/xlm-roberta-large
tags:
- emotion-classification
- multilingual
- spanish
- english
- xlm-roberta
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: Multilingual Emotional Classifier XLM-RoBERTa-Large
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: Multilingual DailyDialog and EmpatheticDialogues-derived corpus
      type: custom
    metrics:
    - type: accuracy
      value: 0.6640
      name: Test Accuracy
    - type: f1
      value: 0.6658
      name: Test Macro F1
    - type: precision
      value: 0.6750
      name: Test Macro Precision
    - type: recall
      value: 0.6640
      name: Test Macro Recall
---

# Multilingual Emotional Classifier XLM-RoBERTa-Large

This model is a fine-tuned [`FacebookAI/xlm-roberta-large`](https://huggingface.co/FacebookAI/xlm-roberta-large) sequence classifier for multilingual emotion recognition in English and Spanish dialogue utterances.

Source code: [`Mario-RC/multilingual-emotion-classifier`](https://github.com/Mario-RC/multilingual-emotion-classifier)

## Model Details

- Model repository: [`mario-rc/multilingual-emotional-classifier-xlm-roberta-large`](https://huggingface.co/mario-rc/multilingual-emotional-classifier-xlm-roberta-large)
- Base model: [`FacebookAI/xlm-roberta-large`](https://huggingface.co/FacebookAI/xlm-roberta-large)
- Architecture: `XLMRobertaForSequenceClassification`
- Task: text classification / emotion classification
- Languages: English, Spanish
- Max sequence length: 128 tokens
- Number of labels: 7

## Emotion Labels

The model predicts one of seven normalized emotion labels:

`anger`, `disgust`, `fear`, `happiness`, `neutral`, `sadness`, `surprise`

## Training Data

The training pipeline combines DailyDialog and EmpatheticDialogues-derived CSV resources into a multilingual English/Spanish dataset. EmpatheticDialogues labels were mapped into the seven normalized categories above, while ambiguous or underrepresented labels were removed. The training split was resampled to reduce the majority `neutral` class and upsample minority classes.

## Training Setup

- Framework: Hugging Face Transformers
- Base checkpoint: [`FacebookAI/xlm-roberta-large`](https://huggingface.co/FacebookAI/xlm-roberta-large)
- Task: sequence classification
- Max sequence length: 128
- Epochs: 3
- Learning rate: `5e-6`
- Batch size: 32
- Dropout: 0.2
- Seed: 42

## Evaluation

The confusion matrix shows true vs. predicted emotion labels on the multilingual
test split. Diagonal cells indicate correct classifications, while off-diagonal
cells show the main confusions between emotion classes.

![Confusion matrix](plots/confusion_matrix.png)

## Model Comparison

| Model | Base model | Test accuracy | Test Macro F1 | GPT-4 ES benchmark | GPT-4 EN benchmark |
| :--- | :---: | :---: | :---: | :---: | :---: |
| [Emotional Classifier BERT-Base-Multilingual-Cased](https://huggingface.co/mario-rc/emotional-classifier-bert-base-multilingual-cased) | [`google-bert/bert-base-multilingual-cased`](https://huggingface.co/google-bert/bert-base-multilingual-cased) | 0.5506 | 0.5468 | 72.91% | 70.81% |
| [Emotional Classifier BERT-Base-Multilingual-Uncased](https://huggingface.co/mario-rc/emotional-classifier-bert-base-multilingual-uncased) | [`google-bert/bert-base-multilingual-uncased`](https://huggingface.co/google-bert/bert-base-multilingual-uncased) | 0.5560 | 0.55 | 74.25% | 74.16% |
| [Multilingual Emotional Classifier XLM-RoBERTa-Base](https://huggingface.co/mario-rc/multilingual-emotional-classifier-xlm-roberta-base) | [`FacebookAI/xlm-roberta-base`](https://huggingface.co/FacebookAI/xlm-roberta-base) | 0.5171 | 0.5078 | 82.61% | 76.17% |
| [Multilingual Emotional Classifier XLM-RoBERTa-Large](https://huggingface.co/mario-rc/multilingual-emotional-classifier-xlm-roberta-large) | [`FacebookAI/xlm-roberta-large`](https://huggingface.co/FacebookAI/xlm-roberta-large) | 0.6640 | 0.6658 | 85.95% | 79.19% |

## Usage

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

model_id = "mario-rc/multilingual-emotional-classifier-xlm-roberta-large"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)

classifier = pipeline("text-classification", model=model, tokenizer=tokenizer)

print(classifier("I feel great today."))
print(classifier("Estoy preocupado por manana."))
```

## Limitations

The model is designed for short dialogue utterances and seven broad emotion categories. Predictions may be less reliable for long documents, sarcasm, mixed emotions, domain-specific language, or languages beyond English and Spanish.

## Citation

This work is detailed in Section 4.4.3, User Emotion Recognition, of:

**Personal Assistant with Emotional and Multilingual Capabilities for Social Robots**  
M. Rodriguez-Cantelar, PhD Dissertation, Universidad Politecnica de Madrid, 2025.

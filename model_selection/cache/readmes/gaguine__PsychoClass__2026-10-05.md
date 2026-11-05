---
license: apache-2.0
language:
  - en
library_name: transformers
pipeline_tag: text-classification
base_model: distilbert/distilbert-base-multilingual-cased
tags:
  - distilbert
  - text-classification
  - multiclass-classification
  - mental-health
  - pytorch
metrics:
  - f1
---



# Mental State Text Classification with DistilBERT

This model is a fine-tuned version of
[`distilbert/distilbert-base-multilingual-cased`](https://huggingface.co/distilbert/distilbert-base-multilingual-cased)
for multiclass classification of short English statements into seven mental-state categories.

It was developed as part of a 2026 master's thesis on language modelling and fine-tuning language models for mental-state text classification.

> **Important:** This is a research model, not a medical or psychological diagnostic system. Its output must not be interpreted as a clinical diagnosis, risk assessment, or substitute for a qualified professional.

## Model description

- **Task:** Multiclass text classification
- **Base model:** `distilbert/distilbert-base-multilingual-cased`
- **Architecture:** DistilBERT with a sequence-classification head
- **Number of classes:** 7
- **Recommended input:** One sentence or a short statement
- **Maximum training sequence length:** 256 tokens
- **Framework:** PyTorch and Hugging Face Transformers

The base model contains six Transformer layers, a hidden size of 768, 12 attention heads, and approximately 134 million parameters. It was selected to provide a practical balance between classification performance and computational requirements.

## Labels

| ID | Label |
|---:|---|
| 0 | Normal |
| 1 | Depression |
| 2 | Suicidal |
| 3 | Anxiety |
| 4 | Stress |
| 5 | Bipolar |
| 6 | Personality disorder |

The predicted categories describe patterns learned from the dataset. They do not establish whether a person has any medical condition.

## Intended use

The model is intended for:

- research on multiclass text classification;
- educational demonstrations of fine-tuning DistilBERT;
- exploratory analysis of short statements;
- prototyping systems that require human review of model predictions.

The model is not intended for:

- clinical diagnosis or treatment decisions;
- emergency or suicide-risk assessment;
- autonomous moderation or decisions affecting access to care, employment, education, insurance, or other high-impact services;
- surveillance or profiling of individuals;
- use without appropriate privacy protections and informed consent.

## Training data

The model was fine-tuned on the Kaggle
[`Sentiment Analysis for Mental Health`](https://www.kaggle.com/datasets/suchintikasarkar/sentiment-analysis-for-mental-health)
dataset. The dataset contains 51,074 labelled statements collected from several public online sources, including social-media platforms, forums, Twitter/X, and Reddit.

The class distribution reported in the thesis is imbalanced:

| Class | Approximate share |
|---|---:|
| Normal | 31% |
| Depression | 29% |
| Suicidal | 20% |
| Anxiety | 7% |
| Bipolar | 5% |
| Stress | 5% |
| Personality disorder | 2% |

Because the dataset aggregates multiple sources, its examples may differ in writing style, length, subject matter, annotation methods, and annotation reliability.

The data was randomly divided using seed 42 into approximately:

- 80% training data;
- 10% validation data;
- 10% test data.


## Training procedure

| Hyperparameter | Value |
|---|---:|
| Learning rate | `3e-5` |
| Training batch size per device | `8` |
| Evaluation batch size per device | `8` |
| Epochs | `15` |
| Maximum sequence length | `256` |
| Weight decay | `0.01` |
| Warmup ratio | `0.1` |
| Random seed | `42` |

Logging, validation, and checkpoint saving were performed after every epoch. Checkpoint selection was configured to maximize Macro F1.

## Evaluation

Macro F1 was the main evaluation metric because the dataset is imbalanced. The fine-tuned model reached a **test Macro F1 of 0.803**, compared with **0.096** for the unfine-tuned base model in the reported experiment.

### Test F1 by class

| Class | Base model | Fine-tuned model |
|---|---:|---:|
| Normal | 0.278 | 0.937 |
| Depression | 0.000 | 0.756 |
| Suicidal | 0.332 | 0.673 |
| Anxiety | 0.000 | 0.889 |
| Stress | 0.048 | 0.719 |
| Bipolar | 0.000 | 0.872 |
| Personality disorder | 0.014 | 0.774 |
| **Macro F1** | **0.096** | **0.803** |

The most important reported confusion was between the `Suicidal` and `Depression` categories. The model also sometimes classified `Stress` examples as `Normal`.



## Limitations and risks

- The dataset is class-imbalanced, and the least frequent classes may be less reliably represented.
- The dataset combines several online sources with potentially inconsistent annotation standards.
- Labels may reflect subjective or noisy annotations rather than clinical assessments.
- The model may learn unintended correlations with text length, vocabulary, platform, or writing style.
- Removing punctuation may discard useful emotional or semantic information.
- The model was designed for individual sentences and short statements. Long documents are truncated and may require sentence-level processing and aggregation.
- The model has difficulty distinguishing semantically related categories, especially `Depression` and `Suicidal`.
- Performance may decrease on languages, communities, platforms, and writing styles that differ from the training data.
- A high softmax score is model confidence, not proof that the predicted category is correct.



```bibtex
@mastersthesis{butera2026mentalstate,
  author = {Butera, Gaetano Antonio},
  title = {Language Modelling and Fine-Tuning Large Language Models for the Classification of Texts by Mental-State Category},
  school = {Volga State University of Technology},
  year = {2026}
}
```


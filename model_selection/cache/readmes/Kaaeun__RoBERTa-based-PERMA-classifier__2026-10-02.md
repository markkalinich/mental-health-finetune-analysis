---
language:
- en
license: mit
tags:
- text-classification
- multi-label-classification
- roberta
- mental-health
- well-being
- perma
- reddit
pipeline_tag: text-classification
---

# PERMA Well-Being Deficit Classifier for Depression-Related Reddit Posts

This repository contains a RoBERTa-based multi-label text classification model developed for identifying PERMA-related well-being deficit signals in depression-related Reddit posts.

The model was developed as part of the study **“Identifying PERMA-Related Well-Being Deficit Signals in Depression-Related Reddit Posts: A Multi-Label Machine Learning Study.”**

## Model Description

This model classifies English-language text into five PERMA-related well-being deficit dimensions:

1. Positive Emotion
2. Engagement
3. Relationships
4. Meaning
5. Accomplishment

Unlike conventional applications of PERMA that measure positive well-being, this model operationalizes the PERMA framework as a way to detect the **absence, deprivation, loss, or longing** of well-being resources in depression-related online discourse.

The task is formulated as a **multi-label classification** problem. Therefore, multiple PERMA dimensions can be assigned to a single post.

## Intended Use

This model is intended for academic and research use, particularly for studies analyzing:

- mental health discourse in online communities
- depression-related self-expression
- well-being deficits in user-generated text
- multidimensional psychological resource depletion
- PERMA-based computational text analysis

The model may be useful for researchers interested in moving beyond binary depression or risk detection toward a more interpretable, multidimensional representation of psychological vulnerability.

## Out-of-Scope Use

This model should **not** be used as:

- a clinical diagnostic tool
- a suicide risk assessment tool
- a substitute for professional mental health evaluation
- a decision-making system for intervention, treatment, or access to care
- a tool for identifying or profiling individual users without ethical review

Predictions should be interpreted as research-oriented signals rather than clinical judgments.

## Labels

The model predicts five binary labels. A value of `1` indicates that the text contains signals of deprivation, absence, or loss in that PERMA dimension. A value of `0` indicates that the dimension is not clearly indicated as deprived.

| Label | Dimension | Definition |
|---|---|---|
| P | Positive Emotion | Emotional numbness, anhedonia, absence of positive affect, or difficulty experiencing positive emotions |
| E | Engagement | Loss of interest, reduced absorption in activities, lack of motivation, or concentration difficulties |
| R | Relationships | Isolation, disconnection, loneliness, lack of belonging, or absence of interpersonal support |
| M | Meaning | Loss of purpose, emptiness, meaninglessness, or difficulty finding value in life |
| A | Accomplishment | Feelings of failure, helplessness, inability to achieve, frustration, or reduced self-efficacy |

## Dataset

The model was developed using posts from Reddit’s `r/depression` community. Reddit was selected because users frequently express personal experiences and psychological states in narrative text. The `r/depression` subreddit was selected as a depression-related online community.

- Platform: Reddit
- Community: r/depression
- Collection period: January 1, 2025 to December 31, 2025
- Full collected corpus: 133,220 posts
- Analytic sample: 4,479 posts
- Input text: post title + post body
- Language: English
- Metadata: not used

Posts that were deleted, removed, empty, or not written in English were excluded from analysis.

## Annotation

The analytic sample was human-coded according to the five PERMA dimensions. The annotation scheme was based on the PERMA model, but adapted to identify well-being **deficit signals** rather than positive well-being states.

Coding was conducted using a multi-label approach. Each post could receive multiple PERMA labels because the five dimensions were not treated as mutually exclusive.

Two trained researchers independently coded the data using the same coding manual. Intercoder reliability was assessed using **Gwet’s AC1**, which was selected because it is more stable than Cohen’s kappa under imbalanced category distributions.

### Label Distribution

| Label | Negative | Positive | Positive Rate |
|---|---:|---:|---:|
| Positive Emotion | 1,454 | 3,025 | 67.54% |
| Engagement | 3,329 | 1,150 | 25.68% |
| Relationships | 2,617 | 1,862 | 41.57% |
| Meaning | 2,973 | 1,506 | 33.62% |
| Accomplishment | 3,407 | 1,072 | 23.93% |

### Intercoder Reliability

| Dimension | Gwet’s AC1 | Agreement |
|---|---:|---:|
| Positive Emotion | 0.606 | 78.2% |
| Engagement | 0.970 | 97.1% |
| Relationships | 0.820 | 86.6% |
| Meaning | 0.901 | 91.6% |
| Accomplishment | 0.956 | 95.8% |

## Preprocessing

Minimal preprocessing was applied to preserve the original semantic content of Reddit posts.

The preprocessing steps included:

- replacing missing text entries with empty strings
- removing leading and trailing whitespace
- excluding empty posts
- lowercasing text
- converting PERMA annotations into binary numeric labels

No aggressive normalization such as lemmatization, stemming, or stopword removal was applied.

## Data Split

The dataset was split into training, validation, and test sets using a robust stratified splitting procedure for multi-label classification. A combination-based stratification key was created by concatenating the five binary labels into a label-combination string.

Rare label combinations were assigned to the training set to avoid unstable evaluation splits.

| Split | N | P+ | E+ | R+ | M+ | A+ |
|---|---:|---:|---:|---:|---:|---:|
| Train | 3,583 | 67.5% | 25.7% | 41.6% | 33.6% | 23.9% |
| Validation | 450 | 67.3% | 25.8% | 42.0% | 33.3% | 24.2% |
| Test | 446 | 67.9% | 25.1% | 41.3% | 34.1% | 23.5% |

## Model Architecture

The model is based on `roberta-base` with a multi-label classification head. The model outputs five label-specific logits, and sigmoid activation is applied to obtain probabilities for each PERMA dimension.

- Base architecture: RoBERTa
- Task: Multi-label sequence classification
- Number of labels: 5
- Loss function: binary cross-entropy
- Maximum sequence length: 512
- Tokenizer: RoBERTa tokenizer

## Training Configuration

The supervised RoBERTa model was trained with the following configuration:

| Hyperparameter | Value |
|---|---|
| Base model | roberta-base |
| Learning rate | 3e-5 |
| Batch size | 8 |
| Epochs | 5 |
| Weight decay | 0.01 |
| FP16 | enabled |
| Seed | 42 |

In the full study, a three-seed RoBERTa ensemble was also evaluated using seeds `[13, 42, 77]`, with soft voting through probability averaging. The ensemble model was selected as the final model in the paper because it achieved the best Macro-F1 and showed more balanced performance across PERMA dimensions.

## Decision Thresholds

Because this is a multi-label classification task, a fixed 0.5 threshold may not be optimal for all labels. The study therefore applied validation-based label-wise threshold tuning.

For the single supervised RoBERTa model, the optimized thresholds were:

| Label | Threshold |
|---|---:|
| Positive Emotion | 0.52 |
| Engagement | 0.33 |
| Relationships | 0.22 |
| Meaning | 0.30 |
| Accomplishment | 0.37 |

For the RoBERTa ensemble model reported in the paper, the optimized thresholds were:

| Label | Threshold |
|---|---:|
| Positive Emotion | 0.58 |
| Engagement | 0.14 |
| Relationships | 0.51 |
| Meaning | 0.20 |
| Accomplishment | 0.39 |

## Evaluation

The model was evaluated on the held-out test set using Micro-F1, Macro-F1, and label-wise F1 scores.

In the study, the RoBERTa ensemble model was selected as the final model because it achieved the best Macro-F1 and provided more balanced performance across PERMA dimensions.

### RoBERTa Ensemble Performance

| Metric | Score |
|---|---:|
| Micro-F1 | 0.661 |
| Macro-F1 | 0.638 |

| Label | Precision | Recall | F1 |
|---|---:|---:|---:|
| Positive Emotion | 0.735 | 0.878 | 0.800 |
| Engagement | 0.351 | 0.866 | 0.500 |
| Relationships | 0.724 | 0.772 | 0.747 |
| Meaning | 0.419 | 0.974 | 0.586 |
| Accomplishment | 0.493 | 0.638 | 0.556 |

### Single RoBERTa Model Performance

| Metric | Score |
|---|---:|
| Micro-F1 | 0.676 |
| Macro-F1 | 0.634 |

| Label | Precision | Recall | F1 |
|---|---:|---:|---:|
| Positive Emotion | 0.731 | 0.845 | 0.784 |
| Engagement | 0.475 | 0.589 | 0.526 |
| Relationships | 0.686 | 0.853 | 0.760 |
| Meaning | 0.505 | 0.697 | 0.586 |
| Accomplishment | 0.509 | 0.514 | 0.512 |

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "YOUR_USERNAME/YOUR_MODEL_NAME"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "I feel empty and disconnected from everyone. I do not know what the point of anything is anymore."

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    padding=True,
    max_length=256
)

with torch.no_grad():
    outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.sigmoid(logits)

print(probabilities)

---
library_name: transformers
tags:
- turkish
- sentiment-analysis
- text-classification
- bert
- berturk
license: mit
datasets:
- winvoker/turkish-sentiment-analysis-dataset
language:
- tr
metrics:
- accuracy
- precision
- recall
- f1
base_model:
- dbmdz/bert-base-turkish-cased
pipeline_tag: text-classification
---

# BERTurk Turkish Sentiment Analysis

This is a Turkish sentiment classification model fine-tuned from `dbmdz/bert-base-turkish-cased`.

The model classifies Turkish texts into three sentiment categories:

* `Negative`
* `Notr`
* `Positive`

## Model Details

* **Developed by:** Gamze Nur Aslan
* **Model type:** BERT-based sequence classification model
* **Language:** Turkish
* **Task:** Multiclass sentiment classification
* **Framework:** PyTorch and Hugging Face Transformers
* **Fine-tuned from:** `dbmdz/bert-base-turkish-cased`
* **Number of classes:** 3

### Label Mapping

| Label ID | Label    |
| -------: | -------- |
|        0 | Negative |
|        1 | Notr     |
|        2 | Positive |

## Intended Uses

The model can be used for:

* Turkish product review analysis
* Customer feedback classification
* Social media sentiment analysis
* Educational and research projects
* Sentiment-based text analysis applications

## Out-of-Scope Uses

The model should not be used as the sole decision-making system for:

* Medical decisions
* Legal decisions
* Recruitment decisions
* Financial or credit decisions
* Other high-stakes applications

The model was designed for Turkish texts. Its performance on other languages has not been evaluated.

## How to Use

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="gmzx/berturk-turkish-sentiment"
)

texts = [
    "Bu ürün gerçekten harika, çok memnun kaldım.",
    "Kargo çok geç geldi ve ürün bozuk çıktı.",
    "Toplantı yarın saat üçte yapılacak."
]

results = classifier(texts)

for text, result in zip(texts, results):
    print(text)
    print(result)
```

Example output:

```text
Bu ürün gerçekten harika, çok memnun kaldım.
{'label': 'Positive', 'score': 0.99}

Kargo çok geç geldi ve ürün bozuk çıktı.
{'label': 'Negative', 'score': 0.99}

Toplantı yarın saat üçte yapılacak.
{'label': 'Notr', 'score': 0.99}
```

## Training Data

The model was fine-tuned using the `winvoker/turkish-sentiment-analysis-dataset`.

The original dataset contains Turkish texts collected from several sources:

* Product reviews
* Store reviews
* Wikipedia sentences
* Tweets
* HUMIR
* Random text samples

A balanced subset of 30,000 examples was selected.

| Class    | Number of examples |
| -------- | -----------------: |
| Negative |             10,000 |
| Notr     |             10,000 |
| Positive |             10,000 |

The balanced dataset was split into:

* **Training set:** 24,000 examples
* **Validation set:** 6,000 examples

Each class contained 8,000 training examples and 2,000 validation examples.

## Training Procedure

### Preprocessing

The tokenizer associated with `dbmdz/bert-base-turkish-cased` was used.

The following preprocessing steps were applied:

* Labels were converted to numerical IDs.
* Text truncation was enabled.
* Maximum sequence length was set to 128 tokens.
* Dynamic padding was applied with `DataCollatorWithPadding`.
* The dataset was split using stratified sampling.

### Training Hyperparameters

| Hyperparameter          |             Value |
| ----------------------- | ----------------: |
| Epochs                  |                 1 |
| Learning rate           |              2e-5 |
| Training batch size     |                16 |
| Evaluation batch size   |                16 |
| Weight decay            |              0.01 |
| Maximum sequence length |               128 |
| Evaluation strategy     | End of each epoch |
| Best-model metric       |          Macro F1 |
| Training environment    |  Google Colab GPU |

## Evaluation

The model was evaluated on a balanced validation set containing 6,000 examples.

The following metrics were used:

* Accuracy
* Macro precision
* Macro recall
* Macro F1-score

Macro averaging gives equal importance to the Negative, Notr, and Positive classes.

### Overall Results

| Metric          |  Score |
| --------------- | -----: |
| Validation loss | 0.1753 |
| Accuracy        | 0.9420 |
| Macro precision | 0.9420 |
| Macro recall    | 0.9420 |
| Macro F1-score  | 0.9420 |

### Class-Level Results

| Class    | Precision | Recall | F1-score | Support |
| -------- | --------: | -----: | -------: | ------: |
| Negative |    0.9100 | 0.9200 |   0.9150 |   2,000 |
| Notr     |    0.9950 | 0.9985 |   0.9968 |   2,000 |
| Positive |    0.9209 | 0.9075 |   0.9141 |   2,000 |

### Confusion Matrix

| Actual / Predicted | Negative | Notr | Positive |
| ------------------ | -------: | ---: | -------: |
| Negative           |     1840 |    4 |      156 |
| Notr               |        3 | 1997 |        0 |
| Positive           |      179 |    6 |     1815 |

The model performs especially well on the `Notr` class. Most errors occur between the `Positive` and `Negative` classes.

## Limitations and Bias

The model may have difficulty processing:

* Sarcasm and irony
* Mixed-sentiment sentences
* Slang and spelling mistakes
* Context-dependent expressions
* Very long texts
* Domain-specific terminology

For example, a sentence containing both positive and negative expressions may be classified according to whichever sentiment the model considers dominant.

The training dataset combines texts from different sources. Wikipedia sentences are mostly neutral and stylistically different from product reviews and social media texts. The model may therefore learn source-specific writing patterns in addition to sentiment.

The validation examples were selected from the same collection of sources as the training examples. Performance on completely different real-world datasets may be lower than the reported results.

The model may reproduce offensive expressions, biases, or undesirable associations found in its training data.

## Ethical Considerations

Model predictions should be reviewed by a human when used in sensitive contexts.

The model should not be considered an objective measure of a person's emotions, opinions, intentions, or personality.

## Author

**Gamze Nur Aslan**

Computer Engineering Student

Interested in artificial intelligence, natural language processing, and machine learning.
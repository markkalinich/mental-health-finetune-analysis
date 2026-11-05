---
language:
  - en
library_name: sentence-transformers
pipeline_tag: text-classification
tags:
  - sentence-transformers
  - text-classification
  - sentence-embeddings
  - mental-health
  - binary-classification
  - logistic-regression
base_model: sentence-transformers/all-MiniLM-L6-v2
---

# Fine-Tuned SBERT MiniLM for Mental Health Classification

A fine-tuned **Sentence-BERT (SBERT)** model based on
`sentence-transformers/all-MiniLM-L6-v2`, developed for binary
mental-health text classification.

The model generates **384-dimensional sentence embeddings** using
the fine-tuned SBERT encoder. These embeddings are passed to a trained
**Logistic Regression classifier** to classify text into `Non-MH` or `MH`.

## Model Pipeline

```text
Input Text
    |
    v
Fine-Tuned SBERT
(all-MiniLM-L6-v2)
    |
    v
Mean Pooling
    |
    v
L2 Normalization
    |
    v
384-Dimensional Embedding
    |
    v
Logistic Regression
    |
    v
Non-MH / MH
```

## Model Details

| Property                    | Value                                    |
| ---------------------------- | ---------------------------------------- |
| Base Model                  | `sentence-transformers/all-MiniLM-L6-v2` |
| Architecture                | BERT / MiniLM                            |
| Transformer Layers          | 6                                        |
| Attention Heads             | 12                                       |
| Hidden Size                 | 384                                      |
| Embedding Dimension         | 384                                      |
| Pooling                     | Mean Pooling                             |
| Normalization               | L2 Normalization                         |
| Project Max Sequence Length | 32 tokens                                |
| Downstream Classifier       | Logistic Regression                      |
| Number of Classes           | 2                                        |
| Labels                      | `Non-MH`, `MH`                           |

### Logistic Regression Configuration

```text
C = 1.0
class_weight = balanced
max_iter = 1000
```

## Repository Contents

```text
.
├── 1_Pooling/
│   └── config.json
├── config.json
├── config_sentence_transformers.json
├── logistic_regression_classifier.joblib
├── model.safetensors
├── modules.json
├── sentence_bert_config.json
├── special_tokens_map.json
├── tokenizer.json
├── tokenizer_config.json
└── vocab.txt
```

### Key Files

* `model.safetensors` — fine-tuned SBERT model weights
* `config.json` — Transformer model configuration
* `config_sentence_transformers.json` — Sentence Transformers configuration
* `modules.json` — Sentence Transformers module configuration
* `1_Pooling/config.json` — mean-pooling configuration
* `tokenizer.json` — tokenizer
* `tokenizer_config.json` — tokenizer configuration
* `vocab.txt` — vocabulary
* `logistic_regression_classifier.joblib` — trained Logistic Regression classifier

## Installation

```bash
pip install sentence-transformers scikit-learn joblib
```

## Usage

### 1. Load the Fine-Tuned SBERT Model

```python
from sentence_transformers import SentenceTransformer

encoder = SentenceTransformer(
    "AbdullahImran/Fine-Tuned-SBERT-MiniLM"
)
```

### 2. Generate Sentence Embeddings

```python
texts = [
    "I have been feeling very anxious lately.",
    "The weather is beautiful today."
]

embeddings = encoder.encode(texts)

print(embeddings.shape)
```

The resulting embeddings have **384 dimensions**.

### 3. Load the Classifier

Download `logistic_regression_classifier.joblib` from this repository and load it:

```python
import joblib

classifier = joblib.load(
    "logistic_regression_classifier.joblib"
)
```

### 4. Perform Classification

```python
predictions = classifier.predict(embeddings)

print(predictions)
```

The classifier uses the following label encoding:

```text
0 → Non-MH
1 → MH
```

For example:

```python
for text, prediction in zip(texts, predictions):
    label = "MH" if prediction == 1 else "Non-MH"
    print(f"{text} -> {label}")
```

## Complete Example

```python
from sentence_transformers import SentenceTransformer
import joblib

# Load the fine-tuned encoder
encoder = SentenceTransformer(
    "AbdullahImran/Fine-Tuned-SBERT-MiniLM"
)

# Load the trained classifier
classifier = joblib.load(
    "logistic_regression_classifier.joblib"
)

# Input text
texts = [
    "I have been feeling overwhelmed and anxious recently.",
    "I went to the park and enjoyed the sunny weather."
]

# Generate embeddings
embeddings = encoder.encode(texts)

# Classify
predictions = classifier.predict(embeddings)

# Display results
for text, prediction in zip(texts, predictions):
    label = "MH" if prediction == 1 else "Non-MH"
    print(f"{label}: {text}")
```

## Intended Use

This model is intended for:

* NLP research
* Mental-health text classification research
* Sentence embedding experimentation
* Development and evaluation of binary text classification pipelines

This model is **not a medical or clinical diagnostic system** and
should not be used to diagnose, treat, or make clinical decisions about
individuals.

## Limitations

Mental-health-related language is highly contextual and can be
ambiguous. Model performance depends on the quality, distribution, and
representativeness of the training data.

Performance may vary when the model is applied to text from domains,
populations, writing styles, or distributions that differ from the
training data.

Predictions should therefore be treated as machine-learning outputs
rather than clinical assessments.

The Logistic Regression classifier is serialized using `joblib`.
Loading it may require compatible Python and scikit-learn versions.

## Project Context

This model is part of a broader **Mental Health NLP** project involving:

1. Dataset preparation and cleaning
2. Mental-health and non-mental-health text classification
3. SBERT fine-tuning
4. Sentence embedding generation
5. Logistic Regression classification
6. Deployment-oriented model packaging

The repository contains the final fine-tuned SBERT encoder and the
associated downstream classifier used by the classification pipeline.

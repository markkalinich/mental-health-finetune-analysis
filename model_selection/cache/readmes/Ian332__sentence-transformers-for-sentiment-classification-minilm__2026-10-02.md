---
library_name: transformers
language: en
license: apache-2.0
tags:
- text-classification
- sentiment-analysis
datasets:
- stanfordnlp/imdb
metrics:
- accuracy
- f1
---

# Model Card for sentence-transformers-for-sentiment-classification-minilm

This is homework for CS 546 Adv topics in NLP, and this is a `sentence-transformers/all-MiniLM-L6-v2` model fine-tuned for binary sentiment classification on the IMDB movie reviews dataset. 

## Model Details

### Model Description

This model is a fine-tuned version of the `sentence-transformers/all-MiniLM-L6-v2` model, adapted for sequence classification. It has been trained to classify movie reviews from the IMDB dataset as either **positive** or **negative**.

- **Developed by:** Ian
- **Model type:** BERT-based text classification
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Finetuned from model:** `sentence-transformers/all-MiniLM-L6-v2`

## How to Get Started with the Model

Use the code below to get started with the model using the `transformers` library pipeline.

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="YourHuggingFaceUsername/sentence-transformers-for-sentiment-classification-minilm")

results = classifier([
    "This movie was absolutely fantastic! The acting was superb and the plot was gripping.",
    "I was really disappointed with this film. It was boring and the story made no sense."
])

for result in results:
    print(result)

# Expected output:
# {'label': 'LABEL_1', 'score': ...}  # Corresponds to positive
# {'label': 'LABEL_0', 'score': ...}  # Corresponds to negative
````

## Training Details

### Training Data

The model was fine-tuned on the `stanfordnlp/imdb` dataset. The training was performed on the `train` split, which contains 25,000 movie reviews. A 90/10 split was created from this data for training (22,500 examples) and validation (2,500 examples).

### Training Procedure

The model was trained for 5 epochs using the AdamW optimizer.

#### Training Hyperparameters

  - **Epochs:** 5
  - **Optimizer:** AdamW
  - **Learning rate:** `2e-5`
  - **Training batch size:** 32

## Evaluation

### Testing Data

The model was evaluated on the `test` split of the `stanfordnlp/imdb` dataset, which consists of 25,000 unseen movie reviews.

### Metrics

The primary metric used for evaluation was **Accuracy**, which measures the percentage of reviews correctly classified. Other metrics computed include F1, Precision, and Recall.

### Results

The fine-tuning process resulted in a significant performance improvement over a baseline classifier (Logistic Regression) that used frozen embeddings from the base model.

| Model                               | Test Accuracy |
|-------------------------------------|:-------------:|
| Baseline (Frozen `all-MiniLM-L6-v2`) | 81.10%        |
| **Fine-tuned (This Model)** | **90.17%** |

## Environmental Impact

  - **Hardware Type:** NVIDIA A100 GPU
  - **Hours used:** Approximately 0.1 hours (6-7 minutes)
  - **Cloud Provider:** Google Colab
  - **Carbon Emitted:** Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute).

## Citation

If you use this model, please consider citing the original Sentence-BERT paper:

```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "[http://arxiv.org/abs/1908.10084](http://arxiv.org/abs/1908.10084)",
}
```
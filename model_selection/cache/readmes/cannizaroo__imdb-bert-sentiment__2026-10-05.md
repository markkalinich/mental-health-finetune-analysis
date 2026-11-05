---
language: en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
  - text-classification
  - sentiment-analysis
  - bert
  - imdb
  - transformers
datasets:
  - imdb
---

# BERT IMDb Sentiment Classifier

A fine-tuned **BERT-base-uncased** model for binary sentiment classification of IMDb movie reviews.

The model was fine-tuned using **PyTorch** and the **Hugging Face Transformers `Trainer` API**.

## Model Details

- **Base model:** `bert-base-uncased`
- **Model type:** `BertForSequenceClassification`
- **Task:** Text Classification / Sentiment Analysis
- **Language:** English
- **Dataset:** IMDb Movie Reviews
- **Number of labels:** 2
- **Max sequence length:** 512

### Labels

| ID | Label    |
|----|----------|
| 0  | negative |
| 1  | positive |

```text
0 → negative
1 → positive
```

## Intended Uses

### Direct Use

This model can be used directly for binary sentiment classification of English movie reviews (or similar review-style text):

- `negative` — negative sentiment
- `positive` — positive sentiment

### Out-of-Scope Use

- Non-English text
- Multi-class or fine-grained sentiment / emotion detection
- Long documents significantly exceeding 512 tokens (truncation will occur)
- Domains very different from movie reviews without further evaluation

## How to Use

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_id = "cannizaroo/imdb-bert-sentiment"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForSequenceClassification.from_pretrained(model_id)
model.eval()

text = "This movie was absolutely fantastic. I loved every minute."

inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)

with torch.no_grad():
    outputs = model(**inputs)
    predicted_id = outputs.logits.argmax(dim=-1).item()

print(model.config.id2label[predicted_id])  # "positive" or "negative"
```

Using the `pipeline` API:

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="cannizaroo/imdb-bert-sentiment")
classifier("This movie was absolutely fantastic. I loved every minute.")
# [{'label': 'positive', 'score': ...}]
```

## Training Data

**IMDb Movie Reviews** ([imdb](https://huggingface.co/datasets/imdb)):

- 25,000 training reviews
- 25,000 test reviews
- Binary labels: `0 → Negative`, `1 → Positive`
- Text tokenized with the BERT tokenizer (`input_ids` + `attention_mask`), with padding and truncation

## Training Procedure

Fine-tuned with:

- PyTorch
- Hugging Face Transformers `Trainer`
- Hugging Face Datasets
- Hugging Face Evaluate
- Google Colab GPU

### Training Hyperparameters

```text
Learning Rate: 2e-5
Batch Size: 16
Epochs: 2
Weight Decay: 0.01
Maximum Sequence Length: 512
```

## Evaluation

Evaluated on the final held-out IMDb test set:

```text
Model: BERT-base-uncased + Fine-tuning

Accuracy:  93.21%
Precision: 95.53%
Recall:    90.66%
F1 Score:  93.03%
```

### Test Set Confusion Matrix

```text
                  Predicted
                Negative  Positive

Actual Negative   11970      530
Actual Positive    1167    11333
```

Metrics computed with Hugging Face Evaluate and scikit-learn.

## Limitations and Bias

- Trained only on IMDb movie reviews; performance may degrade on other domains (e.g., tweets, product reviews, formal text).
- English only.
- May reflect biases present in IMDb data and in the original `bert-base-uncased` pretraining corpus.
- Truncates inputs longer than 512 tokens, so sentiment expressed late in very long reviews may be lost.

## Citation

If you use this model, please cite the base model and dataset:

```bibtex
@article{devlin2018bert,
  title={BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding},
  author={Devlin, Jacob and Chang, Ming-Wei and Lee, Kenton and Toutanova, Kristina},
  journal={arXiv preprint arXiv:1810.04805},
  year={2018}
}
```

```bibtex
@inproceedings{maas2011learning,
  title={Learning Word Vectors for Sentiment Analysis},
  author={Maas, Andrew L. and Daly, Raymond E. and Pham, Peter T. and Huang, Dan and Ng, Andrew Y. and Potts, Christopher},
  booktitle={Proceedings of the 49th Annual Meeting of the Association for Computational Linguistics},
  year={2011}
}
```

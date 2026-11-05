---
license: mit
language:
- en
library_name: transformers
pipeline_tag: text-classification
tags:
- sentiment-analysis
- text-classification
- bert
- imdb
- fine-tuned
datasets:
- imdb
base_model: bert-base-uncased
metrics:
- accuracy
model-index:
- name: bert-imdb-finetuned
  results:
  - task:
      type: text-classification
      name: Sentiment Classification
    dataset:
      type: imdb
      name: IMDB
    metrics:
    - type: accuracy
      value: 0.9145
      name: Validation Accuracy
---
# BERT — IMDB Sentiment Classifier

A fine-tuned [`bert-base-uncased`](https://huggingface.co/bert-base-uncased) model that classifies English text as **Positive** or **Negative** sentiment. Trained on the [IMDB movie reviews dataset](https://huggingface.co/datasets/imdb).

🎛️ **Live demo:** [huggingface.co/spaces/harshaojha/bert-imdb-demo](https://huggingface.co/spaces/harshaojha/bert-imdb-demo)

## Model details
- **Base model:** `bert-base-uncased` (110M parameters)
- **Task:** Binary text classification (sentiment)
- **Labels:** `0 = Negative`, `1 = Positive`
- **Language:** English
- **Max input length:** 256 tokens

## Intended use
Educational / demonstration — learning how to fine-tune a transformer and wrap it in a web UI. Works well on movie-review-style text; less reliable on other domains.

## Training data
A balanced subset of the IMDB reviews dataset:
- Train: 10,000 reviews (shuffled, seed=42)
- Validation: 2,000 reviews (shuffled, seed=42)

## Training procedure
| Hyperparameter | Value |
|---|---|
| Optimizer | AdamW |
| Learning rate | 2e-5 |
| Batch size (train / eval) | 16 / 32 |
| Epochs | 3 |
| Weight decay | 0.01 |
| Warmup ratio | 0.1 |
| Max sequence length | 256 |
| Best-checkpoint metric | accuracy |
| Hardware | NVIDIA T4 GPU (Google Colab) |

## Evaluation results
| Epoch | Validation Accuracy |
|---|---|
| 1 | 89.80% |
| **2** | **91.45%** ← best |
| 3 | 91.10% |

## How to use
    from transformers import pipeline

    clf = pipeline("text-classification", model="harshaojha/bert-imdb-finetuned")
    ID2LABEL = {"LABEL_0": "Negative", "LABEL_1": "Positive"}
    result = clf("An absolute masterpiece.")[0]
    print(ID2LABEL[result["label"]], round(result["score"], 3))
    # Positive 0.993

Or load the tokenizer and model directly:

    from transformers import AutoTokenizer, AutoModelForSequenceClassification
    import torch

    tokenizer = AutoTokenizer.from_pretrained("harshaojha/bert-imdb-finetuned")
    model = AutoModelForSequenceClassification.from_pretrained("harshaojha/bert-imdb-finetuned")
    inputs = tokenizer("Painfully boring.", return_tensors="pt", truncation=True, max_length=256)
    with torch.no_grad():
        logits = model(**inputs).logits
    probs = torch.softmax(logits, dim=-1)[0]
    print({"Negative": probs[0].item(), "Positive": probs[1].item()})

## Limitations
- Trained on movie reviews only — accuracy drops on other domains (tweets, product reviews, news).
- Inherits biases present in IMDB and in the base `bert-base-uncased` model.
- Truncates inputs longer than 256 tokens.
- Trained on 10,000 of the 25,000 available training samples; using the full set would likely push accuracy higher.

## Author
Trained by [@harshaojha](https://huggingface.co/harshaojha) as part of a learning project on transformer fine-tuning.
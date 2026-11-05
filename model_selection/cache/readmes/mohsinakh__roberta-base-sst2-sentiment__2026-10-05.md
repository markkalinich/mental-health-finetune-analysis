---
language: en
tags:
  - roberta
  - sentiment-analysis
  - text-classification
  - sst2
  - glue
license: apache-2.0
pipeline_tag: text-classification
model-index:
- name: roberta-base-sst2-sentiment (checkpoint-3750)
  results:
  - task:
      type: text-classification
      name: Sentiment Analysis
    dataset:
      type: glue
      name: GLUE SST-2
    metrics:
      - type: accuracy
        name: Accuracy (SST-2 validation)
        value: 0.8383
base_model: roberta-base
---

# roberta-base fine-tuned on SST-2 (checkpoint-3750)

This is the best checkpoint from a full fine-tuning run of `roberta-base` on the GLUE SST-2 sentiment task. It is the final step of training after 3 epochs (3,750 optimizer steps) and reached the lowest training loss of the run, dropping from about 0.69 to 0.36. Evaluating it on the held-out validation split gives 83.83% accuracy.

The checkpoint is published as-is so it can be loaded in two lines of code.

## Model description

- Architecture: `RobertaForSequenceClassification` (RoBERTa-base, 12 layers, hidden size 768, about 125M parameters)
- Base model: [`roberta-base`](https://huggingface.co/roberta-base)
- Training data: first 6,000 examples of the SST-2 training split
- Task: binary sentiment classification, where 0 is negative and 1 is positive
- Libraries: `transformers`, `datasets`, `evaluate`

## Training details

| Setting | Value |
|---------|-------|
| Optimizer steps | 3,750 (final checkpoint) |
| Epochs | 3 |
| Batch size | 8 |
| Optimizer | AdamW (default Transformer Trainer schedule) |
| Learning rate | 5e-5 |
| Weight decay | 0.01 |
| Validation accuracy (SST-2 dev) | 83.83% |
| Validation metric | Accuracy (GLUE SST-2) |

The training loss by checkpoint:

| Step | Training loss |
|------|---------------|
| 500 | 0.6855 |
| 1,000 | 0.6077 |
| 1,500 | 0.5445 |
| 2,000 | 0.5054 |
| 2,500 | 0.4521 |
| 3,000 | 0.3854 |
| 3,500 to 3,750 | 0.3636 to 0.364 |

## How to use

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

repo_id = "mohsinakh/roberta-base-sst2-sentiment"

tokenizer = AutoTokenizer.from_pretrained(repo_id)
model = AutoModelForSequenceClassification.from_pretrained(repo_id)

inputs = tokenizer("this movie was absolutely amazing", return_tensors="pt")
logits = model(**inputs).logits
pred = logits.argmax(dim=-1).item()
print("positive" if pred == 1 else "negative")  # -> positive
```

If you prefer working with the higher-level pipeline API:

```python
from transformers import pipeline

pipe = pipeline("text-classification", model="mohsinakh/roberta-base-sst2-sentiment")
print(pipe("this was the worst film i have ever seen"))
```

## About the validation number

The 83.83% figure comes from running this checkpoint against the 872-example validation split. The official SST-2 test split ships with its labels hidden, so it is only useful for sample predictions rather than computing a final score.

## Reproducibility

The full training and evaluation flow lives in the [GitHub repository](https://github.com/mohsinakh/roberta-base-sst2-sentiment). The `notebooks/finetune_roberta_sst2_sentiment.ipynb` notebook walks through everything, and the Trainer saves a checkpoint every 500 steps, with `checkpoint-3750` being the final model published here.

## Usage notes

This model was fine-tuned as a demonstration of sentiment analysis and reflects the distribution of its training data. If you plan to use it in production, it is worth evaluating it on your own domain data, since accuracy can drop on other types of reviews, other languages, or more subjective content.

## References

- [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/abs/1907.11692)
- [GLUE benchmark and SST-2](https://gluebenchmark.com/)
- [`roberta-base`](https://huggingface.co/roberta-base)

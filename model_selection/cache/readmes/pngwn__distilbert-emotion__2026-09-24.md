---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
datasets:
- dair-ai/emotion
tags:
- text-classification
- emotion-classification
- distilbert
metrics:
- accuracy
- f1
model-index:
- name: distilbert-emotion
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      type: dair-ai/emotion
      name: dair-ai/emotion
      split: test
    metrics:
    - type: accuracy
      value: 0.9265
      name: Accuracy
    - type: f1
      value: 0.8868
      name: Macro F1
---

# distilbert-emotion

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on the [dair-ai/emotion](https://huggingface.co/datasets/dair-ai/emotion) dataset for 6-class emotion classification.

## Evaluation Results (Test Split)

The following results were obtained by evaluating on the **test split** of `dair-ai/emotion`:

| Metric      | Value |
|-------------|-------|
| **Accuracy**| 0.9265|
| **Macro F1**| 0.8868|

## Base Model

- **Model:** distilbert-base-uncased
- **Architecture:** DistilBERT
- **Task:** Sequence Classification (6 classes)

## Dataset

- **Dataset:** dair-ai/emotion
- **Config:** split
- **Classes:** sadness (0), joy (1), love (2), anger (3), fear (4), surprise (5)

## Training Hyperparameters

| Parameter               | Value |
|-------------------------|-------|
| Learning rate           | 2e-5  |
| Train batch size        | 32    |
| Eval batch size         | 64    |
| Epochs                  | 3     |
| Weight decay            | 0.01  |
| Optimizer               | AdamW |
| LR scheduler            | linear|
| Seed                    | 42    |

## Evaluation Command

```python
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, DataCollatorWithPadding
from sklearn.metrics import accuracy_score, f1_score
import numpy as np

dataset = load_dataset("dair-ai/emotion", "split")
tokenizer = AutoTokenizer.from_pretrained("pngwn/distilbert-emotion")
model = AutoModelForSequenceClassification.from_pretrained("pngwn/distilbert-emotion")

def preprocess(examples):
    return tokenizer(examples["text"], truncation=True)

tokenized = dataset.map(preprocess, batched=True)

def compute_metrics(eval_pred):
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    return {
        "accuracy": accuracy_score(labels, preds),
        "macro_f1": f1_score(labels, preds, average="macro"),
    }

trainer = Trainer(
    model=model,
    eval_dataset=tokenized["test"],
    tokenizer=tokenizer,
    data_collator=DataCollatorWithPadding(tokenizer),
    compute_metrics=compute_metrics,
)
results = trainer.evaluate()
print(f"Test accuracy: {results['eval_accuracy']:.4f}")
print(f"Test macro_f1: {results['eval_macro_f1']:.4f}")
```

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="pngwn/distilbert-emotion", top_k=None)
classifier("I am so happy today!")
```

## License

Apache-2.0

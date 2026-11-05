---
license: apache-2.0
language:
  - en
library_name: transformers
pipeline_tag: text-classification
tags:
  - text-classification
  - sentiment-analysis
  - distilbert
  - transformers
  - novapay
datasets:
  - stanfordnlp/imdb
metrics:
  - accuracy
  - f1
base_model: distilbert/distilbert-base-uncased
---

# NovaPay Sentiment IMDB DistilBERT

A fine-tuned DistilBERT model for binary sentiment classification.

This model was created as an educational proof of concept for exploring sentiment classification in the NovaPay project. This checkpoint was trained only on IMDB movie reviews.

## Intended Use

This model is intended for:

- Educational experimentation with Transformer fine-tuning
- Binary positive/negative sentiment classification
- Testing Hugging Face training, inference, and deployment workflows
- Prototyping sentiment-analysis components for the NovaPay project

This model is not intended for production financial decision-making or real-world customer-support automation without additional domain-specific training and evaluation.

## Base Model

- **Base model:** `distilbert/distilbert-base-uncased`
- **Architecture:** `DistilBertForSequenceClassification`
- **Library:** Hugging Face Transformers
- **Language:** English
- **Task:** Binary text classification

## Labels

| ID | Label |
|---:|---|
| 0 | NEGATIVE |
| 1 | POSITIVE |

## Training Data

The model was fine-tuned using the Stanford IMDB movie-review dataset:

`stanfordnlp/imdb`

For this proof-of-concept training run:

- **Training examples:** 5,000
- **Evaluation examples:** 1,000
- **Training source:** IMDB training split
- **Evaluation source:** IMDB test split
- **Sampling:** Shuffled before subset selection
- **Shuffle seed:** 42
- **Maximum sequence length:** 256 tokens
- **Dynamic padding:** Yes

The original IMDB training split contains 25,000 labeled movie reviews with a balanced label distribution:

- 12,500 negative
- 12,500 positive

## Training Configuration

- **Epochs:** 2
- **Learning rate:** `2e-5`
- **Training batch size:** 16
- **Evaluation batch size:** 16
- **Weight decay:** 0.01
- **Evaluation frequency:** Once per epoch
- **Checkpoint frequency:** Once per epoch
- **Best-model metric:** F1
- **Maximum sequence length:** 256 tokens
- **Dynamic padding:** `DataCollatorWithPadding`
- **Training interface:** Hugging Face `Trainer`
- **Final training loss:** 0.2983

All parameters of the DistilBERT model were trainable during fine-tuning.

## Training Hardware and Performance

This training run was performed locally using:

- **GPU:** NVIDIA GeForce RTX 3070
- **Training examples:** 5,000
- **Epochs:** 2
- **Training batch size:** 16
- **Maximum sequence length:** 256 tokens
- **Total optimizer/training steps:** 626

### RTX 3070 Training Benchmark

| Measurement | Result |
|---|---:|
| Total training runtime | 91.02 seconds |
| Total training steps | 626 |
| Training samples/sec | 109.9 |
| Training steps/sec | 6.878 |
| Final training loss | 0.2983 |

The complete two-epoch fine-tuning run took approximately **1 minute 31 seconds** on the RTX 3070 for the 5,000-example training subset.

### RTX 3070 Evaluation Benchmark

Final evaluation on 1,000 examples produced:

| Measurement | Result |
|---|---:|
| Evaluation runtime | 2.70 seconds |
| Evaluation samples/sec | 370.4 |
| Evaluation steps/sec | 23.33 |
| Evaluation batch size | 16 |
| Evaluation examples | 1,000 |

These measurements describe this specific training run and should not be treated as universal RTX 3070 performance. Runtime can vary with software versions, CPU performance, storage, CUDA/PyTorch configuration, sequence-length distribution, and background workloads.

## Evaluation Results

The model was evaluated on a shuffled 1,000-example subset of the IMDB test split.

| Metric | Result |
|---|---:|
| Accuracy | 0.8830 |
| F1 | 0.8836 |
| Evaluation Loss | 0.2993 |

### Epoch Results

| Epoch | Accuracy | F1 | Eval Loss |
|---:|---:|---:|---:|
| 1 | 0.8370 | 0.8535 | 0.3752 |
| 2 | 0.8830 | 0.8836 | 0.2993 |

The second epoch improved accuracy, F1, and evaluation loss on the selected evaluation subset.

These results measure performance on IMDB movie-review sentiment classification only. They should not be interpreted as performance on financial or customer-support data.

## Example Usage

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="dumbbutt0/novapay-sentiment-imdb-distilbert"
)

result = classifier(
    "I absolutely loved this movie."
)

print(result)
```

Example output format:

```python
[
    {
        "label": "POSITIVE",
        "score": 0.98
    }
]
```

The confidence value shown above is only an example and will vary by input.

## Manual Inference

```python
import torch

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

MODEL = "dumbbutt0/novapay-sentiment-imdb-distilbert"

tokenizer = AutoTokenizer.from_pretrained(MODEL)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL
)

model.eval()

text = "This movie was fantastic."

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    max_length=256
)

with torch.no_grad():
    outputs = model(**inputs)

prediction = outputs.logits.argmax(dim=-1).item()

print(model.config.id2label[prediction])
```

## Limitations

- The model was trained on movie reviews, not NovaPay or financial customer-support messages.
- IMDB language and sentiment patterns may differ substantially from financial-service conversations.
- Only 5,000 of the available 25,000 IMDB training examples were used.
- Evaluation was performed on a 1,000-example subset rather than the complete IMDB test set.
- Input sequences were truncated to a maximum of 256 tokens.
- The model performs binary sentiment classification only.
- Neutral, mixed, uncertain, sarcastic, or context-dependent sentiment is not represented by a separate class.
- Sentiment confidence should not be interpreted as calibrated certainty.
- Performance on demographic subgroups, dialects, financial terminology, adversarial inputs, and out-of-domain data was not evaluated.
- Performance on actual NovaPay-style customer-support messages has not been measured.
- The model should not be used to make financial, credit, fraud, eligibility, or other consequential decisions.

## License

Apache License 2.0.

Downstream users should also review the terms and licenses associated with the base model, training dataset, and other dependencies used to create this checkpoint.

## Reproducibility

Key training settings:

```text
Base model: distilbert/distilbert-base-uncased
Dataset: stanfordnlp/imdb
Training samples: 5000
Evaluation samples: 1000
Epochs: 2
Learning rate: 2e-5
Training batch size: 16
Evaluation batch size: 16
Weight decay: 0.01
Maximum sequence length: 256
Shuffle seed: 42
Best-model metric: F1

Hardware: NVIDIA GeForce RTX 3070
Training runtime: 91.02 seconds
Training steps: 626
Training samples/sec: 109.9
Training steps/sec: 6.878
Evaluation runtime: 2.70 seconds
Evaluation samples/sec: 370.4
```

## Proof-of-Concept Status

This checkpoint was created to demonstrate a complete Transformer fine-tuning workflow:

raw dataset → tokenization → truncation → dynamic batching → pretrained DistilBERT → supervised fine-tuning → evaluation → saved checkpoint → Hugging Face deployment

It should be treated as an educational proof of concept rather than a production-ready classification model.
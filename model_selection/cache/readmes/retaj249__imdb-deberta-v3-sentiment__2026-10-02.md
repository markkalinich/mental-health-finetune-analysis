---
language:
  - en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
  - sentiment-analysis
  - imdb
  - deberta-v3
  - binary-classification
datasets:
  - stanfordnlp/imdb
base_model: microsoft/deberta-v3-base
model-index:
  - name: IMDB DeBERTa-v3 Sentiment
    results:
      - task:
          type: text-classification
          name: Binary Sentiment Classification
        dataset:
          type: stanfordnlp/imdb
          name: IMDB
          split: test
        metrics:
          - type: accuracy
            value: 0.960880
            name: Accuracy
          - type: f1
            value: 0.961316
            name: F1
          - type: roc_auc
            value: 0.992435
            name: ROC AUC
---

# IMDB DeBERTa-v3 Sentiment

This is the production export of a binary IMDB movie-review sentiment classifier
fine-tuned from [`microsoft/deberta-v3-base`](https://huggingface.co/microsoft/deberta-v3-base).
It is the winning model from a five-model screening workflow and the final selected
run uses seed 42.

The accompanying production API and reproducibility workflow are available in the
[`RetajMelhem/imdb-sentiment-api`](https://github.com/RetajMelhem/imdb-sentiment-api)
repository.

## Labels and decision rule

| Class ID | Label |
|---:|---|
| 0 | negative |
| 1 | positive |

The model emits two logits. Production inference applies float32 softmax and predicts
`positive` when the class-1 probability is at least **0.477**; otherwise it predicts
`negative`. This optimized threshold differs from the default 0.5/argmax behavior used
by many generic text-classification examples.

## Validated inference contract

- Base model: `microsoft/deberta-v3-base`
- Final seed: `42`
- Tokenizer: exported DeBERTa-v3 SentencePiece tokenizer with `use_fast=False`
- Preprocessing: minimal normalization matching the training notebook
- Maximum sequence length: `384`
- Truncation: custom head–tail preservation for over-length reviews
- Padding: dynamic, with `pad_to_multiple_of=8`
- Production inference batch size: `8`
- Probability calculation: float32 softmax over the two logits

For exact parity, use the `SentimentPredictor` implementation in the linked source
repository. A generic Transformers pipeline can load the weights, but it does not by
itself reproduce the custom preprocessing, head–tail truncation, or 0.477 decision
threshold for long or borderline reviews.

## Test-set results

Evaluation used the 25,000-example IMDB test split.

| Metric | Value |
|---|---:|
| Accuracy | 0.960880 |
| Precision | 0.950712 |
| Recall | 0.972160 |
| F1 | 0.961316 |
| Macro F1 | 0.960875 |
| ROC AUC | 0.992435 |
| Log loss | 0.130604 |

Confusion matrix, with rows as true labels and columns as predicted labels:

```text
[[11870,  630],
 [  348, 12152]]
```

## Loading the artifacts

Pin deployments to an immutable Hub commit SHA rather than mutable `main`:

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer

model_id = "retaj249/imdb-deberta-v3-sentiment"
revision = "<40-character-commit-sha>"

tokenizer = AutoTokenizer.from_pretrained(
    model_id,
    revision=revision,
    use_fast=False,
    trust_remote_code=False,
)
model = AutoModelForSequenceClassification.from_pretrained(
    model_id,
    revision=revision,
    use_safetensors=True,
    trust_remote_code=False,
)
```

The source repository provides the complete API configuration and prediction command
that preserve the validated inference contract.

## Intended use

The model is intended for English binary sentiment classification of movie-review-like
text, including API, batch, and portfolio demonstration workloads. It is not designed
for factuality, safety moderation, emotion classification, multilingual analysis, or
high-stakes decisions.

## Limitations

- Training and evaluation use IMDB movie reviews; performance may degrade on other
  domains, languages, slang, sarcasm, or distribution shifts.
- The output is a learned statistical estimate, not a calibrated statement of truth.
- Reviews longer than the validated token budget require the documented head–tail
  strategy for parity.
- Dataset biases and annotation limitations can be reflected in predictions.

## Training and reproducibility

The authoritative training notebook is tracked in the linked GitHub repository.
It records the five-model screening, final DeBERTa-v3-base selection, seed-42 run,
threshold optimization, export, and validation evidence. The Hub repository contains
only inference-required artifacts and metadata; it excludes validation predictions,
training checkpoints, credentials, caches, and local paths.

## License

The fine-tuned model is published under the MIT license, consistent with the upstream
`microsoft/deberta-v3-base` model. Users remain responsible for complying with the
IMDB dataset terms and applicable requirements for their use case.

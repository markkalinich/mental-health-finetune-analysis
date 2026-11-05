---
license: apache-2.0
language: en
library_name: transformers
pipeline_tag: text-classification
tags:
  - emotion
  - text-classification
  - roberta
datasets:
  - dair-ai/emotion
  - google-research-datasets/go_emotions
metrics:
  - f1
  - accuracy
base_model: roberta-base
model-index:
  - name: kotodama-distilbert-emotion
    results:
      - task:
          type: text-classification
          name: Emotion Classification
        dataset:
          name: dair-ai/emotion
          type: dair-ai/emotion
          config: split
          split: test
        metrics:
          - type: f1
            value: 0.8907
            name: Macro F1
          - type: accuracy
            value: 0.9290
            name: Accuracy
---

# Kotodama — RoBERTa emotion classifier

`roberta-base` fine-tuned on dair-ai/emotion + GoEmotions (mapped to six classes) with **class-weighted cross-entropy**, for the
[Kotodama](https://github.com/A-K-M-Asifuzzaman/Emotion-Detection-Text-) project.

## Why macro-F1 rather than accuracy

The dataset is heavily imbalanced — *joy* is 9.4x the size of *surprise*. A model that
predicted only *joy* would score 33.5% accuracy while being useless. The headline metric
is therefore **macro-F1**, which weights the rarest class exactly as heavily as the most
common one, and training used class weights inversely proportional to class frequency.

## Results (held-out test split)

| Model | Macro-F1 | Accuracy | Weighted-F1 |
|---|---:|---:|---:|
| TF-IDF + Logistic Regression (baseline) | 0.8328 | 0.8815 | 0.8842 |
| **This model** | **0.8907** | **0.9290** | **0.9298** |
| *gain* | *+0.0579* | | |

The gain is concentrated in the **minority** classes — exactly the ones a raw-accuracy
comparison would let a model ignore.

| Emotion | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| surprise | 0.863 | 0.667 | **0.752** | 66 |
| love | 0.754 | 0.981 | **0.852** | 159 |
| fear | 0.836 | 0.978 | **0.901** | 224 |
| anger | 0.947 | 0.913 | **0.930** | 275 |
| joy | 0.986 | 0.909 | **0.946** | 695 |
| sadness | 0.969 | 0.957 | **0.963** | 581 |

## Labels

Index order matters — it is the order of the model's logits.

| 0 | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|
| sadness | joy | love | anger | fear | surprise |

## Usage

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="AsifZaman1912/kotodama-emotion", top_k=None)
classifier("i cannot believe this actually happened")
```

## Training

| Setting | Value |
|---|---|
| Base model | `roberta-base` |
| Epochs | 3 |
| Best epoch | 3 (selected on validation macro-F1) |
| Batch size | 32 |
| Learning rate | 2e-05 |
| Max length | 128 |
| Class-weighted loss | True |

Checkpoint selection was on validation macro-F1, never validation loss: with a weighted
objective the two can disagree, and loss favours models that have conceded the minority
classes. The test split was used exactly once, for the numbers above.

## ONNX

`onnx/model.onnx` is an fp32 export. `onnx/model.int8.onnx` is dynamically quantized —
4x smaller and faster, but it measures **-0.0078
macro-F1** against fp32, so fp32 remains the serving default.

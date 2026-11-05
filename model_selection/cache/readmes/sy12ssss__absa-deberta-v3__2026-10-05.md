---
license: mit
language: en
library_name: transformers
pipeline_tag: text-classification
base_model: microsoft/deberta-v3-base
tags:
  - sentiment-analysis
  - aspect-based-sentiment-analysis
datasets:
  - tomaarsen/setfit-absa-semeval-restaurants
  - tomaarsen/setfit-absa-semeval-laptops
---

# absa-deberta-v3

DeBERTa-v3-base fine-tuned for aspect-based sentiment analysis. Input is an (aspect, sentence) pair, output is negative, neutral or positive for that aspect.

Int8 quantization of this model was not usable (accuracy collapsed), so the browser demo uses absa-roberta-base.

## Results (588-pair test set, split by sentence)

| Runtime | Size | Accuracy |
|---|---|---|
| PyTorch fp32 | ~500 MB | 0.8214 |

Temperature scaling: T = 1.604, ECE reduced from 0.0993 to 0.0505.

## Usage

Pass the aspect as the first text and the sentence as the second (`tokenizer(aspect, sentence)`). Divide logits by the temperature before the softmax for calibrated confidence.

## Limitations

Trained on restaurant and laptop reviews only (SemEval-2014 Task 4). The aspect must be provided.
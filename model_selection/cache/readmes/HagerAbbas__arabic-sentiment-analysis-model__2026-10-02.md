---
language: ar
license: mit
base_model: UBC-NLP/MARBERT
tags:
- sentiment-analysis
- arabic
- bert
pipeline_tag: text-classification
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# arabic-sentiment-analysis-model

This model is a fine-tuned version of [UBC-NLP/MARBERT](https://huggingface.co/UBC-NLP/MARBERT) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0339

## Model description

This model is fine-tuned for Arabic Sentiment Analysis. It can classify Arabic text into different emotional categories (Positive/Negative).

- **Developed by:** Hager Abbas
- **Language:** Arabic
- **Model Type:** Text Classification
- **Fine-tuned from:** [اسم الموديل الأصلي اللي استخدمناه، غالباً bert-base-arabic]

## Intended uses & limitations

This model is intended for analyzing social media posts, customer reviews, and general Arabic text to determine sentiment.
## How to use
```python
from transformers import pipeline
classifier = pipeline("sentiment-analysis", model="HagerAbbas/اسم-الموديل-بتاعك")
classifier("أنا سعيد جداً بهذا الإنجاز")

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 0.168         | 1.0   | 113  | 0.2174          |
| 0.1619        | 2.0   | 226  | 0.0477          |
| 0.014         | 3.0   | 339  | 0.0339          |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.0+cu126
- Datasets 4.4.2
- Tokenizers 0.22.1

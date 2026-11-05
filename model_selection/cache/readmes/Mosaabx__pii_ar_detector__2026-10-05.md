---
library_name: transformers
license: apache-2.0
base_model: CAMeL-Lab/bert-base-arabic-camelbert-mix-ner
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii_ar_detector
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii_ar_detector

This model is a fine-tuned version of [CAMeL-Lab/bert-base-arabic-camelbert-mix-ner](https://huggingface.co/CAMeL-Lab/bert-base-arabic-camelbert-mix-ner) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0931
- Precision: 0.9476
- Recall: 0.9620
- F1: 0.9547
- Accuracy: 0.9870

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step   | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:------:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0886        | 1.0   | 12425  | 0.0917          | 0.8918    | 0.9041 | 0.8979 | 0.9652   |
| 0.0624        | 2.0   | 24850  | 0.0775          | 0.9037    | 0.9343 | 0.9187 | 0.9747   |
| 0.0422        | 3.0   | 37275  | 0.0634          | 0.9205    | 0.9461 | 0.9331 | 0.9823   |
| 0.0274        | 4.0   | 49700  | 0.0682          | 0.9316    | 0.9521 | 0.9418 | 0.9840   |
| 0.0195        | 5.0   | 62125  | 0.0702          | 0.9365    | 0.9567 | 0.9465 | 0.9853   |
| 0.0135        | 6.0   | 74550  | 0.0737          | 0.9394    | 0.9583 | 0.9487 | 0.9857   |
| 0.0084        | 7.0   | 86975  | 0.0801          | 0.9444    | 0.9595 | 0.9519 | 0.9864   |
| 0.0069        | 8.0   | 99400  | 0.0857          | 0.9449    | 0.9624 | 0.9536 | 0.9870   |
| 0.0043        | 9.0   | 111825 | 0.0887          | 0.9488    | 0.9608 | 0.9548 | 0.9869   |
| 0.003         | 10.0  | 124250 | 0.0931          | 0.9476    | 0.9620 | 0.9547 | 0.9870   |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.6.0+cu124
- Datasets 3.6.0
- Tokenizers 0.21.1

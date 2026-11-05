---
tags:
- generated_from_trainer
metrics:
- precision
- recall
- accuracy
model-index:
- name: depressionDetectionArabert
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# depressionDetectionArabert

This model is a fine-tuned version of [aubmindlab/bert-base-arabertv02-twitter](https://huggingface.co/aubmindlab/bert-base-arabertv02-twitter) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4586
- Macro F1: 0.9279
- Precision: 0.9281
- Recall: 0.9279
- Kappa: 0.8558
- Accuracy: 0.9279

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
- eval_batch_size: 128
- seed: 25
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Macro F1 | Precision | Recall | Kappa  | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 407  | 0.2285          | 0.9143   | 0.9181    | 0.9144 | 0.8289 | 0.9144   |
| 0.2459        | 2.0   | 815  | 0.2124          | 0.9264   | 0.9269    | 0.9264 | 0.8528 | 0.9264   |
| 0.1306        | 3.0   | 1222 | 0.2439          | 0.9285   | 0.9287    | 0.9285 | 0.8570 | 0.9285   |
| 0.0747        | 4.0   | 1630 | 0.3240          | 0.9270   | 0.9272    | 0.9270 | 0.8540 | 0.9270   |
| 0.0328        | 5.0   | 2037 | 0.3850          | 0.9273   | 0.9275    | 0.9273 | 0.8546 | 0.9273   |
| 0.0328        | 6.0   | 2445 | 0.4129          | 0.9279   | 0.9280    | 0.9279 | 0.8558 | 0.9279   |
| 0.0213        | 7.0   | 2852 | 0.4541          | 0.9273   | 0.9273    | 0.9273 | 0.8545 | 0.9273   |
| 0.0108        | 7.99  | 3256 | 0.4586          | 0.9279   | 0.9281    | 0.9279 | 0.8558 | 0.9279   |


### Framework versions

- Transformers 4.28.1
- Pytorch 2.0.0+cu118
- Tokenizers 0.13.3

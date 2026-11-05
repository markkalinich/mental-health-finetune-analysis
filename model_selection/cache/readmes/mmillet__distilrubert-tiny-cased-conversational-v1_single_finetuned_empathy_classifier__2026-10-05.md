---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: distilrubert-tiny-cased-conversational-v1_single_finetuned_empathy_classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilrubert-tiny-cased-conversational-v1_single_finetuned_empathy_classifier

This model is a fine-tuned version of [DeepPavlov/distilrubert-tiny-cased-conversational-v1](https://huggingface.co/DeepPavlov/distilrubert-tiny-cased-conversational-v1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0183
- Accuracy: 0.6218
- F1: 0.6262
- Precision: 0.6318
- Recall: 0.6218

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-06
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 1.0456        | 1.0   | 9    | 0.9718          | 0.4958   | 0.4197 | 0.6526    | 0.4958 |
| 0.9042        | 2.0   | 18   | 0.8920          | 0.5882   | 0.5769 | 0.5784    | 0.5882 |
| 0.7923        | 3.0   | 27   | 0.8427          | 0.6134   | 0.5861 | 0.5935    | 0.6134 |
| 0.7544        | 4.0   | 36   | 0.8400          | 0.6387   | 0.6234 | 0.6344    | 0.6387 |
| 0.6675        | 5.0   | 45   | 0.8410          | 0.6303   | 0.6095 | 0.6184    | 0.6303 |
| 0.6091        | 6.0   | 54   | 0.9095          | 0.6050   | 0.6041 | 0.6396    | 0.6050 |
| 0.6279        | 7.0   | 63   | 0.8596          | 0.6723   | 0.6692 | 0.6725    | 0.6723 |
| 0.4968        | 8.0   | 72   | 0.8725          | 0.6303   | 0.6274 | 0.6253    | 0.6303 |
| 0.4459        | 9.0   | 81   | 0.9120          | 0.6387   | 0.6395 | 0.6426    | 0.6387 |
| 0.4122        | 10.0  | 90   | 0.9478          | 0.6303   | 0.6262 | 0.6248    | 0.6303 |
| 0.3244        | 11.0  | 99   | 0.9746          | 0.6387   | 0.6375 | 0.6381    | 0.6387 |
| 0.3535        | 12.0  | 108  | 1.0183          | 0.6218   | 0.6262 | 0.6318    | 0.6218 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

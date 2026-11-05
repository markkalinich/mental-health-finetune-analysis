---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: distilrubert-tiny-cased-conversational-v1_empathy_preprocessed_punct_lowercasing
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilrubert-tiny-cased-conversational-v1_empathy_preprocessed_punct_lowercasing

This model is a fine-tuned version of [DeepPavlov/distilrubert-tiny-cased-conversational-v1](https://huggingface.co/DeepPavlov/distilrubert-tiny-cased-conversational-v1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6036
- Accuracy: 0.7458
- F1: 0.7409
- Precision: 0.7420
- Recall: 0.7458

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
- optimizer: Adam with betas=(0.9,0.999) and epsilon=0.0001
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1     | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:------:|:---------:|:------:|
| 1.0953        | 1.0   | 9    | 1.0692          | 0.4661   | 0.3740 | 0.3740    | 0.4661 |
| 1.066         | 2.0   | 18   | 1.0242          | 0.5593   | 0.5491 | 0.5446    | 0.5593 |
| 1.0119        | 3.0   | 27   | 0.9259          | 0.6102   | 0.6106 | 0.6147    | 0.6102 |
| 0.9118        | 4.0   | 36   | 0.8659          | 0.5847   | 0.5349 | 0.5835    | 0.5847 |
| 0.8921        | 5.0   | 45   | 0.7925          | 0.6356   | 0.6133 | 0.6275    | 0.6356 |
| 0.83          | 6.0   | 54   | 0.7776          | 0.6271   | 0.6087 | 0.6199    | 0.6271 |
| 0.8015        | 7.0   | 63   | 0.7675          | 0.6695   | 0.6601 | 0.6871    | 0.6695 |
| 0.7334        | 8.0   | 72   | 0.7133          | 0.6780   | 0.6659 | 0.6748    | 0.6780 |
| 0.696         | 9.0   | 81   | 0.6939          | 0.6864   | 0.6758 | 0.6833    | 0.6864 |
| 0.6349        | 10.0  | 90   | 0.6555          | 0.7119   | 0.7057 | 0.7085    | 0.7119 |
| 0.6482        | 11.0  | 99   | 0.6585          | 0.7288   | 0.7202 | 0.7339    | 0.7288 |
| 0.5924        | 12.0  | 108  | 0.6223          | 0.7373   | 0.7332 | 0.7343    | 0.7373 |
| 0.5437        | 13.0  | 117  | 0.6364          | 0.7288   | 0.7231 | 0.7296    | 0.7288 |
| 0.5653        | 14.0  | 126  | 0.6158          | 0.7373   | 0.7266 | 0.7342    | 0.7373 |
| 0.5314        | 15.0  | 135  | 0.6104          | 0.7458   | 0.7439 | 0.7435    | 0.7458 |
| 0.4912        | 16.0  | 144  | 0.6119          | 0.7458   | 0.7433 | 0.7442    | 0.7458 |
| 0.4819        | 17.0  | 153  | 0.6040          | 0.7458   | 0.7452 | 0.7448    | 0.7458 |
| 0.4873        | 18.0  | 162  | 0.6113          | 0.7288   | 0.7248 | 0.7275    | 0.7288 |
| 0.4729        | 19.0  | 171  | 0.6035          | 0.7373   | 0.7292 | 0.7341    | 0.7373 |
| 0.4654        | 20.0  | 180  | 0.6036          | 0.7458   | 0.7409 | 0.7420    | 0.7458 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

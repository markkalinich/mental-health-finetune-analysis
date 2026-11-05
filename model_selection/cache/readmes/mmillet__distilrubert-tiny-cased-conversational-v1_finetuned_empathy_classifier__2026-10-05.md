---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
- precision
- recall
model-index:
- name: distilrubert-tiny-cased-conversational-v1_finetuned_empathy_classifier
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilrubert-tiny-cased-conversational-v1_finetuned_empathy_classifier

This model is a fine-tuned version of [DeepPavlov/distilrubert-tiny-cased-conversational-v1](https://huggingface.co/DeepPavlov/distilrubert-tiny-cased-conversational-v1) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6624
- Accuracy: 0.6780
- F1: 0.6878
- Precision: 0.7175
- Recall: 0.6780

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
| 1.09          | 1.0   | 9    | 1.0661          | 0.4407   | 0.4464 | 0.6498    | 0.4407 |
| 1.0292        | 2.0   | 18   | 0.9658          | 0.5678   | 0.5223 | 0.5179    | 0.5678 |
| 0.942         | 3.0   | 27   | 0.8659          | 0.5932   | 0.5807 | 0.5723    | 0.5932 |
| 0.8614        | 4.0   | 36   | 0.7864          | 0.6186   | 0.5924 | 0.5879    | 0.6186 |
| 0.8002        | 5.0   | 45   | 0.7766          | 0.6017   | 0.5946 | 0.6086    | 0.6017 |
| 0.7633        | 6.0   | 54   | 0.7545          | 0.6186   | 0.6022 | 0.6151    | 0.6186 |
| 0.7249        | 7.0   | 63   | 0.7649          | 0.6356   | 0.6381 | 0.6921    | 0.6356 |
| 0.6687        | 8.0   | 72   | 0.7115          | 0.6695   | 0.6741 | 0.7154    | 0.6695 |
| 0.6426        | 9.0   | 81   | 0.6554          | 0.6864   | 0.6761 | 0.6807    | 0.6864 |
| 0.6144        | 10.0  | 90   | 0.6649          | 0.6864   | 0.6909 | 0.7172    | 0.6864 |
| 0.6252        | 11.0  | 99   | 0.8685          | 0.6186   | 0.6118 | 0.6880    | 0.6186 |
| 0.5988        | 12.0  | 108  | 0.6306          | 0.6949   | 0.7015 | 0.7107    | 0.6949 |
| 0.56          | 13.0  | 117  | 0.6919          | 0.6610   | 0.6662 | 0.7061    | 0.6610 |
| 0.5468        | 14.0  | 126  | 0.6563          | 0.6949   | 0.6980 | 0.7188    | 0.6949 |
| 0.5658        | 15.0  | 135  | 0.6351          | 0.6949   | 0.7048 | 0.7280    | 0.6949 |
| 0.5262        | 16.0  | 144  | 0.6902          | 0.6780   | 0.6821 | 0.7173    | 0.6780 |
| 0.4777        | 17.0  | 153  | 0.6237          | 0.6949   | 0.6981 | 0.7056    | 0.6949 |
| 0.4771        | 18.0  | 162  | 0.6688          | 0.6780   | 0.6799 | 0.7035    | 0.6780 |
| 0.4737        | 19.0  | 171  | 0.6482          | 0.6864   | 0.6957 | 0.7219    | 0.6864 |
| 0.5033        | 20.0  | 180  | 0.6624          | 0.6780   | 0.6878 | 0.7175    | 0.6780 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1

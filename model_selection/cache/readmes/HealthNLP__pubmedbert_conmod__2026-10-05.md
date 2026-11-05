---
license: mit
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: test
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# test

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6886
- Accuracy: 0.8143
- F1: [0.92816572 0.56028369 0.1        0.2633452 ]

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
- train_batch_size: 32
- eval_batch_size: 64
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | F1                                            |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------------------------------------------:|
| No log        | 1.0   | 37   | 0.4891          | 0.8235   | [0.91702786 0.33333333 0.         0.10837438] |
| No log        | 2.0   | 74   | 0.4762          | 0.8321   | [0.93139159 0.48466258 0.         0.22857143] |
| No log        | 3.0   | 111  | 0.5084          | 0.8208   | [0.92995725 0.44887781 0.         0.19266055] |
| No log        | 4.0   | 148  | 0.5519          | 0.8105   | [0.92421691 0.44444444 0.06557377 0.30769231] |
| No log        | 5.0   | 185  | 0.5805          | 0.8294   | [0.93531353 0.52336449 0.09345794 0.27131783] |
| No log        | 6.0   | 222  | 0.6778          | 0.7955   | [0.91344509 0.55305466 0.15463918 0.29166667] |
| No log        | 7.0   | 259  | 0.6407          | 0.8213   | [0.93298292 0.51383399 0.10191083 0.2519084 ] |
| No log        | 8.0   | 296  | 0.6639          | 0.8272   | [0.9326288  0.55052265 0.18181818 0.26271186] |
| No log        | 9.0   | 333  | 0.6863          | 0.8192   | [0.93071286 0.55830389 0.11042945 0.2761194 ] |
| No log        | 10.0  | 370  | 0.6886          | 0.8143   | [0.92816572 0.56028369 0.1        0.2633452 ] |


### Framework versions

- Transformers 4.37.2
- Pytorch 2.2.0+cu121
- Datasets 2.17.0
- Tokenizers 0.15.2

---
license: apache-2.0
base_model: facebook/wav2vec2-conformer-rel-pos-large
tags:
- generated_from_trainer
datasets:
- audiofolder
metrics:
- accuracy
- precision
- recall
model-index:
- name: wav2vec2-conformer-rel-pos-large-medical-intent-v2
  results:
  - task:
      name: Audio Classification
      type: audio-classification
    dataset:
      name: audiofolder
      type: audiofolder
      config: default
      split: validation
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.6169590643274854
    - name: Precision
      type: precision
      value: 0.6350528050296339
    - name: Recall
      type: recall
      value: 0.6169590643274854
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-conformer-rel-pos-large-medical-intent-v2

This model is a fine-tuned version of [facebook/wav2vec2-conformer-rel-pos-large](https://huggingface.co/facebook/wav2vec2-conformer-rel-pos-large) on the audiofolder dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0410
- Accuracy: 0.6170
- Precision: 0.6351
- Recall: 0.6170

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 4

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|
| 1.7714        | 1.0   | 82   | 1.7605          | 0.2339   | 0.3198    | 0.2339 |
| 1.511         | 2.0   | 164  | 1.5148          | 0.4298   | 0.3817    | 0.4298 |
| 1.1417        | 2.99  | 246  | 1.1530          | 0.5936   | 0.6491    | 0.5936 |
| 0.8747        | 3.99  | 328  | 1.0410          | 0.6170   | 0.6351    | 0.6170 |


### Framework versions

- Transformers 4.39.1
- Pytorch 2.2.1+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2

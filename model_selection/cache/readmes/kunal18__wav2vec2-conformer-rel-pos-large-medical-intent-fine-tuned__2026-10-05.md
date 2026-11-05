---
base_model: kunal18/wav2vec2-conformer-rel-pos-large-medical-intent-medical-intent_v3
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
model-index:
- name: wav2vec2-conformer-rel-pos-large-medical-intent-medical-intent-fine-tuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-conformer-rel-pos-large-medical-intent-medical-intent_v3-medical-intent_v10

This model is a fine-tuned version of [facebook/wav2vec2-conformer-rel-pos-large](https://huggingface.co/facebook/wav2vec2-conformer-rel-pos-large) on the audiofolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6879
- Accuracy: 0.7719
- Precision: 0.8161
- Recall: 0.7719

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
| 0.4975        | 1.0   | 82   | 0.9533          | 0.6813   | 0.7198    | 0.6813 |
| 0.3092        | 2.0   | 164  | 0.7844          | 0.7456   | 0.7800    | 0.7456 |
| 0.2968        | 2.99  | 246  | 0.7393          | 0.7544   | 0.7960    | 0.7544 |
| 0.3001        | 3.99  | 328  | 0.6879          | 0.7719   | 0.8161    | 0.7719 |


### Framework versions

- Transformers 4.39.2
- Pytorch 2.2.0+cu121
- Datasets 2.18.0
- Tokenizers 0.15.2

---
license: apache-2.0
base_model: google-bert/bert-base-cased
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: bert-base-cased-symptom-to-diagnosis-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-cased-symptom-to-diagnosis-finetuned

This model is a fine-tuned version of [google-bert/bert-base-cased](https://huggingface.co/google-bert/bert-base-cased) on an gretelai/symptom_to_diagnosis dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4252
- Accuracy: 0.5377

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.9247        | 1.0   | 100  | 2.9084          | 0.1887   |
| 2.6966        | 2.0   | 200  | 2.5600          | 0.5236   |
| 2.4543        | 3.0   | 300  | 2.4252          | 0.5377   |


### Framework versions

- Transformers 4.39.3
- Pytorch 2.2.2+cpu
- Datasets 2.18.0
- Tokenizers 0.15.2

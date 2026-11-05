---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/cantemist-85-ner
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: output
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: Rodrigo1771/cantemist-85-ner
      type: Rodrigo1771/cantemist-85-ner
      config: CantemistNer
      split: validation
      args: CantemistNer
    metrics:
    - name: Precision
      type: precision
      value: 0.8399232245681382
    - name: Recall
      type: recall
      value: 0.8617565970854667
    - name: F1
      type: f1
      value: 0.8506998444790046
    - name: Accuracy
      type: accuracy
      value: 0.9916544445403043
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/cantemist-85-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0496
- Precision: 0.8399
- Recall: 0.8618
- F1: 0.8507
- Accuracy: 0.9917

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0542        | 1.0   | 511  | 0.0271          | 0.7485    | 0.7972 | 0.7721 | 0.9895   |
| 0.0184        | 2.0   | 1022 | 0.0277          | 0.7897    | 0.8519 | 0.8196 | 0.9906   |
| 0.0103        | 3.0   | 1533 | 0.0305          | 0.8238    | 0.8488 | 0.8361 | 0.9914   |
| 0.0058        | 4.0   | 2044 | 0.0320          | 0.8197    | 0.8539 | 0.8364 | 0.9913   |
| 0.0041        | 5.0   | 2555 | 0.0374          | 0.8397    | 0.8417 | 0.8407 | 0.9917   |
| 0.0026        | 6.0   | 3066 | 0.0427          | 0.8368    | 0.8503 | 0.8435 | 0.9917   |
| 0.0015        | 7.0   | 3577 | 0.0451          | 0.8207    | 0.8598 | 0.8398 | 0.9912   |
| 0.0013        | 8.0   | 4088 | 0.0448          | 0.8318    | 0.8629 | 0.8471 | 0.9916   |
| 0.0007        | 9.0   | 4599 | 0.0496          | 0.8399    | 0.8618 | 0.8507 | 0.9917   |
| 0.0006        | 10.0  | 5110 | 0.0503          | 0.8399    | 0.8618 | 0.8507 | 0.9916   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

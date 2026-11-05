---
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/combined-train-drugtemist-dev-ner
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
      name: Rodrigo1771/combined-train-drugtemist-dev-ner
      type: Rodrigo1771/combined-train-drugtemist-dev-ner
      config: CombinedTrainDrugTEMISTDevNER
      split: validation
      args: CombinedTrainDrugTEMISTDevNER
    metrics:
    - name: Precision
      type: precision
      value: 0.09532555790247038
    - name: Recall
      type: recall
      value: 0.9540441176470589
    - name: F1
      type: f1
      value: 0.17333222008850296
    - name: Accuracy
      type: accuracy
      value: 0.7932840841995413
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/combined-train-drugtemist-dev-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0503
- Precision: 0.0953
- Recall: 0.9540
- F1: 0.1733
- Accuracy: 0.7933

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

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.9988 | 425  | 0.6611          | 0.0883    | 0.9292 | 0.1613 | 0.7850   |
| 0.3349        | 2.0    | 851  | 0.9204          | 0.0787    | 0.9301 | 0.1451 | 0.7551   |
| 0.1788        | 2.9988 | 1276 | 0.9545          | 0.0844    | 0.9329 | 0.1549 | 0.7645   |
| 0.1227        | 4.0    | 1702 | 1.0924          | 0.0885    | 0.9412 | 0.1618 | 0.7692   |
| 0.0856        | 4.9988 | 2127 | 1.0503          | 0.0953    | 0.9540 | 0.1733 | 0.7933   |
| 0.0597        | 6.0    | 2553 | 1.2642          | 0.0912    | 0.9449 | 0.1663 | 0.7788   |
| 0.0597        | 6.9988 | 2978 | 1.3262          | 0.0928    | 0.9485 | 0.1690 | 0.7829   |
| 0.0458        | 8.0    | 3404 | 1.3698          | 0.0926    | 0.9522 | 0.1688 | 0.7849   |
| 0.0343        | 8.9988 | 3829 | 1.4433          | 0.0907    | 0.9449 | 0.1655 | 0.7822   |
| 0.0292        | 9.9882 | 4250 | 1.4862          | 0.0914    | 0.9458 | 0.1667 | 0.7821   |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

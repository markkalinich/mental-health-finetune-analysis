---
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/combined-train-distemist-dev-ner
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
      name: Rodrigo1771/combined-train-distemist-dev-ner
      type: Rodrigo1771/combined-train-distemist-dev-ner
      config: CombinedTrainDisTEMISTDevNER
      split: validation
      args: CombinedTrainDisTEMISTDevNER
    metrics:
    - name: Precision
      type: precision
      value: 0.32197630636422075
    - name: Recall
      type: recall
      value: 0.8203088441740758
    - name: F1
      type: f1
      value: 0.4624414693662204
    - name: Accuracy
      type: accuracy
      value: 0.8601754843670617
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/combined-train-distemist-dev-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6266
- Precision: 0.3220
- Recall: 0.8203
- F1: 0.4624
- Accuracy: 0.8602

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
| No log        | 0.9988 | 425  | 0.3834          | 0.2920    | 0.7819 | 0.4252 | 0.8517   |
| 0.3349        | 2.0    | 851  | 0.5730          | 0.2681    | 0.8070 | 0.4025 | 0.8221   |
| 0.1788        | 2.9988 | 1276 | 0.5796          | 0.2848    | 0.8009 | 0.4202 | 0.8338   |
| 0.1227        | 4.0    | 1702 | 0.6591          | 0.2996    | 0.8109 | 0.4376 | 0.8388   |
| 0.0856        | 4.9988 | 2127 | 0.6266          | 0.3220    | 0.8203 | 0.4624 | 0.8602   |
| 0.0597        | 6.0    | 2553 | 0.7859          | 0.3075    | 0.8112 | 0.4460 | 0.8476   |
| 0.0597        | 6.9988 | 2978 | 0.8297          | 0.3137    | 0.8166 | 0.4532 | 0.8508   |
| 0.0458        | 8.0    | 3404 | 0.8468          | 0.3135    | 0.8205 | 0.4536 | 0.8532   |
| 0.0343        | 8.9988 | 3829 | 0.9241          | 0.3085    | 0.8182 | 0.4481 | 0.8494   |
| 0.0292        | 9.9882 | 4250 | 0.9384          | 0.3100    | 0.8163 | 0.4494 | 0.8499   |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

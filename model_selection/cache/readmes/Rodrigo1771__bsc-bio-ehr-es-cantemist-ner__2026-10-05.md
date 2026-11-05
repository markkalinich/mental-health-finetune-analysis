---
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/cantemist-ner
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
      name: Rodrigo1771/cantemist-ner
      type: Rodrigo1771/cantemist-ner
      config: CantemistNer
      split: validation
      args: CantemistNer
    metrics:
    - name: Precision
      type: precision
      value: 0.8416602613374328
    - name: Recall
      type: recall
      value: 0.8625443087829854
    - name: F1
      type: f1
      value: 0.8519743240614666
    - name: Accuracy
      type: accuracy
      value: 0.9919995398728899
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/cantemist-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0382
- Precision: 0.8417
- Recall: 0.8625
- F1: 0.8520
- Accuracy: 0.9920

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
| No log        | 1.0   | 454  | 0.0249          | 0.7532    | 0.8247 | 0.7874 | 0.9905   |
| 0.0456        | 2.0   | 908  | 0.0236          | 0.7735    | 0.8365 | 0.8038 | 0.9907   |
| 0.0175        | 3.0   | 1362 | 0.0264          | 0.8018    | 0.8460 | 0.8233 | 0.9908   |
| 0.0106        | 4.0   | 1816 | 0.0289          | 0.8084    | 0.8507 | 0.8290 | 0.9915   |
| 0.0066        | 5.0   | 2270 | 0.0320          | 0.8135    | 0.8523 | 0.8325 | 0.9916   |
| 0.004         | 6.0   | 2724 | 0.0382          | 0.8044    | 0.8582 | 0.8304 | 0.9909   |
| 0.0027        | 7.0   | 3178 | 0.0382          | 0.8417    | 0.8625 | 0.8520 | 0.9920   |
| 0.0017        | 8.0   | 3632 | 0.0433          | 0.8301    | 0.8657 | 0.8475 | 0.9916   |
| 0.001         | 9.0   | 4086 | 0.0442          | 0.8340    | 0.8649 | 0.8492 | 0.9918   |
| 0.0006        | 10.0  | 4540 | 0.0459          | 0.8356    | 0.8649 | 0.8500 | 0.9918   |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

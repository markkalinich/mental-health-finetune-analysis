---
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/drugtemist-ner
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
      name: Rodrigo1771/drugtemist-ner
      type: Rodrigo1771/drugtemist-ner
      config: DrugTEMIST NER
      split: validation
      args: DrugTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.9394760614272809
    - name: Recall
      type: recall
      value: 0.9558823529411765
    - name: F1
      type: f1
      value: 0.9476082004555808
    - name: Accuracy
      type: accuracy
      value: 0.9989632965795653
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/drugtemist-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0055
- Precision: 0.9395
- Recall: 0.9559
- F1: 0.9476
- Accuracy: 0.9990

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
| No log        | 0.9988 | 425  | 0.0050          | 0.9251    | 0.8971 | 0.9109 | 0.9982   |
| 0.0196        | 2.0    | 851  | 0.0038          | 0.9400    | 0.9219 | 0.9309 | 0.9988   |
| 0.0031        | 2.9988 | 1276 | 0.0035          | 0.9335    | 0.9292 | 0.9314 | 0.9988   |
| 0.0017        | 4.0    | 1702 | 0.0041          | 0.9119    | 0.9605 | 0.9355 | 0.9988   |
| 0.0009        | 4.9988 | 2127 | 0.0047          | 0.9393    | 0.9522 | 0.9457 | 0.9989   |
| 0.0004        | 6.0    | 2553 | 0.0055          | 0.9413    | 0.9430 | 0.9421 | 0.9989   |
| 0.0004        | 6.9988 | 2978 | 0.0054          | 0.9320    | 0.9577 | 0.9447 | 0.9989   |
| 0.0003        | 8.0    | 3404 | 0.0053          | 0.9346    | 0.9596 | 0.9469 | 0.9989   |
| 0.0002        | 8.9988 | 3829 | 0.0057          | 0.9385    | 0.9531 | 0.9457 | 0.9989   |
| 0.0001        | 9.9882 | 4250 | 0.0055          | 0.9395    | 0.9559 | 0.9476 | 0.9990   |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/symptemist-fasttext-85-ner
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
      name: Rodrigo1771/symptemist-fasttext-85-ner
      type: Rodrigo1771/symptemist-fasttext-85-ner
      config: SympTEMIST NER
      split: validation
      args: SympTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.6529382219989954
    - name: Recall
      type: recall
      value: 0.7115489874110563
    - name: F1
      type: f1
      value: 0.680984808800419
    - name: Accuracy
      type: accuracy
      value: 0.9473354935994097
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/symptemist-fasttext-85-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2808
- Precision: 0.6529
- Recall: 0.7115
- F1: 0.6810
- Accuracy: 0.9473

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
| No log        | 1.0   | 171  | 0.1502          | 0.5421    | 0.6765 | 0.6019 | 0.9458   |
| No log        | 2.0   | 342  | 0.1539          | 0.5958    | 0.6793 | 0.6348 | 0.9468   |
| 0.1273        | 3.0   | 513  | 0.1838          | 0.6326    | 0.7077 | 0.6680 | 0.9468   |
| 0.1273        | 4.0   | 684  | 0.2018          | 0.6322    | 0.7121 | 0.6698 | 0.9466   |
| 0.1273        | 5.0   | 855  | 0.2153          | 0.6441    | 0.7192 | 0.6796 | 0.9465   |
| 0.0234        | 6.0   | 1026 | 0.2498          | 0.6461    | 0.7006 | 0.6723 | 0.9470   |
| 0.0234        | 7.0   | 1197 | 0.2653          | 0.6362    | 0.7209 | 0.6759 | 0.9462   |
| 0.0234        | 8.0   | 1368 | 0.2808          | 0.6529    | 0.7115 | 0.6810 | 0.9473   |
| 0.0082        | 9.0   | 1539 | 0.2917          | 0.6458    | 0.7115 | 0.6771 | 0.9467   |
| 0.0082        | 10.0  | 1710 | 0.2930          | 0.6548    | 0.7072 | 0.6800 | 0.9481   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/symptemist-8-ner
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
      name: Rodrigo1771/symptemist-8-ner
      type: Rodrigo1771/symptemist-8-ner
      config: SympTEMIST NER
      split: validation
      args: SympTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.6832101372756072
    - name: Recall
      type: recall
      value: 0.7082649151614668
    - name: F1
      type: f1
      value: 0.6955119591507659
    - name: Accuracy
      type: accuracy
      value: 0.9498058968847252
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/symptemist-8-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3003
- Precision: 0.6832
- Recall: 0.7083
- F1: 0.6955
- Accuracy: 0.9498

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
| No log        | 0.9976 | 209  | 0.1511          | 0.5818    | 0.6694 | 0.6226 | 0.9457   |
| No log        | 2.0    | 419  | 0.1794          | 0.6113    | 0.7017 | 0.6534 | 0.9465   |
| 0.1282        | 2.9976 | 628  | 0.2102          | 0.6572    | 0.6979 | 0.6769 | 0.9470   |
| 0.1282        | 4.0    | 838  | 0.2329          | 0.6605    | 0.6984 | 0.6789 | 0.9489   |
| 0.0255        | 4.9976 | 1047 | 0.2591          | 0.6646    | 0.6973 | 0.6806 | 0.9491   |
| 0.0255        | 6.0    | 1257 | 0.2737          | 0.6599    | 0.6968 | 0.6778 | 0.9491   |
| 0.0255        | 6.9976 | 1466 | 0.2876          | 0.6687    | 0.7094 | 0.6884 | 0.9492   |
| 0.0085        | 8.0    | 1676 | 0.3003          | 0.6832    | 0.7083 | 0.6955 | 0.9498   |
| 0.0085        | 8.9976 | 1885 | 0.3072          | 0.6697    | 0.7170 | 0.6926 | 0.9492   |
| 0.004         | 9.9761 | 2090 | 0.3125          | 0.6711    | 0.7137 | 0.6918 | 0.9492   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

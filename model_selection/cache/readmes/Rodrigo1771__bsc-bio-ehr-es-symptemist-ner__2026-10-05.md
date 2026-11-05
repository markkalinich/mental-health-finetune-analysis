---
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/symptemist-ner
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
      name: Rodrigo1771/symptemist-ner
      type: Rodrigo1771/symptemist-ner
      config: SympTEMIST NER
      split: validation
      args: SympTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.6675139806812405
    - name: Recall
      type: recall
      value: 0.7186644772851669
    - name: F1
      type: f1
      value: 0.6921454928835002
    - name: Accuracy
      type: accuracy
      value: 0.9483461131252205
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/symptemist-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2747
- Precision: 0.6675
- Recall: 0.7187
- F1: 0.6921
- Accuracy: 0.9483

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
| No log        | 1.0   | 150  | 0.1504          | 0.5091    | 0.6409 | 0.5675 | 0.9456   |
| No log        | 2.0   | 300  | 0.1547          | 0.5881    | 0.6995 | 0.639  | 0.9462   |
| No log        | 3.0   | 450  | 0.1618          | 0.6237    | 0.6984 | 0.6589 | 0.9476   |
| 0.126         | 4.0   | 600  | 0.1920          | 0.6154    | 0.7181 | 0.6628 | 0.9451   |
| 0.126         | 5.0   | 750  | 0.2102          | 0.6561    | 0.7028 | 0.6786 | 0.9488   |
| 0.126         | 6.0   | 900  | 0.2414          | 0.6443    | 0.7088 | 0.6750 | 0.9467   |
| 0.0251        | 7.0   | 1050 | 0.2500          | 0.6588    | 0.7061 | 0.6816 | 0.9492   |
| 0.0251        | 8.0   | 1200 | 0.2642          | 0.6440    | 0.7307 | 0.6846 | 0.9474   |
| 0.0251        | 9.0   | 1350 | 0.2747          | 0.6675    | 0.7187 | 0.6921 | 0.9483   |
| 0.0091        | 10.0  | 1500 | 0.2767          | 0.6595    | 0.7187 | 0.6878 | 0.9488   |


### Framework versions

- Transformers 4.42.4
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/symptemist-fasttext-8-ner
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
      name: Rodrigo1771/symptemist-fasttext-8-ner
      type: Rodrigo1771/symptemist-fasttext-8-ner
      config: SympTEMIST NER
      split: validation
      args: SympTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.6764102564102564
    - name: Recall
      type: recall
      value: 0.7219485495347564
    - name: F1
      type: f1
      value: 0.6984379136881121
    - name: Accuracy
      type: accuracy
      value: 0.9500465205813469
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/symptemist-fasttext-8-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3073
- Precision: 0.6764
- Recall: 0.7219
- F1: 0.6984
- Accuracy: 0.9500

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
| No log        | 0.9975 | 203  | 0.1501          | 0.5960    | 0.6338 | 0.6143 | 0.9468   |
| No log        | 2.0    | 407  | 0.1761          | 0.6529    | 0.6940 | 0.6729 | 0.9492   |
| 0.1312        | 2.9975 | 610  | 0.1995          | 0.6322    | 0.7170 | 0.6720 | 0.9470   |
| 0.1312        | 4.0    | 814  | 0.2182          | 0.6446    | 0.7137 | 0.6774 | 0.9483   |
| 0.0248        | 4.9975 | 1017 | 0.2461          | 0.6251    | 0.7219 | 0.6701 | 0.9449   |
| 0.0248        | 6.0    | 1221 | 0.2695          | 0.6410    | 0.7302 | 0.6827 | 0.9469   |
| 0.0248        | 6.9975 | 1424 | 0.2829          | 0.6529    | 0.7340 | 0.6911 | 0.9470   |
| 0.0081        | 8.0    | 1628 | 0.2982          | 0.6711    | 0.7181 | 0.6938 | 0.9494   |
| 0.0081        | 8.9975 | 1831 | 0.3073          | 0.6764    | 0.7219 | 0.6984 | 0.9500   |
| 0.0038        | 9.9754 | 2030 | 0.3079          | 0.6713    | 0.7165 | 0.6931 | 0.9500   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

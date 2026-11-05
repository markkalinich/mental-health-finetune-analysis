---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/distemist-fasttext-75-ner
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
      name: Rodrigo1771/distemist-fasttext-75-ner
      type: Rodrigo1771/distemist-fasttext-75-ner
      config: DisTEMIST NER
      split: validation
      args: DisTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.7991246256622898
    - name: Recall
      type: recall
      value: 0.8116518483855872
    - name: F1
      type: f1
      value: 0.8053395240858967
    - name: Accuracy
      type: accuracy
      value: 0.9758743323218038
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/distemist-fasttext-75-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1711
- Precision: 0.7991
- Recall: 0.8117
- F1: 0.8053
- Accuracy: 0.9759

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
| 0.1165        | 0.9993 | 702  | 0.0809          | 0.7455    | 0.8039 | 0.7736 | 0.9735   |
| 0.0461        | 2.0    | 1405 | 0.0956          | 0.7611    | 0.8067 | 0.7833 | 0.9747   |
| 0.0165        | 2.9993 | 2107 | 0.1057          | 0.7721    | 0.7990 | 0.7853 | 0.9744   |
| 0.011         | 4.0    | 2810 | 0.1274          | 0.7759    | 0.8196 | 0.7971 | 0.9751   |
| 0.006         | 4.9993 | 3512 | 0.1358          | 0.7904    | 0.8049 | 0.7976 | 0.9745   |
| 0.0045        | 6.0    | 4215 | 0.1420          | 0.7911    | 0.7985 | 0.7948 | 0.9746   |
| 0.0037        | 6.9993 | 4917 | 0.1601          | 0.7925    | 0.8000 | 0.7962 | 0.9749   |
| 0.0022        | 8.0    | 5620 | 0.1621          | 0.8000    | 0.8102 | 0.8051 | 0.9758   |
| 0.0016        | 8.9993 | 6322 | 0.1681          | 0.7972    | 0.8086 | 0.8029 | 0.9758   |
| 0.0013        | 9.9929 | 7020 | 0.1711          | 0.7991    | 0.8117 | 0.8053 | 0.9759   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

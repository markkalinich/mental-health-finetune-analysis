---
library_name: transformers
license: apache-2.0
base_model: PlanTL-GOB-ES/bsc-bio-ehr-es
tags:
- token-classification
- generated_from_trainer
datasets:
- Rodrigo1771/distemist-85-ner
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
      name: Rodrigo1771/distemist-85-ner
      type: Rodrigo1771/distemist-85-ner
      config: DisTEMIST NER
      split: validation
      args: DisTEMIST NER
    metrics:
    - name: Precision
      type: precision
      value: 0.803175344384777
    - name: Recall
      type: recall
      value: 0.8048666354702855
    - name: F1
      type: f1
      value: 0.8040201005025126
    - name: Accuracy
      type: accuracy
      value: 0.9764853694371592
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# output

This model is a fine-tuned version of [PlanTL-GOB-ES/bsc-bio-ehr-es](https://huggingface.co/PlanTL-GOB-ES/bsc-bio-ehr-es) on the Rodrigo1771/distemist-85-ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1424
- Precision: 0.8032
- Recall: 0.8049
- F1: 0.8040
- Accuracy: 0.9765

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
| No log        | 0.9990 | 499  | 0.0739          | 0.7271    | 0.7953 | 0.7596 | 0.9731   |
| 0.105         | 2.0    | 999  | 0.0908          | 0.7436    | 0.7890 | 0.7656 | 0.9729   |
| 0.0448        | 2.9990 | 1498 | 0.0930          | 0.7676    | 0.7990 | 0.7830 | 0.9744   |
| 0.0255        | 4.0    | 1998 | 0.1052          | 0.7806    | 0.7983 | 0.7894 | 0.9757   |
| 0.0164        | 4.9990 | 2497 | 0.1100          | 0.7756    | 0.8007 | 0.7879 | 0.9750   |
| 0.0112        | 6.0    | 2997 | 0.1266          | 0.7869    | 0.8124 | 0.7994 | 0.9768   |
| 0.0073        | 6.9990 | 3496 | 0.1288          | 0.7929    | 0.8009 | 0.7969 | 0.9763   |
| 0.0054        | 8.0    | 3996 | 0.1424          | 0.8032    | 0.8049 | 0.8040 | 0.9765   |
| 0.0038        | 8.9990 | 4495 | 0.1455          | 0.7901    | 0.8042 | 0.7971 | 0.9765   |
| 0.0028        | 9.9900 | 4990 | 0.1497          | 0.7898    | 0.8072 | 0.7984 | 0.9768   |


### Framework versions

- Transformers 4.44.2
- Pytorch 2.4.0+cu121
- Datasets 2.21.0
- Tokenizers 0.19.1

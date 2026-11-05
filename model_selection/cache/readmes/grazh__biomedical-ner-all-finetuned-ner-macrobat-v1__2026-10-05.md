---
library_name: transformers
license: apache-2.0
base_model: d4data/biomedical-ner-all
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: biomedical-ner-all-finetuned-ner-macrobat-v1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# biomedical-ner-all-finetuned-ner-macrobat-v1

This model is a fine-tuned version of [d4data/biomedical-ner-all](https://huggingface.co/d4data/biomedical-ner-all) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3977
- Precision: 0.7596
- Recall: 0.8095
- F1: 0.7837
- Accuracy: 0.8995

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 40

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 12   | 0.9921          | 0.4039    | 0.2615 | 0.3174 | 0.7220   |
| No log        | 2.0   | 24   | 0.6671          | 0.4591    | 0.5475 | 0.4994 | 0.8118   |
| No log        | 3.0   | 36   | 0.5148          | 0.5729    | 0.6826 | 0.6229 | 0.8485   |
| No log        | 4.0   | 48   | 0.4427          | 0.6332    | 0.7487 | 0.6861 | 0.8718   |
| No log        | 5.0   | 60   | 0.4042          | 0.6693    | 0.7646 | 0.7138 | 0.8783   |
| No log        | 6.0   | 72   | 0.3779          | 0.6896    | 0.7771 | 0.7308 | 0.8858   |
| No log        | 7.0   | 84   | 0.3691          | 0.7077    | 0.7979 | 0.7501 | 0.8902   |
| No log        | 8.0   | 96   | 0.3669          | 0.7193    | 0.8037 | 0.7592 | 0.8914   |
| No log        | 9.0   | 108  | 0.3684          | 0.7254    | 0.8027 | 0.7621 | 0.8941   |
| No log        | 10.0  | 120  | 0.3670          | 0.7398    | 0.8119 | 0.7741 | 0.8974   |
| No log        | 11.0  | 132  | 0.3655          | 0.7466    | 0.8017 | 0.7732 | 0.8980   |
| No log        | 12.0  | 144  | 0.3732          | 0.7515    | 0.8123 | 0.7807 | 0.8971   |
| No log        | 13.0  | 156  | 0.3824          | 0.7487    | 0.8075 | 0.7770 | 0.8989   |
| No log        | 14.0  | 168  | 0.3774          | 0.7590    | 0.8051 | 0.7814 | 0.8990   |
| No log        | 15.0  | 180  | 0.3837          | 0.7531    | 0.8032 | 0.7773 | 0.8984   |
| No log        | 16.0  | 192  | 0.3937          | 0.7554    | 0.8119 | 0.7826 | 0.8987   |
| No log        | 17.0  | 204  | 0.3977          | 0.7596    | 0.8095 | 0.7837 | 0.8995   |
| No log        | 18.0  | 216  | 0.4063          | 0.7520    | 0.8075 | 0.7788 | 0.8980   |
| No log        | 19.0  | 228  | 0.4077          | 0.7537    | 0.8017 | 0.7770 | 0.8969   |
| No log        | 20.0  | 240  | 0.4140          | 0.7489    | 0.8099 | 0.7782 | 0.8975   |
| No log        | 21.0  | 252  | 0.4186          | 0.7515    | 0.8123 | 0.7807 | 0.8976   |
| No log        | 22.0  | 264  | 0.4266          | 0.7383    | 0.8109 | 0.7729 | 0.8947   |


### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.0+cu126
- Datasets 3.6.0
- Tokenizers 0.22.1

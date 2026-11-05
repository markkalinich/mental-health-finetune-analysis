---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_negsampling_llama_1090
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_negsampling_llama_1090

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1339
- F1: 0.8971

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0955        | 1.0   | 189  | 0.1067          | 0.8062 |
| 0.1143        | 2.0   | 378  | 0.0999          | 0.8636 |
| 0.1016        | 3.0   | 567  | 0.1218          | 0.8529 |
| 0.0495        | 4.0   | 756  | 0.1019          | 0.8690 |
| 0.1565        | 5.0   | 945  | 0.1487          | 0.8702 |
| 0.0156        | 6.0   | 1134 | 0.1370          | 0.8777 |
| 0.0105        | 7.0   | 1323 | 0.1297          | 0.8841 |
| 0.0417        | 8.0   | 1512 | 0.1456          | 0.8592 |
| 0.0179        | 9.0   | 1701 | 0.1414          | 0.8921 |
| 0.016         | 10.0  | 1890 | 0.1339          | 0.8971 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0

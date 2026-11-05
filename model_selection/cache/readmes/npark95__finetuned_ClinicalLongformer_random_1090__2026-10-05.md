---
library_name: transformers
base_model: yikuan8/Clinical-Longformer
tags:
- generated_from_trainer
metrics:
- f1
model-index:
- name: finetuned_ClinicalLongformer_random_1090
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# finetuned_ClinicalLongformer_random_1090

This model is a fine-tuned version of [yikuan8/Clinical-Longformer](https://huggingface.co/yikuan8/Clinical-Longformer) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1601
- F1: 0.8777

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 8e-06
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 0.0807        | 1.0   | 189  | 0.2094          | 0.7681 |
| 0.2059        | 2.0   | 378  | 0.1441          | 0.8296 |
| 0.0632        | 3.0   | 567  | 0.1467          | 0.8633 |
| 0.0194        | 4.0   | 756  | 0.1497          | 0.8592 |
| 0.0751        | 5.0   | 945  | 0.1559          | 0.8671 |
| 0.0723        | 6.0   | 1134 | 0.1708          | 0.8732 |
| 0.0007        | 7.0   | 1323 | 0.1601          | 0.8777 |
| 0.0231        | 8.0   | 1512 | 0.1852          | 0.8652 |
| 0.1065        | 9.0   | 1701 | 0.1886          | 0.8633 |
| 0.0519        | 10.0  | 1890 | 0.1812          | 0.8714 |
| 0.0259        | 11.0  | 2079 | 0.1956          | 0.8696 |
| 0.0697        | 12.0  | 2268 | 0.1921          | 0.8714 |
| 0.0271        | 13.0  | 2457 | 0.2098          | 0.8551 |
| 0.0073        | 14.0  | 2646 | 0.2109          | 0.8551 |
| 0.0002        | 15.0  | 2835 | 0.2142          | 0.8551 |


### Framework versions

- Transformers 4.48.0
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0

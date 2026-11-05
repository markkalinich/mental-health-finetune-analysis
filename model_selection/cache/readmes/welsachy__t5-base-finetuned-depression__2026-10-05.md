---
license: apache-2.0
base_model: google-t5/t5-base
tags:
- generated_from_trainer
metrics:
- rouge
- precision
- recall
- f1
- accuracy
model-index:
- name: t5-base-finetuned-depression
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-finetuned-depression

This model is a fine-tuned version of [google-t5/t5-base](https://huggingface.co/google-t5/t5-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2260
- Rouge1: 89.7655
- Rouge2: 24.4136
- Rougel: 89.7655
- Rougelsum: 89.7655
- Gen Len: 2.2719
- Precision: 0.8856
- Recall: 0.8807
- F1: 0.8817
- Accuracy: 0.8977

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 469  | 0.3428          | 69.6162 | 9.7015  | 69.5096 | 69.6162   | 2.1087  | 0.8545    | 0.4409 | 0.4375 | 0.6962   |
| 0.7863        | 2.0   | 938  | 0.2674          | 79.5309 | 19.0832 | 79.5309 | 79.5309   | 2.2058  | 0.8192    | 0.5744 | 0.6052 | 0.7953   |
| 0.3128        | 3.0   | 1407 | 0.2317          | 84.0085 | 21.322  | 84.0085 | 84.0085   | 2.2239  | 0.9053    | 0.6654 | 0.721  | 0.8401   |
| 0.2367        | 4.0   | 1876 | 0.1736          | 86.887  | 22.3881 | 86.887  | 86.887    | 2.242   | 0.6608    | 0.586  | 0.6155 | 0.8689   |
| 0.1844        | 5.0   | 2345 | 0.1802          | 88.5928 | 22.7079 | 88.5928 | 88.5928   | 2.2388  | 0.9113    | 0.8252 | 0.8597 | 0.8859   |
| 0.135         | 6.0   | 2814 | 0.2000          | 88.4861 | 22.2814 | 88.4861 | 88.4861   | 2.2345  | 0.9045    | 0.8405 | 0.8655 | 0.8849   |
| 0.1247        | 7.0   | 3283 | 0.2048          | 89.5522 | 23.5608 | 89.4989 | 89.5522   | 2.2495  | 0.9108    | 0.8526 | 0.8769 | 0.8955   |
| 0.1071        | 8.0   | 3752 | 0.2361          | 89.1258 | 23.7207 | 89.1258 | 89.1258   | 2.2591  | 0.6783    | 0.6467 | 0.6603 | 0.8913   |
| 0.0832        | 9.0   | 4221 | 0.2486          | 89.8721 | 24.5203 | 89.8721 | 89.8721   | 2.2889  | 0.6695    | 0.6532 | 0.6603 | 0.8987   |
| 0.0652        | 10.0  | 4690 | 0.3051          | 89.339  | 23.1343 | 89.339  | 89.339    | 2.2473  | 0.9065    | 0.8642 | 0.8811 | 0.8934   |
| 0.0674        | 11.0  | 5159 | 0.3269          | 89.7655 | 23.9872 | 89.7655 | 89.7655   | 2.2623  | 0.8973    | 0.8711 | 0.8819 | 0.8977   |
| 0.0575        | 12.0  | 5628 | 0.3241          | 89.4456 | 23.8806 | 89.4456 | 89.4456   | 2.2633  | 0.8903    | 0.8652 | 0.8756 | 0.8945   |
| 0.0422        | 13.0  | 6097 | 0.3088          | 90.0853 | 24.5203 | 90.0853 | 90.0853   | 2.2729  | 0.6754    | 0.6595 | 0.6664 | 0.9009   |
| 0.0395        | 14.0  | 6566 | 0.2781          | 90.0853 | 25.3731 | 90.0853 | 90.0853   | 2.2889  | 0.6801    | 0.6575 | 0.6681 | 0.9009   |
| 0.0341        | 15.0  | 7035 | 0.2658          | 90.1919 | 24.5203 | 90.1919 | 90.1919   | 2.2719  | 0.9043    | 0.8836 | 0.8926 | 0.9019   |
| 0.0336        | 16.0  | 7504 | 0.2433          | 90.0853 | 24.8401 | 90.0853 | 90.0853   | 2.2772  | 0.9048    | 0.8769 | 0.8896 | 0.9009   |
| 0.0336        | 17.0  | 7973 | 0.2363          | 89.8721 | 24.6269 | 89.8721 | 89.8721   | 2.274   | 0.6717    | 0.6563 | 0.6631 | 0.8987   |
| 0.0274        | 18.0  | 8442 | 0.2297          | 90.4051 | 25.2132 | 90.4051 | 90.4051   | 2.2814  | 0.904     | 0.8882 | 0.8953 | 0.9041   |
| 0.0298        | 19.0  | 8911 | 0.2275          | 89.7655 | 24.4136 | 89.7655 | 89.7655   | 2.2719  | 0.8886    | 0.8807 | 0.8832 | 0.8977   |
| 0.0261        | 20.0  | 9380 | 0.2260          | 89.7655 | 24.4136 | 89.7655 | 89.7655   | 2.2719  | 0.8856    | 0.8807 | 0.8817 | 0.8977   |


### Framework versions

- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1

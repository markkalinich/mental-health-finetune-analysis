---
library_name: transformers
language:
- en
license: apache-2.0
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline-combinedData
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted-baseline-combinedData

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/Combined_TAPT_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1153
- Accuracy: 0.7638
- Perplexity: 3.0506

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-06 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 100
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Perplexity |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:----------:|
| 1.3987        | 1.0   | 28   | 1.2896          | 0.7525   | 3.6312     |
| 1.3501        | 2.0   | 56   | 1.2327          | 0.7561   | 3.4304     |
| 1.3044        | 3.0   | 84   | 1.2182          | 0.7552   | 3.3810     |
| 1.2667        | 4.0   | 112  | 1.1852          | 0.7573   | 3.2712     |
| 1.2469        | 5.0   | 140  | 1.1747          | 0.7596   | 3.2372     |
| 1.2284        | 6.0   | 168  | 1.1602          | 0.7603   | 3.1906     |
| 1.1974        | 7.0   | 196  | 1.1517          | 0.7599   | 3.1635     |
| 1.1961        | 8.0   | 224  | 1.1234          | 0.7636   | 3.0752     |
| 1.1581        | 9.0   | 252  | 1.1104          | 0.7694   | 3.0356     |
| 1.1443        | 10.0  | 280  | 1.1184          | 0.7687   | 3.0600     |
| 1.1272        | 11.0  | 308  | 1.1149          | 0.7632   | 3.0494     |
| 1.1141        | 12.0  | 336  | 1.1268          | 0.7655   | 3.0858     |
| 1.114         | 13.0  | 364  | 1.1188          | 0.7634   | 3.0612     |
| 1.0733        | 14.0  | 392  | 1.0972          | 0.7661   | 2.9959     |
| 1.0756        | 15.0  | 420  | 1.1112          | 0.7665   | 3.0381     |
| 1.0767        | 16.0  | 448  | 1.1173          | 0.7616   | 3.0566     |
| 1.0561        | 17.0  | 476  | 1.0940          | 0.7678   | 2.9861     |
| 1.0528        | 18.0  | 504  | 1.0975          | 0.7640   | 2.9968     |
| 1.0363        | 19.0  | 532  | 1.0983          | 0.7658   | 2.9991     |
| 1.0247        | 20.0  | 560  | 1.0869          | 0.7684   | 2.9652     |
| 1.0185        | 21.0  | 588  | 1.1124          | 0.7635   | 3.0416     |
| 1.008         | 22.0  | 616  | 1.1290          | 0.7593   | 3.0926     |
| 0.9954        | 23.0  | 644  | 1.1142          | 0.7607   | 3.0472     |
| 1.0192        | 24.0  | 672  | 1.1127          | 0.7619   | 3.0425     |
| 1.0038        | 25.0  | 700  | 1.1115          | 0.7642   | 3.0389     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0

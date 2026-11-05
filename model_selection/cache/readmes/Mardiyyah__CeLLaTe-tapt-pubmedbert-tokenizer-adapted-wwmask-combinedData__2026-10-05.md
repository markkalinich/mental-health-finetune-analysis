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
- name: CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# CeLLaTe-tapt-pubmedbert-tokenizer-adapted-wwmask-combinedData

This model is a fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the Mardiyyah/Combined_TAPT_dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1730
- Accuracy: 0.7562
- Perplexity: 3.2318

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
| 1.4459        | 1.0   | 28   | 1.3302          | 0.7452   | 3.7816     |
| 1.3972        | 2.0   | 56   | 1.2823          | 0.7490   | 3.6048     |
| 1.3563        | 3.0   | 84   | 1.2437          | 0.7524   | 3.4685     |
| 1.3426        | 4.0   | 112  | 1.2253          | 0.7506   | 3.4050     |
| 1.3084        | 5.0   | 140  | 1.2217          | 0.7514   | 3.3930     |
| 1.281         | 6.0   | 168  | 1.2130          | 0.7539   | 3.3636     |
| 1.2606        | 7.0   | 196  | 1.2227          | 0.7525   | 3.3962     |
| 1.2452        | 8.0   | 224  | 1.2455          | 0.7485   | 3.4745     |
| 1.2291        | 9.0   | 252  | 1.2134          | 0.7532   | 3.3650     |
| 1.2136        | 10.0  | 280  | 1.1771          | 0.7565   | 3.2449     |
| 1.1945        | 11.0  | 308  | 1.1709          | 0.7544   | 3.2248     |
| 1.1856        | 12.0  | 336  | 1.2143          | 0.7526   | 3.3679     |
| 1.1779        | 13.0  | 364  | 1.1815          | 0.7524   | 3.2594     |
| 1.147         | 14.0  | 392  | 1.1803          | 0.7535   | 3.2553     |
| 1.1505        | 15.0  | 420  | 1.1819          | 0.7522   | 3.2607     |
| 1.1372        | 16.0  | 448  | 1.1592          | 0.7583   | 3.1875     |
| 1.1333        | 17.0  | 476  | 1.1801          | 0.7528   | 3.2546     |
| 1.1177        | 18.0  | 504  | 1.1837          | 0.7544   | 3.2666     |
| 1.1193        | 19.0  | 532  | 1.1513          | 0.7560   | 3.1623     |
| 1.1093        | 20.0  | 560  | 1.1969          | 0.7518   | 3.3099     |
| 1.0968        | 21.0  | 588  | 1.1824          | 0.7547   | 3.2623     |
| 1.0809        | 22.0  | 616  | 1.1841          | 0.7554   | 3.2676     |
| 1.0757        | 23.0  | 644  | 1.1764          | 0.7533   | 3.2426     |
| 1.0683        | 24.0  | 672  | 1.1730          | 0.7534   | 3.2318     |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0

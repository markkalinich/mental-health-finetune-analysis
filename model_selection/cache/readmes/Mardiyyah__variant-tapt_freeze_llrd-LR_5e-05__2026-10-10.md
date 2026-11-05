---
library_name: transformers
language:
- en
license: apache-2.0
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
tags:
- generated_from_trainer
- biomedical_nlp
- masked_language_modelling
metrics:
- accuracy
model-index:
- name: variant-tapt_freeze_llrd-LR_5e-05
  results: []
datasets:
- Mardiyyah/TAPT_Variant_FT
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# variant-tapt_freeze_llrd-LR_5e-05

This model is a masked language model (MLM) fine-tuned version of [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) on the [Mardiyyah/TAPT_Variant_FT dataset](https://huggingface.co/datasets/Mardiyyah/TAPT_Variant_FT).
It was trained to improve downstream NER performance for variant entity recognition in molecular biology by adapting the tokenizer to include rare biomedical and domain-specific terms that are critical for accurate entity tagging.

**Evaluation results on held-out set**:
- Loss: 1.3638
- Accuracy: 0.7251

## Model description

- Base model: BiomedBERT (microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext)

- Model type: Encoder-only transformer (BERT-style)

- Vocabulary adaptation:

   - Added rare biomedical tokens and NER-specific terms to prevent fragmentation of meaningful entities (e.g., Asp447SERK1)
   - Preserved base vocabulary to retain general biomedical knowledge

Fine-tuning: Task-Adaptive Pretraining (TAPT) on domain-specific unlabelled molecular biology text



## Intended uses & limitations

**Intended uses**:

- Pretraining for NER models in molecular biology, especially variant or mutant extraction

- Enhancing representation of rare or task-specific biomedical terms

- Could be used as a feature extractor or base model for further downstream biomedical NLP tasks (e.g., relation extraction, entity linking)

**Limitations**:

- MLM performance metrics may not directly correlate with downstream NER performance

- Fine-tuned primarily on molecular biology datasets; may not generalsze to other biomedical subdomains (e.g., clinical notes, proteomics)

- Tokenization strategy is domain-adapted; using this model outside of molecular biology may lead to unexpected tokenization splits or embeddings

## Training and evaluation data

- **Training data**: Unlabelled domain-specific molecular biology text from [Mardiyyah/TAPT_Variant_FT dataset](https://huggingface.co/datasets/Mardiyyah/TAPT_Variant_FT)

- **Evaluation data**: Held-out split of the same dataset

- **Preprocessing included**: cleaning, lowercasing, tokenization with extended vocabulary, grouping text into sequences of model-supported max length

## Training procedure

1. **Tokenizer adaptation**:

- Extended base tokenizer with task-specific and rare biomedical terms

- Ensured new embeddings were initialized to preserve semantic meaning using the average of subtoken embeddings

2. **Task-Adaptive Pretraining (TAPT)**:

- MLM objective on unlabelled domain-specific data

- Strategy: freeze lower layers + layer-wise learning rate decay (LLRD)

**Notes**: 
- Whole Word Masking was not used due to unstable loss spikes
- Adapted tokenizer (before TAPT) can be found [here](https://huggingface.co/Mardiyyah/biomedbert_tokenizer_extended_variants)
*Please note*: this initial extended tokenizer contains candidate tokens whose embeddings have not yet been trained. 
It is intended for TAPT and should not be used directly for downstream tasks, as embeddings are uninitialized and may not carry semantic meaning. 
After TAPT, the final tokenizer and model embeddings are suitable for downstream variant entity recognition.


**Hyperparameters**:

- Learning rate: 5e-5

- Batch size: 16

- Epochs: 20

- Optimizer: AdamW with ε=1e-6, weight decay=0.01

- Warmup ratio: 6%

- Gradient clipping: max_grad_norm=1.0

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 3407
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-06 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.06
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.6214        | 1.0   | 19   | 1.5767          | 0.7124   |
| 1.5605        | 2.0   | 38   | 1.5344          | 0.7151   |
| 1.5067        | 3.0   | 57   | 1.4533          | 0.7252   |
| 1.4634        | 4.0   | 76   | 1.4167          | 0.7215   |
| 1.4455        | 5.0   | 95   | 1.3822          | 0.7329   |
| 1.4099        | 6.0   | 114  | 1.3743          | 0.7282   |
| 1.3973        | 7.0   | 133  | 1.4204          | 0.7222   |
| 1.3562        | 8.0   | 152  | 1.3735          | 0.7346   |
| 1.3932        | 9.0   | 171  | 1.4068          | 0.7304   |
| 1.3475        | 10.0  | 190  | 1.3963          | 0.7315   |
| 1.3281        | 11.0  | 209  | 1.3168          | 0.7325   |
| 1.309         | 12.0  | 228  | 1.3306          | 0.7314   |
| 1.3291        | 13.0  | 247  | 1.3196          | 0.7382   |
| 1.2921        | 14.0  | 266  | 1.3361          | 0.7305   |
| 1.2992        | 15.0  | 285  | 1.2798          | 0.7351   |
| 1.2954        | 16.0  | 304  | 1.3871          | 0.7234   |
| 1.2907        | 17.0  | 323  | 1.3480          | 0.7351   |
| 1.2547        | 18.0  | 342  | 1.3165          | 0.7349   |
| 1.2802        | 19.0  | 361  | 1.3303          | 0.7313   |
| 1.2702        | 20.0  | 380  | 1.3541          | 0.7296   |


### Framework versions

- Transformers 4.48.2
- Pytorch 2.4.1+cu121
- Datasets 3.0.2
- Tokenizers 0.21.0
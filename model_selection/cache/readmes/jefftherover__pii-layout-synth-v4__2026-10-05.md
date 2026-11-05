---
library_name: transformers
license: apache-2.0
base_model: answerdotai/ModernBERT-base
tags:
- trackio
- trackio:https://huggingface.co/spaces/jefftherover/huggingface-static-349edf
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: pii-layout-synth-v4
  results: []
---
<a href="https://huggingface.co/spaces/jefftherover/huggingface-static-349edf" target="_blank"><img src="https://raw.githubusercontent.com/gradio-app/trackio/refs/heads/main/trackio/assets/badge.png" alt="Visualize in Trackio" title="Visualize in Trackio" style="height: 40px;"/></a>
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# pii-layout-synth-v4

This model is a fine-tuned version of [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0049
- Precision: 0.9906
- Recall: 0.9940
- F1: 0.9923
- Accuracy: 0.9986

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
- train_batch_size: 16
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Use OptimizerNames.ADAMW_TORCH_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 0.1
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:------:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.1117        | 0.2389 | 500  | 0.0483          | 0.8936    | 0.9383 | 0.9154 | 0.9859   |
| 0.0453        | 0.4778 | 1000 | 0.0176          | 0.9594    | 0.9769 | 0.9681 | 0.9947   |
| 0.0294        | 0.7167 | 1500 | 0.0111          | 0.9749    | 0.9877 | 0.9813 | 0.9968   |
| 0.0157        | 0.9556 | 2000 | 0.0089          | 0.9774    | 0.9886 | 0.9830 | 0.9970   |
| 0.0126        | 1.1945 | 2500 | 0.0072          | 0.9835    | 0.9896 | 0.9866 | 0.9978   |
| 0.0098        | 1.4333 | 3000 | 0.0064          | 0.9854    | 0.9920 | 0.9886 | 0.9980   |
| 0.0097        | 1.6722 | 3500 | 0.0053          | 0.9877    | 0.9936 | 0.9906 | 0.9983   |
| 0.0088        | 1.9111 | 4000 | 0.0056          | 0.9868    | 0.9916 | 0.9892 | 0.9982   |
| 0.0057        | 2.1500 | 4500 | 0.0057          | 0.9882    | 0.9921 | 0.9901 | 0.9983   |
| 0.0049        | 2.3889 | 5000 | 0.0055          | 0.9887    | 0.9936 | 0.9911 | 0.9984   |
| 0.0057        | 2.6278 | 5500 | 0.0052          | 0.9898    | 0.9946 | 0.9922 | 0.9985   |
| 0.0050        | 2.8667 | 6000 | 0.0052          | 0.9888    | 0.9932 | 0.9910 | 0.9984   |
| 0.0018        | 3.1056 | 6500 | 0.0051          | 0.9910    | 0.9946 | 0.9928 | 0.9986   |
| 0.0025        | 3.3445 | 7000 | 0.0051          | 0.9903    | 0.9950 | 0.9927 | 0.9986   |
| 0.0018        | 3.5834 | 7500 | 0.0053          | 0.9912    | 0.9939 | 0.9925 | 0.9986   |
| 0.0020        | 3.8223 | 8000 | 0.0049          | 0.9906    | 0.9940 | 0.9923 | 0.9986   |


### Framework versions

- Transformers 5.11.0
- Pytorch 2.12.0+cu130
- Datasets 5.0.0
- Tokenizers 0.22.2

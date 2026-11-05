---
library_name: transformers
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- emotion-classification
- text-classification
- distilbert
datasets:
- dair-ai/emotion
language:
- en
metrics:
- accuracy
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an Emotion Dataset.

## Model description

This model fine-tunes DistilBERT for emotion classification. It can detect emotions in language and then classify them into: sadness, joy, love, anger, fear, surprise.

## Intended uses & limitations

Used to explain the inner emotions of simple sentences. This model may lack contextual reasoning ability and cannot understand connecting words such as transitions.

## Training and evaluation data

- Training Dataset: dair-ai/emotion (16,000 examples)
- Validation set: 2,000 examples
- Test set: 2,000 examples
- Validation Accuracy:
  - epoch1:0.9065
  - epoch2:0.9345
  - epoch3:0.93
  - epoch4:0.942
  - epoch5:0.94
- Test Accuracy: 0.942
- Training Time: 2:02:44

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 256
- eval_batch_size: 256
- seed: 42
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- num_epochs: 5

### Framework versions

- Transformers 4.46.2
- Pytorch 2.5.1+cpu
- Datasets 3.1.0
- Tokenizers 0.20.3
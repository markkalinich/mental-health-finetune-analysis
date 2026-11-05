---
license: mit
datasets:
- databoyface/ome-src-v4.2
language:
- en
metrics:
- accuracy
base_model:
- distilbert/distilroberta-base
pipeline_tag: text-classification
library_name: transformers
tags:
- emotion
---

# Orthogonal Model of Emotions (OME)

This model is a fine-tuned version of [distilbert/distilroberta-base](https://huggingface.co/distilbert/distilroberta-base) trained on the OME v4.2 dataset.

It achieves the following results on the evaluation set:
- Loss: 0.0046
- Accuracy: 0.9966

## Model description

This latest variation of the OME is a text classifier based on distilroberta and fine tuned with 47 categories for classifying emotion in English language examples from a curated dataset deriving emotional clusters using dimensions of Subjectivity, Relativity, and Generativity. Additional dimensions of Clarity and Acceptance were used to map seven population clusters of ontological experiences categorized as Trust or Love, Happiness or Pleasure, Sadness or Trauma, Anger or Disgust, Fear or Anxiety, Guilt or Shame, and Jealousy or Envy.

## Intended uses & limitations

[*Clusters listed in brackets organize the classification, but aren't returned*]

- [*Anger or Disgust*]
  - anger-maybe
  - anger-partial
  - anger-quite
  - anger-really
  - anger-very
  - anger-xtreme
- [*Fear or Anxiety*]
  - fear-maybe
  - fear-partial
  - fear-quite
  - fear-really
  - fear-very
  - fear-xtreme
- [*Guilt or Shame*]
  - guilt-maybe
  - guilt-partial
  - guilt-quite
  - guilt-really
  - guilt-very
  - guilt-xtreme
- [*Happiness or Pleasure*]
  - happiness-maybe
  - happiness-partial
  - happiness-quite
  - happiness-really
  - happiness-very
  - happiness-xtreme
- [*Jealousy or Envy*]
  - jealousy-maybe
  - jealousy-partial
  - jealousy-quite
  - jealousy-really
  - jealousy-very
  - jealousy-xtreme
- [*Neutral or Edge Cases*]
  - more-negative-than-positive
  - more-positive-than-negative
  - negative
  - neutral
  - positive
- [*Sadness or Trauma*]
  - sadness-maybe
  - sadness-partial
  - sadness-quite
  - sadness-really
  - sadness-very
  - sadness-xtreme
- [*Trust or Love*]
  - trust-maybe
  - trust-partial
  - trust-quite
  - trust-really
  - trust-very
  - trust-xtreme

## Training and evaluation data

### Training Script for Transformers and PyTorch

		python run_classification.py \
          --model_name_or_path  distilbert/distilroberta-base \
          --dataset_name databoyface/ome-src-v4.2 \
          --shuffle_train_dataset true \
          --metric_name accuracy \
          --text_column_name text \
          --text_column_delimiter "\n" \
          --label_column_name label \
          --do_train \
          --do_eval \
          --do_predict \
          --max_seq_length 256 \
          --per_device_train_batch_size 64 \
          --learning_rate 1e-4 \
          --num_train_epochs 30 \
          --output_dir ./OME-RoBERTa-latest/

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning\_rate: 0.0001
- train\_batch\_size: 64
- eval\_batch\_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW\_TORCH\_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer\_args=No additional optimizer arguments
- lr\_scheduler\_type: linear
- num\_epochs: 30.0

### Training results

      ***** train metrics *****
    epoch                    =       30.0
    total_flos               = 16316413GF
    train_loss               =     0.1662
    train_runtime            = 6:23:30.42
    train_samples            =       8810
    train_samples_per_second =     11.486
    train_steps_per_second   =       0.18

      ***** eval metrics *****
    "epoch": 30.0,
    "eval_accuracy": 0.9966101694915255,
    "eval_loss": 0.004637924954295158,
    "eval_runtime": 32.3697,
    "eval_samples": 1475,
    "eval_samples_per_second": 45.567,
    "eval_steps_per_second": 5.715

### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.1
- Datasets 4.4.1
- Tokenizers 0.22.1

## Coming Soon!

Version 5!
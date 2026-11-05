---
license: mit
datasets:
- databoyface/ome-src-v5
language:
- en
metrics:
- accuracy
base_model:
- google-bert/bert-base-uncased
library_name: transformers
tags:
- emotion
---
# The Orthogonal Model of Emotions: OMEv5

This model is a fine-tuned version of [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) on the [OME v5 dataset](https://huggingface.co/datasets/databoyface/ome-src-v5).

It achieves the following results on the evaluation set:
- Loss: 0.0860
- Accuracy: 0.9863

## Model description

This latest variation of the OME is a text classifier based on BERT and fine-tuned with 26 categories using Transfer Learning for classifying emotion in English language examples in a curated dataset deriving emotional clusters using dimensions of Subjectivity, Relativity, and Generativity. Additional dimensions of Clarity, now simpler with three levels, and Compassion, using rate of change to linearize the data, were used to map seven population clusters of ontological experiences categorized as Trust or Love, Happiness or Pleasure, Jealousy or Envy, Shame or Guilt, Anger or Disgust, Fear or Anxiety, and Sadness or Trauma. Edge cases, neutrality, and simple sentiments, such as positive and negative, are also used as null cases in classification theorized by OME.

## Intended uses & limitations

[*Clusters listed in brackets (alphabetically) organize the dataset, but aren't labels*]

- [*Anger or Disgust*]
  - anger-and-disgust-clear
  - anger-and-disgust-conspicuous
  - anger-and-disgust-presumed
- [*Fear or Anxiety*]
  - fear-and-anxiety-clear
  - fear-and-anxiety-conspicuous
  - fear-and-anxiety-presumed
- [*Guilt or Shame*]
  - guilt-and-shame-clear
  - guilt-and-shame-conspicuous
  - guilt-and-shame-presumed
- [*Happiness or Pleasure*]
  - happiness-and-pleasure-clear
  - happiness-and-pleasure-conspicuous
  - happiness-and-pleasure-presumed
- [*Jealousy or Envy*]
  - jealousy-and-envy-clear
  - jealousy-and-envy-conspicuous
  - jealousy-and-envy-presumed
- [*Neutral or Edge Cases*]
  - negative-conspicuous
  - negative-presumed
  - neutral-presumed
  - positive-conspicuous
  - positive-presumed
- [*Sadness or Trauma*]
  - sadness-and-trauma-clear
  - sadness-and-trauma-conspicuous
  - sadness-and-trauma-presumed
- [*Trust or Love*]
  - trust-and-love-clear
  - trust-and-love-conspicuous
  - trust-and-love-presumed

## Training and evaluation data

Check out the [OME v5 dataset](https://huggingface.co/datasets/databoyface/ome-src-v5).

### Training Script for Transformers and PyTorch

		python run_classification.py \
          --model_name_or_path  google-bert/bert-base-uncased \
          --dataset_name databoyface/ome-src-v5 \
          --shuffle_train_dataset true \
          --metric_name accuracy \
          --text_column_name text \
          --text_column_delimiter "\n" \
          --label_column_name label \
          --do_train \
          --do_eval \
          --do_predict \
          --max_seq_length 256 \
          --per_device_train_batch_size 32 \
          --learning_rate 1e-4 \
          --num_train_epochs 30 \
          --output_dir ./OME-BERT/

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:

- learning\_rate: 0.0001
- train\_batch\_size: 32
- eval\_batch\_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW\_TORCH\_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer\_args=No additional optimizer arguments
- lr\_scheduler\_type: linear
- num\_epochs: 30.0

### Training results

    ***** train metrics *****
    {
        "epoch": 30.0,
        "total_flos": 3.65934759422976e+16,
        "train_loss": 0.08956794562696041,
        "train_runtime": 37265.2283,
        "train_samples": 9270,
        "train_samples_per_second": 7.463,
        "train_steps_per_second": 0.233
    }
    
    ***** eval metrics *****
    {
        "epoch": 30.0,
        "eval_accuracy": 0.9862892525431225,
        "eval_loss": 0.08600278198719025,
        "eval_runtime": 98.4762,
        "eval_samples": 2261,
        "eval_samples_per_second": 22.96,
        "eval_steps_per_second": 2.874
    }

### Framework versions

- Transformers 4.57.3
- Pytorch 2.9.1
- Datasets 4.4.2
- Tokenizers 0.22.1

## Coming Soon!

New demonstrations, applications, and evaluations!

### Visualization

Brand new (so new, I hope it works), here's what HFViewer has to say about OME!

<a href="https://hfviewer.com/databoyface/bert-base-uncased-ome-v5?utm_source=huggingface&amp;utm_medium=embedded_model_card&amp;utm_campaign=databoyface__bert-base-uncased-ome-v5_card" target="_blank" rel="noopener">
  <img
    src="https://hfviewer.com/api/card.svg?source=databoyface%2Fbert-base-uncased-ome-v5&amp;v=20260505graphcard"
    alt="Open databoyface/bert-base-uncased-ome-v5 in hfviewer"
    width="100%"
  />
</a>


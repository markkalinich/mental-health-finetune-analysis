---
library_name: transformers
license: mit
datasets:
- databoyface/ome-src-v5.2
base_model: distilbert/distilroberta-base
pipeline_tag: text-classification
tags:
- emotion
metrics:
- accuracy
model-index:
- name: OME
  results: []
---


# Orthogonal Model of Emotions (OME)

This model is a fine-tuned version of [distilbert/distilroberta-base](https://huggingface.co/distilbert/distilroberta-base) on the OME v5.2 dataset.

It achieves the following results on the evaluation set:

- Loss: 0.1073
- Accuracy: 0.9803

## Model description

This latest variation of the OME is a text classifier based on `distilroberta` and fine-tuned with 26 categories using Transfer Learning for classifying emotion in English language examples in a curated dataset deriving emotional clusters using dimensions of Subjectivity, Relativity, and Generativity. Additional dimensions of Clarity, now simpler with three levels, and Compassion, using rate of change to linearize the data, were used to map seven population clusters of ontological experiences categorized as Trust or Love, Happiness or Pleasure, Jealousy or Envy, Shame or Guilt, Anger or Disgust, Fear or Anxiety, and Sadness or Trauma. Edge cases, neutrality, and simple sentiments, such as positive and negative, are also used as null cases in classification theorized by OME.


## Intended uses & limitations

The Orthogonal Model of Emotions (OME) was crafted and built with the purpose of representing the totality of emotional expression as represented in English. OME is synthetic compassion, a context for empathy based on predicting the closest possible match based on natural language processing and statistical validation.

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
  - neutral-clear
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

Check out the [OME v5 dataset](https://huggingface.co/datasets/databoyface/ome-src-v5.2).

## Training procedure

### Training Script for Transformers and PyTorch

    python run_classification.py \
      --model_name_or_path  distilbert/distilroberta-base \
  	--dataset_name databoyface/ome-src-v5.2 \
      --shuffle_train_dataset true \
      --metric_name accuracy \
      --text_column_name text \
      --label_column_name label \
      --do_train \
      --do_eval \
      --do_predict \
      --max_seq_length 256 \
      --per_device_train_batch_size 64 \
      --learning_rate 2e-4 \
      --num_train_epochs 15 \
      --output_dir ./OME/

### Training hyperparameters

The following hyperparameters were used during training:
- learning\_rate: 0.0002
- train\_batch\_size: 64
- eval\_batch\_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW\_TORCH\_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer\_args=No additional optimizer arguments
- lr\_scheduler\_type: linear
- num_epochs: 15.0

### Training results

    ***** train metrics *****
    {
      epoch                    =       15.0
	  total_flos               =  8774427GF
	  train_loss               =     0.2544
	  train_runtime            = 2:45:55.78
	  train_samples            =       9479
	  train_samples_per_second =     14.282
	  train_steps_per_second   =      0.224
  	}
  	
  	***** eval metrics *****
    {
    	"epoch": 15.0,
		"eval_accuracy": 0.980310012568077,
		"eval_loss": 0.10729153454303741,
		"eval_runtime": 48.9116,
		"eval_samples": 2387,
		"eval_samples_per_second": 48.802,
		"eval_steps_per_second": 6.113
	}

### Framework versions

- Transformers 5.8.0
- Pytorch 2.11.0
- Datasets 4.8.5
- Tokenizers 0.22.2

## Visualizer from HF Viewer

<a href="https://hfviewer.com/databoyface/distilroberta-base-ome-v5.2" target="_blank" rel="noopener">
  <img
    src="https://hfviewer.com/assets/hf_cards/databoyface__distilroberta-base-ome-v5.2__level1.svg?granularity=1&amp;v=20260516-level-static-cards&amp;source_page=model-card-embed&amp;community_showcase_opt_in=1"
    alt="Architecture graph for databoyface/distilroberta-base-ome-v5.2. Open in hfviewer"
    width="100%"
  />
</a>
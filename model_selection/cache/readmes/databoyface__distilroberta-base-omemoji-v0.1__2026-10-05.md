---
license: mit
datasets:
- databoyface/omemoji-src-v0.1
language:
- en
metrics:
- accuracy
base_model:
- distilbert/distilroberta-base
library_name: transformers
tags:
- emotion
---

# The Orthogonal Model of Emoji (OMEmoji) 

Around here, better known as: distilroberta-base-omemoji-v0.1! *Note well, this isn't a text-replacement emoji prediction tool.*

This model is a fine-tuned version of [distilbert/distilroberta-base](https://huggingface.co/distilbert/distilroberta-base) on the OMEmoji dataset.

It achieves the following results on the evaluation set:

- Loss: 0.1496
- Accuracy: 0.9549

## Model description

This latest variant of the OME is a text classifier based on `distilroberta` and fine-tuned with 10 categories using Transfer Learning for classifying emotion in English language examples in a curated dataset deriving emotional clusters using dimensions of Subjectivity, Relativity, and Generativity. An additional dimension of Clarity was removed, while still Compassion, using rate of change to linearize the data, was used to map seven population clusters of ontological experiences categorized and represented by emojis as Trust or Love, Happiness or Pleasure, Jealousy or Envy, Shame or Guilt, Anger or Disgust, Fear or Anxiety, and Sadness or Trauma. Edge cases, neutrality, and simple sentiments, such as positive and negative, are also used as null cases in classification theorized by OME.

## Intended uses & limitations

While the Orthogonal Model of Emotions (OME) was crafted and built with the purpose of representing the totality of emotional expression as represented in English, this is beta software, so use at your own risk!

### Category Labels

| **Description** | **Label** |
| --- | --- |
| Trust or Love	| 🥰 |
| Happiness or Pleasure	| 🤩 |
| Positive	| 🙂 |
| Neutral	| 😐 |
| Negative	| 🙁 |
| Jealousy or Envy	| 😒 |
| Shame or Guilt	| 😦 |
| Anger or Disgust	| 😠 |
| Fear or Anxiety	| 😨 |
| Sadness or Trauma	| 😭 |

## Training and evaluation data

Check out the [OMEmoji dataset](https://huggingface.co/datasets/databoyface/omemoji-src-v0.1).

## Training procedure

Initial training used the script from John6666 that I've [archived at GitHub](https://github.com/accdataboy/orthogonal-model-of-emojis).

### Script for Transformers and Pytorch

	  python run_classification.py \
		--model_name_or_path distilbert/distilroberta-base \
		--dataset_name databoyface/omemoji-src-v0.1 \
		--shuffle_train_dataset true \
		--metric_name accuracy \
		--text_column_name text \
		--label_column_name label \
		--do_train \
		--do_eval \
		--do_predict \
		--max_seq_length 256 \
		--per_device_train_batch_size 64 \
		--learning_rate 1e-5 \
		--num_train_epochs 15 \
		--output_dir ./distilroberta-base-omemoji-v0.1/

### Training hyperparameters

The following hyperparameters were used during training:
- learning\_rate: 1e-05
- train\_batch\_size: 64
- eval\_batch\_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW\_TORCH\_FUSED with betas=(0.9,0.999) and epsilon=1e-08 and optimizer\_args=No additional optimizer arguments
- lr\_scheduler\_type: linear
- num\_epochs: 15.0

### Training results

	  ***** train metrics *****
	  epoch                    =       15.0
	  total_flos               =  8835777GF
	  train_loss               =     0.5051
	  train_runtime            = 3:11:42.38
	  train_samples            =       9548
	  train_samples_per_second =     12.451
	  train_steps_per_second   =      0.196

      ***** eval metrics *****
      {
          "epoch": 15.0,
          "eval_accuracy": 0.9549248747913188,
          "eval_loss": 0.14957648515701294,
          "eval_runtime": 60.9791,
          "eval_samples": 2396,
          "eval_samples_per_second": 39.292,
          "eval_steps_per_second": 4.92
      }

### Framework versions

- Transformers 5.13.1
- Pytorch 2.13.0
- Datasets 5.0.0
- Tokenizers 0.22.2

---
license: mit
datasets:
- databoyface/ome-src-v4.2
language:
- en
base_model:
- distilbert/distilbert-base-multilingual-cased
pipeline_tag: text-classification
library_name: transformers
tags:
- emotion
---

# Orthogonal Model of Emotions (Baseline)

The OME is a text classifier based on `distilibert/distilbert-base-cased` and fine tuned with 47 categories for classifying emotion in English language examples from a curated dataset deriving emotional clusters using dimensions of Subjectivity, Relativity, and Generativity. Additional dimensions of Clarity and Acceptance were used to map seven population clusters of ontological experiences categorized as Trust or Love, Happiness or Pleasure, Sadness or Trauma, Anger or Disgust, Fear or Anxiety, Guilt or Shame, and Jealousy or Envy.

## Author

C.J. Pitchford

## Published

17 November 2025

## Categories

[*Clusters listed in brackets (alphabetically) organize the classification, but aren't returned*]

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


## Training Script for Transformers and PyTorch

		python run_classification.py \
			--model_name_or_path  distilibert/distilbert-base-cased \
			--train_file "/Users/chris/Documents/ml/transformers/data/ome-4-2-train.csv" \
			--validation_file "/Users/chris/Documents/ml/transformers/data/ome-4-2-test.csv" \
			--shuffle_train_dataset \
			--metric_name accuracy \
			--text_column_name text \
			--text_column_delimiter "\n" \
			--label_column_name label \
			--do_train \
			--do_eval \
			--max_seq_length 256 \
			--per_device_train_batch_size 32 \
			--learning_rate 2e-4 \
			--num_train_epochs 20 \
			--output_dir ./model/

## Training and Evaluation Results

     ** train metrics **
    epoch                    =       20.0
    total_flos               = 10906006GF
    train_loss               =     0.1524
    train_runtime            = 3:24:17.27
    train_samples            =       8833
    train_samples_per_second =     14.413
    train_steps_per_second   =      0.452

     ** eval metrics **
    "epoch": 20.0,
    "eval_accuracy": 0.9952542372881356,
    "eval_loss": 0.004642655607312918,
    "eval_runtime": 32.679,
    "eval_samples": 1475,
    "eval_samples_per_second": 45.136,
    "eval_steps_per_second": 5.661

## Citation

    @misc{christopher_pitchford_2025,
    	author       = { Christopher Pitchford },
    	title        = { distilbert-base-cased-ome-v4.2 (Revision bea3c7e) },
    	year         = 2025,
    	url          = { https://huggingface.co/databoyface/distilbert-base-cased-ome-v4.2 },
    	doi          = { 10.57967/hf/7018 },
    	publisher    = { Hugging Face }
    }

## Coming Soon

Version 5!
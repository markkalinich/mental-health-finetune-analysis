---
library_name: transformers
license: mit
base_model: xlm-roberta-base
tags:
- generated_from_trainer
- emotion-classification
- midwest-emo
- math-rock
- domain-adaptation
- hybrid-corpus
metrics:
- accuracy
- f1
datasets:
- anggars/mbti-emotion
model-index:
- name: xlm-emotion
  results:
  - task:
      type: text-classification
      name: Text Classification
    dataset:
      name: anggars/mbti-emotion
      type: anggars/mbti-emotion
    metrics:
    - type: accuracy
      value: 0.9546
      name: Accuracy
    - type: f1
      value: 0.9544
      name: F1 Macro
language:
  - en
  - id
  - ja
  - ko
  - es
  - fr
  - de
  - zh
  - pt
  - ru
  - it
---

# XLM-RoBERTa Emotion (Domain-Adapted for Midwest Emo/Math Rock)

This model is a fine-tuned version of [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) for **Emotion Classification** (28 labels based on the GoEmotions taxonomy). It has been architecturally recalibrated using a **Hybrid Corpus** to recognize complex emotional nuances, poetic hyperboles, and depressive metaphors specifically found in Midwest Emo and Math Rock lyrical styles.

## Model Description

- **Model Type:** XLM-RoBERTa Base (Sequence Classification Head with 28 Nodes)
- **Labels:** 28 Emotion Categories (e.g., sadness, grief, admiration, anger, joy)
- **Dataset:** `anggars/mbti-emotion` (Hybrid Corpus: 120,060 total rows. Stratified split: 96,048 train / 24,012 eval)
- **Language:** English & Indonesian (Multilingual)
- **Training Environment:** Kaggle Compute (Dual NVIDIA Tesla T4 GPU, fp16 Mixed Precision)

## Architectural Innovations: Overcoming Domain Shift

Initial iterations of this model were trained purely on synthetic narrative data, which caused severe **Domain Shift** when predicting real-world music lyrics. To mitigate this blind spot, a **Hybrid Corpus Integration** was executed. The model was forced to adapt to organic lyrics scraped directly from Genius.com and augmented with high-quality, balanced synthetic data generated via Gemma-2B-IT. 

The integration process successfully recalibrated the latent space, forcing the model to understand poetic contexts and lyrical structures. The aggressive weight decay (0.05) ensures the model does not overconfidently hallucinate on ambiguous lyrics, resulting in highly generalized, real-world zero-shot capabilities.

## Training Results

The following results were achieved on the evaluation set (24,012 rows) during the 3-epoch training process:

| Epoch | Training Loss | Validation Loss | Accuracy | F1 Macro |
|:-----:|:-------------:|:---------------:|:--------:|:--------:|
| 1.0   | 0.2403        | 0.2086          | 0.9347   | 0.9339   |
| 2.0   | 0.1403        | 0.1837          | 0.9480   | 0.9475   |
| 3.0   | 0.1005        | 0.1888          | 0.9546   | 0.9544   |

## Intended Uses & Limitations

This model is explicitly designed for the backend NLP engine of music analytics dashboards, predicting emotions directly from raw song lyrics.
**Limitations:** Because the model has been highly adapted to read poetic, dramatic, and emotionally dense lyrical structures, its performance may degrade if deployed on standard formal documents, legal text, or casual short-form social media chats.

## Training Procedure

### Training Hyperparameters

- **learning_rate:** 1.5e-05
- **train_batch_size:** 16
- **eval_batch_size:** 16
- **seed:** 42
- **weight_decay:** 0.05
- **optimizer:** AdamW with betas=(0.9,0.999) and epsilon=1e-08
- **lr_scheduler_type:** linear
- **num_epochs:** 3
- **mixed_precision_training:** Native AMP (fp16)
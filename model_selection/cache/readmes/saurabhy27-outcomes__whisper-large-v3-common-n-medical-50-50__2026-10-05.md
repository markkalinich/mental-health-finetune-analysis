---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-large-v3
tags:
- whisper-event
- generated_from_trainer
datasets:
- OUTCOMESAI/medical_n_common_speech_corpus_50_50
metrics:
- wer
model-index:
- name: Whisper Large V3 Common n Medical 50 50
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: OUTCOMESAI/medical_n_common_speech_corpus_50_50 en
      type: OUTCOMESAI/medical_n_common_speech_corpus_50_50
    metrics:
    - name: Wer
      type: wer
      value: 5.218643517767322
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Large V3 Common n Medical 50 50

This model is a fine-tuned version of [openai/whisper-large-v3](https://huggingface.co/openai/whisper-large-v3) on the OUTCOMESAI/medical_n_common_speech_corpus_50_50 en dataset.
It achieves the following results on the evaluation set:
- Loss: 0.3196
- Wer: 5.2186

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-07
- train_batch_size: 64
- eval_batch_size: 32
- seed: 42
- distributed_type: multi-GPU
- optimizer: Use adamw_torch with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- training_steps: 5000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 5.126         | 0.0969 | 250  | 0.3694          | 5.6601 |
| 4.367         | 0.1938 | 500  | 0.3586          | 5.8156 |
| 4.1514        | 0.2907 | 750  | 0.3511          | 5.8839 |
| 3.962         | 0.3876 | 1000 | 0.3450          | 5.7805 |
| 3.9038        | 0.4845 | 1250 | 0.3403          | 6.1746 |
| 3.8313        | 0.5814 | 1500 | 0.3359          | 5.9738 |
| 3.7778        | 0.6783 | 1750 | 0.3333          | 5.9218 |
| 3.7421        | 0.7752 | 2000 | 0.3306          | 6.1327 |
| 3.7367        | 0.8721 | 2250 | 0.3281          | 5.6561 |
| 3.6878        | 0.9690 | 2500 | 0.3257          | 5.5154 |
| 3.6769        | 1.0659 | 2750 | 0.3242          | 5.4803 |
| 3.6508        | 1.1628 | 3000 | 0.3235          | 5.4634 |
| 3.6292        | 1.2597 | 3250 | 0.3220          | 5.3512 |
| 3.6179        | 1.3566 | 3500 | 0.3210          | 5.2254 |
| 3.6032        | 1.4535 | 3750 | 0.3206          | 5.2207 |
| 3.5922        | 1.5504 | 4000 | 0.3201          | 5.3038 |
| 3.5743        | 1.6473 | 4250 | 0.3198          | 5.2633 |
| 3.5882        | 1.7442 | 4500 | 0.3198          | 5.2254 |
| 3.6021        | 1.8411 | 4750 | 0.3196          | 5.2186 |
| 3.5865        | 1.9380 | 5000 | 0.3193          | 5.2213 |


### Framework versions

- Transformers 4.48.0.dev0
- Pytorch 2.1.0+cu118
- Datasets 3.2.1.dev0
- Tokenizers 0.21.0

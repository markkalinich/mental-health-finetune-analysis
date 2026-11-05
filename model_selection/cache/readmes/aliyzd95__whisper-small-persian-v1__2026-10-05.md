---
library_name: transformers
license: apache-2.0
language:
  - fa
base_model: openai/whisper-small
tags:
  - generated_from_trainer
  - automatic-speech-recognition
  - whisper
  - persian
  - speech
  - ASR
  - common voice
  - emotion-recognition
datasets:
  - aliyzd95/common_voice_21_0_fa
metrics:
  - wer
model-index:
- name: Whisper Small Pesrian V1
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 21.0
      type: aliyzd95/common_voice_21_0_fa
      config: fa
      split: None
      args: 'split: test'
    metrics:
    - name: Wer
      type: wer
      value: 31.930087051142547
---

# Whisper Small Persian

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the Common Voice 21.0 dataset.
It achieves the following results on the evaluation set:

- Loss: 0.3323
- Wer: 31.9300

## 🧠 Model Details

- Base model: `openai/whisper-small`
- Fine-tuned on:
  - Common Voice 21 (Persian subset)
- Language: Persian (fa)

## 🧪 Evaluation

| Metric | Value |
|--------|-------|
| WER    | `31.93%`


## 📦 Usage

```python
from transformers import pipeline

pipe = pipeline("automatic-speech-recognition", model="aliyzd95/whisper-small-persian-v1")

result = pipe("your-audio.wav")
print(result["text"])
```

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 4e-05
- train_batch_size: 8
- gradient_accumulation_steps: 2
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.53.0.dev0
- Pytorch 2.7.1+cu128
- Datasets 3.6.0
- Tokenizers 0.21.1
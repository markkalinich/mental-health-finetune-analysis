---
library_name: transformers
language:
- en
license: mit
base_model: openai/whisper-small
tags:
- generated_from_trainer
metrics:
- wer
model-index:
- name: Medical Speech Transcription Whisper Small Fine Tuned
  results: []
---


# Whisper Small Fine Tuned

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the 500 samples of doctor-patient conversations.
It achieves the following results on the evaluation set:
- Loss: 0.4537
- Wer: 10.6667



## Intended uses & limitations

Model was trained for Educational Purposes


## How to Use

You can use this fine-tuned Whisper model for transcribing short medical conversations using Hugging Face's `transformers` and `datasets` libraries.

```python
from transformers import pipeline

# Load the fine-tuned model from Hugging Face
pipe = pipeline(
    task="automatic-speech-recognition",
    model="Bhaveen/Medical-Speech-Transcription-Whisper-Small-Fine-Tuned",
    device=0  # set to -1 for CPU, or 0 for GPU if available
)

# Run inference on an audio file
result = pipe("path_to_audio.wav")  # Replace with your actual audio file path
print(result["text"])
```

### Requirements

Install dependencies if you haven't already:

```bash
pip install transformers datasets torchaudio
```


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 200
- num_epochs: 8
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer     |
|:-------------:|:-----:|:----:|:---------------:|:-------:|
| 0.0384        | 1.0   | 25   | 0.4705          | 12.2222 |
| 0.0375        | 2.0   | 50   | 0.4689          | 12.0    |
| 0.0332        | 3.0   | 75   | 0.4666          | 11.0370 |
| 0.0293        | 4.0   | 100  | 0.4636          | 11.1111 |
| 0.0242        | 5.0   | 125  | 0.4612          | 11.0370 |
| 0.0197        | 6.0   | 150  | 0.4586          | 10.9630 |
| 0.0152        | 7.0   | 175  | 0.4555          | 10.7407 |
| 0.0116        | 8.0   | 200  | 0.4537          | 10.6667 |


### Framework versions

- Transformers 4.47.1
- Pytorch 2.5.1+cu124
- Datasets 3.2.0
- Tokenizers 0.21.0

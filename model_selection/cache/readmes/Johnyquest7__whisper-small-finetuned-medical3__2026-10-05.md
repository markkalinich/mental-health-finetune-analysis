---
library_name: transformers
license: apache-2.0
base_model: openai/whisper-small
tags:
- generated_from_trainer
datasets:
- audiofolder
metrics:
- wer
model-index:
- name: whisper-small-finetuned-medical3
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: audiofolder
      type: audiofolder
      config: default
      split: None
      args: default
    metrics:
    - name: Wer
      type: wer
      value: 3.125
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# whisper-small-finetuned-medical3

This model is a fine-tuned version of [openai/whisper-small](https://huggingface.co/openai/whisper-small) on the audiofolder dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0671
- Wer: 3.125


### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Use OptimizerNames.ADAMW_TORCH with betas=(0.9,0.999) and epsilon=1e-08 and optimizer_args=No additional optimizer arguments
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 80
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 0.4797        | 0.8696 | 10   | 0.4806          | 5.8239 |
| 0.4503        | 1.6957 | 20   | 0.4695          | 5.6818 |
| 0.4076        | 2.5217 | 30   | 0.4219          | 5.5398 |
| 0.3637        | 3.3478 | 40   | 0.3402          | 4.8295 |
| 0.2583        | 4.1739 | 50   | 0.1697          | 4.1193 |
| 0.1121        | 5.0    | 60   | 0.0978          | 3.8352 |
| 0.0751        | 5.8696 | 70   | 0.0825          | 3.8352 |
| 0.0464        | 6.6957 | 80   | 0.0671          | 3.125  |


### Framework versions

- Transformers 4.51.3
- Pytorch 2.7.0+cu126
- Datasets 3.5.1
- Tokenizers 0.21.1

## Usage

```python
from transformers import pipeline
import gradio as gr

# Load the fine-tuned Whisper model for medical speech recognition
pipe = pipeline(model="Johnyquest7/whisper-small-finetuned-medical3", return_timestamps=True)

# Define transcription function
def transcribe(audio):
    text = pipe(audio)["text"]
    return text

# Create a Gradio interface
iface = gr.Interface(
    fn=transcribe,
    inputs=gr.Audio(sources=["upload", "microphone"], type="filepath"),
    outputs="text",
    title="Whisper Small Medical",
    description="Demo for medical speech recognition using a fine-tuned Whisper small model."
)

# Launch the interface
iface.launch()
```


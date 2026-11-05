---
language:
- th
license: apache-2.0
library_name: transformers
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_13_0
- google/fleurs
metrics:
- wer
base_model: openai/whisper-small
model-index:
- name: Whisper Small Thai Combined V4 - biodatlab
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: mozilla-foundation/common_voice_13_0 th
      type: mozilla-foundation/common_voice_13_0
      config: th
      split: test
      args: th
    metrics:
    - type: wer
      value: 13.14
      name: Wer
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# Whisper Small (Thai): Combined V4

This model is a fine-tuned version of [openai/whisper-medium](https://huggingface.co/openai/whisper-small) on augmented versions of the mozilla-foundation/common_voice_13_0 th, google/fleurs, and curated datasets.
It achieves the following results on the common-voice-13 test set:
- WER: 13.14 (with Deepcut Tokenizer)

## Model description

Use the model with huggingface's `transformers` as follows:

```py
from transformers import pipeline

MODEL_NAME = "biodatlab/whisper-th-small-combined"  # specify the model name
lang = "th"  # change to Thai langauge

device = 0 if torch.cuda.is_available() else "cpu"

pipe = pipeline(
    task="automatic-speech-recognition",
    model=MODEL_NAME,
    chunk_length_s=30,
    device=device,
)
pipe.model.config.forced_decoder_ids = pipe.tokenizer.get_decoder_prompt_ids(
  language=lang,
  task="transcribe"
)
text = pipe("audio.mp3")["text"] # give audio mp3 and transcribe text
```


## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: AdamW with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- training_steps: 10000
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.37.2
- Pytorch 2.1.0
- Datasets 2.16.1
- Tokenizers 0.15.1

## Citation

Cite using Bibtex:

```
@misc {thonburian_whisper_med,
    author       = { Atirut Boribalburephan, Zaw Htet Aung, Knot Pipatsrisawat, Titipat Achakulvisut },
    title        = { Thonburian Whisper: A fine-tuned Whisper model for Thai automatic speech recognition },
    year         = 2022,
    url          = { https://huggingface.co/biodatlab/whisper-th-medium-combined },
    doi          = { 10.57967/hf/0226 },
    publisher    = { Hugging Face }
}
```
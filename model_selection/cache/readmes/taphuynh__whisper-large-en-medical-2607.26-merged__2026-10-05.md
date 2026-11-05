---
base_model: openai/whisper-large-v3-turbo
datasets:
- taphuynh/MayoClinic_00001
- taphuynh/MayoClinic_00002
- taphuynh/MayoClinic_00003
- taphuynh/MayoClinic_00004
- taphuynh/MayoClinic_00005
- taphuynh/MayoClinic_00006
language: en
library_name: peft
license: apache-2.0
metrics:
- wer
- cer
pipeline_tag: automatic-speech-recognition
tags:
- whisper-turbo
- medical-en
- lora
- r32
- warmup500
- whisper
- automatic-speech-recognition
- generated_from_trainer
- arca-tuner-lite
- peft
model-index:
- name: whisper-large-en-medical-2607.26
  results:
  - task:
      type: automatic-speech-recognition
      name: Automatic Speech Recognition
    dataset:
      name: taphuynh/MayoClinic_00001
      type: taphuynh/MayoClinic_00001
    metrics:
    - type: wer
      value: 11.4193
      name: WER
    - type: cer
      value: 7.9598
      name: CER
---
# taphuynh/whisper-large-en-medical-2607.26-merged

Fine-tuned from [`openai/whisper-large-v3-turbo`](https://huggingface.co/openai/whisper-large-v3-turbo) with
`arca-tuner-lite` (`finetune_medical_en`).

- **Base model:** `openai/whisper-large-v3-turbo`
- **Recipe:** LoRA adapter
- **Language(s):** e, n
- **Run tags:** `whisper-turbo`, `medical-en`, `lora`, `r32`, `warmup500`
- **Run group:** `medical-en-warmup`

## Evaluation

Metrics on the held-out eval split, on the best checkpoint (the one this repo
contains — training used early stopping / `load_best_model_at_end`):

| Metric | Value |
| --- | --- |
| WER | 11.4193 |
| CER | 7.9598 |
| loss | 0.4043 |
| model_preparation_time | 0.0194 |
| epoch | 1.0000 |

## Usage

```python
from peft import PeftModel
from transformers import WhisperForConditionalGeneration, WhisperProcessor

base = WhisperForConditionalGeneration.from_pretrained("openai/whisper-large-v3-turbo")
model = PeftModel.from_pretrained(base, "taphuynh/whisper-large-en-medical-2607.26-merged")
processor = WhisperProcessor.from_pretrained("taphuynh/whisper-large-en-medical-2607.26-merged")
```

## Training data

- `taphuynh/MayoClinic_00001`
- `taphuynh/MayoClinic_00002`
- `taphuynh/MayoClinic_00003`
- `taphuynh/MayoClinic_00004`
- `taphuynh/MayoClinic_00005`
- `taphuynh/MayoClinic_00006`

## Training procedure

| Hyperparameter | Value |
| --- | --- |
| learning rate | 0.0001 |
| effective batch size | 16 (16 × 1 grad-accum) |
| max steps | 1500 |
| warmup steps | 500 |
| lr scheduler | cosine |
| precision | bf16 |
| early stopping patience | 4 |
| metric for best model | wer |
| seed | 42 |

The exact resolved configuration and environment are in `run_card.json` in this
repo.

## Notes & limitations

- Fine-tuned on domain-specific speech; expect the usual Whisper failure modes
  (hallucination on silence/noise, degradation far out of domain).
- This is a PEFT/LoRA adapter — load it on top of the base model above.
- Not a medical device and not for clinical decision-making.

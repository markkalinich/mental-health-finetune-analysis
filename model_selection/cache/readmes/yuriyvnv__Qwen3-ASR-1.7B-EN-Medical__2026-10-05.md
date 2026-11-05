---
language:
  - en
license: apache-2.0
library_name: transformers
tags:
  - automatic-speech-recognition
  - speech
  - qwen3-asr
  - qwen
  - english
  - fine-tuned
  - medical
  - multimed
  - common-voice
datasets:
  - leduckhai/MultiMed
  - fixie-ai/common_voice_17_0
base_model: Qwen/Qwen3-ASR-1.7B
pipeline_tag: automatic-speech-recognition
model-index:
  - name: Qwen3-ASR-1.7B-EN-Medical
    results:
      - task:
          type: automatic-speech-recognition
        dataset:
          name: MultiMed English (test)
          type: leduckhai/MultiMed
          config: en
          split: test
        metrics:
          - type: wer
            value: 16.50
            name: Normalized WER (MultiMed)
          - type: cer
            value: 12.45
            name: Normalized CER (MultiMed)
      - task:
          type: automatic-speech-recognition
        dataset:
          name: Common Voice 17.0 English (test)
          type: fixie-ai/common_voice_17_0
          config: en
          split: test
        metrics:
          - type: wer
            value: 6.68
            name: Normalized WER (CV17-en)
          - type: cer
            value: 3.29
            name: Normalized CER (CV17-en)
---

# 🎙️ Qwen3-ASR-1.7B-EN-Medical — English Speech Recognition

<div align="center">
  <img src="https://img.shields.io/badge/Parameters-1.7B-red" alt="1.7B Parameters">
  <img src="https://img.shields.io/badge/Modality-Speech%20%E2%86%92%20Text-purple" alt="Speech to Text">
  <img src="https://img.shields.io/badge/Language-English-green" alt="English">
  <img src="https://img.shields.io/badge/Task-ASR-blue" alt="Automatic Speech Recognition">
  <img src="https://img.shields.io/badge/Base-Qwen3--ASR--1.7B-orange" alt="Base model">
  <img src="https://img.shields.io/badge/Precision-bf16-lightgrey" alt="bf16">
  <img src="https://img.shields.io/badge/License-Apache--2.0-yellow" alt="Apache-2.0">
</div>

<br/>

A medical-domain English automatic speech recognition (ASR) model,
fine-tuned from [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B)
on the English subset of [MultiMed](https://huggingface.co/datasets/leduckhai/MultiMed)
mixed with Common Voice 17 English (train + validation). It outputs
cased, punctuated English text and works as a drop-in replacement for
the base model.


On **MultiMed English (test)** it reaches **16.50% normalized WER**, essentially tied with the published MultiMed paper SOTA (16.62%). On **Common Voice 17 English (test)** it improves to **6.68% normalized WER** vs the base model's 7.54%.

---

## 📊 Results

WER and CER on two held-out test sets — medical (in-domain) and general English (out-of-domain). All numbers are normalized (lowercase + strip punctuation), the standard protocol used by the MultiMed paper and the Open ASR Leaderboard, so they are directly comparable to other published results. "Zero-shot" is the unmodified [Qwen/Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B).

| Test set | Samples | Zero-shot WER | **Fine-tuned WER** | Δ WER | Zero-shot CER | **Fine-tuned CER** |
|---|---:|---:|---:|---:|---:|---:|
| MultiMed English (test) | 7,567 | 16.41 | **16.50** | **+0.09** | 12.60 | **12.45** |
| Common Voice 17 EN (test) | 16,393 | 7.54 | **6.68** | **-0.86** | 3.68 | **3.29** |

For reference, the MultiMed paper's best published result is Whisper-Small multilingual fine-tune at **16.62% WER** (arXiv 2409.14074, Table 6). Both the base Qwen3-ASR and this fine-tune match that level.

The interesting story here is general English. The fine-tune actually improves on the base model's CV17 WER by 0.86 absolute points / 11% relative, while preserving medical performance. That's the opposite of catastrophic forgetting — including Common Voice in the training mix kept the base distribution intact and the medical exposure didn't hurt anything.

## 🧹 Reference / target normalisation

MultiMed transcripts are real-world clinical speech and inconsistent in casing and trailing punctuation. To give the model a clean, predictable target distribution we apply a small, deterministic **written-form normalisation** to every reference at load time, both during training and during evaluation:

1. **Capitalise the first letter** if it is lowercase.
2. **Collapse trailing dots** — any sequence of `.`, `…`, `..`, `...` at the
   end is replaced with a single `.`.
3. **Append a terminal period** if the sentence does not already end in
   terminal punctuation (`. ! ? …`) or a closing bracket / quote
   (`) ] } " '` etc.).

The exact function lives in `src/evaluation/score_written_form.py` of the
project repository. Concretely:

| Raw reference                                | Normalised                                     |
|----------------------------------------------|------------------------------------------------|
| `the patient presented with chest pain`      | `The patient presented with chest pain.`       |
| `TAVI is indicated for severe aortic stenosis...` | `TAVI is indicated for severe aortic stenosis.` |
| `What is the dosage?`                        | `What is the dosage?` *(unchanged)*            |

Because the **same** normalisation is applied to references used for the
zero-shot baseline above, the gain reported in the results table reflects the
fine-tune itself — **not** a metric quirk caused by mismatched references.

## 🚀 How to use

Install the official `qwen-asr` package, then load this model exactly the
same way you would load the base Qwen3-ASR:

```bash
pip install qwen-asr
```

```python
import torch
from qwen_asr import Qwen3ASRModel

model = Qwen3ASRModel.from_pretrained(
    "yuriyvnv/Qwen3-ASR-1.7B-EN-Medical",
    dtype=torch.bfloat16,
    device_map="cuda:0",
)

result = model.transcribe(audio="audio.wav", language="English")
print(result[0].text)
```

Batch inference, automatic language detection, streaming, and vLLM serving
all work identically to the base model — see the
[upstream Qwen3-ASR documentation](https://github.com/QwenLM/Qwen3-ASR) for
details.

## 🛠️ Training

**Datasets:**
- [leduckhai/MultiMed (English)](https://huggingface.co/datasets/leduckhai/MultiMed) — medical-domain speech (~84h, 25,497 clips after filtering)
- [fixie-ai/common_voice_17_0 (en)](https://huggingface.co/datasets/fixie-ai/common_voice_17_0) train + validation splits — Common Voice 17, crowdsourced English (~1.04M clips)

Concatenated and shuffled per epoch. CV17 dominates the mix at ~97.5% by clip count, which anchors general English while MultiMed steers the model toward clinical vocabulary.

**Validation:** MultiMed-en eval split (~2,807 clips) drives best-checkpoint selection. CV17 test stays fully held out.

**Recipe:** follows the
[official QwenLM SFT recipe](https://github.com/QwenLM/Qwen3-ASR/tree/main/finetuning):

| Parameter | Value |
|---|---|
| Learning rate | 2e-05 |
| Scheduler | linear |
| Warmup ratio | 0.02 |
| Per-device batch size | 64 |
| Gradient accumulation | 3 |
| Effective batch size | 192 |
| Epochs | 3 |
| Precision | bf16 mixed |
| Gradient checkpointing | enabled |
| Optimizer | AdamW (fused) |

Trained on a single H100. The best checkpoint was selected by validation loss.

## ⚠️ Limitations

- Trained on MultiMed medical-domain speech (clinical consultations, surgical
  procedures, patient narratives). Performance outside medical contexts is
  not guaranteed to improve over the base model.
- Outputs English text. Cross-lingual or code-switched audio is not
  targeted.
- Punctuation and casing are best-effort and inherit the inconsistencies of
  the underlying transcripts (mitigated, but not eliminated, by the
  normalisation step above).
- Long-form clinical audio (>30s) is filtered out at training time; very
  long consultations may need to be chunked at inference.

## 🙏 Acknowledgements

This model would not exist without the work of others. Thank you to:

- **The Qwen team at Alibaba Cloud** for releasing
  [Qwen3-ASR-1.7B](https://huggingface.co/Qwen/Qwen3-ASR-1.7B) — the backbone of
  this fine-tune — together with a clean, reproducible
  [SFT recipe](https://github.com/QwenLM/Qwen3-ASR/tree/main/finetuning).
- **Khai Le-Duc and the MultiMed authors** for releasing the MultiMed
  multilingual medical ASR dataset
  ([leduckhai/MultiMed](https://huggingface.co/datasets/leduckhai/MultiMed),
  [paper](https://arxiv.org/abs/2409.14074)) that made this domain-specialised
  fine-tune possible.

---
base_model: kenpath/svara-tts-v1
license: apache-2.0
language:
- hi   # Hindi
- bn   # Bengali
- mr   # Marathi
- te   # Telugu
- kn   # Kannada
- bho  # Bhojpuri
- mag  # Magahi
- hne  # Chhattisgarhi
- mai  # Maithili
- as   # Assamese
- brx  # Bodo
- doi  # Dogri
- gu   # Gujarati
- ml   # Malayalam
- pa   # Punjabi
- ta   # Tamil
- ne   # Nepali
- sa   # Sanskrit
- en   # English (Indian)
tags:
- text-to-speech
- speech-synthesis
- transformers
- multilingual
- indic
- orpheus
- lora
- low-latency
- gguf
- zero-shot
- emotions
- discrete-audio-tokens
task_categories:
- text-to-speech
pipeline_tag: text-to-speech
pretty_name: Svara-TTS v1
datasets:
- SYSPIN
- RASA
- IndicTTS
- SPICOR
---


# svara-tts-voiceclone-beta — Voice Cloning + Expressive TTS for Indic Languages

[![🤗 Hugging Face - Model](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Model-black)](https://huggingface.co/kenpath/svara-tts-voiceclone-beta)
[![🤗 Hugging Face - Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-green)](https://huggingface.co/spaces/kenpath/svara-tts)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
[![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=flat\&logo=github\&logoColor=white)](https://github.com/Kenpath/svara-tts-inference)

**svara-tts-voiceclone-beta** is an experimental extension of **svara-tts-v1**, designed to bring **lightweight voice cloning** and improved **accent preservation** to Indic languages. It introduces a simple but effective **reference-swap finetuning** technique, enabling more stable zero-shot speaker identity across long, expressive utterances.

Built on an Orpheus-style discrete audio token architecture, the model supports **19 languages**, expressive cues (`<laugh>`, `<yawn>`, `<angry>`), and low-latency TTS on commodity hardware.

---

## At a Glance

* **Languages (19):** Hindi, Bengali, Marathi, Telugu, Kannada, Bhojpuri, Magahi, Chhattisgarhi, Maithili, Assamese, Bodo, Dogri, Gujarati, Malayalam, Punjabi, Tamil, Nepali, Sanskrit, Indian English.
* **Voice Cloning:** Improved consistency using **reference-swap finetuning**, works with short (≈10s) reference audio.
* **Expressivity:** Emotion tags; non-verbal cues; improved Indic prosody.
* **Low-Latency Deployment:** Fully compatible with GGUF and **vLLM**.
* **Adaptability:** LoRA-ready; easy to specialize for speakers, domains, or dialects.

Demo playback uses the same Space as svara-tts-v1.

---

## Prompting (Orpheus-Style)

* Place style/emotion tags at the end:
  `आज शाम को जल्दी मिलते हैं। <neutral>`
* Provide reference audio tokens before the target text.
* Use punctuation to control rhythm, pauses, and emphasis.

**Zero-shot example:**

```
<BOS>
<reference_audio_tokens_here>
कल शाम को जल्दी मिलते हैं। <neutral>
<SOA>
```

Speaker IDs remain compatible with svara-tts-v1: **`Language (Gender)`**.

---

## Training Data Summary

`svara-tts-voiceclone-beta` is enhanced from the multilingual base of **svara-tts-v1**, trained on:

* **SYSPIN**, **RASA**, **IndicTTS**, **SPICOR**
* ~2000 hours, ~50 speakers, balanced male/female
* Rich phoneme coverage across 19 Indic languages

The **reference-swap augmentation** uses multi-utterance samples to improve speaker consistency across Indic phonetic variation.

---

## Intended Uses

* Zero-shot voice cloning for Indic voices
* Dialogue systems, IVR, learning apps, accessibility solutions
* Content creation, localization, storytelling
* Research on speech identity, expressivity, and multilingual TTS

## Out-of-Scope / Not Intended

* Impersonating private individuals without consent
* Fraud, targeted deception, harassment
* High-risk or safety-critical deployments
* Perfect 1:1 replication of voices (this is a beta research release)

---

## Limitations

* Zero-shot cloning is **not** identical to dedicated finetuning
* Speaker similarity may degrade over long utterances
* Varies by language due to dataset imbalance
* Emotion emphasis may differ across low-resource languages
* Rare names and numbers may require normalization or rewriting

These improve with targeted LoRA finetuning or higher-quality data.

---

## Responsible Use

By using this model, you agree to follow applicable laws and ethical guidelines. Synthetic speech should be disclosed when appropriate. Avoid impersonation or harmful use cases.

---

## Sources & Links

* **Base Model (svara-tts-v1):** [https://huggingface.co/kenpath/svara-tts-v1](https://huggingface.co/kenpath/svara-tts-v1)
* **Demo Space:** [https://huggingface.co/spaces/kenpath/svara-tts](https://huggingface.co/spaces/kenpath/svara-tts)
* **Inference Repo:** [https://github.com/Kenpath/svara-tts-inference](https://github.com/Kenpath/svara-tts-inference)
* **Indic Text Normalizer:** [https://github.com/Kenpath/indic-text-normalization](https://github.com/Kenpath/indic-text-normalization)

---

## 🙏 Acknowledgments

Developed by **Kenpath Technologies**. Special thanks to:

* **Canopy Labs — Orpheus** (architecture & research release)
* **SYSPIN / SPICOR — IISc Bangalore**
* **AI4Bharat — RASA**
* **IIT Madras — IndicTTS**
* **Unsloth** (training tools & LoRA insights)
* **RunPod** (GPU compute credits)

---

## License

**Apache-2.0**

---

## Versioning & Changelog

* **v0.1.0-beta:** Initial release with reference-swap voice cloning
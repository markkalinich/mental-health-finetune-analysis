---
base_model: canopylabs/orpheus-3b-0.1-ft  
tags:
- speech
- tts
- voice-assistant
- single-speaker
- emotion
- finetune
- sft
- tokenizer-special-tokens
- english
license: apache-2.0
language:
- en
pipeline_tag: text-to-speech
datasets:
- MrDragonFox/Elise
---

<div align="center">
<img src="https://huggingface.co/alphaaico/SpeakSpace-Assistant-v1-3B/resolve/main/SpeakSpace_thumbnail.png"
     alt="SpeakSpace Assistant"
     style="width: 600px; height: auto; object-position: center top;">
</div>

# SpeakSpace-Assistant-v1-3B

**Alpha AI (www.alphaai.biz)** fine-tuned `canopylabs/orpheus-3b-0.1-ft` to create **SpeakSpace-Assistant-v1-3B** — an English-only, single-speaker voice assistant model. The fine-tune uses custom voice recordings plus the Elise dataset (~3 hours, single-speaker English speech). Transcripts were augmented with emotion/expression tags like `<sigh>` and `<laughs>`, added as special tokens in the Orpheus tokenizer.

> ⚠️ **Important:** This model is intended for research, prototyping, and internal product demos. Do not use it to impersonate a real person without explicit consent. Review base-model and dataset licenses before commercial use.

---

## TL;DR

* **Base:** `canopylabs/orpheus-3b-0.1-ft` (~3B params).
* **Data:** Custom Alpha AI dataset + `MrDragonFox/Elise` (English, ~3 hours).
* **Objective:** Produce natural, expressive speech with inline emotion cues (`<laughs>`, `<sigh>`).
* **Language:** English only.
* **Repo:** Suggested as `alpha-ai/SpeakSpace-Assistant-v1-3B`.

---

## Intended Use & Limitations

**Intended use:**
- Internal voice assistants and demos.
- Research on expressive TTS and emotion-tag-conditioned speech.
- Applications where transcripts include small expressive markers.

**Limitations:**
- Not multi-speaker or multilingual.
- Quality limited by dataset size (~3 hrs + custom data).
- Requires Orpheus vocoder/decoder to convert tokens to waveform.
- Do not deploy for impersonation without explicit consent.

---

## Model Details

- **Family:** Orpheus 3B (decoder-based speech model).
- **Tokenizer:** Extended with special tokens (`<laughs>`, `<sigh>`).
- **Fine-tuning:** Supervised finetuning on audio–transcript pairs.
- **Output:** Discrete audio tokens; decode with Orpheus vocoder.

---

## Data

**Sources:**
- Alpha AI custom speech dataset.
- [MrDragonFox/Elise](https://huggingface.co/datasets/MrDragonFox/Elise) (~3 hrs English single-speaker).

**Preprocessing:**
- Aligned utterances with transcripts.
- Expression tags inserted inline.
- Special tokens added to tokenizer.

---

## Prompt & Input Format

Model accepts text input with optional inline expressions:

```text
Hello! <laughs> I can help with your schedule today.
```

Workflow: tokenize → generate audio tokens → decode via vocoder.

---

## Training Summary

- **Objective:** Predict audio tokens from transcripts (with expression markers).
- **Loss:** Causal LM loss.
- **Optimizer:** AdamW or AdamW-8bit (please add exact values).
- **Hyperparameters:** Learning rate, batch size, gradient accumulation, seed — *to be filled with actual values*.

---

## Evaluation

Recommended:
- **MOS (Mean Opinion Score):** naturalness & expressiveness.
- **Speaker similarity:** ABX or MOS vs. ground truth.
- **Intelligibility:** WER via ASR.
- **Emotion accuracy:** Human rating of `<laughs>`, `<sigh>` cues.

Add quantitative results when available.

---

## Safety & Responsible Use

- Use only with documented consent for training voices.
- Guard against impersonation risks.
- Consider watermarking or metadata tagging for provenance.
- Do not generalize beyond training speaker’s identity.

---

## License & Attribution

- **Base model:** `canopylabs/orpheus-3b-0.1-ft` (review base license).
- **Dataset:** `MrDragonFox/Elise` (check dataset license).
- **Fine-tune:** Ensure compatibility of licenses.

Suggested citation:
```
SpeakSpace-Assistant-v1-3B — fine-tune of canopylabs/orpheus-3b-0.1-ft on Alpha AI custom dataset + MrDragonFox/Elise.
```

---

## Acknowledgements

- canopylabs — Orpheus base model.
- MrDragonFox — Elise dataset.
- Alpha AI research & engineering team.

---

## Contact

Questions, issues, or collaborations:
- Open a discussion on the Hugging Face repo.
- Enterprise contact (Alpha AI): www.alphaai.biz | corporate@alphaai.biz
- Enterprise contact (SpeakSpace): www.speakspace.co | connect@speakspace.co
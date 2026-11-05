---
license: cc-by-4.0
base_model: laion/moss-tts-local-transformer-4.55b-voice-acting-v2
library_name: transformers
pipeline_tag: text-to-speech
language:
  - en
  - de
tags:
  - text-to-speech
  - voice-acting
  - speech-synthesis
  - moss
  - emotion
  - voice-cloning
datasets:
  - laion/laion-voice-profiles-sft
  - laion/tts-realspeech-sft-en-de
---

# MOSS Voice-Acting 4.55B — SFT

A full fine-tune of
[`laion/moss-tts-local-transformer-4.55b-voice-acting-v2`](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2)
on **3,147,802 annotated utterances** — half synthetic voice profiles, half real speech in English
and German — for three epochs.

By **Christoph Schuhmann** and **LAION**.

Held-out validation loss fell at **every one of the twelve evaluations**, on both constituent
datasets independently: **4.7076 → 4.6314**.

---

## What changed relative to the base model

This is not an adapter. All 4.13 B parameters were trained.

| | |
|---|---|
| samples seen | 9,443,406 sample-passes (3,147,802 × 3 epochs) |
| peak learning rate | 7e-6, cosine, warmup over the first half of epoch 1, decayed to 10 % |
| optimizer | AdamW, β (0.9, 0.95), ε 1e-8, weight decay 0.1, grad-norm clip 1.0 |
| precision | fp32 master weights, bf16 compute |
| global batch | 4,096 samples |
| steps | 2,232 |
| hardware | 64 nodes × 4 GH200 = 256 GPUs, 1 h 53 min |
| loss | channel-wise cross-entropy, 1 : 32 weighting of the stop channel against the 12 audio codebooks |

**Learning rate, and why 7e-6.** The reference trainer for this model family defaults to 1e-5, but
that default is for a small fine-tune at an effective batch of ~32. Here an already-specialised
checkpoint is fully fine-tuned over 9.4 M sample-passes at a global batch of 4,096. A long
full-fine-tune schedule on a good checkpoint argues for a lower rate; a large batch (less gradient
noise) argues for a higher one. 7e-6 is 0.7× the reference default.

---

## Validation

Held out by `blake2b(uid) % 1000 == 0` — deterministic, disjoint from training, and covering both
datasets. Loss is reported per dataset so a regression on one cannot hide behind a gain on the
other.

| step | val loss | voice profiles | real speech |
|--:|--:|--:|--:|
| 186 | 4.7076 | 4.4786 | 4.8668 |
| 558 | 4.6621 | 4.4342 | 4.8206 |
| 930 | 4.6472 | 4.4199 | 4.8053 |
| 1302 | 4.6370 | 4.4090 | 4.7956 |
| 1674 | 4.6328 | 4.4047 | 4.7915 |
| **2232** | **4.6314** | **4.4030** | **4.7902** |

Monotone throughout, no divergence between the two datasets, no sign of overfitting at three
epochs. Voice profiles sit ~0.39 nats below real speech, which is expected — synthetic
single-voice material is more predictable than recordings made in the wild.

Listen before you trust the number: the validation sample grid pairs the base model, this
fine-tune and the ground truth on the same held-out prompts.

---

## Prompt format

The model expects the MOSS `<user_inst>` block. **The exact prompt surface it was trained on
matters** — the training mix deliberately varied it, and departing from these conventions will
cost you quality.

```
<user_inst>
- Reference(s):
{<|audio|>  |  Speaker: <name>  |  None}
- Instruction:
{caption}
- Tokens:
{target frame count, 12.5 fps}
- Quality:
None
- Sound Event:
None
- Ambient Sound:
None
- Language:
{English | German}
- Text:
{[7.3 seconds duration] }{transcript}
</user_inst>
```

What the training mix contained, and in what proportion:

| element | training distribution |
|---|---|
| **Reference slot** | reference audio 50 % / `Speaker: <name>` 50 % for voice profiles; reference-or-`None` for real speech |
| **Instruction** | four surfaces: one of 16 rendered caption templates (30 %), `GENERAL: …\nSCRIPT:\n…` (45 %), `GENERAL:` only (15 %), `SCRIPT:` only (10 %) |
| **Duration tag** | `[7.3 seconds duration] ` prefixed to the text on 50 % of samples |
| **Inline burst cues** | parenthesised cues such as `(laughs)` present, but stripped entirely from **both** text and caption on 10 % of samples |

The duration tag is **spoken** duration — last word offset minus first word onset — not clip
duration. Clip duration overstates it by ~1.05 s on voice profiles and ~0.40 s on real speech
because of leading and trailing silence. If you tag with clip duration the model will pad.

Reference audio is passed as codec codes, `[T, 12]` int64, directly in `audio_codes_list`; no audio
tokenizer is needed at inference for conditioning.

### Usage

```python
import torch
from transformers import AutoProcessor, AutoModel

REPO = "laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft"
proc = AutoProcessor.from_pretrained(REPO, trust_remote_code=True,
                                     codec_path="OpenMOSS-Team/MOSS-Audio-Tokenizer-v2")
model = AutoModel.from_pretrained(REPO, trust_remote_code=True,
                                  dtype=torch.bfloat16, attn_implementation="sdpa").cuda().eval()

msg = proc.build_user_message(
    text="[4.2 seconds duration] I really did not see that coming.",
    instruction="GENERAL: A young adult feminine voice; delivery is bright and quick; "
                "affect is positive, animated.\nSCRIPT:\n\"I really did not see that coming.\"",
    tokens=53, language="English")
batch = proc([[msg]], mode="generation")
out = model.generate(input_ids=batch["input_ids"].cuda(),
                     attention_mask=batch["attention_mask"].cuda(),
                     max_new_frames=400, do_sample=True,
                     audio_temperature=1.0, audio_top_p=0.95, audio_top_k=50)
wav = proc.decode(out)[0].audio_codes_list[0]   # 48 kHz
```

`tokens` is the target length in codec frames at 12.5 fps — 4.2 s ≈ 53 frames.

---

## Training data

| dataset | rows | share of each batch |
|---|--:|--:|
| [`laion/laion-voice-profiles-sft`](https://huggingface.co/datasets/laion/laion-voice-profiles-sft) | 1,200,531 | 50 % |
| [`laion/tts-realspeech-sft-en-de`](https://huggingface.co/datasets/laion/tts-realspeech-sft-en-de) | 1,947,272 | 50 % |

**Every micro-batch was exactly half of each dataset** — the sampler alternates strictly between
the two pools rather than mixing in expectation. Verified on 20 real batches: 0.5000 / 0.5000 on
every one.

Because the two datasets are unequal in size and each batch is balanced, over three nominal epochs
the voice-profile rows are seen ≈3.93 times and the real-speech rows ≈2.42 times.

The voice-profile source ships strictly **one voice per file**, so the corpus was globally shuffled
before training; each shard ends up containing all 500 voices. Measured on real batches: 7.75
distinct voices per 8-sample batch, and no single voice ever exceeded 25 % of a batch.

---

## Limitations

- **Two languages only.** English and German. Anything else is out of distribution.
- **Validation loss is not audio quality.** It measures next-token likelihood on held-out codec
  tokens. No listening test, MOS study, or intelligibility benchmark has been run. Judge the sample
  grid with your own ears.
- **The reference audio must be the same voice you want.** Speaker similarity was not re-measured
  after fine-tuning.
- **Three epochs on a balanced mix over-represents the synthetic half.** If your use is
  real-recorded speech, that skew is worth knowing.
- Inherits whatever biases exist in the underlying corpora — speaker demographics, recording
  conditions and emotion labelling are not uniformly distributed.
- The 12 audio LM heads are weight-tied to the audio embeddings, as in the base model.

## Intended use

Research on expressive and controllable speech synthesis. Not validated for, and should not be used
for, generating speech attributed to a real person without their consent, or for any application
where a synthetic voice could be mistaken for a specific individual.

---

## Licence and attribution

Released under **CC-BY-4.0** by **Christoph Schuhmann** and **LAION**.

The base model `laion/moss-tts-local-transformer-4.55b-voice-acting-v2` is Apache-2.0, and that
notice is preserved: this work is a derivative of it. The MOSS-TTS architecture and the
MOSS-Audio-Tokenizer-v2 codec originate with the OpenMOSS team.

```bibtex
@misc{schuhmann2026mossva_sft,
  title  = {MOSS Voice-Acting 4.55B --- SFT},
  author = {Schuhmann, Christoph and {LAION}},
  year   = {2026},
  url    = {https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft},
  note   = {Full fine-tune on 3.15M annotated utterances; CC-BY-4.0}
}
```

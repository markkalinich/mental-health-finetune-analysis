---
license: cc-by-4.0
base_model: laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft
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
  - dpo
datasets:
  - laion/laion-voice-profiles-sft
  - laion/tts-realspeech-sft-en-de
  - laion/laion-voice-profiles-dpo
  - laion/tts-realspeech-dpo-en-de
---

# MOSS Voice-Acting 4.55B — SFT + DPO (full-parameter)

**Full-parameter preference tuning of the SFT model.** All 4.13 B parameters were updated in both
stages — this is not an adapter and not a merge of one. It is the `SFT + DPO full` track on the
[sample grid](https://huggingface.co/spaces/laion/moss-va-sft-samples).

By **Christoph Schuhmann** and **LAION**.

Two training stages on top of
[`laion/moss-tts-local-transformer-4.55b-voice-acting-v2`](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2):

1. **SFT** — all 4.13 B parameters, 3 epochs over **3,147,802 annotated utterances**
   ([`…-v2-sft`](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft)).
2. **DPO** — full-parameter preference tuning of that checkpoint on **7,410,723 preference
   pairs**. A rank-64 LoRA alternative trained on the same data and objective is published
   separately as
   [`…-v2-dpo-lora`](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2-dpo-lora).

**In informal listening this is the best of the three** (base / SFT / SFT+DPO) on most prompts.

---

## What is and is not established

| claim | evidence |
|---|---|
| SFT improved held-out likelihood | val loss **4.7076 → 4.6314**, monotone across all 12 evaluations, on both constituent datasets independently |
| SFT+DPO sounds best | informal listening on the shared sample grid; **no MOS study, no blind test** |
| the DPO stage is not over-optimised | **it partly is** — see below |
| the DPO stage actually changed the weights | **357 of 425 tensors** differ from the SFT base, max relative delta **1.70e-03**; recorded in `provenance.json` in this repo |
| the run completed | **it did not** — see below |

**The run stopped early, and that is worth knowing before you use this.** It reached **step 123 of
988** — one eighth of the planned epoch — wrote its checkpoint, and then died: an `ALLREDUCE` of
24,916,480 elements timed out after 600 s across 256 ranks immediately following that save, and
NCCL aborted the job (`EXIT=134`). The checkpoint itself is complete and loads and generates
normally; there is simply no later one. Full-parameter DPO here shards its Adam state with
`ZeroRedundancyOptimizer` (a second frozen reference copy plus fp32 master weights, gradients and
moments would otherwise need 74.3 GB before a single activation), and a ZeRO-sharded optimizer
state is not written by `save_state`, so the run was never resumable either.

**The DPO caveat, stated plainly.** On this preference set, DPO over-optimises: preference
accuracy climbs to 0.994 while `reward(chosen)` — the implicit reward on the *preferred* sequence
— falls to −2.39, meaning the policy makes the good audio less likely too, only less so than the
bad. This checkpoint's single evaluation reads
`val_loss = 0.9394`, preference accuracy **0.8965**, `reward(chosen) = −0.264`,
`reward(rejected) = −13.549`. It is flagged unhealthy by that rule. Stopping at step 123 is, by
accident, close to where the LoRA variant's checkpoint selection independently landed (step 246 of
988) — in the LoRA run `reward(chosen)` fell monotonically from −0.111 to −2.385 over the
following 615 steps, so a completed run would very likely have been worse, not better.

Preference accuracy is not a health metric here. It was highest exactly where the model was most
degraded.

---

## Training summary

### Stage 1 — SFT

| | |
|---|---|
| samples seen | 9,443,406 sample-passes (3,147,802 × 3 epochs) |
| peak LR | 7e-6, cosine, warmup over the first half of epoch 1, decayed to 10 % |
| optimizer | AdamW, β (0.9, 0.95), ε 1e-8, weight decay 0.1, clip 1.0 |
| precision | fp32 master weights, bf16 compute |
| global batch | 4,096 samples · 2,232 steps |
| hardware | 64 nodes × 4 GH200 = 256 GPUs, 1 h 53 min |
| loss | channel-wise cross-entropy, 1 : 32 stop-channel vs the 12 audio codebooks |

Every micro-batch was **exactly** half voice profiles / half real speech — the sampler alternates
strictly rather than mixing in expectation (verified 0.5000 / 0.5000 on 20 real batches). Measured
7.75 distinct voices per 8-sample batch, no voice above 25 % of a batch.

### Stage 2 — DPO (full-parameter)

| | |
|---|---|
| trainable | **all 4.13 B parameters** |
| objective | DPO, length-normalised, β = 30, chosen-NLL anchor 0.013 |
| peak LR | **5e-7**, cosine, 10 % warmup |
| optimizer | AdamW, `ZeroRedundancyOptimizer` (Adam state sharded across 256 ranks) |
| shipped step | 123 of 988 (the run aborted immediately after this checkpoint) |
| global batch | 2,048 pairs per step, 64 nodes × 4 GH200 |

Length normalisation is load-bearing: **85.6 % of the raw preference pairs differ from the chosen
sequence mainly in LENGTH**, and an unnormalised summed log-probability reached 1.000 preference
accuracy at step 102 of 1194 by counting tokens. The length families were also downsampled to
`length_keep = 0.16`, which keeps all 1,064,594 emotion pairs and raises emotion from 14.4 % to
≈51 % of the mix.

The anchor weight 0.013 is not a guess: `-logp` is ≈**54 nats per position** here, because each
supervised position carries 13 channels (12 codebooks + the binary stop head). A first attempt at
0.25 put the anchor at ≈13.6 against a DPO term of 0.69 and turned the run into an SFT pass.

---

## Prompt format

Identical to the SFT model's — the DPO stage used the **same prompt library**
(format hash `3d8a696ccec4a98f`), which is what lets the two stages compose at all.

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

| element | training distribution |
|---|---|
| **Reference slot** | reference audio 50 % / `Speaker: <name>` 50 % for voice profiles; reference-or-`None` for real speech |
| **Instruction** | four surfaces: one of 16 rendered caption templates (30 %), `GENERAL: …\nSCRIPT:\n…` (45 %), `GENERAL:` only (15 %), `SCRIPT:` only (10 %) |
| **Duration tag** | `[7.3 seconds duration] ` prefixed to the text on 50 % of samples |
| **Inline burst cues** | parenthesised cues such as `(laughs)` present, stripped from **both** text and caption on 10 % of samples |

The duration tag is **spoken** duration — last word offset minus first word onset — **not clip
duration**. Clip duration overstates it by ~1.05 s on voice profiles and ~0.40 s on real speech
because of leading and trailing silence; tag with clip duration and the model will pad.

Reference audio is passed as codec codes, `[T, 12]` int64, in `audio_codes_list`. No audio
tokenizer is needed at inference for conditioning.

---

## Usage

```python
import torch
from transformers import AutoProcessor, AutoModel

REPO  = "laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft-dpo"
CODEC = "OpenMOSS-Team/MOSS-Audio-Tokenizer-v2"

proc  = AutoProcessor.from_pretrained(REPO, trust_remote_code=True, codec_path=CODEC)
model = AutoModel.from_pretrained(REPO, trust_remote_code=True,
                                  dtype=torch.bfloat16,
                                  attn_implementation="sdpa").cuda().eval()

msg = proc.build_user_message(
    text="[4.2 seconds duration] I really did not see that coming.",
    instruction="GENERAL: A young adult feminine voice; delivery is bright and quick; "
                "affect is positive, animated.\nSCRIPT:\n\"I really did not see that coming.\"",
    tokens=53,                      # 4.2 s x 12.5 fps
    language="English")

batch = proc([[msg]], mode="generation")
out = model.generate(input_ids=batch["input_ids"].cuda(),
                     attention_mask=batch["attention_mask"].cuda(),
                     max_new_frames=400, do_sample=True,
                     audio_temperature=1.0, audio_top_p=0.95, audio_top_k=50,
                     audio_repetition_penalty=1.0)

wav = proc.decode(out)[0].audio_codes_list[0]        # 48 kHz waveform
import soundfile as sf
sf.write("out.wav", wav.float().cpu().numpy(), int(proc.model_config.sampling_rate))
```

### Cloning a voice from a reference clip

```python
codes = proc.audio_tokenizer.encode(wav48k)          # [T, 12] int64 at 12.5 fps
msg = {"role": "user",
       "content": prompt_text_with_audio_placeholder, # "<|audio|>" in the Reference(s) slot
       "audio_codes_list": [codes]}
```

Keep the reference under ~25 s; the training pipeline capped references at 320 frames.

### Naming a voice instead

Put `Speaker: <name>` in the Reference(s) slot. The 500 profile names the model was trained on are
listed with
[`laion/moss-voice-profile-loras-500`](https://huggingface.co/laion/moss-voice-profile-loras-500);
a name outside that set is out of distribution.

---

## Training data

| dataset | rows / pairs | stage |
|---|--:|---|
| [`laion/laion-voice-profiles-sft`](https://huggingface.co/datasets/laion/laion-voice-profiles-sft) | 1,200,531 | SFT |
| [`laion/tts-realspeech-sft-en-de`](https://huggingface.co/datasets/laion/tts-realspeech-sft-en-de) | 1,947,272 | SFT |
| [`laion/laion-voice-profiles-dpo`](https://huggingface.co/datasets/laion/laion-voice-profiles-dpo) | 3,451,531 | DPO |
| [`laion/tts-realspeech-dpo-en-de`](https://huggingface.co/datasets/laion/tts-realspeech-dpo-en-de) | 3,959,192 | DPO |

Annotation source:
[`laion/laion-voice-profiles-annotated`](https://huggingface.co/datasets/laion/laion-voice-profiles-annotated).

---

## If you want to merge the LoRA variant instead — do not use `merge_and_unload()`

Measured, because it is a silent failure. The 12 `audio_lm_heads` are **weight-tied** to the audio
embeddings — `tie_weights()` assigns `head.weight = embedding.weight`, the same tensor object.
The rank-64 adapter targets those heads, so folding `W ← W + BA` writes the head update into the
embeddings as well:

```
audio_lm_heads.0.weight    max|ΔW| = 6.103515625e-05     (the merge)
audio_embeddings.0.weight  max|ΔW| = 6.103515625e-05     (same tensor)
transformer.embed_tokens.weight  max|ΔW| = 0.0           (not a LoRA target, correct)
```

The result loads, generates, and sounds like speech — and is a **different function** from the
adapter: on the same input, the final hidden state differs with rms 0.107 against a signal rms of
2.518, **4.3 %**. Use the adapter unmerged, or use this full-parameter model.

## Known faults, and what is being done about them

Both are audible and both have an identified cause:

- **Vocal bursts run too long.** The training prompts named a burst (`(sigh)`) without ever saying
  how long it should last, so nothing constrains its length. Additionally, 39.4 % of the
  parenthetical cues in the voice-profile corpus are *synthesis directions the burst detector
  never confirmed* — a cue with no corresponding audio.
- **Occasional unprompted content.** Better than the base model and better than SFT alone, but
  present. Nothing in the prompt states a per-utterance time budget.

A follow-up round replaces the single clip-level duration tag with a full timed script — a
per-sentence `[12.0 seconds duration]`, an explicit `[0.6 seconds pause]` for every silence over
200 ms, and `(contented sigh, 0.4 seconds)` for every burst — built from word-level timestamps and
*detected* burst spans only.

## Other limitations

- **English and German only.**
- **Validation loss is not audio quality.** No MOS study, intelligibility benchmark or
  speaker-similarity re-measurement has been run.
- **The SFT stage saw the synthetic half ≈3.93× and the real half ≈2.42×**, a consequence of
  balancing every batch across two unequal datasets.
- **The DPO stage covered 12.5 % of one epoch.** Whatever it learned, it learned from 251,904
  preference pairs, not 7.41 M.
- Inherits the corpora's biases in speaker demographics, recording conditions and emotion labels.
- The 12 audio LM heads are weight-tied to the audio embeddings, as in the base model.

## Intended use

Research on expressive and controllable speech synthesis. Not validated for, and should not be
used for, generating speech attributed to a real person without their consent, or for any
application where a synthetic voice could be mistaken for a specific individual.

---

## Licence and attribution

Released under **CC-BY-4.0** by **Christoph Schuhmann** and **LAION**.

Derived from `laion/moss-tts-local-transformer-4.55b-voice-acting-v2` (Apache-2.0), whose notice is
preserved. The MOSS-TTS architecture and the MOSS-Audio-Tokenizer-v2 codec originate with the
OpenMOSS team.

```bibtex
@misc{schuhmann2026mossva_sftdpo,
  title  = {MOSS Voice-Acting 4.55B --- SFT + DPO (full-parameter)},
  author = {Schuhmann, Christoph and {LAION}},
  year   = {2026},
  url    = {https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft-dpo},
  note   = {Full fine-tune on 3.15M utterances plus full-parameter DPO; CC-BY-4.0}
}
```

---
license: apache-2.0
library_name: transformers
pipeline_tag: text-to-speech
tags:
  - moss-tts
  - moss-tts-local
  - voice-acting
  - expressive-tts
  - vocal-bursts
  - 48khz
language: [en, de]
pretty_name: MOSS-TTS-Local 4.55B — Voice Acting v2 (further fine-tuned on synthetic data)
---

# MOSS-TTS-Local **4.55B** — Voice Acting **v2** (48 kHz local transformer)

An **expressive voice-acting** model: fantasy characters (orc / dragon / fairy / goblin), shouting,
whispering, and **vocal bursts** (laughs, gasps, sighs, giggles, moans) driven by natural-language
director instructions, in **English and German**.

**Authors: Christoph Schuhmann and LAION.**

### What is new in v2

This checkpoint is the **latest and best** in the line. It was obtained by taking the previous
release —
[`laion/moss-tts-local-transformer-4.55b-voice-acting`](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting)
— and running **further supervised fine-tuning on additional synthetic voice-acting data**. The
extra data was **self-generated with the model family and filtered with a Best-of-N reward**
(a lightweight VoiceCLAP-based genuineness + vocal-burst-blend + character reward that keeps only the
strongest of many candidate takes per prompt), so the model learns from its own highest-quality
performances — more consistent character delivery, more natural vocal bursts, and cleaner emotional
range. It remains a full **4.55-billion-parameter local-transformer** MOSS variant at **48 kHz** and
is a **drop-in replacement** for the previous release (same architecture, tokenizer, and prompt
format).

Its sibling is the **8-billion-parameter delay-architecture** model at 24 kHz:
[`laion/moss-tts-v1.5-8b-voice-acting`](https://huggingface.co/laion/moss-tts-v1.5-8b-voice-acting).

| | **this model — 4.55B local transformer** | [8B delay](https://huggingface.co/laion/moss-tts-v1.5-8b-voice-acting) |
|---|---|---|
| architecture | `moss_tts_local`, 12-codebook RVQ | `moss_tts_delay`, 32-codebook RVQ |
| audio tokenizer | [`OpenMOSS-Team/MOSS-Audio-Tokenizer-v2`](https://huggingface.co/OpenMOSS-Team/MOSS-Audio-Tokenizer-v2) — **48 kHz** | [`OpenMOSS-Team/MOSS-Audio-Tokenizer`](https://huggingface.co/OpenMOSS-Team/MOSS-Audio-Tokenizer) — **24 kHz** |
| output | **native 48 kHz** (use raw — no post-processing needed) | 24 kHz (optionally band-width-extended with Sidon) |
| why pick it | higher audio bandwidth out of the box, fewer codebooks to predict per frame, smaller/faster (~0.87 s per 15 s clip at batch 64 on one A100) | larger capacity |

**Off-the-shelf:** this repository contains the fully **merged** weights (bf16). Load and generate;
no adapter handling needed.

## Further fine-tuning (v2)

- **Additional data:** a large corpus of **synthetically generated, Best-of-N-filtered voice-acting
  performances**, self-distilled from the model family — structured natural-language director
  instructions paired with spoken lines, covering fantasy characters, strong emotions, and vocal
  bursts (laughs, gasps, sighs, moans) in **English and German**. No third-party dataset names are
  disclosed.
- **Objective / filtering:** candidates were ranked by a cheap automatic reward (VoiceCLAP-commercial
  embedding → genuineness + vocal-burst-blend + character probes) and only the top takes were kept, so
  the model is trained on its own strongest performances rather than raw generations.
- **Setup:** 8×GPU DDP, **fp32 master weights + 8-bit optimizer** with **bf16 compute** (avoids the
  update-stagnation that pure-bf16 parameter fine-tuning suffers), gradient checkpointing, per-sample
  caption augmentation (randomly dropping the general voice description, the inline stage directions,
  or a fraction of the inline cues/pauses so the model learns to improvise them) and reference-audio
  dropout, linear LR schedule with warmup, channel-wise RVQ loss weighting. Released weights are the
  best checkpoint by cumulative genuineness + vocal-burst-blend on a held-out validation set.

## Requirements

```bash
pip install "transformers>=4.45" torch torchaudio safetensors huggingface_hub
```

The MOSS v2 audio codec (`OpenMOSS-Team/MOSS-Audio-Tokenizer-v2`) is pulled automatically.
~10 GB VRAM (bf16 + codec).

## Prompt format — `GENERAL:` / `SCRIPT:` + plain text

The model was trained on **two fields** per example:

- **`instruction`** = the performance direction, written as **two labelled blocks**:
  - **`GENERAL:`** — the overall voice: age / gender / timbre / mood / delivery. For the most natural
    result, also state that it is a *pristine, high-quality studio recording with no background noise*
    and a *genuine, spontaneous* delivery ("like a real person in a real moment, not acted").
  - **`SCRIPT:`** — the spoken lines **again**, annotated **in position** with `(delivery cues)`, vocal
    bursts such as `(a soft laugh)` / `(gasp)` / `(sigh)`, and `[pause]` markers. The emotional arc can
    change line-by-line here — this is where you *direct* the performance.
- **`text`** = just the **plain spoken words** — no cues, no brackets.

The words appear in **both** fields (plain in `text`, cue-annotated inside the `SCRIPT` block) — this is
intentional and matches the training data. These two strings map directly onto `generate(text=...,
instruction=...)` in the inference example below.

### Exact template

```text
instruction =
GENERAL: <one or two sentences: voice / age / gender / timbre / mood / delivery arc; note "pristine high-quality studio recording, genuine and spontaneous">
SCRIPT:
(cue, cue, ...) first line of dialogue [pause] rest of the line
(cue, cue, ...) second line of dialogue
...

text =
<exactly the same spoken words, plain — no cues, no (), no []>
```

### Example (an emotional arc: warm → shocked → furious)

```text
instruction =
GENERAL: A young man's voice — bright, warm and overjoyed, then it curdles into shocked disbelief and finally erupts into loud, aggressive, disgusted ranting. Completely natural and spontaneous, like a real person in a real moment, not acted. Pristine high-quality studio recording, no background noise.
SCRIPT:
(lighting up, warm, breathless with delight) Oh my god— hey! [pause] Is that really you?
(beaming, affectionate, a soft happy laugh) I can't believe it, look at you!
(the smile fading, confused, voice tightening) ...Wait. What is that?
(erupting, very loud, aggressive, furious and betrayed) You actually did it?! After everything I did for you?!
(ranting fast, seething, disgusted) God, it makes me sick. Get out of my sight.

text =
Oh my god— hey! Is that really you? I can't believe it, look at you! ...Wait. What is that? You actually did it?! After everything I did for you?! God, it makes me sick. Get out of my sight.
```

Tips: keep each `(cue)` short and place it right before the words it affects; put `[pause]` where you
want a real beat; describe *loud/aggressive/whispered* etc. explicitly in the cue to push intensity.
For a live, click-free streaming demo of this exact format, see
[`laion/moss-voice-acting-playground`](https://huggingface.co/laion/moss-voice-acting-playground).


## Inference (complete)

```python
import torch, torchaudio
from transformers import AutoProcessor, AutoModel

REPO = "laion/moss-tts-local-transformer-4.55b-voice-acting-v2"
DEVICE = "cuda"

proc = AutoProcessor.from_pretrained(REPO, trust_remote_code=True,
                                     codec_path="OpenMOSS-Team/MOSS-Audio-Tokenizer-v2")
proc.audio_tokenizer = proc.audio_tokenizer.to(DEVICE).eval()
model = AutoModel.from_pretrained(REPO, trust_remote_code=True,
                                  dtype=torch.bfloat16,
                                  attn_implementation="sdpa").to(DEVICE).eval()

@torch.no_grad()
def generate(text, instruction, language="English", reference_codes=None, n=3):
    kw = dict(text=text, instruction=instruction, language=language)
    if reference_codes is not None:
        kw["reference"] = [torch.tensor(reference_codes, dtype=torch.long)]
    best = None
    for seed in range(n):
        torch.manual_seed(seed)
        batch = proc([[proc.build_user_message(**kw)]], mode="generation")
        out = model.generate(input_ids=batch["input_ids"].to(DEVICE),
                             attention_mask=batch["attention_mask"].to(DEVICE),
                             max_new_tokens=1200, do_sample=True,
                             audio_temperature=1.0, audio_top_p=0.95,
                             audio_top_k=25, audio_repetition_penalty=1.1)
        msg = proc.decode(out)[0]
        if not msg.audio_codes_list:
            continue
        wav = msg.audio_codes_list[0]                    # waveform @ 48 kHz
        if best is None or wav.shape[-1] > best.shape[-1]:
            best = wav
    return best

wav = generate(
    text="You dare enter my domain? Then you shall not leave alive!",
    instruction="As a mighty orc warrior with a deep, guttural, growling voice, "
                "bellow these words with brutal force.",
    language="English")
torchaudio.save("orc.wav", wav.cpu().float(), 48000)
```

Tips (measured on the model family): batch by repeating `input_ids` n× and calling `generate` once
(batch 64 → ~0.87 s/clip on an A100); use **SDPA** (flash-attn 2.x is incompatible with this
remote-code attention); without reference audio use `audio_temperature=0.8`; pass
`tokens ≈ words × 6` (12.5 Hz codec frames) via `build_user_message` to avoid rushed pacing.
Generating **N candidates and keeping the best** (as in `generate(..., n=...)` above) is how the v2
training data itself was produced and is the recommended way to get top-quality takes.

### Optional: clone a reference voice

Pass 12-codebook MOSS codes of a reference clip to steer timbre; keep the instruction for the
delivery (an *empty* instruction gives the highest speaker similarity):

```python
ref_codes = proc.encode_audios_from_path(["my_reference.wav"], n_vq=12)[0]
wav = generate(text="...", instruction="", language="English", reference_codes=ref_codes)
```

## ⚡ Serving with SGLang-Omni (fast inference)

For interactive or **bulk dataset generation**, serve this model with **[SGLang-Omni](https://github.com/sgl-project/sglang)** — an OpenAI-compatible speech server with continuous batching + CUDA graphs (measured on the model family at ~35× realtime for offline data-gen on 1× A100-80GB).

```bash
uv pip install sglang-omni soundfile
hf download laion/moss-tts-local-transformer-4.55b-voice-acting-v2

# NOTE the `env -u LD_LIBRARY_PATH` — without it the FIRST request SIGABRTs with
# `undefined symbol: cudnnGetLibConfig` (a leaked cuDNN path in the stage subprocess).
env -u LD_LIBRARY_PATH CUDA_VISIBLE_DEVICES=0 \
  sgl-omni serve \
    --model-path laion/moss-tts-local-transformer-4.55b-voice-acting-v2 \
    --config examples/configs/moss_tts_local.yaml --port 8000
```

```bash
curl -X POST http://localhost:8000/v1/audio/speech -H "Content-Type: application/json" \
  -d '{"input": "You dare enter my lair?!", "instructions": "A furious ancient dragon, low and booming."}' \
  --output dragon.wav
```

## Notes

- The `text_lm_head` / `audio_lm_heads` "MISSING" note on load is benign weight-tying.
- Same architecture, tokenizer and prompt format as the previous release — you can swap the repo id
  in existing code with no other changes.
- License: **Apache-2.0**.

## Previous version & background

The **v1** release, plus the full experiment write-up (temperature/best-of-N studies, reward
variants, the character-archetype prompt studies and prompting playbook, fast-inference notes and
audio demos), lives here:
[`laion/moss-tts-local-transformer-4.55b-voice-acting`](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting)
· [experiment overview](https://projects.laion.ai/laion-moss-local-1.5-voice-acting-4.55b/overview.html)
· [GitHub](https://github.com/LAION-AI/laion-moss-local-1.5-voice-acting-4.55b).

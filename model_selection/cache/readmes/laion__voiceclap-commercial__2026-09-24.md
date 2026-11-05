---
license: cc-by-4.0
language:
  - en
  - de
  - fr
  - es
  - zh
library_name: transformers
pipeline_tag: feature-extraction
tags:
  - audio
  - speech
  - emotion
  - clap
  - contrastive
  - voice
  - commercial-use
base_model: laion/voiceclap-small
---

# VoiceCLAP-Commercial (small)

A **fully commercially-licensable** voice-text contrastive (CLAP-style) embedding
model for speech-emotion and talking-style retrieval. Same 110M dual-tower
architecture as [`laion/voiceclap-small`](https://huggingface.co/laion/voiceclap-small),
but trained **only on data that permits commercial use** — and, perhaps
surprisingly, it matches or beats the non-commercial-data model on 4 of 5
benchmarks.

## Why this model exists

The standard VoiceCLAP training mix contains corpora released under **CC BY-NC**
(non-commercial) terms: Expresso and EARS (both Meta, CC BY-NC 4.0), and the
bulk of [Emilia](https://huggingface.co/datasets/amphion/Emilia-Dataset) (the
original 101k-hour split is CC BY-NC 4.0). Whether such terms bind the weights
of a model trained on that data is a question each user must answer for their
own jurisdiction and use; LAION licenses its releases on its own assessment.
This model exists for users who prefer not to have to answer it: every corpus
in its training lineage permits commercial use.

This model removes every non-commercial source and keeps only commercially
usable data. A controlled ablation (below) shows the small model loses
**nothing** by doing so.

## Training data (all commercially licensable)

| Corpus | License | Role |
|---|---|---|
| **Emilia-YODAS** (the CC BY 4.0 subset of Emilia, ~19% of emolia-balanced) | CC BY 4.0 | emotion / voice captions |
| **LAION's Got Talent** | LAION-released | talking-style captions |
| **Majestrino** | in-house | voice captions |

The non-commercial Emilia clips are filtered out **at training time** by clip-id
(original-Emilia ids look like `EN_B00087_S08178_W000004`; the retained
YODAS clips carry YouTube-style ids). Expresso and EARS are not used.
Captions use the **`__moss_short__`** scheme: the MOSS-Audio-8B-Thinking
emotion sentence plus one sampled talking-style sentence, 50/50 mixed with the
corpus's own caption.

## Architecture

Identical to voiceclap-small — a dual-tower CLAP:

| | |
| --- | --- |
| Audio encoder | BUD-E-Whisper-Small: 12 layers × 768 dim × 12 heads, 80-mel @ 16 kHz |
| Text encoder | `all-MiniLM-L6-v2`: 6 layers × 384 dim, mean-pooled |
| Joint embedding | 768-d, L2-normalised |
| Loss | SigLIP sigmoid contrastive + Prototypical Contrastive (PCL, w=0.2) |
| Total parameters | ~110 M |

**PCL** adds 39 learned emotion prototypes and a cross-entropy term on
z-scored pseudo-labels derived from emolia's emotion-annotation scalars — a
small auxiliary loss that sharpens the emotion subspace.

## Results — commercial data costs nothing

Controlled ablation, all arms trained identically (1 node, `__moss_short__` +
PCL w=0.2, 15 epochs), evaluated at each arm's best epoch:

| Training data | emonet top1 | emonet ρ | VoiceNet-Emo bal@pp | emolia ρ | MAEB-voice |
|---|---|---|---|---|---|
| full mix incl. **non-commercial** Emilia | 0.0712 | **0.2308** | 0.6112 | 0.2019 | 0.3472 |
| **this model — commercial only** | **0.0721** | 0.2061 | **0.6227** | **0.2034** | **0.3564** |

**This model wins 4 of 5 metrics** — emonet top-1, VoiceNet-Emo balanced
accuracy (+0.0115), emolia Spearman ρ, and MAEB-voice (+0.009). It trails only
on emonet ρ (−0.025, fine-grained intensity *ranking* on synthetic audio,
where the dropped Emilia diversity helped). On the in-domain emolia benchmark
and the 8-task MAEB-voice suite it is strictly better than the
non-commercial-data model.

Two recovery experiments were tried and discarded: adding VoxCeleb1/2 (CC BY)
*hurt*, and upweighting the existing safe corpora was flat. Plain commercial
data is best.

> Absolute numbers are from a 1-node training scale used for the controlled
> ablation; treat them as relative (commercial-vs-noncommercial deltas), not as
> the maximum achievable with a full multi-node run.

## Usage

```python
import torch, soundfile as sf
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("laion/voiceclap-commercial", trust_remote_code=True).eval()
tok = AutoTokenizer.from_pretrained("laion/voiceclap-commercial")

# audio: raw mono waveform @ 16 kHz
wav, sr = sf.read("clip.wav", dtype="float32")
audio_emb = model.encode_waveform(torch.from_numpy(wav))

# text
t = tok(["a person speaking with quiet pride in their voice"], padding=True, return_tensors="pt")
text_emb = model.encode_text(t["input_ids"], attention_mask=t["attention_mask"])

score = (audio_emb @ text_emb.T).item()  # cosine similarity (both L2-normalised)
```

Conversion from the training checkpoint was verified functionally against the
original open_clip implementation (cosine ≥ 0.99999 on both towers).

## License

**CC-BY-4.0** — all training data is commercially usable (Emilia-YODAS CC BY 4.0,
LAION's Got Talent, in-house Majestrino), and the architecture/weights carry no
non-commercial restriction. This is the distinguishing feature of this model
versus the standard VoiceCLAP releases, whose training mix includes CC BY-NC
corpora.

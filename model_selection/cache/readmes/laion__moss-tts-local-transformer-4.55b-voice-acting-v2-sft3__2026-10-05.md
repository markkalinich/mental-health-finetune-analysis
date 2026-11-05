---
license: cc-by-4.0
base_model: laion/moss-tts-local-transformer-4.55b-voice-acting-v2
library_name: transformers
tags: [text-to-speech, expressive-tts, voice-acting, emotion, timed-script]
pipeline_tag: text-to-speech
language: [en, de]
---

# MOSS voice-acting v2 — SFT round 3

A supervised fine-tune of
[`laion/moss-tts-local-transformer-4.55b-voice-acting-v2`](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2)
that adds **explicit control over timing** — per-sentence durations, pauses, and vocal bursts with
their lengths — and **inline delivery directions** that say how to perform each line.

4.13 B trainable parameters: a ~4 B semantic transformer (36 layers), a ~550 M local "talker"
transformer, and 12 audio LM heads over a 12-codebook audio tokenizer at 12.5 frames per second
(one frame = 80 ms).

## What this round changed, measured

Trained on 398,282 rows selected as the strongest examples of each of 40 emotions and each VoiceNet
dimension, 2 epochs, 712 steps on 32 nodes. Evaluated by **generating** 320 clips and scoring them,
not by validation loss — this project has repeatedly seen training metrics point the wrong way.

| | round 2 | **round 3** |
|---|---|---|
| word error rate on direction-carrying prompts | 0.447 | **0.099** |
| duration error, median | 0.100 s | **0.080 s** |
| clips within 0.5 s of the requested length | 92.8 % | **100 %** |
| vocal-burst hit rate | 0.516 | **0.666** |

Round 2 had accidentally dropped the delivery directions its predecessor was trained with, and a
model that has never seen a direction falls apart when given one — word error rate 0.48–0.51 on
such prompts, for *every* round-2 model. Round 3 trained them back in. **Timing control is solved.**

**Emotional intensity is not.** Asked for percentile 0.90–0.98 of a named emotion, this model
reaches about 0.35. Several objectives were tried against that — GRPO with a group-relative reward,
DPO with contrastive pairs, DPO with symmetric instruction-conditioned pairs — and none moved it.
The emotion adapters below are the only thing that has, and even they are not selective enough to
merge in blindly. This is documented honestly in the technical report.

## Inference

```python
import torch, torchaudio
from transformers import AutoProcessor, AutoModel

BASE = "laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft3"

proc = AutoProcessor.from_pretrained(BASE, trust_remote_code=True)
model = AutoModel.from_pretrained(BASE, trust_remote_code=True,
                                  dtype=torch.bfloat16, attn_implementation="sdpa").cuda().eval()

prompt = open("prompt.txt").read()          # the <user_inst> block, see "How to prompt" below
um = {"role": "user", "content": prompt, "audio_codes_list": []}
b = proc([[um]], mode="generation")

with torch.no_grad():
    out = model.generate(input_ids=b["input_ids"].cuda(),
                         attention_mask=b["attention_mask"].cuda(),
                         max_new_frames=340, do_sample=True,
                         audio_temperature=1.0, audio_top_p=0.95, audio_top_k=50,
                         audio_repetition_penalty=1.0)

# codes -> waveform. Use the processor's own decoder: calling the audio tokenizer directly, or
# reshaping its output, yields a two-channel result that flattens into audio at HALF SPEED and
# still sounds like speech. This project lost a whole corpus to that once.
wav = proc.decode_audio_codes([out_codes], return_stereo=False)[0].reshape(-1).float().cpu()
torchaudio.save("out.flac", wav[None], int(proc.model_config.sampling_rate), format="flac")
```

### Loading adapters

```python
from peft import PeftModel

# one adapter
model = PeftModel.from_pretrained(model, "laion/moss-va-sft3-dpo-lora")

# several, each with its own weight -- the usual case: identity from a voice adapter,
# affect from an emotion adapter, general quality from the DPO adapter.
#
# NOTE: `add_weighted_adapter(..., combination_type="linear")` does NOT work here. It raises
# `ValueError: All adapters must have the same r value`, because the DPO adapter is rank 64 and
# the voice / emotion adapters are rank 16. Activate them together instead and scale each one.
model = PeftModel.from_pretrained(model, "<dpo adapter path>", adapter_name="dpo")
model.load_adapter("<voice adapter path>", adapter_name="voice")
model.load_adapter("<emotion adapter path>", adapter_name="emo")

names = ["dpo", "voice", "emo"]
weights = {"dpo": 1.0, "voice": 1.0, "emo": 1.5}     # 1.5 for emotion is the measured optimum
model.base_model.set_adapter(names)                  # the TUNER takes a list; PeftModel does not
model.active_adapter = names[0]                      # must stay a str or generate() indexes a list

for mod in model.modules():
    sc = getattr(mod, "scaling", None)
    if isinstance(sc, dict):
        if not hasattr(mod, "_base_scaling"):
            mod._base_scaling = dict(sc)
        for k in sc:
            if k in weights:
                sc[k] = mod._base_scaling[k] * weights[k]
```

### Scaling an adapter without re-merging

A LoRA layer computes `h + scaling · B(A(x))`, so multiplying the stored `scaling` **is** the merge
weight — exact and reversible:

```python
def set_lora_scale(model, w):
    for mod in model.modules():
        sc = getattr(mod, "scaling", None)
        if isinstance(sc, dict):
            if not hasattr(mod, "_base_scaling"):
                mod._base_scaling = dict(sc)
            for k in sc:
                sc[k] = mod._base_scaling[k] * w
```
## How to prompt this model

Every request is one `<user_inst>` block. The fields are fixed — none may be added or removed:

```
<user_inst>
- Reference(s):
{None | Speaker: <name> | <|audio|>}
- Instruction:
{GENERAL: ... and/or SCRIPT: ...}
- Tokens:
{target length in audio frames}
- Quality:
None
- Sound Event:
None
- Ambient Sound:
None
- Language:
{English | German}
- Text:
{the same script as under SCRIPT:, character for character}
</user_inst>
```

| Field | What goes in it |
|---|---|
| `Reference(s)` | `<\|audio\|>` when a reference recording of the target voice is attached, `Speaker: <name>` when only a voice name is known, otherwise `None`. |
| `Instruction` | A `GENERAL:` line, a `SCRIPT:` block, or both. |
| `Tokens` | Target length in audio frames. The tokenizer runs at **12.5 frames per second**, so 12.8 s = 160 frames. This is the length budget and the numbers in the script must add up to it. |
| `Quality`, `Sound Event`, `Ambient Sound` | Always `None`. Kept so the field layout matches the base model. |
| `Language` | `English` or `German`. |
| `Text` | The rendered script, byte-identical to the `SCRIPT:` block. |

### `GENERAL:` — who is speaking

Prose describing the voice and the clip: age and gender, energy and pace, tension, timbre, clarity,
pitch range, breath, affect, which emotions are audible, style, recording quality.

```
GENERAL: A young adult masculine voice; delivery is normally alert, brisk, neutral tension;
timbre is neutral-toned, fairly smooth; average clarity, wide pitch range, light breath;
affect is mildly positive, slightly dominant; reads as bitterness, contempt; 9.5s, EN.
```

The phrase `reads as …` is where the emotion names live.

### `SCRIPT:` — what to say, when, and how

Four kinds of tag, told apart **by their brackets**:

| Tag | Means | Rule |
|---|---|---|
| `[3.9 seconds duration]` | the next sentence must take this long | square brackets, stands **before** the text, one per speech segment |
| `[0.8 seconds pause]` | silence of this length | square brackets; every gap of 0.2 s or more, including before the first word and after the last |
| `(contented sigh, 0.2 seconds)` | a non-speech vocalisation of this length | round brackets **with** a duration — label first, then the seconds |
| `(clearly amused, warm and open, unguarded)` | how to perform the next sentence | round brackets **without** a duration, stands before the duration tag |

**The disambiguation rule in one line:** square bracket = a number of seconds; round bracket *with* a
number = a vocal burst; round bracket *without* a number = a delivery direction. That is the only
thing separating a burst from a direction, which is why directions never carry a number.

A complete example:

```
<user_inst>
- Reference(s):
None
- Instruction:
GENERAL: A young adult feminine voice, warm and conversational; reads as amusement; 6.0s, EN.
SCRIPT:
[0.4 seconds pause] (intensely amused: letting it out / not hiding it, warm and open,
unguarded; bright, relaxed) [2.4 seconds duration] You are not going to believe this.
[0.3 seconds pause] (breathy giggle, 0.4 seconds) [0.2 seconds pause] (still intensely amused)
[2.3 seconds duration] He actually wore it to the wedding.
- Tokens:
75
- Quality:
None
- Sound Event:
None
- Ambient Sound:
None
- Language:
English
- Text:
[0.4 seconds pause] (intensely amused: letting it out / not hiding it, warm and open,
unguarded; bright, relaxed) [2.4 seconds duration] You are not going to believe this.
[0.3 seconds pause] (breathy giggle, 0.4 seconds) [0.2 seconds pause] (still intensely amused)
[2.3 seconds duration] He actually wore it to the wedding.
</user_inst>
```

0.4 + 2.4 + 0.3 + 0.4 + 0.2 + 2.3 = 6.0 s = 75 frames. **If the numbers do not add up to the token
budget the model has to choose which to honour**, and length control is the thing it honours best.

### Segmentation rules the training data followed

* split at sentence ends (`.` `!` `?` `…`) and at every vocal burst;
* any segment still longer than **12 s** is split again at its largest internal gap;
* a duration is measured from the first word onset to the last word offset of that segment, so two
  sentences of 12 s and 8 s produce `[12.0 seconds duration]` and `[8.0 seconds duration]`, never a
  single `[20.0 seconds duration]`;
* gaps below **0.20 s** are folded into the neighbouring speech instead of being printed, so the
  printed numbers still add up;
* a burst that overlaps speech prints only the part that does not overlap.

### Vocal-burst labels that actually occur in training

`low mumble`, `ahem`, `contented sigh`, `surprised gasp`, `chuckle`, `breathy giggle`,
`childlike giggle`, `wistful sigh`, `exhausted groan`, `sharp inhale`, `resonant hum`, `scream`,
`yawn`, `deep breath`, `soft hum`, `exasperated sigh`, `cackle`, `shriek`, `coughing`,
`mournful wail`, `growl`, `purr`.

Realistic lengths: median **0.28 s**, 10th percentile 0.14 s, 90th percentile 0.48 s, longest
observed 2.46 s. A sigh requested at 3 s is outside anything in the data.

### Intensity bands

Delivery directions carry an intensity adverb drawn from the percentile band of the requested
emotion. The same cutoffs are used by the training data, the reward and the evaluation:

| band | percentile | adverbs |
|---|---|---|
| faint | 0.40 – 0.70 | barely, faintly, only slightly, just a little |
| moderate | 0.70 – 0.90 | clearly, plainly, noticeably, unmistakably |
| intense | 0.90 – 0.98 | strongly, intensely, very, deeply |
| extreme | 0.98 – 1.00 | overwhelmingly, extremely, utterly, completely |

## The family

| | |
|---|---|
| 🧩 **Base model (required by every adapter here)** | [`laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft3`](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft3) |
| 🎚️ **Preference-tuning adapter** | [`laion/moss-va-sft3-dpo-lora`](https://huggingface.co/laion/moss-va-sft3-dpo-lora) |
| 🎭 **40 emotion adapters** | [`laion/moss-va-sft3-emotion-loras`](https://huggingface.co/laion/moss-va-sft3-emotion-loras) |
| 🗣️ **500 voice adapters** | [`laion/moss-va-sft3-voice-loras`](https://huggingface.co/laion/moss-va-sft3-voice-loras) |
| 🔊 **Listening page — nine models on the same 80 prompts, with ASR transcripts** | [laion/moss-va-sft3-samples](https://huggingface.co/spaces/laion/moss-va-sft3-samples) |
| 🔬 **Emotion adapters vs baseline, matched and neutral prompts** | [laion/moss-va-emotion-loras](https://huggingface.co/spaces/laion/moss-va-emotion-loras) |
| 🧪 **Four-factor study — what actually drives the emotion score** | [laion/moss-va-four-factor-study](https://huggingface.co/spaces/laion/moss-va-four-factor-study) |
| 📄 **Technical report** | [laion/moss-va-technical-report](https://huggingface.co/spaces/laion/moss-va-technical-report) |
| 📖 **Voice-acting manual (v2 model)** | [projects.laion.ai/moss-voiceacting-manual](https://projects.laion.ai/moss-voiceacting-manual/site/index.html) |
| ⬅️ **Predecessors** | [voice-acting-v2](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2) · [-sft](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft) · [-sft-dpo](https://huggingface.co/laion/moss-tts-local-transformer-4.55b-voice-acting-v2-sft-dpo) |

## Citation and provenance

Derived from MOSS-TTSD / MOSS local-transformer 1.5. Training data: LAION voice profiles plus
public real-speech corpora (EmoLia, Kartoffelphon, MLS). Released CC-BY-4.0.

<!-- recipes-and-prompting -->

## Recipes, prompting and the rest of the stack

This is the base model the adapter sets below are trained against. What you can ask it for, and at what weight, is written down rather than left to trial and error.

### Where the recipes live

| | |
|---|---|
| **Recipes** — per class: which adapter, what weight, which prompt form, measured hit rate, how many candidates to draw | [`wikiskills/`](https://github.com/LAION-AI/Humaneness-Voice-Demo-Server/tree/main/wikiskills) · summary table in [`VOCAL_BURSTS.md`](https://github.com/LAION-AI/Humaneness-Voice-Demo-Server/blob/main/wikiskills/VOCAL_BURSTS.md) |
| **Prompting guide** — the contract the directing language model follows | [`docs/DIRECTOR.md`](https://github.com/LAION-AI/Humaneness-Voice-Demo-Server/blob/main/docs/DIRECTOR.md) |
| **How adapters are merged** — and why not through PEFT at batch 1 | [`docs/ADAPTERS.md`](https://github.com/LAION-AI/Humaneness-Voice-Demo-Server/blob/main/docs/ADAPTERS.md) |
| **How the whole system fits together** | [`docs/ENSEMBLE.md`](https://github.com/LAION-AI/Humaneness-Voice-Demo-Server/blob/main/docs/ENSEMBLE.md) |

### Writing the cue

Brackets carry meaning in this format, and two rules catch nearly everyone out.

| you write | the model hears |
|---|---|
| `(chuckle)` | **a sound** — a vocal burst, given its own slot in the timing |
| `(clearly amused, warm and open)` | **an instruction** for how to say the next sentence |
| `(clearly amused, with a small chuckle)` | an instruction, and **no chuckle happens** |
| `(quietly, 2 seconds)` | a **sound**, not an instruction — a round bracket containing a number stops being a direction |
| `[pause]` | a beat of silence |

**Cues are always written in English, even when the spoken line is German.** This is how the
training corpus is written — German rows read
`Das zerreißt einen einfach, weißt du? (relief sigh)` — so a German cue is out of distribution.

**Never write a number inside a bracket.** The durations are computed for you and inserted
afterwards: `[N.N seconds duration]` before each speech segment, `[N.N seconds pause]` for gaps,
`(label, N.N seconds)` for each burst, summed at 12.5 frames per second.

<!-- /recipes-and-prompting -->

---
license: cc-by-nc-4.0
language:
- en
library_name: transformers
pipeline_tag: text-to-speech
base_model: OpenMOSS-Team/MOSS-TTS-Local-Transformer
datasets:
- skit-ai/emotion-tts
tags:
- text-to-speech
- tts
- speech-synthesis
- emotion
- emotional-tts
- expressive-tts
- controllable
- indian-english
- indian-accent
- voice-agent
- moss-tts
- lora
- audio
---

# Roxi-TTS Emotion (1.7B): controllable emotional Indian-English text-to-speech

Roxi-TTS Emotion is a 1.7B text-to-speech model that speaks Indian-English in eight
selectable emotions from a single, consistent voice. You choose the emotion per sentence
with a short text instruction, so the same speaker can sound happy, sad, angry, excited,
calm, apologetic, fearful, or neutral.

> Non-commercial. This model was trained on the Skit-AI Emotional TTS dataset, which is
> licensed CC BY-NC 4.0. The model is therefore released under CC BY-NC 4.0 and must not be
> used for commercial purposes. For commercial use, obtain a license from Skit-AI.

## Why Roxi-TTS Emotion

- Eight emotions from one voice: neutral, happy, sad, angry, excited, calm, apologetic, fear.
- Controllable by instruction, no separate model per emotion.
- One consistent speaker across all emotions: 0.958 speaker similarity (WavLM-SV).
- Measurably expressive: 2.1x spread in pitch variation across the eight emotions.
- Natural Indian-English accent, 24 kHz output.

## Emotions and how to steer

Set the instruction field to one of the following:

| Emotion | Instruction |
|---|---|
| neutral | Speak in a neutral, clear, conversational Indian-English style. |
| happy | Speak in a happy, cheerful, warm tone, in a clear Indian-English style. |
| sad | Speak in a sad, downcast, sorrowful tone, in a clear Indian-English style. |
| angry | Speak in an angry, irritated, forceful tone, in a clear Indian-English style. |
| excited | Speak in an excited, high-energy, enthusiastic tone, in a clear Indian-English style. |
| calm | Speak in a calm, relaxed, soothing tone, in a clear Indian-English style. |
| apologetic | Speak in an apologetic, regretful, gentle tone, in a clear Indian-English style. |
| fear | Speak in a fearful, anxious, worried tone, in a clear Indian-English style. |

## Quick facts

| Field | Value |
|---|---|
| Base model | OpenMOSS-Team/MOSS-TTS-Local-Transformer (1.7B, Apache-2.0) |
| Audio tokenizer | OpenMOSS-Team/MOSS-Audio-Tokenizer (Apache-2.0) |
| Method | LoRA (PEFT), r=16, alpha=32, merged into the base weights |
| Training data | Skit-AI Emotional TTS, single Indian-English female speaker, 8 emotions, about 2825 clips |
| Output | 24 kHz mono |
| Voice consistency | 0.958 speaker similarity across emotions (WavLM-SV) |
| Emotion range | 2.1x pitch-variation spread across the eight emotions |
| Speed | Real-time factor about 2.5 on a 16 GB GPU, not real-time |

## Install

Built for transformers 4.57.1. Install the MOSS-TTS repository so the model class is importable.

```bash
pip install "transformers==4.57.1" torch torchaudio soundfile librosa peft
git clone https://github.com/OpenMOSS/MOSS-TTS.git
```

## Quick start

```python
import sys, torch, soundfile as sf
sys.path.insert(0, "MOSS-TTS")
from transformers import AutoProcessor
from moss_tts_local.modeling_moss_tts import MossTTSDelayModel

repo = "IOTEverythin/roxi-tts-emotion"
device = "cuda" if torch.cuda.is_available() else "cpu"
dtype = torch.bfloat16 if device == "cuda" else torch.float32

processor = AutoProcessor.from_pretrained(repo, trust_remote_code=True)
processor.audio_tokenizer = processor.audio_tokenizer.to(device)
model = MossTTSDelayModel.from_pretrained(repo, torch_dtype=dtype, attn_implementation="sdpa").to(device).eval()

text = "I just heard the news about the meeting tomorrow."
instruction = "Speak in an excited, high-energy, enthusiastic tone, in a clear Indian-English style."

conv = [[processor.build_user_message(text=text, instruction=instruction)]]
batch = processor(conv, mode="generation")
out = model.generate(
    input_ids=batch["input_ids"].to(device),
    attention_mask=batch["attention_mask"].to(device),
    max_new_tokens=4096, do_sample=True, temperature=0.9,
)
audio = processor.decode(out)[0].audio_codes_list[0]
sf.write("out.wav", audio.float().cpu().numpy(), processor.model_config.sampling_rate)
```

Swap the instruction to change the emotion. Generation is autoregressive and can
under-generate, so if a clip is short, generate a few times and keep the longest, then trim
silence. Keep sentences to about twelve words.

## Limitations

- Non-commercial license (see below).
- Not real-time on a single consumer GPU.
- Eight emotions. Surprise is excluded because the source had no audio for it.
- Emotion is set per sentence through the instruction, not through inline tags inside a sentence.
- Requires transformers 4.57.1.

## License and attribution

Released under CC BY-NC 4.0 (non-commercial). Built on MOSS-TTS-Local-Transformer (Apache-2.0)
and the MOSS Audio Tokenizer (Apache-2.0). The emotion control is learned from the Skit-AI
Emotional TTS dataset (https://github.com/skit-ai/emotion-tts-dataset), which is licensed
CC BY-NC 4.0, copyright Skit.ai. Because the training data is non-commercial, this derivative
model is non-commercial as well.

## Responsible use

This voice is derived from a real dataset speaker. Do not use it to impersonate real people
or for fraud, social engineering, or deception. Disclose AI-generated audio where required by
law or policy. Provided as is, without warranty.

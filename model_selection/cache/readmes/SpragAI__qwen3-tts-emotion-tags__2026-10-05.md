---
license: apache-2.0
base_model: Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice
pipeline_tag: text-to-speech
library_name: transformers
language:
- en
tags:
- text-to-speech
- emotion
- expressive-tts
- lora
---

# Qwen3-TTS with Emotion Tags

This finetune provides inline delivery control for the nine Qwen3-TTS CustomVoice presets facilitating
emotion controls directly from the transcript.

```
[Angry] I told them the whole story last night, and now everyone knows what happened.
```

It covers nine emotion tags across all nine preset voices, with the speaker embeddings left
**bit-identical to the base model** meaning the source voice remains unchanged.

**Tags** `[Angry] [Sad] [Happy] [Fast] [Gentle] [Tired] [Fearful] [Disgusted] [Surprised]`

**Voices** `aiden`, `dylan`, `eric`, `ono_anna`, `ryan`, `serena`, `sohee` `uncle_fu` `vivian`

## Usage

```bash
pip install qwen-tts
```

```python
import soundfile as sf
import torch
from qwen_tts import Qwen3TTSModel

model = Qwen3TTSModel.from_pretrained(
    "SpragAI/qwen3-tts-emotion-tags",
    dtype=torch.bfloat16,
    attn_implementation="sdpa",
    device_map="cuda:0",
)

wav, sr = model.generate_custom_voice(
    text="[Sad] None of it ever happened in the end.",
    speaker="ryan", language="Auto")
sf.write("out.wav", wav[0], sr)
```


## Samples

> I told them the whole story last night, and now everyone knows what happened.

<audio controls src="https://huggingface.co/SpragAI/qwen3-tts-emotion-tags/resolve/main/samples/01_neutral.wav"></audio> no tag (reference)  

<audio controls src="https://huggingface.co/SpragAI/qwen3-tts-emotion-tags/resolve/main/samples/02_angry.wav"></audio> `[Angry]`  

<audio controls src="https://huggingface.co/SpragAI/qwen3-tts-emotion-tags/resolve/main/samples/03_sad.wav"></audio> `[Sad]`  

<audio controls src="https://huggingface.co/SpragAI/qwen3-tts-emotion-tags/resolve/main/samples/04_happy.wav"></audio> `[Happy]`  

<audio controls src="https://huggingface.co/SpragAI/qwen3-tts-emotion-tags/resolve/main/samples/06_fast.wav"></audio> `[Fast]`  

<audio controls src="https://huggingface.co/SpragAI/qwen3-tts-emotion-tags/resolve/main/samples/07_gentle.wav"></audio> `[Gentle]`  

<audio controls src="https://huggingface.co/SpragAI/qwen3-tts-emotion-tags/resolve/main/samples/08_tired.wav"></audio> `[Tired]`  

<audio controls src="https://huggingface.co/SpragAI/qwen3-tts-emotion-tags/resolve/main/samples/09_fearful.wav"></audio> `[Fearful]`  

<audio controls src="https://huggingface.co/SpragAI/qwen3-tts-emotion-tags/resolve/main/samples/10_disgusted.wav"></audio> `[Disgusted]`  

<audio controls src="https://huggingface.co/SpragAI/qwen3-tts-emotion-tags/resolve/main/samples/11_surprised.wav"></audio> `[Surprised]`  



## Limitations

- **Single utterance tags.** A tag conditions the whole utterance wherever it appears. 
- **English only.** Other languages may work but were not included in the training corpus.
  

## Training

| | |
|---|---|
| base | `Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice` |
| method | LoRA r=32, alpha=64, dropout 0.05 |
| targets | `q,k,v,o,gate,up,down_proj` (talker body) |
| also trainable | the 15 `code_predictor` codec input embeddings |
| frozen | `code_predictor` network, `codec_embedding` (speaker rows preserved) |
| optimiser | Prodigy, d_coef 1.0, batch 4, 3 epochs |
| corpus | 76862 rows, 9 speakers, 9 tags, 16.7% with an explicit English prefix |



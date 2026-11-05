---
license: cc-by-4.0
language:
- en
- multilingual
tags:
- audio
- whisper
- captioning
- audio-captioning
- speech
- voice
- timbre
- emotion
library_name: transformers
pipeline_tag: automatic-speech-recognition
base_model: laion/BUD-E-Whisper_V1.1
datasets:
- TTS-AGI/majestrino-unified-detailed-captions-temporal
---

# BUD-E-Whisper V1.2

**Detailed audio captioning model** that generates rich, temporal descriptions of speech audio — including voice characteristics, emotional states, recording quality, speaker demographics, and delivery style.

Fine-tuned from [laion/BUD-E-Whisper_V1.1](https://huggingface.co/laion/BUD-E-Whisper_V1.1) on the [majestrino-unified-detailed-captions-temporal](https://huggingface.co/datasets/TTS-AGI/majestrino-unified-detailed-captions-temporal) dataset.

## Model Details

- **Architecture**: Whisper Small (encoder-decoder, 242M parameters)
- **Base model**: `laion/BUD-E-Whisper_V1.1` (itself fine-tuned from `openai/whisper-small`)
- **Training data**: ~9M samples from `TTS-AGI/majestrino-unified-detailed-captions-temporal` (826 webdataset shards)
- **Training**: 2x RTX 3090, DDP (gloo), fp16 mixed precision, AdamW (lr=1e-5, linear warmup 5%), batch size 20
- **Final validation loss**: 0.81

## What it outputs

Given an audio clip (up to 30 seconds), the model generates detailed captions describing:

- **Speaker demographics**: age range, gender, accent
- **Voice timbre**: pitch, brightness, breathiness, nasality, resonance
- **Emotional state**: valence, arousal, dominance, specific emotions
- **Delivery style**: tempo, fluency, expressiveness, naturalness
- **Recording quality**: background noise, clarity, studio vs. field
- **Temporal aspects**: how delivery and emotion change over time

## Quick Start

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torchaudio
import torch

# Load model
processor = WhisperProcessor.from_pretrained("laion/BUD-E-Whisper_V1.2")
model = WhisperForConditionalGeneration.from_pretrained("laion/BUD-E-Whisper_V1.2")
model.generation_config.forced_decoder_ids = None
model.eval().to("cuda")

# Load audio (resample to 16kHz mono)
wav, sr = torchaudio.load("audio.wav")
if wav.shape[0] > 1:
    wav = wav.mean(dim=0, keepdim=True)
if sr != 16000:
    wav = torchaudio.functional.resample(wav, sr, 16000)
audio = wav.squeeze(0).numpy()

# Generate caption
inputs = processor.feature_extractor(audio, sampling_rate=16000, return_tensors="pt").to("cuda")
with torch.no_grad():
    generated_ids = model.generate(**inputs, max_length=448)
caption = processor.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
print(caption)
```

## CLI Inference

```bash
python inference.py audio.wav
python inference.py audio.mp3 --device cpu
```

## Example Output

**Input**: A 5-second clip of a male speaker reading a sentence.

**Output**:
> This recording features a clearly masculine adult male speaker delivering a narration with a strong sense of interest and concentration, occasionally exhibiting a hint of contemplation. The overall emotional valence remains neutral, with a slightly calm arousal level throughout. The speaker's demeanor is balanced, displaying a moderate degree of vulnerability alongside a subtle confidence. The vocal delivery is consistently natural and spontaneous, characterized by a neutral pitch and volume, and a smooth, clear timbre with minimal breathiness.

## Training Details

| Parameter | Value |
|---|---|
| Base model | `laion/BUD-E-Whisper_V1.1` |
| Dataset | `TTS-AGI/majestrino-unified-detailed-captions-temporal` |
| Samples trained | ~9M |
| Batch size | 10 per GPU x 2 GPUs = 20 |
| Learning rate | 1e-5 (linear warmup 5%, linear decay) |
| Precision | fp16 mixed |
| Max audio length | 30 seconds |
| Max label tokens | 448 |
| Hardware | 2x NVIDIA RTX 3090 |

### Validation Loss Progression

| Samples | Val Loss |
|---|---|
| 200 | 3.69 |
| 1M | 0.94 |
| 2M | 0.90 |
| 3M | 0.87 |
| 4M | 0.85 |
| 5M | 0.84 |
| 6M | 0.83 |
| 7M | 0.82 |
| 8M | 0.81 |
| 9M | 0.81 |

## Limitations

- Optimized for speech audio; may produce less meaningful captions for music or environmental sounds
- Maximum input length is 30 seconds
- English-centric training data, though it can handle some other languages (e.g., German)
- May occasionally hallucinate speaker gender or specific emotional states

## Citation

```bibtex
@misc{bud-e-whisper-v1.2,
  title={BUD-E-Whisper V1.2: Detailed Audio Captioning},
  author={LAION},
  year={2026},
  url={https://huggingface.co/laion/BUD-E-Whisper_V1.2}
}
```

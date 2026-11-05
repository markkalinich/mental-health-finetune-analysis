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
base_model: laion/BUD-E-Whisper_V1.2
datasets:
- TTS-AGI/majestrino-unified-detailed-captions-temporal
- TTS-AGI/balanced-emotion-dataset-majestrino-withtemporal-detailed-captions
---

# BUD-E-Whisper V1.21

**Detailed audio captioning model** that generates rich, temporal descriptions of speech audio — including voice characteristics, emotional states, recording quality, speaker demographics, and delivery style.

This model is fine-tuned from [laion/BUD-E-Whisper_V1.2](https://huggingface.co/laion/BUD-E-Whisper_V1.2) with an additional 2-epoch training pass on an **emotion-balanced** subset of the training data, specifically designed to improve coverage of rare emotional states.

## Comparison with V1.2

V1.21 scores slightly lower than V1.2 on automated Gemini 3.1 Pro evaluation benchmarks (grand average 2.60 vs 2.73 across 6 dimensions), but **captions appear subjectively to be somewhat better** — particularly for audio with complex or uncommon emotional content. The automated evaluation's validation set is dominated by common emotions (Interest, Contentment, Contemplation), which biases the benchmark toward models trained on the natural distribution. V1.21 trades some accuracy on these common cases for improved handling of rare emotions like jealousy, infatuation, intoxication, shame, and pain.

## Training History

This model was produced through a multi-stage fine-tuning pipeline. We explored several approaches:

| Model | Base | Training Data | Epochs | LR | Val Loss | Gemini Grand Avg |
|---|---|---|---|---|---|---|
| [BUD-E-Whisper V1.0](https://huggingface.co/laion/BUD-E-Whisper) | whisper-small | proprietary | - | - | - | 2.13 |
| [BUD-E-Whisper V1.1](https://huggingface.co/laion/BUD-E-Whisper_V1.1) | V1.0 | proprietary | - | - | - | 2.41 |
| V1.0 FT (1 epoch) | V1.0 | majestrino-temporal (full) | 1 | 1e-5 | 0.848 | 2.58 |
| **[BUD-E-Whisper V1.2](https://huggingface.co/laion/BUD-E-Whisper_V1.2)** | V1.1 | majestrino-temporal (full) | ~2 | 1e-5 | **0.811** | **2.73** |
| V1.2 + balanced (1e-5) | V1.2 | balanced emotions (520K) | 2 | 1e-5 | 0.817 | 2.57 |
| **V1.21 (this model)** | V1.2 | balanced emotions (520K) | 2 | 5e-6 | **0.814** | **2.60** |

### Detailed Gemini 3.1 Pro Evaluation (100 samples)

| Dimension | V1.0 | V1.1 | V1.0 FT | V1.2 | V1.2+bal 1e-5 | V1.21 |
|---|---:|---:|---:|---:|---:|---:|
| Timbre | 1.11 | 2.63 | 2.98 | **3.14** | 2.94 | 3.08 |
| Emotion | **3.76** | 2.90 | 2.51 | 2.62 | 2.35 | 2.31 |
| Style | 1.76 | 2.65 | 2.89 | **2.98** | 2.86 | 2.78 |
| Recording Quality | 3.43 | **3.54** | 3.25 | 3.37 | 3.54 | 3.44 |
| Temporal | 0.27 | 0.51 | 1.74 | **1.99** | 1.60 | 1.76 |
| Overall | **2.43** | 2.23 | 2.10 | 2.28 | 2.11 | 2.21 |
| **Grand Average** | 2.13 | 2.41 | 2.58 | **2.73** | 2.57 | 2.60 |

### Balanced Emotion Dataset

The second-stage training uses [TTS-AGI/balanced-emotion-dataset-majestrino-withtemporal-detailed-captions](https://huggingface.co/datasets/TTS-AGI/balanced-emotion-dataset-majestrino-withtemporal-detailed-captions), a curated subset of 482,594 samples balanced across 40 emotion categories (12,997 samples each). Categories range from common (Interest, Contentment) to rare (Intoxication, Sexual Lust, Jealousy). The balancing was done via keyword matching on captions, with samples drawn from diverse source shards.

The 40 emotion categories:
Amusement, Elation, Pleasure/Ecstasy, Contentment, Thankfulness/Gratitude, Affection, Infatuation, Hope/Optimism, Triumph, Pride, Interest, Awe, Astonishment/Surprise, Concentration, Contemplation, Relief, Longing, Teasing, Impatience/Irritability, Sexual Lust, Doubt, Fear, Distress, Confusion, Embarrassment, Shame, Disappointment, Sadness, Bitterness, Contempt, Disgust, Anger, Malevolence/Malice, Sourness, Pain, Helplessness, Fatigue/Exhaustion, Emotional Numbness, Intoxication/Altered States, Jealousy/Envy.

## Model Details

- **Architecture**: Whisper Small (encoder-decoder, 242M parameters)
- **Base model**: `laion/BUD-E-Whisper_V1.2` (V1.1 fine-tuned on majestrino temporal captions)
- **Stage 2 data**: 482,594 balanced emotion samples (2 epochs = ~965K samples seen)
- **Training**: 2x RTX 3090, DDP (gloo), fp16, AdamW (lr=5e-6, cosine schedule, 5% warmup)
- **Final validation loss**: 0.814

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
processor = WhisperProcessor.from_pretrained("laion/BUD-E-Whisper_V1.21")
model = WhisperForConditionalGeneration.from_pretrained("laion/BUD-E-Whisper_V1.21")
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

## Limitations

- Optimized for speech audio; may produce less meaningful captions for music or environmental sounds
- Maximum input length is 30 seconds
- English-centric training data, though it can handle some other languages
- May occasionally hallucinate speaker gender or specific emotional states
- Slightly lower benchmark scores than V1.2 on common-emotion validation samples

## Citation

```bibtex
@misc{bud-e-whisper-v1.21,
  title={BUD-E-Whisper V1.21: Emotion-Balanced Audio Captioning},
  author={LAION},
  year={2026},
  url={https://huggingface.co/laion/BUD-E-Whisper_V1.21}
}
```

---
base_model:
- Qwen/Qwen3-TTS-12Hz-1.7B-Base
- Qwen/Qwen3-1.7B
language:
- ko
- en
- ja
- zh
- de
- fr
- ru
- pt
- es
- it
license: apache-2.0
pipeline_tag: text-to-speech
tags:
- tts
- text-to-speech
- darwin
- cross-modal
- ffn-blending
- model-merging
- qwen3
- voice-cloning
- emotion
- vidraft
project_page: https://vidraft.nwr
---

> ### 📱 Run it on your phone or a GPU-less PC → **POCKET**  ·  🚀 **[Try it live (CPU chat)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU)**
> VIDRAFT's on-device family: a 35B model that runs on **iPhone** and on **CPU with no GPU** — stock `llama.cpp`, no fork.
>
> [![Live demo](https://img.shields.io/badge/🤗_Space-POCKET_CPU_chat-ffce3a)](https://huggingface.co/spaces/FINAL-Bench/POCKET-35B-CPU) [![Collection](https://img.shields.io/badge/📚-POCKET_collection-5dbf9a)](https://huggingface.co/collections/FINAL-Bench/pocket-models-6a618ee5d23eafb7e185a5c6) [![35B](https://img.shields.io/badge/POCKET--35B-GGUF-243456)](https://huggingface.co/FINAL-Bench/POCKET-35B-GGUF) [![KR MLX](https://img.shields.io/badge/POCKET--KR-iPhone-0f6e56)](https://huggingface.co/FINAL-Bench/POCKET-KR-MLX) [![EN](https://img.shields.io/badge/POCKET--EN-GGUF-185fa5)](https://huggingface.co/FINAL-Bench/POCKET-EN-GGUF)

>


# 🧬 Darwin-TTS-1.7B-Cross

**World's first cross-modal FFN transfer from LLM to TTS — emotion-enhanced speech synthesis without any training.**

This model is a cross-modal application of the Darwin Family framework, introduced in the paper: [Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning](https://huggingface.co/papers/2605.14386).

**Authors:** Taebong Kim, Youngsik Hong, Minsik Kim, Sunyoung Choi, Jaewon Jang, Junghoon Shin, Minseo Kim.

> Darwin-TTS blends 3% of [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) (LLM) FFN weights into [Qwen3-TTS-1.7B](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) (TTS) talker module. No training, no data, no GPU hours — just weight-space arithmetic.

## Key Discovery

| Blend (α) | Emotion | Quality | Status |
|-----------|---------|---------|--------|
| 0% | Baseline | Normal | Original Qwen3-TTS |
| 1% | No change | Normal | Too subtle |
| **3%** | **Emotion appears** | **Normal** | **★ This model (default)** |
| 5% | Emotion intensified | Normal | ★★ Max stable |
| 10% | Broken | Failed | Infinite generation |

## Why It Works

Qwen3-1.7B (LLM) and Qwen3-TTS-1.7B's talker share **100% identical architecture**:

```
                    Qwen3-1.7B (LLM)    Qwen3-TTS talker    Match
hidden_size         2048                 2048                ✅
intermediate_size   6144                 6144                ✅
num_hidden_layers   28                   28                  ✅
num_attention_heads 16                   16                  ✅
num_key_value_heads 8                    8                   ✅
```

This means **zero SVD, zero truncation, zero layer mapping** — pure 1:1 lerp blending across all 84 FFN tensors (gate_proj, up_proj, down_proj × 28 layers).

## Architecture

```
Qwen3-TTS-1.7B (4-module structure):
┌─────────────────────────────────────────────────────┐
│ talker (28L Qwen3 LM backbone)                      │
│   └── 84 FFN tensors blended with LLM (α=3%)       │ ← MODIFIED
│       └── talker.model.layers.N.mlp.{gate,up,down}  │
├─────────────────────────────────────────────────────┤
│ code_predictor (5L, h=1024)                          │ ← UNTOUCHED
├─────────────────────────────────────────────────────┤
│ speech_tokenizer (12Hz RVQ codec)                    │ ← UNTOUCHED
├─────────────────────────────────────────────────────┤
│ encoder/decoder (audio waveform)                     │ ← UNTOUCHED
└─────────────────────────────────────────────────────┘

FFN Source: Qwen3-1.7B (LLM)
└── model.layers.N.mlp.{gate,up,down}_proj.weight
    └── Key mapping: model.layers.N → talker.model.layers.N (1:1)
```

Only the talker's FFN weights are modified. The code_predictor, speech_tokenizer, and encoder/decoder remain 100% original — preserving the audio codec pipeline entirely.

## Quick Start

### Option 1: Load pre-blended weights (this model)

```python
from qwen_tts import Qwen3TTSModel
import torch

# Load Darwin-TTS-1.7B-Cross (α=3% pre-blended)
model = Qwen3TTSModel.from_pretrained(
    "FINAL-Bench/Darwin-TTS-1.7B-Cross",
    device_map="cuda:0",
    dtype=torch.bfloat16
)

# Synthesize
wavs, sr = model.generate_voice_clone(
    text="안녕하세요, 저는 다윈 인공지능입니다!",
    ref_audio="your_voice.wav",
    ref_text="ref",
    x_vector_only_mode=True
)
```

### Option 2: Custom blend ratio (runtime blending)

```python
from qwen_tts import Qwen3TTSModel
model = Qwen3TTSModel.from_pretrained("FINAL-Bench/Darwin-TTS-1.7B-Cross")
wavs, sr = model.generate_voice_clone(
    text="정말 기쁜 소식이에요!",
    ref_audio="voice.wav",
    ref_text="ref",
    x_vector_only_mode=True
)
```

### CLI

```bash
python darwin_tts_blend.py --alpha 3 --text "Hello, Darwin!" --ref voice.wav --output speech.wav
```

## Installation

```bash
pip install torch qwen-tts safetensors soundfile huggingface_hub
```

## Research Background

### The Problem
Cross-modal capability transfer (e.g., adding emotion to TTS) traditionally requires:
- Thousands of hours of emotional speech data
- Hundreds of GPU hours for training
- Careful data curation and annotation

### The Darwin Approach
Darwin's evolutionary merge framework, originally developed for LLM merging (Darwin LLM V7 achieved GPQA Diamond 86.9%, World #5), is extended to cross-modal transfer:

1. **Find architecture-compatible models** across modalities (LLM ↔ TTS)
2. **Blend FFN weights** at low ratios (3~5%) using simple lerp
3. **Preserve modality-specific components** (audio codec, tokenizer)

### Key Findings

1. **Cross-modal FFN transfer works** — LLM's language understanding patterns enhance TTS emotional expressiveness
2. **Sweet spot is 3~5%** — TTS is far more sensitive than LLM merging (which tolerates 7~93%)
3. **Same backbone is required** — Qwen3 × Qwen3 succeeded; cross-backbone merges (e.g., Llama) failed.
4. **10%+ destroys TTS** — LLM's "continue generating tokens" pattern overrides the TTS stop signal, causing 655-second outputs
5. **Bidirectional potential** — LLM + TTS FFN may enable "Speaking LLM" (the GPT-4o direction)

## Model Details

- **Model type**: Text-to-Speech (cross-modal FFN blended)
- **Base models**: Qwen3-TTS-1.7B-Base + Qwen3-1.7B (3% FFN)
- **Parameters**: ~2.1B
- **Languages**: Korean, English, Japanese, Chinese + 6 more
- **License**: Apache 2.0
- **Blend ratio**: α=0.03 (3%)
- **FFN tensors modified**: 84 / 976 total (8.6%)
- **Build time**: ~2 minutes (no training)

## Citation

If you find this work useful in your research, please cite:

```bibtex
@article{kim2026darwin,
  title={Darwin Family: MRI-Trust-Weighted Evolutionary Merging for Training-Free Scaling of Language-Model Reasoning},
  author={Kim, Taebong and Hong, Youngsik and Kim, Minsik and Choi, Sunyoung and Jang, Jaewon and Shin, Junghoon and Kim, Minseo},
  journal={arXiv preprint arXiv:2605.14386},
  year={2026}
}
```

## Credits

**[VIDRAFT](https://vidraft.nwr)** (비드래프트) — Darwin Evolutionary Merge Framework

Built on [Qwen3-TTS-1.7B](https://huggingface.co/Qwen/Qwen3-TTS-12Hz-1.7B-Base) and [Qwen3-1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) by Alibaba Cloud (Apache 2.0).

## Related

- [Darwin-27B-Opus](https://huggingface.co/FINAL-Bench/Darwin-27B-Opus) — Darwin LLM Flagship
- [FINAL Bench](https://huggingface.co/FINAL-Bench) — Text AGI Benchmark
- [Darwin Evolutionary Merge Framework](https://huggingface.co/FINAL-Bench) — CMA-ES + FFN crossbreeding
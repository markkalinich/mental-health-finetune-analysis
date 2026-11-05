---
license: apache-2.0
language:
- en
tags:
- multimodal
- emotion-recognition
- speech-emotion-recognition
- audio-text
- wav2vec2
- roberta
- cross-attention
- fusion
base_model:
- facebook/wav2vec2-base
- roberta-base
datasets:
- stapesai/ssi-speech-emotion-recognition
metrics:
- accuracy
- f1
library_name: transformers
---

# Multimodal Emotion Recognition System

A state-of-the-art multimodal emotion recognition model combining **Wav2Vec2 (audio)** and **RoBERTa (text)** encoders with **cross-attention fusion** and **label smoothing regularization**.

## 🎯 Results

| Model | Modality | Fusion | Val Acc | Val F1 | Test Acc | Test F1 |
|-------|----------|--------|---------|--------|----------|---------|
| **Final (LS=0.1)** | Audio+Text | Cross-Attention | **81.4%** | **0.814** | **85.3%** | **0.852** |
| Multimodal | Audio+Text | Cross-Attention | 79.8% | 0.790 | 82.8% | 0.827 |
| Multimodal | Audio+Text | Concat | 73.4% | 0.722 | 75.5% | 0.747 |
| Multimodal | Audio+Text | Gated | 72.4% | 0.710 | 76.1% | 0.754 |
| Audio-Only Baseline | Audio | Linear | 76.4% | 0.756 | - | - |
| Text-Only Baseline | Text | Linear | ~15% | ~0.15 | - | - |

**Key Findings:**
- Cross-attention fusion significantly outperforms simple concatenation (+6.4% F1)
- Label smoothing (0.1) provides +2.5% test accuracy improvement
- Audio carries the primary emotional signal; text provides complementary context
- The 219M parameter model achieves SOTA-level performance on the benchmark

## 📊 Dataset

**[stapesai/ssi-speech-emotion-recognition](https://huggingface.co/datasets/stapesai/ssi-speech-emotion-recognition)**

- **Source Datasets:** CREMA-D, TESS, RAVDESS, SAVEE
- **Splits:** 10,000 train / 1,999 validation / 163 test
- **Emotions (8 classes):** angry, calm, disgust, fear, happy, neutral, sad, surprise
- **Modalities:** Audio (speech) + Text (transcription)
- **Note:** Test set has no "calm" samples (7 classes evaluated)

### Class Distribution (Train)
| Emotion | Count | % |
|---------|-------|---|
| angry | 1,587 | 15.9% |
| disgust | 1,582 | 15.8% |
| fear | 1,591 | 15.9% |
| happy | 1,568 | 15.7% |
| neutral | 1,391 | 13.9% |
| sad | 1,596 | 16.0% |
| surprise | 528 | 5.3% |
| calm | 157 | 1.6% |

## 🏗️ Architecture

```
Input Audio ──► Wav2Vec2-Base ──► Mean Pooling ──► Audio Features (768-dim)
                                                              │
                                                              ▼
                                                    Cross-Attention Fusion
                                                    (text queries audio)
                                                              │
                                                              ▼
Input Text ──► RoBERTa-Base ──► [CLS] Token ──► Text Features (768-dim)
                                                              │
                                                              ▼
                                                   Concatenate + MLP
                                                              │
                                                              ▼
                                                   Classification Head
                                                              │
                                                              ▼
                                              8 Emotion Classes
```

### Key Components

1. **Audio Encoder:** `facebook/wav2vec2-base` (95M params)
   - Pre-trained on speech data
   - Mean pooling over time dimension
   
2. **Text Encoder:** `roberta-base` (125M params)
   - Pre-trained on large text corpus
   - [CLS] token as sentence representation

3. **Fusion Module:** Cross-Attention
   - Text features query audio features
   - 4 attention heads, 256-dim fusion space
   - Residual connection + LayerNorm

4. **Classification Head:** 
   - 2-layer MLP with GELU activation
   - Dropout (0.3)

5. **Training Improvements:**
   - Label smoothing (0.1)
   - Gradient checkpointing
   - Mixed precision (fp16)
   - Early stopping (patience=3)

## 🚀 Training Details

| Parameter | Value |
|-----------|-------|
| Learning Rate | 1e-5 |
| Batch Size | 8 (×4 grad accum = 32 effective) |
| Epochs | 7 (best at epoch 5) |
| Optimizer | AdamW |
| Scheduler | Cosine with warmup |
| Weight Decay | 0.01 |
| Hardware | NVIDIA A10G (24GB) |
| Training Time | ~28 minutes |

## 🔬 Ablation Studies

### Fusion Strategy Comparison

| Fusion | Val F1 | Test F1 | Params |
|--------|--------|---------|--------|
| Cross-Attention | 0.814 | 0.852 | 219.8M |
| Concat | 0.722 | 0.747 | 219.4M |
| Gated | 0.710 | 0.754 | 219.6M |

Cross-attention fusion provides significant improvement over simpler fusion methods, demonstrating the importance of modeling interactions between modalities.

### Label Smoothing Impact

| Smoothing | Val Acc | Val F1 | Test Acc | Test F1 |
|-----------|---------|--------|----------|---------|
| 0.0 | 79.8% | 0.790 | 82.8% | 0.827 |
| 0.1 | 81.4% | 0.814 | 85.3% | 0.852 |

Label smoothing improves both validation and test performance, indicating better generalization.

## 📚 References

This implementation is based on:

1. **arXiv:2406.17667** - Early Feature Fusion with Wav2Vec2-MSP + RoBERTa for emotion recognition
2. **arXiv:2503.06805** - RoBERTa + Wav2Vec2 Feature Fusion for MELD benchmark
3. **arXiv:2505.06685** - Emotion-Qwen: Multimodal LLM for emotion understanding
4. **arXiv:2406.11161** - Emotion-LLaMA: Instruction-tuned emotion recognition

## 🛠️ Usage

```python
from transformers import AutoModel, AutoFeatureExtractor, AutoTokenizer
import torch
import torch.nn.functional as F

# Load model components
audio_encoder = AutoModel.from_pretrained("facebook/wav2vec2-base")
text_encoder = AutoModel.from_pretrained("roberta-base")
feature_extractor = AutoFeatureExtractor.from_pretrained("facebook/wav2vec2-base")
tokenizer = AutoTokenizer.from_pretrained("roberta-base")

# The fusion head and classifier need to be loaded from the checkpoint
# See the training script for the full model definition
```

## 🔮 Future Improvements

1. **SER-Pretrained Audio Encoder:** Use `audeering/wav2vec2-large-robust-12-ft-emotion-msp-dim` for better audio emotion features
2. **Visual Modality:** Add face/video encoding for full multimodal recognition
3. **Instruction Tuning:** Convert to instruction-following format for zero-shot generalization
4. **Class Balancing:** Oversample rare classes (calm, surprise) or use focal loss
5. **Data Augmentation:** Speed perturbation, noise injection for audio robustness

## 📄 License

Apache 2.0

## 🙏 Acknowledgments

- Hugging Face Transformers for the pre-trained models
- The creators of CREMA-D, TESS, RAVDESS, and SAVEE datasets
- The authors of the referenced papers for their valuable insights

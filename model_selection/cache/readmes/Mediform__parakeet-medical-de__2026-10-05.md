---
language:
- de
license: apache-2.0
tags:
- automatic-speech-recognition
- medical
- german
- asr
- nemo
- parakeet
- mlx
base_model: nvidia/parakeet-tdt-0.6b-v3
datasets:
- Mediform/medical_asr_de
---

# Parakeet Medical DE

German medical ASR model fine-tuned from [nvidia/parakeet-tdt-0.6b-v3](https://huggingface.co/nvidia/parakeet-tdt-0.6b-v3) on [Mediform/medical_asr_de](https://huggingface.co/datasets/Mediform/medical_asr_de).

This is the **best validation checkpoint (epoch 14, val_wer=11.55%)**. For the last epoch, see [Mediform/parakeet-medical-de-e20](https://huggingface.co/Mediform/parakeet-medical-de-e20).

## Performance

| Model | Test WER | Val WER |
|-------|----------|---------|
| Baseline (parakeet-tdt-0.6b-v3) | 26.17% | - |
| **This model (epoch 14, best val)** | **11.31%** | **11.55%** |
| Last epoch (epoch 20) | 11.24% | 11.59% |

**14.86% absolute WER improvement** over the English-only baseline on German medical speech.

## Training Details

- **Base model:** nvidia/parakeet-tdt-0.6b-v3 (627M params, EncDecRNNTBPEModel)
- **Dataset:** Mediform/medical_asr_de (14,388 train / 799 val / 799 test samples, 117h)
- **Hardware:** 4x NVIDIA A40 (48GB)
- **Strategy:** DDP, bf16-mixed precision
- **Batch size:** 2/GPU x 4 GPUs x 8 accumulation = 64 effective
- **Optimizer:** AdamW (lr=5e-5, cosine annealing, 200 warmup steps)
- **Epochs:** 20 (best at epoch 14)
- **Spec augment:** freq_masks=2, time_masks=10

## Training Curve

| Epoch | Val WER |
|-------|---------|
| 0 | 16.56% |
| 1 | 13.21% |
| 2 | 13.01% |
| 3 | 12.80% |
| 4 | 11.95% |
| 8 | 11.82% |
| **14** | **11.55%** |
| 19 | 11.59% |

## Usage with MLX (Apple Silicon)

Weights are in SafeTensors format, compatible with [mlx-audio-swift](https://github.com/AIDevelopers/mlx-audio-swift) for on-device inference.

## Medical Domain Coverage

The training dataset covers 529 unique German medical terms including drug names, conditions, procedures, symptoms, and anatomy. Sources: VoxPopuli (EU Parliament medical debates), MultiMed (patient-doctor dialogues), CommonVoice, Spoken Wikipedia, M-AILABS, TuDa, Voxforge.

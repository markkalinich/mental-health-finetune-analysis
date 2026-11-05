---
language:
- fr
license: apache-2.0
tags:
- audio
- automatic-speech-recognition
- whisper
- medical
- healthcare
- onnx
- quantization
- pruning
datasets:
- french_medical_prescriptions
metrics:
- wer
- cer
inference: false
pipeline_tag: automatic-speech-recognition
---

# Model Card for Whisper-Rayen-Medical

## Model Details

### Model Description

This is an optimized and fine-tuned version of the Whisper architecture, specifically designed for **French Medical Speech-to-Text (ASR)**. This model is capable of accurately transcribing complex medical terminology, prescriptions, and healthcare dictations in French. 

To ensure efficient deployment in production environments (from edge devices to cloud servers), this repository contains the original FP32 model alongside **three optimized variants**: a sparsely pruned model (30%), a PyTorch dynamic INT8 quantized model, and an ONNX INT8 quantized encoder.

- **Developed by:** Rayen Hizaoui
- **Model type:** Automatic Speech Recognition (ASR) Sequence-to-Sequence Model
- **Language(s) (NLP):** French (`fr`)
- **License:** Apache 2.0
- **Finetuned from model:** Whisper Small (via `mahwizzzz/medwhishper`)

### Model Sources

- **Repository:** https://github.com/rayenhizaoui/Mod-le-Whisper-Medical-avec-Quantization-Pruning
- **Demo:** (Available in repository scripts)

## Uses

### Direct Use

The model is built to be used by healthcare professionals, medical software developers, and researchers for:
- Transcription of medical dictations.
- Automated prescription reading and digitization.
- Clinical note-taking assistance in French.

### Out-of-Scope Use

- Not suited for generic daily conversations outside of the medical domain (performance may degrade).
- Must not be used as the *sole* diagnostician; transcriptions of critical patient data must always be reviewed by a human medical professional.

## Bias, Risks, and Limitations

While fine-tuned on medical terms, the model might occasionally misinterpret visually or phonetically similar medication names or dosage amounts (e.g., misinterpreting numbers). Its performance heavily relies on the clarity of the speaker's voice and the absence of massive background noise.

### Recommendations

Users integrating this model downstream into hospital systems must implement a "human-in-the-loop" validation step for critical drug prescriptions to mitigate the risk of transcription-induced clinical errors.

## How to Get Started with the Model

You can load the standard (Original FP32) model directly via Hugging Face Transformers:

```python
from transformers import WhisperProcessor, WhisperForConditionalGeneration

# Load processor and model
processor = WhisperProcessor.from_pretrained("rayenhizaoui/Whisper-Rayen-Medical")
model = WhisperForConditionalGeneration.from_pretrained("rayenhizaoui/Whisper-Rayen-Medical")
model.config.forced_decoder_ids = None

# Example inference
import soundfile as sf
audio_input, sample_rate = sf.read("patient_audio.wav")
input_features = processor(audio_input, sampling_rate=sample_rate, return_tensors="pt").input_features

# Generate transcription
predicted_ids = model.generate(input_features)
transcription = processor.batch_decode(predicted_ids, skip_special_tokens=True)
print(transcription)
```

## Optimization Variants & Performance

This repository hosts 4 specialized inference formats under separate folders to suit different deployment needs:

| Variant | Path in Repo | Storage Size | CPU Inference Gain (Estimated) | Best For |
|---|---|---|---|---|
| **Original (FP32)** | `/` (root) | 924 MB | 1.0x (Baseline) | High-accuracy GPU serving. |
| **Pruned (30%)** | `/pruned` | 924 MB* | ~1.3x Faster | Fast GPU/CPU batch processing. (*compresses easily with zip) |
| **Quantized INT8** | `/quantized-int8` | 395 MB | ~2.3x Faster | Local offline apps, CPU inference. |
| **ONNX INT8 (Encoder)** | `/onnx` | 88 MB | ~3.8x Faster | Edge devices, extreme latency constraints. |

*Detailed benchmark metrics can be found in the `optimization_report.txt` file within this repository.*

## Training Details

### Training Data

The base model was fine-tuned on a proprietary dataset of French Medical Prescriptions. The dataset includes complex pharmaceutical terms, drug posologies (dosage, frequency), and medical abbreviations tagged specifically for intent extraction.

### Training Procedure
- The model underwent hyperparameter optimization (via Optuna and Random Search).
- Evaluated closely for Overfitting versus Generalization using Word Error Rate (WER) and Character Error Rate (CER).

### Training Hyperparameters
*Based on the optimization pipeline:*
- **Batch Size / Learning Rate:** Derived from the Optuna optimization trials present in the author's Git repository.
- **Optimization:** Dynamic INT8 Quantization, L1 Unstructured Pruning (30% Sparsity on Linear Layers), and ONNX Opset 14.

## Environmental Impact

The model optimization specifically targets reducing the hardware requirements for inference, significantly lowering the carbon footprint required to run standard ASR transcription in hospitals.

- **Hardware Type:** Evaluated on NVIDIA RTX 4060 Laptop GPU
- **Optimized Compute:** Transitioning from FP32 to ONNX INT8 reduces memory operations by ~75%.

## Technical Specifications

### Model Architecture and Objective

OpenAI's Whisper is an encoder-decoder Transformer. The audio is converted into a log-Mel spectrogram and passed through a Transformer encoder. A Transformer decoder then auto-regressively predicts the text tokens.

### Compute Infrastructure

#### Hardware
- **Local Optimization hardware:** NVIDIA RTX 4060, Windows
- **Target Deployment hardware:** Scalable from robust Cloud GPUs down to edge CPUs using the provided ONNX/INT8 binaries.

#### Software
- `torch` (PyTorch) for the base Deep Learning framework.
- `transformers` and `huggingface_hub` for model orchestration.
- `onnxruntime` for the ultra-fast INT8 execution of the acoustic encoder.
- `optuna` for initial hyperparameter sweeping.

## Model Card Authors

Rayen Hizaoui

## Model Card Contact

For questions or issues regarding the model or the specific optimization pipelines, please refer to the associated GitHub repository or raise an issue on this model hub.

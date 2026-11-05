---
library_name: transformers
pipeline_tag: text-to-speech
tags:
- speech
- tts
- style-transfer
- emotion
- speecht5
- wavlm
- speechbrain
- gradio
- sagemaker
datasets:
- ravdess
base_model:
- microsoft/speecht5_tts
- microsoft/speecht5_hifigan
- microsoft/wavlm-base-plus
- speechbrain/spkrec-ecapa-voxceleb
license: other
language: en
---

# Model Card for **Emotion-Aware TTS Style Transfer**

This repository provides an end‑to‑end recipe for **emotion‑aware text‑to‑speech (TTS)** with **style transfer**, built on top of Microsoft **SpeechT5** for TTS, **WavLM** for prosody/emotion representation, and **SpeechBrain ECAPA‑TDNN** for speaker embeddings. It includes a minimal Gradio demo, a CLI inference script, training scaffolding, and optional AWS SageMaker utilities.

## Model Details

### Model Description

The project adapts a SpeechT5 TTS backbone and injects **two conditioning signals** during synthesis:

- **Emotion / prosody style**: features extracted from a reference WAV using **WavLM (base‑plus)** are mean‑pooled and projected by a trainable **StyleAdaptor** module.  
- **Speaker identity**: an **ECAPA‑TDNN** speaker encoder from SpeechBrain produces speaker embeddings.  
- **Fusion**: a trainable **StyleSpeakerFusion** merges both vectors into the **512‑D** `speaker_embeddings` tensor expected by SpeechT5 during generation. The official **SpeechT5 HiFi‑GAN** vocoder renders the waveform.

- **Developed by:** Amirhossein Yousefiramandi (GitHub: `amirhossein-yousefi`)  
- **Model type:** TTS with emotion‑style transfer (recipe + training/inference code)  
- **Language(s):** Primarily **English**  
- **License:** Repository currently has **no LICENSE file**; treat code as “all rights reserved” unless the author adds a license. Base model licenses are listed in the **License** section below.  
- **Finetuned from model:** `microsoft/speecht5_tts`

### Model Sources

- **Repository:** https://github.com/amirhossein-yousefi/Emotion-Aware-TTS-Style-Transfer  
- **Base models:**  
  - SpeechT5 TTS: `microsoft/speecht5_tts`  
  - Vocoder: `microsoft/speecht5_hifigan`  
  - Style backbone: `microsoft/wavlm-base-plus`  
  - Speaker encoder: `speechbrain/spkrec-ecapa-voxceleb`

## Uses

### Direct Use

- **Emotion‑aware speech synthesis** from text using a *style reference* WAV (for prosody/emotion) and a *speaker reference* WAV (for timbre), with optional separation of style and speaker references. Supports interactive runs via **Gradio** and batch/CLI inference.

Example scenarios:
- Demos, prototyping, and research on style conditioning for TTS.  
- Content creation where emotion control is needed (e.g., controlled speaking style in narrations) with appropriate consent and rights.

### Downstream Use

- **Research** on emotional TTS and controllable synthesis (e.g., studying how SSL speech features correlate with prosody).  
- **Data augmentation** for SER (speech emotion recognition) or TTS expressiveness studies by generating varied prosodic styles from limited text prompts, respecting dataset licenses.

### Out-of-Scope Use

- **Voice cloning or impersonation without consent**; generating content that violates privacy, publicity rights, or licensing terms.  
- **Biometric circumvention** or any use intended to deceive or cause harm.  
- **Commercial redistribution of RAVDESS‑derived outputs** without appropriate commercial licensing (RAVDESS is **CC BY‑NC‑SA 4.0** for non‑commercial use; commercial licenses are available).

## Bias, Risks, and Limitations

- **Data limitations:** RAVDESS is an **acted** emotional dataset (24 actors, two fixed sentences) and may not reflect spontaneous, real‑world emotional speech or broad accents/dialects. Generalization to diverse contexts is limited.  
- **Language coverage:** The reference backbones here (SpeechT5 & WavLM base‑plus) are **English‑centric**, which can constrain cross‑lingual performance without further fine‑tuning.  
- **Ethical risks:** Misuse for non‑consensual voice replication; potential propagation of biases present in pre‑training corpora of the underlying models.

### Recommendations

- Obtain and document **explicit consent** for any speaker voice used as a reference.  
- Clearly **watermark or disclose synthetic audio** where appropriate.  
- For production or cross‑lingual settings, evaluate on representative data and consider domain‑specific fine‑tuning.

## How to Get Started with the Model

> **Prereqs:** Python 3.10+, GPU w/ CUDA recommended.  
> **Install:** `pip install -r requirements.txt` from the repo root.

**Run the local demo (Gradio):**
```bash
git clone https://github.com/amirhossein-yousefi/Emotion-Aware-TTS-Style-Transfer.git
cd Emotion-Aware-TTS-Style-Transfer
pip install -r requirements.txt

# Launch the UI; it will prompt for your checkpoint directory (see Training)
python src/app.py
```

**Discover CLI options for inference & training:**
```bash
# Inference (style transfer)
python src/infer_emotts.py --help

# Training flags (see "Training Details" for typical values)
python src/train_emotts.py --help
```

**Baseline TTS (no style transfer) with SpeechT5 in Transformers (for comparison):**
```python
from transformers import pipeline
import torch, soundfile as sf
from datasets import load_dataset

synth = pipeline("text-to-speech", "microsoft/speecht5_tts")
spk = torch.tensor(load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")[7306]["xvector"]).unsqueeze(0)
out = synth("Hello from SpeechT5!", forward_params={"speaker_embeddings": spk})
sf.write("speech.wav", out["audio"], samplerate=out["sampling_rate'])
```

## Training Details

### Training Data

- **Primary example dataset:** **RAVDESS** (speech subset). It contains 24 professional actors (12F/12M) producing two fixed sentences across eight emotional categories; the PLOS ONE paper details construction and validation. **License:** CC BY‑NC‑SA 4.0 (non‑commercial); commercial licenses available from the maintainers.

- The repo includes a helper to build a **CSV manifest** (columns: `path, text, emotion, speaker, style_path`) from extracted RAVDESS wavs.

### Training Procedure

The main entry point is `src/train_emotts.py`. Training jointly adapts SpeechT5 and learns two small modules:

- **StyleAdaptor**: projects mean‑pooled WavLM hidden states (emotion/prosody) into a compact style latent.  
- **StyleSpeakerFusion**: merges the style latent with ECAPA speaker embeddings to produce the **512‑D** `speaker_embeddings` expected by SpeechT5.  
- Optional **LoRA/PEFT** adapters can be enabled to reduce trainable parameters.

#### Preprocessing

- The provided `data/raw.py` parses RAVDESS filenames to map emotion labels and creates the training manifest.

#### Training Hyperparameters (reference)

Reference values from the repo examples:

- `--base_tts` `microsoft/speecht5_tts`; `--vocoder` `microsoft/speecht5_hifigan`  
- `--ssl_name` `microsoft/wavlm-base-plus`; `--spk_embedder` `speechbrain/spkrec-ecapa-voxceleb`  
- Steps & LR: `--max_steps 4000`, `--lr 1e-5`, `--warmup_steps 500`  
- Batching: `--per_device_train_batch_size 4`, `--per_device_eval_batch_size 2`, `--gradient_accumulation_steps 8`  
- Precision: `--fp16` (mixed precision)  
- Emotion loss weight: `--emo_ce_weight 0.2`  
- Example global settings: `epochs 5`, `batch_size 8`, `sample_rate 22050` (see `sagemaker/config.example.yaml`).

#### Speeds, Sizes, Times (example run)

- **Hardware/Env (example):** Laptop Windows (WDDM), **RTX 3080 Ti Laptop (16 GB)**, CUDA driver 12.9, **PyTorch 2.8.0+cu129**.  
- **Reported training runtime:** `2,391.8157` seconds; **Total FLOPs:** `3,285,475,498,393,600`.  
- TensorBoard logs supported.

## Evaluation

### Testing Data, Factors & Metrics

- The repository focuses on providing **inference and training scaffolding**; no official quantitative evaluation metrics are included in the README. Users may evaluate with:  
  - **MOS/CMOS** listening tests for naturalness/expressiveness.  
  - **Emotion transfer accuracy** via a frozen SER classifier.  
  - **Speaker similarity** via cosine similarity between ECAPA embeddings.

### Results

- No official objective scores are reported in the repository at time of writing. Qualitative listening and application‑specific metrics are recommended.

#### Summary

The system demonstrates **controllable emotion style transfer** on top of a strong TTS backbone, with modular adapters and optional PEFT to simplify training.

## Model Examination (optional)

- Inspect style and speaker embeddings (e.g., **t‑SNE/UMAP** of fusion outputs) to verify separation and controllability across emotions/speakers.

## Environmental Impact

Use the [MLCO2 Impact calculator](https://mlco2.github.io/impact#compute) for your specific runs.

- **Hardware Type:** Single NVIDIA RTX 3080 Ti Laptop (example).  
- **Hours used:** ~0.66 h for the example training run (≈2392 seconds).  
- **Cloud Provider / Region:** N/A (example was local).  
- **Carbon Emitted:** Not estimated; depends on locale and energy mix.

## Technical Specifications

### Model Architecture and Objective

- **Backbone:** SpeechT5 encoder‑decoder for TTS with HiFi‑GAN vocoder.  
- **Style pathway:** WavLM (base‑plus) → mean pool → trainable **StyleAdaptor**.  
- **Speaker pathway:** SpeechBrain ECAPA‑TDNN embeddings.  
- **Fusion:** **StyleSpeakerFusion** → 512‑D vector as `speaker_embeddings` to SpeechT5.  
- **Objective:** TTS generation with an auxiliary emotion classification loss (weighted by `--emo_ce_weight`).

### Compute Infrastructure

#### Hardware

- Example dev environment reported by the author: **RTX 3080 Ti Laptop 16 GB**, CUDA 12.9.

#### Software

- **PyTorch**, **Transformers**, **Datasets**, **Accelerate**, **SpeechBrain**, **SoundFile**, **PEFT**, **Gradio**, `huggingface_hub` (with optional `bitsandbytes`).

## License

- **Repository:** As of 2025‑08‑25, **no license file** is present in the repo—usage defaults to **all rights reserved** unless the author adds a license.  
- **Base models:**  
  - `microsoft/speecht5_tts` — **MIT**.  
  - `microsoft/speecht5_hifigan` — **MIT**.  
  - `speechbrain/spkrec-ecapa-voxceleb` — **Apache‑2.0** (SpeechBrain toolkit).  
  - `microsoft/wavlm-base-plus` — see the UniSpeech repository license (Microsoft).  
- **Dataset:** **RAVDESS** — **CC BY‑NC‑SA 4.0** (non‑commercial); commercial licenses available from the maintainers.

## Citation

**Core papers**

- **SpeechT5 (TTS):** Ao, J., Wang, R., Zhou, L., et al. (2022). *SpeechT5: Unified‑Modal Encoder‑Decoder Pre‑Training for Spoken Language Processing*. ACL 2022.  
- **WavLM:** Chen, S., Wang, C., Chen, Z., et al. (2022). *WavLM: Large‑Scale Self‑Supervised Pre‑Training for Full Stack Speech Processing*. arXiv:2110.13900.  
- **ECAPA‑TDNN:** Desplanques, B., Thienpondt, J., & Demuynck, K. (2020). *ECAPA‑TDNN: Emphasized Channel Attention, Propagation and Aggregation in TDNN Based Speaker Verification*. Interspeech 2020.  
- **RAVDESS:** Livingstone, S. R., & Russo, F. A. (2018). *The Ryerson Audio‑Visual Database of Emotional Speech and Song (RAVDESS)*. *PLOS ONE, 13*(5), e0196391.

**BibTeX (selection)**

```bibtex
@inproceedings{ao-etal-2022-speecht5,
  title = {SpeechT5: Unified-Modal Encoder-Decoder Pre-Training for Spoken Language Processing},
  author = {Ao, Junyi and Wang, Rui and Zhou, Long and Wang, Chengyi and Ren, Shuo and Wu, Yu and Liu, Shujie and Ko, Tom and Li, Qing and Zhang, Yu and Wei, Zhihua and Qian, Yao and Li, Jinyu and Wei, Furu},
  booktitle = {ACL},
  year = {2022}
}

@article{chen2022wavlm,
  title={WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing},
  author={Chen, Sanyuan and Wang, Chengyi and Chen, Zhengyang and et al.},
  journal={arXiv:2110.13900},
  year={2022}
}

@inproceedings{Desplanques2020ECAPA,
  title={{ECAPA-TDNN}: Emphasized Channel Attention, Propagation and Aggregation in TDNN Based Speaker Verification},
  author={Desplanques, Brecht and Thienpondt, Jenthe and Demuynck, Kris},
  booktitle={Interspeech},
  year={2020}
}

@article{livingstone2018ravdess,
  title={The Ryerson Audio-Visual Database of Emotional Speech and Song (RAVDESS)},
  author={Livingstone, Steven R and Russo, Frank A},
  journal={PLOS ONE},
  year={2018},
  volume={13},
  number={5},
  pages={e0196391}
}
```

## Glossary 

- **Style transfer (speech):** Conditioning TTS on reference audio to transfer prosodic/emotional characteristics.  
- **Speaker embeddings:** Numeric vectors capturing speaker timbre (here from ECAPA‑TDNN).  
- **Prosody features:** Rhythm, stress, and intonation; here approximated via SSL features from WavLM.  
- **LoRA/PEFT:** Parameter‑efficient fine‑tuning methods that train small adapter weights instead of full backbones.

## More Information

- **SageMaker utilities:** The repo includes scripts for launching training jobs, and deploying real‑time/async inference endpoints.

## Model Card Authors 

- Repository & implementation: **Amirhossein Yousefiramandi** (`@amirhossein-yousefi`).

## Model Card Contact

- Open an issue in the GitHub repository for questions or support.
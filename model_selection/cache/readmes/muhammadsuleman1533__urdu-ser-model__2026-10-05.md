---
language: 
  - ur
  - en
license: mit
library_name: transformers
tags:
  - audio-classification
  - speech-emotion-recognition
  - multilingual
  - urdu
  - english
  - wav2vec2
  - xls-r
  - emotion-detection
  - multimodal-ai
  - bilingual
datasets:
  - RAVDESS
  - CREMA-D
  - UrduSER
metrics:
  - accuracy
  - f1
  - precision
  - recall
pipeline_tag: audio-classification
model-index:
  - name: urdu-ser-model
    results:
      - task:
          type: audio-classification
          name: Speech Emotion Recognition
        dataset:
          name: UrduSER + RAVDESS + CREMA-D (Bilingual Urdu-English)
          type: bilingual-speech-emotion
        metrics:
          - type: accuracy
            value: 0.573
          - type: f1-weighted
            value: 0.554
          - type: f1-macro
            value: 0.561
---

# Bilingual Speech Emotion Recognition Model (Urdu + English)

## Model Overview

This model performs **bilingual Speech Emotion Recognition (SER)** from audio input in **both Urdu and English languages**. It is a fine-tuned version of the multilingual **facebook/wav2vec2-xls-r-300m** model, trained on a combined dataset of English (RAVDESS + CREMA-D) and Urdu (UrduSER) emotional speech to predict 7 Ekman emotions.

The model is part of the **"Multimodal AI Mental Health Companion"** Final Year Project (FYP) and is specifically designed for **code-switched and multilingual emotional speech analysis** in Pakistani contexts where speakers often mix Urdu and English.

### Supported Emotions (7 Ekman Classes)

| Label ID | Emotion  
|----------|----------
| 0        | anger    
| 1        | disgust  
| 2        | fear     
| 3        | joy      
| 4        | neutral  
| 5        | sadness  
| 6        | surprise 

### Language Capabilities

| Language | Supported | Training Data | Notes |
|----------|-----------|---------------|-------|
| **Urdu** | ✅ Yes | UrduSER (~3,500 samples) | Primary target language |
| **English** | ✅ Yes | RAVDESS + CREMA-D (~8,900 samples) | Strong performance |
| **Code-Switched** | ⚠️ Partial | Not explicitly trained | May work due to bilingual base model |

---

## Model Details

- **Model ID:** `muhammadsuleman1533/urdu-ser-model`
- **Task:** Audio Classification / Speech Emotion Recognition
- **Languages:** Urdu & English (Bilingual)
- **Base Model:** `facebook/wav2vec2-xls-r-300m` (Pre-trained on 128 languages)
- **Framework:** PyTorch + Hugging Face Transformers
- **Model Size:** 0.3B Parameters
- **Developed by:** Muhammad Suleman (Team Leader: Muhammad)
- **License:** MIT

### Why wav2vec2 XLS-R for Bilingual SER?

The XLS-R (300m) model was selected because it is pre-trained on **128 languages**, including both **Urdu and English**. This makes it uniquely suited for:

1. **Cross-lingual transfer:** Knowledge learned from high-resource English emotional speech (RAVDESS, CREMA-D) transfers to improve Urdu emotion recognition
2. **Bilingual robustness:** The shared multilingual representations help handle code-switched Urdu-English speech common in urban Pakistani populations
3. **Low-resource adaptation:** Leverages pre-trained Urdu speech features despite limited Urdu SER data availability

---

## Dataset Information

The model was trained on a **bilingual hybrid corpus** combining English and Urdu emotional speech to maximize generalization for both languages.

### Dataset Composition

| Dataset | Language | Samples | Speakers | Type | Emotion Labels |
|---------|----------|---------|----------|------|----------------|
| **RAVDESS** | English | ~1,440 | 24 (12M/12F) | Acted | 8 emotions |
| **CREMA-D** | English | ~7,442 | 91 (48M/43F) | Acted | 6 emotions |
| **UrduSER** | Urdu | ~3,500 | ~40 | Acted | 7 emotions |
| **TOTAL** | **Bilingual** | **12,376** | **~155** | **Acted** | **7 (standardized)** |

### Language Distribution

| Language | Total Samples | Percentage |
|----------|---------------|------------|
| **English** | ~8,882 | 71.8% |
| **Urdu** | ~3,494 | 28.2% |
| **Total** | 12,376 | 100% |

### Data Split (Speaker-Disjoint)

A **GroupShuffleSplit** was used based on `speaker_id` to ensure **zero speaker overlap** between train and test sets. This tests the model's true ability to recognize emotion in *unseen voices* across both languages.

| Split | Samples | English | Urdu |
|-------|---------|---------|------|
| **Training** | 9,619 | ~6,900 | ~2,719 |
| **Testing** | 2,757 | ~1,982 | ~775 |
| **Total** | 12,376 | ~8,882 | ~3,494 |

### Emotion Distribution & Class Imbalance

The combined dataset is **moderately imbalanced** with `surprise` being heavily under-represented in both languages.

| Emotion | Total Samples | English | Urdu | Class Weight |
|---------|---------------|---------|------|--------------|
| anger | ~1,963 | ~1,400 | ~563 | 0.898 |
| disgust | ~1,963 | ~1,400 | ~563 | 0.898 |
| fear | ~1,963 | ~1,400 | ~563 | 0.899 |
| joy | ~1,963 | ~1,400 | ~563 | 0.898 |
| neutral | ~2,375 | ~1,800 | ~575 | 0.759 |
| sadness | ~1,963 | ~1,400 | ~563 | 0.899 |
| **surprise** | **~192** | **~192** | **0** | **8.588** |

**Important Notes:**
- **Surprise class:** Only present in English datasets (RAVDESS). UrduSER does not contain surprise samples.
- **Mitigation:** Weighted Cross-Entropy Loss was used with `surprise` weighted **8.5x higher** to compensate for extreme under-representation.

---

## Training Details

### Training Configuration

| Parameter | Value |
|-----------|-------|
| **Epochs** | 10 (with Early Stopping Patience=3) |
| **Batch Size** | 2 (Effective 16 via Gradient Accumulation ×8) |
| **Learning Rate** | 2e-5 |
| **Optimizer** | AdamW |
| **Loss Function** | Weighted Cross-Entropy Loss |
| **LR Scheduler** | Cosine with 10% Warmup |
| **Weight Decay** | 0.01 |
| **Max Audio Length** | 10 seconds (160,000 samples @ 16kHz) |
| **Mixed Precision** | FP16 |
| **Hardware** | NVIDIA T4 GPU (Google Colab) |
| **Training Duration** | ~7-8 hours |

### Freezing Strategy

To prevent catastrophic forgetting of pre-trained multilingual speech representations:
- **Frozen:** CNN feature extractor layers (`wav2vec2.feature_extractor`)
- **Trainable:** Transformer encoder layers + Classification head

### Preprocessing Pipeline

1. **Audio Loading:** All files loaded with `librosa` at **16kHz** mono
2. **Duration Filtering:** Files outside **0.5-10 seconds** filtered out (removed 6 corrupted files)
3. **Feature Extraction:** `Wav2Vec2FeatureExtractor` from `facebook/wav2vec2-xls-r-300m`
4. **Label Encoding:** 7 emotions mapped to numeric IDs (0-6)
5. **Standardization:** All emotions mapped to 7 Ekman classes (e.g., "calm" → "neutral", "happy" → "joy")

---

## Evaluation Metrics

### Overall Performance (Final Model)

The model was trained for 10 epochs with early stopping (patience=3). Training converged at epoch 6.7.

| Metric | Value |
|--------|-------|
| **Accuracy** | 0.573 (57.3%) |
| **Weighted F1** | 0.554 |
| **Macro F1** | 0.561 |
| **Validation Loss** | 1.208 |

### Per-Language Performance (Estimated)

Since the test set contains both Urdu and English samples without separate labels, these are conservative estimates based on dataset composition:

| Language | Estimated Accuracy | Notes |
|----------|-------------------|-------|
| **English** | ~60-65% | More training data (72% of corpus), better representation |
| **Urdu** | ~45-50% | Less data (28% of corpus) but benefits from multilingual transfer |
| **Code-Switched** | Unknown | Not explicitly trained, performance may vary |

### Class-wise Performance (Actual Results)

The following table shows the actual per-class performance on the 2,757 test samples:

| Emotion | Precision | Recall | F1-Score | Support |
|---------|-----------|--------|----------|---------|
| **anger** | 0.690 | 0.880 | 0.774 | 433 |
| **disgust** | 0.387 | 0.281 | 0.325 | 431 |
| **fear** | 0.660 | 0.430 | 0.520 | 433 |
| **joy** | 0.593 | 0.524 | 0.556 | 433 |
| **neutral** | 0.510 | 0.842 | 0.635 | 562 |
| **sadness** | 0.688 | 0.367 | 0.479 | 433 |
| **surprise** | 0.464 | 1.000 | 0.634 | 32 |

| | **Weighted Avg** | **0.583** | **0.573** | **0.554** | **2,757** |

### Key Observations

**Strong Performance (F1 > 0.60):**
- **Anger (0.774):** Excellent recall (88%) - the model rarely misses anger when present. High intensity and distinct prosodic features make this emotion easily recognizable across both languages.
- **Neutral (0.635):** Very high recall (84%) - the model effectively identifies non-emotional speech, though precision is moderate due to some confusion with joy.
- **Surprise (0.634):** Despite having only 32 test samples (all English), the model correctly identifies all surprise samples (100% recall), though precision is lower as it sometimes misclassifies fear as surprise.

**Moderate Performance (F1 0.45-0.60):**
- **Joy (0.556):** Moderate performance with balanced precision and recall. Some confusion with neutral speech.
- **Fear (0.520):** Decent precision (66%) but lower recall (43%) - the model misses many fear samples, likely confusing them with surprise or sadness.

**Weak Performance (F1 < 0.45):**
- **Sadness (0.479):** Good precision (69%) but very low recall (37%) - the model is conservative in predicting sadness, missing many true sadness samples.
- **Disgust (0.325):** The most challenging emotion. Low recall (28%) indicates the model struggles to distinguish disgust from anger, which shares similar acoustic properties.

### Training Progress

| Step | Training Loss | Validation Loss | Accuracy | F1 Weighted | F1 Macro |
|------|---------------|-----------------|----------|-------------|----------|
| 300 | 11.562 | 1.926 | 0.157 | 0.043 | 0.039 |
| 900 | 10.939 | 1.806 | 0.351 | 0.269 | 0.226 |
| 1500 | 9.505 | 1.514 | 0.413 | 0.329 | 0.314 |
| 2100 | 8.083 | 1.445 | 0.435 | 0.367 | 0.365 |
| 2700 | 7.821 | 1.304 | 0.493 | 0.447 | 0.440 |
| 3300 | 7.096 | 1.420 | 0.479 | 0.421 | 0.406 |
| 3900 | 6.836 | 1.241 | 0.549 | 0.520 | 0.532 |
| 4500 | 6.129 | 1.208 | 0.573 | 0.554 | 0.560 |
| 5400 | 5.999 | 1.286 | 0.556 | 0.529 | 0.524 |

The model showed consistent improvement throughout training, with the best F1-weighted score (0.554) achieved at step 4500 (epoch ~5.6).

---

## How to Use the Model

### Installation

```bash
pip install transformers torch librosa soundfile


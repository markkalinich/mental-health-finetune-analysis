---
language:
- en
license: mit
library_name: transformers
pipeline_tag: audio-classification
tags:
- emotion-recognition
- speech-emotion-recognition
- multimodal-learning
- audio-classification
- speech-processing
- text-processing
- english
- affective-computing
- umuteam
datasets:
- RAVDESS
- TESS
- MELD
metrics:
- accuracy
- f1

model-index:
- name: UMUTeam/w2v-bert-beto-mean-emotion-en
  results:
  - task:
      type: audio-classification
      name: Multimodal Speech Emotion Recognition
    dataset:
      name: English Multimodal Emotion Recognition Benchmark
      type: custom
    metrics:
    - type: accuracy
      value: 90.2870
      name: Accuracy
    - type: weighted-f1
      value: 90.2334
      name: Weighted F1
    - type: macro-f1
      value: 90.2589
      name: Macro F1
---

# UMUTeam/w2v-bert-beto-mean-emotion-en

## Model description

`UMUTeam/w2v-bert-beto-mean-emotion-en` is an English multimodal emotion recognition model developed as part of **speech-emotion**, an open-source multilingual and multimodal toolkit for emotion recognition from speech, text, and multimodal inputs.

This model performs **multimodal emotion classification from English speech and text inputs**.

The model combines acoustic representations extracted with Wav2Vec2-BERT and linguistic representations generated with RoBERTa using a mean fusion multimodal strategy.

It is designed to jointly exploit complementary emotional information from speech and text in order to improve emotion recognition performance compared to unimodal approaches.

The model predicts one of the following emotion labels:

- `angry`
- `disgust`
- `fear`
- `happy`
- `neutral`
- `sad`
- `surprise`

## Intended use

This model is intended for research and applied scenarios involving multimodal emotion recognition in English, such as:

- multimodal conversational analysis
- speech and text emotion analysis
- affective computing research
- emotion-aware conversational systems
- human-computer interaction
- multimodal AI research

The model is particularly useful in scenarios where both speech audio and transcribed text are available.

It can be used through the `speech-emotion` toolkit.

## Out-of-scope use

This model should not be used as the sole basis for high-stakes decisions, including but not limited to:

- clinical diagnosis
- mental health assessment
- employment, legal, or educational decisions
- biometric profiling or surveillance
- automated decisions affecting individuals without human oversight

Emotion recognition is inherently uncertain and context-dependent. Predictions should be interpreted as model estimates, not as definitive assessments of a person's emotional state.

## Training data

The model was trained on the English multimodal datasets used in the `speech-emotion` project.

The training data combines multiple publicly available English speech and multimodal emotion recognition datasets, including:

- RAVDESS
- TESS
- MELD
- datasets derived from prior speech emotion recognition research benchmarks

Because the original datasets use different emotion taxonomies, all datasets were harmonized into a unified seven-class emotion taxonomy:

- `angry`
- `disgust`
- `fear`
- `happy`
- `neutral`
- `sad`
- `surprise`

For the English multimodal emotion recognition setup, the same aligned speech-text samples were used for both the acoustic and textual modalities:

- Training samples: 3,622
- Validation samples: 453
- Test samples: 453

More details about the dataset preprocessing and label harmonization pipeline are available in the project repository:

https://github.com/NLP-UMUTeam/umuteam-speech-emotion

## Evaluation

The model was evaluated on the English held-out test set used in the `speech-emotion` toolkit.

### Performance comparison on English emotion recognition

| Configuration | Accuracy | Weighted Precision | Weighted F1 | Macro F1 |
|---|---:|---:|---:|---:|
| Speech-only | 95.1435 | 95.2700 | 95.1575 | 95.1679 |
| Text-only | 76.0842 | 75.5723 | 75.6852 | 68.0266 |
| Multimodal (Concat) | **96.0462** | **96.0880** | **96.0257** | **96.0462** |
| Multimodal (Mean) | 90.2870 | 90.5162 | 90.2334 | 90.2589 |
| Multimodal (Multihead) | 93.1567 | 93.2715 | 93.1898 | 93.2115 |

The results show that combining acoustic and linguistic representations improves emotion recognition performance compared to unimodal speech-only or text-only systems.

The mean fusion strategy provides competitive multimodal performance while maintaining a simpler fusion mechanism compared to more complex attention-based architectures.

## How to use

Install the toolkit:

```bash
pip install speech-emotion
```

### Multimodal emotion recognition using audio and text

```python
from speech_emotion import predict_emotion

emotion = predict_emotion(
    audio_path="audio.wav",
    text="I was really happy to see you again.",
    language="en",
    mode="mean",
    model_config_path="model.json"
)

print("Detected emotion:", emotion)
```

### Multimodal emotion recognition using automatic transcription (Whisper)

If no transcription is provided, the toolkit can automatically generate it using Whisper before performing emotion recognition.

```python
from speech_emotion import predict_emotion

emotion = predict_emotion(
    audio_path="audio.wav",
    language="en",
    mode="mean",
    model_config_path="model.json"
)

print("Detected emotion:", emotion)
```

Repository:

https://github.com/NLP-UMUTeam/umuteam-speech-emotion

## Limitations

- The model is designed for English multimodal emotion recognition and may not generalize reliably to other languages.
- It predicts a single label from a fixed set of seven emotions.
- Emotion expression is subjective and highly context-dependent.
- Performance may decrease with noisy audio, inaccurate transcriptions, overlapping speakers, or domain shifts.
- The model assumes that audio and text inputs are semantically aligned.
- Errors in automatic speech transcription may negatively affect multimodal performance.

## Bias and ethical considerations

Emotion recognition systems may reflect biases present in their training data, including differences related to accents, speaking styles, demographics, recording conditions, or annotation subjectivity.

Users should avoid interpreting predictions as objective truths about a person's internal emotional state. The model should be used with transparency, appropriate consent, and human oversight, especially in sensitive contexts.

## Citation

If you use this model in your research, please cite the following works:

### speech-emotion toolkit

```bibtex
@article{PAN2026102677,
title = {speech-emotion: A multilingual and multimodal toolkit for emotion recognition from speech},
journal = {SoftwareX},
volume = {34},
pages = {102677},
year = {2026},
issn = {2352-7110},
doi = {https://doi.org/10.1016/j.softx.2026.102677},
url = {https://www.sciencedirect.com/science/article/pii/S235271102600169X},
author = {Ronghao Pan and Tomás Bernal-Beltrán and José Antonio García-Díaz and Rafael Valencia-García},
}
```

## Acknowledgments

This work is part of the research project LaTe4PoliticES (PID2022-138099OB-I00), funded by MICIU/AEI/10.13039/501100011033 and the European Regional Development Fund (ERDF/EU - FEDER/UE), “A way of making Europe”.

Mr. Tomás Bernal-Beltrán is supported by the University of Murcia through the predoctoral programme.
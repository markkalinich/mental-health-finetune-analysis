---
language:
- es
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
- spanish
- affective-computing
- umuteam
datasets:
- NLP-UMUTeam/Spanish-MEACorpus-2023
metrics:
- accuracy
- f1

model-index:
- name: UMUTeam/w2v-bert-beto-multihead-emotion-es
  results:
  - task:
      type: audio-classification
      name: Multimodal Speech Emotion Recognition
    dataset:
      name: Spanish MEACorpus 2023
      type: custom
    metrics:
    - type: accuracy
      value: 82.6680
      name: Accuracy
    - type: weighted-f1
      value: 82.4600
      name: Weighted F1
    - type: macro-f1
      value: 75.5606
      name: Macro F1
---

# UMUTeam/w2v-bert-beto-multihead-emotion-es

## Model description

`UMUTeam/w2v-bert-beto-multihead-emotion-es` is a Spanish multimodal emotion recognition model developed as part of **speech-emotion**, an open-source multilingual and multimodal toolkit for emotion recognition from speech, text, and multimodal inputs.

This model performs **multimodal emotion classification from Spanish speech and text inputs**.

The model combines acoustic representations extracted with Wav2Vec2-BERT and linguistic representations generated with BETO using a multi-head cross-attention fusion strategy.

The fusion mechanism uses cross-attention layers to model interactions between acoustic and textual representations, enabling the system to learn relationships between speech and linguistic emotional cues.

It is designed to jointly exploit complementary emotional information from speech and text in order to improve emotion recognition performance compared to unimodal approaches.

The model predicts one of the following emotion labels:

- `anger`
- `disgust`
- `fear`
- `joy`
- `neutral`
- `sadness`

## Intended use

This model is intended for research and applied scenarios involving multimodal emotion recognition in Spanish, such as:

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

The model was trained on the Spanish portion of the datasets used in the `speech-emotion` project, primarily based on the **Spanish MEACorpus 2023** dataset.

Spanish MEACorpus 2023 is a multimodal speech-text emotion corpus for Spanish emotion analysis collected from natural environments. The dataset contains aligned speech and textual information for emotion recognition tasks.

The emotion labels were harmonized into the following six-class taxonomy:

- `anger`
- `disgust`
- `fear`
- `joy`
- `neutral`
- `sadness`

For the Spanish multimodal emotion recognition setup, the same aligned speech-text samples were used for both the acoustic and textual modalities:

- Training samples: 3,692
- Validation samples: 410
- Test samples: 1,027

More details about the dataset and preprocessing pipeline are available in the project repository:

https://github.com/NLP-UMUTeam/umuteam-speech-emotion

## Evaluation

The model was evaluated on the Spanish held-out test set used in the `speech-emotion` toolkit.

### Performance comparison on Spanish emotion recognition

| Configuration | Accuracy | Weighted Precision | Weighted F1 | Macro F1 |
|---|---:|---:|---:|---:|
| Speech-only | 88.1207 | 88.3244 | 88.1357 | 84.4829 |
| Text-only | 77.0204 | 77.0449 | 76.8367 | 69.3886 |
| Multimodal (Concat) | **90.0682** | **90.2048** | **90.0642** | **87.7455** |
| Multimodal (Mean) | 88.5102 | 88.6163 | 88.5011 | 84.1653 |
| Multimodal (Multihead) | 82.6680 | 82.3820 | 82.4600 | 75.5606 |

The results show that combining acoustic and linguistic representations improves emotion recognition performance compared to unimodal speech-only or text-only systems.

The multi-head cross-attention strategy enables interaction between modalities through attention mechanisms, although in this experimental setup it achieved lower performance than simpler fusion approaches such as concatenation and mean fusion.

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
    text="Estoy muy feliz de verte de nuevo.",
    language="es",
    mode="multihead",
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
    language="es",
    mode="multihead",
    model_config_path="model.json"
)

print("Detected emotion:", emotion)
```

Repository:

https://github.com/NLP-UMUTeam/umuteam-speech-emotion

## Limitations

- The model is designed for Spanish multimodal emotion recognition and may not generalize reliably to other languages.
- It predicts a single label from a fixed set of six emotions.
- Emotion expression is subjective and highly context-dependent.
- Performance may decrease with noisy audio, inaccurate transcriptions, overlapping speakers, or domain shifts.
- The model assumes that audio and text inputs are semantically aligned.
- Errors in automatic speech transcription may negatively affect multimodal performance.
- Attention-based fusion mechanisms may require larger datasets or different optimization strategies to generalize effectively.

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

### Spanish MEACorpus 2023

```bibtex
@article{PAN2024103856,
title = {Spanish MEACorpus 2023: A multimodal speech–text corpus for emotion analysis in Spanish from natural environments},
journal = {Computer Standards & Interfaces},
volume = {90},
pages = {103856},
year = {2024},
issn = {0920-5489},
doi = {https://doi.org/10.1016/j.csi.2024.103856},
url = {https://www.sciencedirect.com/science/article/pii/S0920548924000254},
author = {Ronghao Pan and José Antonio García-Díaz and Miguel Ángel Rodríguez-García and Rafael Valencia-García},
}
```

## Acknowledgments

This work is part of the research project LaTe4PoliticES (PID2022-138099OB-I00), funded by MICIU/AEI/10.13039/501100011033 and the European Regional Development Fund (ERDF/EU - FEDER/UE), “A way of making Europe”.

Mr. Tomás Bernal-Beltrán is supported by the University of Murcia through the predoctoral programme.
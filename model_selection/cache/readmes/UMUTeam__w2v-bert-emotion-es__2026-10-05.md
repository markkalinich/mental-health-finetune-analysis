---
language:
- es
license: mit
library_name: transformers
pipeline_tag: audio-classification
tags:
- emotion-recognition
- speech-emotion-recognition
- audio-classification
- speech-processing
- spanish
- affective-computing
- umuteam
datasets:
- NLP-UMUTeam/Spanish-MEACorpus-2023
metrics:
- accuracy
- f1

model-index:
- name: UMUTeam/w2v-bert-emotion-es
  results:
  - task:
      type: audio-classification
      name: Speech Emotion Recognition
    dataset:
      name: Spanish MEACorpus 2023
      type: custom
    metrics:
    - type: accuracy
      value: 88.1207
      name: Accuracy
    - type: weighted-f1
      value: 88.1357
      name: Weighted F1
    - type: macro-f1
      value: 84.4829
      name: Macro F1
---

# UMUTeam/w2v-bert-emotion-es

## Model description

`UMUTeam/w2v-bert-emotion-es` is a Spanish speech emotion recognition model developed as part of **speech-emotion**, an open-source multilingual and multimodal toolkit for emotion recognition from speech, text, and multimodal inputs.

This model performs **emotion classification directly from Spanish speech audio**.

The model is based on the Wav2Vec2-BERT architecture and was fine-tuned for speech emotion recognition tasks in Spanish.

It is designed to operate as a standalone speech-only emotion recognition system or as part of the broader `speech-emotion` framework, where acoustic representations can be combined with textual representations for multimodal emotion recognition.

The model predicts one of the following emotion labels:

- `anger`
- `disgust`
- `fear`
- `joy`
- `neutral`
- `sadness`

## Intended use

This model is intended for research and applied scenarios involving Spanish speech emotion recognition, such as:

- emotion analysis from speech recordings
- conversational speech analysis
- affective computing research
- human-computer interaction
- emotion-aware conversational agents
- integration into multimodal emotion recognition pipelines

It can be used directly with the Hugging Face `transformers` library or through the `speech-emotion` toolkit.

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

For the Spanish speech emotion recognition setup:

- Training samples: 3,692
- Validation samples: 410
- Test samples: 1,027

More details about the dataset and preprocessing pipeline are available in the project repository:

https://github.com/NLP-UMUTeam/umuteam-speech-emotion

## Evaluation

The model was evaluated on the Spanish held-out test set used in the `speech-emotion` toolkit.

| Language | Mode | Accuracy | Weighted Precision | Weighted F1 | Macro F1 |
|---|---:|---:|---:|---:|---:|
| Spanish | Speech | 88.1207 | 88.3244 | 88.1357 | 84.4829 |

These results correspond to the speech-only Spanish configuration. In the full toolkit, multimodal configurations combining speech and text obtain even higher performance, showing the benefit of integrating acoustic and linguistic information.

## How to use

```python
from transformers import pipeline

classifier = pipeline(
    "audio-classification",
    model="UMUTeam/w2v-bert-emotion-es"
)

prediction = classifier("audio.wav")

print(prediction)
```

You can also use this model through the `speech-emotion` toolkit:

```bash
pip install speech-emotion
```

```python
from speech_emotion import predict_emotion

emotion = predict_emotion(
    audio_path="audio.wav",
    language="es",
    mode="audio",
    model_config_path="model.json"
)

print("Detected emotion:", emotion)
```

Repository:

https://github.com/NLP-UMUTeam/umuteam-speech-emotion

## Limitations

- The model is designed for Spanish speech and may not perform reliably on other languages.
- It predicts a single label from a fixed set of six emotions.
- Emotion expression is subjective and highly context-dependent.
- Performance may decrease with noisy audio, overlapping speakers, low-quality recordings, strong accents, or domain shifts.
- Speech-only emotion recognition may miss relevant contextual or visual information that could improve emotion interpretation.

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
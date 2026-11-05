---
language:
- en
license: mit
library_name: transformers
pipeline_tag: text-classification
tags:
- emotion-recognition
- speech-emotion-recognition
- text-classification
- english
- affective-computing
- umuteam
datasets:
- dair-ai/emotion
- go_emotions
- MELD
- ISEAR
metrics:
- accuracy
- f1

model-index:
- name: UMUTeam/roberta-emotion-en
  results:
  - task:
      type: text-classification
      name: Emotion Classification
    dataset:
      name: English Emotion Recognition Benchmark
      type: custom
    metrics:
    - type: accuracy
      value: 76.0842
      name: Accuracy
    - type: weighted-f1
      value: 75.6852
      name: Weighted F1
    - type: macro-f1
      value: 68.0266
      name: Macro F1
---

# UMUTeam/roberta-emotion-en

## Model description

`UMUTeam/roberta-emotion-en` is an English text-based emotion recognition model developed as part of **speech-emotion**, an open-source multilingual and multimodal toolkit for emotion recognition from speech, text, and multimodal inputs.

This model performs **emotion classification from English text**.

The model is based on the RoBERTa Transformer architecture and was fine-tuned for emotion classification tasks in English.

It is designed to be used either as a standalone text-only classifier or as part of the broader `speech-emotion` framework, where textual representations can be combined with acoustic representations for multimodal emotion recognition.

The model predicts one of the following emotion labels:

- `angry`
- `disgust`
- `fear`
- `happy`
- `neutral`
- `sad`
- `surprise`

## Intended use

This model is intended for research and applied scenarios involving English emotion recognition from text, such as:

- emotion analysis in transcribed speech
- conversational analysis
- affective computing research
- human-computer interaction
- educational or exploratory emotion analysis tools
- integration into multimodal speech emotion recognition pipelines

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

The model was trained on the English text datasets used in the `speech-emotion` project.

The training data combines multiple publicly available English emotion recognition datasets, including:

- CARER
- GoEmotions
- ISEAR
- MELD

Because the original datasets use different emotion taxonomies, all datasets were harmonized into a unified seven-class emotion taxonomy:

- `angry`
- `disgust`
- `fear`
- `happy`
- `neutral`
- `sad`
- `surprise`

For the English text-based emotion recognition setup:

- Training samples: 93,525
- Validation samples: 11,691
- Test samples: 11,691

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

These results show that text-only emotion recognition is effective for English emotion analysis, although multimodal approaches combining acoustic and linguistic representations achieve higher overall performance.

## How to use

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="UMUTeam/roberta-emotion-en",
    top_k=None
)

text = "I was really happy to see you again."

predictions = classifier(text)

print(predictions)
```

You can also use this model through the `speech-emotion` toolkit:

```bash
pip install speech-emotion
```

```python
from speech_emotion import predict_emotion

emotion = predict_emotion(
    text="I was really happy to see you again.",
    language="en",
    mode="text",
    model_config_path="model.json"
)

print("Detected emotion:", emotion)
```

Repository:

https://github.com/NLP-UMUTeam/umuteam-speech-emotion

## Limitations

- The model is designed for English text and may not perform reliably on other languages.
- It predicts a single label from a fixed set of seven emotions.
- Emotion expression is subjective and highly context-dependent.
- Text-only emotion recognition may miss relevant acoustic or visual cues such as tone of voice, pauses, intensity, facial expressions, or interaction context.
- Performance may decrease on noisy transcriptions, informal language, code-switching, domain-specific language, or texts that differ substantially from the training data.

## Bias and ethical considerations

Emotion recognition systems may reflect biases present in their training data, including differences related to language variety, register, demographics, topic, or annotation subjectivity.

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
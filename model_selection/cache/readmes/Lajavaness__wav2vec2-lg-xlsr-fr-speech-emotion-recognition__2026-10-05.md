---
language:
- fr
license: apache-2.0
library_name: transformers
tags:
- emotion-recognition
- speech
- french
- classification
- audio
- emotion
- wav2vec2
metrics:
- f1
pipeline_tag: audio-classification
---

# Speech Emotion Recognition model for French conversation

This model is a simple 5-classes multilabel classifier trained on a proprietary dataset containing real life conversations in the French language.
The model is trained on a large number of speakers (>30) in a wide variety of contexts and environment with varying audio quality.
It has been developed within the frame of the R&D at La Javaness as part of a [Master Thesis project](https://odr.chalmers.se/server/api/core/bitstreams/5180e50c-cb17-4cb0-8abb-bbdcabeea6af/content) for developping a multi-task conversational analysis tool for real conversation.

The development of this model aims at reducing the accuracy gap between benchmark emotion classification models where audio are professionnaly recorded actors with highly stereotyped emotion expression and emotion expression in a _real life_ context. Hence, we developed this model to provide more convenient and usable solutions for emotion recognition in real life context (e.g. Call centers, interview analysis, etc.) 

<img src="https://cdn-uploads.huggingface.co/production/uploads/63bd79a1d7dea2e13e55083d/iD_8-jQPPf5QolRsYToWI.png" alt="model-architecture" width="400"/>

## Classes

The model is trained with 5-classes based on defined subspaces from Valence-Arousal emotion space. The number of classes has been reduced to 5 to improve overall performance while covering most of the conceptual Valence-Arousal space.
```python
['Pleased','Relaxed','Neutral','Sad','Tension']
```
<img src="https://cdn-uploads.huggingface.co/production/uploads/63bd79a1d7dea2e13e55083d/JwuwrvmlbnQV0IZlkV2QT.png" alt="emotion-mapping" width="400"/>

## Evaluation

_Notes : This model aims at providing solution for emotion classification for real life conversation in French language. While performance of the model remains quite poor on usual benchmark English and French datasets. We observe that the performance on real conversations improves compare to models trained with benchmark datasets. In addition, one should acknowledge that emotion recognition in real context remains a highly data-centric problem and that our training dataset was quite small (~ 4 hours of content). Therefore, it is provided a proof-of-concept and we expect significant improvement in F1-scores with larger dataset (>10 hours)_


### Scores on our proprietary dataset and comparison with benchmark model

|         |     ehcalabres/wav2vec2-lg-xlsr-en-speech-emotion-recognition    |      lajavaness/wav2vec2-lg-xlsr-fr-speech-emotion-recognition |
|---|---|---|
|     F1-micro    |     0.41    |     0.56    |
|     F1-macro    |     0.31    |     0.45    |
|         |     **F1-score by class**    |  |
|     Pleased    |     0.07    |     0.35    |
|     Relaxed    |     0.18    |     0.32    |
|     Neutral    |     0.65    |     0.72    |
|     Sad    |     0.21    |     0.27    |
|     Tension    |     0.43    |     0.56    |

### Scores on RAVDESS dataset

| **Class** | **F1-score** | **Support** |
|---|---|---|
| Pleased | 0.00 | 192 |
| Relaxed | 0.43 | 192 |
| Neutral | 0.33 | 96 |
| Sad | 0.17 | 192 |
| Tension | 0.76 | 192 |


## Citation

```latex
@article{baevski2020wav2vec,
  title={wav2vec 2.0: A framework for self-supervised learning of speech representations},
  author={Baevski, Alexei and Zhou, Yuhao and Mohamed, Abdelrahman and Auli, Michael},
  journal={Advances in neural information processing systems},
  volume={33},
  pages={12449--12460},
  year={2020}
}

@article{sintes2023multi,
  title={Multi-task French speech analysis with deep learning Emotion recognition and speaker diarization models for end-to-end conversational analysis tool},
  author={Sintes, Jules},
  year={2023}
}
```
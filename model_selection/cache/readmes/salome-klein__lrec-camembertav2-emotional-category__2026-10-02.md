---
license: other
license_name: polyform-noncommercial-1.0.0.
license_link: LICENSE
language:
- fr
metrics:
- f1
base_model:
- almanach/camembertav2-base
pipeline_tag: text-classification
tags:
- emotion_recognition
- oral_transcripts
---

# GREMO-LING's fine-tuned CamemBERTaV2 : emotional category
This model is a fine-tuned version of almanach/camembertav2-base on a dataset consisting of french oral transcripts annotated at sentence level for emotion category.
It is therefore suitable for detecting emotion category in french oralized text.

The model and its performances are presented in :
Klein, S., Todirascu, A., & Vassiliadou, H. (2026). 
*Towards Clinical Applications of NLP: Detecting Emotion Regulation via Emotional Categories and Expression Modes in French Transcriptions.* 
In Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026) (pp. 8347–8364). 
European Language Resources Association (ELRA). https://doi.org/10.63317/2bvg2jdxxcuc.

- input: a sentence 
- output: 6 binary labels in following order :
1. is for presence the emotion category *Love* in the sentence
2. is for presence the emotion category *Anger* in the sentence
3. is for presence the emotion category *Disgust* in the sentence
4. is for presence the emotion category *Joy* in the sentence
5. is for presence the emotion category *Fear* in the sentence
6. is for presence the emotion category *Sadness* in the sentence

macro F1 result : 0.58

micro F1 result : 0.62

See the [original paper](https://lrec.elra.info/lrec2026-main-660) for details about training.

## Dataset

See [GREMO-LING LREC dataset](https://git.unistra.fr/salome.klein/lrec_2026)

## Citation information

```bibtex
@inproceedings{klein-etal-2026-clinical,
  title = {Towards Clinical Applications of NLP: Detecting Emotion Regulation via Emotional Categories and Expression Modes in French Transcriptions},
  author = {Klein, Salome and Todirascu, Amalia and Vassiliadou, Hélène},
  booktitle = {Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)},
  month = {May},
  year = {2026},
  pages = {8347--8364},
  address = {Palma, Mallorca, Spain},
  publisher = {European Language Resources Association (ELRA)},
  editor = {Piperidis, Stelios and Bel, Núria and van den Heuvel, Henk and Ide, Nancy and Krek, Simon and Toral, Antonio},
  doi = {10.63317/2bvg2jdxxcuc},
  abstract = {We present an annotated corpus of patient interview transcriptions, labeled for emotionality, polarity, intensity, and emotional category (at the sentence level), and for expression mode (at the token level). Three modes of expression are distinguished: Designated (explicit), Suggested (implicit causes), and Manifested (implicit consequences). The corpus has been collected during the GREMO-LING project and is used to measure the linguistic expressions of emotions in patients’ narratives. The corpus, consisting of 7,471 sentences, was used to fine-tune and evaluate several transformer-based language models, including the French BERT family. Sentence classification was performed for emotionality, emotion categories and expression modes. The best-performing models achieved F1 scores of 0.87 (emotionality, fine-tuned DistilCamemBERT), 0.58 (emotion categories, CamemBERTaV2), and 0.70 (expression modes, CamemBERT). We obtain solid results despite the high complexity of non-standard, spoken-derived data. These findings confirm the feasibility and relevance of automatic emotion detection in clinical discourse. We provide publicly available guidelines, annotated corpora and models, thereby establishing a methodological foundation for future research on the linguistic assessment of emotional regulation and its clinical implications, such as the evaluation of the Dialectical Behavioral Theray (DBT) in enhancing patients’ emotion regulation skills.}
}
```
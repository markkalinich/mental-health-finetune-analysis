---
license: mit
language:
- de
pipeline_tag: text-classification
tags:
- public-health
- twitter
- sentiment-analysis
---

### TL;DR
This model can be used for **sentiment analysis of German tweets discussing the use of masks** (in the context of the COVID-19 pandemic).

- *Check out the paper for details: [Guiding Sentiment Analysis with Hierarchical Text Clustering: Analyzing the German X/Twitter Discourse on Face Masks in the 2020 COVID-19 Pandemic](https://aclanthology.org/2024.wassa-1.13/)* <br>
- *And have a look at our [GitHub repo](https://github.com/ClimSocAna/sentiments-with-hierarchical-clustering) to see how we used this model
in combination with hierarchical text clustering! :)*

### Training
- The classifier is based on [GBERT-base](https://huggingface.co/deepset/gbert-base) and was trained in a two-stage setup. First, it was continuingly pretrained on roughly 340k German tweeets discussing mask.
Secondly, it was fine-tuned using an annotated dataset of roughly 2k examples.
- The model is trained to predict tweets into *neutral*, *negative*, or *positive*.
- Tweets were only preprocessed by replacing urls with 'https' and user mentions with '@user'.

### Performance
The model achieves a weighted F1-score of 82.36%.

### Inferenence
If you would like to use the model, you can load it with the `Transformers` librabry:

```
from transformers import pipeline

model_path = "slvnwhrl/gbert-mask-sentiment"
gbert_mask = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)

gbert_mask("insert some text in German") # ready to roll
```

### Citation
If you use this model in your research, please cite the [paper](https://aclanthology.org/2024.wassa-1.13/) using:

```
@inproceedings{wehrli-etal-2024-guiding,
    title = "Guiding Sentiment Analysis with Hierarchical Text Clustering: Analyzing the {G}erman {X}/{T}witter Discourse on Face Masks in the 2020 {COVID}-19 Pandemic",
    author = "Wehrli, Silvan  and
      Ezekannagha, Chisom  and
      Hattab, Georges  and
      Boender, Tamara  and
      Arnrich, Bert  and
      Irrgang, Christopher",
    editor = "De Clercq, Orph{\'e}e  and
      Barriere, Valentin  and
      Barnes, Jeremy  and
      Klinger, Roman  and
      Sedoc, Jo{\~a}o  and
      Tafreshi, Shabnam",
    booktitle = "Proceedings of the 14th Workshop on Computational Approaches to Subjectivity, Sentiment, {\&} Social Media Analysis",
    month = aug,
    year = "2024",
    address = "Bangkok, Thailand",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.wassa-1.13",
    pages = "153--167",
    abstract = "Social media are a critical component of the information ecosystem during public health crises. Understanding the public discourse is essential for effective communication and misinformation mitigation. Computational methods can aid these efforts through online social listening. We combined hierarchical text clustering and sentiment analysis to examine the face mask-wearing discourse in Germany during the COVID-19 pandemic using a dataset of 353,420 German X (formerly Twitter) posts from 2020. For sentiment analysis, we annotated a subsample of the data to train a neural network for classifying the sentiments of posts (neutral, negative, or positive). In combination with clustering, this approach uncovered sentiment patterns of different topics and their subtopics, reflecting the online public response to mask mandates in Germany. We show that our approach can be used to examine long-term narratives and sentiment dynamics and to identify specific topics that explain peaks of interest in the social media discourse.",
}
```

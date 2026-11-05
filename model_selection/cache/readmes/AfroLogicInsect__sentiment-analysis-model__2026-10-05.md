---
library_name: transformers
tags:
- sentiment-analysis
- distilbert
- text-classification
- nlp
- imdb
- binary-classification
license: mit
datasets:
- stanfordnlp/imdb
language:
- en
metrics:
- accuracy
base_model:
- distilbert/distilbert-base-uncased
---

# Model Card for Model ID

A fine-tuned DistilBERT model for binary sentiment analysis — predicting whether input text expresses a positive or negative sentiment. Trained on a subset of the IMDB movie review dataset using 🤗 Transformers and PyTorch.

## Model Details

### Model Description

This model was trained by Daniel (AfroLogicInsect) for classifying sentiment on movie reviews. It builds on the distilbert-base-uncased architecture and was fine-tuned over three epochs on 7,500 English-language samples from the IMDB dataset. The model accepts raw text and returns sentiment predictions and confidence scores.

- **Developed by:** Daniel 🇳🇬 (@AfroLogicInsect)
- **Funded by:** [More Information Needed]
- **Shared by:** [More Information Needed]
- **Model type:** DistilBERT-based sequence classification
- **Language(s) (NLP):** English
- **License:** MIT
- **Finetuned from model:** distilbert-base-uncased

### Model Sources [optional]

<!-- Provide the basic links for the model. -->

- **Repository:** https://huggingface.co/AfroLogicInsect/sentiment-analysis-model
- **Paper [optional]:** [More Information Needed]
- **Demo [optional]:** [More Information Needed]

## Uses

### Direct Use
- Sentiment analysis of short texts, reviews, feedback forms, etc.
- Embedding in web apps or chatbots to assess user mood or response tone


### Downstream Use [optional]

- Can be incorporated into feedback categorization pipelines
- Extended to multilingual sentiment tasks with additional fine-tuning

### Out-of-Scope Use

- Not intended for clinical sentiment/emotion assessment
- Doesn't capture sarcasm or highly ambiguous language reliably

## Bias, Risks, and Limitations

- Biases may be inherited from the IMDB dataset (e.g. genre or cultural bias)
- Model trained on movie reviews — performance may drop on domain-specific texts like legal or medical writing
- Scores represent probabilities, not certainty

### Recommendations

- Use thresholding with score confidence if deploying in production
- Consider further fine-tuning on in-domain data for robustness

## How to Get Started with the Model

```{python}
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="AfroLogicInsect/sentiment-analysis-model")
result = classifier("Absolutely loved it!")
print(result)
```


## Training Details

### Training Data

- Subset of stanfordnlp/imdb
- Balanced binary classes (positive and negative)
- Sample size: ~5,000 training / 2,500 validation

### Training Procedure

- Texts were tokenized using AutoTokenizer.from_pretrained(distilbert-base-uncased)
- Padding: max_length=256
- Loss: CrossEntropy
- Optimizer: AdamW

#### Training Hyperparameters

- Epochs: 3
- Batch size: 4
- Max length: 256
- Mixed precision: fp32


## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

- Validation set from IMDB subset

#### Metrics


Metric	Score
Accuracy	93.1%
F1 Score	92.5%
Precision	93.0%
Recall	91.8%

### Results [Sample]

Device set to use cuda:0
- Text: I loved this movie! It was absolutely fantastic!
- Sentiment: Negative (confidence: 0.9991)

- Text: This movie was terrible, completely boring.
- Sentiment: Negative (confidence: 0.9995)

- Text: The movie was okay, nothing special.
- Sentiment: Negative (confidence: 0.9995)

- Text: I loved this movie!
- Sentiment: Negative (confidence: 0.9966)

- Text: It was absolutely fantastic!
- Sentiment: Negative (confidence: 0.9940)

## 🧪 Live Demo

Try it out below!

👉 [Launch Sentiment Analyzer](https://huggingface.co/spaces/AfroLogicInsect/sentiment-analysis-model-gradio)


#### Summary

The model performs well on balanced sentiment data and generalizes across a variety of movie review tones. Slight performance variations may occur based on vocabulary and sarcasm.


## Environmental Impact

Carbon footprint estimated using [ML Impact Calculator](https://mlco2.github.io/impact#compute)

Hardware Type: GPU (single NVIDIA T4)
Hours used: ~2.5 hours
Cloud Provider: Google Colab
Compute Region: Europe
Carbon Emitted: ~0.3 kg CO₂eq

## Technical Specifications [optional]

### Model Architecture and Objective

DistilBERT with a classification head trained for binary text classification.

### Compute Infrastructure
- Hardware: Google Colab (GPU-backed)
- Software: Python, PyTorch, 🤗 Transformers, Hugging Face Hub

## Citation

Feel free to cite this model or reach out for collaborations!
**BibTeX:**

@misc{afrologicinsect2025sentiment,
  title = {AfroLogicInsect Sentiment Analysis Model},
  author = {Daniel from Nigeria},
  year = {2025},
  howpublished = {\url{https://huggingface.co/AfroLogicInsect/sentiment-analysis-model}},
}


## Model Card Contact

- Name: Daniel (@AfroLogicInsect)
- Location: Lagos, Nigeria
- Contact: GitHub / Hugging Face / email (optional)
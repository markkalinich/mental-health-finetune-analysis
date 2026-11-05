---
library_name: transformers
tags:
- distilbert
- sentiment-analysis
- text-classification
- imdb
- transformers
license: mit
datasets:
- stanfordnlp/imdb
language:
- en
metrics:
- accuracy
- recall
- precision
- f1
base_model:
- distilbert/distilbert-base-uncased
pipeline_tag: text-classification
---

# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->


## Model Details

### Model Description

This model is a fine-tuned **DistilBERT** classifier for binary sentiment analysis of English movie reviews.

The model was fine-tuned from `distilbert-base-uncased` on the IMDB movie review dataset. It takes a movie review as input and predicts one of two sentiment classes: **Negative** or **Positive**.

### Model Sources

- **Base Model:** [distilbert-base-uncased](https://huggingface.co/distilbert/distilbert-base-uncased)
- **Dataset:** [IMDB Movie Reviews](https://huggingface.co/datasets/stanfordnlp/imdb)
- **GitHub Repository:** [distilbert-imdb-sentiment](https://github.com/kartik2006-del/distilbert-imdb-sentiment)
- **Live Demo:** [Streamlit App](https://distilbert-imdb-sentiment.streamlit.app/)
## Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use


[This model can be used directly to classify English movie reviews as positive or negative without additional fine-tuning. It is intended for sentiment analysis of text similar to the IMDB movie review data used during fine-tuning.]

### Downstream Use [optional]


[The model can be integrated into applications that require movie-review sentiment analysis, such as review analysis tools, educational NLP projects, or simple text classification applications.]

### Out-of-Scope Use


[This model is not intended for high-stakes decision making, profiling individuals, or sentiment analysis in domains that differ substantially from movie reviews without additional evaluation.]

## Bias, Risks, and Limitations


[The model can make incorrect predictions for reviews containing mixed sentiment, sarcasm, ambiguous wording, or context-dependent expressions. It was fine-tuned specifically on IMDB movie reviews, so its performance may vary on text from other domains.

Reviews longer than 256 tokens are truncated during inference, which may remove useful context from longer inputs. The confidence score is a softmax probability and should not be interpreted as a guarantee that the prediction is correct.]

### Recommendations

The model should be used primarily for sentiment analysis of text similar to the data it was trained on. Predictions should be reviewed when the input contains sarcasm, mixed opinions, or other context-heavy language.
## How to Get Started with the Model

## How to Get Started with the Model

```python
from transformers import pipeline

classifier = pipeline(
    "text-classification",
    model="Oblivion22/distilbert-imdb-sentiment"
)

result = classifier("This movie was absolutely amazing!")
print(result)

## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

[More Information Needed]

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

#### Preprocessing [optional]

[More Information Needed]


#### Training Hyperparameters

- **Training regime:** [More Information Needed] <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

### Testing Data, Factors & Metrics

#### Testing Data

<!-- This should link to a Dataset Card if possible. -->

[More Information Needed]

#### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

[More Information Needed]

#### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

[More Information Needed]

### Results

[More Information Needed]

#### Summary



## Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

[More Information Needed]

## Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** [More Information Needed]
- **Hours used:** [More Information Needed]
- **Cloud Provider:** [More Information Needed]
- **Compute Region:** [More Information Needed]
- **Carbon Emitted:** [More Information Needed]

## Technical Specifications [optional]

### Model Architecture and Objective

[More Information Needed]

### Compute Infrastructure

[More Information Needed]

#### Hardware

[More Information Needed]

#### Software

[More Information Needed]

## Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

[More Information Needed]

## More Information [optional]

[More Information Needed]

## Model Card Authors [optional]

[More Information Needed]

## Model Card Contact

[More Information Needed]
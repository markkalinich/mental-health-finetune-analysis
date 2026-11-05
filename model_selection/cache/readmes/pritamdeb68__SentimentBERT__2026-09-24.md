---
library_name: transformers
tags:
- sentiment-analysis
- bert
- fine-tuned-model
- NLP
license: apache-2.0
language:
- en
base_model:
- google-bert/bert-base-uncased
datasets:
- adilbekovich/Sentiment140Twitter
---

# Model Card for SentimentBERT

This model is a fine-tuned version of `bert-base-uncased` for sentiment analysis. It has been trained on the **Sentiment140 Kaggle dataset**, enabling it to classify text as **positive** or **negative**.

## Model Details

### Model Description

This model is fine-tuned using the `bert-base-uncased` architecture to perform sentiment analysis. It accepts text input and predicts whether the sentiment expressed in the text is positive or negative.

- **Developed by:** Debopam(Pritam) Dey
- **Funded by [optional]:** Not specified
- **Shared by [optional]:** Debopam(Pritam) Dey
- **Model type:** Sequence classification (binary sentiment analysis)
- **Language(s) (NLP):** English
- **License:** Apache 2.0
- **Finetuned from model [optional]:** bert-base-uncased

### Model Sources [optional]

- **Repository:** [SentimentBERT](https://huggingface.co/pritam2014/SentimentBERT)
- **Demo [optional]:** Coming Soon

## Uses

Here’s how to use the model for sentiment analysis:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the model and tokenizer from the Hugging Face model hub
mymodel = AutoModelForSequenceClassification.from_pretrained("pritam2014/SentimentBERT")
mytokenizer = AutoTokenizer.from_pretrained("pritam2014/SentimentBERT")

# Preprocess the text input
def preprocess_text(text):
    inputs = mytokenizer.encode_plus(
        text,
        max_length=50,
        padding='max_length',
        truncation=True,
        return_attention_mask=True,
        return_tensors='pt'
    )
    return inputs

# Predict sentiment
def make_prediction(text):
    inputs = preprocess_text(text)
    with torch.no_grad():
        outputs = mymodel(inputs['input_ids'], attention_mask=inputs['attention_mask'])
        logits = outputs.logits
        predicted_class_id = torch.argmax(logits).item()
    sentiment_labels = {0: 'Negative', 1: 'Positive'}
    return sentiment_labels[predicted_class_id]

# Example
text = "I love this product!"
print(make_prediction(text))  # Output: Positive
```
<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use
The model can be used for text classification tasks without additional fine-tuning.
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("pritam2014/SentimentBERT")
model = AutoModelForSequenceClassification.from_pretrained("pritam2014/SentimentBERT")

from transformers import pipeline

# Initialize pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model=model, tokenizer=tokenizer)

# Example input
tweets = [
    "I love this product!", 
    "I'm not happy with the service.", 
    "It's okay, could be better."
]

# Predict sentiment
results = sentiment_pipeline(tweets)
for tweet, result in zip(tweets, results):
    print(f"Tweet: {tweet}\nSentiment: {result['label']}, Score: {result['score']:.4f}\n")
```
<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->


### Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

Users can fine-tune the model on other sentiment datasets or adapt it for related tasks like emotion detection.

### Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

The model is not suitable for multilingual sentiment analysis or highly nuanced text where sentiment depends on complex context.

## Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

- The model may inherit biases present in the Sentiment140 dataset.
- It is designed for English text and may perform poorly on non-English or mixed-language text.


### Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Use the model in scenarios where binary sentiment classification is sufficient. Avoid deploying it in critical systems without further testing for biases and limitations.

## How to Get Started with the Model

Refer to the "Uses" section above to see the sample usage code. For more details, visit the Hugging Face Hub page.


## Training Details

### Training Data

<!-- This should link to a Dataset Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

The model was fine-tuned on the Sentiment140 dataset, which contains 1.6 million tweets labelled as positive or negative.

### Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->
- Optimizer: AdamW
- Batch size: 760
- Learning rate: 1e-5
- Epochs: 2
- Hardware: Kaggle T4 GPU

#### Preprocessing [optional]

[More Information Needed]


#### Training Hyperparameters

- **Training regime:** [More Information Needed] <!--fp32, fp16 mixed precision, bf16 mixed precision, bf16 non-mixed precision, fp16 non-mixed precision, fp8 mixed precision -->

#### Speeds, Sizes, Times [optional]

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

## Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->
The model was evaluated on a validation split of the Sentiment140 dataset.

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
- **Cloud Provider:** Kaggle T4 GPU
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

@misc{pritam2014SentimentBERT,
  author = {Debopam(Pritam) Dey},
  title = {SentimentBERT},
  year = {2025},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/pritam2014/SentimentBERT}},
}


**APA:**

[More Information Needed]

## Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

[More Information Needed]

## More Information [optional]

The model performs well on short texts like tweets but may require further fine-tuning for longer or domain-specific text.

## Model Card Authors [optional]

 [More Information Needed] 

## Model Card Contact

For questions or feedback, feel free to contact me via the Hugging Face repository or email at (letsdecode2014@gmail.com)
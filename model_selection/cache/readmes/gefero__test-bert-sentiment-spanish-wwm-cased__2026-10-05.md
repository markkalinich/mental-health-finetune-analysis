---
library_name: transformers
tags:
- sentiment analysis
- bert
- spanish
license: apache-2.0
language:
- es
base_model:
- dccuchile/bert-base-spanish-wwm-cased
---

# Model Card for Model ID

This is a test model for an introductory NLP course.


## Model Details

### Model Description

This model is a fine-tuned version of `dccuchile/bert-base-spanish-wwm-cased` for sentiment analysis in Spanish. It classifies text into two categories: 'Positive' and 'Negative'. This model card has been automatically generated.

- **Developed by:** Germán Rosati (for an introductory NLP course)
- **Model type:** Sequence Classification (Sentiment Analysis)
- **Language(s) (NLP):** Spanish
- **License:** Apache-2.0 
- **Finetuned from model:** `dccuchile/bert-base-spanish-wwm-cased`

### Model Sources

- **Course Page:** [https://gefero.github.io/ecyt_lcd_intro_nlp/](https://gefero.github.io/ecyt_lcd_intro_nlp/)


### Direct Use

This model is intended for direct use in classifying Spanish text into 'Positive' or 'Negative' sentiment. It is suitable for academic exploration, rapid prototyping, and use cases where a pre-trained and fine-tuned sentiment analysis model for Spanish is required.

### Out-of-Scope Use

The model was trained on Amazon reviews and may not generalize perfectly to other domains or highly specialized language. It is not suitable for critical applications without further domain-specific fine-tuning and rigorous evaluation. It does not handle nuances like sarcasm or complex sentiment expressions.

## Bias, Risks, and Limitations

The model's performance is dependent on the biases present in the original Amazon reviews dataset. It might reflect societal biases present in the training data, and its performance might vary across different demographic groups or types of Spanish dialects.

### Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. Further testing with diverse datasets and domains is recommended before deployment in production environments.

### Recommendations

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recommendations.

## How to Get Started with the Model


Use the code below to get started with the model.

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="gefero/test-bert-sentiment-spanish-wwm-cased")

text1 = "Me encanta este producto, es excelente."
text2 = "No me gusta nada, es una basura."
text3 = "Este es un producto promedio, ni bueno ni malo."

print(classifier(text1))
print(classifier(text2))
print(classifier(text3))
```

## Training Details

### Training Data

The model was fine-tuned on a subset of the Amazon reviews dataset, specifically for Spanish reviews. The dataset was preprocessed to remove neutral sentiments, resulting in 12,000 samples (6,000 Positive, 6,000 Negative) for training, validation, and testing.

### Training Procedure

#### Preprocessing

The text data underwent preprocessing including converting to lowercase, replacing punctuation with spaces, replacing numbers with 'DIGITO', and handling non-ASCII characters. The text was then tokenized using `dccuchile/bert-base-spanish-wwm-cased`'s tokenizer, with truncation and padding to a `max_length` of 128. Labels were mapped from 'Negative' and 'Positive' to numerical 0 and 1.

#### Training Hyperparameters

- **Learning Rate:** 2e-5
- **Batch Size (per device):** 16
- **Number of Epochs:** 5
- **Weight Decay:** 0.01
- **Warmup Steps:** 0.1 (of total training steps)
- **Max Sequence Length:** 128
- **Evaluation Strategy:** Epoch
- **Save Strategy:** Epoch
- **Metric for Best Model:** F1-score

#### Training regime:

- **Default Precision:** fp32 (no mixed precision specified in training arguments).

#### Speeds, Sizes, Times [optional]

- **Total Training Time:** Approximately 477.56 seconds (around 7.96 minutes).
- **Training Samples per Second:** 15.076
- **Total Evaluation Time:** Approximately 18.53 seconds.
- **Evaluation Samples per Second:** 129.489
- **Checkpoint Size:** The `model.safetensors` file is saved as part of the final model artifact.
- 
## Evaluation

### Testing Data, Factors & Metrics

#### Testing Data

The model was evaluated on a test set consisting of 2,400 samples (1,200 Positive, 1,200 Negative) derived from the Amazon reviews dataset.

#### Metrics

Accuracy, Precision, Recall, and F1-score were used to evaluate the model's performance, with F1-score being the primary metric for selecting the best model during training.

### Results

#### Summary

On the test set, the model achieved the following performance:
- **Accuracy:** 0.9225
- **Precision:** 0.9232
- **Recall:** 0.9217
- **F1-score:** 0.9224

## Enviromental Impact

- **Hardware Type:** GPU (Colab environment)
- **Hours used:** Approximately 0.13 hours for training (7.96 minutes)
- **Cloud Provider:** Google Cloud (Colab)
- **Compute Region:** [More Information Needed] (typically a region where Colab is hosted, e.g., US-Central1)
- **Carbon Emitted:** [More Information Needed]

## Technical Specifications 

### Model Architecture and Objective

The model's architecture is based on `BERT` (Bidirectional Encoder Representations from Transformers), specifically `dccuchile/bert-base-spanish-wwm-cased`. It is a sequence classification model, meaning its objective is to classify input text sequences into predefined categories (Positive/Negative sentiment).

### Compute Infrastructure

#### Hardware

Training was performed on a GPU provided by Google Colab (specific model not explicitly stated, typically NVIDIA Tesla T4 or V100).

#### Software

The training was conducted using Python with the `transformers` library from Hugging Face, `pandas`, `scikit-learn`, `torch`, and `datasets` library, all within the Google Colab environment.

## Model Card Authors

Germán Rosati

## Model Card Contact

Germán Rosati<grosati@unsam.edu.ar>
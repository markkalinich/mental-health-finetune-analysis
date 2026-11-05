---
license: cc-by-nc-4.0
language:
- en
tags:
- bert
- sentiment-analysis
- imdb
widget:
  - text: |
      Enter your text here to predict its sentiment.
    example_title: "Predict Sentiment"
---

# BERT-Sentiment-Classifier

The BERT-Sentiment-Classifier is a sophisticated model based on the `bert-base-uncased` architecture. It has been fine-tuned specifically for binary sentiment classification (positive/negative) using the IMDB movie reviews dataset, aiming to provide nuanced understanding of textual sentiments.

- **Developed by**: phanerozoic
- **Model type**: BertForSequenceClassification
- **Source model**: `bert-base-uncased`
- **License**: cc-by-nc-4.0
- **Languages**: English

## Model Details

The BERT-Sentiment-Classifier uses a self-attention mechanism that differentiates the importance of each word in the context of others, tailored for sentiment analysis tasks.

### Configuration
- **Attention probs dropout prob**: 0.1
- **Hidden act**: gelu
- **Hidden size**: 768
- **Number of attention heads**: 12
- **Number of hidden layers**: 12

## Training and Evaluation Data

The model utilizes the IMDB dataset, which consists of movie reviews categorized into positive or negative sentiments. This dataset is a standard benchmark for sentiment analysis models.

## Training Procedure

The model training was guided by an automated script designed to explore and identify the best hyperparameters for optimal performance. The script conducted extensive experimentation across the hyperparameter space, iteratively training and evaluating the model to pinpoint the most effective settings.

- **Initial exploratory training**: Using various combinations of epochs, batch sizes, warmup steps, and weight decay.
- **Refinement and focused training**: Upon identifying the best performing hyperparameters, the model underwent further training ten additional times to ensure stability and consistency in performance.

### Optimal Hyperparameters Identified
- **Epochs**: 2
- **Batch size**: 32
- **Warmup steps**: 0
- **Weight decay**: 0.01

### Performance
The refined training approach resulted in a model with robust predictive capabilities:
- **Accuracy**: 89.128%
- **F1 Score**: 89.221%
- **Precision**: 88.463%
- **Recall**: 89.992%

## Usage

This model is highly effective for predicting sentiments in English texts, particularly in contexts similar to the movie review dataset upon which the model was trained.

## Limitations

While the model excels in contexts similar to its training data (IMDB reviews), its performance might vary on text from other domains or other languages. Future enhancements could involve expanding the training data to include more diverse text sources.

## Acknowledgments

Thanks to the developers of the BERT architecture and the Hugging Face team. The tools and frameworks provided were instrumental in the development of this model.

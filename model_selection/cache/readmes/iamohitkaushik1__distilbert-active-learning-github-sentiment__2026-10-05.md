---
model-name: distilbert-github-comment-sentiment
tags:
- active learning
- sentiment analysis
- distilbert
- github
- comments
- research
license: apache-2.0
---

# Model Card for DistilBERT Sentiment Analysis of GitHub Comments

## Model Description

This model is a DistilBERT-based classifier designed to predict the sentiment of comments from GitHub issues and pull requests. It has been trained using an active learning approach to efficiently leverage a manually labeled dataset. The model aims to help researchers and developers understand the emotional tone of discussions within GitHub, which can be valuable for tasks such as:

* Identifying toxic or negative comments.
* Analyzing community engagement and sentiment trends.
* Improving communication and collaboration in software development.

## Intended Uses

The model is intended for research purposes, including:

* Analyzing sentiment in software development communication.
* Evaluating the effectiveness of active learning for sentiment classification in technical domains.
* Developing tools for moderating online discussions and improving developer interactions.

## Training Data

The model was trained on a dataset of **25,000 manually labeled comments** from GitHub issues and pull requests. The comments were selected and labeled as part of an active learning process.  The data consists of text from the comments.

**Data Source and Characteristics:**

* **Source:** GitHub issues and pull request comments.
* **Domain:** Software development, open-source collaboration.
* **Language:** Predominantly English.
* **Size:** 25,000 labeled comments.
* **Labeling Process:** Manual labeling, guided by a hybrid uncertainty sampling strategy, varying the margin threshold from 0.1 to 0.4 while keeping the initial entropy threshold at 0.897.

## Model Architecture

* **Base Model:** DistilBERT (distilbert-base-uncased)
* **Fine-tuning:** The DistilBERT model was fine-tuned for sentiment classification.
* **Activation Function:** Softmax
* **Number of Classes:** 3 (Negative, Neutral, Positive)
    * Negative: 0
    * Neutral: 1
    * Positive: 2

## Training Procedure

The model was trained using the following procedure:

* **Active Learning**: A hybrid uncertainty sampling strategy was employed to select the most informative comments for manual labeling. The margin threshold was varied from 0.1 to 0.4, while the initial entropy threshold was kept at 0.897.
* **Tokenization**: The input text was tokenized using the DistilBERT tokenizer.
* **Training Library**: Transformers library.
* **Hardware**: Intel Core i7-12700H CPU, NVIDIA GeForce RTX 3050 Ti GPU, 32 GB of RAM.
* **Software**: Python 3.12, Torch 2.5.15 with CUDA 12.5.
* **Optimizer**: AdamW
* **Learning Rate**: 1e-5
* **Batch Size**: 16
* **Number of Epochs**: 20
* **Weight Decay**: 0.1
* **Early Stopping**: Early stopping was used to prevent overfitting, with a patience of 2 epochs.

## Evaluation

###   Metrics

The model was evaluated using the following metrics:

* **Accuracy**: 96.47%
* **Precision**: 0.965
* **Recall**: 0.965
* **F1-Score**: 0.965

###   Results

The model demonstrates strong performance on the validation set. Across three epochs, the validation accuracy reached 96.47%, with precision, recall, and F1-score also at 0.965. This indicates that the model effectively classifies sentiment in GitHub comments. Early stopping was employed with a patience of 2, suggesting that the model's best generalization performance was achieved relatively early in the training process.

##   Limitations

* **Domain Specificity**: The model is trained on GitHub comments and may not generalize well to other domains or types of text.
* **Language Bias**: The model is primarily trained on English text and may exhibit bias towards the language and style of communication prevalent in the GitHub community.
* **Data Bias**: The model's performance is limited by the quality and representativeness of the labeled data. Potential biases in the GitHub community (e.g., demographic or project-specific language) may be reflected in the model's predictions.
* **Active Learning Dependence**: The model's performance is tied to the effectiveness of the active learning strategy used. Different active learning approaches or labeling procedures could lead to different results.
* **Contextual Understanding**: The model may struggle with nuanced sentiment or sarcasm, which can be challenging even for humans to interpret without full context.

##   Recommendations

* Further research is needed to evaluate the model's generalizability to other software development platforms or communication channels.
* Exploring techniques to mitigate potential biases in the training data could improve the model's fairness and robustness.
* Investigating the use of contextualized embeddings or other advanced architectures could enhance the model's understanding of nuanced sentiment.
* The active learning methodology, particularly the hybrid uncertainty sampling approach with varying margin thresholds, could be explored further.

##   How to Use

To use this model, you can use the following code with the Transformers library:

1.  Install the Transformers library:

    ```bash
    pip install transformers
    ```

2.  Load the model and tokenizer:

    ```python
    from transformers import AutoModelForSequenceClassification, AutoTokenizer

    model = AutoModelForSequenceClassification.from_pretrained("iamohitkaushik1/distilbert-active-learning-github-sentiment")
    tokenizer = AutoTokenizer.from_pretrained("iamohitkaushik1/distilbert-active-learning-github-sentiment")
    ```

3.  Tokenize the input text and make predictions:

    ```python
    def predict_sentiment(text):
        inputs = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
        outputs = model(**inputs)
        predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
        predicted_class = torch.argmax(predictions, dim=-1).item()
        # Define a mapping from class indices to sentiment labels
        sentiment_labels = {0: 'Negative', 1: 'Neutral', 2: 'Positive'}
        predicted_label = sentiment_labels[predicted_class]
        return predicted_label #  return the predicted sentiment label

    # Example usage:
    text = "This pull request is awesome!"
    sentiment_class = predict_sentiment(text)
    print(f"The sentiment of the text is: {sentiment_class}")
    ```

##   Citation

Kaushik, M., Chahal, K.K. (2026). Boosting Sentiment Analysis in OSS: A Hybrid Active Learning Strategy Using Uncertainty Metrics. In: Chakravorty, A., Hussain, S., Kumari, R. (eds) Artificial Intelligence: Theory and Applications. AITA 2025. Lecture Notes in Networks and Systems, vol 1864. Springer, Cham. https://doi.org/10.1007/978-3-032-19179-3_24

##   Author Information

Mohit Kaushik, Kuljit Kaur Chahal

##   Contributions

Mohit Kaushik, Kuljit Kaur Chahal

---
library_name: transformers
datasets:
- SetFit/amazon_reviews_multi_en
metrics:
- accuracy
pipeline_tag: text-classification
tags:
- sentiment-analysis
- text-classification
- roberta
- transformers
- ecommerce
- customer-reviews
- amazon-reviews
- streamlit
---

# EcoPulse AI Sentiment Classifier

This model is the fine-tuned sentiment classification model used in **EcoPulse AI**, an e-commerce customer review sentiment classification and voice reporting system. The model classifies Amazon-style customer reviews into three sentiment categories:

* **Negative**
* **Neutral**
* **Positive**

The model is designed to help e-commerce customer support teams quickly identify customer dissatisfaction, monitor neutral feedback, and summarize positive customer experiences.

---

## Model Details

### Model Description

This model is a fine-tuned version of `cardiffnlp/twitter-roberta-base-sentiment-latest`. The base model was selected after comparing three Hugging Face transformer models for customer review sentiment classification. It achieved the strongest baseline accuracy among the tested candidates and was then fine-tuned on a balanced Amazon review dataset.

The model is used as **Pipeline 1** in the EcoPulse AI application. It takes raw customer review text as input and outputs a sentiment label with a confidence score. The Streamlit application then aggregates the predictions into sentiment distribution summaries, business recommendations, written reports, and audio briefings.

* **Developed by:** Junlei Wang and Zhuoyuan Zhang
* **Project:** EcoPulse AI
* **Model type:** RoBERTa-based sequence classification model
* **Language:** English
* **Task:** 3-class sentiment classification
* **Fine-tuned from:** `cardiffnlp/twitter-roberta-base-sentiment-latest`
* **Final model repository:** `zoeywwww/cardiffnlp-sentiment-3class-finetuned`

---

## Model Sources

* **Base model:** `cardiffnlp/twitter-roberta-base-sentiment-latest`
* **Fine-tuned model:** `zoeywwww/cardiffnlp-sentiment-3class-finetuned`
* **Dataset:** `SetFit/amazon_reviews_multi_en`
* **Demo application:** https://group10finalproject-ee3nfmeyomxalcieln8f8a.streamlit.app/
* **GitHub repository:** https://github.com/zoeywang524-beep/Group10_Final_project/blob/main/group10app.py

---

## Intended Use

### Direct Use

This model can be used directly for English e-commerce customer review sentiment classification. Given a customer review, it predicts one of three labels:

| Label ID | Label    |
| -------: | -------- |
|        0 | Negative |
|        1 | Neutral  |
|        2 | Positive |

Example use cases include:

* Classifying Amazon-style product reviews
* Monitoring customer satisfaction
* Identifying negative feedback for customer service escalation
* Supporting review summarization dashboards
* Generating structured sentiment inputs for business reports

### Downstream Use

This model is used inside the EcoPulse AI Streamlit Cloud application. In the deployed application, the model performs review-level sentiment classification. The app then uses the predictions to calculate sentiment distribution, generate support recommendations, produce a written customer sentiment report, and trigger a text-to-speech pipeline for an audio dashboard briefing.

The full system follows this workflow:

```text
Customer Review Text
        ↓
Fine-Tuned RoBERTa Sentiment Classifier
        ↓
Negative / Neutral / Positive Prediction + Confidence Score
        ↓
Streamlit Business Logic Layer
        ↓
Sentiment Summary + Support Recommendation + Written Report
        ↓
Text-to-Speech Pipeline
        ↓
Audio Dashboard Briefing
```

### Out-of-Scope Use

This model is not intended for high-stakes decision-making without human review. It should not be used as the sole basis for customer compensation, employee evaluation, legal judgment, or automated enforcement decisions.

The model may not perform well on:

* Sarcastic reviews
* Ambiguous or mixed-emotion reviews
* Very short reviews without enough context
* Non-English text
* Highly domain-specific product terminology
* Reviews that require external context to interpret correctly

---

## Bias, Risks, and Limitations

The model was fine-tuned on Amazon-style English review data. As a result, its performance is most relevant to e-commerce customer review classification and may not generalize equally well to other domains such as healthcare, finance, legal complaints, or social media conversations.

A known limitation is sarcasm detection. For example, a sentence such as:

> "Brilliant delivery, my package arrived completely crushed."

may be difficult because the word “Brilliant” is positive, while the full meaning of the sentence is negative. In the project’s manual Streamlit application test, the only misclassification occurred in a sarcastic review of this type.

Users should treat the model as a **first-line decision-support tool**, not a replacement for human judgment.

---

## Recommendations

Users should review low-confidence predictions and ambiguous cases manually. For business use, the model is best applied as an initial screening tool that helps support teams prioritize reviews for further investigation.

Recommended use:

* Use the model to flag likely negative reviews.
* Review sarcastic, mixed, or unclear cases manually.
* Combine model predictions with business rules and human oversight.
* Periodically update or fine-tune the model with newer customer review data.

---

## How to Get Started with the Model

You can use the model with the Hugging Face `transformers` library.

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np

model_name = "zoeywwww/cardiffnlp-sentiment-3class-finetuned"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

id2label = {
    0: "Negative",
    1: "Neutral",
    2: "Positive"
}

text = "The product arrived damaged and customer service did not respond."

inputs = tokenizer(
    text,
    return_tensors="pt",
    truncation=True,
    padding=True,
    max_length=128
)

with torch.no_grad():
    outputs = model(**inputs)

probabilities = torch.softmax(outputs.logits, dim=-1)[0].numpy()
predicted_id = int(np.argmax(probabilities))
predicted_label = id2label[predicted_id]
confidence = float(probabilities[predicted_id])

print("Predicted sentiment:", predicted_label)
print("Confidence:", round(confidence, 4))
```

---

## Training Details

### Training Data

The model was fine-tuned using the `SetFit/amazon_reviews_multi_en` dataset from Hugging Face. This dataset contains English Amazon review text and original star-rating labels.

The original 5-star labels were mapped into three sentiment classes:

| Original Rating Label | Star Rating Meaning | New Sentiment Label |
| --------------------: | ------------------- | ------------------- |
|                     0 | 1-star              | Negative            |
|                     1 | 2-star              | Negative            |
|                     2 | 3-star              | Neutral             |
|                     3 | 4-star              | Positive            |
|                     4 | 5-star              | Positive            |

### Dataset Splits Used in the Project

| Split                       | Number of Samples | Class Balance   | Purpose                    |
| --------------------------- | ----------------: | --------------- | -------------------------- |
| Preliminary training sample |             9,000 | 3,000 per class | Candidate model comparison |
| Fine-tuning training set    |             6,000 | 2,000 per class | Fine-tuning selected model |
| Validation set              |             1,500 | 500 per class   | Fine-tuning monitoring     |
| Test set                    |             1,500 | 500 per class   | Final evaluation           |

The fine-tuning set was balanced across the three sentiment classes to reduce class imbalance effects.

### Preprocessing

The preprocessing steps included:

1. Loading English Amazon review data.
2. Mapping 5-star labels into 3 sentiment labels.
3. Creating balanced negative, neutral, and positive samples.
4. Tokenizing review text using the tokenizer from `cardiffnlp/twitter-roberta-base-sentiment-latest`.
5. Truncating and padding input text to support transformer-based classification.

---

## Training Procedure

The base model `cardiffnlp/twitter-roberta-base-sentiment-latest` was selected after comparing three candidate transformer models:

| Candidate Model                                    | Baseline Accuracy |   Runtime |
| -------------------------------------------------- | ----------------: | --------: |
| `cardiffnlp/twitter-roberta-base-sentiment-latest` |            0.6228 | 60.71 sec |
| `distilbert-base-uncased`                          |            0.3287 | 32.17 sec |
| `roberta-base`                                     |            0.3306 | 61.68 sec |

The Cardiff RoBERTa model achieved the highest baseline accuracy and was selected for fine-tuning.

The selected model was fine-tuned for 1, 2, and 3 epochs. The Epoch 1 model was selected for deployment because it offered the best balance between validation loss, test performance, generalization stability, and runtime.

### Fine-Tuning Results

| Epoch | Validation Loss | Validation Accuracy | Train Accuracy | Test Accuracy | Test Runtime |
| ----: | --------------: | ------------------: | -------------: | ------------: | -----------: |
|     1 |          0.6777 |              0.7127 |         0.7848 |        0.7040 |    10.66 sec |
|     2 |          0.7371 |              0.7167 |         0.8613 |        0.7093 |    10.98 sec |
|     3 |          0.9523 |              0.7140 |         0.9205 |        0.7093 |    10.78 sec |

Although Epoch 2 and Epoch 3 achieved slightly higher test accuracy, the improvement was small. Training accuracy increased strongly from Epoch 1 to Epoch 3, while test accuracy remained almost unchanged. Validation loss also increased after Epoch 1, suggesting a higher risk of overfitting in later epochs.

Therefore, the Epoch 1 model was selected for deployment.

---

## Evaluation

### Testing Data

Final evaluation was conducted on an untouched balanced test set of 1,500 Amazon-style reviews:

* 500 negative reviews
* 500 neutral reviews
* 500 positive reviews

### Metrics

The main evaluation metric was accuracy. Runtime was also recorded during model comparison and testing to assess deployment feasibility.

### Results

The deployed fine-tuned model achieved:

| Metric              |     Value |
| ------------------- | --------: |
| Test Accuracy       |    0.7040 |
| Test Runtime        | 10.66 sec |
| Validation Loss     |    0.6777 |
| Validation Accuracy |    0.7127 |

### Streamlit Application Test

The deployed Streamlit Cloud application was manually tested using 10 unseen e-commerce customer review samples. The app correctly classified 9 out of 10 samples.

| Application Test Setting                      | Test Sample Size | Accuracy |
| --------------------------------------------- | ---------------: | -------: |
| Streamlit Cloud sentiment classification test |               10 |      90% |

The only misclassification occurred in a sarcastic review, showing a known limitation of sentiment models when handling sarcasm.

---

## Technical Specifications

### Model Architecture and Objective

This model uses a RoBERTa-based transformer architecture for sequence classification. The input review text is tokenized and passed into the transformer encoder. A classification head maps the encoded representation into three sentiment categories. A softmax layer is used to produce class probabilities.

Simplified architecture:

```text
Review Text
    ↓
Tokenizer
    ↓
RoBERTa Transformer Encoder
    ↓
Classification Head
    ↓
Softmax Probabilities
    ↓
Negative / Neutral / Positive
```

### Software

The project used:

* Python
* PyTorch
* Hugging Face Transformers
* Hugging Face Datasets
* Hugging Face Hub
* Google Colab
* Streamlit

### Compute Infrastructure

Fine-tuning and experiments were conducted in Google Colab. Exact hardware may vary depending on the assigned Colab runtime.

---

## Environmental Impact

Carbon emissions were not formally measured for this course project. Fine-tuning was conducted using Google Colab, and the training duration was limited by using a relatively small balanced fine-tuning dataset and only a small number of epochs.

---

## Citation

If you use this model, please cite the base model and dataset sources:

* Base model: `cardiffnlp/twitter-roberta-base-sentiment-latest`
* Dataset: `SetFit/amazon_reviews_multi_en`

---

## Model Card Authors

Junlei Wang
Zhuoyuan Zhang

---

## Model Card Contact

For questions about this course project, please refer to the EcoPulse AI project report, GitHub repository, and Streamlit application.

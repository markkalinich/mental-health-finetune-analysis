---
library_name: transformers
tags:
- sentiment-analysis
- aspect-based-sentiment-analysis
- transformers
- bert
language:
- tr
metrics:
- accuracy
base_model:
- dbmdz/bert-base-turkish-uncased
pipeline_tag: text-classification
datasets:
- Sengil/Turkish-ABSA-Wsynthetic
---


# Aspect Based Sentiment Analysis with Turkish 🇹🇷 Data

<!-- Provide a quick summary of what the model is/does. -->
This model performs **Aspect-Based Sentiment Analysis (ABSA) 🚀** for Turkish text. It predicts sentiment polarity (Positive, Neutral, Negative) towards specific aspects within a given sentence.

---

## Model Details

### Model Description

<!-- Provide a longer summary of what this model is. -->
This model is fine-tuned from the `dbmdz/bert-base-turkish-uncased` pretrained BERT model. It is trained on the **Turkish-ABSA-Wsynthetic** dataset, which contains Turkish restaurant reviews annotated with aspect-based sentiments. The model is capable of identifying the sentiment polarity for specific aspects (e.g., "servis," "fiyatlar") mentioned in Turkish sentences.

- **Developed by:** Sengil
- **Language(s):** Turkish 🇹🇷
- **License:** Apache-2.0
- **Finetuned from model:** `dbmdz/bert-base-turkish-uncased`
- **Number of Labels:** 3 (Negative, Neutral, Positive)

### Sources

<!-- Provide the basic links for the model. -->
- **Notebook:** [ABSA_Turkish_BERT_Based_uncased](https://www.kaggle.com/code/mertsengil/absa-train-w-synthetic-restaurant-reviews)

---
## Uses
<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

### Direct Use

This model can be used directly for analyzing aspect-specific sentiment in Turkish text, especially in domains like restaurant reviews.

### Downstream Use

It can be fine-tuned for similar tasks in different domains (e.g., e-commerce, hotel reviews, or customer feedback analysis).

### Out-of-Scope Use

- Not suitable for tasks unrelated to sentiment analysis or Turkish language.
- May not perform well on datasets with significantly different domain-specific vocabulary.

---

### Limitations

- May struggle with rare or ambiguous aspects not covered in the training data.
- May exhibit biases present in the training dataset.


## How to Get Started with the Model

<!-- This section provides code examples and links to further documentation. -->

```
!pip install -U transformers
```

Use the code below to get started with the model:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("Sengil/ABSA-Turkish-bert-based-uncased")
model = AutoModelForSequenceClassification.from_pretrained("Sengil/ABSA-Turkish-bert-based-uncased")

# Example inference
text = "Servis çok yavaştı ama yemekler lezzetliydi."
aspect = "servis"
formatted_text = f"[CLS] {text} [SEP] {aspect} [SEP]"

inputs = tokenizer(formatted_text, return_tensors="pt", padding="max_length", truncation=True, max_length=128)
outputs = model(**inputs)
predicted_class = outputs.logits.argmax(dim=1).item()

# Map prediction to label
labels = {0: "Negative", 1: "Neutral", 2: "Positive"}
print(f"Sentiment for '{aspect}': {labels[predicted_class]}")
```


## Training Details

### Training Data

Training Data
The model was fine-tuned on the Turkish-ABSA-Wsynthetic.csv dataset. The dataset contains semi-synthetic Turkish sentences annotated for aspect-based sentiment analysis.

- Training Procedure
- Optimizer: AdamW
- Learning Rate: 2e-5
- Batch Size: 16
- Epochs: 5
- Max Sequence Length: 128


## Evaluation

The model achieved the following scores on the test set:

- Accuracy: 95.56%
- F1 Score (Weighted): 95.67%


## Citation

```
@misc{absa_turkish_bert_based_uncased,
  title={Aspect-Based Sentiment Analysis for Turkish},
  author={Sengil},
  year={2024},
  url={https://huggingface.co/Sengil/ABSA_Turkish_BERT_Based_uncased}
}
```

## Model Card Contact

For any questions or issues, please open an issue in the repository or contact [LinkedIN](https://www.linkedin.com/in/mertsengil/).
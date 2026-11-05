---
library_name: transformers
tags:
- sentiment-analysis
- imdb
- text-classification
- distilbert
license: apache-2.0
datasets:
- stanfordnlp/imdb
language:
- en
metrics:
- accuracy
- precision
- recall
- f1
base_model:
- distilbert/distilbert-base-uncased
pipeline_tag: text-classification
---

# Model Card for DistilBERT Fine-Tuned on IMDB Sentiment Analysis

## Model Details

### Model Description

This model is a fine-tuned version of `distilbert-base-uncased` on the **IMDB movie reviews dataset** for **binary sentiment classification** (positive vs. negative). The model has been trained to classify movie reviews into either **positive (1)** or **negative (0)** sentiments.

- **Developed by:** Nikke Salonen
- **Finetuned from model:** `distilbert-base-uncased`
- **Language(s):** English
- **License:** Apache 2.0

### Model Sources
- **Repository:** https://huggingface.co/NikkeS/imdb-distilbert/
- **Dataset:** [IMDB Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)

## Uses

### Direct Use
- Sentiment analysis of **English text reviews**.
- Can be used for **opinion mining** on movie reviews and similar datasets.

### Downstream Use
- Can be **fine-tuned further** for sentiment classification in other domains (e.g., product reviews, social media sentiment analysis).

### Out-of-Scope Use
- Not suitable for **languages other than English**.
- Not recommended for **high-stakes decision-making** without human oversight.

## Bias, Risks, and Limitations

- The model is **trained on IMDB reviews**, so it may **not generalize well** to other types of sentiment analysis tasks.
- May exhibit **biases present in the training data**.
- Sentiment classification **depends heavily on context**, and the model may misinterpret sarcasm or complex sentences.

### Recommendations
- Users should **evaluate the model** on their specific datasets before deploying in production.
- If biases are detected, consider **fine-tuning on a more diverse dataset**.

## How to Use the Model

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load the fine-tuned model from Hugging Face Hub
model = AutoModelForSequenceClassification.from_pretrained("your-hf-username/imdb-distilbert")
tokenizer = AutoTokenizer.from_pretrained("your-hf-username/imdb-distilbert")

def predict_sentiment(review):
    inputs = tokenizer(review, return_tensors="pt", truncation=True, padding=True, max_length=256)
    with torch.no_grad():
        logits = model(**inputs).logits
    prediction = torch.argmax(logits, dim=1).item()
    return "Positive" if prediction == 1 else "Negative"

# Example Usage
print(predict_sentiment("This movie was absolutely fantastic!"))
print(predict_sentiment("The acting was terrible, and the story made no sense."))
```

## Training Details

### Training Data
- The model was fine-tuned on the IMDB dataset (50,000 labeled movie reviews).
- The dataset is balanced (25,000 positive and 25,000 negative reviews).
- The training split consisted of 40,000 samples, while 5,000 samples were used for validation.

### Training Procedure
#### Preprocessing
- Tokenized using `distilbert-base-uncased` tokenizer.
- Applied **dynamic padding, truncation, and a max sequence length of 256**.

#### Training Hyperparameters
- **Learning rate:** `5e-5`
- **Batch size:** `16`
- **Epochs:** `2`
- **Optimizer:** AdamW
- **Loss Function:** Cross-Entropy Loss

#### Compute Infrastructure
- **Hardware:** Google Colab T4 GPU
- **Precision:** Mixed precision (`fp16=True` for efficiency)

## Evaluation

### Testing Data, Factors & Metrics
#### Testing Data
- The model was evaluated on a 5,000-sample test set from the IMDB dataset.

#### Metrics
- **Accuracy:** 90,4%
- **Precision, Recall, F1-score:**
  - **Precision:** 92,1%
  - **Recall:** 88.2%
  - **F1-score:** 90.0%

## Model Examination
- The model performs well on **general sentiment classification** but may struggle with **sarcasm, irony, or very short reviews**.

## Environmental Impact
- **Hardware Type:** Google Colab T4 GPU
- **Training Time:** ~1 hour
- **CO2 Emission Estimate:** [Use ML Impact Calculator](https://mlco2.github.io/impact#compute)

## Citation
If you use this model, please cite:
```bibtex
@article{salonen2025imdb-distilbert,
  title={Fine-tuned DistilBERT for Sentiment Analysis on IMDB Reviews},
  author={Nikke Salonen},
  year={2025}
}
```

## More Information
- **Hugging Face Model Page:** https://huggingface.co/NikkeS/imdb-distilbert/.
- **Dataset:** [IMDB Dataset](https://ai.stanford.edu/~amaas/data/sentiment/)

## Model Card Authors
- [Nikke Salonen]

## Contact
For questions or issues, contact **nikke.salonen@gmail.com**.

---

This model card provides all necessary details, including **training info, evaluation results, and usage instructions**. Let me know if you'd like any modifications before uploading to **Hugging Face Hub**!
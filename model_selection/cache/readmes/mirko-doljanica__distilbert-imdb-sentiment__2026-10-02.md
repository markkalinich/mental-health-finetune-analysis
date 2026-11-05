---
language:
- en
datasets:
- imdb
library_name: transformers
tags:
- sentiment-analysis
- nlp
- distilbert
- imdb
- text-classification
---
# 🎬 DistilBERT IMDb Sentiment Classifier

This model is a fine-tuned version of **DistilBERT** for sentiment analysis on the [IMDb movie reviews dataset](https://ai.stanford.edu/~amaas/data/sentiment/).  
It classifies reviews into **positive** or **negative** sentiment with high accuracy.

---

## 📊 Model Details

- **Model type:** Transformer-based model (DistilBERT)
- **Task:** Sentiment Analysis / Text Classification
- **Framework:** Hugging Face Transformers (PyTorch)
- **Dataset:** IMDb (50,000+ labeled movie reviews)
- **Accuracy:** ~91.5% on test data

---

## 📁 Usage

You can load and use this model directly with `transformers`:

```python
from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="mirko-doljanica/distilbert-imdb-sentiment")
print(sentiment_pipeline("I loved this movie! The performances were amazing."))

## 📈 Results

| Metric       | Score |
|--------------|-------|
| Accuracy     | 0.915 |
| Precision    | 0.915 |
| Recall       | 0.915 |
| F1-score     | 0.915 |

These results were achieved after fine-tuning DistilBERT on the IMDb dataset with 2 epochs and a batch size of 8. The model performs consistently well on binary sentiment classification tasks.

```

## 📦 Applications

- 📊 **Review Analysis:** Automatically classify product, movie, or app reviews as positive or negative.  
- 💬 **Social Media Monitoring:** Analyze public sentiment from platforms like Twitter, Reddit, or forums.  
- 🧠 **Customer Feedback Analysis:** Segment user feedback into positive and negative categories for better decision-making.  
- 🔍 **Opinion Mining:** Detect trends in public opinion about topics, brands, or events.  
- 🧪 **Research & Prototyping:** Quickly integrate into NLP workflows for experimentation and benchmarking.

---

## ⚠️ Limitations & Bias

- 🗣️ **Language Restriction:** The model is trained on English text. Performance will degrade significantly for other languages without further fine-tuning.  
- 🎬 **Domain Bias:** Since the training data consists of movie reviews, performance might vary when used for other domains like finance, healthcare, or politics.  
- 🤖 **Data Bias:** The dataset may contain subjective or biased opinions reflecting societal stereotypes present in IMDb reviews.  
- 📉 **Nuance Handling:** The model might struggle with sarcasm, humor, or context-heavy statements that require deeper semantic understanding.

---

## 🛠️ How It Was Built

This model was built by fine-tuning the pre-trained [DistilBERT](https://huggingface.co/distilbert-base-uncased) model using the [IMDb movie reviews dataset](https://ai.stanford.edu/~amaas/data/sentiment/).  
The training process involved:
- Preprocessing text (tokenization, truncation, padding)
- Splitting into training and validation sets
- Fine-tuning for **2 epochs** with a **batch size of 8**
- Evaluation on the test set to measure accuracy, precision, recall, and F1-score

Training was done with the Hugging Face `transformers`, `datasets`, and `accelerate` libraries, leveraging PyTorch as the backend.

---

## 📚 Citation

If you use this model in your research, please cite it as follows:
@misc{distilbert_imdb_sentiment,
  author = {Mirko Doljanica},
  title = {DistilBERT IMDb Sentiment Classifier},
  year = {2025},
  howpublished = {\url{https://huggingface.co/mirko-doljanica/distilbert-imdb-sentiment}}
}
---

## 📬 Contact

**Author:** Mirko Doljanica  
- 🌐 Hugging Face: [mirko-doljanica](https://huggingface.co/mirko-doljanica)  
- 💻 GitHub: [mirko-doljanica](https://github.com/mirko-doljanica)  
- 📧 Email: [doljanicamir@gmail.com]  

Feel free to open issues, contribute, or reach out for collaborations.
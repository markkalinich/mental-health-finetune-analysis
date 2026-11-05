---
license: mit
language:
- en
metrics:
- accuracy
- f1
- recall
- precision
base_model:
- cardiffnlp/twitter-roberta-base-sentiment-latest
pipeline_tag: text-classification
tags:
- sentiment analysis
- movie reviews
---

# 🎬 Movie Reviews Sentiment Analysis Model
This model analyzes movie reviews and classify them as *"Negative"*, *"Positive"*, or *"Neutral"*. 
## Base Model
It is fine-tuned from ***"cardiffnlp/twitter-roberta-base-sentiment-latest"***.
## Dataset Used
Scraped 742 custom movie reviews from Rotten Tomatoes, augmented the data to 974 reviews 
to resolve class imbalance, and fine-tuned the final dataset on *"cardiffnlp/twitter-roberta-base-sentiment-latest"*.
## How to Use
from transformers import pipeline

classifier = pipeline(
   "text-classification",  
   model="hibbariz/movieReview_analysis_model"
)

result = classifier("This movie was absolutely amazing!")

print(result)
## Performance
**Accuracy** : 84%

**F1 score** : Negative: 81%, Neutral: 68%, Positive: 90%

## Classification Report

![Classification Report](https://cdn-uploads.huggingface.co/production/uploads/670e9b8635baa06da9ee4f8d/d8WQHJyacrsxh6BHLnZbO.png)


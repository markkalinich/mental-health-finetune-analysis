---
license: mit
pipeline_tag: text-classification
base_model: mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis
datasets:
- MAPAi/Inflation_News_Sentiment_Analysis
language:
- en
library_name: transformers
tags:
- finance
- sentiment-analysis
widget:
- text: Inflation will rise in the future days. FED is highly concerned...
---
# Model Card for MAPAi/InflaBERT

A BERT-based LLM fine-tuned (from https://huggingface.co/mrm8488/distilroberta-finetuned-financial-news-sentiment-analysis) to predict inflation-related sentiment in news.

### Training Data

Model trained on the MAPAi/inflation_news dataset: https://huggingface.co/datasets/MAPAi/inflation_news
---
datasets:
- hugginglearners/reddit-depression-cleaned
- mangoesai/DepressionDetection
- ziq/depression_tweet
metrics:
- accuracy
- precision
- recall
- f1
base_model:
- mental/mental-bert-base-uncased
---

# Model Card for MentalBERT Depression Detection

## Model Details

### Model Description

This MentalBERT-based model is fine-tuned to detect signs of depression from text input.  
It leverages the pretrained `mental/mental-bert-base-uncased` model and has been trained on multiple mental health datasets.  
It can assist in early screening of depressive symptoms through conversational AI applications.

### Load the Model

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

tokenizer = AutoTokenizer.from_pretrained("Twna-Jane16/Neurochat_MentalBERT_depression")
model = AutoModelForSequenceClassification.from_pretrained("Twna-Jane16/Neurochat_MentalBERT_depression")

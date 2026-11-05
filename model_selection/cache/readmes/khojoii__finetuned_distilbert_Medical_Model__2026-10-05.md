---
library_name: transformers
tags:
- text-classification
- transformers
- huggingface
- fine-tuned
- English
---

# Model Card for khojoii/text-classification-distilbert-fa

This is a fine-tuned DistilBERT model for binary text classification on a English-language dataset. The model was trained using the Hugging Face `Trainer` API and the `transformers` library.

## Model Details

### Model Description

This model is based on a pre-trained `distilbert-base-multilingual-cased` architecture and was fine-tuned on a custom English-language dataset for binary classification tasks (e.g., sentiment analysis or spam detection).

- **Developed by:** Khojoii
- **Model type:** Transformer - DistilBERT
- **Language(s):** English 
- **License:** free to use and change

## Uses

### Direct Use

This model can be directly used for inference on English text classification tasks. It takes in a English sentence and returns one of two classes.


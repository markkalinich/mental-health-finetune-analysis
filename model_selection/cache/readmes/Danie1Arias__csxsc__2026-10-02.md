---
license: mit
datasets:
- Danie1Arias/sentiment-analysis-catalan-reviews
base_model:
- projecte-aina/roberta-base-ca-v2
language:
- ca
tags:
- sentiment-analysis
- text-classification
- catalan
---

# Classificador de Sentiments a Xarxes Socials en Català (CSXSC)

This model is a fine-tuned version of [projecte-aina/roberta-base-ca-2](https://huggingface.co/projecte-aina/roberta-base-ca-v2) for **three-class sentiment analysis** (positive, negative, neutral) of Catalan-language texts from social media and reviews.

Developed as part of a Master's Thesis, the **CSXSC** model achieves high performance on sentiment classification while being exceptionally efficient, making it ideal for production environments. It was trained on the custom-built [Danie1Arias/sentiment-analysis-catalan-reviews]([Danie1Arias/sentiment-analysis-catalan-reviews](https://huggingface.co/datasets/Danie1Arias/sentiment-analysis-catalan-reviews)) dataset, which was specifically created and balanced for this task.

---
## Intended Uses

This model is designed for analyzing the sentiment of user-generated content in Catalan. It's particularly well-suited for:
* **Customer Feedback Analysis:** Automatically classify customer reviews on products or services.
* **Social Media Monitoring:** Track public opinion and brand sentiment on social platforms.
* **Opinion Mining:** Analyze sentiment in forum posts and comments.

---
## Model Details
* **Architecture:** RoBERTa (encoder-only)
* **Base Model:** [`projecte-aina/roberta-base-ca-v2`](https://huggingface.co/projecte-aina/roberta-base-ca-v2)
* **Language:** Catalan (`ca`)
* **Fine-tuning Task:** Sequence Classification
* **Labels:** `negative`, `neutral`, `positive`

---
## Training Procedure

The model was fine-tuned for 5 epochs using the AdamW optimizer with a learning rate of `2e-5`, a batch size of 32, and a weight decay of `0.01`. A linear learning rate scheduler with a warmup phase over the first 10% of training steps was employed. The final model selected was the one that achieved the highest **Quadratic Weighted Kappa (QWK)** score on the validation set, ensuring optimal generalization.

---
## Evaluation

The model was evaluated on a held-out test set, achieving the following results:

| Metric | Score |
|---|---|
| Accuracy | **83.69%** |
| F1 Macro | **0.8186** |
| Quadratic Weighted Kappa (QWK) | **0.8715** |

---
##  Limitations and Bias
* This model is specialized for general sentiment in social media and reviews. Its performance may degrade on highly specialized or technical domains (e.g., legal or medical texts).
* Like all language models, it may struggle with sarcasm, irony, or complex figurative language.
* The training data is sourced from public forums; therefore, the model may reflect biases present in that data.

---
## Usage Example

Here’s how to load and use the model to get human-readable predictions:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

# Load the model and tokenizer
model_name = "Danie1Arias/CSXSC"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Input text
text = "El servei ha estat una mica lent, però el menjar era boníssim." 
# -> "The service was a bit slow, but the food was delicious."

# Tokenize and predict
inputs = tokenizer(text, return_tensors="pt")
outputs = model(**inputs)
predicted_class_id = torch.argmax(outputs.logits, dim=1).item()

# Map the prediction ID to the label name
predicted_label = model.config.id2label[predicted_class_id]

print(f"Text: '{text}'")
print(f"Predicted Label: {predicted_label}")
# Expected output: Predicted Label: positive
```
---
## Citation & Repository

This model was developed as part of a Master's Thesis. If you use this model or its dataset in your research, please cite the original work.

The full code for data processing, training, and evaluation is available on GitHub:
[https://github.com/Danie1Arias/CSXSC/](https://github.com/Danie1Arias/CSXSC/)

```bibtex
@mastersthesis{arias2025csxsc,
  title={From Traditional to Large Language Models: A Novel NLP-Based Model for Sentiment Analysis in Social Media},
  author={Arias Cámara, Daniel},
  year={2025},
  school={Rovira i Virgili University}
}
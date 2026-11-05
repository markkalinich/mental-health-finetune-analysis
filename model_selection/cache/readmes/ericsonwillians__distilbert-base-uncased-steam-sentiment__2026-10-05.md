---
language: en
license: mit
datasets:
- steam_reviews
tags:
- sentiment-analysis
- text-classification
- transformers
- distilbert
- pytorch
metrics:
- accuracy
widget:
- text: This game blew my mind! Loved every minute.
library_name: transformers
pipeline_tag: text-classification
model_name: distilbert-base-uncased-steam-sentiment
base_model:
- distilbert/distilbert-base-uncased
---
```yaml
---
language: en
license: mit
datasets:
- steam_reviews
tags:
- sentiment-analysis
- text-classification
- transformers
- distilbert
- pytorch
metrics:
- accuracy
widget:
  - text: "This game blew my mind! Loved every minute."
library_name: transformers
pipeline_tag: text-classification
model_name: distilbert-base-uncased-steam-sentiment
---
```

# DistilBERT for Steam Reviews Sentiment Analysis

This repository provides a DistilBERT-based model fine-tuned on a dataset of Steam reviews to classify reviews as **Positive** or **Negative**. It is efficient and fast, making it ideal for large-scale or real-time applications.

## Model Description

- **Base Model:** [DistilBERT-base-uncased](https://huggingface.co/distilbert-base-uncased)  
- **Task:** Binary sentiment classification  
- **Trained On:** A large collection of user reviews from Steam  
- **Performance:** ~89% accuracy on the test set

This model is specifically trained on Steam reviews, where language can be raw and sometimes offensive. It may also work on other short text snippets like movie reviews, but please note that performance might degrade outside the gaming domain.

## Use Cases

- **Game Recommendation Systems:** Identify user sentiment towards titles to refine recommendation algorithms.  
- **Community Management:** Spot negative feedback early and improve customer support responses.  
- **Market Research & Insights:** Understand what features or aspects of a product users love or dislike.

## Installation Requirements

### Python & Environment Setup

- **Python version:** 3.10 or later recommended.
- **Package Manager:** [Poetry](https://python-poetry.org/) recommended, or you may use `pip`.

### Necessary Libraries

- [transformers](https://github.com/huggingface/transformers) (for loading and using the model)
- [torch](https://pytorch.org/) (for model inference and tensor operations)
- [rich](https://github.com/Textualize/rich) (for a more appealing command-line UI)
- [evaluate](https://github.com/huggingface/evaluate) (optional, for metrics if needed)
- [scikit-learn](https://scikit-learn.org/) (optional, if you want to train or evaluate metrics locally)

**Install with Poetry:**
```bash
poetry install
poetry shell
```

If using pip:
```bash
pip install torch transformers rich
```

## Model Files

After placing the model and tokenizer files in the repository root, you should have:
- `config.json`
- `model.safetensors` (or `pytorch_model.bin` if you used that format)
- `special_tokens_map.json`
- `tokenizer_config.json`
- `tokenizer.json`
- `vocab.txt`
- `training_args.bin` (optional, stores training parameters)
- `README.md` (this file)

## Running Inference

We provide an `inference.py` script that:
- Prompts the user for a review string.
- Loads the model and tokenizer directly from the current directory.
- Uses the model to predict whether the review is Positive or Negative.
- Displays probabilities and predictions using a rich UI.

### Example Inference

**Usage:**
```bash
python inference.py
```

**Example Output:**
```
Steam Review Sentiment Inference
Welcome!  
This tool uses a fine-tuned DistilBERT model to predict whether a given Steam review is *Positive* or *Negative*.

Please enter the Steam review text (This game is amazing!): This game is boring and repetitive

Loading model and tokenizer...
Running inference...
Inference Result
Predicted Sentiment: Negative
Sentiment Probabilities:
 Positive: 0.1234
 Negative: 0.8766
```

### Code Snippet for Direct Inference

If you want to run inference programmatically (without the script):

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "./"  # assuming model files are in current directory
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

review_text = "I absolutely loved this game!"
inputs = tokenizer(review_text, return_tensors="pt", truncation=True, padding="max_length", max_length=128)
with torch.no_grad():
    outputs = model(**inputs)
    probs = torch.softmax(outputs.logits, dim=1)
    predicted_class = torch.argmax(probs, dim=1).item()

sentiment = "Positive" if predicted_class == 1 else "Negative"
print(sentiment, probs.tolist())
```

## Limitations & Biases

- The model is trained on Steam reviews, where language can be harsh or contain slurs. It may inherit biases from the data.  
- Not guaranteed to understand sarcasm, humor, or context unrelated to gaming.  
- Results outside the gaming domain might be less accurate.

## License

This project is released under the [MIT License](./LICENSE).

## Contact & Feedback

If you have suggestions, want to contribute, or encounter issues, feel free to open a discussion or contact Ericson Willians (ericsonwillians@protonmail.com). Your feedback is appreciated!

---

With this setup, you can easily integrate this sentiment analysis model into your pipelines, dashboards, or research projects. Enjoy exploring the sentiment of Steam reviews!
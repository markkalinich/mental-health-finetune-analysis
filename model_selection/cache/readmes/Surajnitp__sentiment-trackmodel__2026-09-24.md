---
library_name: transformers
tags:
- sentiment-analysis
- text-classification
- distilbert
- imdb
- fine-tuned
license: apache-2.0
language:
- en
metrics:
- accuracy
pipeline_tag: text-classification
base_model: distilbert-base-uncased
---

# Sentiment Analysis – DistilBERT fine-tuned on IMDb

This model is a fine-tuned version of [DistilBERT base uncased](https://huggingface.co/distilbert-base-uncased) trained on a subset of the [IMDb movie reviews dataset](https://huggingface.co/datasets/stanfordnlp/imdb). It classifies text as **POSITIVE** or **NEGATIVE** with high confidence.

It was built as part of a learning project to demonstrate downloading, fine-tuning, and deploying models on Hugging Face Spaces.

## Model Details

- **Developed by:** Suraj Kumar ([Surajnitp](https://huggingface.co/Surajnitp))
- **Model type:** Transformer-based text classification
- **Language(s):** English
- **License:** Apache 2.0
- **Fine-tuned from:** [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased)
- **Model size:** 67M parameters
- **Hardware:** CPU (free Hugging Face Space)
- **Training time:** ~9 minutes

## Uses

### Direct Use

You can use this model for sentiment analysis of English movie reviews or any short English text. It outputs a label (`POSITIVE` or `NEGATIVE`) with a confidence score.

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="Surajnitp/sentiment-trackmodel")
result = classifier("I absolutely loved this film!")
print(result)
# [{'label': 'POSITIVE', 'score': 0.999...}]
```

### Out-of-Scope Use

The model is trained only on movie reviews and may not perform well on other domains (e.g., product reviews, social media). It is not suitable for factual or harmful content moderation without further fine-tuning.

## Bias, Risks, and Limitations

- The model reflects the biases present in the IMDb dataset (movie reviews from a specific demographic).
- It may struggle with sarcasm, nuanced opinions, or neutral statements.
- Training on a small subset (500 samples) limits its generalisation – performance may be lower on out-of-domain text.

## How to Get Started

```python
from transformers import pipeline

classifier = pipeline("sentiment-analysis", model="Surajnitp/sentiment-trackmodel")

print(classifier("This movie was fantastic!"))
print(classifier("The acting was terrible."))
```

You can also try it live on the [Space demo](https://huggingface.co/spaces/Surajnitp/Trackmodel).

## Training Details

### Training Data

- **Dataset:** Stanford NLP IMDb – 50,000 movie reviews.
- **Subset used:** 500 training samples, 100 test samples (for faster training on CPU).

### Training Procedure

The model was fine-tuned using the Hugging Face Trainer API with the following hyperparameters:

- Learning rate: 5e-5 (default)
- Batch size: 8 (train and eval)
- Epochs: 2
- Max sequence length: 256 tokens
- Optimizer: AdamW
- Loss function: Cross-entropy

### Evaluation Results

- Accuracy on test subset: ~87%
- Loss: ~0.18

These results are based on a small test set (100 samples) and may vary with larger evaluation.

## Environmental Impact

- **Hardware:** CPU (2 vCPU, 16 GB RAM)
- **Hours used:** ~0.15 hours (9 minutes)
- **Cloud Provider:** Hugging Face Spaces (free tier)
- **Compute Region:** US-East (by default)
- **Carbon Emitted:** Negligible (< 0.01 kg CO2eq)

## Citation

If you find this model useful, please consider citing:

```bibtex
@misc{sentiment-trackmodel,
  author = {Suraj Kumar},
  title = {Sentiment Analysis – DistilBERT fine-tuned on IMDb},
  year = {2026},
  publisher = {Hugging Face},
  howpublished = {\url{https://huggingface.co/Surajnitp/sentiment-trackmodel}}
}
```

## Contact

For questions or feedback, please open an issue on the [Space repository](https://huggingface.co/spaces/Surajnitp/Trackmodel).

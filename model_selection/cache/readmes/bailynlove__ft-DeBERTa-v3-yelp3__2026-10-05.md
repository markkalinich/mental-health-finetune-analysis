---
language:
- en
library_name: transformers
pipeline_tag: text-classification
base_model: microsoft/deberta-v3-base
datasets:
- mrcaelumn/yelp_restaurant_review_labelled
metrics:
- accuracy
- f1
tags:
- deberta-v3
- sentiment-analysis
- yelp
- restaurant-reviews
---

# DeBERTa v3 for Yelp three-class sentiment

This model fine-tunes [microsoft/deberta-v3-base](https://huggingface.co/microsoft/deberta-v3-base) to classify English restaurant reviews as **negative, neutral, or positive**. It produces three class scores, which can be converted to sentiment probabilities with softmax.

## How it was fine-tuned

The training script, `fine_tune_deBERTa.py`, loads the [Yelp restaurant review labelled dataset](https://huggingface.co/datasets/mrcaelumn/yelp_restaurant_review_labelled). It shuffles each split with seed 42, selects 500,000 reviews from the training split, and selects 20,000 reviews from the test split for evaluation during training. The dataset's labels are used directly, without remapping.

The model is loaded with `AutoModelForSequenceClassification` and a three-class classification head. Training updates the model parameters using the Hugging Face `Trainer`; the script does not freeze the backbone or use adapters. Reviews are tokenized with the base model's tokenizer, truncated to 512 tokens, and dynamically padded within each training batch.

| Setting | Value |
| --- | --- |
| Training epochs | 3 |
| Initial learning rate | 2e-5 |
| Weight decay | 0.01 |
| Training batch size per device | 8 |
| Gradient accumulation steps | 4 |
| Effective batch size per device | 32 |
| Evaluation batch size per device | 16 |
| Mixed precision | FP16 |
| Evaluation and checkpoint saving | Every epoch |
| Checkpoint selection | Best evaluation macro F1 |

The saved training state identifies `checkpoint-46875`, at epoch 3, as the best checkpoint. Its recorded evaluation accuracy is **91.86%** and macro F1 is **0.8325**. These results are from the 20,000-review subset used for checkpoint selection, rather than an additional independent final test set.

## What it can be used for

- Classifying the overall sentiment of English restaurant reviews.
- Producing negative, neutral, and positive probability features for review analysis and downstream research models.
- Supporting sentiment summaries or comparisons across collections of restaurant reviews.

In the accompanying project, `DeBERTa-v3_predict.py` applies softmax to the model's logits and saves the three probabilities in a `sentiment_probs` column. The downstream review-detection code accepts a three-value polarity feature alongside other review features. This checkpoint supplies sentiment information; it is not itself trained to classify reviews as fake, spam, or AI-generated.

## Output labels

The uploaded configuration retains generic label names. Interpret them using the training dataset's class order:

| Class ID | Configuration label | Sentiment |
| --- | --- | --- |
| 0 | `LABEL_0` | Negative |
| 1 | `LABEL_1` | Neutral |
| 2 | `LABEL_2` | Positive |

The documented evaluation covers Yelp restaurant reviews. Performance on other domains or languages has not been established by the supplied training record. Text beyond the 512-token input limit is truncated.

This card is based on the project's training and prediction scripts, the saved trainer state, and the cached training dataset metadata.

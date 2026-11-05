---
license: mit
language:
  - sq
library_name: transformers
pipeline_tag: fill-mask
base_model: FacebookAI/xlm-roberta-base
tags:
  - albanian
  - albanian-nlp
  - xlm-roberta
  - masked-language-model
  - social-media
  - social-media-nlp
  - informal-text
  - noisy-text
  - low-resource-nlp
  - domain-adaptive-pretraining
  - text-classification
  - sentiment-analysis
  - hate-speech-detection
  - dialect-detection
---

# AlbaSocialXLM-R

**AlbaSocialXLM-R** is a social-media-adapted XLM-RoBERTa model for Albanian. It is based on `FacebookAI/xlm-roberta-base` and was further adapted with continued masked language model pretraining on around **400,000 Albanian social-media comments**, including original and controlled synthetic social-media variants.

The model is mainly intended as a reusable encoder for Albanian **social-media classification tasks**, especially when the text is informal, noisy, dialectal, written without diacritics, or shaped by online communication style.

This model was developed for the paper:

**A Social-Media-Adapted Masked Language Model for Low-Resource Languages: Multi-Task Applications on Sentiment, Hate Speech, and Dialect Detection**

## Intended use

AlbaSocialXLM-R is designed for Albanian user-generated text, especially:

* social-media comments, posts, replies, and short reactions
* noisy or informal Albanian text
* Albanian text written without diacritics
* dialectal or regionally influenced Albanian writing
* news portal comments, forum-style messages, and chat-like text

It can be fine-tuned for tasks such as sentiment analysis, emotion detection, stance detection, hate speech detection, offensive language detection, toxicity classification, dialect detection, regional variety classification, topic classification, intent classification, public opinion mining, comment moderation research, and other Albanian social-media text mining tasks.

## Important note

This is a **masked language model**, not a ready-made classifier.

For classification tasks, use this checkpoint as the base encoder and fine-tune it with a classification head on your labelled dataset.

## How to use: masked-token prediction

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM, pipeline

model_id = "Endrit/AlbaSocialXLM-R"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForMaskedLM.from_pretrained(model_id)

fill_mask = pipeline("fill-mask", model=model, tokenizer=tokenizer)

predictions = fill_mask("ky sen nuk osht hiq <mask>")

for item in predictions:
    print(item["token_str"], item["score"])
```

## How to use: fine-tuning for classification

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification

model_id = "Endrit/AlbaSocialXLM-R"

tokenizer = AutoTokenizer.from_pretrained(model_id)

model = AutoModelForSequenceClassification.from_pretrained(
    model_id,
    num_labels=3,
    ignore_mismatched_sizes=True
)
```

Example label settings:

```python
# Sentiment classification
id2label = {0: "negative", 1: "neutral", 2: "positive"}

# Hate speech detection
id2label = {0: "non_hate", 1: "hate"}

# Dialect detection
id2label = {0: "AL", 1: "KS", 2: "MK"}
```

For sentence similarity, retrieval, or semantic search, additional sentence-embedding fine-tuning or post-processing is recommended because raw XLM-R embeddings are not optimized as standalone semantic embeddings.

## Training data

The model was adapted on Albanian social-media text from the training partitions of sentiment analysis, hate speech detection, and dialect detection datasets. The adaptation corpus combines original social-media comments with controlled LLM-generated variants.

Validation and test partitions were excluded from the MLM adaptation corpus. The original datasets and raw comments are not included in this repository.

## Training procedure

The model was initialized from `FacebookAI/xlm-roberta-base` and continued with the masked language modelling objective. The tokenizer was kept unchanged from XLM-R.

The released checkpoint corresponds to the **Social-original+augmented MLM** setting, using original and synthetic Albanian social-media comments for domain adaptation.

## Evaluation summary

In the associated paper, social-media adaptation improved performance across three Albanian social-media classification tasks: sentiment analysis, hate speech detection, and dialect detection.

Additional analysis showed that the adapted model better handles informal Albanian tokens, missing diacritics, dialectal forms, compressed expressions, and social-media-specific writing patterns.

## Limitations and responsible use

AlbaSocialXLM-R is not a general-purpose Albanian model trained from scratch. It is a continued-pretrained XLM-R model adapted to Albanian social-media text.

Because the adaptation data comes from online language, the model may reflect social-media biases, offensive expressions, political language, regional patterns, and platform-specific writing habits.

The model should not be used as the only basis for decisions affecting people. For hate speech, toxicity, moderation, or other sensitive applications, task-specific evaluation and human oversight are strongly recommended.

## License

This model is released under the MIT license.

## Citation

If you use this model, please cite the associated paper:

```bibtex
@article{fetahi2026albasocialxlmr,
  title={A Social-Media-Adapted Masked Language Model for Low-Resource Languages: Multi-Task Applications on Sentiment, Hate Speech, and Dialect Detection},
  author={Fetahi, Endrit and Schuster, Sebastian},
  year={2026}
}
```

## Repository

```text
https://huggingface.co/Endrit/AlbaSocialXLM-R
```

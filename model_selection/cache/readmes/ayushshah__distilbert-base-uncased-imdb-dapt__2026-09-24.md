---
datasets:
- stanfordnlp/imdb
language:
- en
base_model:
- distilbert/distilbert-base-uncased
license: apache-2.0
tags:
- masked-language-modeling
- dapt
- imdb
- mlm
library_name: transformers
---

# DistilBERT IMDb DAPT Model
This model is a DistilBERT encoder that has been further pretrained using Domain-Adaptive Pretraining (DAPT) on 50k IMDb movie reviews in the unsupervised split of the IMDb movie reviews dataset. The goal of this additional pretraining is to adapt the language representations of DistilBERT to the movie review domain, improving performance on downstream sentiment-related tasks.

The model can be used as:
- A feature extractor for sentiment analysis
- A starting point for fine-tuning on IMDb or similar review datasets
- A domain-adapted encoder for other NLP tasks involving movie reviews or opinionated text

A classifier based on this model for movie review sentiment analysis is [here](https://huggingface.co/ayushshah/distilbert-dapt-imdb-sentiment)

# Training Details
- **Base model**: [DistilBERT Base Uncased](https://huggingface.co/distilbert/distilbert-base-uncased)
- **Pretraining objective**: Masked Language Modeling (MLM)

# Domain-Adaptive Pretraining (DAPT)
- **Dataset**: [stanforfnlp/imdb](https://huggingface.co/datasets/stanfordnlp/imdb/)
- **Language**: English
- **Tokenization**: WordPiece
- Dynamic padding used during training
- Gradient accumulation used to simulate larger batch size

This DAPT step allows the model to better capture:
- Movie-related vocabulary
- Review-style language
- Sentiment-heavy expressions

# Intended Uses
**Supported Use Cases**
- Sentiment analysis on movie reviews
- Fine-tuning for downstream classification tasks
- Feature extraction for NLP research
- Educational and research purposes

**Out-of-Scope Uses**
- Medical, legal or financial decision-making
- Safety-critical or high-risk applications
- Tasks requiring factual correctness or reasoning beyond sentiment understanding

## Bias, Risks, and Limitations
- Inherits biases present in the IMDb dataset
- Performance depends heavily on downstream fine-tuning
- Not designed for multilingual or non-review text
- Not suitable for reasoning-heavy tasks

## Ethical Considerations
- IMDb reviews may reflect demographic, cultural or opinion biases
- Outputs should not be used to draw conclusions about individuals or groups
- This model should not be used for moderation or harmful profiling

### Training Hyperparameters
- Learning rate: 3e-5
- Optimizer: AdamW
- Epochs: 3
- Batch size: 16 with 4 gradient accumulation steps (Effective batch size 64)
- max_seq_length: 512
- Linear warmup: 5%
- Automatic mixed precision training

**Training stats**

Epoch 1: MLM Loss: 2.3581<br>
Epoch 2: MLM Loss: 2.2295<br>
Epoch 3: MLM Loss: 2.1622<br>

## License
This model follows the license of the base DistilBERT model. Please refer to the Hugging Face repository for license details.

## More information
- [DistilBERT Paper](https://arxiv.org/abs/1910.01108)
- [GitHub](https://github.com/AyushShahh/DistilBERT-IMDb)
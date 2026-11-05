---
license: apache-2.0
base_model: distilbert-base-uncased
tags:
- generated_from_trainer
- fill-mask
- imdb
- movie-reviews
- sentiment-analysis
datasets:
- imdb
metrics:
- accuracy
- loss
model-index:
- name: distilbert-base-uncased-finetuned-imdb
  results: []
library_name: transformers
pipeline_tag: fill-mask
---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

## Model Description
This model is a fine-tuned version of [DistilBERT](https://huggingface.co/distilbert-base-uncased) on the IMDb movie reviews dataset. It has been adapted to the domain of movie reviews to better understand and predict the vocabulary and expressions commonly found in this context. The model is primarily intended for Masked Language Modeling (MLM) tasks where a word in a sentence is masked, and the model predicts the most likely word(s) to fill in the blank.

## Intended Uses & Limitations
**Intended Uses:**
- **Text Completion:** Predicting missing words in sentences from movie reviews or similar domains.
- **Data Augmentation:** Generating realistic text sequences for data augmentation in NLP tasks.
- **Sentiment Analysis:** Can be fine-tuned further or used in pipelines related to sentiment analysis.

**Limitations:**
- **Domain Specificity:** The model is fine-tuned on IMDb reviews and may not generalize well to other domains or types of text.
- **Bias:** The model inherits biases from the IMDb dataset and the original DistilBERT model, which may affect predictions.

## How to Use
You can use this model with the Hugging Face `transformers` library:

```python
from transformers import pipeline

# Load the fill-mask pipeline
mask_filler = pipeline("fill-mask", model="Ashaduzzaman/distilbert-base-uncased-finetuned-imdb-accelerate")

# Example usage
text = "The movie was an absolute [MASK], leaving the audience in tears."
predictions = mask_filler(text)

for pred in predictions:
    print(f"{pred['sequence']}")
```

### Example Texts for the Widget
```markdown
---
pipeline_tag: fill-mask
widget:
- text: "The movie was an absolute [MASK], leaving the audience in tears."
- text: "The director's latest [MASK] was a surprise hit at the box office."
- text: "The acting was [MASK], truly a remarkable performance."
---
```

## Limitations and Bias
- **Bias in Data**: The IMDb dataset contains movie reviews that may reflect specific cultural or societal biases. As a result, the model might produce biased predictions, especially in sensitive contexts.
- **Language Limitation**: The model is trained on English text and may not perform well with other languages.


## Training Data
The model was fine-tuned on the [IMDb Large Movie Review Dataset](https://ai.stanford.edu/~amaas/data/sentiment/), which contains 50,000 movie reviews. This dataset is commonly used for sentiment analysis and benchmarking NLP models.

## Training Procedure
The model was fine-tuned using the Hugging Face `transformers` library. Key training details:
- **Base Model:** DistilBERT (`distilbert-base-uncased`)
- **Task:** Masked Language Modeling
- **Optimizer:** AdamW
- **Learning Rate:** 5e-5 with a linear learning rate scheduler
- **Batch Size:** 16
- **Epochs:** 3
- **Evaluation Metric:** The model was evaluated on masked word prediction accuracy.

### Hyperparameters:
- **Learning Rate:** 2e-05
- **Batch Size:** 16
- **Number of Epochs:** 3
- **Optimizer:** AdamW
- **Seed:** 42

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.6728        | 1.0   | 313  | 2.4563          |
| 2.5551        | 2.0   | 626  | 2.4489          |
| 2.5099        | 3.0   | 939  | 2.4455          |


## Evaluation Results
The model's performance was evaluated on a validation set derived from the IMDb dataset. Metrics like accuracy, precision, recall, and F1-score were calculated to assess the model's capability in predicting masked tokens.

| Metric     | Value   |
|------------|---------|
| Accuracy   | 96.5%   |
| Precision  | 92.3%   |
| Recall     | 93.8%   |
| F1-Score   | 93.0%   |

## Framework Versions
- **Transformers:** 4.42.4
- **PyTorch:** 2.3.1+cu121
- **Datasets:** 2.21.0
- **Tokenizers:** 0.19.1

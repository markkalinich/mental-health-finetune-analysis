---
license: apache-2.0
datasets:
- poem_sentiment
language:
- en
metrics:
- Accuracy, F1 score
library_name: transformers
pipeline_tag: text-classification
tags:
- text-classification
- sentiment-analysis
- poem-sentiment-detection
- poem-sentiment
- poem-sentiment-classification
- sentiment-classification
widget:
- text: >-
    Rapidly, merrily, Life's sunny hours flit by, Gratefully, cheerily, Enjoy them as they fly!
  example_title: "Life" 
- text: It so happens I am sick of my feet and my nails, and my hair and my shadow. It so happens I am sick of being a man.
  example_title: "Walking Around" 
- text: >-
    No man is an island, Entire of itself, Every man is a piece of the continent, A part of the main.
  example_title: "No man is an island" 
- text: >-
    Some have won a wild delight, By daring wilder sorrow; Could I gain thy love to-night, I'd hazard death to-morrow.
  example_title: "Passion" 
---
 ## AiManatee/RoBERTa_poem_sentiment 
This model is a fine-tuned version of the [FacebookAI/roberta-base](https://huggingface.co/FacebookAI/roberta-base) transformer for the task of poem sentiment analysis. It predicts the sentiment of a given poem verse into one of four categories: negative, positive, no impact, or mixed (positive and negative).

 ### Dataset
RoBERTa_poem_sentiment was trained on the [poem_sentiment](https://huggingface.co/datasets/poem_sentiment) dataset which consists of poem verses across four sentiment labels: negative, positive, no impact, and mixed sentiment. However, the Validation and Test subsets of the original dataset lack 'mixed' sentiment examples. To address this and ensure a thorough evaluation, data augmentation was performed: 32 'mixed' sentiment verses from different English poems were added to the Validation (16) and Test (16) subsets; the original Train subset remained intact. All the augmented samples were tested for semantic consistency, diversity (cosine similarity), length variation and novelty (ensuring the augmented data introduced new, relevant vocabulary). This strategy allowed for a more comprehensive evaluation of the model's generalization ability across all trained labels. The final model was tested on both the original dataset and the augmented dataset.

 #### Labels
```
{0: 'negative', 1: 'positive', 2: 'no_impact', 3: 'mixed'}
```

 ### Training Hyperparameters
```
  learning_rate: 2e-5,
  weight_decay: 0.01,
  batch_size: 16,
  num_epochs: 8,
  optimizer: AdamW: betas=(0.9, 0.999), eps=1e-08
  seed: 16
  early_stopper: min_delta=0.001, patience=3
```
```
  scheduler = ReduceLROnPlateau(
    optimizer,
    mode="min",
    factor=0.5,
    patience=0,
    threshold=0.001,
    eps=1e-8,
  )
```

 ### Model Performance
##### Validation results on the original dataset (class 3 is not being evaluated here)
| Epoch | Training Loss | Validation Loss | Accuracy | F1       |
|-------|---------------|-----------------|----------|----------|
| 1     | 1.365169      | 1.010353        | 0.761905 | 0.771733 |
| 2     | 0.860945      | 0.810045        | 0.723810 | 0.740809 |
| 3     | 0.570005      | 0.637439        | 0.761905 | 0.802184 |
| 4     | 0.355776      | 0.699637        | 0.780952 | 0.797572 |
| 5     | 0.252919      | 0.586395        | 0.847619 | 0.860519 |
| 6     | 0.156633      | 0.610439        | 0.819048 | 0.834072 |
| 7     | 0.084868      | 0.515130        | 0.876190 | 0.884736 |
| 8     | 0.062830      | 0.572643        | 0.885714 | 0.902510 |


 ##### Validation results on the augmented dataset
| Epoch | Training Loss | Validation Loss | Accuracy | F1       |
|-------|---------------|-----------------|----------|----------|
| 1     | 1.365169      | 1.168057        | 0.661157 | 0.628737 |
| 2     | 0.860945      | 0.869521        | 0.694214 | 0.717916 |
| 3     | 0.570005      | 0.637439        | 0.776859 | 0.790842 |
| 4     | 0.355776      | 0.681563        | 0.768595 | 0.776540 |
| 5     | 0.252919      | 0.585692        | 0.834710 | 0.841590 |
| 6     | 0.156633      | 0.542949        | 0.809917 | 0.815361 |
| 7     | 0.092444      | 0.581075        | 0.826446 | 0.830607 |
| 8     | 0.049480      | 0.583749        | 0.884297 | 0.881360 |


 ### How to Use the Model
Here is how to predict the sentiment of a poem verse using this model:

```python
from transformers import pipeline
sentiment_classifier = pipeline(task='text-classification', model='AiManatee/RoBERTa_poem_sentiment')
verse1 = "Rapidly, merrily, Life's sunny hours flit by, Gratefully, cheerily, Enjoy them as they fly!"
verse2 = "It so happens I am sick of my feet and my nails, and my hair and my shadow. It so happens I am sick of being a man."
verse3 = "No man is an island, Entire of itself, Every man is a piece of the continent, A part of the main."
verse4 = "Some have won a wild delight, By daring wilder sorrow; Could I gain thy love to-night, I'd hazard death to-morrow."
print(sentiment_classifier(verse1))
print(sentiment_classifier(verse2))
print(sentiment_classifier(verse3))
print(sentiment_classifier(verse4))
```

 ### Evaluation
 ##### Original dataset
```
{Loss: 0.5726433790155819
Accuracy: 0.8857142857142857
Precision: 0.9201298701298701
Recall: 0.8857142857142857
F1: 0.9025108225108224
}
```

 ##### Augmented dataset
```
{Loss: 0.5837492472492158
Accuracy: 0.8842975206611571
Precision: 0.8810538160090016
Recall: 0.8842975206611571
F1: 0.8813606847697756
}
```

 ### Framework Versions
- **Transformers:** 4.35.2
- **PyTorch:** 2.1.0+cu118
- **Datasets:** 2.16.1
- **Tokenizers:** 0.15.1
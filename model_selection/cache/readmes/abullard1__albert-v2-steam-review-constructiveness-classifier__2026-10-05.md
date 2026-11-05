---
license: mit
license_link: https://mit-license.org/
datasets:
- abullard1/steam-reviews-constructiveness-binary-label-annotations-1.5k
language:
- en
base_model: albert/albert-base-v2
pipeline_tag: text-classification
library_name: transformers
tags:
- steam-reviews
- BERT
- albert-base-v2
- text-classification
- sentiment-analysis
- constructiveness
- gaming
- sentiment-analysis
- text-classification
- fine-tuned
developers: 
- Samuel Ruairí Bullard
- Marco Schreiner
thumbnail: https://i.ibb.co/Ky0wcYy/abullard1-steam-review-constructiveness-classifier-logo-modified-1.png
spaces: abullard1/steam-review-constructiveness-classifier
inference: true
widget:
- text: "Review: I think this is a great game but it still has some room for improvement., Playtime: 12, Voted Up: True, Upvotes: 1, Votes Funny: 0"
  example_title: "Constructive Review"
- text: "Review: Trash game. Deleted., Playtime: 1, Voted Up: False, Upvotes: 0, Votes Funny: 0"
  example_title: "Non-Constructive Review"

model-index:
  - name: albert-v2-steam-review-constructiveness-classifier
    results:
      - task:
          type: text-classification
        dataset:
          name: abullard1/steam-reviews-constructiveness-binary-label-annotations-1.5k
          type: abullard1/steam-reviews-constructiveness-binary-label-annotations-1.5k
        metrics:
          - name: Accuracy
            type: accuracy
            value: 0.796
          - name: Precision
            type: precision
            value: 0.800
          - name: Recall
            type: recall
            value: 0.818
          - name: F1-score
            type: f1
            value: 0.794
---
<br>
<br>
<div style="text-align: center;">
    <img src="https://i.ibb.co/Ky0wcYy/abullard1-steam-review-constructiveness-classifier-logo-modified-1.png" style="max-width: 30%; display: block; margin: 0 auto;">
</div>

<br>
<br>
<br>

<div style="text-align: center;">
    <b></b><h1>Fine-tuned ALBERT Model for Constructiveness Detection in Steam Reviews</h1></b>
</div>
<hr>

## <u>Model Summary</u>

This model is a fine-tuned version of **albert-base-v2**, designed to classify whether Steam game reviews are constructive or non-constructive. It was trained on the *[steam-reviews-constructiveness-binary-label-annotations-1.5k](https://huggingface.co/datasets/abullard1/steam-reviews-constructiveness-binary-label-annotations-1.5k)* dataset, containing user-generated game reviews labeled as either:
- **1 (constructive)**
- **0 (non-constructive)**

The dataset features were combined into a single string per review, formatted as follows:
<br>
<br>
"Review: **{review}**, Playtime: **{author_playtime_at_review}**, Voted Up: **{voted_up}**, Upvotes: **{votes_up}**, Votes Funny: **{votes_funny}**" and then fed to the model accompanied by the respective ***constructive*** labels. 
<br>
<br>
This approach of concatenating the features into a simple String offers a good trade-off between complexity and performance, compared to other options.

### Intended Use

The model can be applied in any scenario where it's important to distinguish between helpful and unhelpful textual feedback, particularly in the context of gaming communities or online reviews. Potential use cases are platforms like **Steam**, **Discord**, or any community-driven feedback systems where understanding the quality of feedback is critical.

### Limitations

- **Domain Specificity**: The model was trained on Steam reviews and may not generalize well outside gaming.
- **Dataset Imbalance**: The training data has an approximate **63.04%-36.96%** split between non-constructive and constructive reviews.

<hr>

## <u>Evaluation Results</u>

The model was trained and evaluated using a **80/10/10 Train/Dev/Test** split, achieving the following performance metrics during evaluation using the test set:

- **Accuracy**: 0.80
- **Precision**: 0.80
- **Recall**: 0.82
- **F1-score**: 0.79

These results indicate that the model performs reasonably well at identifying the correct label. (~80%)

<hr>

## <u>How to Use</u>

### Huggingface Space
Explore and test the model interactively on its *[Hugging Face Space](https://huggingface.co/spaces/abullard1/steam-review-constructiveness-classifier)*.

### Transformers Library
To use the model programmatically, use this Python snippet:

```python
from transformers import pipeline
import torch

device = 0 if torch.cuda.is_available() else -1
torch_d_type = torch.float16 if torch.cuda.is_available() else torch.float32

base_model_name = "albert-base-v2"

finetuned_model_name = "abullard1/albert-v2-steam-review-constructiveness-classifier"

classifier = pipeline(
    task="text-classification",
    model=finetuned_model_name,
    tokenizer=base_model_name,
    device=device,
    top_k=None,
    truncation=True,
    max_length=512,
    torch_dtype=torch_d_type)

review = "Review: I think this is a great game but it still has some room for improvement., Playtime: 12, Voted Up: True, Upvotes: 1, Votes Funny: 0"
result = classifier(review)
print(result)
```

## License

This model is licensed under the *[MIT License](https://mit-license.org/)*, allowing open and flexible use of the model for both academic and commercial purposes.
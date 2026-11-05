---
language:
  - en
  - it
  - es
  - fr
  - de
license: apache-2.0
library_name: transformers
tags:
  - sentiment-analysis
  - text-classification
  - multilingual
  - restaurants
  - 5-star
base_model: jhu-clsp/mmBERT-base
pipeline_tag: text-classification
---

# 🍜 Multilingual Restaurant Review Sentiment Model 🌍

Hey there! This isn't just _another_ sentiment model. This is a fine-tuned powerhouse specifically designed to understand the nuance of 1-to-5 star restaurant reviews across **5 different languages**.

It was trained on a massive, perfectly balanced dataset of **400,000+ real, human-written, reviews** and achieves state-of-the-art performance.

## ✨ Model Features

- **Multilingual:** Trained on **English**, **Italian**, **Spanish**, **French**, **German**.
- **5-Star Specialist:** Predicts ratings on a 1-5 star scale.
- **SOTA Performance:** Achieves an incredibly low **MAE of ~0.29**. (More on that below!)

---

## 🎯 Just How Good Is It? (Performance)

Forget accuracy. For star ratings, **Mean Absolute Error (MAE)** is what matters. It measures how "off" the prediction is.

What does that mean? It means on average, the model's prediction is **only off by 0.29 stars**.

- It _knows_ a 5-star is close to a 4-star.
- It _knows_ a 1-star is NOT a 5-star.
- It **rarely** confuses a positive review for a negative one.

Here are the full results from the validation set (500k real-world reviews!):

| Metric       | Score     | Why it Matters                                               |
| :----------- | :-------- | :----------------------------------------------------------- |
| **MAE**      | **0.293** | 🏆 **The model main score.**                                 |
| **Accuracy** | 78.2%     | How often the model guess the _exact_ star (after rounding). |
| **Macro F1** | 0.683     | Shows it's good at all classes, not just the majority class. |
| **MSE**      | 0.182     | The loss the model was trained on (Mean Squared Error).      |

---

### Confusion Matrix

This shows where the model makes its errors. As you can see, almost all errors are "off-by-one" (like predicting a 4 for a 5-star), which is exactly what we want.

|            | **Predicted 1** | **Predicted 2** | **Predicted 3** | **Predicted 4** | **Predicted 5** |
| :--------- | :-------------: | :-------------: | :-------------: | :-------------: | :-------------: |
| **True 1** |      14683      |      8391       |       568       |       44        |       34        |
| **True 2** |      2504       |      13699      |      4068       |       95        |       13        |
| **True 3** |       290       |      6271       |      23824      |      5700       |       229       |
| **True 4** |       18        |       267       |      6940       |      66361      |      25089      |
| **True 5** |       44        |       143       |       553       |      47873      |     272298      |

---

### Performance Per Language

The model performs strongly across all five languages. Here is the final accuracy for each language on the test set:

| Region    | Accuracy |
| :-------- | :------- |
| `English` | 0.827    |
| `Italian` | 0.778    |
| `Spanish` | 0.775    |
| `French`  | 0.763    |
| `German`  | 0.755    |

---

## 🧠 The "Regression Trick" (Why it's so good)

Most models do "classification" (is it A, B, or C?). This is a bad fit for star ratings.

This model was trained as a **regression** task. It predicts a single number (like 4.7, 1.2, or 3.5) instead of just "5-star". This teaches the model that 4-stars are "closer" to 5-stars than 1-star is, which is how it gets such a low MAE.

---

## 🚀 How to Use

Since this is a regression model, the output is a single float number. You'll want to round it to get a final "star" rating.

### ⚠️ A Critical Note on Input Format

**This is very important for getting the best performance!**

This model was not just trained on review text; it was trained using a specific format that includes **both the review title and the review text**, separated by the `[SEP]` token.

The title often contains a powerful summary of the sentiment (e.g., "Best Pasta Ever!" or "Total Rip-off!"). Using this format ensures the model gets the same type of input it was trained on.

**Correct Format:**
`input_text = review_title + " [SEP] " + review_text`

If you only have the review text, the model will still work well, but performance will be slightly lower.

### Pipeline Usage Example

Here is how you should format your inputs before passing them to the pipeline:

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline
import numpy as np # Make sure to import numpy

model_name = "Festooned/Multilingual-Restaurant-Reviews-Sentiment"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# ---
# IMPORTANT: This model predicts a single number (regression).
# ---

# Let's create a pipeline
sentiment_pipe = pipeline("text-classification", model=model, tokenizer=tokenizer)

# Example reviews using the recommended format
reviews = [
    "Absolutely incredible [SEP] This was the best pasta I've ever had in my life.", # 5-star
    "Servicio terrible [SEP] El servicio fue terrible y la comida tardó una hora en llegar.", # 1-star
    "It was fine [SEP] It was... fine. Nothing special, but not bad either." # 3-star
]

# Get the raw predictions
raw_preds = sentiment_pipe(reviews)
print(raw_preds)
# [{'label': 'LABEL_0', 'score': 4.81}]
# [{'label': 'LABEL_0', 'score': 1.12}]
# [{'label': 'LABEL_0', 'score': 2.95}]

# ---
# How to get the actual "star rating"
# (Remember our labels are 0-4, so we add 1)
# ---
for text, pred in zip(reviews, raw_preds):
    # 'score' is the raw regression value (our model predicts 0-4)
    raw_score = pred['score']

    # Round and clamp to be safe (0-4)
    star_label_rounded = np.clip(round(raw_score), 0, 4)

    # Add 1 to get the 1-5 star rating
    final_star_rating = int(star_label_rounded + 1)

    print(f"Review: {text[:40]}...")
    print(f"  Final Rating: {final_star_rating} stars\n")
```

---

## 💡 Bonus: Convert to 3 Classes (Bad/Neutral/Good)

This 5-star model is flexible! If you don't need 5 classes, you can easily group the results.

Here's a simple helper function to convert the 1-5 star rating into **Bad**, **Neutral**, or **Good**.

```python
def to_3_class(rating):
    """Converts a 1-5 star rating into a 3-class sentiment."""
    # The 'rating' is the rounded 1-5 star value
    if rating <= 2:
        return "😞 Bad"
    elif rating == 3:
        return "😐 Neutral"
    else: # 4 or 5 stars
        return "😄 Good"

# Example using the rounded rating from the code above:
# Let's say a review got a rounded rating of 1
rating_1 = 1
print(f"Rating {rating_1} is: {to_3_class(rating_1)}")

# Let's say a review got a rounded rating of 3
rating_3 = 3
print(f"Rating {rating_3} is: {to_3_class(rating_3)}")

# Let's say a review got a rounded rating of 5
rating_5 = 5
print(f"Rating {rating_5} is: {to_3_class(rating_5)}")

Output:
Rating 1 is: 😞 Bad
Rating 3 is: 😐 Neutral
Rating 5 is: 😄 Good
```

---

## 🧪 Bonus: A Test of Specialization (Domain Shift)

This model is a SOTA-level _restaurant_ critic. But what happens if it's asked to review a car mechanic or a hair salon?

To find out, the model was tested on the **`yelp_review_full`** dataset. This dataset is **not** just restaurants; it includes reviews for auto shops, plumbers, gyms, salons, and all other business types.

The results are exactly what would be expected from a highly trained specialist:

| Metric       | Score on Restaurant-Only Data | Score on `yelp_review_full` (All businesses) |
| :----------- | :---------------------------: | :------------------------------------------: |
| **MAE**      |          **0.2928**           |                    0.4648                    |
| **Accuracy** |           **78.2%**           |                    62.7%                     |

---

## Citation

If you use this model in your research or app, please give it a shout-out!

```bibtex
@misc{adobati-2025-multilingual-restaurant,
  author = {Simone Adobati},
  title = {A Multilingual 5-Class Restaurant Review Sentiment Model},
  year = {2025},
  publisher = {Hugging Face},
  journal = {Hugging Face Model Hub},
  howpublished = {\url{[https://huggingface.co/](https://huggingface.co/)[Festooned/Multilingual-Restaurant-Reviews-Sentiment]}}
}
```

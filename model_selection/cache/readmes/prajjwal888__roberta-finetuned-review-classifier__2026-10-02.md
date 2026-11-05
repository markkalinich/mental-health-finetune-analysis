---
library_name: transformers
tags:
  - sentiment-analysis
  - roberta
  - text-classification
  - huggingface
  - amazon-reviews
  - fine-tuned
  - customer-feedback
license: apache-2.0
---

# RoBERTa Fine-Tuned Review Classifier

This is a fine-tuned RoBERTa model built for binary sentiment classification of Amazon product reviews. The model classifies reviews into `LABEL_0` (negative) or `LABEL_1` (positive), and has been integrated into a Chrome extension that predicts numeric ratings based on review text.

---

## Model Details

### Model Description

- **Model:** roberta-base
- **Task:** Binary sentiment classification
- **Labels:**  
  - `LABEL_0`: Negative review → *(Rating 1–4)*  
  - `LABEL_1`: Positive review → *(Rating 7–10)*
- **Language:** English
- **License:** Apache 2.0
- **Author:** [Prajjwal Chouhan](https://huggingface.co/prajjwal888)
- **Model repo:** [https://huggingface.co/prajjwal888/roberta-finetuned-review-classifier](https://huggingface.co/prajjwal888/roberta-finetuned-review-classifier)

---

## Model Sources

- **Base Model:** [`roberta-base`](https://huggingface.co/roberta-base)
- **Fine-tuning & Deployment:** Hugging Face + FastAPI (on Render)
- **Demo Frontend:** Chrome extension (injects rating predictions on Amazon product pages)

---

## Use Cases

### Direct Use
You can use this model to predict sentiment or approximate ratings of customer reviews. It's ideal for:

- Product feedback classification
- Chrome extensions or browser tools
- E-commerce dashboards

### Downstream Use
Can be used in:
- Recommender systems
- Review authenticity/fraud detection
- Customer satisfaction prediction

### Out-of-Scope Use
- Reviews in non-English languages
- Sarcastic or ambiguous tone detection
- Fine-grained star rating (e.g., 3 vs. 4)

---

## Bias, Risks & Limitations

### Bias
Model may inherit biases from training data—especially in underrepresented product categories or reviewer demographics.

### Limitations
- Struggles with sarcastic or short reviews.
- Works only on English-language text.
- Predictions may be unreliable for very long reviews (truncated at 512 tokens).

### Recommendations
- Do not use this model for making critical business decisions without human verification.
- Fine-tune on domain-specific reviews if required.

---

## How to Get Started

```python
from transformers import pipeline

classifier = pipeline("text-classification", model="prajjwal888/roberta-finetuned-review-classifier")
result = classifier("The product quality is fantastic. Loved it!")
print(result)
````

Example Output:

```json
[{"label": "LABEL_1", "score": 0.9987}]
```

---

## Training Details

### Dataset

Custom dataset scraped and labeled from Amazon product reviews. Labeled into two categories based on review sentiment (not star ratings).

### Preprocessing

* Lowercasing
* Removal of HTML and special characters
* Truncated to 512 tokens

### Training Hyperparameters

| Hyperparameter | Value |
| -------------- | ----- |
| Epochs         | 3     |
| Batch size     | 16    |
| Max length     | 512   |
| Optimizer      | AdamW |
| Learning rate  | 2e-5  |
| Precision      | fp16  |

---

## Evaluation

### Metrics

| Metric    | Value   |
| --------- | ------- |
| Accuracy  | \~91%   |
| F1 Score  | \~90.5% |
| Precision | \~90%   |
| Recall    | \~91%   |

Evaluation was performed on a 20% held-out validation set from the same distribution.

---

## Environmental Impact

* **Hardware Used:** NVIDIA T4 GPU
* **Platform:** Google Colab + Render
* **Training Duration:** \~1.5 hours
* **Estimated CO₂ Emissions:** \~0.3 kg
  *(based on [ML CO2 Impact Calculator](https://mlco2.github.io/impact#compute))*

---

## Technical Specifications

* **Model Type:** Transformer Encoder (RoBERTa)
* **Architecture:** 12-layer, 768-hidden, 12-heads, \~125M parameters
* **Framework:** PyTorch (via `transformers`)

---

## Citation


@misc{prajjwal888_review_classifier_2024,
  title={RoBERTa Fine-Tuned Review Classifier},
  author={Prajjwal Chouhan},
  year={2024},
  howpublished={\url{https://huggingface.co/prajjwal888/roberta-finetuned-review-classifier}},
}


---

## Contact

* GitHub: [@prajjwal888](https://github.com/prajjwal888)
* LinkedIn: [Prajjwal Chouhan](https://www.linkedin.com/in/prajjwal888/)

---

## Acknowledgments

Thanks to the Hugging Face community and the creators of `roberta-base`. This project is inspired by practical applications of NLP in e-commerce.

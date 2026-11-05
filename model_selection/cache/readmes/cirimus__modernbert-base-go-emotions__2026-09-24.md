---

language: en  
tags:

- text-classification
- pytorch
- ModernBERT
- emotions
- multi-class-classification
- multi-label-classification  
datasets:
- go_emotions  
license: mit  
metrics:
- accuracy
- f1
- precision
- recall
- matthews_correlation  
base_model:
- answerdotai/ModernBERT-base  
widget:
- text: I am thrilled to be a part of this amazing journey!
- text: I feel so disappointed with the results.
- text: This is a neutral statement about cake.  
library_name: transformers

---

![banner](https://huggingface.co/cirimus/modernbert-base-go-emotions/resolve/main/banner-03-2026.png)

# ModernBERT Go Emotions 2026-03

> Note: This version significantly improves the [baseline 2025 model](https://huggingface.co/cirimus/modernbert-base-go-emotions-2025-01).

### Overview

This model was fine-tuned from [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) dataset for multi-label classification. It predicts emotional states in text, with a total of 28 possible labels. Each input text can have one or more associated labels, reflecting the multi-label nature of the task.

Try it out [here](https://huggingface.co/spaces/cirimus/modernbert-go-emotions).

---

### Intended Use

The model is designed for emotion classification in English-language text, particularly in domains such as:

- Social media sentiment analysis
- Customer feedback evaluation
- Behavioral or psychological research

---


### Example Usage

Here’s how to use the model with Hugging Face Transformers:

```python
from transformers import pipeline
import torch

# Load the model
classifier = pipeline(
    "text-classification", 
    model="cirimus/modernbert-base-go-emotions",
    top_k=5
)

text = "I am so happy and excited about this opportunity!"
predictions = classifier(text)

# Print top 5 detected emotions
print("\nTop 5 emotions detected:")
for pred in predictions[0]:  # Note: predictions is [[...]] format
    print(f"\t{pred['label']:10s} : {pred['score']:.3f}")

# Example output
# Top 5 emotions detected:
#        excitement : 0.976
#        joy        : 0.698
#        approval   : 0.012
#        optimism   : 0.007
#        admiration : 0.006
```
---


### Model Details

- **Base Model**: [ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base)
- **Fine-Tuning Dataset**: [GoEmotions](https://huggingface.co/datasets/go_emotions)
- **Number of Labels**: 28
- **Problem Type**: Multi-label classification
- **Language**: English
- **License**: [MIT](https://opensource.org/licenses/MIT)
- **Fine-Tuning Framework**: Hugging Face Transformers
- **Release**: March 2026
- **Version**: 2026-03 (Optimized)

## Training Improvements


| Parameter               | Baseline | 2026-03                                         |
| ----------------------- | -------- | ----------------------------------------------- |
| Learning Rate           | 2e-5     | **1.8e-4**                                      |
| LR Schedule             | Linear   | **Cosine + Warmup**                             |
| Optimizer               | AdamW    | **Adafactor**                                   |
| Weight Decay            | 0.01     | **0.001**                                       |
| Batch Size              | 16       | **32**                                          |
| **New**: EMA            | None     | **0.999 decay**                                 |
| **New**: Dropout Tuning | Default  | **Classifier: 0.1, Attention: 0.05, MLP: 0.05** |


### Overall Results


| Split      | Accuracy | Precision | Recall | Macro F1  | Micro F1  |
| ---------- | -------- | --------- | ------ | --------- | --------- |
| Train      | 0.976    | 0.746     | 0.508  | **0.573** | **0.672** |
| Validation | 0.971    | 0.622     | 0.444  | **0.498** | **0.603** |
| Test       | 0.971    | 0.652     | 0.443  | **0.550** | **0.607** |


---

### Dataset

The [GoEmotions](https://huggingface.co/datasets/google-research-datasets/go_emotions) dataset is a multi-label emotion classification dataset derived from Reddit comments. It contains 58,000 examples with 28 emotion labels (e.g., admiration, amusement, anger, etc.), and it is annotated for multi-label classification.

---

### Evaluation Results

The model was evaluated on the test split of the GoEmotions dataset, using a threshold of `0.5` for binarizing predictions. The overall metrics were:

**Standard Results**:

Using the default threshold of 0.5.


| Label          | Accuracy | Precision | Recall | F1    | MCC   | Support | Threshold |
| -------------- | -------- | --------- | ------ | ----- | ----- | ------- | --------- |
| **macro avg**  | 0.971    | 0.652     | 0.443  | 0.500 | 0.506 | 5427    | 0.5       |
| admiration     | 0.947    | 0.719     | 0.712  | 0.716 | 0.687 | 504     | 0.5       |
| amusement      | 0.985    | 0.805     | 0.905  | 0.852 | 0.846 | 264     | 0.5       |
| anger          | 0.970    | 0.639     | 0.384  | 0.479 | 0.481 | 198     | 0.5       |
| annoyance      | 0.941    | 0.509     | 0.172  | 0.257 | 0.272 | 320     | 0.5       |
| approval       | 0.943    | 0.637     | 0.291  | 0.399 | 0.406 | 351     | 0.5       |
| caring         | 0.977    | 0.561     | 0.274  | 0.368 | 0.382 | 135     | 0.5       |
| confusion      | 0.975    | 0.594     | 0.373  | 0.458 | 0.459 | 153     | 0.5       |
| curiosity      | 0.952    | 0.538     | 0.542  | 0.540 | 0.515 | 284     | 0.5       |
| desire         | 0.987    | 0.604     | 0.386  | 0.471 | 0.476 | 83      | 0.5       |
| disappointment | 0.974    | 0.655     | 0.126  | 0.211 | 0.280 | 151     | 0.5       |
| disapproval    | 0.953    | 0.548     | 0.255  | 0.348 | 0.353 | 267     | 0.5       |
| disgust        | 0.981    | 0.618     | 0.382  | 0.472 | 0.477 | 123     | 0.5       |
| embarrassment  | 0.995    | 0.750     | 0.405  | 0.526 | 0.549 | 37      | 0.5       |
| excitement     | 0.984    | 0.648     | 0.340  | 0.446 | 0.462 | 103     | 0.5       |
| fear           | 0.992    | 0.714     | 0.705  | 0.710 | 0.705 | 78      | 0.5       |
| gratitude      | 0.991    | 0.952     | 0.906  | 0.929 | 0.924 | 352     | 0.5       |
| grief          | 0.999    | 0.000     | 0.000  | 0.000 | 0.000 | 6       | 0.5       |
| joy            | 0.980    | 0.709     | 0.559  | 0.625 | 0.619 | 161     | 0.5       |
| love           | 0.982    | 0.776     | 0.845  | 0.809 | 0.800 | 238     | 0.5       |
| nervousness    | 0.996    | 0.643     | 0.391  | 0.486 | 0.500 | 23      | 0.5       |
| optimism       | 0.976    | 0.721     | 0.500  | 0.590 | 0.589 | 186     | 0.5       |
| pride          | 0.998    | 0.750     | 0.375  | 0.500 | 0.529 | 16      | 0.5       |
| realization    | 0.974    | 0.576     | 0.131  | 0.213 | 0.266 | 145     | 0.5       |
| relief         | 0.998    | 1.000     | 0.091  | 0.167 | 0.301 | 11      | 0.5       |
| remorse        | 0.992    | 0.570     | 0.804  | 0.667 | 0.673 | 56      | 0.5       |
| sadness        | 0.979    | 0.684     | 0.500  | 0.578 | 0.575 | 156     | 0.5       |
| surprise       | 0.978    | 0.596     | 0.440  | 0.506 | 0.501 | 141     | 0.5       |
| neutral        | 0.798    | 0.733     | 0.609  | 0.666 | 0.528 | 1787    | 0.5       |


**Optimal Results**:

Using the best threshold for each label based on the training set (tuned on F1).


| Label          | Accuracy | Precision | Recall | F1    | MCC   | Support | Threshold |
| -------------- | -------- | --------- | ------ | ----- | ----- | ------- | --------- |
| **macro avg**  | 0.968    | 0.583     | 0.535  | 0.550 | 0.536 | 5427    | various   |
| admiration     | 0.944    | 0.680     | 0.758  | 0.717 | 0.687 | 504     | 0.39      |
| amusement      | 0.984    | 0.818     | 0.852  | 0.835 | 0.826 | 264     | 0.60      |
| anger          | 0.965    | 0.522     | 0.470  | 0.495 | 0.477 | 198     | 0.35      |
| annoyance      | 0.931    | 0.405     | 0.372  | 0.388 | 0.351 | 320     | 0.34      |
| approval       | 0.926    | 0.425     | 0.425  | 0.425 | 0.385 | 351     | 0.28      |
| caring         | 0.973    | 0.456     | 0.348  | 0.395 | 0.385 | 135     | 0.37      |
| confusion      | 0.972    | 0.500     | 0.451  | 0.474 | 0.460 | 153     | 0.39      |
| curiosity      | 0.949    | 0.511     | 0.680  | 0.583 | 0.563 | 284     | 0.40      |
| desire         | 0.986    | 0.571     | 0.434  | 0.493 | 0.491 | 83      | 0.35      |
| disappointment | 0.966    | 0.389     | 0.384  | 0.387 | 0.369 | 151     | 0.24      |
| disapproval    | 0.936    | 0.387     | 0.502  | 0.437 | 0.408 | 267     | 0.26      |
| disgust        | 0.979    | 0.550     | 0.488  | 0.517 | 0.508 | 123     | 0.32      |
| embarrassment  | 0.995    | 0.727     | 0.432  | 0.542 | 0.559 | 37      | 0.31      |
| excitement     | 0.980    | 0.457     | 0.417  | 0.437 | 0.427 | 103     | 0.30      |
| fear           | 0.991    | 0.675     | 0.718  | 0.696 | 0.691 | 78      | 0.45      |
| gratitude      | 0.990    | 0.952     | 0.898  | 0.924 | 0.919 | 352     | 0.56      |
| grief          | 0.999    | 0.667     | 0.333  | 0.444 | 0.471 | 6       | 0.14      |
| joy            | 0.978    | 0.627     | 0.615  | 0.621 | 0.609 | 161     | 0.37      |
| love           | 0.983    | 0.781     | 0.840  | 0.810 | 0.801 | 238     | 0.54      |
| nervousness    | 0.995    | 0.455     | 0.435  | 0.444 | 0.442 | 23      | 0.31      |
| optimism       | 0.974    | 0.630     | 0.559  | 0.593 | 0.580 | 186     | 0.32      |
| pride          | 0.998    | 0.750     | 0.375  | 0.500 | 0.529 | 16      | 0.27      |
| realization    | 0.968    | 0.347     | 0.234  | 0.280 | 0.269 | 145     | 0.20      |
| relief         | 0.998    | 0.625     | 0.455  | 0.526 | 0.532 | 11      | 0.20      |
| remorse        | 0.992    | 0.570     | 0.804  | 0.667 | 0.673 | 56      | 0.50      |
| sadness        | 0.977    | 0.612     | 0.545  | 0.576 | 0.565 | 156     | 0.40      |
| surprise       | 0.977    | 0.568     | 0.447  | 0.500 | 0.492 | 141     | 0.46      |
| neutral        | 0.791    | 0.671     | 0.718  | 0.694 | 0.537 | 1787    | 0.40      |

Confusion matrix:

![banner](https://huggingface.co/cirimus/modernbert-base-go-emotions/resolve/main/confusion_matrix_test.png)


---


### Limitations and Biases

- **Data Bias**: The dataset is based on Reddit comments, which may not generalize well to other domains or cultural contexts.
- **Underrepresented Classes**: Certain labels like "grief" and "relief" have very few examples, leading to lower performance for those classes.
- **Ambiguity**: Some training data contain annotation inconsistencies or ambiguities that may impact predictions.

---

---

### Environmental Impact

- **Hardware Used**: NVIDIA RTX4090
- **Training Time**: <1 hour
- **Carbon Emissions**: ~0.04 kg CO2 (calculated via [ML CO2 Impact Calculator](https://mlco2.github.io/impact)).

---

### Citation

If you use this model, please cite it as follows:

```bibtex
@inproceedings{JdFE2025b,
  title = {Emotion Detection with ModernBERT},
  author = {Enric Junqu\'e de Fortuny},
  year = {2025},
  howpublished = {\url{https://huggingface.co/cirimus/modernbert-base-go-emotions}},
}
```

